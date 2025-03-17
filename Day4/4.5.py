"Create a function/input that returns the sum of all even elements in a 2D matrix.,Examplessum_of_evens([ [1, 0, 2], [5, 5, 7], [9, 4, 3] ]) ➞ 6   // 2 + 4 = 6,sum_of_evens([ [1, 1], [1, 1] ]) ➞ 0,sum_of_evens([ [42, 9], [16, 8] ]) ➞ 66,sum_of_evens([ [], [], [] ]) ➞ 0"

def sum_of_evens(matrix):
    total_sum = 0 
    
    for row in matrix:
        for element in row:
            if element % 2 == 0:
                total_sum += element  
                
    return total_sum
print(sum_of_evens([ [1, 0, 2], [5, 5, 7], [9, 4, 3] ]))  
print(sum_of_evens([ [1, 1], [1, 1] ])) 
print(sum_of_evens([ [42, 9], [16, 8] ]))  
print(sum_of_evens([ [], [], [] ]))  
