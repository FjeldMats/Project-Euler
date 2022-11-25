import sys
sys.setrecursionlimit(10**4)

def count_farey_sequence(s, e, D):

    middle = (s[0] + e[0], s[1] + e[1])

    if middle[1] > D:
        return 0
    else: 
        return 1 + count_farey_sequence(s, middle, D) + count_farey_sequence(middle, e, D)

if __name__ == "__main__":
    print(count_farey_sequence((1,3), (1,2), 8))
    print(count_farey_sequence((1,3), (1,2), 12_000))