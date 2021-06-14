# Singly Linked List
<!-- Short summary or background information -->
add new three method to LL calss to add new node in different postions
## Challenge
hard two deal with two class and get what are looking for , 
<!-- Description of the challenge -->
.append(value) which adds a new node with the given value to the end of the list
.insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
.insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
1. append function time big O(n) space O(1) constant 
2. insert_before function  ; time big O(n), loop ,  space O(1) for the 
3. insert_after function time big O(n) loop ,  space O(1) 

## API
<!-- Description of each method publicly available to your Linked List -->
1. append , add new node to the end 
2. insert before , add new node  before specific old node 
3. insert after , add new node  after specific old npde

white-board:
![img1](/img/CC6_1.PNG)
![img2](/img/CC6_2.PNG)
![img3](/img/CC6_3.PNG)

## Solution
<!-- Show how to run your code, and examples of it in action -->
 ll=LinkedList() #we create empty list new 
    ll.insert('a')
    ll.insert('50')
    ll.insert('cc')
    ll.append('last')
    output / print(str(ll))/ { cc } -> { 50 } -> { a } -> { last } -> NULL
    ll.insertBefore('50','before')
    print(str(ll))output/{ cc } -> { before } -> { 50 } -> { a } -> { last } -> NULL
    ll.insertAfter('before','after')
    print(str(ll))#{ cc } -> { before } -> { after } -> { 50 } -> { a } -> { last } -> NULL
    

