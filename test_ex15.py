from ex15 import *

def test_push():
    teams = Stack()
    teams.push("Giants")
    teams.push("Twins")

    assert teams.top.value == "Indians"

def test_pop():
    teams = Stack()
    teams.push("Cavaliers")
    teams.push("Mavericks")

    assert teams.pop() == "Mavericks"

def test_count():
    teams = Stack()
    teams.push("Brewers")
    teams.push("Reds")

    assert teams.count() == 2
