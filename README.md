## 数据分析练习

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green)
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange) ![topics](https://img.shields.io/static/v1?label=Topics&message=data-analysis&color=blue)



### 1. Titanic 数据

| PassengerId | Survived | Pclass | Name                              | Sex    | Age | SibSp | Parch | Ticket  | Fare    | Cabin | Embarked |
|-------------|----------|--------|-----------------------------------|--------|-----|-------|-------|---------|---------|-------|----------|
| 172         | 1        | 3      | Johnson       | female | 1.0 | 1     | 1     | 347742  | 11.1333 | NaN   | S        |
| 524         | 0        | 3      | Kassem                 | male   | NaN | 0     | 0     | 2700    | 7.2292  | NaN   | C        |
| 452         | 0        | 1      | Foreman    | male   | 30.0| 0     | 0     | 113051  | 27.7500 | C111  | C        |
| 170         | 0        | 1      | Van          | male   | 61.0| 0     | 0     | 111240  | 33.5000 | B19   | S        |
| 620         | 0        | 3      | Yasbeck                | male   | 27.0| 1     | 0     | 2659    | 14.4542 | NaN   | C        |

字段说明：

- PassengerId: 乘客ID
- Survived: 是否存活
- Pclass: 船票等级
- Name: 姓名
- Sex: 性别
- Age: 年龄
- SibSp: 同行的兄弟姐妹/配偶数
- Parch: 同行的父母/子女数
- Ticket: 票号
- Fare: 票价
- Cabin: 船舱号
- Embarked: 登船港口

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

【pic2】

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

【pic3】

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

【pic4】

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

【pic5】

### 2.Bank Customer 数据

|   id |   age | job          | marital   | education          | default   | housing   | loan   | contact   | month   |   ... |   campaign |   pdays |   previous | poutcome   |   emp_var_rate |   cons_price_index |   cons_conf_index |   lending_rate3m |   nr_employed | subscribe   |
|-----:|------:|:-------------|:----------|:-------------------|:----------|:----------|:--------|:-----------|:--------|-------:|-----------:|--------:|-----------:|:-----------|---------------:|-------------------:|------------------:|------------------:|---------------:|:------------|
|    1 |    51 | admin.       | divorced  | professional.course | no        | yes       | yes     | cellular   | aug     |   ... |          1 |     112 |          2 | failure    |            1.4 |              90.81 |            -35.53 |              0.69 |        5219.74 | no          |
|    2 |    50 | services     | married   | high.school        | unknown   | yes       | no      | cellular   | may     |   ... |          1 |     412 |          2 | nonexistent|           -1.8 |              96.33 |            -40.58 |              4.05 |        4974.79 | yes         |
|    3 |    48 | blue-collar  | divorced  | basic.9y           | no        | no        | no      | cellular   | apr     |   ... |          0 |    1027 |          1 | failure    |           -1.8 |              96.33 |            -44.74 |              1.5  |        5022.61 | no          |
|    4 |    26 | entrepreneur | single    | high.school        | yes       | yes       | yes     | cellular   | aug     |   ... |         26 |     998 |          0 | nonexistent|            1.4 |              97.08 |            -35.55 |              5.11 |        5222.87 | yes         |
|    5 |    45 | admin.       | single    | university.degree  | no        | no        | no      | cellular   | nov     |   ... |          1 |     240 |          4 | success    |           -3.4 |              89.82 |            -33.83 |              1.17 |        4884.7  | no          |