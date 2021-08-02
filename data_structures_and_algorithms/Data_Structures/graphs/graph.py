'''

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
Steps before :
1. class for Vertix(Node)
    * value
2. class for Edge
    * origin vertix 
    * weight
'''
# data_structures_and_algorithms/Data_Structures/stacks_and_queues/stack_and_queues.md
# from stacks_and_queues import Queue

import re

class Node:
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next Node(next).
    '''
    def __init__(self,value=None):
        self.value = value
        self.next = None  

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
        if self.front==None:
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
# // -----------------must be import 
class Vertix:
    def __init__(self,value):
        '''
        Vertix is container that have value
        '''
        self.value=value
    def __str__(self):
        return f'value > {self.value} '
class Edges:
    def __init__(self,vertix,weight=None):
        self.vertix = vertix
        self.weight = weight
class Graph:
    '''
    graph representes as an adjacency list
    '''
    def __init__(self):
        self.adjacency_list={}# dic : key the vertix and the value is array ot set with connect vertix

    def add_vertix(self,value):
        '''add new vertix with value as arg
        '''
        # 1. instances new vertix 
        newVertix = Vertix(value)
        # 2. Add a node to the graph # the vertix is key and the edges in list or set 
        self.adjacency_list[newVertix]=[]
        # 3. Returns: The added node
        return newVertix 
        # Arguments: value
    def add_adge(self,start_vertix,end_vertix,weight=None):
        '''Adds a new edge between two vertix in the graph with ability to add weight
        > Both nodes should already be in the Graph
        '''
        # 1. Arguments: 2 nodes to be connected by the edge, weight (optional)
        # 2. Both nodes should already be in the Graph
        if  start_vertix not in self.adjacency_list and end_vertix not in self.adjacency_list :
            raise KeyError('the first and secend vertices is not in the graph')
        elif start_vertix not in self.adjacency_list :
            raise KeyError('the first vertix is not in the graph')
        elif end_vertix not in self.adjacency_list :
            raise KeyError('the second vertix is not in the graph')

        # 2. Adds a new edge between two nodes in the graph
        self.adjacency_list[start_vertix]+=[{end_vertix:weight}]# its end_vertix not vertix.value
        # 2. Returns: nothing
        # 4. If specified, assign a weight to the edge
    def get_vertix(self):
        '''No argument needed;Returns all of the nodes in the graph as a collection list'''
        allVertices=list(self.adjacency_list.keys())
        
        return allVertices
    
    def get_neighbors(self,sourceVertix):
        '''Returns a collection of edges connected to the given node,Include the weight of the connection in the returned collection'''
        vertixKey=self.adjacency_list[sourceVertix] # [{VertixConnected: weight}, {VertixConnected: weight}]
        return vertixKey
    def size(self):
        '''Returns the total number of nodes in the graph'''
        return len(self.adjacency_list)
        # return self.adjacency_list
    def __str__(self):
        outPut=''# empty string 
        for vertix in self.adjacency_list:# loop throgh the vertix keys 
            outPut += str(vertix) + 'connect with =>  ' # add Node(vertix value) to outPut str
            for edge in self.adjacency_list[vertix]:# array with connect vertices and weights
                outPut+=str(list(edge.keys())[0])+' the weight is '+str(list(edge.values())[0]) + ' , '
                # print()
            outPut+='\n'
        return outPut
    def BreadthFirst(self,startVertix):
        '''takes Vertix as argument; Return: A collection of nodes in the order they were visited.
        '''
        if  startVertix not in self.adjacency_list :
            raise KeyError('The vertix is not in Graph ')
        # 1. defind return array, queue , and visisted set 
        nodes = []
        valueNodes = []
        breadth = Queue()
        visited= set()
        testvisited=set()
        # 2. add to queue and set
        breadth.enqueue(startVertix)
        visited.add(startVertix)
        testvisited.add(startVertix.value)
        # loop until queue is empty 
        while breadth.front != None:
            parentVertix=breadth.dequeue()
            nodes.append(parentVertix)# change it to [parentVertix.value] 
            valueNodes.append(parentVertix.value)# change it to [parentVertix.value] 
            childVertices= self.adjacency_list[parentVertix] # array with dic items {edges as key weight value}
            for child in childVertices:
                childVertix=list(child.keys())[0]
                if childVertix not in visited:
                    visited.add(childVertix)
                    testvisited.add(childVertix.value)
                    breadth.enqueue(childVertix)
        # print('visted => ', testvisited)
        # print('Node => ',nodes)
        # print('value Node => ',valueNodes)
        return nodes
        
        
if __name__=='__main__':
    # newGraph=Graph()
    # a=newGraph.add_vertix('A')# 1
    # b=newGraph.add_vertix('B')#2 
    # c=newGraph.add_vertix('C')#3
    # d=newGraph.add_vertix('D')#4
    # e=newGraph.add_vertix('E')#5
    # z=Graph().add_vertix('Z')#6
    # newGraph.add_adge(a,b,10)
    # newGraph.add_adge(a,e)
    # newGraph.get_neighbors(a)
    # # print(newGraph.size())
    # print(newGraph)
    # # print(newGraph.get_neighbors(a))
    # # print(newGraph)
    # newGraph=Graph()
    # a=newGraph.add_vertix('A')
    # b=newGraph.add_vertix('B') 
    # c=newGraph.add_vertix('C')
    # d=newGraph.add_vertix('D')
    # newGraph.add_adge(a,b,10)
    # newGraph.add_adge(a,c)
    # newGraph.add_adge(b,c)
    # newGraph.add_adge(c,d)
    # newGraph.BreadthFirst(a)
    # # print(newGraph.get_vertix())
    # test from CC37
    newGraph=Graph()
    Pandora = newGraph.add_vertix('Pandora')
    Arendelle = newGraph.add_vertix('Arendelle')
    Metroville = newGraph.add_vertix('Metroville')
    Monstroplolis = newGraph.add_vertix('Monstroplolis')
    Narnia = newGraph.add_vertix('Narnia')
    Naboo = newGraph.add_vertix('Naboo')
    newGraph.add_adge(Pandora,Arendelle)
    newGraph.add_adge(Arendelle,Metroville)
    newGraph.add_adge(Arendelle,Monstroplolis)
    newGraph.add_adge(Metroville,Narnia)
    newGraph.add_adge(Metroville,Naboo)
    newGraph.add_adge(Metroville,Monstroplolis)
    newGraph.add_adge(Monstroplolis,Monstroplolis)
    print(newGraph.BreadthFirst(Pandora))
    pass

