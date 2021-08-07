from graph_business_trip import *
import pytest
def test_empty_list():
    newGraph=Graph()
    
    newGraph.add_vertix('N2')
    assert businesstTrip(newGraph,[]) ==None
def test_happy_path():
    newGraph=Graph()
    
    B = newGraph.add_vertix('B')
    M = newGraph.add_vertix('M')
    M2 = newGraph.add_vertix('M2')
    N2 = newGraph.add_vertix('N2')
    N = newGraph.add_vertix('N')
    
    newGraph.add_adge(B,M2,42)
    newGraph.add_adge(M,M2,105)
    newGraph.add_adge(N2,M2,73)
    newGraph.add_adge(N,N2,250)
    excepted =178
    assert businesstTrip(newGraph,['N2','M2','M'])==excepted  
def test_city_not_in_graph():
    newGraph=Graph()
    B = newGraph.add_vertix('B')
    M = newGraph.add_vertix('M')
    M2 = newGraph.add_vertix('M2')
    N2 = newGraph.add_vertix('N2')
    N = newGraph.add_vertix('N')
    newGraph.add_adge(B,M2,42)
    newGraph.add_adge(M,M2,105)
    newGraph.add_adge(N2,M2,73)
    newGraph.add_adge(N,N2,250)
    # actual=businesstTrip(newGraph,['N2','M2','M','not in'])
    with pytest.raises(ValueError):
        businesstTrip(newGraph,['N2','M2','M','not in'])