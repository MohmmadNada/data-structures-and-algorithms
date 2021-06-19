from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import Node
from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import Stack
import pytest
 

def test_push(test_fixture):# LIFO(top)   50   a    5 
    # Can successfully push onto a stack
    test_fixture.push('head?')#head? LIFO(top)   50   a    5 
    actual=test_fixture.peek()
    excepted='head?'
    assert actual==excepted
def test_push_multi(test_fixture):# LIFO(top)   50   a    5 
    # Can successfully push multiple values onto a stack
    test_fixture.push('new1')#new1 LIFO(top)   50   a    5 
    excepted01='new1'
    actual01=test_fixture.peek()
    assert actual01 == excepted01
    test_fixture.push('new2')#new2 new1 LIFO(top)   50   a    5 
    excepted='new2'
    actual=test_fixture.peek()
    assert actual == excepted
def test_pop(test_fixture):# LIFO(top)   50   a    5 
    # Can successfully pop off the stack
    test_fixture.pop()# (top)   50   a    5 
    actual=test_fixture.peek()# new2 new1 LIFO   50   a    5 
    excepted ='50'
    assert excepted==actual
def test_pop_empty(test_fixture):
    # Can successfully empty a stack after multiple pops
    test_fixture.pop()
    test_fixture.pop()
    test_fixture.pop()
    test_fixture.pop()
    actual01=test_fixture.isEmpty()
    excepted=True
    assert actual01==excepted
def test_peek_next_item(test_fixture):# LIFO(top)   50   a    5 
# Can successfully peek the next item on the stack
    actual=test_fixture.peek()
    excepted='LIFO'
    assert excepted==actual
def test_empty_stock():
    # Can successfully instantiate an empty stack
    stack=Stack()
    actual=stack.isEmpty()
    assert actual==True

def test_raise_exception():
# Calling pop or peek on empty stack raises exception
    stack=Stack()
    actual=stack.pop()
    excepted='Oops , empty stock'
    assert excepted ==actual

@pytest.fixture
def test_fixture():
    stock=Stack()
    stock.push(5)
    stock.push('a')
    stock.push('50')
    stock.push('LIFO')# LIFO(top)   50   a    5 
    return stock