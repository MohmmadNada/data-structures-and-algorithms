from _pytest.outcomes import Skipped
# import re
# from typing import Counter
import pytest
from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList,Node

def test_k_equal_length():
    # Where k and the length of the list are the same
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    assert ll.kthFromEnd(3)==5
    
def test_k_greater_than_length():
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    with pytest.raises(Exception):  # Pass in the expected error
        ll.kth_from_end(10)

def test_k_not_positive_out_range():
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    with pytest.raises(Exception):  # Pass in the expected error
        ll.kth_from_end(-10)

def test_k_not_positive_in_range():
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    assert ll.kthFromEnd(-2)==10
def test_k_lenght_equal_1():
    ll=LinkedList()
    ll.append('a')
    assert ll.kthFromEnd(0)=='a'
def test_k_in_middle():
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    assert ll.kthFromEnd(1)==150

@pytest.fixture
def test_fixture_01():
    ll=LinkedList()
    ll.append(5)# 5 -> none
    ll.append(10)# 5 -> 10 -> none
    ll.append(150)# 5 -> 10 -> 150 -> none
    ll.append(10)# 5 -> 10 -> 150 -> 10 -> none
    return ll