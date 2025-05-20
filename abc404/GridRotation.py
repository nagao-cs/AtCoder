def solve():
    n = int(input())
    grid_s = [[cell for cell in input()] for _ in range(n)]
    grid_t = [[cell for cell in input()] for _ in range(n)]
    min_ope = n**2
    
    #[i, j]は90度回転すると[j, n-i-1]に移動する
    def rotate(grid):
        return [[grid[n-j-1][i] for j in range(n)] for i in range(n)]
    
    def diff(grid_s, grid_t):
        diff = 0
        for i in range(n):
            for j in range(n):
                if grid_s[i][j] != grid_t[i][j]:
                    diff += 1
        return diff
    current = grid_s
    for rot in range(4):
        min_ope = min(min_ope, rot+diff(current, grid_t))
        current = rotate(current)
    return min_ope
        


if __name__ == '__main__':
    print(solve())