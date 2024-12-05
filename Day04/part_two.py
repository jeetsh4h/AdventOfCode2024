import numpy as np

search_grid = np.array(
    [list(row.strip()) for row in open("./Day04/input.txt").readlines()]
)

# from pprint import pprint; pprint(search_grid)
n_rows, n_cols = search_grid.shape
word_to_find = "MAS"

count = 0
for i in range(n_rows):
    for j in range(n_cols):
        diag_mat = search_grid[i : i + 3, j : j + 3]
        left_to_right_diag = "".join(np.diag(diag_mat))
        right_to_left_diag = "".join(np.diag(np.fliplr(diag_mat)))

        if (
            left_to_right_diag == right_to_left_diag
            or left_to_right_diag[::-1] == right_to_left_diag
        ):
            if left_to_right_diag == word_to_find:
                count += 1
            if left_to_right_diag[::-1] == word_to_find:
                count += 1

print(count)

# test_input => 9
# input => 18
