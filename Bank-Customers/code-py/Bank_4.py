import pandas as pd
import matplotlib.pyplot as plt

# 【分析二】统计每个职业的分布情况
# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

# 统计每个职业的人数
job_counts = df['job'].value_counts()

# 根据人数进行排序
job_counts = job_counts.sort_values()

print(job_counts)

# 人数最多的职业占比
print(f'{round(max(job_counts) / df["job"].count() * 100,2)}%')

# 【分析二的结论】该份数据中职业为管理人员(admin.)的人数最多，达到了5557，占比 24.7%

# 【分析二的可视化】使用统计图表示各个职业的人数分布情况

plt.figure(figsize=(10, 6))
job_counts.plot(kind='barh')
plt.title('Number of People by Job')
plt.xlabel('Count')
plt.ylabel('Job')
plt.show()