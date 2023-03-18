from Flower import Flower
class Counter:
    def __init__(self):
        self.iris_setosa = 0
        self.iris_versicolor = 0
        self.iris_virginica = 0

    def count(self, flower_type: str):
        if flower_type == "Iris-setosa":
            self.iris_setosa = self.iris_setosa + 1
        elif flower_type == "Iris-versicolor":
            self.iris_versicolor = self.iris_versicolor + 1
        elif flower_type == "Iris-virginica":
            self.iris_virginica = self.iris_virginica + 1

    def which_one(self) -> str:
        if self.iris_setosa >= self.iris_virginica and self.iris_setosa >= self.iris_versicolor:
            return "Iris-setosa"
        elif self.iris_virginica >= self.iris_setosa and self.iris_virginica >= self.iris_versicolor:
            return "Iris-virginica"
        elif self.iris_versicolor >= self.iris_setosa and self.iris_versicolor >= self.iris_virginica:
            return "Iris-versicolor"
def which_path(chosen_file):
    if chosen_file == 1:
        return r"data/iris_test.txt"
    elif chosen_file == 2:
        return r"data/iris_training.txt"
def read_from_file(chosen_file) -> list:
    list_of_flowers_to_return = []
    path = which_path(chosen_file)

    with open(path, "r") as file:
        read_content = file.read()
        data_in_lines = read_content.split("\n")
        for line in data_in_lines:
            line_as_list = line.split("\t")
            if len(line_as_list) == 1:
                continue
            for i in range(len(line_as_list)):
                line_as_list[i] = line_as_list[i].strip()
            list_of_flowers_to_return.append(Flower(line_as_list[:len(line_as_list)-1], line_as_list[len(line_as_list)-1]))

    return list_of_flowers_to_return


def reformat_data_commas_to_dots(data):
    for flower in data:
        flower.change_commas_to_dots()
def main():
    training_data = read_from_file(2)
    test_data = read_from_file(1)
    reformat_data_commas_to_dots(training_data)
    reformat_data_commas_to_dots(test_data)
    how_many_neighbours = int(input('What will be the k value, in the kNN algorithm: '))
    correct_guesses = 0
    for current_flower_test in test_data:
        counter = Counter()
        distances = []

        for current_flower_training in training_data:
            distances.append((current_flower_test.calculate_distance(current_flower_training), current_flower_training.flower_type))
        distances.sort(key=lambda a: a[0])

        for neighbour in range(how_many_neighbours):
            counter.count(distances[neighbour][1])
        if counter.which_one() == current_flower_test.flower_type:
            correct_guesses = correct_guesses + 1

    print(str(correct_guesses) + " " + str(round((correct_guesses * 100) / len(test_data), 2)) + "%")

    does_user_want_to_input = int(input("0 - I want to input my own attributes \n1 - End the program\n")) == 0
    while does_user_want_to_input:
        user_input = input("Give me values separated by spaces, and with dots as number pointer,"
                           " NOT COMMAS LIKE IN DATA GIVEN BY FABULOUS UNIVERSITY, in this program version required number of attributes is "
                           + str(len(test_data[0].attributes)) + ":").split(" ")



if __name__ == '__main__':
    main()
