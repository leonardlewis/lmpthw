from ex15 import *

def test_push():
    teams = Stack()
    teams.push("Giants")
    teams.push("Indians")

    assert teams.top.value == "Indians"
