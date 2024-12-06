def check_safety_of_level(level: list[int]) -> bool:
    # this assumes that the list is longer than length 2
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


safe_reports = 0
with open("./Day02/input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break

        level = list(map(int, line.split()))
        if check_safety_of_level(level):
            safe_reports += 1

print(safe_reports)

# test_input => 2
# input => 660
