from tree_intersection import preOrder,Node,BinarySearch,treeInserction
def test_treeInserction_happy_path():
    BT=BinarySearch()
    BT.root=Node(150)
    BT.root.left=Node(100)
    BT.root.left.left=Node(75)
    BT.root.left.right=Node(160)
    BT.root.left.right.left=Node(125)
    BT.root.left.right.right=Node(175)
    BT.root.right=Node(250)
    BT.root.right.left=Node(200)
    BT.root.right.right=Node(350)
    BT.root.right.right.left=Node(300)
    BT.root.right.right.right=Node(500)
    BT2=BinarySearch()
    BT2.root=Node(42)
    BT2.root.left=Node(100)
    BT2.root.left.left=Node(15)
    BT2.root.left.right=Node(160)
    BT2.root.left.right.left=Node(125)
    BT2.root.left.right.right=Node(175)
    BT2.root.right=Node(600)
    BT2.root.right.left=Node(200)
    BT2.root.right.right=Node(350)
    BT2.root.right.right.left=Node(4)
    BT2.root.right.right.right=Node(500)
    actual=treeInserction(BT,BT2)
    excepted =[100, 160, 125, 175, 200, 350, 500]
    assert actual== excepted
def test_treeInserction_empty_tree():
    BT=BinarySearch()
    BT2=BinarySearch()
    BT2.root=Node(42)
    BT2.root.left=Node(100)
    BT2.root.left.left=Node(15)
    actual=treeInserction(BT,BT2)
    excepted =[]
    assert actual== excepted
def test_treeInsertion_same_tree():
    BT2=BinarySearch()
    BT2.root=Node(42)
    BT2.root.left=Node(100)
    BT2.root.left.left=Node(15)
    actual=treeInserction(BT2,BT2)
    excepted =[42,100,15]
    assert actual== excepted
