import pandas


test_dir = {"feri": [1], "robin": [58]}

test_dir_df = pandas.DataFrame.from_dict(test_dir, orient="columns")

print(test_dir_df)
