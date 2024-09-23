# game.py
import random
from draw import draw_game, clear_screen

def play_game():
    """
    Simulates playing a game by randomly selecting a result.
    The result can either be 'win', 'lose', or 'draw'.
    """
    print("Playing the game...")
    outcomes = ["win", "lose", "draw"]
    return random.choice(outcomes)

def main():
    """
    The main function that clears the screen, plays the game,
    and draws the result.
    """
    # Clear the screen first
    clear_screen()

    # Play the game and get the result
    result = play_game()

    # Draw the game result
    draw_game(result)

if __name__ == '__main__':
    main()
