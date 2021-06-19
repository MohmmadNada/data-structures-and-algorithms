from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList,Node
'''
1. Can successfully instantiate an empty linked list (Done)
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list

4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list
'''
def test_instantiate_empty_linked_list():
    '''
    instantiate an empty linked list
    head = null
    '''
    actual = LinkedList().head
    axept = None
    assert actual == axept

def test_insert_into_empty_linked_list():
    '''
    Can properly insert into the linked list
    '''
    ll=LinkedList()
    val=50
    ll.insert(val)
    actual_1=ll.head.value
    actual_2=ll.head.next
    except_1 = 50
    except_2 = None
    assert actual_1==except_1
    assert actual_2==except_2

def test_head_point():
    '''
    3. The head property will properly point to the first node in the linked list
    4. Can properly insert multiple nodes into the linked list
    '''
    ll= LinkedList()
    node_1 = ll.insert('10')
    assert ll.head.value == '10'
    node_2 = ll.insert('50')
    assert   ll.head.value== '50'
    assert ll.head.next.value =='10'

def test_multiple_insert():
    '''
    5. Will return true when finding a value within the linked list that exists
    '''
    ll=LinkedList()
    ll.insert('5')
    ll.insert('10')
    ll.insert('a')
    include01=ll.includes('a')
    include02=ll.includes('10')
    include03=ll.includes('5')
    assert  include01 == True
    assert  include02 == True
    assert  include03 == True

def test_false_not_existing():
    '''
    6. Will return false when searching for a value in the linked list that does not exist
    '''
    ll=LinkedList()
    ll.insert('5')
    ll.insert('10')
    include01=ll.includes('105')
    assert include01 == False

def test_collection():
    '''
    7. Can properly return a collection of all the values that exist in the linked list
    '''
    ll=LinkedList()
    ll.insert('a')
    ll.insert('50')
    ll.insert('cc')
    assert str(ll) == "{ cc } -> { 50 } -> { a } -> NULL"