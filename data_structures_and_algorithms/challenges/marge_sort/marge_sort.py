def margeSort(arr):
  n=len(arr)
  if n>1:# not one element 
    # divide into 2 array
    if n%2:# EVEN 
      mid =int(n/2)
    else:
      mid =(n/2)+0.5
      mid=int(mid)
    left=arr[:mid]
    right=arr[mid:]
    margeSort(left)# sort the left side
    margeSort(right)# sort the right side
    marge(left,right,arr) # merge the sorted left and right sides together
def marge(left,right,arr):
    i,j,k=0,0,0
    while i< len(left) and j< len(right):
      if left[i]<= right[j]:
        arr[k]=left[i]
        i=i+1
      else:
        arr[k]=right[j]
        j=j+1
      k=k+1
    if i == len(left):
      #set remaining entries in arr to remaining values in right
      for remain in right[j:]:
        arr[k] = remain
        k =k+ 1
    else:
        # set remaining entries in arr to remaining values in left
      for remain in left[i:]:
        arr[k] = remain
        k = k+1
