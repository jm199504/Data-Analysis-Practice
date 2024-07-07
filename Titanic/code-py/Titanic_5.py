import pandas as pd
import matplotlib.pyplot as plt
# 【分析三】一等舱生还率为 XX%，二等舱为 XX%，三等舱为 XX%。
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 统计不同舱位的乘客人数
first_class_total = df[df['Pclass'] == 1]['PassengerId'].count()
second_class_total = df[df['Pclass'] == 2]['PassengerId'].count()
third_class_total = df[df['Pclass'] == 3]['PassengerId'].count()

# 统计不同舱位生还的乘客人数
first_class_survived = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]['PassengerId'].count()
second_class_survived = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]['PassengerId'].count()
third_class_survived = df[(df['Pclass'] == 3) & (df['Survived'] == 1)]['PassengerId'].count()

# 计算不同舱位的生还率，并保留两位小数
first_class_percent_survived = round((first_class_survived / first_class_total) * 100, 2)
second_class_percent_survived = round((second_class_survived / second_class_total) * 100, 2)
third_class_percent_survived = round((third_class_survived / third_class_total) * 100, 2)

# 打印结果
print(f"一等舱生还率为 {first_class_percent_survived}%")
print(f"二等舱生还率为 {second_class_percent_survived}%")
print(f"三等舱生还率为 {third_class_percent_survived}%")

# 【分析三的结论】一等舱生还率为 61.99%，二等舱生还率为 43.92%，三等舱生还率为 22.84%，可见客舱等级越高，生还率越高。

# 【分析三的可视化】使用柱状图表示不同舱位的生还率

# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 统计不同舱位的乘客人数
class_counts = df['Pclass'].value_counts(sort=False)

# 统计不同舱位生还的乘客人数
survived_counts = df[df['Survived'] == 1]['Pclass'].value_counts(sort=False)

# 计算不同舱位的生还率，并保留两位小数
survival_rates = round((survived_counts / class_counts) * 100, 2)

# 创建柱状图
plt.bar(survival_rates.index, survival_rates.values)

# 设置图表标题和标签
plt.title('Survival Rates by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate (%)')

# 显示图表
plt.show()

# 【分析三的可视化】使用饼图表示不同舱位的生还率
# # 读取 train.csv 文件
# df = pd.read_csv('train.csv')
#
# # 统计不同舱位的乘客人数
# class_counts = df['Pclass'].value_counts(sort=False)
#
# # 统计不同舱位生还的乘客人数
# survived_counts = df[df['Survived'] == 1]['Pclass'].value_counts(sort=False)
#
# # 计算不同舱位的生还率，并保留两位小数
# survival_rates = round((survived_counts / class_counts) * 100, 2)
#
# # 创建饼图
# plt.pie(survival_rates, labels=survival_rates.index, autopct='%1.1f%%')
#
# # 设置图表标题
# plt.title('Survival Rates by Passenger Class')
#
# # 显示图表
# plt.show()