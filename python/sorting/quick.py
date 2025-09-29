def quickSort(arr, left, right):
   if left < right:
      pivot = partition(arr left, right)
    
def partition(arr, left, right):
   mid = (left + right) // 2
   pivot = max(arr[left], arr[mid], arr[right])

   i = left - 1

   for j in range(left, right):
      if arr[j] <= pivot:
         i += 1
        #  continuar daqui

arr = [0, 1, 5, 3, 2, 4]
quickSort(arr, 0, len(arr)  - 1)