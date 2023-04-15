n = int(input())  
lst = []  
for i in range(n):
    element = input() 
    lst.append(element)  


sorted_lst = sorted(lst, key=lambda x: x[-2])

print(sorted_lst) 
