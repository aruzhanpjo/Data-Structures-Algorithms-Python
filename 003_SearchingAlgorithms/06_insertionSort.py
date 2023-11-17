"""
it is simple, stable, and in-place.

1. takes an array arr as an input parameter.
2. iterates through the array starting from the second element (index 1) to the end.
3. for each element, it compares it with the elements before it and moves the
    elements greater than the current element to the right.
4. it repeats this process until it finds the correct position for the current element,
    and then inserts it into that position.
    
Time Complexity: avg: O(n^2), best: O(n), worst: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
