import pandas as pd
import matplotlib.pyplot as plt
# 【分析六】不同登船港口的乘客生存情况

# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 对 Embarked 的缺失值进行处理
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 统计不同港口上船的乘客人数以及生还人数
embarked_count = df.groupby('Embarked')['PassengerId'].count()
survived_count = df.groupby('Embarked')['Survived'].sum()

# 计算不同港口上船的乘客生还率
survival_rate = survived_count / embarked_count

print(survival_rate)

# 【分析六的可视化】使用柱状图表示不同登船港口的乘客生存情况
# 可视化结果
plt.bar(['C', 'Q', 'S'], survival_rate, color=['#2a9df4', '#f44336', '#ffc107'])
plt.xlabel('Embarked')
plt.ylabel('Survival rate')
plt.title('Survival Rate of Different Embarked Ports')
plt.ylim(0.0, 1.0)
plt.show()