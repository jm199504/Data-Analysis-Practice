import pandas as pd
import matplotlib.pyplot as plt

# 【分析七】登船港口为C的男性和女性的生存情况
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 筛选登船港口为 C 的数据
embarked_c_df = df[df['Embarked'] == 'C']

# 统计登船港口为 C 的男性和女性生存情况
male_survived = embarked_c_df[(embarked_c_df['Sex'] == 'male') & (embarked_c_df['Survived'] == 1)]
female_survived = embarked_c_df[(embarked_c_df['Sex'] == 'female') & (embarked_c_df['Survived'] == 1)]

# 输出结果
print("登船港口为 C 的男性生存人数:", len(male_survived))
print("登船港口为 C 的女性生存人数:", len(female_survived))

# 【分析七的可视化】使用柱状图表示登船港口为C的男性和女性的生存情况

# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 筛选登船港口为 C 的数据
embarked_c_df = df[df['Embarked'] == 'C']

# 统计登船港口为 C 的男性和女性生存情况
male_survived = embarked_c_df[(embarked_c_df['Sex'] == 'male') & (embarked_c_df['Survived'] == 1)]
female_survived = embarked_c_df[(embarked_c_df['Sex'] == 'female') & (embarked_c_df['Survived'] == 1)]

# 可视化结果
labels = ['Male', 'Female']
survived_counts = [len(male_survived), len(female_survived)]

plt.bar(labels, survived_counts, color=['#2196f3', '#f44336'])
plt.xlabel('Gender')
plt.ylabel('Survived Count')
plt.title('Survival Count of Male and Female Passengers Embarked at C')
plt.show()