def parse_instruction(instruction: str):
    return instruction.split(" ")[2].split("=")


def perform_transformation(point, axis, number):
    if point[axis] > number:
        point[axis] = 2 * number - point[axis]
    return point


def perform_instruction(points, instruction):
    axis, number = parse_instruction(instruction)
    return list(map(lambda x: perform_transformation(x, axis, int(number)), points))


with open("13/input.txt") as file:
    data = file.read().splitlines()



folds = []
points = []
for input in data:
    if not input:
        continue
    elif "fold" in input:
        folds.append(input)
    else:
        list_point = [int(num) for num in input.split(",")]
        points.append({"x": list_point[0], "y": list_point[1]})

for fold in folds:
    points = perform_instruction(points, fold)


max_x = 0
max_y = 0
for point in points:
    if point["x"] > max_x:
        max_x = point["x"]
    if point["y"] > max_y:
        max_y = point["y"]

field = []
for i in range(max_y+1):
    line = []
    for j in range(max_x+1):
        line.append(".")
    field.append(line)

print(field)

for point in points:
    field[point["y"]][point["x"]] = "X"

with open("13/output.txt", "w") as file:
    for line in field:
        file.write("".join([str(temp) for temp in line]))
        file.write("\n")