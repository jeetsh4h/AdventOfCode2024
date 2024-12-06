import numpy as np

search_grid = np.array(
    [list(row.strip()) for row in open("./Day04/input.txt").readlines()]
)

# from pprint import pprint; pprint(search_grid)
n_rows, n_cols = search_grid.shape
word_to_find = "XMAS"

count = 0
for i in range(n_rows):
    for j in range(n_cols):
        horizontal_word = "".join(search_grid[i, j : j + 4])
        if horizontal_word == word_to_find:
            count += 1
        if horizontal_word[::-1] == word_to_find:
            count += 1

        vertical_word = "".join(search_grid[i : i + 4, j])
        if vertical_word == word_to_find:
            count += 1
        if vertical_word[::-1] == word_to_find:
            count += 1

        diag_mat = search_grid[i : i + 4, j : j + 4]
        left_to_right_diag = "".join(np.diag(diag_mat))
        if left_to_right_diag == word_to_find:
            count += 1
        if left_to_right_diag[::-1] == word_to_find:
            count += 1

        right_to_left_diag = "".join(np.diag(np.fliplr(diag_mat)))
        if right_to_left_diag == word_to_find:
            count += 1
        if right_to_left_diag[::-1] == word_to_find:
            count += 1

print(count)

# test_input => 18
# input => 18
