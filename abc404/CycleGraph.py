def solve():
    n, m = map(int, input().split())
    
    graph = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].add(b)
        graph[b-1].add(a)
    
    seen = [False for _ in range(n)]
    finised = [False for _ in range(n)]
    def dfs(graph: list, v: int):
        seen[v-1] = True
        for next_v in graph[v-1]:
            if seen[next_v]:
                continue
            if finised[next_v-1]:
                continue
            if seen[next_v-1] and not finised[next_v-1]:
                return True
            if dfs(graph, next_v):
                return True
            
        finised[v-1] = True
        return False  
    return dfs(graph, 0)          
    
if __name__ == '__main__':
    print(solve())