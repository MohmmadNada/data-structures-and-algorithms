import pysnooper
import re


'''
* Create a Binary Tree class
    Define a method for each of the depth first traversals:
        pre order
        in order
        post order which returns an array of the values, ordered appropriately.
* Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
Structure and Testing

* Done
* Done
* Done
* Done
* Can successfully return a collection from an inorder traversal
* Can successfully return a collection from a postorder traversal

'''

# depth first , pre order , from last depth , from left to right , use recursion

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class Queue :
    def __init__(self):
        '''
        This object should be aware of a default empty value assigned to front when the queue is created.
        '''
        self.front=None
        self.rear=None
    def enqueue(self,value):
        '''
         takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''
        newNode=Node(value)
        if self.rear==None:
            self.rear=newNode
            self.front=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    def dequeue (self):
        '''
        Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value. Should raise exception when called on empty queue
        '''
        # try:
            # if self.rear==None:
            #     raise Exception('THIS Queue is Empty')
            # else:
        if self.front==self.rear:
            temp=self.front
            temp.next=None
            self.front=None
            self.rear=None
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
        return temp.value
        # except ValueError:
        #     return 'Oops  , empty Queue'
    def peek(self):
        '''
        does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue. Should raise exception when called on empty queue
        '''
        try:
            if self.front==None:
                raise Exception('Oop`s This Queue is Empty ')
            else:
                temp=self.front
                return temp.value
        except AttributeError:
            return 'the queue is empty '
    def isEmpty(self):
        '''
        Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
        '''
        if self.front==None:
            return True
        else:
            return False

class BinaryTree:
    def __init__(self):
        self.root=None
    def preOrder(self):
        '''
        return all value from tree , start reading from top to bottom , left to right.
        '''
        outputStr=''
        if self.root ==None:
            '''
            empty tree 
            '''
            return ''

        else:
            '''
            not empty tree case . 
            '''
            def _traverse(node=self.root):
                nonlocal outputStr
                outputStr+= str(node.value)
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                return outputStr
            _traverse()
        return outputStr
    def inOrder(self):
        node = self.root
        outputStr=''
        if self.root==None:
            return ''
        else: 
              
            def _traverse(node):
                nonlocal outputStr
                if node.left:
                    _traverse(node.left)
                outputStr+=str(node.value)
                if node.right:
                    _traverse(node.right)
            _traverse(node)
        return outputStr
    def postOrder(self):
        node=None or self.root 
        # outputStr=''
        outputArr=[]
        if node!=None:
            # left >> right >> root
            def _traverse(node):
                nonlocal outputArr
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                outputArr=outputArr+ [str(node.value)]
                return outputArr
            _traverse(node)
        return outputArr
    def find_max_value(self):
        '''
        find maximum value
        Arguments: none
        Returns: number
        Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
        '''
        outputArr=[]
        if self.root ==None:
            '''
            empty tree 
            '''
            return 'Oops, empty binary tree '

        else:
            '''
            not empty tree case . 
            '''
            def _traverse(node=self.root):
                nonlocal outputArr
                outputArr.append(node.value)
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                return outputArr
            _traverse()
        return max(outputArr)
def breadthFirst (tree):
    if tree.root==None:
        return 'Empty Tree'
    else: # in case not empty  
        queue=Queue()
        nodesList=[]
        currentNode=tree.root# node 2       keep in mind ,queue.front.value.value  queue.front.value.left
        queue.enqueue(currentNode)
        nodesList.append(queue.front.value.value)
        while not queue.isEmpty():
            queue.dequeue()
            if currentNode.left:
                queue.enqueue(currentNode.left)
            if currentNode.right:
                queue.enqueue(currentNode.right)
            if queue.front:
                currentNode=queue.front.value
                nodesList.append(currentNode.value)
        return nodesList
        
'''
first version traverse 

def  fizz_buzz_tree(tree):


if tree.root:# not empty tree
    currentNode=tree.root
    queue.enqueue(currentNode)
    while not queue.isEmpty():# not empty queue
        queue.dequeue()
        if len(currentNode.Children)!=0:
            for childNodes in currentNode.Children:
                queue.enqueue(childNodes)
            currentNode=queue.front.value
        

else: 
    return newKtree
'''

# Binary Search Tree method needs ; Add and Contains
class BinarySearch(BinaryTree):
    # make the child class inherit all the methods and properties from its parent
    # @pysnooper.snoop()
    def add(self,value):
        ''' Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
        '''
        if type(value)!= type(5):
            raise Exception('this value not number type , please input number only')
        if self.root == None:
            # Case : empty Tree
            newNode=Node(value)
            self.root=newNode
        elif self.root != None:
            # Case : we Have not empty Tree 
            newNode=Node(value)            
            current=self.root
            while True:
                if newNode.value <= current.value:
                    # less or equal , Go left side 
                    if current.left:
                        current=current.left
                        continue
                    else: 
                        current.left=newNode
                        break
                if newNode.value > current.value:
                    if current.right:
                        current=current.right
                        continue
                    else: 
                        current.right=newNode
                        break
    def contains(self,value):
        '''
        * Argument: value
        * Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        if type(value)!= type(5):
            raise Exception('this value not number type , please input number only')
        checkValue=value # check with node.value
        if self.root==None:
            return False
        elif self.root != None:
            current=self.root
            while True:
                if current.value == checkValue:
                    return True # will break the loop automaticly
                if checkValue <= current.value:
                    if current.left:
                        current=current.left
                        continue
                    else: # no left 
                        return False
                if checkValue > current.value:
                    if current.right:
                        current=current.right
                        continue
                    else:# no right
                        return False



if __name__=='__main__':
    # # Btree=BinaryTree()
    # BST=BinarySearch()
    # BST.root=Node(23)
    # BST.root.left=Node(8)
    # BST.root.right=Node(42)
    # leftRoot=BST.root.left# 8
    # rightRoot=BST.root.right# 42
    # leftRoot.left=Node(4)
    # leftRoot.right=Node(16)
    # leftRoot.right.left=Node(15)
    # leftRoot.right.right=Node(22)
    # BST.root.right.left=Node(27)# 42 27 
    # BST.root.right.right=Node(85)
    # BST.root.right.right.right=Node(105)
    # # print(BST.add('15')) # self.root = None ???
    # print(BST.postOrder()) # 4815162223274285105
    # # print(BST.contains(100))
    # -------------- CC 17 
    Btree=BinaryTree()
    Btree=BinaryTree()
    Btree.root=Node(2)
    Btree.root.left=Node(7)
    Btree.root.left.left=Node(2)
    Btree.root.left.right=Node(6)
    Btree.root.left.right.right=Node(11)
    Btree.root.left.right.left=Node(5)
    Btree.root.right=Node(5)
    Btree.root.right.right=Node(9)
    Btree.root.right.right.left=Node(4)
    print(breadthFirst(Btree))

