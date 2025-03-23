# print(df.head()) #shows headers
# print(df.info()) #shows datatypes
# print(df.describe()) # shows extra information basic stats
# print(df.isnull().sum())
# print(df.head(5))
# Loading all columns
# print(df['Name'].iloc[0:5]) # Prints on difrent lines
# print(df['Name'].iloc[0:5].tolist()) # Prints it as a list
# print(df.iloc[2,1]) #looks at a specific location [x,y] x=row y collum
# loading row
# print(df.iloc[0:2]) # Printing amount of rows
# for index, row in df.iterrows():
#     print(index, row['Name'])
# Prints only the rows that have the data inside the collum
# df.loc[df['Genre'] == 'Shooter']
# print(df.sort_values('Name'))
# probeersel
# print(df.info())
