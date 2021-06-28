import pytest
from tree import Node , BinaryTree,BinarySearch

def test_instance_empty_tree():
    '''
    Can successfully instantiate an empty tree
    '''
    actual=BinaryTree().root
    excepted= None
    assert actual==excepted

def test_single_node_tree():
    '''
    Can successfully instantiate a tree with a single root node
    '''
    bTree=BinaryTree()
    bTree.root=Node('RootItem')
    actual=bTree.root.value
    excepted='RootItem'
    assert actual==excepted

def test_add_left_and_right_to_root():
    '''
    Can successfully add a left child and right child to a single root node
    '''
    btree=BinaryTree()
    btree.root=Node('rootItem')
    btree.root.right=Node('rightRoot')
    actual01=btree.root.right.value
    btree.root.left=Node('leftRoot')
    actual02=btree.root.left.value
    excepted01='rightRoot'
    excepted02='leftRoot'
    assert excepted01==actual01 
    assert excepted02==actual02 

    # Can successfully return a collection from a preorder traversal
def test_preorder_traversal(test_fixure):
    excepted= 'rootItem left left_left left_left_left right right_left right_right '
    actual=test_fixure.preOrder()
    assert excepted==actual

def test_inOrder_traversal(test_fixure):
    excepted= 'left_left_left left_left left rootItem right_left right right_right '
    actual=test_fixure.inOrder()
    assert excepted==actual
def test_postOrder_traversal(test_fixure):
    excepted= ['left_left_left ', 'left_left ', 'left ', 'right_left ', 'right_right ', 'right ', 'rootItem ']
    actual=test_fixure.postOrder()
    assert excepted==actual

def test_find_max(test_fixture_find_max):
    actual = test_fixture_find_max.find_max_value()
    axcepted = 151
    assert actual == axcepted

def test_find_max_empty_tree():
    actual = BinaryTree().find_max_value()
    excepted = 'Oops, empty binary tree '
    assert actual  == excepted

@pytest.fixture
def test_fixture_find_max():
    Btree=BinaryTree()
    Btree.root=Node(2)
    Btree.root.left=Node(18)
    Btree.root.right=Node(22)
    leftRoot=Btree.root.left
    leftRoot.left=Node(43)
    leftRoot.right=Node(6)
    leftRoot.right.left=Node(11)
    leftRoot.right.right=Node(22)
    Btree.root.right.left=Node(37)
    Btree.root.right.right=Node(51)
    Btree.root.right.right.right=Node(151)
    return Btree


@pytest.fixture
def test_fixure():
    btree=BinaryTree()
    btree.root=Node('rootItem ')# rootItem
    btree.root.left=Node('left ')# leftRootItem
    btree.root.right=Node('right ')# rightRootItem
    btree.root.left.left=Node('left_left ')# rightRootItem
    btree.root.left.left.left=Node('left_left_left ')# rightRootItem
    btree.root.right.left=Node('right_left ')# rightRootItem
    btree.root.right.right=Node('right_right ')# rightRootItem
    return btree
# ------------------CC17 test -----------------

def test_breath_first_Happy_Path(test_tree_breadth_first):
    actual = test_tree_breadth_first.breadthFirst(test_tree_breadth_first)
    excepted =[2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual ==excepted
def test_breath_first_Happy_Path():
    Btree=BinaryTree()
    actual= Btree.breadthFirst(Btree)
    excepted = 'Empty Tree'
    assert actual ==excepted
    
@pytest.fixture
def test_tree_breadth_first():
    Btree=BinaryTree()
    Btree.root=Node(2)
    Btree.root.left=Node(7)
    Btree.root.left.left=Node(2)
    Btree.root.left.right=Node(6)
    Btree.root.left.right.right=Node(11)
    Btree.root.left.right.left=Node(5)
    Btree.root.right=Node(5)
    Btree.root.right.right=Node(9)
    Btree.root.right.right.left=Node(4)
    return Btree