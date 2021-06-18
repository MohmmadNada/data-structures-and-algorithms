# should add class node and LL from 
from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import Node,LinkedList
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
            return 'Oops , empty stock'
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


if __name__=='__main__':
    stock=Stack()
    print('---------')
    
    stock.push(5)
    stock.push('a')
    stock.push('50')
    stock.push('LIFO')
    print(stock.peek())
    # exception desont work 
