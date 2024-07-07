## Bank Customer

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green)
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange) ![topics](https://img.shields.io/static/v1?label=Topics&message=data-analysis&color=blue)

#### 2.0 数据

|   id |  age | job          | marital  | education           | default | housing | loan | contact  | month |  ... | campaign | pdays | previous | poutcome    | emp_var_rate | cons_price_index | cons_conf_index | lending_rate3m | nr_employed | subscribe |
| ---: | ---: | :----------- | :------- | :------------------ | :------ | :------ | :--- | :------- | :---- | ---: | -------: | ----: | -------: | :---------- | -----------: | ---------------: | --------------: | -------------: | ----------: | :-------- |
|    1 |   51 | admin.       | divorced | professional.course | no      | yes     | yes  | cellular | aug   |  ... |        1 |   112 |        2 | failure     |          1.4 |            90.81 |          -35.53 |           0.69 |     5219.74 | no        |
|    2 |   50 | services     | married  | high.school         | unknown | yes     | no   | cellular | may   |  ... |        1 |   412 |        2 | nonexistent |         -1.8 |            96.33 |          -40.58 |           4.05 |     4974.79 | yes       |
|    3 |   48 | blue-collar  | divorced | basic.9y            | no      | no      | no   | cellular | apr   |  ... |        0 |  1027 |        1 | failure     |         -1.8 |            96.33 |          -44.74 |            1.5 |     5022.61 | no        |
|    4 |   26 | entrepreneur | single   | high.school         | yes     | yes     | yes  | cellular | aug   |  ... |       26 |   998 |        0 | nonexistent |          1.4 |            97.08 |          -35.55 |           5.11 |     5222.87 | yes       |
|    5 |   45 | admin.       | single   | university.degree   | no      | no      | no   | cellular | nov   |  ... |        1 |   240 |        4 | success     |         -3.4 |            89.82 |          -33.83 |           1.17 |      4884.7 | no        |

字段说明：

- id：每个客户的唯一标识符。这可以是一个客户编号或其他唯一代码，用于区分不同的客户。
- age：客户的年龄，以年为单位。
- job：客户的工作或职业。这是判断客户收入水平、经济稳定性和风险状况的重要指标。
- marital：客户的婚姻状况，包括已婚、单身、离异或丧偶等。婚姻状况可能与客户的财务决策和风险状况相关。
- education：客户的教育水平。教育水平通常与收入水平和风险状况相关联。
- default：客户是否有过违约记录。如果有违约，则可能标记为“是”，否则为“否”。
- housing：指示客户是拥有住房还是租房。这与客户的财务状况有一定关联。
- loan：表示客户是否有未偿还的贷款。这可以帮助银行了解客户的负债情况。
- contact：与客户的联系方式，如手机、电话、电子邮件等。
- month：数据收集或相关活动发生的月份。
- campaign：客户接收到的营销活动的数量。
- pdays：自上一次营销活动以来与客户最后一次联系的天数。
- previous：在过去一个月内与客户的联系次数。
- poutcome：上一次联系的结果，如“成功”、“失败”或“未发生”。

#### 2.1 查看训练数据的前5行和后5行

```python
# 查看前五行数据
train.head()

# 查看后五行数据
train.tail()
```

#### 2.2 输出各字段缺失值数量

```python
# 检测缺失值
missing_values = df.isnull().sum()

# 输出各字段的缺失值数量，其中Age、Cabin、Embarked存在缺失值
missing_values
```

#### 2.3 检测重复值

```python
# 检测重复值
duplicate_rows = df.duplicated()
duplicate_rows_count = duplicate_rows.sum()
print("重复行数:", duplicate_rows_count)
```

#### 2.4 基本统计分析

```python
# 基本统计分析(包含数量、均值、方差、最小值、最大值等)
statistics = df.describe()
print(statistics)
```
|       | id        | age       | duration  | campaign  | pdays     | previous  | emp_var_rate | cons_price_index | cons_conf_index | lending_rate3m | nr_employed |
| ----- | --------- | --------- | --------- | --------- | --------- | --------- | ------------ | ---------------- | --------------- | -------------- | ----------- |
| count | 22500.000 | 22500.000 | 22500.000 | 22500.000 | 22500.000 | 22500.000 | 22500.000    | 22500.000        | 22500.000       | 22500.000      | 22500.000   |
| mean  | 11250.500 | 40.408    | 1146.304  | 3.365     | 773.992   | 1.316     | 0.079        | 93.549           | -39.877         | 3.302          | 5137.211    |
| std   | 6495.335  | 12.086    | 1432.432  | 7.224     | 326.934   | 1.919     | 1.574        | 2.806            | 5.805           | 1.612          | 170.671     |
| min   | 1.000     | 16.000    | 0.000     | 0.000     | 0.000     | 0.000     | -3.400       | 87.640           | -53.280         | 0.600          | 4715.420    |
| 25%   | 5625.750  | 32.000    | 143.000   | 1.000     | 557.750   | 0.000     | -1.800       | 91.190           | -44.160         | 1.430          | 5008.510    |
| 50%   | 11250.500 | 38.000    | 353.000   | 1.000     | 964.000   | 0.000     | 1.100        | 93.540           | -40.600         | 3.920          | 5133.955    |
| 75%   | 16875.250 | 47.000    | 1873.000  | 3.000     | 1005.000  | 2.000     | 1.400        | 95.920           | -35.798         | 4.830          | 5267.678    |
| max   | 22500.000 | 101.000   | 5149.000  | 57.000    | 1048.000  | 6.000     | 1.400        | 99.460           | -25.550         | 5.270          | 5489.500    |

#### 2.5 柱状图：按教育程度和婚姻状况进行分组

```python
import matplotlib.pyplot as plt

# 按教育程度和婚姻状况进行分组，并计算每个组的数量
grouped_data = df.groupby(['education', 'marital']).size().unstack()

# 绘制柱状图
grouped_data.plot(kind='bar', stacked=True)

# 设置图形属性
plt.xlabel('Education')
plt.ylabel('Count')
plt.title('Marital Status by Education')
plt.xticks(rotation=45)

# 显示图形
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic1_martial_status_by_education.png?raw=true)

分组数据（`grouped_data`）：

| education           | marital.divorced | marital.married | marital.single | marital.unknown |
| ------------------- | ---------------- | --------------- | -------------- | --------------- |
| basic.4y            | 304              | 1724            | 255            | 39              |
| basic.6y            | 145              | 971             | 196            | 37              |
| basic.9y            | 337              | 2185            | 706            | 38              |
| high.school         | 641              | 2641            | 1705           | 44              |
| illiterate          | 29               | 42              | 45             | 45              |
| professional.course | 375              | 1669            | 772            | 37              |
| university.degree   | 714              | 3379            | 2385           | 46              |
| unknown             | 113              | 567             | 280            | 34              |

#### 2.6  【分析一】统计高中学历婚姻状况的比例

```python
# 筛选出高中学历的数据
high_school_data = df[df['education'] == 'high.school']

# 统计高中学历下不同婚姻状况的数量
grouped_data = high_school_data.groupby('marital').size().reset_index(name='count')

# 计算比例
total_count = grouped_data['count'].sum()
grouped_data['ratio'] = grouped_data['count'] / total_count

# 输出统计结果
print(grouped_data[['marital', 'ratio']])
```

输出结果：

```
    marital     ratio
0  divorced  0.127410
1   married  0.524945
2    single  0.338899
3   unknown  0.008746
```

#### 2.7  【分析一的可视化】使用饼图表示高中学历婚姻状况的比例
```python
plt.figure(figsize=(6, 6))
labels = grouped_data['marital']
sizes = grouped_data['count']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Marital Status of High School Graduates')
plt.show()

# 【分析一的结论】高中学历中结婚的比例达到了52.5%
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic2_marital_status_of_high_school_graduates.png?raw=true)

