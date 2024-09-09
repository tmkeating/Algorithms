def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = mergeSort(array[:half])
    right = mergeSort(array[half:])

    return merge(left, right)

def main():
    array = input("Enter an array: ")
    print(f'Entered array: {array}')
    sortedArray = mergeSort(array)
    print(f'Sorted array: {sortedArray}')

if __name__ == "__main__":
    main()