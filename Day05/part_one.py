from collections import defaultdict

with open("./Day05/input.txt") as f:
    rules_over = False
    rules = defaultdict(lambda: [])
    updates = []
    while True:
        line = f.readline().strip()
        if not rules_over:
            if not line:
                rules_over = True
                continue
            parsed_rule = list(map(int, line.split("|")))
            rules[parsed_rule[0]].append(parsed_rule[1])
            continue

        if not line:
            break

        updates.append(list(map(int, line.split(","))))


def in_correct_order(update):
    for i, page in enumerate(update):
        if not all(
            [x in rules[page] for x in update[i + 1 :]]
        ):  # this assumes that every page does have an ordering rule
            return False

    return True


answer = 0
for update in updates:
    if in_correct_order(update):
        # print(update)
        answer += update[len(update) // 2]

print(answer)

# test_input => 143
# input => 4996
