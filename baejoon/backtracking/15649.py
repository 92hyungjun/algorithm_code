#https://www.acmicpc.net/problem/15649
import copy
#print("enter N, M")
N, M = map(int, input().split())
#N = 4
#M = 2

def contain( list, val ):
    for i in list:
        if( val == i ):
            return True

    return False

def print_cnt( val, parents ):
    #print(val, "", end="")
    if( len(parents) == M ):
        for i in parents:
            print(i,"",end="")
        print()
        return

    for i in range(N):
        print_val = i + 1
        if contain(parents, print_val):
            continue
        new_parents = copy.deepcopy(parents)
        new_parents.append(print_val)
        if( len(new_parents) > M ):
            break
        print_cnt( print_val, new_parents )
        #print()



for i in range(N):
    print_cnt(i+1, [i+1] )
    #print()
