a=int(input("Enter a number:"))
count=0
i=1
while(i<=a):
   if a%i==0:
    count+=1
   i+=1
if count==2:
    print("It is a prime number:")
else:
    print("It is not a prime number:")
