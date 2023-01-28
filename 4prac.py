# find a maximum of two numbers.
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# def max(a,b):
#     if a>=b:
#        return a
#     else:
#        return b
# print(max(a,b))

# print stars pattern


n=int(input("Enter the number:"))
num=1
for i in range(0,n+1):
   for j in range(0,i+1):
      print(num,end=" ")
      num+=1
   print()


