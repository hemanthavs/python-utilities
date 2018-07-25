"""
    Merge Sort
"""


def sort(collection):

    collection_length = len(collection)

    if collection_length < 2:
        return collection

    mid = collection_length // 2

    left = sort(collection[:mid])
    right = sort(collection[mid:])

    return merge(left, right)


def merge(left, right):

    sorted_array = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index = left_index + 1
        else:
            sorted_array.append(right[right_index])
            right_index = right_index + 1

    sorted_array = sorted_array + left[left_index:]
    sorted_array = sorted_array + right[right_index:]

    return sorted_array
