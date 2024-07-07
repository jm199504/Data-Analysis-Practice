import pandas as pd
import matplotlib.pyplot as plt

# 【分析三】统计20-30岁之间用户订阅该产品的比例分布
# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

# 筛选年龄在 20-30 岁之间的数据
age_filter = (df['age'] >= 20) & (df['age'] <= 30)
subset_df = df[age_filter]

# 计算各个年龄的订阅比例
age_counts = subset_df['age'].value_counts()
age_proportions = (age_counts / age_counts.sum()) * 100

print(age_proportions)

# 【分析三的可视化】使用饼图绘制20-30岁之间用户订阅该产品的比例分布
plt.figure(figsize=(8, 6))
plt.pie(age_proportions, labels=age_proportions.index, autopct='%1.1f%%')
plt.title('Proportion of Subscribers Aged 20-30')
plt.show()

# 【分析三的可视化】使用柱状图绘制20-30岁之间用户订阅该产品的比例分布
# plt.figure(figsize=(8, 6))
# plt.bar(age_counts.index, age_counts.values)
# plt.xlabel('Age')
# plt.ylabel('Number of Subscribers')
# plt.title('Distribution of Subscribers Aged 20-30')
# plt.show()