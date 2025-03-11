"Finding the maximum difference between tuple pair Input: tupList = [(5, 7), (2, 6), (1, 9), (1, 3)]"

def max_difference(tupList):
    max_diff = float('-inf')  
    
    for t in tupList:
        diff = abs(t[0] - t[1])
        
        if diff > max_diff:
            max_diff = diff
            
    return max_diff

tupList = [(5, 7), (2, 6), (1,8), (1, 3)]
result = max_difference(tupList)
print(result)  
