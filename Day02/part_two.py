def check_safety_of_level(level: list[int]) -> bool:
    increasing = True
    if level[1] - level[0] < 0:
        increasing = False

    for index in range(len(level) - 1):
        difference = level[index + 1] - level[index]
        if difference == 0:
            return False

        if (difference < 0) == increasing:
            return False

        if abs(difference) > 3:
            return False

    return True


def check_safety_with_one_removed(level: list[int]) -> bool:
    if check_safety_of_level(level):
        return True

    for index in range(len(level) - 1):
        dampened_level = level[:index] + level[index + 1 :]
        if check_safety_of_level(dampened_level):
            return True

    # last index case
    return check_safety_of_level(level[:-1])


safe_reports = 0
with open("./Day02/input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break

        level = list(map(int, line.split()))
        if check_safety_with_one_removed(level):
            safe_reports += 1

print(safe_reports)

# test_input => 4
# input => 689
