print('Welcome to the quiz')
playing = input('Wanna play? ')
print(playing)
if playing.lower() != 'yes':
    quit()
print("Ok, let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " score")
print("you got ", score/4*100, "%")

