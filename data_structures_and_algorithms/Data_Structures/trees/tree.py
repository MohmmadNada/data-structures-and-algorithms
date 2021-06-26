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
    # Btree=BinaryTree()
    BST=BinarySearch()
    BST.root=Node(23)
    BST.root.left=Node(8)
    BST.root.right=Node(42)
    leftRoot=BST.root.left# 8
    rightRoot=BST.root.right# 42
    leftRoot.left=Node(4)
    leftRoot.right=Node(16)
    leftRoot.right.left=Node(15)
    leftRoot.right.right=Node(22)
    BST.root.right.left=Node(27)# 42 27 
    BST.root.right.right=Node(85)
    BST.root.right.right.right=Node(105)
    # print(BST.add('15')) # self.root = None ???
    print(BST.postOrder()) # 4815162223274285105
    # print(BST.contains(100))
  