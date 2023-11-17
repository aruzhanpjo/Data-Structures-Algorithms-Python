"""
mergse sort: The unsorted array is divided into two halves. This division continues until each 
sub-array contains only one element. The two halves created in the previous step are recursively 
sorted using the merge sort algorithm. The sorted halves are merged back together to create a 
single sorted array. The merging process involves comparing elements from the two sorted 
halves and arranging them in sorted order.

Space complexity: O(n)
Time complexity: O(nlogn)
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print("Sorted list:", my_list)
