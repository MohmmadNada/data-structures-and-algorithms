# Selection Sort
Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

## Pseudocode
```
SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1  
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
```
## Trace
sample :[8,4,23,42,16,15]
![whiteBoard](./../../../img/cc26/CC26_1.jpeg)
![whiteBoard](./../../../img/cc26/CC26_2.jpeg)
![whiteBoard](./../../../img/cc26/CC26_3.jpeg)
![whiteBoard](./../../../img/cc26/CC26_4.jpeg)

## Efficency
Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).