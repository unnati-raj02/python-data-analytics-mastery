import pandas as pd
students_df1 = pd.DataFrame({
"StudentID":[101,102,103,104],
"Name":["Aarav","Diya","kabir","Anaya"],
"Branch":["CSE","IT","ECE","CSE"]

})

marks_df2 = pd.DataFrame({
"StudentID":[101,102,103,105],
"Marks":[85,92,76,88]

})

students_df3 = pd.DataFrame({
"StudentID":[105,106,107,102],
"Name":["Roshan","Ram","sam","vishal"],
"Branch":["IT","ECE","CSE","IT"]

})

print("Dataset 1 (students):\n",students_df1, "\n")
print("Dataset 2(marks):\n",marks_df2, "\n")
print("Dataset 3(New Students):\n",students_df3, "\n")
combined_students = pd.concat(
    [students_df1 ,students_df3],
    axis=0,
    ignore_index=True)

print("vertical concatenation(axis=0):\n",combined_students,"\n")

attendance_values = [34,45,67,89]
extra_info = pd.DataFrame({
"Attendance(%)":attendance_values})

horizontal_concat = pd.concat(
[students_df1,extra_info],
axis=1
)


print("Horizontal Concatenation(axis=1):\n",
horizontal_concat,"\n")

inner_merge = pd.merge(
students_df1,marks_df2, on="StudentID",
how="inner"
)

print("inner merge:\n",inner_merge,"\n")

left_merge = pd.merge(
students_df1,
 marks_df2,
on="StudentID",
how="left")

print("Left Merge:\n",left_merge,"\n")


right_merge = pd.merge(
students_df1,
 marks_df2,
on="StudentID",
 how="right")

print("Right Merge:\n",right_merge,"\n")


outer_merge = pd.merge(
students_df1,
 marks_df2,
 on="StudentID",
 how="outer")

print("outer Merge:\n",outer_merge,"\n")


df_a = students_df1.set_index("StudentID")
df_b = marks_df2.set_index("StudentID")

joined_df = df_a.join( 
df_b, how="inner" ) 

print("Join (index-based, inner):\n", 
joined_df, "\n")

joined_outer_df = df_a.join(
    df_b,
    how="outer"
)
print("join(index-based,outer):\n",joined_outer_df,"\n")

marks_df_renamed =marks_df2.rename(
columns={"StudentID":"ID"}
      )
merger_diff_cols = pd.merge(
students_df1,marks_df_renamed,
left_on="StudentID",
 right_on="ID",
how="inner").drop(columns=["ID"])

print("Merge with different columns names:\n",merger_diff_cols,"\n")

df_x = pd.DataFrame({ 
"StudentID": [101, 102, 103, 104], 
"Semester": [1, 1, 2, 2], 
"Subject": ["Python", "DBMS", "Data Science", "Networks"] 
}) 


df_y = pd.DataFrame({ 
"StudentID": [101, 102, 103, 105], 
"Semester": [1, 1, 2, 2], 
"Grade": ["A", "A+", "B+", "A"] 
}) 

print("Dataset X (Subjects):\n", df_x, "\n") 
print("Dataset Y (Grades):\n", df_y, "\n") 


merge_multi_key = pd.merge( 
df_x, df_y, 
on=["StudentID", "Semester"], how="inner" 
) 

print("Merge on Multiple Keys:\n", merge_multi_key, "\n")