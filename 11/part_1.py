from typing import List, Set
from dataclasses import dataclass


@dataclass
class DumboOctupus:
    x: int
    y: int
    energy: int
    flashed_this_turn: bool

    # def __hash__(self):
    #     return hash((self.x, self.y, self.energy))


class OctopusField:
    octopuses: List[DumboOctupus]
    total_flashes: int

    def __init__(self, string_octopuses: List[str]):
        self.total_flashes = 0
        self.octopuses = []
        for y, line in enumerate(string_octopuses):
            for x, energy_level in enumerate(line):
                self.octopuses.append(DumboOctupus(x=x, y=y, energy=int(energy_level), flashed_this_turn=False))

    def tick(self):
        self.__increment_all_octopuses()
        for octopus in self.octopuses:
            if octopus.energy > 9:
                self.__flash(octopus)
        flashed_octopuses = [octo for octo in self.octopuses if octo.flashed_this_turn is True]
        self.total_flashes += len(flashed_octopuses)
        for octo in flashed_octopuses:
            octo.energy = 0
            octo.flashed_this_turn = False

    def __flash(self, octopus: DumboOctupus):
        octopus.flashed_this_turn = True
        adjacent_octopuses = [
            octo for octo in self.octopuses
            if (octopus.x - 1 <= octo.x <= octopus.x+1 and octopus.y - 1 <= octo.y <= octopus.y+1)
            and (octo is not octopus)
            and octo.flashed_this_turn is False
        ]
        for octopus in adjacent_octopuses:
            self.__catch_a_flash(octopus)

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

for i in range(100):
    field.tick()

print(field.total_flashes)

