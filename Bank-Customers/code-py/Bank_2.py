import pandas as pd
import matplotlib.pyplot as plt

# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

# 按教育程度和婚姻状况进行分组，并计算每个组的数量
grouped_data = df.groupby(['education', 'marital']).size().unstack()

# 绘制柱状图
grouped_data.plot(kind='bar', stacked=True)

# 设置图形属性
plt.xlabel('Education')
plt.ylabel('Count')
plt.title('Marital Status by Education')
plt.xticks(rotation=45)

# 显示图形
plt.show()

print(grouped_data)