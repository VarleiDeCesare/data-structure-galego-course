from random import randint

def quicksort(arr):
    def partition(low, high):
        pivot = arr[high // 2]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr


test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array:", test_array)
print("Sorted array:", quicksort(test_array))


# Alternative implementation of Quick Sort using 3-way partitioning and apparenttly better performance
def quick_sort(left, right):
            if left >= right:
                return

            pivot = nums[randint(left, right)]
            less_than_pointer, greater_than_pointer, current = left - 1, right + 1, left

            while current < greater_than_pointer:
                if nums[current] < pivot:
                    less_than_pointer += 1
                    nums[less_than_pointer], nums[current] = nums[current], nums[less_than_pointer]
                    current += 1
                elif nums[current] > pivot:
                    greater_than_pointer -= 1
                    nums[greater_than_pointer], nums[current] = nums[current], nums[greater_than_pointer]
                else:
                    current += 1

            quick_sort(left, less_than_pointer)
            quick_sort(greater_than_pointer, right)