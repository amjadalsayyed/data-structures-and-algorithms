import pytest
from Trees.Tree import BinarySearchTree, BinaryTree

def test_1():
    tree= BinaryTree()
    actual = tree.pre_order(tree.root)
    expected = []
    assert actual==expected

def test_2():
    tree= BinarySearchTree()
    tree.add(5)
    tree.add(4)
    tree.add(7)
    actual = tree.in_order(tree.root)
    expected = [4,5,7]
    assert actual==expected   

def test_3(BST):
    assert BST.pre_order(BST.root) == [5,3,2,4,7,6,8]


def test_4(BST):
    assert BST.in_order(BST.root) == [2,3,4,5,6,7,8]

def test_5(BST):
    assert BST.post_order(BST.root) == [2,4,3,6,8,7,5]    


def test_6(BST):
    assert BST.contain(8) == True

def test_7(BST):
    assert BST.contain(9) == False    

@pytest.fixture
def BST():
    BST= BinarySearchTree()
    BST.add(5)
    BST.add(3)
    BST.add(2)
    BST.add(4)
    BST.add(7)
    BST.add(6)
    BST.add(8)
    return BST