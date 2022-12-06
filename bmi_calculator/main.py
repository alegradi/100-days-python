height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


int_height = float(height)
int_weight = float(weight)

print(round(int_weight / (int_height ** 2)))

# The above can be expressed like this also

bmi = int(weight) / float(height) ** 2
print(round(bmi))
