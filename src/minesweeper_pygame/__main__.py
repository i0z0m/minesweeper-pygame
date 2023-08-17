import pygame

# ゲームの設定
WIDTH = 400
HEIGHT = 400
ROWS = 20
COLS = 20
CELL_SIZE = WIDTH // COLS

# 色の定義
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# 初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# ゲームループ
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリック
                x, y = event.pos
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                print(f"Clicked cell: ({row}, {col})")

    screen.fill(WHITE)

    # グリッドを描画
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    # クリックされたセルを赤色で塗りつぶす
    mouse_pos = pygame.mouse.get_pos()
    mouse_row = mouse_pos[1] // CELL_SIZE
    mouse_col = mouse_pos[0] // CELL_SIZE
    rect = pygame.Rect(
        mouse_col * CELL_SIZE, mouse_row * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, RED, rect)

    pygame.display.flip()

pygame.quit()

