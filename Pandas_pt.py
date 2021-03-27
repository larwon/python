import numpy as np
import pandas as pd

s = pd.Series([0, 0.25, 0.5, 0.75, 1],
             index = ['a', 'b', 'c', 'd', 'e'])
print(s) #index를 따로 구성
print(s['c'])
print(s[['c', 'd', 'e']])
print('b') in s #s변수 안에 b가 있냐?

