#             ////////                    ///////
#              //     ///                //.     //
#              //       //             //.       //
#              ///       //            //       //
#                 ////  //             //   /////
#                    //////////////////////          /////   ///
#                  ///                    ///      ///.          //
#                 //                         /// ///   //         //
#               ///                            ////   /     ////  //
#              //           //////////          ///  /    //    /./
#             //         ///          ///        /// /    //    /
#             //        //    /    /    //        //  /   //
#             //       ///   //   //    //.       //  /    /
#             //        //             ///        //  /   //
#              //         ///        ///         //   /   /
#               //           ///////            //   /  //
#                 ///                        /  ////  //
#                   //////              //////.
#                    //   /////////////.   //
#                     ///////       .///////
#
#
#   _____ ____  ____  _____________    __    ____  _   __   ______
#  / ___// __ \/ __ \/  _/ ____/   |  / /   / __ \/ | / /  / ____/
#  \__ \/ /_/ / /_/ // // / __/ /| | / /   / / / /  |/ /  /___ \
# ___/ / ____/ _, _// // /_/ / ___ |/ /___/ /_/ / /|  /  ____/ /
# /____/_/   /_/ |_/___/\____/_/  |_/_____/\____/_/ |_/  /_____/
#
#         THE SPRIGGY INC. FUTURISTIC RECRUITMENT TOOL
#


import random
import os
from os import system
from termcolor import colored, cprint
from pygame import mixer
import webbrowser

# Monster variables. Name, HP, attack, and HP after player runs away.
cthulhu = ['Monster like the one in the movie "Cloverfield"', 200, 15, 300]
rous = ['Rodent of unusual size', 50, 5, 50]
rockMonster = ['Rock Monster named Calvin', 100, 10, 100]
shroom = ['Angry Mushroom', 120, 15, 120]
keith = ['Normal Keith', 70, 10, 90]
keiths_mom = ["Keith's Angry Mother", 100, 25, 100]

# Travel Location definition set
north = {
    'north': 1,
    'south': 6,
    'east': 4,
    'west': 2,
    'mapname': 'North',
    'mapDescript': 'Mountain Foothills',
    'aText': "\tAfter a day of travel, you find yourself in the mountains.",
    'aText2': "\tThe sky is grey and threatening. \n\tThere is a winding path to the west, \n\ta jagged path up the mountain to the north, \n\tand another rocky path to the east.",
    'items': 'raw vegetables'
}

farnorth = {
    'south': 3,
    'mapname': 'Far North',
    'mapDescript': 'Craggy Mountains',
    'aText': "\tYou find yourself high in the mountains.",
    'aText2': "\tThe air is thin. \nThere are no plants, just rock and wind for miles.",
    'items': 'metal ore',
    'monster': rockMonster,
}

northeast = {
    'west': 3,
    'mapname': 'Northeast',
    'mapDescript': 'Light Jungle',
    'aText': "\tThe mountain pass begins to clear, you find yourself overlooking a sunny jungle.",
    'aText2': "\tIt is hot. \n\tThe only path leads back west.",
    'items': 'a strange document',
    'monster': keith
}

northwest = {
    'east': 3,
    'mapname': 'Northwest',
    'mapDescript': 'Dense Jungle',
    'aText': "\tHacking through thick, dense undergrowth, you find yourself in a dense jungle.",
    'aText2': "\tYou cannot see the sky. \n\tThe only path leads back east.",
    'items': 'gillyweed',
    'monster': shroom
}

ship = {
    'north': 3,
    'east': 7,
    'west': 5,
    'south': 9,
    'mapname': 'Ship',
    'mapDescript': 'A wrecked spaceship',
    'aText': "\tYou are on your ship. It is safe here.",
    'aText2': "\tAfter a night of rest, you feel refreshed.\n\tYou know that if this ship is ever going to\n\tfly again though, you will need to find\n\tsome pulse crystals. \n\tHealth at 100%."
}

east = {
    'west': 6,
    'mapname': 'East',
    'mapDescript': 'Damp Woods',
    'aText': "\tLeaving the ship, you follow the path into the woods.",
    'aText2': "\tIt is misty. \n\tThe only path leads back west to the ship.",
    'items': 'sticks and rocks',
    'monster': rous
}

west = {
    'east': 6,
    'mapname': 'West',
    'mapDescript': 'Sunny Beach',
    'aText': "\tLeaving the ship, you walk along the beach.",
    'aText2': "\tIt is a beautiful day. \n\tThe only path leads back east to the ship.",
    'items': 'pulse crystal dust'
}

south = {
    'north': 6,
    'east': 10,
    'west': 8,
    'mapname': 'South',
    'mapDescript': 'Ocean',
    'aText': "\tYou attach the breather, allowing you to breathe underwater!",
    'aText2': "\tYou step beneath the waves. You can travel east or west.",
    'items': 'flint',
}

southeast = {
    'west': 9,
    'mapname': 'Southeast',
    'mapDescript': 'Evil Ocean Cave',
    'aText': "\tYou step deeper and deeper into the dark waters. You find the entrance of an underwater cave.",
    'aText2': "\tStepping over the broken body of the sea monster, you look around in the darkness...",
    'items': 'pulse crystals',
    'monster': cthulhu
}

southwest = {
    'east': 9,
    'mapname': 'Southwest',
    'mapDescript': 'Shallow Ocean Floor',
    'aText': "\tYou walk along the bottom of the ocean.",
    'aText2': "\tAncient shipwrecks around you, you see the distant lights above you. \n\tThe only way to go is back east.",
    'items': 'raw vegetables'
}

# Locations.  Used in mapping/traveling

