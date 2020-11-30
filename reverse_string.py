# level: easy


def reverse_string(s):
    i, j = 0, len(s) - 1
    while True:
        print(s)
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


# def reverse_string(s):
#     s.reverse()  # O(n)
#     print(s)


if __name__ == "__main__":
    my_str = ["H", "a", "n", "n", "a", "h"]
    print(reverse_string(my_str))
