import pygame
import random
from typing import List

# マインスイーパーの本家デザインに近づけるためのコード

# ゲームの設定
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 10, 10  # セルの数を減らす
CELL_SIZE = WIDTH // COLS

# 爆弾と旗の記号定義
BOMB_SYMBOL = 'X'
FLAG_SYMBOL = 'F'

# 色の定義
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0,0,0)

# 数字の色の定義
NUMBER_COLORS = {
    1: (0, 0, 255),   # 青
    2: (0, 128, 0),   # 緑
    3: (255, 0, 0),   # 赤
    4: (128, 0, 128), # 紫
    5: (139, 69, 19), # 茶色
    6: (0, 255, 255)  # シアン
}

# マインスイーパーのゲームロジックを追加したコード

# ゲームの設定
MINE_COUNT = 10

# セルのクラス
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_open = False
        self.is_flagged = False
        self.number = 0


def init_grid(rows: int, cols: int, mine_count: int) -> List[List[Cell]]:
    """グリッドを初期化する関数"""
    grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mine_count)
    for pos in mine_positions:
        row = pos // cols
        col = pos % cols
        grid[row][col].is_mine = True
        # 周囲のセルの数字を計算
        for r in range(max(row-1, 0), min(row+1, rows-1) + 1):
            for c in range(max(col-1, 0), min(col+1, cols-1) + 1):
                grid[r][c].number += 1
    return grid



def draw_grid(screen, grid, cell_size):
    """グリッドを描画する関数"""
    font = pygame.font.Font(None, 36)  # フォントの設定
    for row in range(ROWS):
        for col in range(COLS):
            cell = grid[row][col]
            color = LIGHT_GRAY if cell.is_open else DARK_GRAY
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size), 0)
            pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
            if cell.is_open:
                if cell.is_mine:
                    text = BOMB_SYMBOL
                    text_color = BLACK
                else:
                    text = str(cell.number) if cell.number > 0 else ""
                    text_color = NUMBER_COLORS.get(cell.number, BLACK)
                text_surface = font.render(text, True, text_color)
                text_rect = text_surface.get_rect(center=(col * cell_size + cell_size//2, row * cell_size + cell_size//2))
                screen.blit(text_surface, text_rect)
            elif cell.is_flagged:
                text_surface = font.render(FLAG_SYMBOL, True, RED)
                text_rect = text_surface.get_rect(center=(col * cell_size + cell_size//2, row * cell_size + cell_size//2))
                screen.blit(text_surface, text_rect)

def reveal_adjacent_cells(row, col, grid):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col].is_open:
        return
    grid[row][col].is_open = True
    if grid[row][col].number == 0:
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                reveal_adjacent_cells(r, c, grid)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper")
    clock = pygame.time.Clock()

    grid = init_grid(ROWS, COLS, MINE_COUNT)

    # ゲームループ
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen, grid, CELL_SIZE)

        # マウスオーバーのセルを赤色で表示
        mouse_pos = pygame.mouse.get_pos()
        mouse_row = mouse_pos[1] // CELL_SIZE
        mouse_col = mouse_pos[0] // CELL_SIZE
        pygame.draw.rect(screen, RED, (mouse_col * CELL_SIZE, mouse_row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE
                cell = grid[row][col]
                if event.button == 1 and not cell.is_flagged:  # 左クリックでセルを開く
                    reveal_adjacent_cells(row, col, grid)
                elif event.button == 3:  # 右クリックで旗を立てる/取り除く
                    cell.is_flagged = not cell.is_flagged
        
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
