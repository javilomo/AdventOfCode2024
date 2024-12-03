import re
def isCorrupted():
    with open(r'C:\Users\javier.lopez.morale\Documents\GitHub\AdventOfCode2024\03\input_03.txt', 'r') as input3:
        text = input3.read()
        total_sum = 0
        enabled = True

        instructions = re.findall(r"(mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\))", text)

        for inst in instructions:
            if inst == "do()":
                enabled = True
            elif inst == "don't()":
                enabled = False
            elif enabled:
                match = re.match(r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)", inst)
                if match:
                    x, y = map(int, match.groups())
                    total_sum += x * y

        return total_sum


print(isCorrupted())

