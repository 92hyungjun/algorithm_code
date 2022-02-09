# https://www.acmicpc.net/problem/1018
#print("enter N, M")
N, M = map(int, input().split())
vals = []
for i in range(N):
    row = list(map(str, input().split()))
    #row = (map(str, input().split()))
    vals.append( row )




START_POSITION_ROW_SIZE = N - 7
START_POSITION_COL_SIZE = M - 7

TOGGLE_COLOR_MAP = { "W":"B", "B":"W" }

def find_rewrite_cnt( row_offset, col_offset, first_color ):
    rewrite_cnt = 0
    #print("first color ", first_color)
    for base_row in range(8):
        rewrite_row = 0
        if( base_row % 2 == 0 ):
            toggle_color = first_color
        else:
            toggle_color = TOGGLE_COLOR_MAP[first_color]

        for base_col in range(8):
            r_idx = base_row + row_offset
            c_idx = base_col + col_offset

            target_color = vals[r_idx][0][c_idx]
            #print( target_color, "", end="" )
            if( target_color != toggle_color ):
                rewrite_row += 1

            toggle_color = TOGGLE_COLOR_MAP[toggle_color]

        #print("diff cnt", rewrite_row)
        rewrite_cnt += rewrite_row
    return rewrite_cnt

rewrite_cnts = []
for i in range( START_POSITION_ROW_SIZE ):
    for j in range( START_POSITION_COL_SIZE ):
        start_row = i
        start_col = j

        case1 = find_rewrite_cnt(start_row, start_col, "W")
        case2 = find_rewrite_cnt(start_row, start_col, "B")
        rewrite_cnts.append( min(case1, case2) )

rewrite_cnts.sort()
print(rewrite_cnts[0])

