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
    if not in_correct_order(update):
        correct_update = update.copy()
        for i, page in enumerate(correct_update):
            for j in range(0, i):
                if correct_update[j] in rules[page]:
                    correct_update[i], correct_update[j] = (
                        correct_update[j],
                        correct_update[i],
                    )  # swap

        # print(correct_update)
        answer += correct_update[len(correct_update) // 2]

print(answer)

# test_input => 123
# input => 6311