#### 【分析二】统计每个职业的分布情况

```python
# 统计每个职业的人数
job_counts = df['job'].value_counts()

# 根据人数进行排序
job_counts = job_counts.sort_values()

job_counts
```

输出结果：

```
job
unknown           274
student           573
unemployed        647
housemaid         657
self-employed     836
entrepreneur      863
retired          1006
management       1600
services         2083
technician       3530
blue-collar      4874
admin.           5557
Name: count, dtype: int64
```

人数最多的职业占比：

```python
print(f'{round(max(job_counts) / df["job"].count() * 100,2)}%')
# 24.7%
```

【分析二的结论】该份数据中职业为管理人员(admin.)的人数最多，达到了5557，占比 24.7%

#### 【分析二的可视化】使用统计图表示各个职业的人数分布情况

```python
plt.figure(figsize=(10, 6))
job_counts.plot(kind='barh')
plt.title('Number of People by Job')
plt.xlabel('Count')
plt.ylabel('Job')
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic3_number_of_people_by_job.png?raw=true)

#### 【分析三】统计20-30岁之间用户订阅该产品的比例分布

```python
# 筛选年龄在 20-30 岁之间的数据
age_filter = (df['age'] >= 20) & (df['age'] <= 30)
subset_df = df[age_filter]

