import sys
n = int(input())
smallest = sys.maxsize
biggest = -sys.maxsize


for i in range(0, n):
    nums = int(input())
    if nums > biggest:
        biggest = nums
    if nums < smallest:
        smallest = nums
    
    

    
        
        
        
print(f"Max number: {biggest}")
print(f"Min number: {smallest}")