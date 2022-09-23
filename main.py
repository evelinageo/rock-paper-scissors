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

#making a list for the images above
image=[rock,paper,scissors]

#rules for the user
print("RULES OF THE GAME:")
print("->Rock wins against scissors\n->Scissors wins against paper\n->Paper wins against rock")
print("Type 0 for rock, 1 for paper, 2 for scissors\n")

#Take input from user for his/her choice
user=int(input("What do you choose? ")) 
if user>=3 or user<0:
  print("You typed something wrong.Try again..")
else:
  print(image[user])

  #Computer's random choice, from 0 to 2
  computer=random.randint(0,2)
  print(f"Computer chose: {computer}")
  print(image[computer])

  if user==0 and computer==2:
    print("You won!")
  elif computer > user :
    print("You lost.")
  elif user>computer:
    print("You won!")
  elif computer==user:
    print("It's a draw!")
  elif computer==0 and user==2:
    print("You lost.")
#the end
