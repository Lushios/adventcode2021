from typing import List
import itertools
from dataclasses import dataclass


@dataclass
class DumboOctupus:
    x: int
    y: int
    energy: int
    flashed_this_turn: bool


class OctopusField:
    octopuses: List[DumboOctupus]

    def __init__(self, string_octopuses: List[str]):
        self.octopuses = []
        for y, line in enumerate(string_octopuses):
            for x, energy_level in enumerate(line):
                self.octopuses.append(DumboOctupus(x=x, y=y, energy=int(energy_level), flashed_this_turn=False))

    def tick(self):
        self.__increment_all_octopuses()
        for octopus in self.octopuses:
            if octopus.energy > 9 and not octopus.flashed_this_turn:
                self.__flash(octopus)

        flashed_octopuses = [octo for octo in self.octopuses if octo.flashed_this_turn is True]
        for octo in flashed_octopuses:
            octo.energy = 0
            octo.flashed_this_turn = False

        if len(flashed_octopuses) == 100:
            return True
        else:
            return False

    def __flash(self, octopus: DumboOctupus):
        octopus.flashed_this_turn = True
        for octo in self.octopuses:
            if (octopus.x - 1 <= octo.x <= octopus.x + 1 and octopus.y - 1 <= octo.y <= octopus.y + 1) and (
                    octo is not octopus) and octo.flashed_this_turn is False:
                self.__catch_a_flash(octo)

    def __catch_a_flash(self, octopus: DumboOctupus):
        octopus.energy += 1
        if octopus.energy > 9:
            self.__flash(octopus)

    def __increment_all_octopuses(self):
        for octopus in self.octopuses:
            octopus.energy += 1


with open("11/input.txt") as file:
    data = file.read().splitlines()

field = OctopusField(data)

for i in itertools.count():
    print(i)
    are_we_there_yet = field.tick()
    if are_we_there_yet:
        print(i)
        break


