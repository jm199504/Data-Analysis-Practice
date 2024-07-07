import pandas as pd
import matplotlib.pyplot as plt

# 【分析一】统计高中学历婚姻状况的比例

# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

# 筛选出高中学历的数据
high_school_data = df[df['education'] == 'high.school']

# 统计高中学历下不同婚姻状况的数量
grouped_data = high_school_data.groupby('marital').size().reset_index(name='count')

# 计算比例
total_count = grouped_data['count'].sum()
grouped_data['ratio'] = grouped_data['count'] / total_count

# 输出统计结果
print(grouped_data[['marital', 'ratio']])

# 【分析一的可视化】使用饼图表示高中学历婚姻状况的比例
plt.figure(figsize=(6, 6))
labels = grouped_data['marital']
sizes = grouped_data['count']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Marital Status of High School Graduates')
plt.show()
# 【分析一的结论】高中学历中结婚的比例达到了52.5%