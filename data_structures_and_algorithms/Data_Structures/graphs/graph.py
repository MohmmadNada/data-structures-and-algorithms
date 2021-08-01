'''

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
Steps before :
1. class for Vertix(Node)
    * value
2. class for Edge
    * origin vertix 
    * weight
'''

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
    Implement your own Graph. The graph should be represented as an adjacency list
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
        self.adjacency_list[start_vertix]+=[{end_vertix:weight}]# check of you need end_vertix.value or end_vertix 
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
    newGraph=Graph()
    a=newGraph.add_vertix('A')
    b=newGraph.add_vertix('B') 
    c=newGraph.add_vertix('C')
    newGraph.add_adge(a,b,10)
    newGraph.add_adge(a,c)
    newGraph.add_adge(b,c)
    print(newGraph.get_vertix())