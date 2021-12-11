from dataclasses import dataclass

# @dataclass
# class BracketType:
#     opening_bracket: str
#     closing_bracket: str
#
# possible_brackets = [BracketType(opening_bracket=bracket1, closing_bracket=bracket2) for bracket1, bracket2 in [["<", ">"], ["[", "]"], ["{", "}"], ["(", ")"]]]


brackets_values = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def delete_pairs(line: str):
    for pattern in ["()", "[]", "{}", "<>"]:
        line = line.replace(pattern, "")
    return line


with open("10/input.txt") as file:
    data = file.read().splitlines()

result = 0

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
    first_closing_character = closing_characters[0] if closing_characters else None
    if first_closing_character:
        result += brackets_values[first_closing_character]

print(result)

