from Flower import Flower

"""
Class Counter, is class that is being used to check what is type
of K (attribute given by User), flowers in the distances list, after sorting it
"""
class Counter:
    def __init__(self):
        self.iris_setosa = 0
        self.iris_versicolor = 0
        self.iris_virginica = 0

    """
    Checks what is the type of N out of K flowers, and increment 
    the variable that represents the number of its flower type
    """
    def count(self, flower_type: str):
        if flower_type == "Iris-setosa":
            self.iris_setosa = self.iris_setosa + 1
        elif flower_type == "Iris-versicolor":
            self.iris_versicolor = self.iris_versicolor + 1
        elif flower_type == "Iris-virginica":
            self.iris_virginica = self.iris_virginica + 1
    """
    Returns the type of flower that has been found the most in the  
    distances list, out of first K
    """
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
                line_as_list[i] = line_as_list[i].strip()  # removing white spaces cause University decided to gives us data not only with spaces but also with tabulators :))))
            list_of_flowers_to_return.append(
                Flower(line_as_list[:len(line_as_list) - 1], line_as_list[len(line_as_list) - 1]))  # We know that the last in the list will always be flower type rest is attributes

    return list_of_flowers_to_return


def reformat_data_commas_to_dots(data):
    for flower in data:
        flower.change_commas_to_dots()


def classify_data(test_data, training_data, how_many_neighbours):
    correct_guesses = 0
    for current_flower_test in test_data:
        counter = Counter()
        distances = []

        """
        Adds tuple of the distance and the type of flower, from investigated flower
        """
        for current_flower_training in training_data:
            distances.append(
                (current_flower_test.calculate_distance(flower=current_flower_training), current_flower_training.flower_type))
        distances.sort(key=lambda a: a[0])

        for neighbour in range(how_many_neighbours):
            counter.count(flower_type=distances[neighbour][1])

        """ We check if the flower type is None, cause if it is that means we are classifying users data not iris_training.txt data"""
        if current_flower_test.flower_type is not None:
            if counter.which_one() == current_flower_test.flower_type:
                correct_guesses = correct_guesses + 1
        else:
            print("By given attributes flower has been classified as: " + counter.which_one())

    """ If correct guesses are equal to 0 that means we have been checking users data and there is no need to print % value of correct guesses"""
    if correct_guesses != 0:
        print(str(correct_guesses) + " " + str(round((correct_guesses * 100) / len(test_data), 2)) + "%")


def user_input_part(training_data, how_many_neighbours):
    user_input = input("Give me values separated by spaces, and with dots as number pointer,"
                       " NOT COMMAS LIKE IN DATA GIVEN BY FABULOUS UNIVERSITY, in this program version required number of attributes is "
                       + str(len(training_data[0].attributes)) + ": ").split(" ")
    for i in range(len(user_input)):
        user_input[i] = float(user_input[i])
    classify_data(test_data=[Flower(user_input, None)], training_data=training_data,
                  how_many_neighbours=how_many_neighbours)


def main():
    training_data = read_from_file(2)
    test_data = read_from_file(1)
    reformat_data_commas_to_dots(training_data)
    reformat_data_commas_to_dots(test_data)
    how_many_neighbours = int(input('What will be the k value, in the kNN algorithm: '))

    classify_data(test_data=test_data, training_data=training_data, how_many_neighbours=how_many_neighbours)

    does_user_want_to_input = int(input("0 - I want to input my own attributes \n1 - End the program\n")) == 0

    while does_user_want_to_input:
        user_input_part(training_data=training_data, how_many_neighbours=how_many_neighbours)
        does_user_want_to_input = int(input("0 - I want to input my own attributes again\n1 - End the program\n")) == 0


if __name__ == '__main__':
    main()
