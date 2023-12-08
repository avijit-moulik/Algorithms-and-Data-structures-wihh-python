def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)
            
def verify(result):
    print("Target found: ",result)
    
numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers,8)  # the number you want to search
verify(result)



"""
    Worst-case: O(log n) - In the worst-case scenario, each recursive call divides the search space in half. This leads to a time complexity of logarithmic base 2, similar to the iterative binary search.
    Best-case: O(1) - In the best-case scenario, the target element is found with the first comparison, resulting in constant time complexity.

Space Complexity:

    O(log n) - The space complexity of recursive binary search is determined by the maximum depth of the recursion, which is logarithmic. Each recursive call consumes space on the call stack. In the worst case, the maximum depth of the recursion is O(log n), where n is the size of the input.

It's important to note that the space complexity in the worst case is O(log n) due to the recursive calls. If the binary search were implemented iteratively, it would have a space complexity of O(1).

In summary, the recursive binary search algorithm has a time complexity of O(log n) in the worst case and O(1) in the best case. Its space complexity is O(log n) due to the recursive nature of the algorithm and the function call stack.

"""
