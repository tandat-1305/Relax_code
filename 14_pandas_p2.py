import pandas as pd

a = {'một': pd.Series([1,2,3,4,5], index=['a','b','c','d','e']),
     'hai': pd.Series([10,20,30,40,50], index=['a','b','c','d','f'])}

b = pd.DataFrame(a)
print(b)

print('\n')
c = pd.DataFrame(b, index=['a','c','f'])
print(c)

#chọn cột 2
print("\n cột 2")
df = pd.DataFrame(a)
df_hai = df['hai']
print(df_hai)

