with open("./Day01/input.txt") as f:
    lines = f.readlines()

# could probably insert the elements sorted here, for optimisation
list1, list2 = [], []
for line in lines:
    elements = line.split()
    list1.append(int(elements[0]))
    list2.append(int(elements[1]))

print(sum(abs(x - y) for x, y in zip(sorted(list1), sorted(list2))))

# test_input => 11
# input => 2769675
