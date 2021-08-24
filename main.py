import time

name = input('Wassup dude, please tell me your name so i dont have to refer to you as "dude" ')
nameconfirm = input(f'Just gonna confirm real quick, u sure you want your name to be {name}? ')
if nameconfirm == ('NO'.lower()):
    name = input('Alright, what do you want to be called then?')
    print('Time to start you awesome adventure!')
    print("Quick note: only write your answers in lowercase")
elif nameconfirm == ('YES'.lower()):
    print('Time to start your adventure!')
else:
    print('Well, that was not an answer, so i guess u gotta restart completely')
print()
print('New Floor! Dark Cave')
print()
floor = "Dark Cave"
f1darkcave = input('Alright, so, you are in a dark cave, wanna go up or down? ')
if f1darkcave == ('UP'.lower()):
    print()
    print('New Floor! Less Dark Cave')
    print()
    floor = "Less Dark Cave"
elif f1darkcave == ('DOWN'.lower()):
    print()
    print('New Floor! Darker Cave')
    print()
    floor = "Darker Cave"
if floor == "Less Dark Cave":
    print("you see a pit to your left or you can go further upwards")
    f2lessdarkcave = input("do you want to go left(A) or further upward(B)? ")
    if f2lessdarkcave == ("B".lower()):
        floor = "kinda bright cave"
        print()
        print("New Floor! kinda bright cave")
        print()
    elif f2lessdarkcave == ("A".lower()):
        floor = "The Pit"
        print()
        print("New Floor! The Pit")
        print()
if floor == "Darker Cave":
    print("Wow, a cave even darker than the last, you can barely see, but through the darkness you do see a lot of "
          "goblins staring right back at you")
    f2darkercave = input("so do you want to fight or run? ")
    if f2darkercave == ("FIGHT".lower()):
        print()
        print("so, you go to cast your EpIC MaGIc and then you ReaLIsE ThaT YoU CaNt UsE MaGiC, and get mauled by "
              "little goblins, and die")
    elif f2darkercave == ("RUN".lower()):
        print()
        print("you use your awesome loser skills from years of binge watching batman to use the "
              "conveniently placed grapple hook that was 100% not put there on purpose, to flee the goblins")
        print()
        print("New Floor! The bottom of the barrel!")
        print()
        floor = "BOB"
if floor == "kinda bright cave":
    print("you see a bright light, not far ahead, but you dont know whether you should go there, so you can go there "
          "or play it safe and go back")
    f3kindabrightcave = input(f"you have two options {name}, you can go back, or AsCeND, wich u gonna do, ascend(a) "
                              f"or go back(b) ")
    if f3kindabrightcave == ("A".lower()):
        print()
        print("New Floor! Surface!")
        print()
    elif f3kindabrightcave == ("B".lower()):
        print()
        print("you tried to go back, but fell on the way down the tunnel and landed on a particularly sharp rock, and died ")
        print()
        floor = "U ded"
if floor == "The Pit":
    print("you see a massive, open hole in the ground which seems to have no end")
    f3thepit = input("You can jump down and take a chance(a), or just stay there(b)")
    if f3thepit == ("A".lower()):
        print()
        print("New Floor! the 7th circle of hell")
        print()
        print("A random old dude called sullivan approaches you and asks if you want to be his grandson")
        floor = ("7thcircle")
    elif f3thepit == ("B".lower()):
        print()
        print("you wait there until the day you die(of hunger)")
        print("u ded")
if floor == "7thcircle":
    f47thcircle = input("do you want to be his grandson(a) or say no(b)")
    if f47thcircle == "a":
        print()
        print('Ending reached! you became the chair-demon sullivans grandson!(btw this is an anime reference to "welcome to demon school Iruma-kun"')
        print("this is just one of the potential endings")

