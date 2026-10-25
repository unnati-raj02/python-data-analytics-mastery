
import pandas as pd

def calculate_average(marks):
    return sum(marks) / len(marks)

names = ["Riya","Arjun","Kavya","Sameer"]
marks = [45,89,76,90]

df = pd.DataFrame({
    "name":names,
    "marks":marks
})

def result(mark):
    if mark >= 75:
     return "Distinction"
    elif mark >= 50:
     return "Pass"
    else:
     return "Fail"

df["result"] = df["marks"].apply(result)

print("\nDataset:")
print(df)
print("\nStudent Analysis:")

for mark in marks:
 if mark >= 75:
    print(mark, "Distinction")
 elif mark >= 50:
     print(mark, "Pass")
 else:
       print(mark, "Fail")

print("\nAverage Marks:", calculate_average(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
