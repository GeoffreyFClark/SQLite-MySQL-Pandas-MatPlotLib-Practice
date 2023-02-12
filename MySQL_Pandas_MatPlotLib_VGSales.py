import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the MySQL server
cnx = mysql.connector.connect(user='<username>', password='<password>', host='<host>', database='<database>')
cursor = cnx.cursor()

# Retrieve the data from the table
df = pd.read_sql_query("SELECT * FROM vgsales", cnx)

# To see the first 5 rows of the dataframe
print(df.head())

# To get the shape of the dataframe (number of rows, number of columns)
print(df.shape)

# To get the summary statistics of numerical columns
print(df.describe())

# To get the number of unique values in each column
print(df.nunique())

# To check if there are any missing values
print(df.isnull().sum())

# To fill missing values with a specific value
df.fillna(0, inplace=True)

# To drop rows with missing values
df.dropna(inplace=True)


df["id"] = df["Name"] + " (" + df["Platform"] + " " + df["Year"].astype(str) + ")"
df = df.sort_values(by="Global_Sales", ascending=False)
df = df.head(20)

fig, ax = plt.subplots(figsize=(15, 7))
plt.subplots_adjust(bottom=0.5)
ax.bar(df.index, df["Global_Sales"], color="red")

ax.set_xlabel("Videogame Index")
ax.set_ylabel("Global Sales")
ax.set_xticks(df.index[:20])
ax.set_xticklabels(df["Name"][:20], rotation=90, fontsize=12)

plt.show()

# Commit the changes
cnx.commit()

# Close the connection
cursor.close()
cnx.close()



# To create a histogram
# df['column_name'].hist()
# plt.show()
#
# To create a bar chart
# df['column_name'].value_counts().plot(kind='bar')
# plt.show()
#
# To create a scatter plot
# plt.scatter(df['column_x'], df['column_y'])
# plt.show()
#
#
# To group data by one or multiple columns and calculate the sum of another column
# df.groupby(['column_x', 'column_y'])['column_z'].sum()
