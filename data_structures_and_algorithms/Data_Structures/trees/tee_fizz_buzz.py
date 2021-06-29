''' Problem domain 
Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.

Set the values of each of the new nodes depending on the corresponding node value in the source tree.
def = > class Node with value and array child 
def = > class k_ary_tree  and method for traverse
'''
'''
Feature Tasks
Write a function called fizz buzz tree
Arguments: k-ary tree
Return: new k-ary tree
# Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

* If the value is divisible by 3, replace the value with “Fizz”
* If the value is divisible by 5, replace the value with “Buzz”
* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
* If the value is not divisible by 3 or 5, simply turn the number into a String.
* Limit the list items
    # # if len(ar) > 10:
    #   raise Exception('Items exceeds the maximum allowed length of 10')
'''
# 1. Node Class 
class Node:
    '''
    Node class that has properties for the value stored in the Node, and a pointer to his childs Node.
    '''
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.Children=[]
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
        try:
            if self.rear==None:
                raise Exception('THIS Queue is Empty')
            else:
                if self.front==self.rear:
                    temp=self.front
                    self.front=self.front.next
                    temp.next=None
                    self.rear=None
                    # print('from 63')
                else:
                    temp=self.front
                    self.front=self.front.next
                    temp.next=None
            return temp.value
        except ValueError:
            return 'Oops  , empty Queue'
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
class k_ary_tree:

    def __init__(self,k):
        self.root=None
        self.maxNumbersOfChildern=k


def  fizz_buzz_tree(tree):
    ''' * Write a function called fizz buzz tree
        * Arguments: k-ary tree
        * Return: new k-ary tree
    '''
    def cahngeValue(value):
        value=int(value)
        if value%3==0 and value%5==0:
            return 'Fizz Buzz'
        elif value%3==0:
            return 'Fizz'
        elif value%5==0:
            return 'Buzz'
        else:
            return str(value)

    k=tree.maxNumbersOfChildern
    newKtree=k_ary_tree(k)
    queue=Queue()
    if tree.root:# not empty tree
        currentNode=tree.root
        newValue=cahngeValue(currentNode.value)
        newKtree.root=Node(newValue)
        newTreeLevel=newKtree.root.Children# array 
        queue.enqueue(currentNode)
        while not queue.isEmpty():# not empty queue
            queue.dequeue()# this return value , should I start from it ? 
            if len(currentNode.Children)!=0:
                for childNodes in currentNode.Children:
                    print(childNodes.Children.append())
                    # newTreeLevel.Children.append(Node(cahngeValue(childNodes.value)))
                    # queue.enqueue(childNodes)
                # currentNode=queue.front.value
                # newTreeLevel=newTreeLevel.Children


    else: 
        return newKtree
         

    
if __name__=='__main__':
    kTree= k_ary_tree(3)
    kTree.root=Node('10')
    kTree.root.Children.append(Node('15'))# empty list 
    kTree.root.Children.append(Node('20'))
    kTree.root.Children.append(Node('25'))
    # FIRST LEVEL   [B  C  D]
    kTree.root.Children[0].Children.append(Node('50'))# [E  F ]
    kTree.root.Children[0].Children.append(Node('100'))
    kTree.root.Children[1].Children.append(Node('150'))
    kTree.root.Children[2].Children.append(Node('200'))
    print(fizz_buzz_tree(kTree))



'''
first version traverse 

def  fizz_buzz_tree(tree):

    
    k=tree.maxNumbersOfChildern
    newKtree=k_ary_tree(k)
    queue=Queue()
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