import re
from functools import reduce
from operator import mul, add

corrupted_instruction = reduce(add, open("./Day03/input.txt").readlines())
real_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_instruction)

print(sum(reduce(mul, map(int, instr[4:-1].split(","))) for instr in real_instructions))

# test_input => 161
# input => 168539636
