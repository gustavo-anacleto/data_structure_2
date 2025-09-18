def binary_search(nums, n):
    l = 0
    r = len(nums)
    steps = 0

    while l < r:
        steps+=1
        mid = int((l + r) / 2)
        
        if nums[mid] == n:
            print("steps: ", steps)
            return mid
        elif nums[mid] < n:
            l = mid + 1
        else:
            r = mid
    return -1

a = lista = list(range(1, 6))
b = lista = list(range(1, 11))
c = lista = list(range(1, 41))

# binary_search(a, 3)
binary_search(b, 7)
# binary_search(c, 3)

    
        


        
                    

            
            

    
    
    
    