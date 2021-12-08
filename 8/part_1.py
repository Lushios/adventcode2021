from typing import List, Dict

correct_numbers_mapping = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


class Display:
    numbers_info: List[str]
    numbers_shown: List[str]
    decypher_dict: Dict[str, str]

    def __init__(self):
        self.numbers_info = []
        self.numbers_shown = []
        self.decypher_dict = {}

    def decypher(self):
        one, seven = self.__get_numbers_by_length([2, 3])
        for character in seven:
            if character not in one:
                self.decypher_dict["a"] = character

        six_zero_nine = self.__get_numbers_by_length([6])
        for number in six_zero_nine:
            for character in one:
                if character not in number:
                    self.decypher_dict["c"] = character
                    six = number

        self.decypher_dict["f"], = [
            character for character in seven
            if character not in [self.decypher_dict["a"], self.decypher_dict["c"]]
        ]
        four, = self.__get_numbers_by_length([4])
        three_two_five = self.__get_numbers_by_length([5])
        # three = [number for number in three_two_five if "".join(sorted(seven)) in "".join(sorted(number))]
        # for num in three_two_five:
        #     print("".join(sorted(seven)))
        #     print("".join(sorted(num)))

        for number in three_two_five:
            is_three = True
            for character in seven:
                if character not in number:
                    is_three = False
            if is_three:
                three = number
        self.decypher_dict["g"], = [
            character for character in three if character not in four and character != self.decypher_dict["a"]
        ]
        self.decypher_dict["d"], = [
            character for character in three if character not in list(self.decypher_dict.values())
        ]
        nine_zero_six = self.__get_numbers_by_length([6])
        for number in nine_zero_six:
            temp = number
            for character in three:
                temp = temp.replace(character, "")
            if len(temp) == 1:
                self.decypher_dict["b"] = temp
                nine = number
        eight, = self.__get_numbers_by_length([7])
        self.decypher_dict["e"], = [character for character in eight if character not in nine]
        return self

    def get_part_1_answer(self):
        actual_numbers = self.__translate_numbers_shown()
        return sum([1 for number in actual_numbers if number in [1, 4, 7, 8]])

    def get_part_2_answer(self):
        actual_numbers = self.__translate_numbers_shown()
        number_on_the_screen = int("".join([str(number) for number in actual_numbers]))
        return number_on_the_screen


    def __translate_numbers_shown(self):
        local_numbers_mapping = {}
        for key in correct_numbers_mapping:
            value = ''.join(sorted([self.decypher_dict[character] for character in correct_numbers_mapping[key]]))
            local_numbers_mapping[value] = key
        actual_numbers = []
        for number in self.numbers_shown:
            actual_numbers.append(local_numbers_mapping[''.join(sorted(number))])
        return actual_numbers




    def __get_numbers_by_length(self, length):
        return sorted(filter(lambda x: len(x) in length, self.numbers_info), key=len)


inputs = []
with open("8/input.txt") as file:
    for data in file.read().splitlines():
        split_data = data.split(" | ")
        append = Display()
        append.numbers_info = split_data[0].split(" ")
        append.numbers_shown = split_data[1].split(" ")
        inputs.append(append)

# part_1_answer = sum([display.decypher().get_part_1_answer() for display in inputs])
part_2_answer = sum([display.decypher().get_part_2_answer() for display in inputs])
print(part_2_answer)
# print(part_1_answer)

