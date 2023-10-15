import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
ISOMETRIC_WIDTH = TILE_SIZE * 2
ISOMETRIC_HEIGHT = TILE_SIZE

# Colors
SAND = (255, 223, 186)
GRASS = (124, 252, 0)
WATER = (0, 191, 255)
ICE = (240, 255, 255)
BLACK = (0, 0, 0)

# Create screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Isometric Tilemap Demo")
clock = pygame.time.Clock()

# Sample tilemap (2D array)
tilemap = [
    ['grass', 'sand', 'water', 'ice'],
    ['sand', 'water', 'ice', 'grass'],
    ['water', 'ice', 'grass', 'sand'],
    ['ice', 'grass', 'sand', 'water']
]

def draw_tile(x, y, terrain):
    colors = {
        'sand': SAND,
        'grass': GRASS,
        'water': WATER,
        'ice': ICE
    }

    # Convert cartesian coordinates to isometric
    iso_x = x - y
    iso_y = (x + y) / 2

    # Adjusting for screen center and scaling tile size
    screen_x = WIDTH // 2 + iso_x * ISOMETRIC_WIDTH // 2
    screen_y = HEIGHT // 4 + iso_y * ISOMETRIC_HEIGHT

    pygame.draw.polygon(screen, colors[terrain], [
        (screen_x, screen_y),
        (screen_x + ISOMETRIC_WIDTH // 2, screen_y + ISOMETRIC_HEIGHT // 2),
        (screen_x, screen_y + ISOMETRIC_HEIGHT),
        (screen_x - ISOMETRIC_WIDTH // 2, screen_y + ISOMETRIC_HEIGHT // 2)
    ])

    # Draw grid overlay
    pygame.draw.lines(screen, BLACK, True, [
        (screen_x, screen_y),
        (screen_x + ISOMETRIC_WIDTH // 2, screen_y + ISOMETRIC_HEIGHT // 2),
        (screen_x, screen_y + ISOMETRIC_HEIGHT),
        (screen_x - ISOMETRIC_WIDTH // 2, screen_y + ISOMETRIC_HEIGHT // 2)
    ])

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((220, 220, 220))

        for row in range(len(tilemap)):
            for col in range(len(tilemap[row])):
                draw_tile(col, row, tilemap[row][col])

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
