import time

endings = 3
name = input('Wassup dude, please tell me your name so i dont have to refer to you as "dude" ')
nameconfirm = input(f'Just gonna confirm real quick, u sure you want your name to be {name}? ')
if nameconfirm == ('NO'.lower()):
    name = input('Alright, what do you want to be called then?')
    print('Time to start you awesome adventure!')
elif nameconfirm == ('YES'.lower()):
    print('Time to start your adventure!')
else:
    print('Well, that was not an answer, so i guess u gotta restart completely')
print()
print("Quick note: only write your answers in lowercase")
print()
print("PS: if u see this(¯\_(ツ)_/¯) you are dead and have to restart")
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
    f2lessdarkcave = input("do you want to go left(a) or further upward(b)? ")
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
        print("¯\_(ツ)_/¯")
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
        floor = "surface"
    elif f3kindabrightcave == ("B".lower()):
        print()
        print("you tried to go back, but fell on the way down the tunnel and landed on a particularly sharp rock, "
              "and died ")
        print("¯\_(ツ)_/¯")
        floor = "U ded"
if floor == "The Pit":
    print("you see a massive, open hole in the ground which seems to have no end")
    f3thepit = input("You can jump down and take a chance(a), or just stay there(b) ")
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
        print("¯\_(ツ)_/¯")
if floor == "7thcircle":
    f47thcircle = input("do you want to be his grandson(a) or say no(b)")
    if f47thcircle == ("A".lower()):
        print()
        print('Ending reached! you became the chair-demon sullivans grandson!(btw this is an anime reference to '
              '"welcome to demon school Iruma-kun"')
        print(f"this is just one of the {endings} endings!")
    elif f47thcircle == ("B".lower()):
        print()
        print("The demon approaches you and says, so you dont want to be my grandson, well i guess you will have to "
              "die, after all, i can always find another suitable grandson candidate")
        print("Sullivan was unhappy with your decision to say no, and quickly severed your head and neck from your "
              "shoulders, you died")
        print("¯\_(ツ)_/¯")
if floor == "BOB":
    print("so, you have reached the bottom of the barrel, having to use you EpIc LosER SkiLls, there are two "
          "potential paths to take, you can go to the basement of the barrel, or... you can go out of the barrels "
          "beer dispensing pipe thingy")
    f3bottomofthebarrel = input(f"so, which is going to be {name}, the basement(a) or  the beer dispenser(b)? ")
    if f3bottomofthebarrel == ("A".lower()):
        print()
        print("New Floor! The Barrels Basement(a record low)!")
        print()
        floor = "thebarrelsbasement"
    elif f3bottomofthebarrel == ("B".lower()):
        print()
        print("you climbed out of the beer dispenser and fell out, but strangely enough, you never hit the bottom, "
              "because there is none, because i haven't coded that far so i guess you just died then?(if i continue "
              "after submission this may be added to) ")
        print("¯\_(ツ)_/¯")
if floor == "thebarrelsbasement":
    print("you see a computer, in the middle of the basement, but there seems to only be two apps installed, "
          "PyCharm Community Edition and Fortnite")
    f4thebarrelsbasement = input("Are you going to learn python(a) or play fortnite(b)? ")
    if f4thebarrelsbasement == ("A".lower()):
        print()
        print("You learnt python and and learning to code bit by bit, you bolster yourself to coding success, "
              "and then get a cushy job as some companys, emplyee, and live happily ever after")
        print(f'the end, well one of {endings} endings to be precise(this is a reference to the anime "a parallel '
              f'world that started with a death march"(more anime)')
    elif f4thebarrelsbasement == ("B".lower()):
        print()
        print("you log onto fortnite, and the computer immediately explodes directly into your face, like a claymore, "
              "probably because it was a claymore, so it seems you failed the test, you chose wrong, you should have "
              "chose the other option, after all, fortnite = disgusting")
        print('You died an immediate, painless death(wich is less than you deserve for playing fortnite in 2021), '
              'due to having your head exploded by a claymore built into the pc, set to go off when fortnite is '
              'turned on')
        print("¯\_(ツ)_/¯")
if floor == "surface":
    print("you see a light, and you sprint towards, it and finally break exit the caves, but what now? you can go "
          "look for civilisation, or just chill out.")
    f4surface = input(f"so {name}, you can go look for civilisation(a), or you can go chill out, and live the loners "
                      f"life(b) ")
    if f4surface == ("A".lower()):
        print()
        print('you see a cool looking village filled with magic and cool stuff like that, i guess, (this is a '
              'reference to literally every isekai anime that exists (with a few exceptions))')
        print(f"this is just one of {endings} endings")
    elif f4surface == ("B".lower()):
        print()
        print("you just, hangout, and chill for the rest of your life,leading the life of an absolute loner, "
              "until you get assasinated in the middle of the night by a wild skunk")
        print("as a result of this, you bleed out and die of sensory over load as the skunk sprays da stinky stuff "
              "directly into your "
              "face, so, all in all, you died of stinkyness(i guess)")
        print("¯\_(ツ)_/¯")


