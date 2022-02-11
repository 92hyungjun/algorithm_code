# https://www.acmicpc.net/problem/15651
# 시간초과 때문에 copy를 제거함.

import copy
#print("enter N, M")
N, M = map(int, input().split())
#N = 3
#M = 3

def print_cnt( val, parents ):
    if( len(parents) == M ):
        for i in parents:
            print(i,"",end="")
        print()
        del parents[-1]
        return

    for i in range(N):
        print_val = i + 1
        #new_parents = copy.deepcopy(parents)
        new_parents = parents
        if (len(new_parents) + 1 > M):
            break
        new_parents.append(print_val)
        print_cnt( print_val, new_parents )
        #print()
    del parents[-1]

for i in range(N):
    print_cnt(i+1, [i+1] )

