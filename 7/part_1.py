from statistics import median

def count_overral_distance_to_point(point, values):
    distance = 0
    for value in values:
        distance += abs(value-point)
    return distance

with open("7/input.txt") as file:
    values = [int(num) for num in file.read().splitlines()[0].split(",")]

median = int(median(values))
minimal_distance = count_overral_distance_to_point(median, values)
print(minimal_distance)

for i in range(10):
    for j in [i, -i]:
        temp = count_overral_distance_to_point(median+i, values)
        print(temp)
        if temp < minimal_distance:
            minimal_distance = temp

print(minimal_distance)