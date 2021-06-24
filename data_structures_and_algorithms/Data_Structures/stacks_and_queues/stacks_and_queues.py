# should add class node and LL from 
from ..linked_list.linked_list import Node,LinkedList
import re
# from tests.test_stacks import test_empty_stock
# import sys
# sys.path.append('linked_list/linked_list.py')
# import Node,LinkedList
# class Node :
#     '''
#     Node class that has properties for the value stored in the Node, and a pointer to the next node.
#     '''
#     def __init__(self,value):
#         self.value=value
#         self.next=None

class Stack :
    '''
    Stack class that has a top property. It creates an empty Stack when instantiated.
    '''
    def __init__(self):
        '''
        default empty value assigned to top when the stack is created.
        '''
        self.top=None

    def push(self,value):
        '''
        takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
        '''
        newNode=Node(value)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        '''
        1. not take any argument, removes the node from the top of the stack, and returns the node’s value.
        2. Should raise exception when called on empty stack or check isEmpty() first 
        '''
        # try:
        if self.isEmpty()==True:
            return 'Oops , empty stock'
        else:
            temporary=self.top
            self.top=self.top.next
            temporary.next=None
            return temporary.value
   
        # except AttributeError:
        #     print('This value desn`t in Stack elements')
  
    def peek(self):
        '''
        1. does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack
        2. Should raise exception when called on empty stack
        '''
        if self.isEmpty()==True:
            raise Exception('Oops , empty stock')
        # if self.top.value:
        else:
            temporary=self.top
            if temporary.value==None:
                return 'this stock is empty'
            return temporary.value
        # else:
        #     raise Exception(' this K value is put of range ')

    def isEmpty(self):
        '''
        takes no argument, and returns a boolean indicating whether or not the stack is empty.
        '''
        temp=self.top
        if temp == None:
            return True
        else:
            return False

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
if __name__=='__main__':
    # stock=Stack()
    # print('---------')
    
    # stock.push(5)
    # stock.push('a')
    # stock.push('50')
    # stock.push('LIFO')
    # print(stock.peek())
    # # exception desont work 
    queue=Queue()
    print('is it true ?',queue.isEmpty())
    # print('------- raise--- ',queue.peek())# front aa   
    queue.enqueue('a')# a=front
    queue.enqueue('aa')# front a  aa
    queue.enqueue('0')# front a  aa 0 
    print(queue.front.value)
    print(queue.front.next.value)
    print(queue.front.next.next.value)
    print('----',queue.dequeue()) # front aa 0 
    print('------- peek --- ',queue.peek())# front aa
    print('is it true ?',queue.isEmpty())
