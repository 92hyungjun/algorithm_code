# https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())
#N = 4
#M = 2
out = []

def solve(depth, idx):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        solve(depth+1, i)
        out.pop()

solve(0, 0)
