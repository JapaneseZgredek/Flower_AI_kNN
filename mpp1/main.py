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
        data_in_list = read_content.split("\t")
        
    return []


def main():
    data = read_from_file()


if __name__ == '__main__':
    main()