locations = {
    1: farnorth,
    2: northwest,
    3: north,
    4: northeast,
    5: west,
    6: ship,
    7: east,
    8: southwest,
    9: south,
    10: southeast
}


# Game Entry Point.  Setting up the story

def start():
    system('mode con: cols=200 lines=49')
    mixer.init()
    mixer.music.load('intro.mp3')
    mixer.music.play()
    """Commences the game."""
    print("\n" * 3)
    cprint('''
                ////////                    ///////
                //     ///                //.     //
                //       //             //.       //
                ///       //            //       //
                   ////  //             //   /////
                      //////////////////////          /////   ///
                    ///                    ///      ///.          //
                   //                         /// ///   //         //
                 ///                            ////   /     ////  //
                //           //////////          ///  /    //    /./
               //         ///          ///        /// /    //    /
               //        //    /    /    //        //  /   //
               //       ///   //   //    //.       //  /    /
               //        //             ///        //  /   //
                //         ///        ///         //   /   /
                 //           ///////            //   /  //
                   ///                        /  ////  //
                     //////              //////.
                      //   /////////////.   //
                       ///////       .///////
                                                                                ''', 'red', attrs=['blink'])
    print("\n")
    print("""
     _____ ____  ____  _____________    __    ____  _   __   ______
    / ___// __ \/ __ \/  _/ ____/   |  / /   / __ \/ | / /  / ____/
    \__ \/ /_/ / /_/ // // / __/ /| | / /   / / / /  |/ /  /___ \  
   ___/ / ____/ _, _// // /_/ / ___ |/ /___/ /_/ / /|  /  ____/ /  
  /____/_/   /_/ |_/___/\____/_/  |_/_____/\____/_/ |_/  /_____/                                                             

           THE SPRIGGY INC. FUTURISTIC RECRUITMENT TOOL

    """)
    print("Hit RETURN to continue.")
    input("> ")
    screen_clear()
    print("You are in a spiral hurtling toward the ground...")
    cprint("you are in and out of consciousness...", 'white', attrs=['blink'])
    print("""

        Everything
                            .....goes
                                            ...black.""")
    print("Hit RETURN to continue.")
    input("> ")
    mixer.music.stop()
    screen_clear()
    print("And silent...")
    print("\n" * 35)
    print("Hit RETURN to continue.")
    input("> ")
    screen_clear()
    print("""
                                                        *****/                  
                                                       **+**/**                 
                     ***                               **    +**                
                   ******:                             /**//***                 
                   *** ***             *                 /**+*                  
                    ******      *+********/  **                                 
                       *     *****/*******   ***/   **:::///:*                  
                            ****   *********/* /***************/                
                          ****     **     */**** /*********  /*+                
                         ***                 ***/ ***:/****:**/                 
                         ***                   ** ******/***+*                  
                        ***                   */****++*****                     
                      *+**/              *:+****+/+*****                        
                   *+***+**         *:+*****//+****/**                          
                 :***/+*****  *:/******///*****:*  +*:                          
               ***/*+**+/********+//+*****/**     :**                           
               ***  /*****++++******+/*         ****                            
               +****************:*            *****                             
                 ********     /***+:*******/*****                               
                                 :+*********/*                                  

                                        **                                      
                                      ******                                    
                                      +*/ ***                                   
                                       /***:                                                                  
                                                      """)
    cprint('''
                    ▄████▄   ██▀███   ▄▄▄        ██████  ██░ ██ 
                   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒
                   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░
                   ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ 
                   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓
                   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
                    ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
                   ░          ░░   ░   ░   ▒   ░  ░  ░   ░  ░░ ░
                   ░ ░         ░           ░  ░      ░   ░  ░  ░
                   ░                                            ''')
    print("Hit RETURN to continue.")
    input("> ")
    screen_clear()
    print("""\t
    Your spaceship crash lands on the desolate planet Beta-Z in the outer quadrant. 
    Without Pulse Crystals, the vital fuel for your craft, you are stranded and alone
    on a planet where everything is trying to kill you.
    Nobody knows you are here. Nobody is coming to find you.
    You stare at the foreboding sky in fear... """)
    print("\n" * 3)
    print("Hit RETURN to continue.")
    input("> ")
    screen_clear()

    print("""
    'Snap out of it!' you say to yourself. 
    You grab some supplies, check your injuries and survey the damage.
    It doesn't look great, but all is not lost either.
    You gather yourself and immediately you resolve to survive and find a way home... no matter what it takes.

    Stepping out of your craft, you have some decisions to make...""")
    print("\n" * 3)
    print("Hit RETURN to continue.")
    input("> ")
    screen_clear()


# Function for clearing screen
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# The Turn loop
def myTurn():
    global health
    while True:
        print("\nWhat would you like to do? Type H for help.")
        choice = input("> ")
        choice = choice.lower()

        if choice == 'h':
            screen_clear()
            print("\n********** HELP **********")
            print("""You may do the following:
            travel
            supplies
            search
            check health
            read
            eat
            map
            workshop
            ship computer""")
        elif choice == 'travel':
            travel()
            break
        elif choice == "supplies":
            supplies.sort()
            screen_clear()
            print("\n********** SUPPLIES **********")
            for i in supplies:
                print("\t", i)
        elif choice == 'search':
            screen_clear()
            print("You look around the area you are standing...")
            if 'items' in myLocation:
                print(f"You found {myLocation['items']}!")
                supplies.append(myLocation['items'])
                del myLocation['items']
            else:
                print("There is nothing of significance here.")
        elif choice == 'check health':
            print(f"Your health is currently at {health}%")
        elif choice == 'eat':
            eat()
        elif choice == 'read':
            read()
        elif choice == 'workshop':
            if myLocation == ship:
                workshop()
                break
            else:
                print("You can only do this at the ship!")
        elif choice == 'ship computer':
            if myLocation == ship:
                screen_clear()

                print("-" * 20)
                print("|                   |")
                print("|                   |")
                print("|                   |")
                cprint('   C:>', 'red', attrs=['blink'])
                print("|                   |")
                print("|                   |")
                print("|                   |")
                print("-" * 20)
                print("\n" * 5)
                print("\nYou saunter over to the ship computer and pull out the terminal... "
                      "a cursor blinks on the screen")
                input("Hit RETURN to continue > ")

                computer()
                break
            else:
                print("You can only do this at the ship!")
        elif choice == "map":
            screen_clear()
            print("\n********** MAP **********")
            for i in map:
                print(f"{i} : {map[i]}")
            print()
        else:
            print("Sorry, you cannot do that here.")


