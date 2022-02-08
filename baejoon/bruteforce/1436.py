#  https://www.acmicpc.net/problem/1436
N = int(input())
#N = 500

def find_666(int_val):
    str_val = str(int_val)
    str_size = len(str_val)

    same_val_cnt = 0
    for i in range(str_size):
        if str_val[i] == "6":
            same_val_cnt += 1
        else:
            same_val_cnt = 0

        if same_val_cnt == 3:
            return True
    return False

val = 0
cnt = 0
while True:
    if find_666(val):
        #print(val)
        cnt += 1

    if cnt == N:
        print(val)
        break

    val += 1
