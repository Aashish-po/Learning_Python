print("Welcome to the Quiz Game!")
play = input("Do you want to play? (yes/no): ")
print("play: ", play)
if play.lower() != "yes":
    print("Maybe next time. Goodbye!")
    quit()
print("Great! Let's get started.")
score = 0
answer = input("What is the capital of Nepal? ")
print("answer: ", answer)
if answer.lower() == "kathmandu":
    print("Correct! You earn 1 point.")
    score += 1
else:
    print("Wrong! The correct answer is Kathmandu.")
answer = input("What is the largest planet in our solar system? ")
print("answer: ", answer)
if answer.lower() == "jupiter":
    print("Correct! You earn 1 point.")
    score += 1
else:
    print("Wrong! The correct answer is Jupiter.")
print("Your score is: ", score)
