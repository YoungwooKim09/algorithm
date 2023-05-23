a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def solve(a):
    ans = 0

    for i in range(len(a)) :
        ans = ans + a[i]

    return ans

print(solve(a))