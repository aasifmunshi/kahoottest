from javascript import require
import sys

Kahoot = require("kahoot.js-latest")


def join_kahoot(game_pin: str, nickname: str):
    print(f"Creating client with name: {nickname}")
    Kahoot.join(game_pin, nickname)


def flood_bots(game_pin: str, nickname: str, num_bots: int):
    print("Flooding bots...")
    for i in range(num_bots):
        join_kahoot(game_pin, f"{nickname} {i + 1}")
    print("Done creating clients.")


def main():
    gamePin = input("Game PIN: ")
    nick = input("Nickname: ")
    amount = int(input("How many bots would you like to add?: "))
    print()
    try:
        flood_bots(gamePin, nick, amount)
    except ValueError:
        print("Error joining kahoot, sorry...")
        sys.exit()

    try:
        while True:
            pass  # Keep the script running, ensuring the bots stay in-game
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, exiting...")
        print("Please note that it may take a while for the bots to leave, so please be patient.")


if __name__ == "__main__":
    main()
