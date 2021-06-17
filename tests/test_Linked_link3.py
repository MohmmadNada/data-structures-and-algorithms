from _pytest.outcomes import Skipped
from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList,Node
import pytest
ll=LinkedList()
ll=LinkedList()
ll.insert('a')
ll.insert('0')
ll.insert('10')
# def test_kthFromEnd_equal_lengh(test_fixture):
#     '''
#     Where k and the length of the list are the same 
#     '''
#     ll.insert('a')
#     ll.insert('0')
#     ll.insert('10') #{ 10 } -> { 0 } -> { a } -> NULL
#     actual=ll.kthFromEnd(0)
#     assert actual == 1
def test_k_greter_than_length(test_fixture):
    '''
    Where k is greater than the length of the linked list
    '''
    # ll.kthFromEnd(100)
    with pytest.raises(Exception):  # Pass in the expected error
        ll.kth_from_end(-100)

def test_k_equal_length(test_fixture):
    '''
    Where k and the length of the list are the same
    '''
    # ll.kthFromEnd(2)
    # assert ll.kthFromEnd(5)=='10'
    pass
def test_negative_integer():
    # Where the linked list is of a size 1
    ll=LinkedList()
    ll.insert('a')
    ll.append('a')
    assert ll.kthFromEnd(0)
# @pytest.fixture
# def test_fixture():
#     ll=LinkedList()
#     ll.insert('a')
#     ll.insert('0')
#     ll.insert('10')
#     return ll