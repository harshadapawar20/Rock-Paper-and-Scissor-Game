import random
user_choice = int(input("Enter your choice:\n Type 0 for Rock\n Type 1 for Paper\n Type 2 for Scissor: "))
computer_choice = random.randint(0,2)
print("Computer chose: ",computer_choice)

if computer_choice == user_choice:
    print("It's a tie!")

elif user_choice == 0 and computer_choice == 1:
    print("You Lose.")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif user_choice == 1 and computer_choice == 2:
    print("You Lose.")

elif user_choice == 1 and computer_choice == 0:
    print("You Win!")

elif user_choice == 2 and computer_choice == 0:
    print("You Lose.")

elif user_choice == 2 and computer_choice == 1:
    print("You win!")

else:
    print("Enter the valid input!")   
