GLOBAL_ADD_FISH = 0


def update_fish(singular_fish):
    if singular_fish == 0:
        singular_fish = 6
        global GLOBAL_ADD_FISH
        GLOBAL_ADD_FISH += 1
    else:
        singular_fish -= 1
    return singular_fish


with open("6/input.txt") as file:
    values = file.read().splitlines()

NUMBER_OF_DAYS = 80

fish = [int(day) for day in values[0].split(",")]

for i in range(256):
    add_fish = 0
    fish = list(map(update_fish, fish))
    fish += [8] * GLOBAL_ADD_FISH
    GLOBAL_ADD_FISH = 0

print(len(fish))