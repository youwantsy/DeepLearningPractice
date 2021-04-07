import pandas as pd
import numpy as np

#%%
series = pd.Series(data=None, index=None, name=None)

series = pd.Series(
    data=["오렌지", "바나나", "딸기"]
)
print(series)
#%%
series = pd.Series(
    data=np.array(["오렌지", "바나나", "딸기"]),
    index=["f1", "f2", "f3"]
)

print(series)

#%%
series = pd.Series(
    data=np.array(["오렌지", "바나나", "딸기"]),
    name="PNAME"
)
print(series)

#%% DataFrame 생성
pd.DataFrame(data=None, index=None, columns=None)
series1 = pd.Series(data=["오렌지", "바나나", "딸기", "사과"])
series2 = pd.Series(data=[3000, 2000, 6000, 4500])
series3 = pd.Series(data=[50, 30, 10, 100])
series4 = pd.Series(data=["미국", "필리핀", "한국", "한국"])

dataframe = pd.DataFrame(
    data={
        "PNAME":series1,
        "PPRICE":series2,
        "PSTOCK":series3,
        "PORIGIN":series4
    }
)

print(dataframe)

#%%
series1 = pd.Series(
    data=["오렌지", "바나나", "딸기", "사과"],
    index=["F1", "F2", "F3", "F4"]
)
series2 = pd.Series(
    data=[3000, 2000, 6000, 4500],
    index=["F1", "F2", "F3", "F4"]
)
series3 = pd.Series(
    data=[50, 30, 10, 100],
    index=["F1", "F2", "F3", "F4"]
)
series4 = pd.Series(
    data=["미국", "필리핀", "한국", "한국"],
    index=["F1", "F2", "F3", "F4"]
)

dataframe = pd.DataFrame(
    data={
        "PNAME":series1,
        "PPRICE":series2,
        "PSTOCK":series3,
        "PORIGIN":series4
    }
)
print(dataframe)