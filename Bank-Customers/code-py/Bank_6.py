import pandas as pd
import matplotlib.pyplot as plt

# 【分析四】统计拥有房屋贷款、个人贷款、房屋贷款&个人贷款的人数，并计算其占比总人数
# 读取 Bank_customers.csv 文件
df = pd.read_csv('Bank_customers.csv')

# 计算同时拥有房屋贷款和个人贷款的人数
housing_count = len(df[(df['housing'] == 'yes')])
loan_count = len(df[(df['loan'] == 'yes')])
both_loans_count = len(df[(df['housing'] == 'yes') & (df['loan'] == 'yes')])

# 计算占比总人数
total_count = len(df)
housing_loans_ratio = round(housing_count / total_count * 100, 2)
loans_ratio = round(loan_count / total_count * 100, 2)
both_loans_ratio = round(both_loans_count / total_count * 100, 2)

# 输出结果
print(f"拥有房屋贷款的人数: {housing_count}")
print(f"拥有个人贷款的人数: {loan_count}")
print(f"同时拥有房屋贷款和个人贷款的人数: {both_loans_count}")
print(f"总人数: {total_count}")
print(f"拥有房屋贷款的人数占比总人数: {housing_loans_ratio}%")
print(f"拥有个人贷款的人数占比总人数: {loans_ratio}%")
print(f"同时拥有房屋贷款和个人贷款的人数占比总人数: {both_loans_ratio}%")

# 【分析四的可视化】使用柱状图统计拥有房屋贷款、个人贷款、房屋贷款&个人贷款的人数，并计算其占比总人数

# 创建柱状图数据
labels = ['Housing', 'Loan', 'Both']
counts = [housing_count, loan_count, both_loans_count]

# 设置柱状图参数
x = range(len(labels))
width = 0.5

# 绘制柱状图
plt.bar(x, counts, width, align='center')
plt.xticks(x, labels)
plt.xlabel('Loan Type')
plt.ylabel('Count')
plt.title('Count of Individuals with Housing Loan and Personal Loan')

# 添加数据标签
for i, count in enumerate(counts):
    plt.text(x[i], count, str(count), ha='center', va='bottom')

# 显示图形
plt.show()

# 【分析四的结论】
# 拥有房屋贷款的人数: 11568
# 拥有个人贷款的人数: 3657
# 同时拥有房屋贷款和个人贷款的人数: 2055
# 总人数: 22500
# 拥有房屋贷款的人数占比总人数: 51.41%
# 拥有个人贷款的人数占比总人数: 16.25%
# 同时拥有房屋贷款和个人贷款的人数占比总人数: 9.13%
