#https://www.acmicpc.net/problem/9663

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# 한줄씩 재귀하며 dfs 실행

def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


# N = int(input())/
N = int(input())
#N = 4
row = [0] * N
result = 0

#import time
#st = time.time()
dfs(0)
#ed = time.time()
#print( ed-st )

print(result)
