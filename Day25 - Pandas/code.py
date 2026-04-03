# # with open("Day25 - Pandas/weather_data.csv") as file:
# #     files = file.read()

# import csv
# with open("Day25 - Pandas/weather_data.csv") as data_file:
#     files = csv.reader(data_file)
#     temp = []
#     for row in files:
#         if(row[1] != 'temp'):
#             temp.append(int(row[1]))

# import pandas
# data = pandas.read_csv("Day25 - Pandas/weather_data.csv")

# print(data)
# print(data['temp'])
# print(type(data))

# data_dict = data.to_dict()
# print(type(data_dict))

# print(data_dict)

# temp_list = data['temp'].to_list()

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data['temp'].mean())

# print(data['condition'])

# # get data in row
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()].day)

# # pandas ada 2 jenis, dataframe sama series

import pandas

squirrel_data = pandas.read_csv("Day25 - Pandas/squirrel_park.csv")
# print(squirrel_data.head())
print(squirrel_data.columns)

fur_color = squirrel_data['Primary Fur Color'].unique()
# print(fur_color)

furs = []

for fur in fur_color:
    temp = [fur, len(squirrel_data[squirrel_data['Primary Fur Color'] == fur])]
    furs.append(temp)

    # # another way
    # temp = [fur, squirrel_data['Primary Fur Color'].value_counts()]
    # furs.append(temp)
()

for fur in furs:
    print(fur)

df = pandas.DataFrame(furs, columns = ['Fur Color', 'Count'])
print(df)

df.to_csv('Day25 - Pandas/task1.csv')

# import pandas as pd

# # =========================
# # LOAD / SAVE
# # =========================

# df = pd.read_csv("file.csv")
# df.to_csv("output.csv", index=False)

# # =========================
# # QUICK INSPECTION
# # =========================

# df.head()              # first 5 rows
# df.tail()              # last 5 rows
# df.columns             # column names
# df.info()              # structure + data types
# df.describe()          # numeric summary
# df.shape               # (rows, columns)

# # Show all columns
# pd.set_option("display.max_columns", None)

# # =========================
# # SELECTING DATA
# # =========================

# df["ColumnName"]                     # single column
# df[["Col1", "Col2"]]                 # multiple columns
# df.loc[0]                            # row by label
# df.iloc[0]                           # row by index
# df[df["Age"] > 30]                   # filter rows

# # =========================
# # BASIC OPERATIONS
# # =========================

# df["Column"].unique()                # unique values
# df["Column"].value_counts()          # count categories
# df["Column"].mean()
# df["Column"].sum()
# df["Column"].max()
# df["Column"].min()

# # Count rows after filter
# len(df[df["Column"] == "Value"])

# # =========================
# # GROUPING
# # =========================

# df.groupby("Column").size()

# df.groupby("Column")["OtherColumn"].mean()

# df.groupby("Column").size().reset_index(name="Count")

# # =========================
# # CREATING DATAFRAME
# # =========================

# data = [
#     ["Gray", 100],
#     ["Black", 80]
# ]

# df = pd.DataFrame(data, columns=["Fur Color", "Count"])

# # OR cleaner (dict style)
# data = [
#     {"Fur Color": "Gray", "Count": 100},
#     {"Fur Color": "Black", "Count": 80}
# ]

# df = pd.DataFrame(data)

# # =========================
# # MODIFYING DATA
# # =========================

# df["NewColumn"] = df["OldColumn"] * 2

# df.rename(columns={"OldName": "NewName"}, inplace=True)

# df.drop(columns=["ColumnToRemove"], inplace=True)

# # =========================
# # HANDLE MISSING VALUES
# # =========================

# df.isna().sum()         # count NaN per column
# df.dropna()             # remove rows with NaN
# df.fillna(0)            # replace NaN

# # =========================
# # SORTING
# # =========================

# df.sort_values("Column", ascending=False)

# # =========================
# # RESET INDEX
# # =========================

# df.reset_index(drop=True, inplace=True)