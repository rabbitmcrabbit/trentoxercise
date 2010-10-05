# -*- coding: utf-8 -*-
import set

def get_row(grid, nr):
    return grid[nr]

def get_column(grid,nr):
    return [x[nr] for x in grid]

def get_box(grid,nr):
    col_idx = [x + (nr%3)*3 for x in range(3)]
    row_idx = [y + (nr/3)*3 for y in range(3)]
    return [grid[y][x] for y in row_idx for x in col_idx]

def is_solution(grid):
    set9 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(9):
        if (set(get_row(grid, i)) != set9) || 
           (set(get_column(grid, i)) != set9) || 
           (set(get_box(grid, i)) != set9):
            return False
    return True
    