# The travel Logic.  This writes the journey story
def travel():
    screen_clear()
    global health
    while True:
        print("\n********** TRAVEL **********")
        print("You ready yourself for a journey and grit your teeth against the pain.\n"
              "Mustering all your strnegth you set out...")
        print("Which direction would you like to go?")
        direction = input("> ")
        direction = direction.lower()
        if direction in myLocation:
            destinationIndex = myLocation[direction]
            destination = locations[destinationIndex]
            if destination == south:
                if 'breather' in supplies:
                    arrive(destination)
                else:
                    screen_clear()
                    print("You see a vast ocean spreading off to the horizon.")
                    print("You walk until you hit the waves. \nYou can go no further.")
                    print("Hit ENTER to return to the ship.")
                    input("> ")
                    arrive(ship)
            arrive(destination)
        elif direction == 'home':
            if health <= 20:
                dead("On the way home, you collapse from exhaustion.")
            else:
                arrive(ship)
        else:
            print("Sorry, you cannot travel that direction from here.")


# The Arrive at location Logic.  This writes the location story based on location
def arrive(newLocation):
    screen_clear()
    global myLocation
    global health
    health -= 10
    if health <= 0:
        dead("You collapse from exhaustion.")
    myLocation = newLocation
    map[newLocation['mapname']] = newLocation['mapDescript']
    if newLocation == ship:
        health = 100
    if 'monster' in newLocation:
        fight(newLocation['monster'])
        del newLocation['monster']
    print(newLocation['aText'])
    print(newLocation['aText2'])
    myTurn()


# The fight scenes.  This writes fight story based on Monster data
def fight(baddie):
    global health
    hit = 10
    if 'spear' in supplies:
        hit = 20

    if 'blade' in supplies:
        hit = 30
    screen_clear()
    print(f"You are attacked by a {baddie[0]}!")

    while True:
        if health <= 0:
            dead(f"You have been slain by the {baddie[0]}!")

        # player's turn
        while True:
            print("\n")
            print(f"your health: {health}")
            print(f"baddie's health: {baddie[1]}")
            print("What do you do? Type H for help.")
            choice = input("> ")
            choice = choice.lower()
            if choice == "h":
                print("\n********** CONFLICT OPTIONS **********")
                print("""You may do the following:
                Run
                Attack
                Eat""")
            elif choice == 'eat':
                eat()
                break
            elif choice == 'attack':
                myAttack = random.randint(1, 21)
                screen_clear()
                if myAttack >= 19:
                    print(f"CRITICAL HIT! \nYou have badly wounded the {baddie[0]}!\n")
                    baddie[1] -= (hit + 10)
                    break
                elif myAttack >= 4:
                    print(f"You have wounded the {baddie[0]}!\n")
                    baddie[1] -= hit
                    break
                else:
                    print("Your attack missed!\n")
                    break
            elif choice == 'run':
                if health <= 20:
                    dead("You collapse on the way home from exhaustion.")
                baddie[1] = baddie[3]
                screen_clear()
                print("\t\t YOU ARE RUNNING AWAY TO SAVE YOUR MORTAL SOUL!!!\n\n\n")
                print("Hit RETURN to continue.")
                input("> ")
                arrive(ship)
                break
            else:
                print("Sorry, you can't do that now!")

        if baddie[1] <= 0:
            print(f"You have defeated the {baddie[0]}!\n")
            print("Hit RETURN to continue.")
            input("> ")
            break

        # baddie's turn
        print(f"The {baddie[0]} attacks!")
        baddieAttack = random.randint(1, 21)
        if baddieAttack >= 18:
            print("CRITICAL HIT!\n")
            health -= (baddie[2] * 2)
        elif baddieAttack >= 4:
            print("You are hit!\n")
            health -= baddie[2]
        else:
            print(f"The {baddie[0]} misses!")


# Eat function Handles eating and health
def eat():
    global health
    screen_clear()
    if 'food' in supplies:
        print("You eat the food and feel much better!")
        health += 20
        if health >= 100:
            health = 100
        print(f"Your health is now at {health}.\n")
        supplies.remove('food')
    else:
        print("You have no food to eat!\n")


# Reading the document dropped by Normal Keith
def read():
    screen_clear()
    if 'a strange document' in supplies:
        print("You pull out the document you had picked up. It reads:\n'"
              "'Have you ever found yourself crash landed on an inhospitable planet?\n"
              "Have you wondered then that perhaps you are in the wrong job, with the wrong company?\n"
              "Who leaves a person stranded on an angry planet with angry monsters!!!???\n"
              "Well the good news is we have the answer for you!  No more being attacked by angry monsters\n"
              "No more scavenging for food and supplies.  No more having to find your own way home. Why?\n"
              "Because at Spriggy Inc. we are a family, and family takes care of each other! Join our team\n"
              "and we will send a rescue vessel to the planet you are stranded on and rescue you from your\n"
              "job immidiately.  We will even give you some shwag for the journey home.  To join simply, find\n"
              "a computer terminal and message portal code 'Klondike Five' into the interstellar messaging system\n"
              "answer some simple questions and then find the right job for you.  We will take care of the rest.\n"
              "\nSincerely, Spriggy Inc.'")
    else:
        print("You have nothing to read... if only there was a document laying around.\n")


