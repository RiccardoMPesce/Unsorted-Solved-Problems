import math

def find_shortest_path(v, w):
    distances = {}
    vertices = {}

    # We initialize all the distances either with inf (if we do not have it in our weights) or with their weight
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if i == j:
                distances[(i, j)] = 0
            else:
                distances[(i, j)] = w.get((i, j), w.get((j, i), math.inf))

            if (i, j) in w or (j, i) in w:
                vertices[(i, j)] = [i, j]
            else:
                vertices[(i, j)] = []

    # Between nodes i and j, if there is an intermediate node k through which distance is shorter, we update the 
    # distance with it
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            min_vert = vertices[(i, j)]
            for k in range(1, v + 1):
                if distances[(i, j)] > distances[(i, k)] + distances[(k, j)]:
                    distances[(i, j)] = distances[(i, k)] + distances[(k, j)]
                    # [1:] so we do not repeat k twice in the list
                    min_vert = vertices[(i, k)] + vertices[(k, j)][1:]
            vertices[(i, j)] = min_vert
            

    # Returning the shortest path from beginning to end and all the vertices through which we move
    return distances[(1, v)], vertices[(1, v)]

def main():
    v = 4
    w = {(1, 2): 3, (3, 4): 5} 

    print("Shortest path: ", find_shortest_path(v, w))

if __name__ == "__main__":
    main()