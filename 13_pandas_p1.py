import pandas as pd
import numpy as np

a = pd.Series([1,2,3,4])
print(a)

#truyền index
b = pd.Series([0,1,2,3], index = ["a","b","c","d"])
print(b)

#dict
c = {'a': 13,'b':10,'d':22,'e':32}
d = pd.Series(c, index = ['a','b','c','d','e'])
print(d)
print(d['e'])
print(d[:'c'])
print(d[:2])

#Chuyển đổi dạng 
e = np.asarray(d)
print(e)