# The ship computer terminal and logic
def computer():
    screen_clear()
    print("-" * 20)
    print("|                   |")
    print("|                   |")
    print("|                   |")
    cprint(' C:> Enter command', 'red', attrs=['blink'])
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("-" * 20)
    print("\n" * 5)
    portal = input("The screen reads 'Enter a PORTAL CODE to access, type EXIT to leave, HELP for help' >")
    if portal.lower() == "klondike five":
        screen_clear()
        cprint('''
                    `.-::::::::::::::::::::::::::::::::::-.`                    
               `-+ydmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmhs/.`               
             `+hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNms-`             
           ./omNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdh+`           
          -ssymNNNNmddddddddddddddddddddddddddddddddddddddddmNNNNNNNh-          
         +dmmNNNNm+.````````````````````````````````````````-oNNNNNNNd:         
        :mNNNNNNNh`         ``                    ``         .dNNNNNNNd-        
       `hNNNNNNNNy      `:oyyys+-`            `:oyyys+-`     .dNNNNNNNNy        
       :mNNNNNNNNy     -yNNNdsymms.          -yNmysmNNms.    .dNNNNNNNNm.       
       /NNNNNNNNNy    `hNNNNs.-dNNs         `hNNh..yNNNNs`   .dNNNNNNNNm:       
       /NNNNNNNNNy    -mNNNNNmmNNNd`        .mNNNmmNNNNNd.   .dNNNNNNNNm:       
       /NNNNNNNNNy    `sNNNNNNNNNNo         `yNNNNNNNNNNo    .dNNNNNNNNm:       
       /NNNNNNNNNy     `odNNNNNNd/`          `odNNNNNNd/`    .dNNNNNNNNm:       
       /NNNNNNNNNy       `-/++/-`              `-/++/-`      .dNNNNNNNNm:       
       /NNNNNNNNNy                                           .dNNNNNNNNm:       
       /NNNNNNNNNy             `s+/..`   ``.:oyo             .dNNNNNNNNm:       
       :NNNNNNNNNy             `syysmdhhhddmNNN+             .dNNNNNNNNm-       
       .dNNNNNNNNy              `+hydmmNmmmdmmo`             .dNNNNNNNNh`       
        oNNNNNNNNy               `/syo++++oys:`              .dNNNNNNNm/        
        `yNNNNNNNd-                `.:://:-.`               `:mNNNNNNNo`        
         .sNNNNNNNdsooooooooooooooooooooooooooooooooooooooooymNNNNNNmo`         
          `/dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh:           
            .+hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmh/`            
              `:ohmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmh+-`              
                  .:/osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysso/-.                  




        ''', 'green')

        apply = input("""
            You have reached the Intergalactic Spriggy Hiring Robot.
            Welcome! Would you like to hear about our jobs
            and Intergalactic rescue package today? Y/N >""")
        if apply.lower() == "y":
            job("false")
        else:
            print("""Ok! Thanks you for taking the time to talk to a simple robot like me.
                            Stay safe. I hope the mosters dont eat you!""")
            print("\n" * 3)
            input("Hit RETURN to continue > ")
            computer()
    elif portal.lower() == "google":
        print("""

                                  ...                            
                         .:-=+***********+=--.                   
                     :-+***********************+=:               
                  :=*******************************=:            
               .-*************************************:          
             .=*************************************+:           
            -******************+==---==+**********+:             
           +**************+=:.            :-+***+:               
         .+*************=.                   .=:                 
         -=+**********=.                                         
        -====+******+.                                           
       :========+**+.                                            
       -===========.               ............................  
      .===========:                :===========================  
      :===========.                :===========================. 
      :===========.                :===========================. 
      :===========.                :===========================. 
      .===========:                :===========================. 
       -===========.               ................-==========-  
       .============.                             .===========:  
        :============:                           .-==========-   
         -============-.                        :============.   
          -=============-:                   .:-============:    
           -================:..          .:-===============.     
            .======================-=====================-.      
              :========================================-:        
                :=====================================:          
                  .:===============================-:            
                     .:-=======================-:.               
                          ..:---=======---::.   


                    They have no answers for you here    

        """)
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "amazon":
        print("""
x


                         :-+**######*+=:                         
                      =*%%%%%%%%%%%%%%%%%#-                      
                    =%%%%%%%%%%%%%%%%%%%%%%%:                    
                   *%%%%%%%%%*+==+#%%%%%%%%%%.                   
                  +%%%%%%%%=       :%%%%%%%%%+                   
                  =*###%%%+         =%%%%%%%%*                   
                                    =%%%%%%%%*                   
                          .:--=++***#%%%%%%%%*                   
                      :+#%%%%%%%%%%%%%%%%%%%%*                   
                   .+%%%%%%%%%%%%#**#%%%%%%%%*                   
                  -%%%%%%%%%*-.     =%%%%%%%%*                   
                 :%%%%%%%%%-        =%%%%%%%%*                   
                 #%%%%%%%%*         *%%%%%%%%#                   
                 %%%%%%%%%*        -%%%%%%%%%%.                  
                 #%%%%%%%%%=     .+%%%%%%%%%%%#.                 
                 -%%%%%%%%%%%*+*#%%%%%%%%%%%%%%%-                
                  =%%%%%%%%%%%%%%%%%#=*%%%%%%%%=.                
                   .+%%%%%%%%%%%%%+:   -#%%%#-                   
  ..                  .-=++++==-.        -=:       .:--====--.   
   :--:.                                           ..     :==.   
     .:==-:..                                       .:--  :=-    
        .:-====-::..                         .::--===:.   ==     
            .:-========----::::::::::----=======--:.     --      
                ..:--=====================--:..          .       
                        ....::::::::...                          

            Ah shame. They don't deliver to this planet...
... if you cant sue your way to the moon, you for sure cant sue your way
                           to Beta-Z                

""")
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "space invaders":
        webbrowser.open("https://funhtml5games.com/spaceinvaders/index.html")
        print("""
      redirect to space invaders... feels appropriate

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@****@@@@@@@@@@@@@@@@@@@@@****@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#    @@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%::::####@@@@@@@@@@@@@####::::@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@    %@@@@@@@@@@@#    @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%    #%%%%%%%%%%%+    %%%%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#                             @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#                             %@@@@@@@@@@@@@@@@
@@@@@@@@@@@+        @@@@.           :@@@@        #@@@@@@@@@@@@
@@@@@@@@@@@+        @@@@.           :@@@@        #@@@@@@@@@@@@
@@@@@@@=                                             +@@@@@@@@
@@@@@@@=                                             +@@@@@@@@
@@@@@@@=   -%%%*                             #%%%:   +@@@@@@@@
@@@@@@@=   =@@@#                             @@@@:   +@@@@@@@@
@@@@@@@=   =@@@#    #####################    @@@@:   +@@@@@@@@
@@@@@@@=   =@@@#    @@@@@@@@@@@@@@@@@@@@@    @@@@:   +@@@@@@@@
@@@@@@@%***%@@@@****--------#@@@*--------****@@@@#***%@@@@@@@@
@@@@@@@@@@@@@@@@@@@@        *@@@+        @@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@********%@@@%********@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        """)
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "nasa":
        print("""                                                                                
     :=++*+=:        :---:       .-=++=-          .:::::::::::::.        .:---:           
   .*########*.      *###*      +########=      =################      :*#######+         
   =####+=####*      *###*     +####+*####:   .#################*      #####*###%=        
   +####  .####=     *###*    :####+  #####.  +####:                  +####. =##%%:       
   +####   =####.    *####    *####   :####+  +####:                 -####=   *##%#       
   +####    ####+    *####   =####-    =####-  *#############*=:     ####*    .##%%+      
   =####    -####:   *####  :####+      *####   -*##############*   +####:     =###%:     
   =####     *###*   *####  *####.      .####+     ..:::::::=####* :####=       *##%#     
   =####.    :####-  *#### +####-        =####-              +####.#####        .###%*    
   =####.     =####==#####:####*          *####+++++++++++++*####=+####:         =##%%-   
   -####.      +#########-*####.          .####%%%%%%%%%%#######-:####+           *#%%#.  
   .----        .-++*+=:  ====:            :======++++++++++=-:  -++++.           .++++-       

                Sorry, NASA doesn't service planets in the Outer Quadrant.
                        ... Maybe they need some engineers too  
""")
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "space x":
        print("""                    .                                      
                         *@@*+#%%*##%%%#*=.   .                       
                   .%#+=%@@@@@@@@@@@@@@@@@@%*::%:                     
                 :%%@@@@@@@@@@%@@@@@@@%@@%@@%@*%#                     
                -@@%@@%%@@@@@@%%%@%@%@@@@@@@@@@@@-                    
              -%%@@%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@%###%**.             
              =@@@@@@@@@@@@@@@@%##*****+*##@@@@%@%%@@@@@+.            
          .:+@@@@@@@%@@*: ::.              .-%@@@@@@@@@@%:            
          :-@@@@%%@@%+.                      .#@@@@@@@@##=            
           =%%@@@@@%.                          %%@%%@@@%@=            
            .%@@@@@.                           -%@@@@@@@-             
             #@@@%-                            -@@@@@@@@+             
             -%@@*                             :%@@%@@@%              
              %@@.                               +@@@@@-              
              +@%  -**==-.        .+*##%%+=-     -@@@@*               
              -%% -+=--===.       :----:..::     -@@@@*               
               @@.  :*#@@#+.     .+**%@%++.      =%@#*-               
               *@-   - :-  . -     .-::.         +@@                  
               -%*   .--:   -=        .          *@-                  
                *%          +=                   *-                   
                 %.        =%=                   #.                   
                 +*        #@*  -*+  .-.         *.                   
                 =@%-       .-=-       **=.      *.                   
                 -@@%%:                  ::      %.                   
                  %@ ::  :=++=++=-=**++=:        %                    
                  =@#.   .+@+=--::::++          +-                    
                   +@%-     ----::::          -#:                     
                    :#%+.                   .*+                       
                      :%@+.               :*+.                        
                        =%@+-.        .:=+:                           
                          :=%@%*==+#@@*-                              
                              :-==--.  

                Elon can't take your call right now.                              
""")
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "help" or portal.lower() == "h":
        screen_clear()

        print("-" * 20)
        print("|                   |")
        print("|                   |")
        print("|                   |")
        cprint('   C:> HELP', 'red', attrs=['blink'])
        print("|                   |")
        print("|                   |")
        print("|                   |")
        print("-" * 20)
        print("\n" * 5)
        print(""" 
    You will need to find an Intergalactic Dialing Code and enter that
    or you could use a code stored in your database:
        Google
        Space Invaders
        Amazon
        NASA
        Space X
        or type EXIT to exit terminal""")
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        computer()
    elif portal.lower() == "exit":
        print("\n" * 3)
        myTurn()

    print("\n" * 3)
    myTurn()


