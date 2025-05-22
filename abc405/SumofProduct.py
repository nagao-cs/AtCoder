def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    ans = 0
    for i in range(n):
        total -= a[i]
        if a[i] == 0:
            continue
        ans += a[i] * total
    return ans

if __name__ == '__main__':
    print(solve())