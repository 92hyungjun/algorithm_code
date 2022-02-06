# https://www.acmicpc.net/problem/2231

#N = 216
N = int( input() )

def get_each_element(origin_val):
    NEW_N = origin_val
    arr = []
    while True:
        val = NEW_N % 10
        #print(val)
        if (NEW_N == 0):
            break
        arr.append(val)
        NEW_N = int(NEW_N / 10)
    return arr

def array_sum( arr ):
    sum = 0
    offset = 1
    for i in arr:
        sum = sum + (i * offset)
        #offset *= 10
    return sum

#elements_arr = get_each_element(N)
#a = array_sum(elements_arr)

target = N
minimum_const = 0
while True:
    if( target == 0 ):
        #print("target is 0")
        break
    elements_arr = get_each_element(target)
    element_sum_val = array_sum(elements_arr)
    sum_val = target + element_sum_val
    if( sum_val == N ):
        #print("goal", target, sum_val, elements_arr)
        minimum_const = target
        #if( minimum_const > target ):
        #    minimum_const = target
        #break
    target = target - 1

print(minimum_const)
