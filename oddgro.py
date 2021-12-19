
#odd grosshopper

ra= int(input())
for i in range(ra):
    a , b = map(int, input().split())
    ans = a
    answer =[]
    for i in range(b - (b % 4) + 1, b + 1):
        if ans % 2 == 0:
            ans -= i
            answer.append(ans)
        else:
            ans += i
            answer.append(ans)
            
print(answer)