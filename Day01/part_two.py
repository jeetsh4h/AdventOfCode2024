from collections import defaultdict

with open("./Day01/input.txt") as f:
    lines = f.readlines()

# element1: frequency_in_list1
frequency1 = defaultdict(lambda: 0)
frequency2 = defaultdict(lambda: 0)

for line in lines:
    elements = line.split()
    frequency1[int(elements[0])] += 1
    frequency2[int(elements[1])] += 1

answer = 0
for k, v in frequency1.items():
    answer += (k * frequency2[k]) * v

print(answer)

# test_input => 31
# input => 24643097
