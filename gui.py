import os
import time

import pygame

from config import BOARD_SIZE

WIDTH = 1050
HEIGHT = 800
ART_DIR = os.path.join(os.path.dirname(__file__), "ART")   # mettre knight.png ici
BOARD_IMAGE_PATH = os.path.join(ART_DIR, "board.jpg")
BOARD_IMAGE = None
BOARD_IMAGE_SIZE = None
BOARD_RATIO = 0.797
BOARD_OFFSET = 0.102

# Couleurs suggérées (à ajuster selon la Figure 2)
LIGHT_SQUARE = (238, 238, 210)
DARK_SQUARE = (118, 150, 86)
VISITED_LIGHT = (214, 224, 127)
VISITED_DARK = (160, 190, 70)
TEXT = (60, 70, 50)


def load_knight_image(tile):
    image_path = os.path.join(ART_DIR, "knight.png")
    if not os.path.exists(image_path):
        return None

    image = pygame.image.load(image_path).convert_alpha()
    return pygame.transform.smoothscale(image, (tile, tile))


def draw_board(screen, path, step, tile, ox, oy, font, knight_img):
    global BOARD_IMAGE, BOARD_IMAGE_SIZE

    board_image_size = int(tile * BOARD_SIZE / BOARD_RATIO)

    if BOARD_IMAGE is None or BOARD_IMAGE_SIZE != board_image_size:
        image = pygame.image.load(BOARD_IMAGE_PATH).convert()
        BOARD_IMAGE = pygame.transform.smoothscale(
            image, (board_image_size, board_image_size)
        )
        BOARD_IMAGE_SIZE = board_image_size

    screen.blit(BOARD_IMAGE, (ox, oy))

    board_left = ox + int(board_image_size * BOARD_OFFSET)
    board_top = oy + int(board_image_size * BOARD_OFFSET)
    current_step = min(step, len(path) - 1)
    visited_overlay = pygame.Surface((tile, tile), pygame.SRCALPHA)
    visited_overlay.fill((80, 190, 80, 110))

    for index in range(current_step + 1):
        x, y = path[index]
        cell = pygame.Rect(board_left + x * tile, board_top + y * tile,
                           tile, tile)
        screen.blit(visited_overlay, cell.topleft)
        number = font.render(str(index + 1), True, TEXT)
        number_rect = number.get_rect(center=cell.center)
        screen.blit(number, number_rect)

    if knight_img is not None:
        x, y = path[current_step]
        cell = pygame.Rect(board_left + x * tile, board_top + y * tile,
                           tile, tile)
        knight_rect = knight_img.get_rect(center=cell.center)
        screen.blit(knight_img, knight_rect)


def show_solution(path, generation=0, fitness=0, elapsed=0.0, delay_ms=300):
    if not path:
        raise ValueError("path cannot be empty")

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Knight's Tour")

    tile = 70
    board_x = 20
    board_y = 20
    font = pygame.font.SysFont(None, 24)
    info_font = pygame.font.SysFont(None, 30)
    knight_img = load_knight_image(tile)
    clock = pygame.time.Clock()

    step = 0
    next_step_time = pygame.time.get_ticks() + delay_ms
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    step = 0
                    next_step_time = pygame.time.get_ticks() + delay_ms

        now = pygame.time.get_ticks()
        if step < len(path) - 1 and now >= next_step_time:
            step += 1
            next_step_time = now + delay_ms

        screen.fill((45, 35, 30))
        draw_board(screen, path, step, tile, board_x, board_y, font, knight_img)

        info_x = 770
        screen.blit(info_font.render("Knight's Tour", True, (255, 255, 255)),
                    (info_x, 100))
        screen.blit(info_font.render("Generation: " + str(generation),
                                     True, (255, 255, 255)), (info_x, 160))
        screen.blit(info_font.render("Fitness: " + str(fitness),
                                     True, (255, 255, 255)), (info_x, 205))
        screen.blit(info_font.render("Time: " + str(round(elapsed, 2)) + " s",
                                     True, (255, 255, 255)), (info_x, 250))
        screen.blit(font.render("R: replay    ESC: quit", True, (255, 255, 255)),
                    (info_x, 320))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
