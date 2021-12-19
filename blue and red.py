
#blue & red

for _ in range(int(input('chand ta add mikhay bedi: '))):
    n=int(input('mikhay chand raghami bashe: '))
    arr=list(map(int,input('add ro beghoo: ').split()))
    s=input(' az beyn b va r yeki ro beghoo: ')
    b=[]
    r=[]
    ans=True
    for i in range(n):
        if s[i]=="B":
            b.append(arr[i])
        else :
            r.append(arr[i])
 
    b.sort()
    r.sort(reverse=True)
    for i in range(len(b)):
        if b[i]<=i:
            ans=False
            break
    for i in range(len(r)):
        if r[i]>n-i:
            ans=False
            break
    if ans:
        print("YES")
    else :
        print("NO")

