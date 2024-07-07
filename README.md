## 数据分析练习

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green)
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange) ![topics](https://img.shields.io/static/v1?label=Topics&message=data-analysis&color=blue)



### 1. Titanic

#### 1.1 抽取80%的数据作为训练数据

- 读取全量数据集
- 使用`sample`方法进行抽取训练集，设置随机状态参数
- 使用`to_csv`保存训练集到新的csv文件

```python
import pandas as pd

# 读取 Titanic.csv 文件
df = pd.read_csv('Titanic.csv')

# 随机抽取80%的数据
train = df.sample(frac=0.8, random_state=123)

# 将抽取的数据保存到 train.csv 文件中
train.to_csv('train.csv', index=False)
```

#### 1.2 查看训练数据的前5行和后5行

```python
# 查看前五行数据
train.head()

# 查看后五行数据
train.tail()
```

#### 1.3 输出各字段缺失值数量

```python
# 读取 Titanic.csv 文件
df = pd.read_csv('train.csv')

# 检测缺失值
missing_values = df.isnull().sum()

# 输出各字段的缺失值数量，其中Age、Cabin、Embarked存在缺失值
print(missing_values)
```

输出结果：

```
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            139
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          555
Embarked         1
```

#### 1.4 对缺失值进行填充

- 使用`fillna`方法填充缺失值，第一个参数即为缺失值的默认值，通常可以考虑均值/指定值/众数等等
- 其中`df['Embarked'].mode()[0]` 指的是 `Embarked` 列中的众数（即出现频率最高的值）

```python
# 对上述存在缺失值的字段进行填补
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Cabin'].fillna('Unknown', inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
```

#### 1.5 检测重复值

```python
# 检测重复值
duplicate_rows = df.duplicated()
duplicate_rows_count = duplicate_rows.sum()
print("重复行数:", duplicate_rows_count)
```

#### 1.6 数据降重

```python
df.drop_duplicates(inplace=True)
```

#### 1.7 基本统计分析(包含数量、均值、方差、最小值、最大值等)
```python
statistics = df.describe()
print(statistics)
```

|      PassengerId |    Survived |     Pclass |        Age |    SibSp |      Parch |       Fare |
|-----------------:|------------:|-----------:|-----------:|---------:|-----------:|-----------:|
|       713.000000 |  713.000000 | 713.000000 |  713.000000 | 0.507714 |  0.360449 |  31.026296 |
|       451.237027 |    0.366059 |   2.312763 |   29.422613 | 1.086309 |  0.781065 |  47.260244 |
|       257.904310 |    0.482064 |   0.834015 |   12.728972 | 0.000000 |  0.000000 |   0.000000 |
|         1.000000 |    0.000000 |   1.000000 |    0.420000 | 0.000000 |  0.000000 |   0.000000 |
|       228.000000 |    0.000000 |   2.000000 |   22.000000 | 0.000000 |  0.000000 |   7.895800 |
|       455.000000 |    0.000000 |   3.000000 |   29.422613 | 0.000000 |  0.000000 |  13.862500 |
|       677.000000 |    1.000000 |   3.000000 |   35.000000 | 1.000000 |  0.000000 |  30.500000 |
|       891.000000 |    1.000000 |   3.000000 |   74.000000 | 8.000000 |  6.000000 | 512.329200 |

#### 1.8 【分析一】海难发生前，一等舱有 XX 人，二等舱 XX 人，三等舱 XX 人，分别占总人数的 XX%，XX%，XX%

```python
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
```

输出结果：

```
一等舱人数：171
二等舱人数：148
三等舱人数：394
一等舱乘客占比：23.98%
二等舱乘客占比：20.76%
三等舱乘客占比：55.26%
```

分析题一答案：

```
# 【分析一的结论】
# 一等舱人数：171
# 二等舱人数：148
# 三等舱人数：394
# 一等舱乘客占比：23.98%
# 二等舱乘客占比：20.76%
# 三等舱乘客占比：55.26%
```

#### 1.9 【分析二】海难发生后，一等舱、二等舱、三等舱的乘客人数剩余 XX、XX、XX 人，分别占总人数的 XX%，XX%，XX%

```python
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
```

输出结果：

```
海难发生后，一等舱乘客剩余人数： 106
海难发生后，二等舱乘客剩余人数： 65
海难发生后，三等舱乘客剩余人数： 90
海难发生后，一等舱乘客占比： 40.61%
海难发生后，二等舱乘客占比： 24.9%
海难发生后，三等舱乘客占比： 34.48%
```

分析题二答案：

```
# 【分析二的结论】
# 海难发生后，一等舱乘客剩余人数： 106
# 海难发生后，二等舱乘客剩余人数： 65
# 海难发生后，三等舱乘客剩余人数： 90
# 海难发生后，一等舱乘客占比： 40.61%
# 海难发生后，二等舱乘客占比： 24.9%
# 海难发生后，三等舱乘客占比： 34.48%
```

####  1.10 【分析三】一等舱生还率为 XX%，二等舱为 XX%，三等舱为 XX%。

```python
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
```

输出结果：

```
一等舱生还率为 61.99%
二等舱生还率为 43.92%
三等舱生还率为 22.84%
```

分析题三答案：

```
# 【分析三的结论】
# 一等舱生还率为 61.99%
# 二等舱生还率为 43.92%
# 三等舱生还率为 22.84%
# 可见客舱等级越高，生还率越高。
```

####  1.11【分析三的可视化】使用柱状图表示不同舱位的生还率

```python
import matplotlib.pyplot as plt

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
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/titanic/pic1_survival_rates_by_passenger_class.png?raw=true)



####  1.12【分析四】乘客的性别与生还率关系

```python
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 计算不同性别的生还人数
survived_counts = df[df['Survived'] == 1]['Sex'].value_counts()
total_counts = df['Sex'].value_counts()

# 计算不同性别的生还率
survival_rates = round((survived_counts / total_counts) * 100, 2)

survival_rates
```

输出结果：

```
Sex
female    72.13
male      18.12
Name: count, dtype: float64
```

分析题四答案：

```
# 【分析四的结论】：
# 男性的生还率为18.12%
# 女性的生还率为72.13%
# 女性乘客可能更容易生还。
```

####  1.13【分析四的可视化】使用柱状图表示乘客的性别与生还率关系

```python
# 创建柱状图
plt.bar(survival_rates.index, survival_rates.values)

# 设置图表标题和标签
plt.title('Survival Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate (%)')

# 显示图表
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/titanic/pic2_survival_rates_by_gender.png?raw=true)

