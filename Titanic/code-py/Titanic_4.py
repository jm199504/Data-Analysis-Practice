import pandas as pd
# 【分析二】海难发生后，一等舱、二等舱、三等舱的乘客人数剩余 XX、XX、XX 人，分别占总人数的 XX%，XX%，XX%
# 读取 Titanic.csv 文件
df = pd.read_csv('train.csv')

# 统计海难发生后不同舱位的乘客人数
first_class_survived = df[(df['Pclass'] == 1) & (df['Survived'] == 1)]['PassengerId'].count()
second_class_survived = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]['PassengerId'].count()
third_class_survived = df[(df['Pclass'] == 3) & (df['Survived'] == 1)]['PassengerId'].count()

# 计算不同舱位的乘客人数占总人数的比例，并保留2位小数
total_passengers_survived = df[df['Survived'] == 1]['PassengerId'].count()
first_class_percent_survived = round((first_class_survived / total_passengers_survived) * 100, 2)
second_class_percent_survived = round((second_class_survived / total_passengers_survived) * 100, 2)
third_class_percent_survived = round((third_class_survived / total_passengers_survived) * 100, 2)

# 打印结果
print(f"海难发生后，一等舱乘客剩余人数： {first_class_survived}")
print(f"海难发生后，二等舱乘客剩余人数： {second_class_survived}")
print(f"海难发生后，三等舱乘客剩余人数： {third_class_survived}")
print(f"海难发生后，一等舱乘客占比： {first_class_percent_survived}%")
print(f"海难发生后，二等舱乘客占比： {second_class_percent_survived}%")
print(f"海难发生后，三等舱乘客占比： {third_class_percent_survived}%")

# 【分析二的结论】
# 海难发生后，一等舱乘客剩余人数： 106
# 海难发生后，二等舱乘客剩余人数： 65
# 海难发生后，三等舱乘客剩余人数： 90
# 海难发生后，一等舱乘客占比： 40.61%
# 海难发生后，二等舱乘客占比： 24.9%
# 海难发生后，三等舱乘客占比： 34.48%