def job(selection):
    screen_clear()
    print("\n" * 3)
    print("\n********** POSITIONS VACANT **********")
    print("\n" * 3)
    if selection != "true":
        print("""
    Spriggy helps Aussie families teach their kids about money and makes it possible
    to manage it all from your pocket. We provide parents with a safe and simple way 
    to pay their kids pocket money, set chores, manage savings, monitor spending, pay
    for school lunches and invest for their kids' future.

    Spriggy launched in late 2016 and has had over 500,000 members join and a 4.8 star
    rating average from over 20,000 reviews. We recently closed our Series B round of
    $35m and are backed by high-calibre Australian investors, including Mike Cannon-Brookes'
    Grok Ventures and NAB ventures.

    We’re a rapidly growing team, with people from diverse backgrounds that include engineering,
    design, physics, genetics, medicine, sports, ex-founders and mathematics. We’re all passionate
    problem solvers and we truly care about how people learn to use money.

    Below are some of our current opportunities:
    """)
    else:
        print("""
            That seems like a great choice for you!

            Why not take a look at some of the other opportunities:
            """)

    print("\n" * 3)
    print("1. Mid-level Python/Java Developer\n"
          "2. SRE/Python (Java) Developer\n"
          "3. Senior Python/Java Developer\n"
          "4. UI/UX 'Librarian' Developer\n"
          "5. exit")
    print("\n" * 3)
    jobnum = input("Select the job number you would like more information on or 5 to EXIT >")
    if jobnum == "1":
        webbrowser.open("https://spriggy.bamboohr.com/jobs/view.php?id=61")
        job("true")
    elif jobnum == "2":
        webbrowser.open("https://spriggy.bamboohr.com/jobs/view.php?id=60")
        job("true")
    elif jobnum == "3":
        webbrowser.open("https://spriggy.bamboohr.com/jobs/view.php?id=59")
        job("true")
    elif jobnum == "4":
        webbrowser.open("https://spriggy.bamboohr.com/jobs/view.php?id=58")
        job("true")
    elif jobnum == "5" or jobnum.lower() == "exit":
        screen_clear()
        cprint('''
                            `.-::::::::::::::::::::::::::::::::::-.`                    
                       `-+ydmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmhs/.`               
                     `+hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNms-`             
                   ./omNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmdh+`           
                  -ssymNNNNmddddddddddddddddddddddddddddddddddddddddmNNNNNNNh-          
                 +dmmNNNNm+.````````````````````````````````````````-oNNNNNNNd:         
                :mNNNNNNNh`         ``                    ``         .dNNNNNNNd-        
               `hNNNNNNNNy      `:oyyys+-`            `:oyyys+-`     .dNNNNNNNNy        
               :mNNNNNNNNy     -yNNNdsymms.          -yNmysmNNms.    .dNNNNNNNNm.       
               /NNNNNNNNNy    `hNNNN   dNNs         `hNNh  yNNNNs`   .dNNNNNNNNm:       
               /NNNNNNNNNy    -mNNNNNmmNNNd`        .mNNNmmNNNNNd.   .dNNNNNNNNm:       
               /NNNNNNNNNy    `sNNNNNNNNNNo         `yNNNNNNNNNNo    .dNNNNNNNNm:       
               /NNNNNNNNNy     `odNNNNNNd/`          `odNNNNNNd/`    .dNNNNNNNNm:       
               /NNNNNNNNNy       `-/++/-`              `-/++/-`      .dNNNNNNNNm:       
               /NNNNNNNNNy                                           .dNNNNNNNNm:       
               /NNNNNNNNNy             `s+/..      .:oyo             .dNNNNNNNNm:       
               :NNNNNNNNNy             `syysmdhhhddmNNN+             .dNNNNNNNNm-       
               .dNNNNNNNNy              `+hydmmNmmmdmmo`             .dNNNNNNNNh`       
                oNNNNNNNNy               `/syo++++oys:`              .dNNNNNNNm/        
                `yNNNNNNNd-                `.:://:-.`               `:mNNNNNNNo`        
                 .sNNNNNNNdsooooooooooooooooooooooooooooooooooooooooymNNNNNNmo`         
                  `/dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh:           
                    .+hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmh/`            
                      `:ohmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmh+-`              
                          .:/osyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysso/-.                  




                ''', 'green')
        print("""
                                  <crackling noise and static>""")
        applied = input("""
            Did you apply for a job? Shall we send a rescue craft and bring you back 
                                  to Spriggy Inc. H.Q.? Y/N >""")
        if applied.lower() == "y":
            endSpriggy()
        else:
            print("""
                Ok! Thanks you for taking the time to talk to a simple robot like me.
                             Stay safe. I hope the mosters dont eat you!""")
            print("\n" * 3)
            input("Hit RETURN to continue > ")
            computer()
    else:
        print("You shouldn't go around doing things that don't make sense...")
        print("\n" * 3)
        input("Hit RETURN to continue > ")
        job()
    job()