####  1.14 【分析五】年龄与生还率关系

```python
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

survival_rates
```

输出结果：

```
AgeGroup
Adult       36.27
Children    55.56
Teenager    47.22
Elderly      0.00
Name: count, dtype: float64
```

分析题五答案：

```
# 【分析五的结论】：根据年龄段进行分类，不同年龄段的乘客生还率如下：
# 儿童（0-12岁）的生还率为55.56%
# 少年（12-18岁）的生还率为47.22%
# 成人（18-65岁）的生还率为36.27%
# 老年（65-100岁）的生还率为0.00%
```

#### 1.15 【分析五的可视化】使用柱状图表示年龄与生还率关系

```python
# 创建柱状图
plt.bar(survival_rates.index, survival_rates.values)

# 设置图表标题和标签
plt.title('Survival Rates by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate (%)')

# 显示图表
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/titanic/pic3_survival_rates_by_age_group.png?raw=true)

#### 1.16【分析六】不同登船港口的乘客生存情况

```python
# 读取 train.csv 文件
df = pd.read_csv('train.csv')

# 对 Embarked 的缺失值进行处理
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 统计不同港口上船的乘客人数以及生还人数
embarked_count = df.groupby('Embarked')['PassengerId'].count()
survived_count = df.groupby('Embarked')['Survived'].sum()

# 计算不同港口上船的乘客生还率
survival_rate = survived_count / embarked_count

survival_rate
```

输出结果：

```
Embarked
C    0.561538
Q    0.333333
S    0.321293
dtype: float64
```

#### 1.17 【分析六的可视化】使用柱状图表示不同登船港口的乘客生存情况

```python
# 可视化结果
plt.bar(['C', 'Q', 'S'], survival_rate, color=['#2a9df4', '#f44336', '#ffc107'])
plt.xlabel('Embarked')
plt.ylabel('Survival rate')
plt.title('Survival Rate of Different Embarked Ports')
plt.ylim(0.0, 1.0)
plt.show()
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/titanic/pic4_survival_rate_of_different_embarked_ports.png?raw=true)

