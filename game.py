import pygame
from items import load_items
from sprites.player import Player
from levels import level1, level2
TILE_SIZE = 40

#800x600

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/working-bg.png").convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, self.screen.get_size())
        
        self.overlay_image = pygame.image.load("assets/images/outer-bg-png.png").convert_alpha()
        self.overlay_image = pygame.transform.scale(self.overlay_image, self.screen.get_size())

        self.levels={
            "level1": level1,
            "level2": level2,
        }
        self.items = load_items()
        self.current_level="level1"
        self.player = Player(0, 0, self.levels[self.current_level])
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.interaction_text = None
        self.show_more_text = False
        self.button_rect = pygame.Rect(0, 0, 120, 40)
        

    #ADDED to change level
    def switch_level(self, new_level_name):
        self.current_level = new_level_name
        self.player.rect.topleft = (0, 0)
        self.interaction_text = None
        self.show_more_text = False

    def handle_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    tile = self.levels[self.current_level].get_tile_at_pixel(
                        self.player.rect.centerx,
                        self.player.rect.centery
                    )
                    if tile == "C":
                        self.interaction_text = "You found a treasure chest!"
                        self.show_more_text = False  # Reset button state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left-click
                    if self.button_rect.collidepoint(event.pos):
                        self.show_more_text = True

    def update(self):
        self.player.update()

        # Check teleport level
        tile = self.levels[self.current_level].get_tile_at_pixel(
            self.player.rect.centerx,
            self.player.rect.centery
        )
        if tile == "T":
            if self.current_level == "level1":
                self.switch_level("level2")
            else:
                self.switch_level("level1")
        player_tile = (self.player.rect.centerx // 40, self.player.rect.centery // 40)
        for item in self.items:
            item.try_pickup(player_tile)


    def draw(self,screen):
        screen.blit(self.background_image,(0,0))
        screen.blit(self.overlay_image, (0, 0))
        self.levels[self.current_level].draw_level(self.screen)
        self.player_group.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)

        if self.interaction_text:
            modal_width = 500
            modal_height = 400
            modal_x = (self.screen.get_width() - modal_width) // 2
            modal_y = 30

            modal_surface = pygame.Surface((modal_width, modal_height), pygame.SRCALPHA)
            pygame.draw.rect(modal_surface, (30, 30, 30, 240), modal_surface.get_rect(), border_radius=10)

            font_title = pygame.font.SysFont(None, 40, bold=True)
            title_surf = font_title.render("Computer Interaction", True, (255, 215, 0))
            modal_surface.blit(title_surf, (20, 10))

            font_body = pygame.font.SysFont(None, 28)
            base_text = self.interaction_text
            if self.show_more_text:
                base_text += "\n It's full of mysterious glowing code and secret files..."

            lines = self.wrap_text(base_text, font_body, modal_width - 40)
            y_offset = 60
            for line in lines:
                text_surf = font_body.render(line, True, (255, 255, 255))
                modal_surface.blit(text_surf, (20, y_offset))
                y_offset += text_surf.get_height() + 4

            # Draw button
            button_width = 120
            button_height = 40
            button_x = modal_width - button_width - 200
            button_y = modal_height - button_height - 10
            self.button_rect = pygame.Rect(modal_x + button_x, modal_y + button_y, button_width, button_height)

            pygame.draw.rect(self.screen, (70, 70, 200), self.button_rect, border_radius=8)
            button_font = pygame.font.SysFont(None, 26)
            button_text = "Show More" if not self.show_more_text else "Thanks!"
            btn_text_surf = button_font.render(button_text, True, (255, 255, 255))
            self.screen.blit(btn_text_surf, btn_text_surf.get_rect(center=self.button_rect.center))

            # Blit modal
            self.screen.blit(modal_surface, (modal_x, modal_y))

        ##inventory hud
        hud_width=90
        hud_height=270
        padding=2
        item_size=20
        #hud_x=self.screen.get_width()-hud_width-padding
        #hud_y=self.screen.get_height() -hud_height-padding
        hud_x=30
        hud_y=300
        #hud background
        pygame.draw.rect(self.screen,(0,0,0),(hud_x,hud_y,hud_width,hud_height))
        #hud border
        pygame.draw.rect(self.screen, (60,191, 253), (hud_x, hud_y, hud_width, hud_height), width=2)

        font = pygame.font.SysFont(None, 24)
        title = font.render("Inventory", True, (255, 255, 255))
        self.screen.blit(title, (hud_x + 10, hud_y + 10))

        # Draw items in a 4x3 grid
        x_offset = hud_x + 10
        y_offset = hud_y + 40
        columns = 2

        for index, item in enumerate(self.items):
            col = index % columns
            row = index // columns
            slot_x = x_offset + col * (item_size + 10)
            slot_y = y_offset + row * (item_size + 10)
            slot_rect = pygame.Rect(slot_x, slot_y, item_size, item_size)

            # Draw item slot background
            pygame.draw.rect(self.screen, (40, 40, 40), (slot_x, slot_y, item_size, item_size), border_radius=4)

            # If collected, draw the item image
            if item.collected:
                img = pygame.transform.scale(item.surface, (item_size, item_size))
                self.screen.blit(img, (slot_x, slot_y))
            else:
                # Draw a placeholder "locked" slot (X icon)
                pygame.draw.line(self.screen, (120, 120, 120), (slot_x, slot_y), (slot_x + item_size, slot_y + item_size), 2)
                pygame.draw.line(self.screen, (120, 120, 120), (slot_x + item_size, slot_y), (slot_x, slot_y + item_size), 2)
            mouse_pos = pygame.mouse.get_pos()
            
            if slot_rect.collidepoint(mouse_pos):
                font = pygame.font.SysFont(None, 20)
                tooltip_text = font.render(item.name, True, (255, 255, 255))
                tooltip_bg = pygame.Surface((tooltip_text.get_width() + 10, tooltip_text.get_height() + 6))
                tooltip_bg.fill((0, 0, 0))
                tooltip_bg.blit(tooltip_text, (5, 3))

                # Draw tooltip near mouse
                tooltip_x = mouse_pos[0] + 12
                tooltip_y = mouse_pos[1] + 12
                self.screen.blit(tooltip_bg, (tooltip_x, tooltip_y))
        pygame.display.flip()


    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
        return lines
