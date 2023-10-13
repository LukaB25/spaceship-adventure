import os


def clear():
    """
    Clears the terminal before continuing with the code.
    Code was taken and implemented from Dante Lee's video tutorial:
    https://www.youtube.com/watch?v=lI6S2-icPHE&t=57s
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def end_game():
    """
    Ends the game at the user's request.
    """
    print("\nThank you for playing, ending the game at the user's request.")
    print("Game Ended!\n")
    quit()


def start_game_message():
    """
    Prints out the welcome message and some details to set the scene.
    Offers some insight in the game for the user.
    """
    print("Welcome to your spaceship adventure!")
    print('\nIf for any reason you decide to end the game, you can do so '
          'by writing "end" into any input field at any stage of the '
          'game.\n')
    print("It is a year 3076. You are an interplanetary traveler, "
          "at least that is what they said you will be. \n")
    print("Due to an overpopulation on our home planet Earth"
          "The Collective Government devised a plan to send three million "
          "people to the newly discovered habitable planet 'Terra Novus'.")
    print("You have left your planet for a long trip "
          "through the vast space in search of a better life.\n")
    print("You are suddenly awoken. You woke up before all other travellers, "
          "and you need to find out what is going on.")
    print("Are you ready to open and leave your hibernation pod? [y/n]")


fall_decision = None
cut_state = 0
navigation_threat = 0
navigation_error = False
bleeding = False
broken_vase = False
reboot_code = 29137


def bleeding_wound(cut_state):
    """
    Handles user choice to fall and deals damage until user either finds
    bandages or reaches critical state.
    """
    global bleeding
    if bleeding:
        cut_state += 1
        if cut_state <= 5:
            print("\nYou are slowly bleeding out, "
                  "find some bandages quickly.")
            print(f"You are hurt, reach the Med Bay: {cut_state}/6\n")
        elif cut_state == 6:
            print(f"\nYou reached critical state {cut_state}/6. "
                  "You didn't reach Med Bay.")
            print("You died.\n")
            bleeding = False
            quit()
    return cut_state


def fall_choice():
    global bleeding, cut_state
    while True:
        fall_decision = input("What do you do? [a/b/c] \n> ").lower()

        if fall_decision == "end":
            end_game()

        if fall_decision == "a":
            print("You managed to grab onto the pod door")
            print("You regained your balance and start exploring. You are "
                  "in the room containing hibernation pods.\n")
            print("You see two paths, you can either go straight "
                  "towards the ship Control Room, or to the right "
                  "towards the Med Bay.")
            choose_path(fall_decision)
        elif fall_decision == "b":
            print("You accidentally grabbed the electrical cord "
                  "and got electrocuted.")
            print("You died.")
            print("The End.")
            quit()
        elif fall_decision == "c":
            print("You fell and cut your hand; you are bleeding.")
            print("You should find some bandages to cover the wound.")

            bleeding = True
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state

            print("You start exploring the room.\n")
            print("You see two paths, you can either go "
                  "straight towards the Control Room[a] "
                  "or to the right towards the Med Bay.[b]")

            choose_path(fall_decision)
        else:
            print("\nInvalid input. Try again.")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{fall_decision}"\n')


def open_hibernation_pod():
    """
    Waits for users response.
    Runs a while loop until user decides to leave the hibernation pod.
    Sets up the decision on how to progress through the game.
    """
    while True:
        pod_choice = input("> ").lower()
        if pod_choice == "end":
            end_game()
        if pod_choice == "yes" or pod_choice == "y":
            print("\nWith a little bit of struggle, the pod creaks open.")
            print("You step out but your legs falter, you start falling.\n")
            print("As you are falling, you decide to: \n"
                  "(a) grab onto the pod door \n"
                  "(b) grab a cord hanging from the ceiling \n"
                  "(c) risk injury from the fall\n")
            fall_choice()
        elif pod_choice == "no" or pod_choice == "n":
            print("\nYou chose not to open the hibernation pod.")
            print("You fell asleep. \n")
            print("//////////////////////////////////////////\n")
            print("Let's try again.")
            print("Are you ready to open and leave the hibernation pod? "
                  "[y/n]\n")
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{pod_choice}"\n')


# def restart_game_choice():
#     global fall_decision  # Updates the global fall_decision
#     global cut_state    # Updates the global cut_state
#     restart_choice = input("Do you want to restart the game? [y/n] \n> ")
#     if restart_choice == "y" or restart_choice == "yes":
#         print("\nRestarting game!\n")
#         fall_decision = None
#         cut_state = 0
#         start_game_message()
#         open_hibernation_pod()
#     elif restart_choice == "n" or restart_choice == "no":
#         print("Thank you for playing!")
#         print("Closing the game")
#         quit()


def navigation_failure(navigation_threat):
    """"
    Handles the player's actions and choices after they decide to explore
    the screens in the Control Room.
    The user will have certain amount of steps to reach the Airlock and to
    exit to repair the ships navigation controls.
    """
    global navigation_error
    navigation_threat += 1
    if navigation_threat <= 3:
        print("\nNavigation failure! Approaching a critical "
              f"level. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    elif navigation_threat <= 6:
        print("\nNavigation failure! Critical condition "
              f"nearing severity. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    elif navigation_threat <= 9:
        print("\nNavigation failure! Critical state "
              f"is imminent. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    else:
        clear()
        print("\nNavigation failure! Critical state "
              f"reached. Level: {navigation_threat}/10\n"
              "The ship has entered an asteroid field.\n")
        print("/////////////////////\n")
        print("Collision in:\n")
        print("3")
        print("2")
        print("1")
        print("\nBANG\nBLAST\nBLOW\nBOOM")
        print("\nThe spaceship perished.")
        print("You died.")
        print("The End.")
        quit()
    navigation_error = True
    return navigation_threat


def engineering_bay_path_choice():
    """
    Handles the player's actions and choices when they decide to leave the
    Engineering Bay.
    The user can choose to explore the Engineering Bay or head left to
    leave towards the Cargo Hold, right to the observation deck or straight
    ahead into the airlock.
    """


def engineering_bay():
    """
    Handles the player's actions and choices when they arrive to the
    Engineering Bay.
    The user can choose to explore the Engineering Bay or continue
    on their way to explore the rest of the ship.
    """
    global cut_state

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    if broken_vase is True:
        print("\nAs you step into the Engineering Bay, you think back "
              "to a shadowy figure running from the broken vase.")
        print("You wonder who they might be, and where are they directing "
              "you to, why don't they just aproach you, to help with this "
              "situation we find ourselves in.")
        print("The questions keep running through your head, but you can't"
              " stop now. You continue on.")

    print("\nYou enter the room and find yourself surrounded by a magnificent "
          "array of computers, intricate crafting stations, precision "
          "constructors, and deconstructors, each humming with purpose.")
    print("You can imagine all of the tinkering that could be done in here.")
    print("You always loved to build machines that could better the life as "
          "we know today.")
    print("Maybe that was the reason you were awoken.")
    print("Would you like to explore the Engineering bay?[y]yes or [n]no")

    while True:
        explore_engineering_bay = input("\n> ")
        if explore_engineering_bay == "y" or explore_engineering_bay == "yes":
            print("\nYou start exploring and walking around. You are as exited"
                  " as a lettle kid in a chocolate factory.")
            print("Which machine would you like to explore?\n"
                  "[a] Approach the crafting station.\n"
                  "[b] Examine the constructors and deconstructors.\n"
                  "[c] Investigate the mysterious old computer in the corner "
                  "of the room.\n"
                  "[d] Decide to stop exploring and continue on your way.\n")

            while True:
                explore_choice = input("\n> ")
                if explore_choice == "a" or explore_choice == "crafting":
                    print("\nYou approach the crafting station and immediately"
                          " start looking through all of the blueprints for "
                          "various machinery.")
                    print("The blueprints reveal a world of possibilities, "
                          "with a mix of cutting-edge designs crafted "
                          "specifically for this mission and some foundational"
                          " ones.")
                    print("Some that stick out are various rovers and hovers, "
                          "each equipped with innovative features. These "
                          "vehicles seem perfect for exploring the unknown "
                          "terrain of Terra Novus.")
                    print("Additionally, you spot blueprints for an assortment"
                          " of transport and theoretical teleportation devices"
                          ", hinting at advanced methods for traveling great "
                          "distances.")
                    print("The accompanying notes explain that the "
                          "construction of such a device depends on the "
                          "availability of rare and specific minerals that can"
                          " only be foundwithin the Terra Novus galactic "
                          "system, minerals what are sadly not present on the "
                          "spaceship.")
                    print("Disappointment creeps in as you realize that "
                          "instant teleportation, which would be an "
                          "incredible asset on this journey, remains far from"
                          " being attainable.")
                    print("After realizing you have spent a while going "
                          "through the blueprints, you decide to move on.")
                          
                elif (explore_choice == "b" or explore_choice == "contructors"
                      or explore_choice == "deconstructors"):
                    print("")
                elif (explore_choice == "c" or explore_choice == "mystery"
                      or explore_choice == "computer"):
                    print("")
                elif (explore_choice == "d" or explore_choice == "stop"
                      or explore_choice == "continue"):
                    print("")
                else:
                    print("Invalid input, your choices are [a/b/c/d]")
                    print('You can end the game by typing "end"')
                    print(f'\nYou typed in "{explore_choice}"\n')

        elif explore_engineering_bay == "n" or explore_engineering_bay == "no":
            print("")
        else:
            print("Invalid input, your choices are [y]yes or [n]no")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{explore_engineering_bay}"\n')


def escape_pods_lift_ending():
    """
    Handles another possible ending depending on the player's choices so far.
    The game ends in the softer tone, leaving an opening for future additions
    to the game.
    The user can choose to leave the Control Room across the room towards
    the Engineering Bay or to use a lift to go down into Escape Pods.
    """
    global cut_state

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    print("\nAs the elevator starts to ascend to the Cargo Hold, it "
          "suddenly halts and the metallic groans grow louder and more "
          "unsettling, echoing within the confined space.")
    print("The pit in your stomach doubles in size and you start to panic.")
    print("You can feel your end is near, the cold shiver running down your "
          "spine.")
    print("The metallic groans intensify, reaching an ear-piercing screech, "
          "just as the elevator takes a sudden alarming dive.")
    print("\n You never should have decided to leave for this expedition.")
    print("In the last seconds you wish to be back in your tiny apartment"
          "safe in your bed, waking up from this nightmare, but...")
    print("\nEverything goes dark, you loose consciousness and slip away "
          "into nothingness.")
    print("\nThe End.")


def escape_pods():
    """
    Handles the player's actions and choices when they arrive to the
    Escape Pods.
    The user can choose to save themselves or use a lift and go back into
    Cargo Hold and continue to explore the rest of the ship.
    """
    global cut_state, navigation_threat

    global cut_state
    if bleeding is False:
        clear()

    print("Only few seconds pass before the elevator stops.\n")
    print("The doors swing open, and you find yourself in a state "
          "of awe.")
    print("As you look around, you notice a numerous escape pods, "
          "each with its own unique design, waiting to be explored.\n"
          "The soft, pulsating glow of their control panels and the "
          "promise of safety within them beckon you closer.")

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    if navigation_error is True:
        print("\nYou can't help but remember the unsettling navigation error "
              "and the looming threat of a critical system failure, which "
              "hangs like a heavy cloud over your thoughts.")
        print("The weight of responsibility presses on your shoulders.")
        print("The stress of it all seems a bit too much to handle.")
        print("Being at this place, you start to feel a nudge towards using "
              "an escape pod.")
    else:
        print("\nYou can't help but think of all of the mysteries that are "
              "surrounding the whole scenario since you woke up.")
        print("The uncertainty of the whole situation looms over you as "
              "a shadow.\n")

    print("Do you: [a]give into the feeling and escape or [b] turn around"
          " and go back to try and save everyone?")

    while True:
        escape_pod_option = input("\n> ")

        if escape_pod_option == "end":
            end_game()
        if navigation_threat > 0:
            navigation_threat = navigation_failure(navigation_threat)
            # Updates the navigation_threat

        if escape_pod_option == "a" or escape_pod_option == "escape":
            if navigation_error is True:
                print("\nAs the weight of responsibility becomes too much to "
                      "bear on your own, the overwhelming stress drives you to"
                      " make the difficult decision to leave.")
            print("\nWith a heavy heart and knowing that you are leaving "
                  "behind the lives of your fellow travelers. You step "
                  "into one of the escape pods.")
            print("As the pod door seals shut, you look out the window,"
                  " gazing one last time at the massive starship that "
                  "had been your home.")
            print("\nAt the push of a button your escape pod disengages "
                  "and drifts away into the unknown depths of space, "
                  "leaving behind the vessel and your companions.")
            print("Tears start to stream down your face as you watch "
                  "the distance between you and the ship grow, knowing "
                  "the choice you just made and that you may never see "
                  "them again.")
            print("You're filled with a mix of relief and sorrow, haunted"
                  " by the choice you have just made.")
            if navigation_error is True:
                print("\nThe road to Terra Novus is uncertain, but at least "
                      "you managed to escape the impending doom.")
            else:
                print("\nThe road to Terra Novus is unknown, but at least "
                      "you managed to escape the uncertainty.")
            print("\nAs you speed through space, a shadowy figure is staring"
                  " at your escape pod from the ship, their identity and "
                  "intentions veiled in mystery, you get an unsettling "
                  "sense of uncertainty and a feeling of dread that this"
                  " is not completely over.\n")
            print("...\n")
            print("The End.")
            print("\nThank you for playing")
            quit()
        elif escape_pod_option == "b" or escape_pod_option == "save":
            print("\nAs you start thinking about the weight of the "
                  "responsibility, you start doubting whether you can do "
                  "this or not.")
            print("You push your fears and doubts aside and start thinking"
                  "about the numerous fellow travellers that are unaware"
                  " of the predicament that we are in.")
            print("You can't get yourself to leave them behind.")
            print("You turn around and leave the escape pods section, "
                  "your determination to help them and make a difference"
                  " outweighs all your fears and uncertainties.")
            print("You step into the elevator and head on upstairs, back "
                  "into the Cargo Hold")
            escape_pods_lift_ending()
        else:
            print("Invalid input, your choices are [a]escape or [b]go back")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{escape_pod_option}"\n')


def cargo_hold_path_choice():
    """
    Handles the player's actions and choices when they decide to leave
    the Cargo Hold.
    The user can choose to leave the Control Room across the room towards
    the Engineering Bay or to use a lift to go down into Escape Pods.
    """
    global cut_state, navigation_threat, broken_vase

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    print("\nAs you start to leave, a large Egyptian vase falls in "
          "the distance. \nYou jump, startled out of your mind, you "
          "run in the direction of the fallen vase.\n")
    print("You explore the rubble and realise that the vase couldn't"
          " have fallen on it's own. \nYou see a shadow running away "
          "from you.")
    print("You decide to follow, but soon find yourself at the cross "
          "section. \nWhich way do you follow?"
          "\n[a] left into the suspiciously old and unmarked lift that "
          "takes you down a level"
          "\n[b] right into the Engineering Bay")

    broken_vase = True

    while True:
        cargo_hold_path_options = input("\n> ")

        if cargo_hold_path_options == "end":
            end_game()
        if navigation_threat > 0:
            navigation_threat = navigation_failure(navigation_threat)
            # Updates the navigation_threat

        if (cargo_hold_path_options == "a" or
                cargo_hold_path_options == "left"):
            print("\nYou step into the mysterious elevator, its metal doors "
                  "creak and slide shut as it whisks you away to a lower "
                  "level.\n")
            print("Riding the elevator, you realise you don't know where "
                  "you are going, you start to doubt whether it was a "
                  "smart idea just to jump in like that...\n")
            escape_pods()
        elif (cargo_hold_path_options == "b" or
              cargo_hold_path_options == "right"):
            print("You decide to follow to the Engineering Bay, hoping "
                  "your mind is not playing tricks on you, or worse"
                  "you have started loosing your mind and are becoming"
                  " delirious.")
            print("You run as fast as your legs can carry you. But "
                  "can't seem to catch up.")
            engineering_bay()
        else:
            print("Invalid input, your choices are [a/b/c/d]")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{cargo_hold_path_options}"\n')


def cargo_hold():
    """
    Handles the player's actions and choices when they reach the Cargo Hold.
    After a user reaches Control Room they can choose to explore the Cargo
    Hold, or continue on exploring the ship.
    """
    global cut_state, navigation_threat

    global cut_state
    if bleeding is False:
        clear()

    print("\nAs you continue your exploration, you eventually reach "
          "the massive Cargo Hold.\n")
    print("The Cargo Hold is filled with an array of cargo: stacked "
          "boxes, vital supplies, sturdy containers, various vehicles, "
          "reserves of fuel, an assortment of spare parts, live animal "
          "specimens in their own special cryo-hibernation chambers and more.")

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    while True:
        cargo_hold_options = input("Which part of the Cargo Hold "
                                   "would you like to explore?\n"
                                   "[a] boxes and supplies\n"
                                   "[b] vehicles\n"
                                   "[c] specimens\n"
                                   "[d] continue on/ don't explore\n> ")

        if cargo_hold_options == "end":
            end_game()

        if navigation_threat > 0:
            navigation_threat = navigation_failure(navigation_threat)
            # Updates the navigation_threat
        if cargo_hold_options == "a" or cargo_hold_options == "box":
            print("\nYou start reading the signs on all of the boxes "
                  "and containers")
            print("You have been searching through boxes for hours...")
            print("You have discovered various Ancient Relics, Rare Minerals, "
                  "advanced holo communicators...")
            print("After spending another hour of searching you reached a "
                  "heavily armoured cage containing various advanced "
                  "weaponry and ammunition, mining and building "
                  "tools...\n")
            print("You decide to stop exploring the supply boxes "
                  "and containers")
        elif (cargo_hold_options == "b" or
                cargo_hold_options == "vehicles"):
            print("\nYou continue walking among all of the advanced "
                  "and antique vehicles and machinery.")
            print("You are awed by the vast array before your sight.")
            print("There are numerous hover crafts, flying saucers, "
                  "antique cars, excavators, diggers, but also "
                  "the all mighty Structure Synthesizers and "
                  "Instant Fabricators")
            print("You remember the first time you saw Structure "
                  "Synthesizer at work. It managed to construct "
                  "the whole ten story building in a matter of "
                  "seconds.")
            print("After hours of exploring you decide to stop "
                  "exploring the vehicles that The Collective "
                  "Government supplied us with.")
        elif (cargo_hold_options == "c" or
                cargo_hold_options == "specimens"):
            print("You choose to examine the collection of live "
                  "animal specimens that were sent with us on this "
                  "journey to Terra Novus.")
            print("You find yourself at a loss for words, completely "
                  "captivated by the magnificent sight.")
            print("All the specimens lay within specialized cryo-hibernation "
                  "chambers, in a peaceful slumber awaiting our arrival to "
                  "the new world, our new home.")
            print("We were equipped with an extensive array of livestock, "
                  "mammals, a variety of avian species, as well as insects "
                  "and critters, and new variety of spicies that scientist "
                  "managed to create just for this expedition all intended "
                  "to populate our new world.")
            print("You could continue exploring the animal specimens for "
                  "days, but you know it is time to continue with your "
                  "exploration of the ship.")
        elif (cargo_hold_options == "d" or
                cargo_hold_options == "continue"):
            print("You made a decision to continue exploring the ship.")
            print("Who knows what you might find next...")
            cargo_hold_path_choice()
        else:
            print("Invalid input, your choices are [a/b/c/d]")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{cargo_hold_options}"\n')


def control_room_choose_path():
    """
    Handles the player's actions and choices which
    way they would like to go from the Control Room.
    User is located in the Control Room and needs
    to choose which way they would like to continue going.
    """
    global cut_state, navigation_threat
    print("You find yourself at the cross section. Your options are: \n"
          "Go left into the Cargo Hold [a] or "
          "go right into the Engineering Bay [b]?")

    while True:
        control_path_choice = input("Which path would you like to "
                                    "take? [a/left or b/right] \n> ").lower()
        if control_path_choice == "end":
            end_game()

        if control_path_choice == "a" or control_path_choice == "left":
            print("You head left towards the Cargo Hold.")
            cargo_hold()
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state
            if navigation_threat > 0:
                navigation_threat = navigation_failure(navigation_threat)
                # Updates the navigation_threat
        elif control_path_choice == "b" or control_path_choice == "right":
            print("You head right towards the Engineering Bay.")
            print("Wondering what might you find there.")
            engineering_bay()
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state
            if navigation_threat > 0:
                navigation_threat = navigation_failure(navigation_threat)
                # Updates the navigation_threat
        else:
            print("Invalid input, you can go either [a]left or [b]right")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{control_path_choice}"\n')


def control_room():
    """
    Handles the player's actions and choices when they reach the Control Room.
    After a user reaches Control Room they can choose to either check out
    the screens or continue with their exploration of the spaceship.
    If users decide to check the screens they get a mission to save
    everyone on the spaceship by fixing the navigation system manually
    by leaving through the airlock.
    """
    global cut_state, navigation_threat

    if bleeding is False:
        clear()

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    print("\nYou reach the Control Room.")
    print("You are fascinated by all of the screens "
          "and blinking lights in this room.")
    print("You can explore the screens "
          "or continue on?\n")

    while True:
        control_room_options = input("Do you [a/explore or b/continue]? "
                                     "\n> ").lower()

        if control_room_options == "end":
            end_game()

        if control_room_options == "explore" or control_room_options == "a":
            print("\nYou look at all of the screens. You reach one "
                  "that is blinking with multiple error messages.")
            print("You start reading the messages, but one catches "
                  "your eye.\n")
            print(("Imminent threat!!! Navigation failure! Manual "
                  "reboot necessary to recalibrate system.\n").upper())
            print("...you must find the airlock, leave the spaceship and "
                  "manually reboot the system from the outside.")
            print(f"System reboot code: {reboot_code}")
            navigation_threat = navigation_failure(navigation_threat)
            break
            # Updates the navigation_threat
        elif control_room_options == "continue" or control_room_options == "b":
            print("You decide to ignore all of the screens and "
                  "continue on your way to explore the ship.")
            break
        else:
            print("Incorrect input, please choose [a]explore or [b]continue")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{control_room_options}"\n')

    control_room_choose_path()


def healing_procedure():
    """
    Healing procedure that runs after the user arrives to the Med Bay
    and decides to try using the Regenesis Chamber 3000. It updates
    the bleeding variable to False to disable the bleeding_wound function.
    """
    global bleeding

    print("Scanning the wound.")
    print("Decontamination")
    print("Tissue Regeneration")
    print("Cellular Rejuvenation")
    print("Completion")
    bleeding = False


def forceful_healing_procedure():
    """
    Forceful healing procedure that runs after the user arrives to the Med Bay
    and decides to try using the Regenesis Chamber 3000 but decides they don't
    want to heal an existing wound. The system tries to force a
    healing_procedure onto the user, which ends up ending users life and the
    Regenesis Chamber 3000 starts shutting down.
    """
    print("\nSpecimen denies healing procedure.. Error..")
    print("Forcefull healing engaged.")
    print(("Restraints engaged!\n").upper())
    healing_procedure()
    print("\nInjecting a short term memory loss serum.")
    print("Error.. error..")
    print("Specimen has received the wrong serum.\n")
    print("Regene.. \nCham.. \n30.. shut.. \ndow..")
    print("\n/////////////////\n")
    print("You have received a deadly dose of serum.")
    print("You died.")
    print("The End")
    quit()


def med_bay_choose_path():
    """
    Handles the player's actions and choices when in the Med Bay.
    The user can choose to continue exploring the spaceship and continue
    moving through the rest of the rooms left to explore.
    """
    global cut_state

    global cut_state
    if bleeding is False:
        clear()

    print("You walk through the Med Bay exploring.")
    print("You pass around the Regenesis Chamber 3000 and "
          "reach two corridors.\n")
    print("To your left you can see the long winding corridor "
          "that will take you to the Observation Deck[a]")
    print("To your right you have a straight path into the Library[b]\n")

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    while True:
        med_bay_path_choice = input("What would you like to explore? "
                                    "[a/left or b/right] \n> ").lower()

        if med_bay_path_choice == "end":
            end_game()

        if med_bay_path_choice == "a" or med_bay_path_choice == "left":
            print("\nYou take the long winding corridor towards the "
                  "Observation Deck.")
            print("You turn the corner and find yourself rendered speechless"
                  " by the most breathtaking sight you ever witnessed.\n")
            print("The room is an enormous, circular cascading staircase, "
                  "offering a panoramic view of a brilliant tapestry of stars"
                  " and planets gracing throught the glass wall.\n")
            print("You sit down, taking in the view, feeling humbled and small"
                  " in the vastness of the universe that surrounds you.")
            print("You feel at home. As if you were meant to be there.\n")
            print("Time stretches on, but you decide it is time to continue "
                  "your exploration. \nYou silently promise yourself to return"
                  " to this place.")
        elif med_bay_path_choice == "b" or med_bay_path_choice == "right":
            print("\nYou decide to head through the small straight corridor"
                  " to your right")
            print("As you begin to walk, you can't help but be awed by the "
                  "vastness of the library; its expanse seems to stretch on"
                  "endlessly...\n")
            print('You recall the brochures you received about the expedition.'
                  ' "Our Library holds every book in human existence, in every'
                  ' language. All books are also available in digital, audio '
                  'and holographic form."\n')
            print("In center of the room, you see a single book open on the "
                  "table. It peaks your interest...")
            print("You approach it, looking arround you, trying to see if "
                  "there is someone else there, someone else that is awake "
                  "same as you are.\n")
            shout = ("Hello, is there anybody here??").upper()
            print(f"You shout: {shout}. \n But nobody answers. "
                  "\nYou are left intrigued. \nWho left that book?!\n")
            print("You explore the room further, but decide it is time to "
                  "continue with your exploration of the ship.")
        else:
            print("\n Invalid input. Please choose [a]left or [b]right")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{med_bay_path_choice}"\n')


def med_bay():
    """
    Handles the player's actions and choices when they reach the Med Bay.
    After a user reaches Med Bay they can choose to either check their health,
    heal their wound and stop the bleeding if they were damaged at the start
    or they can continue with their exploration of the spaceship.
    """
    global cut_state
    if bleeding is False:
        clear()

    cut_state = bleeding_wound(cut_state)
    # Updates the cut_state

    print("You enter the Med Bay. Straight away you notice "
          "all of the medical supplies. You are mesmerised "
          "by the size of it, you couldn\'t even imagine "
          "something like that would fit onto the ship.\n")

    print("Amongst the sea of medical supplies, you notice a "
          "machine in the middle of the room. You approach it.")
    print("\nRegenesis Chamber 3000. Sounds so majestic.\n")
    print("You remember all of the advertising the collective "
          "government made, trying to sell them for at "
          "home use back in the day.\n")
    while True:
        healing_chamber = input("Would you like to test your health? "
                                "[y/n] \n> ")

        if healing_chamber == "end":
            end_game()

        if healing_chamber == "y" or healing_chamber == "yes":
            print("\nScanning...\n")
            print("Scan complete!")
            if bleeding:
                print("Anomaly detected.")
                print("Wound detected on the left forearm.")
                heal_wound = input("Would you like to heal the wound? "
                                   "[y/n] \n> ").lower()

                if heal_wound == "y" or heal_wound == "yes":
                    healing_procedure()
                elif heal_wound == "n" or heal_wound == "no":
                    forceful_healing_procedure()
                elif heal_wound == "end":
                    print("Thank you for playing, ending game at user "
                          "request.")
                    print("Game Ended!")
                    quit()
                print("Thank you for using Regenesis Chamber 3000")
            else:
                print("No anomalies detected.")
                print("\nYou are a healthy specimen.\n")
            print("Thank you for using Regenesis Chamber 3000\n")
            med_bay_choose_path()
        elif healing_chamber == "n" or healing_chamber == "no":
            med_bay_choose_path()
            if cut_state > 0:
                cut_state = bleeding_wound(cut_state)
                # Updates the cut_state
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{healing_chamber}"\n')


def choose_path(fall_decision):
    """
    Sets up the game progress depending on users choice at the
    beginning of the game.
    User gets a different message depending on what they chose
    to do in the beginning of the game.
    """

    while True:
        path_choice = input("Which path would you like to "
                            "take? [a/straight or b/right] \n> ").lower()

        if path_choice == "end":
            end_game()

        if (path_choice == "a" or path_choice == "straight"
                and fall_decision == "a"):
            print("You head straight towards the Control Room.")
            print("Eager to continue exploring.\n")
            control_room()
        elif (path_choice == "a" or path_choice == "straight"
              and fall_decision == "c"):
            print("You head straight towards the Control Room.\n")
            control_room()
        elif (path_choice == "b" or path_choice == "right"
              and fall_decision == "a"):
            print("You head right towards the Med Bay.")
            print("Eager to continue exploring.")
            med_bay()
        elif (path_choice == "b" or path_choice == "right"
              and fall_decision == "c"):
            print("You head right towards the Med Bay.")
            print("Where hopefully you will find "
                  "the bandages needed to stop the bleeding.\n")
            med_bay()
        else:
            print("Invalid input. Please choose [a]straight or [b]right")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{path_choice}"\n')


def main():
    """
    Starts the game progress and controls the outcomes depending on the
    initial user choice of what they decided to do in the beginning of
    the game.
    """
    clear()

    print("SPACESHIP ADVENTURE \n")
    start_game_message()
    open_hibernation_pod()


if __name__ == "__main__":
    main()
