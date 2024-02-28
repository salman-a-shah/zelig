a = [4, 5, 7, 8, 9, 13, 15, 20, 22]


def f(a, x):
    ret = -1
    for n in a:
        if x == n:
            ret = n
            break
        elif x > n:
            ret = n
            continue
        elif x < n:
            break

    return ret


for k in range(25):
    print(k, f(a, k))
