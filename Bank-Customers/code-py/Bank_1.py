import pandas as pd

# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

print(df.head())

print(df.tail())

# 检测缺失值
missing_values = df.isnull().sum()

# 输出各字段的缺失值数量，其中Age、Cabin、Embarked存在缺失值
print(missing_values)
# 该份数据不存在缺失值

# 检测重复值
duplicate_rows = df.duplicated()
duplicate_rows_count = duplicate_rows.sum()
print("重复行数:", duplicate_rows_count)
# 该份数据不存在重复行

# 基本统计分析(包含数量、均值、方差、最小值、最大值等)
statistics = df.describe()
print(statistics)