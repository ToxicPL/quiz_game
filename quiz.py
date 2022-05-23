print("Welcome to the quiz game :)")
start = input("Do you want to play? ")

if start.lower() != "yes":
    print("Bye")
    quit()

print("---------------------------------Games has been started---------------------------")
points = 0
cpu = input("What is full name of the CPU ? ")
if cpu.lower() == "central processing unit":
    print("Great you have a point")
    points += 1
else:
    print("Your answer was wrong")

hdd = input("What is full name name of HDD? ")
if hdd.lower() == "hard disk drive":
    print("Great you have a point")
    points += 1
else:
    print("Your answer was wrong")

ssd = input("What is full name name of SSD? ")
if hdd.lower() == "solid state drive":
    print("Great you have a point")
    points += 1
else:
    print("Your answer was wrong")

print("---------------------------------Games has been ENDED---------------------------")
print("Number of your points {}".format(points))