#### 1.18【分析七】登船港口为C的男性和女性的生存情况

```python
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
```

输出结果：

```
登船港口为 C 的男性生存人数: 22
登船港口为 C 的女性生存人数: 51
```

#### 1.19 【分析七的可视化】使用柱状图表示登船港口为C的男性和女性的生存情况

```python
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
```

![](https://github.com/jm199504/Data-Analysis-Practice/blob/main/images/titanic/pic5_survival_count_of_male_and_female_passengers_embarked_at_C.png?raw=true)

### 2.Bank Customer 数据

|   id |   age | job          | marital   | education          | default   | housing   | loan   | contact   | month   |   ... |   campaign |   pdays |   previous | poutcome   |   emp_var_rate |   cons_price_index |   cons_conf_index |   lending_rate3m |   nr_employed | subscribe   |
|-----:|------:|:-------------|:----------|:-------------------|:----------|:----------|:--------|:-----------|:--------|-------:|-----------:|--------:|-----------:|:-----------|---------------:|-------------------:|------------------:|------------------:|---------------:|:------------|
|    1 |    51 | admin.       | divorced  | professional.course | no        | yes       | yes     | cellular   | aug     |   ... |          1 |     112 |          2 | failure    |            1.4 |              90.81 |            -35.53 |              0.69 |        5219.74 | no          |
|    2 |    50 | services     | married   | high.school        | unknown   | yes       | no      | cellular   | may     |   ... |          1 |     412 |          2 | nonexistent|           -1.8 |              96.33 |            -40.58 |              4.05 |        4974.79 | yes         |
|    3 |    48 | blue-collar  | divorced  | basic.9y           | no        | no        | no      | cellular   | apr     |   ... |          0 |    1027 |          1 | failure    |           -1.8 |              96.33 |            -44.74 |              1.5  |        5022.61 | no          |
|    4 |    26 | entrepreneur | single    | high.school        | yes       | yes       | yes     | cellular   | aug     |   ... |         26 |     998 |          0 | nonexistent|            1.4 |              97.08 |            -35.55 |              5.11 |        5222.87 | yes         |
|    5 |    45 | admin.       | single    | university.degree  | no        | no        | no      | cellular   | nov     |   ... |          1 |     240 |          4 | success    |           -3.4 |              89.82 |            -33.83 |              1.17 |        4884.7  | no          |

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
|       | id        | age      | duration | campaign | pdays | previous | emp_var_rate | cons_price_index | cons_conf_index | lending_rate3m | nr_employed |
|-------|-----------|----------|----------|----------|-------|----------|--------------|------------------|-----------------|----------------|-------------|
| count | 22500.000 | 22500.000| 22500.000| 22500.000| 22500.000| 22500.000| 22500.000| 22500.000| 22500.000| 22500.000| 22500.000|
| mean  | 11250.500 | 40.408   | 1146.304 | 3.365    | 773.992| 1.316    | 0.079    | 93.549    | -39.877   | 3.302  | 5137.211|
| std   | 6495.335  | 12.086   | 1432.432 | 7.224    | 326.934| 1.919    | 1.574    | 2.806     | 5.805     | 1.612  | 170.671 |
| min   | 1.000     | 16.000   | 0.000    | 0.000    | 0.000  | 0.000    | -3.400   | 87.640    | -53.280   | 0.600  | 4715.420|
| 25%   | 5625.750  | 32.000   | 143.000  | 1.000    | 557.750| 0.000    | -1.800   | 91.190    | -44.160   | 1.430  | 5008.510|
| 50%   | 11250.500 | 38.000   | 353.000  | 1.000    | 964.000| 0.000    | 1.100    | 93.540    | -40.600   | 3.920  | 5133.955|
| 75%   | 16875.250 | 47.000   | 1873.000 | 3.000    | 1005.000| 2.000   | 1.400    | 95.920    | -35.798   | 4.830  | 5267.678|
| max   | 22500.000 | 101.000  | 5149.000 | 57.000   | 1048.000| 6.000   | 1.400    | 99.460    | -25.550   | 5.270  | 5489.500|

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

