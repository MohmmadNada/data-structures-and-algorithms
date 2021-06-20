import pytest
from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import Node,Stack,PseudoQueue

# “Happy Path” - Expected outcome
def test_enqueue_empty(test_fixture):
    test_fixture.enqueue('firstIn')
    actual=test_fixture.first_stack.peek()
    excepted='firstIn'
    assert actual==excepted
def test_enqueue_NotEmpty(test_fixture):
    test_fixture.enqueue('notFirstIn')
    test_fixture.enqueue('topItem')
    actual=test_fixture.first_stack.peek()
    excepted='topItem'
    assert actual==excepted
    assert str(test_fixture)=='from the top => topItem => notFirstIn => NULL'

def test_dequeue_Empty(test_fixture):
    # Expected failure
    with pytest.raises(Exception):
        test_fixture.pop()

@pytest.fixture
def test_fixture():
    pseudo_queue=PseudoQueue()
    return pseudo_queue