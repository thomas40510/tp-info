def fact(n):
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k


def fact_r(n):
    if n == 0:
        return 1
    else:
        return n * fact_r(n - 1)


def tablePytha(n):
    a = ['x']
    for u in range(1, n + 1):
        a.append(u)
    b = [u for u in a]
    for i in range(1, n + 1):
        b[0] = i
        for y in range(1, n + 1):
            b[y] = a[y] * a[i]
        print(b)


tablePytha(3)

L = [i for i in range(7, -1, -3)]
print(L)

L1 = [i for i in range(0, 20)]
L2 = [i for i in L1 if i % 2 == 0 and i % 5 != 0]

print(L1, L2)


def remplace(lst, e, f):
    return [i if i != e else f for i in lst]

L3 = 4*L
print(L3)
print(remplace(L3, 4, 15))

print(L1[:len(L1)//2])
print(L1[len(L1)//2:])
