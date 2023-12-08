def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 4)  # the number you want to search
verify(result)


"""
Time Complexity:

    Worst-case: O(log n) - In the worst-case scenario, binary search divides the search interval in half with each step, resulting in a time complexity of logarithmic base 2. This is highly efficient compared to linear search, especially for large datasets.
    Best-case: O(1) - In the best-case scenario, where the target element is found with the first comparison, the time complexity is constant.

Space Complexity:

    O(1) - Binary search has a constant space complexity, similar to linear search. It does not require additional space proportional to the size of the input.

Binary search is advantageous over linear search for sorted lists because it reduces the search space exponentially, making it much faster for large datasets. However, it's important to note that binary search is applicable only to sorted lists.

In summary, binary search has a time complexity of O(log n) in the worst case and O(1) in the best case. Its space complexity is constant, making it an efficient algorithm for searching in sorted lists.

"""
