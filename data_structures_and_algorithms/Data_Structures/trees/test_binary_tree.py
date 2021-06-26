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
    excepted= 'left_left_left left_left left right_left right_right right rootItem '
    actual=test_fixure.postOrder()
    assert excepted==actual

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
