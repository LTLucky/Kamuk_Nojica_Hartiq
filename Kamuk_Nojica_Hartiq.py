import random
from re import A

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
while True:
p_move = input("Choose, [r]ock,[p]aper or [s]cissors: ")

if p_move == "r":
    p_move = rock
elif p_move == "p":
    p_move = paper
elif p_move == "s":
    p_move = scissors
else :
    print("Invalid input. Try again...")
    continue

ai_move = ""

computer_random_number = random.randint(1,3)

if computer_random_number == 1:
    ai_move = rock
    print("the computer chose Rock")
elif computer_random_number == 2:
    ai_move = paper
    print("the computer chose Paper")
else:
    ai_move = scissors
    print("the computer chose Scissors")
    
if (p_move == rock and ai_move == scissors) or (p_move == paper and ai_move == rock) or (p_move == scissors and ai_move == paper):
    print("You Win!")
elif (p_move == rock and ai_move == rock) or (p_move == paper and ai_move == paper) or (p_move == scissors and ai_move == scissors): 
    print("Draw!")
elif(p_move == rock and ai_move == paper) or (p_move == paper and ai_move == scissors) or (p_move == scissors and ai_move == rock):
    print("You lose!")
if play_again == "no":
    print("Thanks for playing!")
    break
