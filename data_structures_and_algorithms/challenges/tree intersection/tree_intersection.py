# 1. add all element from first binary tree in one array 
# 2. loop through the array and add loop to search in second binary tree , if exist add it to array  

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
    @staticmethod
    def breadthFirst (tree):
        if tree.root== None:
            return 'Empty Tree'
        else: 
            resultValues ,tempNodes = [],[]
            tempNodes.append(tree.root)
            resultValues.append(tree.root.value)
            currentNode = tree.root
            while currentNode:
                tempNodes.pop(0) 
                if currentNode.left:
                    resultValues.append(currentNode.left.value)
                    tempNodes.append(currentNode.left)
                if currentNode.right:
                    resultValues.append(currentNode.right.value)
                    tempNodes.append(currentNode.right)
                if len(tempNodes)==0:
                    break
                currentNode = tempNodes[0]
                
            return (resultValues)
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
                if checkValue < current.value:
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

'''
# PESUDO CODE  :

ALGORITHM treeInserction(tree1,tree2) do
   treeelements=traverseTree(tree)
   for i <- 0 to treeelements.length-1 do
    checkElement = treeelements[0].value
          current=root2
   commonElement = []
   while current do
    if checkElement ==current.value
                  commonElement.append(current.value)
               if checkElement< current.value do
     if current.left do
       current = current.left
     else:
      break
    if checkElement> current.value do
       if current.right do
             current = current.right
          else:
            break
'''
def preOrder(tree):
    '''
        return all value from tree as an array  , start reading from top to bottom ,root => left => right.
    '''
    outputArr=[]
    if tree.root == None:
        '''
        1. empty tree ; return empty array  
        '''
        return outputArr

    else:
        '''
        2. not empty tree case; loop and add all in array  
        '''
        def _traverse(node=tree.root): # 3. def _traverse function
            nonlocal outputArr
            outputArr.append(node.value)#4.  append node in array 
            if node.left: # 5. check of we have left call the function 
                _traverse(node.left)
            if node.right:# 6. check of we have right call the function 
                _traverse(node.right)
            return outputArr# 7. return the array 
        _traverse()# 4. call _traverse function
    return outputArr
def treeInserction(bt1,bt2):
    '''Find all values found to be in 2 binary trees'''
    firstArrItems = preOrder(bt1)
    secondArrItems = preOrder(bt2)
    commonNumbers=[]
    for x in firstArrItems:
        if x in secondArrItems:
            if not x in commonNumbers:
                commonNumbers.append(x)
    return commonNumbers
            
# if __name__=='__main__':
#     BT=BinarySearch()
#     BT.root=Node(150)
#     BT.root.left=Node(100)
#     BT.root.left.left=Node(75)
#     BT.root.left.right=Node(160)
#     BT.root.left.right.left=Node(125)
#     BT.root.left.right.right=Node(175)
#     BT.root.right=Node(250)
#     BT.root.right.left=Node(200)
#     BT.root.right.right=Node(350)
#     BT.root.right.right.left=Node(300)
#     BT.root.right.right.right=Node(500)
#     # print(preOrder(BT))# [150, 100, 75, 160, 125, 175, 250, 200, 350, 300, 500]
#     BT2=BinarySearch()
#     BT2.root=Node(42)
#     BT2.root.left=Node(100)
#     BT2.root.left.left=Node(15)
#     BT2.root.left.right=Node(160)
#     BT2.root.left.right.left=Node(125)
#     BT2.root.left.right.right=Node(175)
#     BT2.root.right=Node(600)
#     BT2.root.right.left=Node(200)
#     BT2.root.right.right=Node(350)
#     BT2.root.right.right.left=Node(4)
#     BT2.root.right.right.right=Node(500)
#     # print(preOrder(BT2))# [42, 100, 125, 175, 600, 200, 350, 4, 500]

#     print(treeInserction(BT,BT2))