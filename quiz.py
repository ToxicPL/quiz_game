# start = input("Hi, do you want to start the game? ")
points =+ 0
start = 'yes'
if start.lower() != "yes":
    quit()

print("Okay so lets start.")

print("Question 1:\n Who create first light bulb? ")
q1 = input().lower()
if q1 == "thomas edison":
    points =+ 1
    print("Good answer. Now you have {} points".format(points))
else:
    print("Sorry no points, wrong answer.")

print("Question 2:\n Who create first light bulb? ")
q2 = input().lower()
if q1 == "thomas edison":
    points =+ 1
    print("Good answer. Now you have {} points".format(points))
else:
    print("Sorry no points, wrong answer.")

print("Question 3:\n Who create first light bulb? ")
q3 = input().lower()
if q2 == "thomas edison":
    points =+ 1
    print("Good answer. Now you have {} points".format(points))
else:
    print("Sorry no points, wrong answer.")

print("Question 4:\n Who create first light bulb? ")
q4 = input().lower()
if q3 == "thomas edison":
    points =+ 1
    print("Good answer. Now you have {} points".format(points))
else:
    print("Sorry no points, wrong answer.")

print("Question 5:\n In which year gta 5 was released? ")
q5 = input().lower()
if q5 == "2013":
    points =+ 1
    print("Good answer. Now you have {} points".format(points))
else:
    print("Sorry no points, wrong answer.")

print("At the end you have {}".format(points))
print("Thanks for playing :)")