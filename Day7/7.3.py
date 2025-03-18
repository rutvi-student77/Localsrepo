"""Write a function to replace all instances of character c1 with character c2 and vice versa.
Examples:double_swap("aabbccc", "a", "b") ➞ "bbaaccc"
	double_swap("random w#rds writt&n h&r&", "#", "&") ➞ "random w&rds writt#n h#r#"
	double_swap("128 895 556 788 999", "8", "9") ➞ "129 985 556 799 888"""
 
def double_swap(txt, c1, c2):
    trans = str.maketrans(c1 + c2, c2 + c1)
    return txt.translate(trans)

print(double_swap("aabbccc", "a", "b")) 
print(double_swap("random w#rds writt&n h&r&", "#", "&"))  
print(double_swap("128 895 556 788 999", "8", "9"))  
