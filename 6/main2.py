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
fish = [5]

# 5 - 256
# 4 - 257
# 3 - 258
# 2 - 259
# 1 - 260
result = []


for i in range(260):
    fish = list(map(update_fish, fish))
    fish += [8] * GLOBAL_ADD_FISH
    if i >= 255:
        result.append(len(fish))
    GLOBAL_ADD_FISH = 0

print(result)
