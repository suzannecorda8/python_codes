num=[1,2,5,8,9,6,4,0]
n=int(input("Enter the number to be found:"))
flag=0
for i in range(len(num)):
    if (n==num[i]):
       print("Number found at index",i)
       flag=1
       break
if(flag==0):
       print("Number not found")
      
    