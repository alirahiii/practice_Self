#factorial 


# def factor (a):
#     if a < 0:
#         raise Exception('adad manfi nadarim ')
#     if a == 1 or a == 0:
#         return 1
#     else:
#         return a * factor(a-1)
    
# print(factor(5))


# def fibo (n , cache ={}):
#     if n in cache:
#         return cache[n]
#     if n == 1 or n ==2 :
#         cache[n]=1
#         return 1
#     else :
#         temp = fibo(n-1)+fibo(n-2)
#         cache[n]=temp
#         return fibo(n -1) + fibo(n-2)





# print(fibo(200))

from os import write


myuser =[
    {
        'name':'ali',
        'age':20
    },
    {
        'name':'ali',
        'age':21
    }
    
    
    
]
with open('log.txt' ,'w+') as f :
    for elm in myuser :
        f.write(f"name:{elm['name']} age:{elm ['age']}\n")
        f.write(' '*10)
    with open('log.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print (last_line)
  
    
    




