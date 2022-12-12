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

choices = [rock, paper, scissors]
your_choice_number = int(input('What is your choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
# your_choice = choices[your_choice_number]
computer_choice_number = int(random.randint(0,2))
computer_choice = choices[computer_choice_number]

if (your_choice_number >= 3 or your_choice_number < 0):
  print('You typed an invalid number, you lose!')
else:
  print(choices[your_choice_number])
  print('\nComputer chose:', computer_choice)
  if your_choice_number == computer_choice_number:
    print("It's a draw")
  elif (your_choice_number == 0 and computer_choice_number == 1) or (your_choice_number == 1 and computer_choice_number == 2) or (your_choice_number == 2   and computer_choice_number == 2):
    print('You lose')
  else:
    print('You win')