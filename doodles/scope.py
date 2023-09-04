enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Modifying global scope
def increase_enemies2():
    global enemies
    enemies += 1
    print(f"enemies inside function (globally edited): {enemies}")

increase_enemies2()


# Global variable declaration
# Convention - full capital name
PI = 3.14159
