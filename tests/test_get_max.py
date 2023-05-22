import pytest
from Trees.Tree import BinarySearchTree , BinaryTree ,Node


"""I took these tests from abdullah shaghnoba to try it on my code """


def test_1(tree):
    actual = tree.find_maximum_value()
    expected = -1
    assert actual == expected

def test_2(tree2):
    actual = tree2.find_maximum_value()
    expected = 155
    assert actual == expected

def test_3():
    tree5 = BinaryTree()
    actual = tree5.find_maximum_value()
    expected = 'Empty Tree!'
    assert actual == expected

@pytest.fixture
def tree():
    tree= BinaryTree()
    node1 = Node(-5)
    tree.root = node1
    tree.root.left=Node(-10)
    tree.root.left.left=Node(-155)
    tree.root.left.right=Node(-1)
    tree.root.right=Node(-3)
    tree.root.right.right = Node(-2)
    tree.root.right.left = Node(-4)
    return tree

@pytest.fixture
def tree2():
    tree2= BinaryTree()
    node1 = Node(5)
    tree2.root = node1
    tree2.root.left=Node(10)
    tree2.root.left.left=Node(155)
    tree2.root.left.right=Node(1)
    tree2.root.right=Node(3)
    tree2.root.right.right = Node(2)
    tree2.root.right.left = Node(4)
    return tree2