def quickSort(arr, left, right):
   if left < right:
      print(arr[left:right + 1 ])
      pivot = partition(arr, left, right)
      quickSort(arr, left, pivot - 1)
      quickSort(arr, pivot + 1, right)
    
def partition(arr, left, right):
   pivot = arr[right]

   i = left - 1

   for j in range(left, right):
      if arr[j] <= pivot:
         i += 1
         arr[i], arr[j] = arr[j], arr[i]
      
   arr[i + 1], arr[right] = arr[right], arr[i + 1]
      
   return i + 1


arr = [0, 1, 5, 3, 2, 4]
quickSort(arr, 0, len(arr) - 1)
print("Final Array:", arr)