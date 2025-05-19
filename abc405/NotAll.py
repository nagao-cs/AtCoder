from collections import Counter
def solution():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    
    m_set = {i for i in range(1, m+1)}
    print(m_set, set(a))
    if not set(a).issubset(m_set):
      return 0

    a_dict = Counter(a)

    cnt = 0
    while True:
        item = a.pop()
        if item <= m:
            a_dict[item] -= 1
            cnt += 1
            if a_dict[item] == 0:
                break

    return cnt

if __name__ == '__main__':
    cnt = solution()
    print(cnt)