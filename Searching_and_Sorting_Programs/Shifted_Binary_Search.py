# O(logn) time | O(1) space
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)


def shiftedBinarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]

        # If we find the target
        if potentialMatch == target:
            return middle
        
        # Check if the left side is sorted
        if leftNum <= potentialMatch:
            # Target is in the left sorted portion
            if target >= leftNum and target < potentialMatch:
                right = middle - 1
            else:
                left = middle + 1
        # Otherwise, the right side must be sorted
        else:
            # Target is in the right sorted portion
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else:
                right = middle - 1

    # Target not found
    return -1

# Example usage:
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
index = shiftedBinarySearch(array, target)
print(index)  # Output: 8 (index of 33 in the array)
