#Flip a coin and bet:
#Need random library to generate random numbers
import random as rdn

score = 0
count_run = 0

while True:
    message = "Head or Tail or exit ? "
    rdn_number = rdn.randrange(2)
    prompt_user = input(message)

    if prompt_user == "exit":
        break

    match int(rdn_number):
        case 0 :
            computer = "head"
        case _:
            computer = "tail"

    count_run += 1

    if prompt_user == computer:
        score += 1
    
    print(computer, "your score is : ", float((score/count_run)*100), "%")

print("bye")