# Workshop special location logic like using resources
def workshop():
    global supplies
    if 'tools' not in supplies:
        if 'sticks and rocks' not in supplies:
            print("\nYou have no tools. If only you could find some sticks and rocks!")
            input("Hit RETURN to continue > ")
        else:
            toolChoice = input("Would you like to build some tools with your sticks and rocks? Y/N > ")
            if toolChoice.lower() == "y":
                print("""
                You set to work on the sticks and rocks.
                After several hours, you emerge with a set of tools. 
                You can now work on other things!""")
                supplies.append('tools')
                supplies.remove('sticks and rocks')
    else:
        print("\nYou have the following to work from:")
        for n in supplies:
            print(n)
        print("\nWhat would you like to work with? hit RETURN to go back to the ship.")
        workWith = input("> ")
        workWith = workWith.lower()
        if workWith == "":
            myTurn()
        elif workWith not in supplies:
            print("Sorry, you don't have that with you.")
            workshop()
        elif workWith == 'gillyweed':
            print("""
            You set to work on the gillyweed. 
            After several hours, you emerge with a breather.""")
            supplies.remove('gillyweed')
            supplies.append('breather')
        elif workWith == 'raw vegetables':
            print("""
            You set to work on the raw vegetables.
            After several hours, you emerge with two pieces of food.""")
            supplies.remove('raw vegetables')
            supplies.append('food')
            supplies.append('food')
        elif workWith == "flint":
            print("""
            You set to work on the flint.
            After several hours, you emerge with a spear.""")
            supplies.remove('flint')
            supplies.append('spear')
            if 'blade' in supplies:
                print("""
                \nAfter consideration, you realize that it isn't as strong as your blade.
                You leave it here.""")
                supplies.remove('spear')
        elif workWith == 'metal ore':
            print("""
            You set to work with the metal ore.
            After several hours, you emerge with a blade.""")
            supplies.remove('metal ore')
            supplies.append('blade')
            if 'spear' in supplies:
                supplies.remove('spear')
        elif workWith == 'pulse crystal dust':
            print("""
            You set to work on the pulse crystal dust.
            After many days, you realize it is not enough to power the ship.
            If only you could find more!!""")
        elif workWith == 'pulse crystals':
            finish()
        else:
            print("Sorry, there's nothing you can do with that.")

    print("\n" * 3)
    myTurn()


