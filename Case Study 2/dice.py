import random

def roll_dice():
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_game():
    
   
    first_roll = roll_dice()
    print(f"First roll: {first_roll}")


    if first_roll in (7, 11):
        print("You win!")
        return True
    elif first_roll in (2, 3, 12):
        print("Craps! You lose.")
        return False


    point = first_roll
    print(f"Point to make: {point}")


    while True:
        roll = roll_dice()
        print(f"Rolled: {roll}")
        if roll == point:
            print("You made your point! You win!")
            return True
        elif roll == 7:
            print("Rolled a 7. You lose.")
            return False


play_game()
