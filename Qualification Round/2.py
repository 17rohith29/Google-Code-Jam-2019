def solve(p):
    ans = ""
    for i in p:
        if i == "S":
            ans += "E"
        else:
            ans += "S"
    return ans


for i in range(int(input())):
    w = input()
    p = input()
    ans = solve(p)
    
    print("Case #{}: {}".format(i + 1, ans))
