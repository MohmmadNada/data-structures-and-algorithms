'''
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
'''
def insertion_sort(arr):

  for i in range(1,len(arr)):
    j=i-1# start trverse from next index 
    temp = arr[i]   

    while j >=0 and temp < arr[j]:

      arr[j+1]=arr[j]
      j=j-1 
    arr[j+1]=temp
  return(arr)