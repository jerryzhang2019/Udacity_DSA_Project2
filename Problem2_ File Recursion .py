
# coding: utf-8

# In[3]:


#Problem 2: File Recursion 
import os
def find_files(suffix, path):
    if path[-2:] == suffix:
        print(path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                find_files(suffix, os.path.join(path, file))
# Test case
find_files(".a", "./testdir")
print("--------------------")
find_files(".c", "./testdir")
print("--------------------")
find_files(".h", "./testdir")

