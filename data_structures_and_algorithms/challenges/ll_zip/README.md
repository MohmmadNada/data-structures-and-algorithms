# Challenge Summary
<!-- Description of the challenge -->
Add new methods; get two Linked Lists as arguments , returns new Linkedlist have all nodes from arg  as zigzag .

## Whiteboard Process
<!-- Embedded whiteboard image -->
![ll_zip](/img/ll_zip.PNG)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O time and space O(n) , depand on lenght
## Solution
<!-- Show how to run your code, and examples of it in action -->
[code link ](https://github.com/MohmmadNada/data-structures-and-algorithms/blob/ll-zip/data_structures_and_algorithms/challenges/ll_zip/ll_zip/ll_zip.py)
```
    ll_1=LinkedList()
    ll_1.append('5')
    ll_1.append('-1')
    ll_1.append('-11')
    ll_1.append(1111)
    ll_1.append('05')
    ll_1.append('stright')
    ll_1.append('stright1')
    ll_2=LinkedList()
    ll_2.append('start')
    ll_2.append('2')
    ll_2.append(' sss ')
    ll_2.append('done ')
    print(' linked list first arg :    ',ll_2) #output// { start } -> { 2 } -> {  sss  } -> { done  } -> NULL
```