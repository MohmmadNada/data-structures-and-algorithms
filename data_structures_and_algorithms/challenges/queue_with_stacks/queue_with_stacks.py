'''
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:
'''
import re
from typing import Counter


class Node :
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next node.
    '''
    def __init__(self,value):
        self.value=value
        self.next=None
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
        if self.top==None:
        # if self.isEmpty()==True:
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
        # if self.isEmpty()==True:
        if self.top==None:
            raise Exception('Oops , empty stock')
        else:
            temporary=self.top
            if temporary.value==None:
                return 'this stock is empty'
            return temporary.value
        # else:
        #     raise Exception(' this K value is put of range ')


class PseudoQueue: # Stack LIFO queue FILO we want queue to be LIFO
    '''
    implement our standard queue interface (the two methods listed below)
    '''
    def __init__(self):
        self.first_stack= Stack()
        self.second_stack=Stack()
    def enqueue(self,value):
        '''
        inserts value into the PseudoQueue, using a first-in, first-out approach.
        '''
        self.first_stack.push(value)
    def dequeue(self):
        '''
        extracts a value from the PseudoQueue, using a first-in, first-out approach.
        '''
        if self.first_stack.top!=None:
            #Not empty stack
            while self.first_stack.top!=None:
                pop_element=self.first_stack.pop()
                self.second_stack.push(pop_element) 
            last_element=self.second_stack.pop()# will return the last element from the main stack
                # new we need to push every element from second to first stack 
            if self.first_stack.top==None:
                while self.second_stack.top!=None:
                    popElement=self.second_stack.pop()
                    self.first_stack.push(popElement)
            return last_element
        else:
            #Not empty stack
            raise Exception('Oops; Empty Stack')
    def __str__(self):
        current=self.first_stack.top
        allItemsString='from the top => '
        while True:
            if(current!=None):
                allItemsString+=str(current.value)+' => '
                current=current.next
            elif current==None:
                allItemsString+= 'NULL'
                break
        return allItemsString

if __name__=='__main__':
    pseudo_queue_init=PseudoQueue()# instance
    pseudo_queue_init.enqueue('first')
    pseudo_queue_init.enqueue('2')# last in first out in normal stack
    pseudo_queue_init.enqueue('second')# last in first out in normal stack
    # print(pseudo_queue_init.first_stack.top.value)
    # print('the peek value',pseudo_queue_init.first_stack.peek())
    print(str(pseudo_queue_init))
    print('----------------------before pop -------------- from last ')
    print(' we poped === ',    pseudo_queue_init.dequeue())
    print(str(pseudo_queue_init))
