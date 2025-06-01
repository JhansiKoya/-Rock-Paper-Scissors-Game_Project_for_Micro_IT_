#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Rock-Paper-Scissors Game
import random
choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
while True:
    print("\nRock-Paper-Scissors Game")
    print("Choose: rock, paper, scissors or type 'exit' to quit.")
    
    player_choice = input("Your choice: ").lower()
    if player_choice == "exit":
        print("Thanks for playing!")
        break
    if player_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(player_choice, computer_choice)
    print(result)


# In[ ]:





# In[ ]:




