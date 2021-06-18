'''
CC5:
1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
2. Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
    * Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    * Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    * Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
3. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
4. Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
'''
from inspect import EndOfBlock, currentframe
import re

# from _pytest.python_api import raises


class Node:
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next Node(next).
    '''
    def __init__(self,value=None):
        self.value = value
        self.next = None  

class LinkedList:
    '''
    class for linked list instance 
    '''
#-----------------------------------------CC5----------------------------#

    def __init__(self):
        '''
        empty list should be created
        '''
        self.head = None

    def insert(self,value):
        '''
        we want to add a node with an O(1) efficiency, we have to replace the current Head of the linked list with the new node, without losing the reference to the next node in the list.
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node 
        
    def includes(self,value):
        '''
        takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        '''
        current = self.head #first node , we will loop through all nodes by add next 
        while  current :
            if current.value == value :
                return True    
            else :
                current = current.next
        return False # incase not found after all node 
    def __str__(self):
        '''
        takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        '''
        current =self.head 
        linkListString=''
        while True :
            if current != None:
                linkListString += '{ '+str(current.value)+' } -> ' 
                current=current.next
            elif current == None:
                linkListString +=  'NULL'
                break
        return linkListString
#-----------------------------------------CC6----------------------------#
    def append(self,value):
        '''
        adds a new node with the given value to the end of the list
        '''
        new_node=Node(value)
        current=self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_node
            new_node.next=None
        else :
            self.head=new_node      
    def insertBefore(self,value, newVal):
        '''
        add a new node with the given newValue immediately before the first value node
        '''
        if self.includes(value):
            current=self.head
            if current.value==value:
                new_node=Node(newVal)
                new_node.next=current
                self.head=new_node
            else:
                while current.next:
                    if current.next.value==value:
                        new_node=Node(newVal)
                        new_node.next=current.next
                        current.next=new_node
                        break
                    current=current.next
        else:
            return 'This item does not exist'
    def insertAfter(self,value, newVal):
        '''
        add a new node with the given newValue immediately after the first value node
        '''
        if self.includes(value):
            current=self.head
            while current :
                if current.value==value:
                    new_node=Node(newVal)
                    new_node.next=current.next
                    current.next=new_node
                    break
                elif current.next ==None:
                    new_node=Node(newVal)
                    current.next=new_node
                current=current.next
        else:
            return 'not found value to insert after it '
    def __len__(self):
        current = self.head
        length = 0
        while current:
                length+=1
                current=current.next
        return length
    def kthFromEnd(self,k):
        '''
        Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
        '''
        current = self.head
        length=len(self)
        # while current:
        #     length+=1
        #     current=current.next
        # current=self.head
        if not -length < k < length:
            raise Exception(' this K value is put of range ')
        else :
            if k<0:
                k=abs(k)
            steps= length-k-1
            for x in range(steps):
                current = current.next
            return current.value
        
        
if __name__=='__main__':
#     ll=LinkedList()#we create empty list new 
# #    #show what inside 
# #    print('********** head -> none')
# #    print(ll.head)#==>none
# #    print(ll.head.value,'----',ll.head.next)#==>a , none 
#     ll.insert('a')
#     ll.insert('50')
#     ll.insert('cc')
# # #    print(ll.head.value)#aa
# # #    print(ll.head.next.value)#a
# # #    print(ll.head.next.next)#none
# # #    print(ll.includes('c'))
# # #    print(ll.includes('b'))
# #    print('********** ********** * ** ** * ** ')
#     ll.append('last')
#     # print(str(ll))#{ cc } -> { 50 } -> { a } -> { last } -> NULL
#     ll.insertBefore('50','before')
#     # print(str(ll))#{ cc } -> { before } -> { 50 } -> { a } -> { last } -> NULL
#     ll.insertAfter('before','after')
#     # ll.insertAfter('beforess','after')# not found
#     # print('after insert\n',str(ll))#{ cc } -> { before } -> { after } -> { 50 } -> { a } -> { last } -> NULL
#     ll.insertAfter('last','after last')
#     print(str(ll))
#     print(ll.kthFromEnd(6))
    #     # ll.kthFromEnd(6)
    ll=LinkedList()
    ll.insert('a')
    ll.insert('50')
    ll.append('last')# { 50 } -> { a } -> { last } -> NULL
    print(str(ll))
    print('the lenght is --- ',len(ll))
    # print(ll.kthFromEnd(0))# { last } 
    # print(ll.kthFromEnd(1))# 
    # print(ll.kthFromEnd(2))# 
    # print(ll.kthFromEnd(3)) #{ 50 } 
    # print(ll.kthFromEnd(4)) # out of range
    # print(ll.kthFromEnd(10))
    # ll.insert('a')
    # ll.insert('0')
    # ll.insert('10')
    # actual=ll.kthFromEnd(0)
    