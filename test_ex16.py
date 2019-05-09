from ex16 import *
from ex14 import DoubleLinkedList
from random import randint

max_numbers = 800

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

def test_merge_sort():
    numbers = random_list(max_numbers)
    while is_sorted(numbers) == True:
        numbers = random_list(max_numbers)

    merge_sort(numbers)

    assert is_sorted(numbers) == True

if __name__ == '__main__':
    test_bubble_sort()
    test_merge_sort()
