from ex13 import *

def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = SingleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None

def test_shift():
    colors = SingleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1

    colors.shift("Carbazole Violet")
    assert colors.count() == 2

    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 1
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 0

def test_remove():
    colors = SingleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    assert colors.remove("Cobalt") == 0
    colors.dump("before perinone")
    assert colors.remove("Perinone") == 2
    colors.dump("after perinone")
    assert colors.remove("Nickle Yellow") == 1
    assert colors.remove("Zinc White") == 0

def test_get():
    colors = SingleLinkedList()
    colors.push("Red")
    assert colors.get(0) == "Red"
    colors.push("White")
    assert colors.get(1) == "White"
    colors.push("Blue")
    assert colors.get(0) == "Red"
    assert colors.get(2) == "Blue"
