import re
from typing import Counter
from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList,Node
import pytest
'''
CC6 test /home/mohammad/401/data-structures-and-algorithms/data-structures-and-algorithms/data_structures_and_algorithms/Data_Structures/linked_list/linked_list.py
1. Can successfully add a node to the end of the linked list
2. Can successfully add multiple nodes to the end of a linked list
3. Can successfully insert a node before a node located i the middle of a linked list
4. Can successfully insert a node before the first node of a linked list
5. Can successfully insert after a node in the middle of the linked list
6. Can successfully insert a node after the last node of the linked list
    '''
ll=LinkedList()
ll.insert('a')
ll.insert('c')
ll.insert('d')
ll.insert('C2')#{ C2 } -> { d } -> { c } -> { a } -> NULL
def test_append(append_fixture):
    ll.append('last')
    assert str(ll)=='{ C2 } -> { d } -> { c } -> { a } -> { last } -> NULL'

def test_insert_before(append_fixture):
    ll.insertBefore('d','before')
    assert str(ll)=='{ C2 } -> { before } -> { d } -> { c } -> { a } -> { last } -> NULL'
    ll.insertBefore('d','beforebefore')
    assert str(ll)=='{ C2 } -> { before } -> { beforebefore } -> { d } -> { c } -> { a } -> { last } -> NULL'




@pytest.fixture
def append_fixture(): 
    ll=LinkedList()
    ll.insert('a')
    ll.insert('c')
    ll.insert('d')
    ll.insert('C2')#{ C2 } -> { d } -> { c } -> { a } -> NULL
    return ll