def recursive_binary_search(value, low, high, list):
    if low <= high:
        middle = (low + high) // 2

        if list[middle] == value:
            return middle
        
        elif list[middle] > value:
            return recursive_binary_search(value, low, middle - 1, list)
        
        elif list[middle] < value:
            return recursive_binary_search(value, middle + 1, high, list)
        
        else:
            return None
        

a = [1,2,3,4,5,6]
print(recursive_binary_search(7, 0, len(a),a))