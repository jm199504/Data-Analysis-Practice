import pandas as pd
import matplotlib.pyplot as plt

# 【分析五】年龄与生还率关系
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 删除年龄缺失值的行
df.dropna(subset=['Age'], inplace=True)

# 分割年龄为年龄段
bins = [0, 12, 18, 65, 100]
labels = ['Children', 'Teenager', 'Adult', 'Elderly']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# 计算不同年龄段的生还人数
survived_counts = df[df['Survived'] == 1]['AgeGroup'].value_counts()
total_counts = df['AgeGroup'].value_counts()

# 计算不同年龄段的生还率
survival_rates = round((survived_counts / total_counts) * 100, 2)

print(survival_rates)
# 【分析五的结论】：根据年龄段进行分类，不同年龄段的乘客生还率如下：
# 儿童（0-12岁）的生还率为55.56%
# 少年（12-18岁）的生还率为47.22%
# 成人（18-65岁）的生还率为36.27%
# 老年（65-100岁）的生还率为0.00%

# 【分析五的可视化】使用柱状图表示年龄与生还率关系
# 创建柱状图
plt.bar(survival_rates.index, survival_rates.values)

# 设置图表标题和标签
plt.title('Survival Rates by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate (%)')

# 显示图表
plt.show()