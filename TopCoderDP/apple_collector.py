def collect_max(grid):
    grid_path = grid[:][:]

    for i in range(len(grid_path)):
        for j in range(len(grid_path[i])):
            if i == 0 and j == 0:
                grid_path[i][j] = grid_path[i][j]
            elif i == 0:
                grid_path[i][j] = grid[i][j] + grid_path[i][j - 1]
            elif j == 0:
                grid_path[i][j] = grid[i][j] + grid_path[i - 1][j]
            else:
                grid_path[i][j] = grid[i][j] + max(grid_path[i][j - 1], grid_path[i - 1][j])

    return grid_path[-1][-1]


def main():
    print(collect_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == "__main__":
    main()