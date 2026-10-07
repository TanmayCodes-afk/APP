import pandas as pd

#Series with default index
ser=pd.Series([10,20,30,40,50])
print(ser)

#series with custom index
ser_custom=pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(ser_custom)   

#Series with ten random numbers
import pandas as pd
import numpy as np

series = pd.Series(np.random.randint(1, 100, 10))

print(series)