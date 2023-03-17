from Flower import Flower
def read_from_file() -> list:
    chosen_file = int(input("Which file are you going to choose: \n "
                            "1.iris_test.txt \n 2.iris_training.txt \n"))
    path = ""
    list_of_flowers_to_return = []

    if chosen_file == 1:
        path = r"data/iris_test.txt"
    elif chosen_file == 2:
        path = r"data/iris_training.txt"
    else:
        print("Wrong input, are you really such a dummy???")

    with open(path, "r") as file:
        read_content = file.read()
        data_in_lines = read_content.split("\n")
        for line in data_in_lines:
            line_as_list = line.split("\t")
            if len(line_as_list) == 1:
                continue
            for i in range(len(line_as_list)):
                line_as_list[i] = line_as_list[i].strip()
            print(line_as_list)
            list_of_flowers_to_return.append(Flower(line_as_list[:len(line_as_list)-1], line_as_list[len(line_as_list)-1]))

    return list_of_flowers_to_return


def main():
    data = read_from_file()
    for flower in data:
        print(flower.attributes, end=" ")
        print(flower.flower_type)


if __name__ == '__main__':
    main()
