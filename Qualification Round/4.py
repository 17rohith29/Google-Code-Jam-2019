def pad(str, a):
    x = str
    ptr = 0
    for i in a:
        s, e, b = i
        numsValid = e + 1 - s - b
        ptr = ptr + numsValid - 1 # after this we should add
        x = x[:(ptr + 1)] + '9'*b + x[ptr + 1:]
        ptr = ptr + b + 1
    return x

def calc(str, s, e):
    a = str[s:(e + 1)]
    z, o = 0, 0
    for i in a:
        if i == '0':
            z += 1
        elif i == '1':
            o += 1
    return (z, o)

def solve (n, b, f): # s and e inc
    a = [[0, n - 1, b]] # start end(inc) defective
    for pp in range(f):
        q = ""
        new = []
        for i in a:
            s, e, b = i
            if s == e:
                new.append([s, e, b])
                tempQ = '0' * (e + 1 - s)
            else:
                mid = (s + e) // 2
                tempQ = '0' * (mid + 1 - s) + '1' * (e - mid)
                new.append([s, mid, 0])
                new.append([mid + 1, e, 0])
            q += tempQ
        # interface
        print(q)
        got = input()
        got = pad(got, a)
        #print(got)
        # update new
        x = 0
        i = 0
        while i < len(a):
            s, e, b = a[i]
            if s == e:
                i += 1
                x += 1
            else:
                zero, one = calc(got, s, e)
                new[x] = [new[x][0], new[x][1], new[x][1] + 1 - new[x][0] - zero]
                x += 1
                new[x] = [new[x][0], new[x][1], new[x][1] + 1 - new[x][0] - one]
                x += 1
                i += 1
        a = new
        # debug
        #for i in a:
         #   print('s{} e{} b{}'.format(i[0], i[1], i[2]))
    ans = ""
    for i in range(len(a)):
        s, e, b = a[i]
        if b >= 1:
            if ans == "":
                ans += str(s)
            else:
                ans += " " + str(s)
    print(ans)

for i in range(int(input())):
    n, b, f = list(map(int, input().split(' ')))
    solve(n, b, f)
    input()