import numpy as np
import pandas as pd

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
print(s)
print(s.values)
print(s.index)
print(s[1])
print(s[1:4])