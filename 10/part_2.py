from statistics import median

brackets_values = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

brackets = {
    "<": ">",
    "{": "}",
    "[": "]",
    "(": ")",
}

def delete_pairs(line: str):
    for pattern in ["()", "[]", "{}", "<>"]:
        line = line.replace(pattern, "")
    return line


with open("10/input.txt") as file:
    data = file.read().splitlines()

result = []

for line in data:
    current_length = len(line)
    should_continue = True
    while should_continue:
        line = delete_pairs(line)
        new_length = len(line)
        if new_length == current_length:
            should_continue = False
        current_length = new_length
    closing_characters = [char for char in line if char in brackets_values]
    if closing_characters:
        continue

    line_score = 0
    for open_char in reversed(line):
        line_score = line_score * 5 + brackets_values[brackets[open_char]]
    result.append(line_score)




print(median(result))

