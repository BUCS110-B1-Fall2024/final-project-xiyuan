import pygame
from pygame.locals import *
from src.camera import Camera
from src.gallery import Gallery
from src.environment import Environment
from src.photo import Photo
import time
import os


class Controller:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Fullscreen mode
        self.screen_width = 1920  # Fullscreen width (example for 16:9 aspect ratio)
        self.screen_height = 1080  # Fullscreen height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Virtual World Photography")
        
        # Font and instructions
        self.font = pygame.font.Font(None, 36)
        self.show_instructions_flag = True
        self.instructions = [
            "1. Use Arrow Keys/WASD to move the camera.",
            "2. Press Spacebar to take a photo.",
            "3. Press P to pause/unpause the game.",
            "4. Press ESC to quit.",
            "5. Use + or - to zoom in or out."
        ]

        # Load the 360-degree background
        self.background = pygame.image.load("assets/nyc.jpg").convert()
        self.bg_width, self.bg_height = self.background.get_size()

        # Initialize camera
        self.camera = Camera(0, 0)
        
        # Game states
        self.running = True
        self.game_state = "start"  # Possible states: "start", "active", "pause", "game_over"
        self.clock = pygame.time.Clock()
        
        # To store captured screenshots
        self.screenshot_folder = "screenshots"
        if not os.path.exists(self.screenshot_folder):
            os.makedirs(self.screenshot_folder)
        
        # Zoom and drag variables
        self.zoom_level = 1.0  # Initial zoom level (1.0 is normal size)
        self.offset_x = 0  # Initial horizontal offset for dragging
        self.offset_y = 0  # Initial vertical offset for dragging
        self.dragging = False
        self.mouse_x = 0
        self.mouse_y = 0

    def handle_events(self):
        """Handles user input and updates the game state."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Quit the game if the window is closed

            if event.type == pygame.KEYDOWN:
                if self.game_state == "start" and event.key == pygame.K_RETURN:
                    self.game_state = "active"  # Start the game
                elif self.game_state == "active":
                    if event.key == pygame.K_p:  # Pause the game
                        self.toggle_pause()
                    elif event.key == pygame.K_SPACE:  # Take a photo
                        self.take_photo()
                if event.key == pygame.K_ESCAPE:  # Quit the game
                    self.running = False
                elif event.key == pygame.K_EQUALS:  # Zoom in (increase zoom level)
                    self.zoom_level += 0.1
                elif event.key == pygame.K_MINUS:  # Zoom out (decrease zoom level)
                    self.zoom_level = max(0.1, self.zoom_level - 0.1)  # Don't go below zoom level of 0.1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse click
                    if event.button == 1:  # Start dragging on left click
                        self.dragging = True
                        self.mouse_x, self.mouse_y = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Stop dragging on left click release
                    self.dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    dx = event.pos[0] - self.mouse_x
                    dy = event.pos[1] - self.mouse_y
                    self.offset_x += dx
                    self.offset_y += dy
                    self.mouse_x, self.mouse_y = event.pos

    def toggle_pause(self):
        """Toggle between active and pause states."""
        if self.game_state == "active":
            self.game_state = "pause"
        elif self.game_state == "pause":
            self.game_state = "active"

    def take_photo(self):
        """Capture a "photo" of the screen and save it."""
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(self.screenshot_folder, f"photo_{timestamp}.png")
        pygame.image.save(self.screen, filename)
        print(f"Photo saved as {filename}")

    def draw_background(self):
        # Calculate the scaled width and height based on zoom level
        scaled_bg_width = int(self.bg_width * self.zoom_level)
        scaled_bg_height = int(self.bg_height * self.zoom_level)

        # Draw the background with the zoom and drag offsets
        scaled_bg = pygame.transform.scale(self.background, (scaled_bg_width, scaled_bg_height))
        
        # Calculate the horizontal and vertical offsets for the panoramic background
        offset_x = (self.camera.x * self.zoom_level + self.offset_x) % scaled_bg_width
        offset_y = (self.camera.y * self.zoom_level + self.offset_y) % scaled_bg_height

        # Draw only the part inside the focus frame
        frame_width = 1600  # Adjust for full screen
        frame_height = int(frame_width * 9 / 16)
        frame_rect = pygame.Rect(self.screen_width // 2 - frame_width // 2,
                                 self.screen_height // 2 - frame_height // 2,
                                 frame_width, frame_height)

        # Draw the black background for everything else
        self.screen.fill((0, 0, 0))

        # Draw the section of the background inside the frame
        self.screen.blit(scaled_bg, (-offset_x, -offset_y), (frame_rect.left, frame_rect.top, frame_width, frame_height))
        
        # Handle seamless wrapping for background
        if offset_x > 0:
            self.screen.blit(scaled_bg, (scaled_bg_width - offset_x, -offset_y), (frame_rect.left, frame_rect.top, frame_width, frame_height))
        if offset_y > 0:
            self.screen.blit(scaled_bg, (-offset_x, scaled_bg_height - offset_y), (frame_rect.left, frame_rect.top, frame_width, frame_height))

    def draw_center_rectangle(self):
        """Draw a small red rectangle in the center."""
        rect_width = 50
        rect_height = 30
        center_rect = pygame.Rect(self.screen_width // 2 - rect_width // 2,
                                  self.screen_height // 2 - rect_height // 2, rect_width, rect_height)
        pygame.draw.rect(self.screen, (255, 0, 0), center_rect, 3)  # Red rectangle, no fill color

    def redraw(self):
        # Redraw the game
        if self.game_state == "start":
            # Fill the screen with black
            self.screen.fill((0, 0, 0))
            # Display instructions
            y_offset = 100
            for line in self.instructions:
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (50, y_offset))
                y_offset += 50
            press_enter = self.font.render("Press Enter to Start", True, (255, 255, 0))
            self.screen.blit(press_enter, (250, 400))

        elif self.game_state == "active":
            # Draw the panoramic background inside the frame
            self.draw_background()

            # Draw the red center rectangle
            self.draw_center_rectangle()

    def run(self):
        """Start the game loop."""
        while self.running:
            self.handle_events()
            self.redraw()
            pygame.display.flip()
            self.clock.tick(60)  # Limit to 60 frames per second
        pygame.quit()