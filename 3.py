import pandas as pd

with open('test.csv', 'r', encoding='utf-8') as rf:
    df = pd.read_csv(rf)

# 按行遍历csv文件
for index in df.index:
    Source = df.loc[index].values[0]  # Source
    Target = df.loc[index].values[1]  # Target
    Weight = df.loc[index].values[2]  # Weight
    print(Source, Target, Weight)
