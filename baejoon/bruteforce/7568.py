#https://www.acmicpc.net/problem/7568

N = int(input())
vals = []
for i in range(N):
    #weight, height = map(int, input().split())
    w_and_h = list(map(int, input().split()))
    vals.append( w_and_h )

"""
vals = [ [55,185],
         [58,183],
         [88,186],
         [60,175],
         [46,155] ]
"""

ranks = []
for i in range(N):
    rank = 1
    for y in range(N):
        if( i == y ):
            continue

        me = vals[i]
        target = vals[y]
        if( me[0] < target[0] and me[1] < target[1] ):
            rank += 1
    ranks.append( rank )

for rank in ranks:
    print(rank,"",end="")
