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


def main():
    training_data = read_from_file(2)
    test_data = read_from_file(1)
    for flower in training_data:
        print(flower.attributes, end=" ")
        print(flower.flower_type)
    print("---------------------")
    for flower in test_data:
        print(flower.attributes, end=" ")
        print(flower.flower_type)


if __name__ == '__main__':
    main()
