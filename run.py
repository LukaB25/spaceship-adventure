print("SPACESHIP ADVENTURE \n")

def start_game_message():
    """
    Prints out the welcome message and some details to set the scene.
    Offers some insight in the game for the user.
    """
    print("Welcome to your spaceship adventure!")
    print("It is a year 3076. You are an interplanetary traveler, "
          "at least that is what they said you will be. \n")
    print("As due to an overpopulation on our home planet Earth"
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
            print("\nWith a little bit of struggle, the pod creaks open")
            print("You step out but your legs falter, you start falling.\n")
            print("As you are falling, you decide: \n"
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
            print("Are you ready to open and leave the hibernation pod? [y/n]\n")
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")


def restart_game_choice():
    restart_choice = input("Do you want to restart the game? [y/n] \n> ")
    if restart_choice == "y" or restart_choice == "yes":
        print("\nRestarting game!\n")
        start_game_message()
        open_hibernation_pod()
    elif restart_choice == "n" or restart_choice == "no":
        print("Thank you for playing!")
        print("Closing the game")
        quit()


fall_choice = None
cut_state = 0


def bleeding_wound(cut_state):
    """
    Handles user choice to fall and deals damage until user either finds
    bandages or reaches critical state.
    """
    
    cut_state += 1
    if cut_state >=5:
        print("You are slowly bleeding out, "
              "find some bandages quickly.")
    elif cut_state == 6:
        print("You reached critical state.")
        print("You died.")
        quit()
    return cut_state


cut_state = bleeding_wound(cut_state)


def choose_path(fall_choice):
    """
    Sets up the game progress depending on users choices.
    """
    global path_choice
    while True:
        path_choice = input("Which path would you like to \
take? [a/b] \n> ").lower()

        if path_choice == "a" and fall_choice == "a":
            print("You head straight towards the deck.")
            print("Eager to continue exploring.")
        elif path_choice == "a" and fall_choice == "c":
            print("You head straight towards the deck.\n")
            bleeding_wound()
            # future function that will handle bleeding outcome
        elif path_choice == "a" and fall_choice == "c":
            print("You head right towards the infirmary.")
            print("Eager to continue exploring.")
        elif path_choice == "b" and fall_choice == "c":
            print("You head right towards the infirmary.")
            print("Where hopefully you will find "
                  "the bandages needed to stop the bleeding.\n")
            bleeding_wound()
            # future function that will handle bleeding outcome
        else:
            print("Invalid input. Please choose [a/b]")
            quit()

def main():
    start_game_message()
    fall_choice = open_hibernation_pod()

    if fall_choice == "a":
        print("You managed to grab onto the pod door")
        print("You regained your balance and start exploring the room.")
        print("You see two paths, you can either go straight "
              "towards the ship deck, or to the right towards the infirmary.")
        choose_path("a")
    elif fall_choice == "b":
        print("You accidentally grabbed the electrical cord and got electrocuted.")
        print("You died.")
        print("The End.")
        restart_game_choice()
    elif fall_choice == "c":
        print("You fell and cut your hand; you are bleeding.")
        print("You should find some bandages to cover the wound.")
        print("You start exploring the room.")
        print("You see two paths, you can either go straight towards the deck[a] "
              "or to the right towards the infirmary.[b]")
        choose_path("c")
    else:
        print("You fell and back into the hibernation pod and lost consciousness.")
        restart_game_choice()

if __name__ == "__main__":
    main()