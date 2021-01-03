def longest_sequence(seq):
    s = [1] * len(seq)
    ss = [[num] for num in seq]

    for i in range(len(seq)):
        best_seq = []
        for j in range(i):
            if seq[j] <= seq[i] and s[j] + 1 > s[i]:
                s[i] = s[j] + 1
                best_seq = ss[j]
        ss[i] = best_seq + ss[i]

    return s[-1], ss[-1]


def main():
    print(longest_sequence([1, 3, 2, 4, 5, 6, 0, 2, 13]))


if __name__ == "__main__":
    main()
