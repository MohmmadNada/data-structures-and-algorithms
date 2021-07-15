# Merge Sort
 Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.



### Pseudo Code
```
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left
``` 
### Trace
Sample Array: [8,4,23,42,16,15]
pass1: Mergesort devides lists to half until reach one element 
![CC27](img/../../../../img/CC27/CC27_1.jpeg)
pass2: Merge start from left botton , order and marge 
Merge(left, right, arr)
![CC27](img/../../../../img/CC27/CC27_2.jpeg)
pass3
![CC27](img/../../../../img/CC27/CC27_3.jpeg)
pass4
![CC27](img/../../../../img/CC27/CC27_4.jpeg)
pass5
![CC27](img/../../../../img/CC27/CC27_5.jpeg)
pass6 : last marge call and the result is [4,8,15,16,23,42]
![CC27](img/../../../../img/CC27/CC27_6.jpeg)
### Efficency
* Space : Big O(n)
* time : Big O(n log n)

