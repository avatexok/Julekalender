import pygame

pygame.init()

# Hvor stort vinduet skal være
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# for skjermen og display på vinduet
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Julekalender")

# game variables
tile_size = 150

# farger
bakgrunn = (255, 255, 255)
svart = (0, 0 ,0)

# font

font = pygame.font.Font(None, 50)

# functions

def draw_grid(tile_size):
    screen.fill(bakgrunn)

    # Passe på at tallene går opp riktig

    number = 1

    rows = SCREEN_HEIGHT // tile_size
    cols = SCREEN_WIDTH // tile_size

    for row in range(rows):
        for col in range(cols):
            # kalkulere størrelse av hver tile
            x = col * tile_size
            y = row * tile_size
            rect = pygame.Rect(x, y, tile_size, tile_size)

            # tallene
            if number <= 24: # siden jeg har 24 tiles
                text = font.render(str(number), True, svart)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
                number += 1

    # vertikale linjer
    for x in range(tile_size, SCREEN_WIDTH, tile_size):
        pygame.draw.line(screen, svart, (x, 0), (x, SCREEN_HEIGHT))
    # horistontale linjer
    for y in range(tile_size, SCREEN_HEIGHT, tile_size):
        pygame.draw.line(screen, svart, (0, y), (SCREEN_WIDTH, y))


# selve spillet
run = True
while run:

    draw_grid(tile_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()