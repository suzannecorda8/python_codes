sample_list = [87, 45, 41, 65, 94, 41, 99, 94]  
print("Original list: ", sample_list)  
sample_list = list(set(sample_list))  
print("Unique list: ", sample_list)  
a = tuple(sample_list)  
print("Tuple: ", a)  
print("Minimum number is: ", min(a))  
print("Maximum number is: ", max(a)) 
