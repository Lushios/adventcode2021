from statistics import mean
from typing import Dict


class DistanceCalculator:
    distance_calculations_cache: Dict[int, int]

    def __init__(self):
        self.distance_calculations_cache = {}

    def count_overral_distance_to_point(self, point, values):
        distance = 0
        for value in values:
            distance += self.__calculate_distance(point, value)
        return distance

    def __calculate_distance(self, point1, point2):
        distance = abs(point2 - point1)
        starting_calculations_point = 0
        if self.distance_calculations_cache:
            current_cache_value = self.distance_calculations_cache.get(distance)
            if current_cache_value:
                return current_cache_value
            else:
                starting_calculations_point = max(self.distance_calculations_cache)
        fuel_spent = self.distance_calculations_cache.get(starting_calculations_point, 0)
        for i in range(starting_calculations_point, distance):
            fuel_spent += i + 1  # + 1 bc we start with 0
            self.distance_calculations_cache[i] = fuel_spent

        return fuel_spent

with open("7/input.txt") as file:
    values = [int(num) for num in file.read().splitlines()[0].split(",")]

mean = int(mean(values))
distance_calculator = DistanceCalculator()

minimal_distance = distance_calculator.count_overral_distance_to_point(mean, values)
print(minimal_distance)

for i in range(30):
    for j in [i, -i]:
        temp = distance_calculator.count_overral_distance_to_point(mean + i, values)
        print(temp)
        if temp < minimal_distance:
            minimal_distance = temp

print(minimal_distance)
