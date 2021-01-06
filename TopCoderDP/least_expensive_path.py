import math

def least_expensive_path(v, w, amount):
    visited_states = {}
    min_cost = []

    for i in range(len(v)):
        min_cost += [[]]
        for j in range(amount + 1):
            visited_states[(i, j)] = False
            min_cost[i] += [math.inf]

    min_cost[0][amount] = 0

    while True:
        valid_unvisited = [(k, v) for (k, v) in visited_states if visited_states[(k, v)] == False and min_cost[k][v] < math.inf]
        if len(valid_unvisited) == 0:
            break
        else:
            for (i, j) in valid_unvisited:
                visited_states[(i, j)] = True
                near_vertices = [v for v in range(len(v)) if (i, v) in w]
                for ve in near_vertices:
                    if j - v[ve] >= 0 and min_cost[ve][j - v[ve]] > min_cost[i][j] + w[(i, ve)]:
                        min_cost[ve][j - v[ve]] = min_cost[i][j] + w[(i, ve)]

    best_index = max([idx for idx in range(amount + 1) if min_cost[-1][idx] == min(min_cost[-1])])

    return min_cost[-1][best_index]


def main():
    v = {0: 0, 1: 1, 2: 1, 3: 1}
    w = {(0, 1): 1, (1, 0): 1, (0, 2): 1, (2, 0): 1, (1, 3): 1, (3, 1): 1, (2, 3): 1, (3, 2): 1}
    amount = 10

    print(least_expensive_path(v, w, amount))


if __name__ == "__main__":
    main()