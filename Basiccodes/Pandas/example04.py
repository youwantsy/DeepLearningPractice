import pandas as pd
import numpy as np
import tensorflow as tf

pname = ["오렌지", "바나나", "딸기", "사과"]
pprice = [3000, 2000, 6000, 4500]
pstock = [50, 30, 10, 100]
porigin = ["미국", "필리핀", "한국", "한국"]
pdate = ["2019-01-01", "2019-02-01", "2019-03-01", "2019-04-01"]

dataframe = pd.DataFrame(
    data={
        "PNAME":pname,
        "PPRICE":pprice,
        "PSTOCK":pstock,
        "PORIGIN":porigin,
        "PDATE":pdate
    }
)
#%%
values = dataframe.values
# values = dataframe.to_numpy()
print(type(values))
print(values)
#%%
values = dataframe["PNAME"].values
# values = dataframe["PNAME"].to_numpy()
print(type(values))
print(values)
#%% shape 속성 (raw, cloumns)
print(dataframe.shape)