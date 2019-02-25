from ex14 import *

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Coral")
    colors.push("Teal")
    assert colors.unshift() == "Coral"
    assert colors.unshift() == "Teal"
    assert colors.unshift() == None

def test_get():
    colors = DoubleLinkedList()
    colors.push("Sarcoline")
    colors.push("Coquelicot")
    colors.push("Smaragdine")
    assert colors.get(2) == "Smaragdine"
    assert colors.get(1) == "Coquelicot"
    assert colors.get(0) == "Sarcoline"

def test_remove():
    colors = DoubleLinkedList()
    colors.push("Mikado")
    colors.push("Glaucous")
    colors.push("Wenge")

    colors.remove("Mikado")

    node = colors.begin
    while node:
        if node.value != "Mikado":
            node = node.next

        else:
            assert 1 == 2

    assert node == None
