'''
Created on Sep 5, 2023

@author: unixk
'''
print('''
                                                    !_
                                                    |*~=-.,
                                                    |_,-'`
                                                    |
                                                    |
                                                   /^\
                     !_                           /   \
                     |*`~-.,                     /,    \
                     |.-~^`                     /#"     \
                     |                        _/##_   _  \_
                _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
               [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
             !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
             |*`--,_- _        |            |*`~-.,= []  |
             |.-'|=     []     |   !_       |_.-"`_-     |
             |   |_=- -        |   |*`~-.,  |  |=_-      |
            /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
        _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
       [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
        |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
       _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\
      [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \
      |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \
       | _- =-     |-_   | ((* |      |= _=       | -    |___\
       |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
       | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
       |-_=- _     |=_   =            |=_= -_     |  =   ||+||
       |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
       |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
       |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
       |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
       | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
       |=_ =       | =_-_| |  | |     |   =_      | -_   |
   jgs |_=-_       |=_=  | |  | |     |=_=        |=-    |
 `^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
''')

print("Welcome to the Castle of Chaos!.")
print("Your mission is to find the princess.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You stand before the mythical Castle of Chaos, where the evil wizard Devostraxus has taken the princess to hold her for ransom!")
print("The drawbridge is closed, but you can use your Medallion of Teleporting to get past the castle's defenses.")
teleport_target = input("Do you teleport to the (B)asement, (G)allery or (T)all, tall tower? (b/g/t)")

print("You speak the magic word  that activates the Medallion, and *poof!*")
if teleport_target.lower() == "b":
    print("You find yourself in a dark, chilly, damp environment with stone walls and a slippery floor, coated in algae.")
    print("In the distance, you see a dim, yellowish light.  At the same time, you feel a soft, cool breeze blowing past you to the left.")
    direction = input("Will you approach the (l)ight, move toward the (s)ource of the breeze, or (f)ollow where the breeze goes? (l/s/f)")
    if direction == "l":
        print("You move cautiously toward the light.  As you get nearer, you realize it's the dim glow of the eyes of a gigantic, 10-foot wide spider!")
        print("You freeze in terror as it lunges at you!  Your last thought is that at least you'll be remembered as a hero...")
    elif direction == "s":
        print("You move slowly toward the source of the breeze.  In the darkness, you find stairs leading up!")
        c_direction = input("You climb the stairs, and open a door that reveals a corridor that goes (r)ight or (l)eft.  Which way? (r/l)")
        if c_direction == "r":
            print("You turn right and head down the corridor, hearing a low rumble as you go.  With each step, the rumble increases until the floor below your feet collapses!")
            print("You fall, among the paving stones and support beams, into t he dank cellar once again.")
            print("You try to stand, but find yourself pinned beneath the rubble.  As you struggle to move, you realize that you cannot move.  Your adventure ends here, in the dark...")
        elif c_direction == "l":
            print("You turn left, coming to a heavy iron door with a massive lock.  You reach into your belt pouch and produce your lockpicking kit.")
            print("After a few moments, you're able to open the door.  In the chamber beyond, you find a massive treasure!")
            print("With money like this, who needs the reward for the princess?  You chuckle madly as you fill your pack with as much gold as you can carry and teleport away!")
            print("You set up an inn with your gold, retire, and live comfortably for the rest of your days.")
    else:
         print("You follow the air current to see where it leads.  In the darkness, you lose your footing and begin to slide, out of control toward an underground river.")
         print("The current drags you swiftly through an underground river for miles, until eventually you find yourself on a riverbank several miles away.  Try again!")
elif teleport_target.lower() == "g":
    print("You find yourself in a massive, open space.  Tapestries hang from the walls.")  
    print("The tapestries depict epic battles of Devostraxus defeating armies, slaying dragons and commanding demons!")
    print("Ahead of you, on a massive thronw made from skulls, sits an imposing figure, dresses in crimson and black.")
    greeting = input("Do you (c)all out to them, (r)un away, or (a)ttack?  (c/r/a")
    if greeting == "c":
        print("You call to the seated figure.  He raises his head and looks at you with pure, undisguised malice.  It's Devostraxus himself!")
        print("He points to you, and whispering a spell, chanted in an ancient, lost language.  You feel dizzy and faint, ans as your life ebbs away, you hear him laughing...")
    elif greeting == "a":
        print("You rush forward, roaring an ancient battle cry as you reach for your sword...")
        print("Only then realizing that you forgot to bring it.")
        print("Devostraxus laughs coldly as a magical chain appears on the floor, holding you in place as his army of undead arrive to feast.")
        print("At least, as you are magically forced to join the army of undead, you will be given a sword...")
    else:
        print("Tucking tail between your legs, you turn and run, diving ou t of the nearest window.")
        print("You land with a *thud* on the ground outside, and run as fast as you can all the way back to town.")
        print("You are forever known as the coward of the county, and the princess was never seen again.")
        print("But at least you're alive...")
else:
    print("You find yourself standing on a winding staircase.  The stairs descend below you, and continue up above you.  There is also a door in front of you.")
    choice = input("Will you (o)pen the door, go (d)own, or go (u)p?")
    if choice == "o":
        print("You push the door open and find yoursel face to face with four heavily armed skeletal guards!")
        print("You feel their malice as they advance upon you, silent as the grave.  You stumble back, startled, and find yourself falling!")
        print("You have just enough time to whisper the command word to use the Medallion of Teleporting!")
        print("Not that you remembered in time...")
        print("*WHUMP*")
    elif choice == "d":
        print("You descend the stairs, cautiously looking for any sign of the princess.")
        print("Suddenly you realize that you're heading the wrong way!  This way leads to Devostraxus' chambers!")
        print("You spin on your heel to go up, but a magical trap is sprung, and the stairs shift, becoming a slide!")
        print("Unable to stop yourself or slow, you slide down, down down, until you reach a chute that leads to the basement...")
        print("Devostraxus' pet spider finds you a tasty, if rather small, morsel.")
    else:
        print("Realizing the wisdom of your choices, you know that all the fantasy stories put the damsel in the highest part of the tallest tower!")
        print("You climb the stairs and come to a locked door.  Sick of playing this crazy game you just kick it down.")
        print("Inside, you find the princess!  She is grateful to you for the rescue, and you use your Medallion to teleport her and yourself back home.")
        print("The King rewards you well, and the princess gives you her favor at the jousting tournament.")
        print("Fame and fortune are yours, and you retire happy and wealthy after a long carteer of adventuring!")
        
print("Thanks for playing my game.  Hopefully it was worth the minutes you spent on it, 'cause you aren't getting them back!  XD")
