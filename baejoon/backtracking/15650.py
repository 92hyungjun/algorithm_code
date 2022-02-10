#https://www.acmicpc.net/problem/15650

import copy
#print("enter N, M")
N, M = map(int, input().split())
#N = 4
#M = 4

global_list = []

def contain_list( list ):
    for g_list in global_list:

        same_cnt = 0
        for g_element in g_list:
            if contain(list, g_element):
                same_cnt += 1
        if same_cnt == M:
            return True

    return False

def contain( list, val ):
    for i in list:
        if( val == i ):
            return True

    return False

def print_cnt( val, parents ):
    #print(val, "", end="")
    if( len(parents) == M ):
        if contain_list(parents):
            return

        global_list.append( parents )
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
