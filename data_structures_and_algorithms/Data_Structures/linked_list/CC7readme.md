# Challenge Summary
<!-- Description of the challenge -->
Add new methods; get k as argument , returns the node value this node is k number element from the end of the linked list.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![ll-kth-from-end](/img/ll-kth-from-end.PNG)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* I add new method for lenght , (single response),  function time big O(n) space big O(1) 
* method .kth_from_end() function time big O(n) space big O(1)

## API
kth_from_end(k)- method to find k-th value from the end of the linked list. In our implementation K can be positive or negative and list can be empty 

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
ll=LinkedList()
ll.insert('a')
ll.insert('50')
ll.append('last')# output // { 50 } -> { a } -> { last } -> NULL
ll.kthFromEnd(1)# output // a
```