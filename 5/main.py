from typing import List
import random


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __key(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__key())


class Field:
    points: set[str]
    returning_points: set[str]
    answer_counter: int

    def __init__(self):
        self.points = set()
        self.returning_points = set()
        self.answer_counter = 0

    def mark_vector_as_dangerous(self, vector):
        point1 = vector[0]
        point2 = vector[1]
        if point1[0] == point2[0]:
            bigger_y = max(int(point1[1]), int(point2[1]))
            smaller_y = min(int(point1[1]), int(point2[1]))
            for i in range(smaller_y, bigger_y+1):
                self.__mark_point_as_dangerous(point1[0], i)
        elif point1[1] == point2[1]:
            bigger_x = max(int(point1[0]), int(point2[0]))
            smaller_x = min(int(point1[0]), int(point2[0]))
            for i in range(smaller_x, bigger_x+1):
                self.__mark_point_as_dangerous(i, point1[1])
        else:
            y_direction = int(point2[1]) > int(point1[1])
            if int(point2[0]) > int(point1[0]):
                step = 1
            else:
                step = -1

            for num, i in enumerate(range(int(point1[0]), int(point2[0])+step, step)):
                if not y_direction:
                    num = -num
                self.__mark_point_as_dangerous(i, int(point1[1]) + num)

    def __mark_point_as_dangerous(self, x, y):
        point = str(x) + "|" + str(y)
        if point in self.points:
            self.returning_points.add(point)
        else:
            self.points.add(point)

    def get_answer(self):
        return len(self.returning_points)


with open("5/input.txt") as file:
    values = file.read().splitlines()

vectors = []
max_x = 0
max_y = 0
for value in values:
    vector = [point.split(",") for point in value.split(" -> ")]
    vectors.append(vector)

    for point in vector:
        if int(point[0]) > max_x:
            max_x = int(point[0])
        if int(point[1]) > max_y:
            max_y = int(point[1])


field = Field()
for vector in vectors:
    field.mark_vector_as_dangerous(vector)


print(field.get_answer())

