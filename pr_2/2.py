import pandas as pd
def calculate_average(marks):
    return sum(marks)/len(marks)

names = ["Riya","Arjun","kavya","Sameer"]
marks = [82,89,90,67]
df = pd.DataFrame({
    "Name":names,
    "Marks":marks
})

def result(mark):
    if mark >= 75:
        return "distinction"
    elif mark >= 50:
        return "pass"
    else:
        return"fail"
df["Result"] = df["Marks"].apply(result)

print("\nDataset:")
print(df)

print("\nStudent Analysis:")
for mark in marks:
    if mark >= 75:
        print(mark,"Distinction")
    elif mark >=50:
        print(mark,"pass")
    else:
        print(mark,"fail")

print("\nAverage Marks:", calculate_average(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))