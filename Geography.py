print("welcome to this game")

their_interest = input("do you want to play? ") 
the_game = input("How much do you rate for yourself to campare it at end with real score out of 30?")

if their_interest.lower() != "yes":
    quit()

print("Let's get start it  ")
score = 0

answer = input("Name the biggest continant? ")
if answer == "Asia":
    print("Well Done")
    score += 10
else:
    print("No way but don't worry you will answer the next question")
    
answer = input("by clicking shift + bottom 2 waht will be shown? but dont cheat🙃 ")
if answer == "@":
    print("Well done")
    score += 10
else:
    print("it's fine even if it was supper easy")
    
answer = input("This is the last question which if you can answer it you will get 30 score to get the prize which you will see it by your eyes ok lets go to the quastion what are you? ")
if answer == "Human":
    print("You are a genius and don't talk abo`ut the prize YOU ARE THE PRIZE")
    score += 30
else:
    print("I dont know what should i say to you but see in the next round")

print("And you score isssss " + str(score) + " XP.")
print("Your Percentage is " + str((score / 3)*100))


    
input("Press enter to exit")