import cv2
import mediapipe as mp
import pygame
import sys
import math

class Button:
    def __init__(self, pos, text, size=(85, 85)):
        self.pos = pos
        self.size = size
        self.text = text
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self, screen, font, color, hover_color, is_hovered):
        current_color = hover_color if is_hovered else color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        
        text_surf = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

def main():
    pygame.init()
    
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("AI Dynamic Virtual Keyboard")
    clock = pygame.time.Clock()

    cap = cv2.VideoCapture(0)
    cap.set(3, screen_width)
    cap.set(4, screen_height)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    key_layout = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]
    
    button_list = []
    start_x, start_y = 100, 100
    key_gap = 10
    key_size = 85
    
    for row_idx, row in enumerate(key_layout):
        for col_idx, key in enumerate(row):
            x = start_x + col_idx * (key_size + key_gap) + (row_idx * key_size // 2)
            y = start_y + row_idx * (key_size + key_gap)
            button_list.append(Button((x, y), key, (key_size, key_size)))

    font = pygame.font.SysFont("Arial", 50)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False

        success, frame = cap.read()
        if not success:
            continue
            
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

        frame_rgb_for_pygame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pygame_frame = pygame.surfarray.make_surface(frame_rgb_for_pygame.swapaxes(0, 1))
        
        screen.blit(pygame_frame, (0, 0))
        
        for button in button_list:
            button.draw(screen, font, (50, 50, 50), (100, 100, 100), False)
            
        pygame.display.flip()
        clock.tick(60)

    cap.release()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()