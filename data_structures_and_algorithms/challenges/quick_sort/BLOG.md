# Quick Sort
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

Always pick first element as pivot.
**Always pick last element as pivot (implemented below)**
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

### Pseudocode
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Trace
Sample Array: [8,4,23,42,16,15]

as shown in the figure, every coulmn shown the step and what happiend in the array 
![trace](/img/CC28/codechellange28_visual.PNG)

pass 1 :
from 0 to 5 index , pivot last element array[5]= 15
put it in the correct postion , left items value less than 15 and the right side have more values 
array= [8,4,15,42,16,23]
divids the left and right 
pass 2 : input 8,4 from 0 to 1 pivot = 4 

after sort 
array= [4,8,15,42,16,23]

pass 3 :  input 42,16,23 from 3 to 5 pivot = 23

after sort 
array= [4,8,15,16,23,42]

### Efficency
Time: O(n log n )

Space: O(1)
    * No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).


