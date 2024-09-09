def merge(left, right):
    print(f'left input, right input: {left}, {right}')
    leftIndex, rightIndex = 0, 0
    print(f'leftIndex, rightIndex: {leftIndex}, {rightIndex}')

    mergedArray = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            mergedArray.append(left[leftIndex])
            leftIndex += 1
            print(f'Merged array left appended: {mergedArray}')
            print(f'leftIndex, rightIndex: {leftIndex}, {rightIndex}')
        else:
            mergedArray.append(right[rightIndex])
            rightIndex += 1
            print(f'Merged array right appended: {mergedArray}')
            print(f'leftIndex, rightIndex: {leftIndex}, {rightIndex}')
    
    mergedArray += left[leftIndex:]
    print(f'Merged array += left: {mergedArray}')
    mergedArray += right[rightIndex:]
    print(f'Merged array +=: right: {mergedArray}')
    return mergedArray


def mergeSort(array):
    if len(array) <= 1:  # base case
        return array

    half = len(array) // 2
    print(f'Half: {half}')

    left = mergeSort(array[:half])
    print(f'Left: {left}')

    right = mergeSort(array[half:])
    print(f'Right: {right}')

    return merge(left, right)



def main():
    array = [5,2,3,1,4,4,7]
    # array = input("Enter an array: ")
    print(f'Entered array: {array}')
    sortedArray = mergeSort(array)
    print(f'Sorted array: {sortedArray}')



if __name__ == "__main__":
    main()