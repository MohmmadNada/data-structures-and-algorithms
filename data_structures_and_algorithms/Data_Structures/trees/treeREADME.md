# Trees
<!-- Short summary or background information -->
add tree datastructure , 1. Binary , which take max child nodes = 2 , use recursion method , to out put the nodes value with specific arrangement , preOrder ,inOrder and postOrder
    2. BinarySearch class , tree which contains , number only ,always the left node is less than right .
     with add method , add ; add nodes in specific way adn contain , return true (in case we have this value)or false(in case we have not  this value)  
## Challenge
<!-- Description of the challenge -->
Create a Binary Tree class with methods pre_order, in_order and post_order Create a BinarySearch class with methods add(value) and contains(value)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Binary Tree ; recursion and stack the nodes. Big O(n)
BST; while loop and break when find Big O(h) , space Big O(n)

## API
<!-- Description of each method publicly available in each of your trees -->
BinaryTree - preOrder :return string with oreder root left right 
BinaryTree - inOrder :return string with oreder  left root right 
BinaryTree - postOrder :return string with oreder  left  right root
BinarySearch -add :Adds a new node with that value in the correct location in the binary search tree.
BinarySearch -contains :Returns: boolean indicating whether or not the value is in the tree at least once.