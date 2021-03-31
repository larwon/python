import numpy as np
import pandas as pd


#여러 개의 값들을 딕셔너리 값으로 넣어보자
a = pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}]) 
print(a)
#총 칼럼은 A, B, C, D
#값이 없는 부분은 NaN으로 처리 (누락값)
s = pd.DataFrame(np.random.rand(5, 5),
            columns=['A', 'B', 'C', 'D', 'E'],
            index=[1, 2, 3, 4, 5])
print(s)