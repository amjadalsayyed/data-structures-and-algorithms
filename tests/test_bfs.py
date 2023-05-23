from Trees.Tree import breadth_first,Node,BinaryTree
import pytest

def test_1():
    tree = BinaryTree()
    assert breadth_first(tree) == 'Empty Tree!'


def test_2(tree2):
   assert breadth_first(tree2) == [5, 10, 3, 155, 1, 4,2]

def test_3(tree):
    assert breadth_first(tree) == [-5,-10,-3,-155,-1,-4,-2]   


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
