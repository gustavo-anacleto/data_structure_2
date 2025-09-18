def binary_search(nums, n, l, r):
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


def exponential_seach(nums, target):
    if nums[0] == target:
        return 0

    i = 1
    n = len(nums)

    while i < n and nums[i] < target:
        i *= 2 

    if nums[i] == target:
        return i
    
    binary_search(nums, target, i // 2, i)
    
a = lista = list(range(1, 10000000))

exponential_seach(a, 867)
    
        


        
                    

            
            

    
    
    
    