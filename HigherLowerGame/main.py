from welcome import welcome, action
import random
from gameData import data

print(welcome)

A = random.choice(data)
B = random.choice(data)

print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

print(action)

print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

choice = input("Who has more followers? Type 'A' or 'B': ")
if choice.capitalize() == 'A':
    if A['follower_count'] > B['follower_count']:
        print("You are right!")
    else:
        print("You are wrong")
elif choice.capitalize() == 'B':
    if B['follower_count'] > A['follower_count']:
        print("You are right!")
    else:
        print("You are wrong")
else:
    print("Invalid choice. Please type 'A' or 'B'.")