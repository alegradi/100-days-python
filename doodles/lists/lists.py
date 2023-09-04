### String concatanation ###
first_var = "Pi"
second_var = "Thon"
full_thingy = first_var + second_var
print(full_thingy)
#################################################

### Numerical lists ###

squares = []
for i in range(1,11):   ## Doesn't include the last element
    squares.append(i**2)
print(squares)
#################################################

### Slice a list ###

first_2_squares = squares[:2]
last_2_squares = squares[-2:]
all_but_last_2_squares = squares[:-2]

print(first_2_squares)
print(last_2_squares)
print(all_but_last_2_squares)

#################################################

### Copy a list ###

champs = ["Roger", "Boris", "Graf"]
new_champs = champs[:]
print(new_champs)
#################################################

### List comprehensions ###


