from ex16 import bubble_sort
from ex14 import DoubleLinkedList
from random import randint

max_numbers = 36

def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers

def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next
    return True

def test_bubble_sort():
    numbers = random_list(max_numbers)
    while is_sorted(numbers) == True:
        numbers = random_list(max_numbers)

    bubble_sort(numbers)

    assert is_sorted(numbers) == True
