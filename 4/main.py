from typing import List


class MatrixNumber:
    number: int
    marked: bool

    def __init__(self, number, marked):
        self.number = number
        self.marked = marked

    def is_marked(self):
        return self.marked


class Matrix:
    numbers: List[List[MatrixNumber]]
    won: bool

    def __init__(self):
        self.numbers = []
        self.won = False

    def mark_number(self, number):
        for row in self.numbers:
            for element in row:
                if element.number == number:
                    element.marked = True

    def check_for_win(self):
        if self.won:
            return False
        for y in range(len(self.numbers[0])):
            sum = 0
            for x in range(len(self.numbers)):
                if self.numbers[x][y].is_marked():
                    sum += 1
            if sum == len(self.numbers):
                return True

        for x in range(len(self.numbers)):
            sum = 0
            for y in range(len(self.numbers[0])):
                if self.numbers[x][y].is_marked():
                    sum += 1
            if sum == len(self.numbers[0]):
                return True
        return False

    def win(self, koef):
        self.won = True
        winning_sum = self.__count_winning_sum(koef)
        print(winning_sum)

    def __count_winning_sum(self, koef):
        sum = 0
        for row in self.numbers:
            for element in row:
                if not element.is_marked():
                    sum += element.number
        return sum * koef


def announce_a_number(matrixes, number):
    for matrix in matrixes:
        matrix.mark_number(int(number))
        if matrix.check_for_win():
            matrix.win(int(number))


with open("input.txt") as file:
    values = file.read().splitlines()

input_numbers = values.pop(0).split(",")

matrixes = []

current_matrix = False

for value in values:
    if not value:
        if current_matrix:
            matrixes.append(current_matrix)

        current_matrix = Matrix()
    else:
        vals = value.split(" ")
        current_matrix.numbers.append([MatrixNumber(number=int(num), marked=False) for num in filter(None, value.split(" "))])

for number in input_numbers:
    announce_a_number(matrixes, number)
