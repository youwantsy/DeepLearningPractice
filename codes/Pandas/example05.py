import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
    data={
        "eno":[1,2,3,4,5],
        "name":["춘봄이","하여름","추가을","동겨울","춘순이"],
        "dept":["개발팀","분석팀","홍보팀","인사팀","설계팀"],
        "date":[
            pd.to_datetime("2015-09-22"),
            pd.to_datetime("2016-09-22"),
            pd.to_datetime("2017-09-22"),
            pd.to_datetime("2018-09-22"),
            pd.to_datetime("2019-09-22")
        ],
        "salary":[8000,7500,7300,7200,7700]
    }
)

print(dataframe)

#%%
dataframe["city"] = "서울"
print(dataframe)
#%%
dataframe["city"] = ["서울", "대전", "대구", "광주", "부산"]
print(dataframe)

#%% 삽입
dataframe.insert(3, "city", "서울")
print(dataframe)

#%%
dataframe.insert(dataframe.columns.get_loc("date"),"city","서울")
print(dataframe)

#%%
dataframe.insert(3, "city", ["서울", "대전", "대구", "광주", "부산"])
print(dataframe)

#%% 컬럼 삭제
# 목록으로 지정
resultDF = dataframe.drop(columns=["date","salary"])
print(resultDF)

#%%
# 슬라이싱으로 범위 지정
start = dataframe.columns.get_loc("date")
end = dataframe.columns.size
resultDF = dataframe.drop(columns=dataframe.columns[start:end])
print(resultDF)

#%% 행삭제
# 목록으로 지정
resultDF = dataframe.drop(index=[1,2])
print(resultDF)

#%%
# 슬라이싱으로 범위 지정
resultDF = dataframe.drop(index=dataframe.index[1:3])
print(resultDF)

#%% 행 label reindexing
resultDF = dataframe.drop(index=[1,2])
resultDF1 = resultDF.reset_index()
print(resultDF1)
print(dataframe)

#%%
resultDF = dataframe.drop(index=[1,2])
resultDF1 = resultDF.reset_index(drop=True)
print(resultDF1)

#%%
dataframe.drop(index=[1,2], inplace=True)
dataframe.reset_index(drop=True, inplace=True)
print(dataframe)
