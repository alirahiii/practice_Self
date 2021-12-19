




    
for i in range(int(input())):
    n = int(input(' '))
    a = list(map(int , input().split()))
    s = 0
    for i in range(n):
        s = max(s, a[i] -i -1)
    print(s)
    
    
    