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
