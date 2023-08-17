import pygame

# ゲームの設定
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS

# 色の定義
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

def draw_grid(screen, cell_size):
    """グリッドを描画する関数"""
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, GRAY, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()

    # ゲームループ
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen, CELL_SIZE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()