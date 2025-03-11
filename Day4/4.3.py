"Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3],duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99],duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None"

def duplicate_nums(nums):
    count = {}
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    duplicates = [num for num, freq in count.items() if freq > 1]
    
    return sorted(duplicates) if duplicates else None


print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))  
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12,12, 54]))  
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) 
