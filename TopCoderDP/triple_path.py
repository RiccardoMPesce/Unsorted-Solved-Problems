def triple_path_finder(grid):
    path = []
    items = []
    after_path = []
    three_paths = []

    for i in range(len(grid)):
        path += [[]]
        items += [[]]
        for j in range(len(grid[i])):
            path[i] += [0]
            items[i] += [[]]

    for n in range(3):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    path[i][j] = grid[i][j]
                    items[i][j] = [(i, j)]
                elif i == 0:
                    path[i][j] = grid[i][j] + path[i][j - 1]
                    items[i][j] = items[i][j - 1] + [(i, j)]
                elif j == 0:
                    path[i][j] = grid[i][j] + path[i - 1][j]
                    items[i][j] = items[i - 1][j] + [(i, j)]
                elif i == len(grid) - 1 and j == 0:
                    path[i][j] = grid[i][j] + path[i - 1][j]
                    items[i][j] = items[i - 1][j] + [(i, j)]
                elif i == 0 and j == len(grid[i]) - 1:
                    path[i][j] = grid[i][j] + path[i][j - 1]
                    items[i][j] = items[i][j - 1] + [(i, j)]
                else:
                    if path[i - 1][j] > path[i][j - 1]:
                        path[i][j] = grid[i][j] + path[i - 1][j]
                        items[i][j] = items[i - 1][j] + [(i, j)]
                    else:
                        path[i][j] = grid[i][j] + path[i][j - 1]
                        items[i][j] = items[i][j - 1] + [(i, j)]

        after_path.append(path[-1][-1])
        three_paths.append(items[-1][-1])
        
        for (p1, p2) in items[-1][-1]:
            grid[p1][p2] = 0

    return sum(after_path), three_paths


def main():
    grid = [[3, 2, 1, 2], [4, 5, 1, 2], [5, 4, 8, 1], [6, 4, 1, 1]]

    print(triple_path_finder(grid))


if __name__ == "__main__":
    main()
