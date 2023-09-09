import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]
user_choice = int(input("Choose a number 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if(user_choice > 2):
  print("It is an invalid number")
print(options[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer's Choice is {computer_choice}")
print(options[computer_choice])
if user_choice == computer_choice:
  print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
  print("You Win!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
elif user_choice < computer_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You Win!")
else:
  print("Invalid Input")
