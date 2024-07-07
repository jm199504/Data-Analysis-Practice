import pandas as pd
import matplotlib.pyplot as plt
# 【分析四】乘客的性别与生还率关系
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 计算不同性别的生还人数
survived_counts = df[df['Survived'] == 1]['Sex'].value_counts()
total_counts = df['Sex'].value_counts()

# 计算不同性别的生还率
survival_rates = round((survived_counts / total_counts) * 100, 2)

print(survival_rates)
# 【分析四的结论】：男性和女性乘客生还率如下：男性的生还率为18.12%，女性的生还率为72.13%，女性乘客可能更容易生还。

# 【分析四的可视化】使用柱状图表示乘客的性别与生还率关系

# 创建柱状图
plt.bar(survival_rates.index, survival_rates.values)

# 设置图表标题和标签
plt.title('Survival Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate (%)')

# 显示图表
plt.show()