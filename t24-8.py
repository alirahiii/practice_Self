# class Parent:
#     def __init__(self, name , txt):
#         self.name = name
#         self.message = txt

#     def printmessage(self):
#         print(f'{self.name} nevesht {self.message}')
        
        
        

# class Child(Parent):
#     def __init__(self,name ,  txt):
#         super().__init__(name,txt)
        
        
        
        
        
        
        
        

# x =Child('ali ' , 'salalm khobin::::')
# x.printmessage()




# def factor (n):
#     if n == 1 :
#         return 1
#     else:
#         return n * factor(n-1)


# print(factor(3))





# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 

# print(Fibonacci(9))
 




  
# def TowerOfHanoi(n , source, destination, auxiliary):
#     if n==1:
#         print ("Move disk 1 from source"),source,("to destination")
#         return
#     TowerOfHanoi(n-1, source, auxiliary, destination)
#     print (("Move disk"),n,("from source"),source,("to destination"),destination)
#     TowerOfHanoi(n-1, auxiliary, destination, source)
# n = 4
# TowerOfHanoi(n,'A','B','C') 


# def TowerOfHanoi(n , s_pole, d_pole, i_pole):           
#     if n == 1:
#         print("Move disc 1 from pole",s_pole,"to pole",d_pole)
#         return
#     TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
#     print("Move disc",n,"from pole",s_pole,"to pole",d_pole)
#     TowerOfHanoi(n-1, i_pole, d_pole, s_pole)

# n = 3
# TowerOfHanoi(n, 'A', 'C', 'B')
# # A, C, B are the name of poles
 



