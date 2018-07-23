
from module1 import find_index, test 
import sys
sys.path.append('/Users/jxi/python')

courses = ['History', 'Math', 'Français', 'Physics', 'Compsci']

index = find_index(courses, 'Français')
index1 =  find_index(courses, 'French')

print(index)
print('---------------------')
print(index1)
print('---------------------')
print(test) 
print('---------------------')
print(sys.path)
print('---------------------')

import module2