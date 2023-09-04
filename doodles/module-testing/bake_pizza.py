
def bake_pizza(size, *toppings):
    """Bake a pizza to the specifications"""
    print("\nBaking a " + size + " Pizza!")
    print("Toppings: ")
    for topping in toppings:
        print("- " + topping)
