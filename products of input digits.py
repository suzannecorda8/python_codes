a=int(input("Enter a number:"))
p=1
while(a):
    r=a %10
    p=p*r
    a=a//10
print("product of digits",p)