import numpy as np
import pandas as pd


pop_tuple = {'서울특별시':9720846,
            '부산광역시':3404423,
            '인천광역시':2947217,
            '대구광역시':2427954,
            '대전광역시':1471040,
            '광주광역시':1455048}
population = pd.Series(pop_tuple)
print(population) #튜플형태로 Series를 만들 수 있다 (인덱스가 한글도 가능)

print(population['서울특별시':'인천광역시']) #서울부터 인천까지 다 보여줌