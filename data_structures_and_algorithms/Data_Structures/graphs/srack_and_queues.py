from ..linked_list.linked_list import Node
import re

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
