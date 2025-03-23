import pandas as pd

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
# print(index, row['Name'])
# Prints only the rows that have the data inside the collum
# df.loc[df['Genre'] == 'Shooter']
# print(df.sort_values('Name'))
# probeersel
# print(df.info())


def cleaning_csv(df):
    # Identify all columns that end with "_Sales"
    sales_columns = df.columns[df.columns.str.endswith("_Sales")]

    # Fill missing values in sales columns with 0 and convert these columns from float to int
    df[sales_columns] = df[sales_columns].fillna(0).astype(int)

    # Calculate the average sales by summing the individual sales columns and dividing by 5
    # Parentheses ensure the sum is computed before the division
    df["Total_Sales_Average"] = (
        df["NA_Sales"]
        + df["EU_Sales"]
        + df["JP_Sales"]
        + df["Other_Sales"]
        + df["Global_Sales"]
    ) / 5

    # Clean the 'Year' column by filling missing values with 0 and converting the values to int
    df["Year"] = df["Year"].fillna(0).astype(int)

    # Optionally drop the original individual sales columns if they're no longer needed
    df = df.drop(
        columns=[
            "NA_Sales",
            "EU_Sales",
            "JP_Sales",
            "Other_Sales",
            "Global_Sales",
            "Publisher",
        ]
    )

    # Return the cleaned DataFrame
    return df


def main():
    # Load the CSV file into a DataFrame
    df = pd.read_csv("vgsales.csv")

    # Clean the DataFrame using the cleaning_csv function
    clean_df = cleaning_csv(df)
    print("Cleaned data preview")
    print(clean_df.head(50))


if __name__ == "__main__":
    main()
