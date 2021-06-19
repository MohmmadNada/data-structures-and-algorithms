# Stacks and Queues
<!-- Short summary or background information -->
Add new Classes 1. stock that have nodes , ponit to next node , and deal with it by LIFO .
                2. Queue Ckass , that have numbers of nodes , deal with it from front and rear , LIFO
<!-- Description of the challenge -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
add new Node class , and use it in every method in stock and queue , Big O(1). constant space used and time.
## API
<!-- Description of each method publicly available to your Stack and Queue-->
#### Stock
    1. push: add new node to top sock 
    2. pop: remove from the top 
    3. peek: return top value 
    4. isEmpty: return true or false , if empty or noy 
#### Queue 
    1. enqueue: add new node to the back 
    2. dequeue: remove node from front
    3. peek: return front node value
    4. isEmpty: return true(incase empty queue) or flase (incase not empty)