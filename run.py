print("SPACESHIP ADVENTURE \n")

print("Welcome to your spaceship adventure!")
print("It is a year 3076. You are an interplanetary traveler, \
at least that is what they said you will be. \n")
print("As due to an overpopulation on our home planet Earth, \
the collective government devised a plan to send three million \
people to the newly discovered habitable planet.")
print("You have left your planet for a long trip \
through the vast space in search of a better life.\n")
print("You are suddenly awoken. You woke up before all other travellers, \
and you need to find out what is going on.")
print("Are you ready to open and leave your hibernation pod? [y/n]\n")


def open_hibernation_pod():
    """
    Waits for users response.
    Runs a while loop until user decides to leave the hibernation pod.
    Sets up the decision on how to progress through the game.
    """
    while True:
        pod_choice = input("> ").lower()
        if pod_choice == "yes" or pod_choice == "y":
            print("With a little bit of struggle, the pod creaks open")
            print("You step out but your legs falter, you start falling")
            print("As you are falling, you decide: \n\
                (a) grab onto the pod door \n\
                (b) grab a cord hanging from the ceiling \n\
                (c) risk injury from the fall")
            fall_choice = input("What do you do? [a/b/c] \n> ")
            return fall_choice
        elif pod_choice == "no" or pod_choice == "n":
            print("\nYou chose not to open the hibernation pod.")
            print("You fell asleep. \n")
            print("//////////////////////////////////////////\n")
            print("Let's try again.")
            print("Are you ready to open and leave the hibernation pod? [y/n]")
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")


fall_choice = open_hibernation_pod()

if fall_choice == "a":
    print("You managed to grab onto the pod door")
    print("You regained your balance and start exploring the room.")
    print("You see two paths, you can either go straight \
towards the ship deck, or to the right towards the infirmary.")
elif fall_choice == "b":
    print("You accidentally grabbed the electrical cord and got electrocuted.")
    print("You died.")
    print("The End.")
elif fall_choice == "c":
    print("You fell and cut your hand; you are bleeding.")
    print("You should find some bandages to cover the wound.")
    print("You start exploring the room.")
    print("You see two paths, you can either go straight towards the deck \
or to the right towards the infirmary.")
else:
    print("Invalid input, please choose [a/b/c]")