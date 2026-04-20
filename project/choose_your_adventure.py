name = input("What is your name? ")
print(f"Welcome {name} to the adventure game!")


answer = input("You are in a dark room. Do you want to go left or right? (left/right) ")
print("answer: ", answer)
if answer.lower() == "left":
    print("You have entered a room full of treasure! You win!")
elif answer.lower() == "right":
    print("You have entered a room full of monsters! You lose!")
else:
    print("Invalid choice! You lose!")


answer = input("Do you want to play again? (yes/no) ")
print("answer: ", answer)
if answer.lower() == "yes":
    print("Restarting the game...")
else:
    print("Thanks for playing! Goodbye!")
