import pandas as pd
df = pd.DataFrame({
    "name":["Rohan","Ananya","vikram"],
    "Dept":["ECE","CSE","ESE"],
    "Marks":[45,67,89]
})

print("originak data:\n",df)

print("\nSubset(Marks>50):\n",df[df["Marks"]>50])

print("\nSorted by Marks (Ascending):\n", df.sort_values("Marks"))

print("\nSorted by Marks (Descending):\n", df.sort_values("Marks", ascending=False))

print("\nGrouped(average marks by dept):\n",
df.groupby("Dept")["Marks"].mean())


print("\nMean = ",df["Marks"].mean())
print("\nMedian = ",df["Marks"].median())
print("\nMode = ")
print(df["Marks"].mode())
