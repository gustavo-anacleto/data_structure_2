from typing import List

# Fulano Code O(n)
def findValue(transactionsSorted: List[int], target: int) -> int:
    steps = 0
    for transaction, i in enumerate(transactionsSorted):
        if transaction == target:
            print("[findValue]:", steps)
            return i
        steps += 1
    
    print(-1)
    return -1
#  1 <-

# Beltrano Code O(logn)
def findValueWithBinarySearch(transactionsSorted: List[int], target: int) -> int:
    r = len(transactionsSorted)
    l = 0
    steps = 0
    while l < r:
        steps += 1
        mid = (l + r) // 2

        if transactionsSorted[mid] == target:
            print("[findValueWithBinarySearch]:", steps)
            return mid
        elif target < transactionsSorted[mid]:
            r = mid
        else:
            l = mid + 1
        

    print(-1)
    return -1

# [1...10]
findValue(range(1, 11), 1)
findValueWithBinarySearch(range(1, 11), 1)