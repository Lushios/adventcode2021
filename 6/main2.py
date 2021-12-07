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

# fish = [int(day) for day in values[0].split(",")]
fish = [1]

# 7 - 256
# 6 - 257
# 5 - 258
# 4 - 259
# 3 - 260
# 2 - 261
# 1 - 262


for i in range(262):
    fish = list(map(update_fish, fish))
    fish += [8] * GLOBAL_ADD_FISH
    print(GLOBAL_ADD_FISH)
    GLOBAL_ADD_FISH = 0

print(len(fish))
