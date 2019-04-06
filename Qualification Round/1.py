def help(n):
    a = str(n)
    lst = []
    for i in a:
        lst.append(int(i))

    a, b = [], []
    for i in lst:
        if i == 4:
            a.append(3)
            b.append(1)
        else:
            a.append(i)
            b.append(0)
    x, y = "", ""
    for i in a:
        x += str(i)
    for j in b:
        y += str(j)
    return (int(x), int(y))

for i in range(int(input())):
    n = int(input())
    a,b = help(n)
    print("Case #{}: {} {}".format(i + 1,a, b))
