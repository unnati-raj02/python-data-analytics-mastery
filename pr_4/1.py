import pandas as pd
names = ["rohit sharma", "PRIYA MEHTA", "Arjun patel", "Sneha joshi"]

ages = ["20", "21", "19", "22"]
departments = ["computer science", "information technology", "electronics", "mechanical"]

dates = ["15-07-2024", "22-08-2023", "10-01-2025", "05-11-2022"]

data = {
'Name': names,
'Age': ages,
'Department': departments,
'Admission_Date': dates
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)
print("\nOriginal Data Types:")
print(df.dtypes)

df['Age'] = df['Age'].astype(int)

df['Name'] = df['Name'].str.strip()


df['Name'] = df['Name'].str.title()
df['Department'] = df['Department'].str.title()

df['Admission_Date'] = pd.to_datetime(df['Admission_Date'],format='%d-%m-%Y')

df['Year'] = df['Admission_Date'].dt.year

df['Month'] = df['Admission_Date'].dt.month
df['Day'] = df['Admission_Date'].dt.day

print("\nTransformed Data:")
print(df)
print("\nTransformed Data Types:")
print(df.dtypes)