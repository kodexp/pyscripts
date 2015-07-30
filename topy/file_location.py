"""
fzhang:~$ python file_location.py 
/home
/home/fzhang
/home/fzhang/file_location.py

"""
import os
path_to_this_file=os.path.abspath(__file__)
parent_dir=os.path.dirname(path_to_this_file)
g_parent_dir=os.path.dirname(parent_dir)

print g_parent_dir
print parent_dir
print path_to_this_file
