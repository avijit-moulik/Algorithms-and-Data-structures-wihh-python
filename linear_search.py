def lenear_surch(list,target):    #Return the index psition of the target....if found ,else return None
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None
    
def verify(index):
    if index is not None:
        print("Target found at index : ",index)
    else:
        print("Target not found in list ")
numbers =[1,2,3,4,5,6,7,8,9,10]
result = lenear_surch(numbers,3)     #the number you want to surch
verify(result)    


"""

Time Complexity:

    Worst-case: O(n) - In the worst-case scenario, where the element being searched is at the end of the list or not present at all, the algorithm may need to check every element in the list.
    Best-case: O(1) - In the best-case scenario, where the target element is found at the beginning of the list, the algorithm will terminate after checking the first element.

Space Complexity:

    O(1) - The linear search algorithm has a constant space complexity because it uses a fixed amount of extra space regardless of the size of the input. It only requires a few variables (e.g., loop counters) and does not rely on additional data structures.

In summary, the linear search algorithm has a linear time complexity O(n) in the worst case and constant space complexity O(1). It is a straightforward algorithm but may not be the most efficient for large datasets compared to more advanced search algorithms like binary search for sorted lists or hash-based methods.


"""
