import re
from operator import add
from functools import reduce

corrupted_instruction = reduce(add, open("./Day03/input.txt").readlines())
real_instructions = re.findall(
    r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", corrupted_instruction
)

answer = 0
active = True
for instr in real_instructions:
    if instr == "do()":
        active = True
        continue

    if instr == "don't()":
        active = False
        continue

    if active:
        parsed_args = instr[4:-1].split(",")
        answer += int(parsed_args[0]) * int(parsed_args[1])

print(answer)

# test_input => 48
# input => 97529391
