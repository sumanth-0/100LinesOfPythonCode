# Best: O(nlog(n)) time | O(1) space
# Average: O(nlog(n)) time | O(1) space
# Worst: O(nlog(n)) time | O(1) space

def heapSort(array):
    buildMaxHeap(array)  # First, build a max heap
    # Start sorting by iterating backwards through the array
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)  # Move the largest element (at index 0) to the end
        shiftDown(0, endIdx - 1, array)  # Restore heap property for the remaining elements
    return array  # The array is now sorted in place


def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2  # The last non-leaf node (starting point for heapifying)
    for currentIdx in reversed(range(firstParentIdx + 1)):
        shiftDown(currentIdx, len(array) - 1, array)  # Heapify each subtree


def shiftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1  # Left child index
    while childOneIdx <= endIdx:  # Ensure we're still within bounds of the heap
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1  # Right child index, if it exists
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            indexToSwap = childTwoIdx  # Swap with the larger child (right child)
        else:
            indexToSwap = childOneIdx  # Swap with the left child
        if heap[indexToSwap] > heap[currentIdx]:
            swap(currentIdx, indexToSwap, heap)  # Swap if child is greater than the current node
            currentIdx = indexToSwap  # Move down to the child's position and continue
            childOneIdx = currentIdx * 2 + 1  # Update the left child index
        else:
            return  # Heap property is restored, so we can stop


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]  # Simple swap function

# Example usage:
array = [12, 11, 13, 5, 6, 7]
sortedArray = heapSort(array)
print(sortedArray)  # Output will be a sorted array: [5, 6, 7, 11, 12, 13]
