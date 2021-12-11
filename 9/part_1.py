from dataclasses import dataclass
from typing import List


max_x = 99
max_y = 99

@dataclass
class Point:
    x: int
    y: int
    value: int
    is_low_point: bool = False

    def get_adjacent_points_coordinates(self):
        adjecent_points = []
        if self.x != 0:
            adjecent_points.append({"x": self.x - 1, "y": self.y})
        if self.x != 99:
            adjecent_points.append({"x": self.x + 1, "y": self.y})
        if self.y != 0:
            adjecent_points.append({"x": self.x, "y": self.y - 1})
        if self.y != 99:
            adjecent_points.append({"x": self.x, "y": self.y + 1})
        return adjecent_points






class Field:
    points: List[Point]

    def __init__(self):
        self.points = []

    def mark_low_points(self):
        for point in self.points:
            if point.value == 9:
                continue
            print(point.x, point.y)
            points_to_check = point.get_adjacent_points_coordinates()
            is_point_low = True
            for check_point in points_to_check:
                check_point = self.__get_point_by_x_y(check_point["x"], check_point["y"])
                if check_point.value < point.value:
                    is_point_low = False
                    break
            point.is_low_point = is_point_low


    def get_part_1_answer(self):
        return sum([point.value + 1 for point in self.points if point.is_low_point is True])



    def __get_point_by_x_y(self, x, y) -> Point:
        return list(filter(lambda point: point.x == x and point.y == y, self.points))[0]




field = Field()

with open("9/input.txt") as file:
    for y, line in enumerate(file.read().splitlines()):
        for x, point in enumerate(line):
            field.points.append(Point(x=x, y=y, value=int(point)))

field.mark_low_points()
print(field.get_part_1_answer())
