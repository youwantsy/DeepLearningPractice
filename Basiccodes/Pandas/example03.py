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

print(dataframe)
#%%
print(type(dataframe))
#%%
print(type({"a":1,"b":2}))
print(type((1,2,3)))
#%%
dataframe.index = ["F1", "F2", "F3", "F4"]
dataframe.columns = ["상품명", "가격", "재고", "원산지", "수확일"]
print(dataframe)

#%% 학습용 데이터셋과 테스트용 데이터셋이 같은 dataframe으로 되어있어야 하므로 비교
dataframe1 = pd.DataFrame(
    data={"A":[1, 2],
          "B":[3, 4]},
    index=["L1", "L2"]
)
dataframe2 = pd.DataFrame(
    data={"A":[10, 20],
          "C":[30, 40]},
    index=["L1", "L3"]
)

print(dataframe1, "\n")
print(dataframe2, "\n")

print(dataframe1.columns.symmetric_difference(dataframe2.columns))
print(dataframe1.columns.difference(dataframe2.columns))
print(dataframe2.columns.difference(dataframe1.columns), "\n")

print(dataframe1.index.symmetric_difference(dataframe2.index))
print(dataframe1.index.difference(dataframe2.index))
print(dataframe2.index.difference(dataframe1.index))

#%% dtype 속성
print(dataframe.dtypes)

#%% dtype 변경
dataframe = dataframe.astype({"PSTOCK":np.float32}, errors="ignore")
dataframe = dataframe.astype({"PPRICE":np.float}, errors="ignore")
print(dataframe.dtypes)

dataframe = dataframe.astype({"PDATE": 'datetime64'})
print(dataframe.dtypes)