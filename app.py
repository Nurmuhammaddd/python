print("welcome to this game")

their_interest = input("do you want to play? ") 
the_game = input("how much do you rate for yourself to campare it at end with real score out of 30 ")

if their_interest.lower() != "yes":
    quit()

print("lets get start it  ")
score = 0

answer = input("name the biggest continant? ")
if answer == "asia":
    print("well done")
    score += 10
else:
    print("no way but dont worry you will answer the next quastion")
    
answer = input("by clicking shift + bottom 2 waht will be shown? buut dont cheat🙃 ")
if answer == "@":
    print("well done")
    score += 10
else:
    print("its fine even if it was supper easy")
    
answer = input("this is the last quastion which if you can answer it you will get 30 score to get the prize which you will see it by your eyes ok lets go to the quastion what are you? ")
if answer == "human":
    print("you are a genius and dont talk abiut the prize YOU ARE THE PRIZE")
    score += 30
else:
    print("i dont know what should i say to you but see in the next round")

print("and you score isssss " + str(score) + " XP.")
print("your percentage is " + str((score / 3)*100))


    
input("press enter to exit")