import os

def get_filename_from_path(path):
    return os.path.basename(path)

file_path = "D:\rutvi\index.html"
filename = get_filename_from_path(file_path)
print(filename)  
