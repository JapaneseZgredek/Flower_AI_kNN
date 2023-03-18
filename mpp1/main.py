from Flower import Flower
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
    # how_many_neighbours = int(input('What will be the k value, in the kNN algorithm: '))
    for current_flower_test in test_data:
        distances = []
        for current_flower_training in training_data:
            distances.append(current_flower_test.calculate_distance(current_flower_training))
        print(distances)


if __name__ == '__main__':
    main()
