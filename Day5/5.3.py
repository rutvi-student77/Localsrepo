"Given a function that accepts unlimited arguments,check and count how many data types are in those arguments.Finally return the total in a list."
def count_data_types(*args):
    type_counts = {}
    for arg in args:                              
        arg_type = type(arg) 
        if arg_type in type_counts:
            type_counts[arg_type] += 1
        else:
            type_counts[arg_type] = 1
    return list(type_counts.values())
print(count_data_types(1, "hello", 3.14, 2, "world", True, [1, 2], (3, 4)))   
print(count_data_types(1, 2, 3, 4, 5))  
print(count_data_types("hello","world"))  
print(count_data_types(True, False, 1, 0, 3.14))  