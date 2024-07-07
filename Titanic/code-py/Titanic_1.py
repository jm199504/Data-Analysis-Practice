import pandas as pd

# 读取 Titanic.csv 文件
df = pd.read_csv('Titanic.csv')

# 随机抽取80%的数据
train = df.sample(frac=0.8, random_state=123)

# 将抽取的数据保存到 train.csv 文件中
train.to_csv('train.csv', index=False)

# 查看前五行数据
print(train.head())

# 查看后五行数据
print(train.tail())
