# def duplicateArray(arr:list,n:int):
#     arr.sort
#     for i in range(1,n):
#         if arr[i-1]== arr[i]:
#             return arr[i]
arr=(input("Enter an array:"))
print(arr)
print("Duplicate elements are:")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]== arr[j]):
           print(arr[i])


