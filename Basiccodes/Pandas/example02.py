import pandas as pd
import numpy as np
import tensorflow as tf
#%%
pname = ["오렌지", "바나나", "딸기", "사과"]
pprice = [3000, 2000, 6000, 4500]
pstock = np.array([50, 30, 10, 100])
porigin = np.array(["미국", "필리핀", "한국", "한국"])

dataframe = pd.DataFrame(
    data={
        "PNAME":pname,
        "PPRICE":pprice,
        "PSTOCK":pstock,
        "PORIGIN":porigin
    },
    index=["F1", "F2", "F3", "F4"]
)
print(dataframe)

#%%
dataframe = pd.DataFrame(
    #data=np.column_stack([pname, pprice, pstock, porigin]),
    data=np.c_[pname,pprice,pstock,porigin],
    columns=["PNAME", "PPRICE","PSTOCK", "PORIGIN"],
    index=["F1", "F2", "F3", "F4"]
)
print(dataframe)

#%% dataframe 복제
dataframe_cloned = dataframe.copy()
dataframe_cloned.at["F4", "PSTOCK"] = 1000
print(dataframe)
print(dataframe_cloned)