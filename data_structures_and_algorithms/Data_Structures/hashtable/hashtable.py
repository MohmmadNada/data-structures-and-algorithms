class Node:
    '''Class for the Node instances'''
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    '''Method to instance a LinkedList'''
    def __init__(self):
        self.head = None
    def insert(self,value):
        '''insert new item into LinkedList , to head '''
        newNode=Node(value)# create node 
        if  self.head == None :
        # case 1 : empty LinkedList
            self.head = newNode
        else:
            # case 2 : empty LinkedList 
            # put the head => newnode.next => pre head 
            newNode.next = self.head
            self.head = newNode
    def __str__(self):
        values=[]
        current=self.head
        while current :
            values.append(current.value)
            current = current.next
        return f'=> {values} '

# - - ---- -- -- - - -- - -- -- - --- -- - -- --- -- -- ---- ---- ------ -hashtable part --------- -- - -- - - --

class Hashtable:

    def __init__(self,size=1024):
        # the size in memory is 2024 by defult 
        self.size = size
        self._array = [0 for i in range(size)]
        # self.map = [None]*size # [None, None, None, ....., None] size of 1024
 
    def hash(self,key):
        '''Method that takes in an arbitrary key and returns an index in the collection.'''
        key=str(key)
        sum_char=0 
        for letter in key:
            sum_char = sum_char + ord(letter)# ord retuen number from every letter 
        # get the index 
        index = (sum_char * 599) % self.size # 599 for security 
        return index 
    def add(self,key,value):
        '''input key and value to add it in specific address '''
        ''''This method should hash the key, and add the key and value pair to the table, handling collisions as needed.'''
        hshed_key= self.hash(key)# the index 
        # check if we have item in that address
        if  not self._array[hshed_key]:
            # empty index
            # create likedist
            ll=LinkedList()
            # add to ll
            # insert key and value as tuple  
            ll.insert((key,value))
            self._array[hshed_key]=ll
        else:
            # case we have linked list in that address 
            self._array[hshed_key].insert((key,value))
        # print('the hased index ',hshed_key)
    def get(self,key):
        '''get Value associated with that key in the hashe table'''
        # Arguments: key
        # Returns: Value associated with that key in the table
        # steps : 1. from key , get hashedkey = index , check if 
        hashed_key=self.hash(key) # index 
        if not self._array[hashed_key]:
            # emppty , no item 
            return None
        else:
            '''we have item in this address inside the linkedlist '''
            self._array[hashed_key]
            temp=self._array[hashed_key].head
            while temp:
                if temp.value[0] == key:
                    return temp.value[1]
                else:
                    temp=temp.next
            
    def contains(self,key):
        '''enter the key , if it exists , return true , if not , return flase'''
        hashed_key=self.hash(key)
        if self._array[hashed_key] == None : 
            return False
        else :
            return True
    
if __name__=='__main__':
    ht=Hashtable()
    # ht.add('ahmad', 25)
    # ht.add('hamad', 29) 
    # ht.add('silent', True)
    # ht.add('listen', 'Hey man')
    ht.add('nada', 'man')
    
    print(ht.get('silent'))
    # for index, item in enumerate(ht._array):
    #     if item:
    #         print(index, item)