# 计算各个年龄的订阅比例
age_counts = subset_df['age'].value_counts()
age_proportions = (age_counts / age_counts.sum()) * 100

age_proportions
```

输出结果：

```
age
30    21.876399
29    18.696820
28    13.949843
27    11.867443
26     9.740260
25     7.120466
24     6.829378
23     4.343932
22     2.642185
21     1.724138
20     1.209136
Name: count, dtype: float64
```

#### 【分析三的可视化】使用饼图绘制20-30岁之间用户订阅该产品的比例分布

```python
plt.figure(figsize=(8, 6))
plt.pie(age_proportions, labels=age_proportions.index, autopct='%1.1f%%')
plt.title('Proportion of Subscribers Aged 20-30')
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic4_proportion_of_subscribers_aged_20_30.png?raw=true)

#### 【分析三的可视化】使用柱状图绘制20-30岁之间用户订阅该产品的比例分布

```python
plt.figure(figsize=(8, 6))
plt.bar(age_counts.index, age_counts.values)
plt.xlabel('Age')
plt.ylabel('Number of Subscribers')
plt.title('Distribution of Subscribers Aged 20-30')
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic5_distribution_of_subscribers_aged_20_30.png?raw=true)

#### 【分析四】统计拥有房屋贷款、个人贷款、房屋贷款&个人贷款的人数，并计算其占比总人数

```python
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
```

输出结果：

```
拥有房屋贷款的人数: 11568
拥有个人贷款的人数: 3657
同时拥有房屋贷款和个人贷款的人数: 2055
总人数: 22500
拥有房屋贷款的人数占比总人数: 51.41%
拥有个人贷款的人数占比总人数: 16.25%
同时拥有房屋贷款和个人贷款的人数占比总人数: 9.13%
```

#### 【分析四的可视化】使用柱状图统计拥有房屋贷款、个人贷款、房屋贷款&个人贷款的人数，并计算其占比总人数

```python
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
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/bank_customer/pic6_count_of_individuals_with_housing_loan_and_personal_loan.png?raw=true)

【分析四的结论】

```
# 拥有房屋贷款的人数: 11568
# 拥有个人贷款的人数: 3657
# 同时拥有房屋贷款和个人贷款的人数: 2055
# 总人数: 22500
# 拥有房屋贷款的人数占比总人数: 51.41%
# 拥有个人贷款的人数占比总人数: 16.25%
# 同时拥有房屋贷款和个人贷款的人数占比总人数: 9.13%
```
