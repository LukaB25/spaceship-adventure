import os

print("SPACESHIP ADVENTURE \n")


def clear():
    """
    Clears the terminal before continuing with the code.
    Code was taken and implemented from Dante Lee's video tutorial:
    https://www.youtube.com/watch?v=lI6S2-icPHE&t=57s
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game_message():
    """
    Prints out the welcome message and some details to set the scene.
    Offers some insight in the game for the user.
    """
    print("Welcome to your spaceship adventure!")
    print("It is a year 3076. You are an interplanetary traveler, "
          "at least that is what they said you will be. \n")
    print("Due to an overpopulation on our home planet Earth"
          "the collective government devised a plan to send three million "
          "people to the newly discovered habitable planet.")
    print("You have left your planet for a long trip "
          "through the vast space in search of a better life.\n")
    print("You are suddenly awoken. You woke up before all other travellers, "
          "and you need to find out what is going on.")
    print("Are you ready to open and leave your hibernation pod? [y/n]")


def open_hibernation_pod():
    """
    Waits for users response.
    Runs a while loop until user decides to leave the hibernation pod.
    Sets up the decision on how to progress through the game.
    """
    while True:
        pod_choice = input("> ").lower()
        if pod_choice == "yes" or pod_choice == "y":
            print("\nWith a little bit of struggle, the pod creaks open.")
            print("You step out but your legs falter, you start falling.\n")
            print("As you are falling, you decide to: \n"
                  "(a) grab onto the pod door \n"
                  "(b) grab a cord hanging from the ceiling \n"
                  "(c) risk injury from the fall\n")
            fall_choice = input("What do you do? [a/b/c] \n> ")
            return fall_choice
        elif pod_choice == "no" or pod_choice == "n":
            print("\nYou chose not to open the hibernation pod.")
            print("You fell asleep. \n")
            print("//////////////////////////////////////////\n")
            print("Let's try again.")
            print("Are you ready to open and leave the hibernation pod? "
                  "[y/n]\n")
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")


# def restart_game_choice():
#     global fall_choice  # Updates the global fall_choice
#     global cut_state    # Updates the global cut_state
#     restart_choice = input("Do you want to restart the game? [y/n] \n> ")
#     if restart_choice == "y" or restart_choice == "yes":
#         print("\nRestarting game!\n")
#         fall_choice = None
#         cut_state = 0
#         start_game_message()
#         open_hibernation_pod()
#     elif restart_choice == "n" or restart_choice == "no":
#         print("Thank you for playing!")
#         print("Closing the game")
#         quit()


fall_choice = None
cut_state = 0
navigation_threat = 0


def bleeding_wound(cut_state):
    """
    Handles user choice to fall and deals damage until user either finds
    bandages or reaches critical state.
    """

    cut_state += 1
    if cut_state <= 5:
        print("You are slowly bleeding out, "
              "find some bandages quickly.")
        print(f"You are hurt, reach the Med Bay: {cut_state}/6")
    elif cut_state == 6:
        print(f"You reached critical state {cut_state}/6. "
              "You didn't reach Med Bay.")
        print("You died.")
        quit()
    return cut_state


def navigation_failure(navigation_threat):
    """"
    Handles the player's actions and choices after they decide to explore
    the screens in the Control Room.
    The user will have certain amount of steps to reach the Airlock and to
    exit to repair the ships navigation controls.
    """
    navigation_threat += 1
    if navigation_threat <= 3:
        print("Navigation failure! Approaching a critical "
              f"level. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    elif navigation_threat <= 6:
        print("Navigation failure! Critical condition "
              f"nearing severity. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    elif navigation_threat <= 9:
        print("Navigation failure! Critical state "
              f"is imminent. Level: {navigation_threat}/10")
        print("Manual reboot necessary.\n")
    else:
        print("Navigation failure! Critical state "
              f"reached. Level: {navigation_threat}/10\n"
              "The ship has entered an asteroid field.\n")
        print("/////////////////////\n")
        print("Collision in:\n")
        print("3")
        print("2")
        print("1")
        print("BANG\nBLAST\nBLOW\nBOOM")
        print("\nThe spaceship perished.")
        print("You died.")
        print("The End.")
        quit()
    return navigation_threat


def control_room_choose_path():
    """
    Handles further progress. User is located in the control
    room and needs to choose which way they would like to
    continue going.
    """
    global cut_state, navigation_threat
    while True:
        control_path_choice = input("Which path would you like to "
                                    "take? [a/b] \n> ").lower()
        if control_path_choice == "a" and fall_choice == "a":
            print("You head left towards the Cargo Hold.")
        elif control_path_choice == "a" and fall_choice == "c":
            print("You head straight towards the Control Room.\n")
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state
        elif control_path_choice == "a" and fall_choice == "c":
            print("You head right towards the Med Bay.")
            print("Eager to continue exploring.")
        elif control_path_choice == "b" and fall_choice == "c":
            print("You head right towards the Med Bay.")
            print("Where hopefully you will find "
                  "the bandages needed to stop the bleeding.\n")
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state


def control_room():
    """
    Handles the player's actions and choices when they reach the Control Room.
    After a user reaches Control Room they can choose to either check out
    the screens or continue with their exploration of the spaceship.
    If users decide to check the screens they get a mission to save
    everyone on the spaceship by fixing the navigation system manually
    by leaving through the airlock.
    """
    global navigation_threat
    clear()
    print("You reach the Control Room.")
    print("You are fascinated by all of the screens "
          "and blinking lights in this room.")
    print("Would you like to explore the screens "
          "or continue on?\n")
    control_room_options = input("Do you [explore/continue]? \n> ").lower()

    if control_room_options == "explore":
        print("You look at all of the screens. You reach one "
              "that is blinking with multiple error messages.")
        print("You start reading the messages, but one catches "
              "your eye.\n")
        print("Imminent threat!!! Navigation failure! Manual "
              "reboot necessary to recalibrate system.\n")
        print("You continue reading and find out you need to "
              "find the airlock, leave the spaceship and "
              "manually reboot the system from the outside.")
        navigation_threat = navigation_failure(navigation_threat)
        # Updates the navigation_threat
    elif control_room_options == "continue":
        print("You decide to ignore all of the screens and "
              "continue on your way to explore the ship.")
    else:
        print("Incorrect input, please choose [explore/continue]")


def choose_path(fall_choice):
    """
    Sets up the game progress depending on users choices.
    """
    global cut_state
    while True:
        path_choice = input("Which path would you like to "
                            "take? [a/b] \n> ").lower()

        if path_choice == "a" and fall_choice == "a":
            print("You head straight towards the Control Room.")
            print("Eager to continue exploring.\n")
            control_room()
        elif path_choice == "a" and fall_choice == "c":
            print("You head straight towards the Control Room.\n")
            cut_state = bleeding_wound(cut_state)
            control_room()
            # Updates the cut_state
        elif path_choice == "a" and fall_choice == "c":
            print("You head right towards the Med Bay.")
            print("Eager to continue exploring.")
        elif path_choice == "b" and fall_choice == "c":
            print("You head right towards the Med Bay.")
            print("Where hopefully you will find "
                  "the bandages needed to stop the bleeding.\n")
            cut_state = bleeding_wound(cut_state)
            # Updates the cut_state
        else:
            print("Invalid input. Please choose [a/b]")


def main():
    start_game_message()
    fall_choice = open_hibernation_pod()

    if fall_choice == "a":
        print("You managed to grab onto the pod door")
        print("You regained your balance and start exploring. You are "
              "in the room containing hibernation pods./n")
        print("You see two paths, you can either go straight "
              "towards the ship Control Room, or to the right "
              "towards the Med Bay.")
        choose_path(fall_choice)
    elif fall_choice == "b":
        print("You accidentally grabbed the electrical cord "
              "and got electrocuted.")
        print("You died.")
        print("The End.")
        quit()
    elif fall_choice == "c":
        print("You fell and cut your hand; you are bleeding.")
        print("You should find some bandages to cover the wound.\n")
        print("You start exploring the room.\n")
        print("You see two paths, you can either go "
              "straight towards the Control Room[a] "
              "or to the right towards the Med Bay.[b]")
        choose_path(fall_choice)
    else:
        print("You fell and back into the hibernation pod "
              "and lost consciousness.")


if __name__ == "__main__":
    main()
