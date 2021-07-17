from hashtable import Node,LinkedList,Hashtable
import pytest

@pytest.fixture
def general_hashtable():
    ht=Hashtable()
    ht.add('name','age')
    ht.add('ahmad',22)
    ht.add('mohmmad',28)
    return ht
def test_add_hashtable():
    '''Adding a key/value to your hashtable results in the value being in the data structure'''
    ht=Hashtable()
    ht.add('nada',15)
    actual = ht._array[332].head.value
    excepted = ('nada',15)
    assert actual == excepted
def test_get_value(general_hashtable):
    '''Retrieving based on a key returns the value stored'''
    newHT=general_hashtable
    actual = newHT.get('mohmmad')
    excepted = 28
    assert actual == excepted
def test_get_value_not_exsit(general_hashtable):
    newHT=general_hashtable
    actual = newHT.get('ssssss')
    excepted = None
    assert actual == excepted
def test_handle_collision(general_hashtable):
    '''
    1. Successfully handle a collision within the hashtable
    2. Successfully retrieve a value from a bucket within the hashtable that has a collision

    '''
    newHT=general_hashtable
    newHT.add('ahmad','newAge')
    newHT._array[589]
    actual_1 = newHT._array[589].head.value
    actual_2 = newHT._array[589].head.next.value
    excepted_1 = ('ahmad','newAge')
    excepted_2 = ('ahmad',22)
    assert actual_1 == excepted_1
    assert actual_2 == excepted_2
def test_hash_key_inrange(): 
    '''Successfully hash a key to an in-range value
''' 
    newHT=Hashtable()
    index=newHT.hash(10)
    assert 0 <= index <= 1024
    index=newHT.hash('samed')
    assert 0 <= index <= 1024
    index=newHT.hash('ramosuper')
    assert 0 <= index <= 1024
    
