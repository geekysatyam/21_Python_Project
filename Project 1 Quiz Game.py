print("Welcome to my Computer Game")
score=0
playing = input("Do yu want to play my game?? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :") 

answer = input("What is Full form of CPU")
if answer.lower() == "central processing unit" :
    print("Correct answer")
    score +=1
else:
    print("Incoreect Answer")

answer = input("What is Full form of GPU")
if answer.lower()== "graphics processing unit" :
    print("Correct answer")
    score +=1
else:
    print("Incoreect Answer") 

answer = input("What is Full form of PSU")
if answer.lower()== "power supply unit" :
    print("Correct answer")
    score +=1
else:
    print("Incoreect Answer") 

answer = input("What is Full form of UPS")
if answer.lower()== "unified power supply" :
    print("Correct answer")
    score +=1
else:
    print("Incoreect Answer") 

answer = input("What is Full form of NPU")
if answer.lower() == "neural processing unit" :
    print("Correct answer")
    score +=1
else:
    print("Incoreect Answer") 

print("Your Total Score is :",score)

print("You got :",((score/5) *100),"%")