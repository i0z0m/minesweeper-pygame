import pygame
# マインスイーパーの本家デザインに近づけるためのコード

# ゲームの設定
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 10, 10  # セルの数を減らす
CELL_SIZE = WIDTH // COLS

# 色の定義
WHITE = (255, 255, 255)
LIGHT_GRAY = (192, 192, 192)  # セルの色を明るいグレーに
DARK_GRAY = (128, 128, 128)
RED = (255, 0, 0)

def draw_grid(screen, cell_size):
    """グリッドを描画する関数"""
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, LIGHT_GRAY, (col * cell_size, row * cell_size, cell_size, cell_size), 0)  # セルの背景を塗りつぶす
            pygame.draw.rect(screen, DARK_GRAY, (col * cell_size, row * cell_size, cell_size, cell_size), 1)  # 境界線を描画

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

        # マウスオーバーのセルを赤色で表示
        mouse_pos = pygame.mouse.get_pos()
        mouse_row = mouse_pos[1] // CELL_SIZE
        mouse_col = mouse_pos[0] // CELL_SIZE
        pygame.draw.rect(screen, RED, (mouse_col * CELL_SIZE, mouse_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
