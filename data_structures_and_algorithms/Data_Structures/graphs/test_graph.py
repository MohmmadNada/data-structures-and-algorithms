from _pytest.python_api import ApproxScalar, approx
import pytest
from graph import Graph

@pytest.fixture
def basicGraph():
    newGraph=Graph()
    a=newGraph.add_vertix('A')
    b=newGraph.add_vertix('B') 
    c=newGraph.add_vertix('C')
    newGraph.add_adge(a,b,10)
    newGraph.add_adge(a,c)
    newGraph.add_adge(b,c)
    return newGraph

def test_add_vertix():
    '''Node can be successfully added to the graph'''
    newGraph=Graph()
    actual=newGraph.add_vertix('A')# value > A connect with =>  value > B  the weight is 10 , value > E  the weight is None ,
    excepted = 'A'
    assert actual.value==excepted
def test_get_neighbors():
    '''An edge can be successfully added to the graph'''
    '''The proper size is returned, representing the number of nodes in the graph'''
    newGraph=Graph()
    vertixA=newGraph.add_vertix('A')
    vertixB=newGraph.add_vertix('B')
    newGraph.add_adge(vertixA,vertixB,50)
    actual= newGraph.get_neighbors(vertixA)
    actual1=len(actual)
    excepted1= 1
    assert list(actual[0].keys())[0].value =='B'
    assert  actual1 ==excepted1

def test_all_verices():
    '''A collection of all nodes can be properly retrieved from the graph'''
    '''All appropriate neighbors can be retrieved from the graph'''
    '''Neighbors are returned with the weight between nodes included'''
    newGraph=Graph()
    a=newGraph.add_vertix('A')
    b=newGraph.add_vertix('B') 
    # c=newGraph.add_vertix('C')
    newGraph.add_adge(a,b,10)
    # newGraph.add_adge(a,b)
    # newGraph.add_adge(b,c)
    assert str(newGraph)=="value > A connect with =>  value > B  the weight is 10 , \nvalue > B connect with =>  \n"

def test_graph_with_one_vertix():
    '''A graph with only one node and edge can be properly returned'''
    newGraph=Graph()
    a=newGraph.add_vertix('A')
    assert newGraph.get_neighbors(a)==[]
    listVertic=newGraph.get_vertix()
    assert listVertic[0].value=='A'

def test_all_vertices(basicGraph):
    actual=basicGraph.get_vertix()
    excepted = ['A','B','C']
    i=0
    for vertix in actual :
        assert vertix.value == excepted[i]
        i+=1
def test_empty_graph():
    '''An empty graph properly returns null'''
    newGraph=Graph()
    assert newGraph.size()==0