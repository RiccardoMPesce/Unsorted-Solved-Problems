def triple_path_finder(path):
    max_amount = []

    for i in range(len(path)):
        max_amount += [[]]
        for j in range(len(path[i])):
            max_amount[i] += [0]

    # TODO

    return max_amount


def main():
    path = [[3, 2, 1, 2], [4, 5, 1, 2], [5, 4, 8, 1], [6, 4, 1, 1]]

    print(triple_path_finder(path))

if __name__ == "__main__":
    main()
