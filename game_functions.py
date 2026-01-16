import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    return (current_val > next_val and user_input == "l") or (current_val < next_val and user_input == "h")

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        for i in range(len(board)):
            if word[i] == letter:
                board[i] = letter
        print("Well done!",letter,"is in the word")
        return True
    print("Sorry,",letter,"is not in the word")
    return False
