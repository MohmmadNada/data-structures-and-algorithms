'''
1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
2. Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
    * Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    * Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    * Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
3. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
4. Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
'''
class Node:
    '''
    Class for the Node instances
    '''
    def __init__(self,value=None):
        self.value = value
        self.next = None       

class LinkedList:
    '''
    class for linked list instance 
    '''
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
        while current :
        
            linkListString += str(current.value)
            current=current.next
        return linkListString

if __name__=='__main__':
   ll=LinkedList()#we create empty list new 
   #show what inside 
   print('********** head -> none')
   print(ll.head)#==>none
   ll.insert('1111100')
   print('********** ')
   print(ll.head.value,'----',ll.head.next)#==>a , none 
   print('********** ')
   ll.insert('aa0')
   print(ll.head.value)#aa
   print(ll.head.next.value)#a
   print(ll.head.next.next)#none
   print('********** ********** * ** ** * ** ')
   print(ll.includes('a'))
   print(ll.includes('as'))
   print(str(ll))


