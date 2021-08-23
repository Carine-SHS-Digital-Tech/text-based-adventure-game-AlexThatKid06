import time
import F2
name = input('Wassup dude, please tell me your name so i dont have to refer to you as "dude" ')
time.sleep(1.5)
nameconfirm = input(f'Just gonna confirm real quick, u sure you want your name to be {name}? ')
if nameconfirm == 'no':
    time.sleep(1.5)
    name = input('Alright, what do you want to be called then?')
    print('Time to start you awesome adventure!')
elif nameconfirm == 'yes':
    time.sleep(1.5)
    print('Time to start you poggers adventure!')
else:
    print('Well, that was not an answer, so i guess u gotta restart completely')
print()
time.sleep(1.5)
print('New Floor! Dark Cave')
print()
floor = "Dark Cave"
f1darkcave = input('Alright, so, you are in a dark cave, wanna go up or down? ')
if f1darkcave == 'up':
    print()
    print('New Floor! Less Dark Cave')
    print()
    floor = "Less Dark Cave"
elif f1darkcave == 'down':
    print()
    print('New Floor! Darker Cave')
    print()
    floor = "Darker Cave"
if floor == "Less Dark Cave":
    print("you see a pit to your left or you can go further upwards")
    f2lessdarkcave = input("do you want to go left(A) or further upward(B)? ")
    if f2lessdarkcave == "B":
        floor = "kinda bright cave"
        print()
        print("New Floor! kinda bright cave")
        print()
    elif f2lessdarkcave == "A":
        floor = "The Pit"
        print()
        print("New Floor! The Pit")





