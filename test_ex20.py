from ex20 import *

def test_get():
    root = BSTreeNode(None, None, 7, 20)
    assert root.get(7) == (7, 20)

# def test_set():
#    root = BSTreeNode(None, None, 7, 20)
#    root.set(8, 100)
#    assert root.get(8, 100) == (8, 100)
