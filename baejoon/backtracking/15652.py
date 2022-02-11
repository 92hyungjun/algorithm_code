#import copy
#print("enter N, M")
N, M = map(int, input().split())
#N = 3
#M = 3

def print_cnt( start, parents ):
    if( len(parents) == M ):
        print(' '.join(map(str, parents)))
        return

    for i in range(start, N):
        print_val = i + 1
        parents.append(print_val)
        print_cnt( i, parents )
        parents.pop()

print_cnt(0, [] )

