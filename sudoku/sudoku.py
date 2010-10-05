# -*- coding: utf-8 -*-
def get_row(grid, nr):
    return grid[nr]

def get_column(grid,nr):
    return [x[nr] for x in grid]

def get_box(grid,nr):
    col_idx = [x + (nr%3)*3 for x in range(3)]
    row_idx = [y + (nr/3)*3 for y in range(3)]
    return [grid[y][x] for y in row_idx for x in col_idx]
    