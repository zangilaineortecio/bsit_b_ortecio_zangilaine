# Sum all numbers in an array using recursion
def sum_array(arr):
    if len(arr) == 0:
        return 0

    first_num = arr[0]
    remaining = arr[1:]

    return first_num + sum_array(remaining)


print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4]))
print(sum_array([-1, 5, -3, 2]))


# Find the largest number in an array
def find_largest(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")

    if len(arr) == 1:
        return arr[0]

    current = arr[0]
    largest_in_rest = find_largest(arr[1:])

    if current > largest_in_rest:
        return current

    return largest_in_rest


print(find_largest([5]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 4, 8, 12]))
print(find_largest([-5, -2, -10, -1]))


# Count how many times a chosen number appears
def count_number(arr, target):
    if len(arr) == 0:
        return 0

    count = 1 if arr[0] == target else 0

    return count + count_number(arr[1:], target)


print(count_number([], 5))
print(count_number([1, 5, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 5))
print(count_number([7, 7, 7, 7], 7))