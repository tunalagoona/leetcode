# level: easy


def reverse_string(s):
    i = 0
    j = len(s) - 1
    while True:
        print(s)
        if i >= j:
            return
        a = s[i]
        s[i] = s[j]
        s[j] = a
        i += 1
        j -= 1


if __name__ == "__main__":
    my_str = ["H", "a", "n", "n", "a", "h"]
    print(reverse_string(my_str))
