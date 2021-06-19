from re import T
from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import Node
from data_structures_and_algorithms.stacks_and_queues.stacks_and_queues import Stack,Queue
import pytest

def test_enqueue(test_fixture):
    # Can successfully enqueue into a queue
    actual=test_fixture.enqueue('test')
    actual=test_fixture.rear.value
    excepted ='test'
    assert excepted==actual
def test_enqueue_multiple_values(test_fixture):
#Can successfully enqueue multiple values into a queue
    test_fixture.enqueue('test1')
    acual_1=test_fixture.rear.value#'test1
    except_1='test1'
    assert except_1==acual_1
    test_fixture.enqueue('test2')#'test2
    acual_2=test_fixture.rear.value
    except_2='test2'
    assert acual_2==except_2
def test_dequeue(test_fixture):
    #Can successfully dequeue out of a queue the expected value
    actual=test_fixture.dequeue()
    excepted='first'
    assert actual==excepted

def test_peek(test_fixture): 
#Can successfully peek into a queue, seeing the expected value
    actual=test_fixture.peek()
    excepted='first'
    assert actual==excepted

def test_empty_by_dequeues(test_fixture):
    #Can successfully empty a queue after multiple dequeues
    test_fixture.dequeue()
    test_fixture.dequeue()
    test_fixture.dequeue()
    actual=test_fixture.isEmpty()
    excepted=True
    assert actual==excepted

def test_instance_empty(): 
#Can successfully instantiate an empty queue
    q=Queue()
    actual=q.isEmpty()
    assert actual == True

def test_raise_exception(): 
#Calling dequeue or peek on empty queue raises exception
    QQ =Queue()
    with pytest.raises(Exception):
        QQ.dequeue()
    with pytest.raises(Exception):
        QQ.peek()
@pytest.fixture
def test_fixture():
    queue=Queue()
    queue.enqueue('first') #add from the end 
    queue.enqueue('second')
    queue.enqueue('third')# first(front) second third 
    return queue