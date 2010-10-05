# -*- coding: utf-8 -*-

def get_row(grid, nr):
    return grid[nr]

def get_column(grid,nr):
    return [x[nr] for x in grid]

def get_box(grid,nr):
    col_idx = [x + (nr%3)*3 for x in range(3)]
    row_idx = [y + (nr/3)*3 for y in range(3)]
    return [grid[y][x] for y in row_idx for x in col_idx]
    
def is_block_solved(block):
    set9 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    return set(block) == set9
    
def is_block_valid(block):
    s = set(block)
    l = [x for x in block if (x > 0 and x <= 9)]
    muddyStick = [x for x in block if x > 9 or x < 0]
    if muddyStick:
        return False
    return len(set(l)) == len(l)

def is_solution(grid):
    for i in range(9):
        if (not is_block_solved(get_row(grid, i))) or \
           (not is_block_solved(get_column(grid, i))) or \
           (not is_block_solved(get_box(grid, i))):
                return False
    return True
    
def is_valid_but_maybe_incomplete(grid):
    for i in range(9):
        if (not is_block_valid(get_row(grid, i))) or \
           (not is_block_valid(get_column(grid, i))) or \
           (not is_block_valid(get_box(grid, i))):
                return False
    return True

def get_value(grid, index):
    x = index % 9
    y = index / 9
    return grid[y][x]

def set_value(grid, index, value)
    x = index % 9
    y = index / 9
    grid[y][x] = value
