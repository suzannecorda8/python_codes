a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b  and a>c:
    largest_num=a
elif b>a and b>c:
    largest_num=b
else:
    largest_num=c
print(largest_num)