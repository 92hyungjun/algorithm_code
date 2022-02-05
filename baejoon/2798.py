N, M = map(int, input().split())
cards = list(map(int, input().split()))

def find_val():
    indexs = []
    max_val = 0
    for x in range( N ):
        for y in range( N ):
            for z in range( N ):
                if x == y:
                    continue
                if x == z:
                    continue
                if y == z:
                    continue
                sum = cards[x] + cards[y] + cards[z]
                # M보다 큰 경우
                if( sum > M ):
                    continue

                #정답
                if( sum == M ):
                    indexs.clear()
                    indexs.append(x)
                    indexs.append(y)
                    indexs.append(z)
                    #print( f"equal {x},{y},{z}  {cards[x]} + {cards[y]} + {cards[z]} = {sum}" )
                    return sum
                elif( sum > max_val ): # 여태까지 가장 큰 값인경우.
                    indexs.clear()
                    indexs.append(x)
                    indexs.append(y)
                    indexs.append(z)
                    #print(f"max {x},{y},{z}  {cards[x]} + {cards[y]} + {cards[z]} = {sum}")
                    max_val = sum

    return max_val

z = find_val()
print(z)
