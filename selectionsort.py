def selectionsort(arr,n):
 
  for i in range(n):
      min_indx=i
    
      for j in range(i+1,n):
        if arr[j]< arr[min_indx]:
            min_indx=j
          
      arr[i],arr[min_indx]= arr[min_indx],arr[i]
arr = [1,5,2,9,0,6,4]
n=len(arr)
selectionsort(arr, n)
print('The array in Ascending Order by selection sort :', arr)
