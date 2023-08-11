import pandas

# Pandas testing ground

student_dict = {
    "student": ["Ferko", "Trevor", "Angie"],
    "score": [56, 70, 89]
}

# Loop through dictionary
for key, value in student_dict.items():
    print(key)

# Create dataframe
student_dict_df = pandas.DataFrame(student_dict)
print(student_dict_df)

# Loop through dataframe
for (key, value) in student_dict_df.items():
    print(value)

# Use built in method to loop through dataframe rows
for (index, row) in student_dict_df.iterrows():
    print(row)

# Get the value under a particular column
for (index, row) in student_dict_df.iterrows():
    print(row.score)

# Search for something specific
for (index, row) in student_dict_df.iterrows():
    if row.student == "Ferko":
        print(row.score)

