import pandas as pd
# 【分析一】海难发生前，一等舱有 XX 人，二等舱 XX 人，三等舱 XX 人，分别占总人数的 XX%，XX%，XX%
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 统计海难发生前不同舱位的乘客人数
first_class_count = df[df['Pclass'] == 1]['PassengerId'].count()
second_class_count = df[df['Pclass'] == 2]['PassengerId'].count()
third_class_count = df[df['Pclass'] == 3]['PassengerId'].count()

# 计算不同舱位的乘客人数占总人数的比例，并保留2位小数
total_passengers = df['PassengerId'].count()
first_class_percent = round((first_class_count / total_passengers) * 100, 2)
second_class_percent = round((second_class_count / total_passengers) * 100, 2)
third_class_percent = round((third_class_count / total_passengers) * 100, 2)

# 打印结果
print(f"一等舱人数：{first_class_count}")
print(f"二等舱人数：{second_class_count}")
print(f"三等舱人数：{third_class_count}")
print(f"一等舱乘客占比：{first_class_percent}%")
print(f"二等舱乘客占比：{second_class_percent}%")
print(f"三等舱乘客占比：{third_class_percent}%")

# 【分析一的结论】
# 一等舱人数：171
# 二等舱人数：148
# 三等舱人数：394
# 一等舱乘客占比：23.98%
# 二等舱乘客占比：20.76%
# 三等舱乘客占比：55.26%