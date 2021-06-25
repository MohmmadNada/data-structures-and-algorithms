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
            # @pysnooper.snoop()  
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
        outputStr=''
        if node!=None:
            # left >> right >> root
            def _traverse(node):
                nonlocal outputStr
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)
                outputStr+=str(node.value)
                return outputStr
            _traverse(node)
        return outputStr







if __name__=='__main__':
    Btree=BinaryTree()
    # print(Btree.root)
    Btree.root=Node('rootItem ')
    # print('the root value is =>               ',Btree.root.value) # root 'rootItem'             
    Btree.root.right=Node('rightRoot ')
    Btree.root.left=Node('leftRoot ')
    rightRoot=Btree.root.right
    leftRoot=Btree.root.left
    # print(leftRoot.value, '                             ********                ',rightRoot.value)
    # print()
    leftRoot.left=Node('left_left ')
    leftRoot.right=Node('left_right ')
    rightRoot.left=Node('right_left ')
    rightRoot.right=Node('right_right ')
    rightRoot.right.right=Node('right_right_right ')
    # print(leftRoot.left.value , '     ',leftRoot.right.value, '         ***************         ',rightRoot.left.value,'     ',rightRoot.right.value)
    # print(Btree.preOrder())
    # Btree.inOrder()
    # print(Btree.inOrder())
    print(Btree.postOrder())