# Handle picking up items
def pickup(item):
    global supplies
    if "backpack" not in supplies:
        if len(supplies) >= 8:
            print("Sorry, you cannot carry more than 8 things!")
        else:
            print(f"You've added ${item} to your supplies!")
            supplies.append(item)
    else:
        print(f"You've added ${item} to your supplies!")
        supplies.append(item)


# Backpack
def backpack():
    global supplies
    # not implimented


# Death... Its coming for all of us
def dead(reason):
    screen_clear()
    print("""                                        
                         :-+**##%%##*+=-.                        
                    .-*%@@@@@@@@@@@@@@@@@@#+:                    
                  -#@@@@@@@@@@@@@@@@@@@@@@@@@%+.                 
               .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-               
              =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.             
             *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:            
            *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.           
           :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*           
           +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           
           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:          
           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:          
           *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          
           :@@@@@@@@@@@%%%%@@@@@@@@@@@%%%%@@@@@@@@@@@#           
            #@@@@@@%=.      -@@@@@@@*.     .-*@@@@@@@:           
            .@@@@@#          -@@@@@%          -@@@@@+            
             .%@@@-          =@@@@@%           @@@@+             
              :@@@#.       :+@@@@@@@%-        =@@@#              
              :@@@@@#****#@@@@@@=*@@@@@%#***#@@@@@*              
              -@@@@@@@@@@@@@@@@.  *@@@@@@@@@@@@@@@%              
              :@@@@@@@@@@@@@@@-    %@@@@@@@@@@@@@@*              
                -+*###%@@@@@@@#*##*@@@@@@@@%##**=.               
         :+*+=.        .@@@@@@@@@@@@@@@@@+         -+*+=         
        *@@@@@@+       .@@@@@@@@@@@@@@@@@*       :%@@@@@@:       
        @@@@@@@@=      +@@@@@@@@@@@@@@@@@@      .%@@@@@@@+       
       .@@@@@@@@@=      =#%@@@@@@@@@@@@%+:     .%@@@@@@@@+       
     -#@@@@@@@@@@@%=.       .:------:.       -*@@@@@@@@@@@@+.    
    =@@@@@@@@@@@@@@@@%+:                 .=#@@@@@@@@@@@@@@@@%    
    -@@@@@@@@@@@@@@@@@@@@#+:         .=*@@@@@@@@@@@@@@@@@@@@#    
     :*%@@%*+-:-=+#@@@@@@@@@@#+: .=*%@@@@@@@@@%*=-:-=+#%@@#=     
                    .-+#@@@@@@@@@@@@@@@@@%*=:                    
                        .+@@@@@@@@@@@@@#-                        
        ..         .-+#@@@@@@@@@@@@@@@@@@@%*=:          ..       
     =%@@@@%*+==*#@@@@@@@@@@%*-.  :=#@@@@@@@@@@%*+==*#@@@@@*.    
    =@@@@@@@@@@@@@@@@@@@%*-.          :=#@@@@@@@@@@@@@@@@@@@%    
    :@@@@@@@@@@@@@@@@*-.                  :+%@@@@@@@@@@@@@@@#    
     .+%@@@@@@@@@@*:                         .=%@@@@@@@@@@#=     
        @@@@@@@@%.                              *@@@@@@@@=       
        @@@@@@@@:                                #@@@@@@@+       
        +@@@@@%-                                  *@@@@@%.       
          -=-:                                     .-=-:                   

                  _____  ______          _____  
                 |  __ \|  ____|   /\   |  __ \ 
                 | |  | | |__     /  \  | |  | |
                 | |  | |  __|   / /\ \ | |  | |
                 | |__| | |____ / ____ \| |__| |
                 |_____/|______/_/    \_\_____/ 

    """)
    print(reason)
    print("\n\n\nYou have died, alone, without a trace, with nobody to mourn your passing")
    print("\n\n\n\t\t\tGAME OVER\n\n\n")
    exit(0)


