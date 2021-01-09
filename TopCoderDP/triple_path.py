def triple_path_finder(grid):
    path = []

    for i in range(len(grid)):
        path += [[]]
        for j in range(len(grid[i])):
            path[i] += [0]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                path[i][j] = grid[i][j]
            elif i == 0:
                path[i][j] = grid[i][j] + path[i][j - 1]
            elif j == 0:
                path[i][j] = grid[i][j] + path[i - 1][j]
            elif i == len(grid) - 1 and j == 0:
                path[i][j] = grid[i][j] + path[i - 1][j]
            elif i == 0 and j == len(grid[i]) - 1:
                path[i][j] = grid[i][j] + path[i][j - 1]
            else:
                if path[i - 1][j] > path[i][j - 1]:
                    path[i][j] = grid[i][j] + path[i - 1][j]
                else:
                    path[i][j] = grid[i][j] + path[i][j - 1]

    return path


def main():
    grid = [[3, 2, 1, 2], [4, 5, 1, 2], [5, 4, 8, 1], [6, 4, 1, 1]]

    print(triple_path_finder(grid))


if __name__ == "__main__":
    main()
