## Testing while loops

game_over = False
highscore = 0

def game():
    global game_over
    global highscore
    choice = input("Please choose another letter than 'a': ")

    if choice == 'a':
        game_over = True
        return game_over
    else:
        print("Current highscore: " + str(highscore))
        print("Adding +1 to it")
        highscore = highscore + 1
        print(f"New score is: {highscore}")

while not game_over:
    game()