# Spriggy applicant end sequence.
def endSpriggy():
    screen_clear()
    print("\tFor days, you wait, not sure if you can\n\thold out while you wait for the rescue craft.")
    print("\tYou wonder out loud, 'Did they get my\n\tmessage? Am I still all alone?'")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tMonsters claw and scrape at the ship day and\n\tnight, pulling panels from their housing...")
    print("\tAny fleeting moment could mean the end of your\n\tship and you'll be stranded here forever...")
    print("\tA week passes, then two, food has run out,\n\twater is down to sips, not cups...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tThe monsters are almost in now.  Their claws tear\n\tat the fuselage...but you are too weak to fight...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tWith trembling fingers on your blaster trigger, you\n\tconsider... who should I use this last shot on...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tPEW! PEW!... blasters... then the scream of lander\n\trockets... the scream of monsters fleeing...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tThe steady reassuring thud of your rescuers boots beat\n\tin rhythm toward you like a drum.\n"
          "\tYou are saved. For the first time in months you breathe\n\tfreely... deep exhales give way to deep heaving  sobs...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tWith tears in your eyes, you stare off into the sky, just\n\tlike the night you landed...")
    print("\tBut now rather than being filled with foreboding, it is\n\tfilled with hope, filled with promise...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print(
        "\tAs the warp drive engages, the Spriggy logo blurs across\n\tthe starless sky... and with it, it is taking you...")
    print("\t... home")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("""

                  ___           ___                    ___           ___          _____    
      ___        /__/\         /  /\                  /  /\         /__/\        /  /::\   
     /  /\       \  \:\       /  /:/_                /  /:/_        \  \:\      /  /:/\:\  
    /  /:/        \__\:\     /  /:/ /\              /  /:/ /\        \  \:\    /  /:/  \:\ 
   /  /:/     ___ /  /::\   /  /:/ /:/_            /  /:/ /:/_   _____\__\:\  /__/:/ \__\:|
  /  /::\    /__/\  /:/\:\ /__/:/ /:/ /\          /__/:/ /:/ /\ /__/::::::::\ \  \:\ /  /:/
 /__/:/\:\   \  \:\/:/__\/ \  \:\/:/ /:/          \  \:\/:/ /:/ \  \:\~~\~~\/  \  \:\  /:/ 
 \__\/  \:\   \  \::/       \  \::/ /:/            \  \::/ /:/   \  \:\  ~~~    \  \:\/:/  
      \  \:\   \  \:\        \  \:\/:/              \  \:\/:/     \  \:\         \  \::/   
       \__\/    \  \:\        \  \::/                \  \::/       \  \:\         \__\/    
                 \__\/         \__\/                  \__\/         \__\/                  

                               THANK YOU FOR PLAYING SPRIGALON 5
                 OUR TEAM WILL CONTACT YOU SHORTLY REGARDING YOU APPLICATION.
                      THANK YOU FOR CONSIDERING SPRIGGY AS YOUR NEW HOME.
          PLEASE TAKE A MOMENT TO LOOK AT OUR OTHER OUTSTANDING CAREER OPPORTUNITIES


    """)
    print("\n" * 3)
    print("Hit ENTER to quit")
    input("> ")
    webbrowser.open("https://www.spriggy.com.au/careers")
    exit(0)


# End of game final scene sequence
def finish():
    screen_clear()
    print("\tFor days, you delicately work on the pulse crystals.")
    print("\tAny tiny mistake will mean the end of your ship. You'll be stranded here forever...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tFinally the crystals are calibrated. You install them in the ship's engine...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tWith trembling fingers, you fire up the engine...")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tIT WORKS!")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("\tYou point the ship towards the stars.")
    print("\tWith tears in your eyes, you vanish into the night.")
    print("\n" * 3)
    print("Hit ENTER to continue")
    input("> ")
    screen_clear()
    print("""

                     ___           ___                    ___           ___          _____    
         ___        /__/\         /  /\                  /  /\         /__/\        /  /::\   
        /  /\       \  \:\       /  /:/_                /  /:/_        \  \:\      /  /:/\:\  
       /  /:/        \__\:\     /  /:/ /\              /  /:/ /\        \  \:\    /  /:/  \:\ 
      /  /:/     ___ /  /::\   /  /:/ /:/_            /  /:/ /:/_   _____\__\:\  /__/:/ \__\:|
     /  /::\    /__/\  /:/\:\ /__/:/ /:/ /\          /__/:/ /:/ /\ /__/::::::::\ \  \:\ /  /:/
    /__/:/\:\   \  \:\/:/__\/ \  \:\/:/ /:/          \  \:\/:/ /:/ \  \:\~~\~~\/  \  \:\  /:/ 
    \__\/  \:\   \  \::/       \  \::/ /:/            \  \::/ /:/   \  \:\  ~~~    \  \:\/:/  
         \  \:\   \  \:\        \  \:\/:/              \  \:\/:/     \  \:\         \  \::/   
          \__\/    \  \:\        \  \::/                \  \::/       \  \:\         \__\/    
                    \__\/         \__\/                  \__\/         \__\/                  

                                THANK YOU FOR PLAYING SPRIGALON5.
                     WE HOPE YOU ENJOYED THE GAME.  TAKE A MOMENT TO CONSIDER
                OUR CAREERS PAGE.  WE MAY JUST BE THE PERFECT PLACE TO CALL HOME


       """)
    print("\n" * 3)
    print("Hit ENTER to quit")
    input("> ")
    webbrowser.open("https://www.spriggy.com.au/careers")
    exit(0)


health = 100
map = {'North': '?', 'Far North': '?', 'Northwest': '?', 'Northeast': "?", 'West': '?', 'East': '?', 'South': '?',
       'Southwest': '?', 'Southeast': '?'}
supplies = ['food', 'food', 'food']
myLocation = ship

start()
myTurn()
