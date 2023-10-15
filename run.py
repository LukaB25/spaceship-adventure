import os
from datetime import datetime  # Import for date and time
import pytz                    # Import for timezones
import random                  # Import for randomness

# Date and time
# Gets and extracts current date and time for Dublin
# Took part of code from Free Code Camp for the timezone
dublin_timezone = pytz.timezone('Europe/Dublin')
dublin_date = datetime.now(dublin_timezone)
day = dublin_date.day
month = dublin_date.month
time = dublin_date.strftime("%H:%M:%S")
rand_number = random.randint(2, 100)
year = 3076
updated_end_year = year + rand_number

update_end_date = (f"{day}" + "/" + f"{month}" + "/" + f"{updated_end_year}"
                   + ", " + f"At time: {time}")

reboot_code = 29137
max_reboot_attempts = 3
cut_state = 0
nav_threat = 0
fall_decision = None
navigation_fault = False
bleeding = False
shadow_figure = False
space_suit = False
bypass_system = False


def clear():
    """
    Clears the terminal before continuing with the code.
    Code was taken and implemented from Dante Lee's video tutorial:
    https://www.youtube.com/watch?v=lI6S2-icPHE&t=57s
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def end_game():
    """
    Ends the game as part of user's choices to restart teh game or not.
    """
    print("Thank you for playing.")
    print("Good Luck on your future voyage.")
    print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
          "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
          "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")
    quit()


class HealthState:
    """
    Handles te effect of users choice to fall and deals damage until user
    either goes into the Medical Bay or reaches critical state.
    If there is no bleeding effect it clears the termial to make space
    for new prompts.
    """
    def __init__(self):
        self.health = 100
        self.bleeding = False

    def take_damage(self):
        if self.bleeding:
            damage_amount = 20
            self.health -= damage_amount
            if self.health <= 0:
                print(f"\nYou reached critical state. "
                      "You didn't reach Med Bay.")
                print(f"Health state: |{'_' * self.health}| 0% X___X")
                print("You died.\n")
                print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
                      "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
                      "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")
                self.bleeding = False
                restart_game_choice()
            else:
                print("\nYou are slowly bleeding out, "
                      "find some bandages quickly.")
                print(f"You are hurt, reach the Med Bay.\n")
                print(f"Health state: |{'█' * self.health}"
                      f"{'_' * (100 - self.health)}| "
                      f"{self.health}% *___*")


class NavigationFailure:
    """
    Handles the consequences to the users's actions and choices after they
    decide to explore the screens in the Control Room.
    The user will have certain amount of steps to reach the Airlock and to
    repair the ships navigation controls within 5 steps or they will meet
    their end.
    """
    def __init__(self):
        self.nav_threat = 0
        self.navigation_error = False

    def navigation_failure(self):
        if self.navigation_error:
            threat_amount = 20
            self.nav_threat += threat_amount
            if self.nav_threat <= 40:
                print("\nNavigation failure! Approaching a critical "
                      "level."
                      f"\nThreat Level: |{'█' * self.nav_threat}"
                      f"{'_' * (100 - self.nav_threat)}|  "
                      f"{self.nav_threat}%")
                print("Manual reboot necessary.\n")
            elif self.nav_threat <= 80:
                print("\nNavigation failure! Critical state "
                      "is imminent. "
                      f"\nThreat Level: |{'█' * self.nav_threat}"
                      f"{'_' * (100 - self.nav_threat)}|  "
                      f"{self.nav_threat}%")
                print("Manual reboot necessary.\n")
            else:
                self.handle_game_over()

    def handle_game_over(self):
        clear()
        print("\nNavigation failure! Critical state "
              f"reached. "
              f"\nThreat Level: |{'█' * self.nav_threat}"
              f"|  {self.nav_threat}%")
        print("The ship has entered an asteroid field.\n")
        print(".  ⭐ *     . 🪐  ･ﾟ’☆  *    .🌙      *  🌌  .  ☄*"
              "    *     *   ☄️.    *  ･ﾟ’☆  *    .\n")
        print("🌍*      .   ★,｡･:*:♪  .    *   💫 *    . ･ﾟ’☆  *   🌟   "
              ".     .  *.       ✨ *    .  *     \n")
        print("🌑  ･ﾟ’☆  .    *    ☄️     *    .  *     🌕  .    "
              "*    .  *  .      *   🛰 .  ’★,｡    *.   \n")
        print(".  ⭐ *  :*:･ﾟ   . 🪐      *    *     *   .   .🚀 * ."
              "    *     *  🌙  ★,｡･:*: *  🌌  .  ☄*\n")
        print("Collision in:\n")
        print("3")
        print("2")
        print("1")
        print("\nBANG\nBLAST\nBLOW\nBOOM")
        print("\nThe spaceship perished.")
        print("You died.")
        print("The End.")
        restart_game_choice()


player_health = HealthState()
navigation_fault = NavigationFailure()


def reset_initial_values():
    """
    Resets all of the values to the initial state to prepare for the complete
    restart of the game, so user can start from the beginning.
    """
    global fall_decision, navigation_fault
    global shadow_figure, space_suit, player_health
    fall_decision = None
    shadow_figure = False
    space_suit = False
    player_health = HealthState()
    navigation_fault = NavigationFailure()


def restart_game():
    """
    Restarts the game and starts from the beginning.
    Resets the values, clears the screen and runs the main() function.
    """
    reset_initial_values()
    clear()
    main()


def restart_game_choice():
    """
    Gives user a choice to either restart the game or to end the game.
    Restarts the game and starts from the beginning.
    """
    restart_choice = input("\nDo you want to restart the game from the"
                           " beginning? \n[y]yes \n[n]no \n> ").lower()
    if restart_choice == "y" or restart_choice == "yes":
        print("\nRestarting game...\n")
        restart_game()
    elif restart_choice == "n" or restart_choice == "no":
        print("\nEnding the game...")
        end_game()


def start_game_message():
    """
    Prints out the welcome message and some details to set the scene.
    Offers some insight in the game for the user.
    """
    print("                                               *★                \n"
          "          *★   ░░                     ░░                  ░░     \n"
          "   ███ ███ ███ ███ ███ ┼┼ ███ ██▄ █▄█ ███ █┼┼█ ███ █┼█ ███ ███   \n"
          "   █▄▄ █▄█ █▄█ █┼┼ █▄┼ ┼┼ █▄█ █┼█ ███ █▄┼ ██▄█ ┼█┼ █┼█ █▄┼ █▄┼   \n"
          "   ▄▄█ █┼┼ █┼█ ███ █▄▄ ┼┼ █┼█ ███ ┼█┼ █▄▄ █┼██ ┼█┼ ███ █┼█ █▄▄   \n"
          "          ░░           ░░   *☆*★                 ░░              \n"
          "                 ░░                   ░░                         \n"
          "      ░░                    ░░  ██        ░░                     \n"
          "  ░░       *                    ██        *✩‧₊˚       ░░░░       \n"
          "                 ░░             ██                               \n"
          "                              ▓▓▓▓▓▓                             \n"
          "    :*.°★*                  ▓▓▓▓▓▓▓▓▓▓           ₊˚*             \n"
          "          ▒▒          ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                         \n"
          "              ✩           ▓▓▒▒▓▓▓▓▒▒▓▓▓▓         ▒▒    *☆*       \n"
          "                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ░░                  \n"
          "    ▒▒       ░░  *★       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ✩‧₊           ░░      \n"
          "                          ░░░░▒▒░░░░░░░░                         \n"
          "   * ✩            ✩‧₊     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ░░             \n"
          "       ░░                 ▓▓▒▒▒▒▓▓▒▒▒▒▓▓   ▒▒                    \n"
          "                  ░░      ▓▓▒▒▒▒██▒▒▒▒▓▓            ░░           \n"
          "                        ████▓▓▓▓▓▓██▓▓▓▓██      ░░        ✩‧₊    \n"
          "         ▒▒   *☆      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                     \n"
          "                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                   \n"
          "             ░░     ▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ░░         \n"
          "   ░░               ▓▓▓▓▓▓░░████████████░░████              ░░   \n"
          "                    ▓▓    ▓▓░░░░░░▓▓░░░░    ▓▓   ░░              \n"
          "                   ░░  ▒▒               ▒▓░░ ▒▒      *☆*★        \n"
          "                  ▒▒▓░▓▓▒▒             ░░ ▓▓▒▒                   \n"
          "      *☆*★         ░░▓▒▒                ▒▒▓▒░░                   \n"
          "                    ▒ ▓░░               ░░▒▓▒                    \n"
          "                     ░░                   ░░                     \n"
          "            ▒▒                ▒▒    ▒▒          ▒▒    ▒▒        \n")
    # The rocket was taken from https://textart.sh/topic/rocket
    # The sign was created and taken from https://www.textartgenerator.net/
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


def fall_choice():
    while True:
        fall_decision = input("As you are falling, you decide to: \n"
                              "[a] grab onto the pod door \n"
                              "[b] grab a cord hanging from the ceiling \n"
                              "[c] risk injury from the fall \n> ").lower()

        if fall_decision == "end":
            restart_game_choice()

        if fall_decision == "a":
            print("\nYou managed to grab onto the pod door")
            print("You regained your balance and start exploring. You are "
                  "in the room containing hibernation pods.")

            choose_path(fall_decision)
        elif fall_decision == "b":
            print("\nYou accidentally grabbed the electrical cord "
                  "and got electrocuted.")
            print("You died.")
            print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
                  "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
                  "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")
            restart_game_choice()
        elif fall_decision == "c":
            print("\nYou fell and cut your hand; you are bleeding.")
            print("You should find some bandages to cover the wound.")

            player_health.bleeding = True
            player_health.take_damage()
            # Use the HealthStats instance

            print("You start exploring the room.\n")

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
        pod_choice = input("\nAre you ready to open and leave your "
                           "hibernation pod? \n[y]yes "
                           "\n[n]no\n> ").lower()
        if pod_choice == "end":
            restart_game_choice()
        if pod_choice == "yes" or pod_choice == "y":
            print("\nWith a little bit of struggle, the pod creaks open.")
            print("You step out but your legs falter, you start falling.\n")
            fall_choice()
        elif pod_choice == "no" or pod_choice == "n":
            print("\nYou chose not to open the hibernation pod.")
            print("You fell asleep. \n")
            print("(-, –)｡｡zZ💤💤💤\n")
            print("Let's try again.")
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{pod_choice}"\n')


def the_end_message():
    """
    Prints out the endgame message and some details to set the scene.
    Offers an open ending with a possibility of expanding the game or
    creating a sequel in the future.
    """
    print("\nAs you contemplate the vastness of space and your uncertain "
          "journey, you realize that every choice you made has "
          "consequences.\n")
    if navigation_fault.nav_threat > 0:
        print("The fate of the mission and its crew now rests in your hands.")
        print("You've overcome adversity, saved the mission from disaster, "
              "and made tough decisions. But the mysteries of space remain,"
              " and your story is far from over.\n")
        if bypass_system is True:
            print("The ship, now set on an unknown path, drifting through the "
                  "cosmos.")
    else:
        print("You think about how far you have already come and the great "
              "distance you traveled to get to here. And you can't help but"
              " smile at the thought of everything that awaits you on your "
              "new planet Terra Novus, with all of the fellow travellers.\n")
    print("The future is still uncertain, but one thing is clear: your "
          "journey has only just begun.")
    print("\nThank you for playing this adventure. The possibilities are "
          "endless, and the story can continue in many directions. Will you "
          "wander deeper into space, face more challenges, or perhaps return"
          " to your home planet? The choice is yours to make in the next "
          "chapter.\n")
    print("Stay tuned for future possible updates and sequels to this "
          "thrilling journey through the unknown.")
    print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
          "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
          "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")
    restart_game_choice()


def outer_space():
    """
    Handles the player's actions and choices when they leave the
    Airlock and 'step' into the vastness of space.
    After putting on the space suit in the Airlock the user can decide
    to exit the space ship and explore the outside of it.
    """
    global bypass_system
    player_health.take_damage()
    # Updates the health state

    print("As you step outside the Airlock, you are immediately struck"
          " by the breathtaking view of the cosmos. Countless stars "
          "twinkle in the distance, and you're surrounded by the void of"
          " space.")
    print("The silence is eerie, and you feel a strange mix of awe and"
          " vulnerability.")

    if navigation_fault.nav_threat > 0:
        print("After a few minutes of floating through the emptiness of"
              " space, you head to find the navigation panel. As you "
              "finally reach the designated area. The navigation reboot panel"
              " is in sight, and it's your only hope to set things right.")
        print("You follow the instructions step by step and reach the reboot "
              "panel. You open it and notice that the power source seems to "
              "be malfunctioning, which is likely the cause of the ship's "
              "navigation error.")

        while True:
            outer_space_choice = input("You have two options: \n[a]"
                                       "repair the power source "
                                       "\n[b]bypass it \n> ").lower()

            if outer_space_choice == "end":
                restart_game_choice()

            if outer_space_choice == "a" or outer_space_choice == "repair":
                reboot_attempt = 0
                while reboot_attempt < max_reboot_attempts:
                    print("Please enter in the reboot code to initialise the "
                          "repair port: ")
                    print(f"(Attempt: {reboot_attempt + 1})")
                    try:
                        reboot_code_input = int(input("\n> "))
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                    if reboot_code_input == reboot_code:
                        print("You are in, the reboot code was correct! "
                              "\nWell done!!")
                        print("You carefully start repairing the power source."
                              " After some time and with your steady hands, "
                              "you manage to fix it. The navigation system "
                              "comes back online, and the ship's trajectory "
                              "is corrected.")
                        print("Congratulations! You've successfully saved the "
                              "mission, and the ship is now back on track. "
                              "\nThe travellers will one day find out about "
                              "your heroics and appreciate everything you did "
                              "for them, complete strangers, on this faraway "
                              "voyage into unknown.")
                        the_end_message()
                    else:
                        print("Incorrect code. Please try again.")
                        reboot_attempt += 1
                else:
                    print("Maximum number of attempts reached. The navigation "
                          "malfunction remains unrepaired.")
                    if navigation_fault.nav_threat > 0:
                        navigation_fault.navigation_failure()
                        # Updates the navigation threat

            elif outer_space_choice == "b" or outer_space_choice == "bypass":
                print("You decide to bypass the malfunctioning power source as"
                      " it's too risky to repair it without proper tools. The "
                      "navigation system reboots, but you notice that the "
                      "course is set for an unknown destination.")
                print("You have a sinking feeling that your actions might have"
                      " dire consequences, but for now, you've successfully "
                      "fixed the immediate issue. The future of the mission "
                      "remains uncertain.")
                print("We are on an unknown path now, we will weave our own"
                      " destiny.")
                print("Maybe one day we will manage to get to our planet "
                      "Terra Novus, but for now we will drift through space,"
                      " until we find our way home.")
                bypass_system = True
                the_end_message()

            else:
                print("You're paralyzed by the weight of the decision. Time is"
                      " running out. The navigation system awaits your "
                      "choice.")
                print("Invalid input, your choices are [a]repair or [b]bypass")
                print('You can end the game by typing "end"')
                print(f'\nYou typed in "{outer_space_choice}"\n')
    else:
        the_end_message()


def airlock():
    """
    Handles the player's actions and choices when they arrive to the
    Airlock.
    The user can decide to put on the space suit and exit the spaceship.
    If the navigation system error is active, they will have a mission,
    otherwise they will meet their end.
    """
    player_health.take_damage()
    # Updates the health state

    if space_suit is True:
        print("You approach the Airlock hatch and secure your spacesuit.")
        print("The hatch opens smoothly, and you step into the airlock "
              "chamber.")
        print("You feel the rush of air leaving the chamber as it "
              "depressurizes.")
        print("Once the process is complete, the outer airlock door opens, "
              "revealing the vastness of space.")
        print("You're now ready to continue your journey into the unknown")

        if navigation_fault.nav_threat > 0:
            navigation_fault.navigation_failure()
            # Updates the navigation threat

        outer_space()

    else:
        print("You approach the Airlock hatch and begin to turn the "
              "wheel to open it. The hatch, however, seems much"
              " heavier than expected.\n")
        print("With a lot of effort, you manage to turn the wheel "
              "and start opening the hatch, but as you do, you feel"
              " the air pressure in the chamber drop rapidly. The "
              "alarm sirens begin to blare, and you realize your "
              "mistake.\n")
        print("The airlock chamber starts depressurizing rapidly,"
              " causing extreme discomfort as you struggle to "
              "breathe. Panic sets in as you realize you won't "
              "survive in the vacuum of space without a "
              "spacesuit.\n")
        print("Desperation takes over as you scramble to put on the "
              "nearby spacesuit, but it's too late. The airlock door "
              "to space opens, and you're sucked out into the cold, "
              "unforgiving void.\n")

        if shadow_figure is True:
            print("As you slowly freeze and your vision darkens, the"
                  "very last thing you see is a dark shadow looming "
                  "over you.")
            print("You can't make out any features, just a vague, "
                  "unsettling silhouette.")
            print("Fear and regret wash over you as you wonder who "
                  "or what this shadow is and why it's watching you"
                  " in your final moments. But it's too late, and your"
                  " consciousness fades into nothingness in the void "
                  "of space.")

        print("You died.")
        print("Your adventure ends here.")
        print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
              "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
              "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")
        restart_game_choice()


def engineering_bay():
    """
    Handles the player's actions and choices when they arrive to the
    Engineering Bay.
    The user can choose to explore the Engineering Bay or continue
    on their way to explore the rest of the ship.
    """
    player_health.take_damage()
    # Updates the health state

    def engineering_bay_path_choice():
        """
        Handles the player's actions and choices when they decide to leave the
        Engineering Bay.
        The user can choose stay insideof the engineering bay and continue to "
        "explore orleave towards the Airlock, and continue the story."
        """
        global space_suit

        player_health.take_damage()
        # Updates the health state

        print("As you head on out to leave you stop for a second.")

        while True:
            engineering_bay_path_options = input("Do you:\n[a]stay and explore"
                                                 " the Engineering Bay further"
                                                 "\n[b]leave to explore the "
                                                 "Airlock\n> ").lower()

            if engineering_bay_path_options == "end":
                restart_game_choice()

            if (engineering_bay_path_options == "a" or
                    engineering_bay_path_options == "stay"):
                print("\nYou are certain you didn't discover all of the secret"
                      " within the Engineering Bay, you decide to continue "
                      "exploring it.")

                if navigation_fault.nav_threat > 0:
                    navigation_fault.navigation_failure()
                    # Updates the navigation threat

                engineering_bay()

            elif (engineering_bay_path_options == "b" or
                    engineering_bay_path_options == "leave"):
                print("\nYou feel the time has come to continue exploring "
                      "further.")

                if navigation_fault.nav_threat > 0:
                    navigation_fault.navigation_failure()
                    # Updates the navigation threat

                if shadow_figure is True:
                    print("You are still curious why you haven't encountered "
                          "the shadowy figure from earlier. You are completly "
                          "confounded as to why the person wouldn't help you. "
                          "\nWere they the reason why you woke up? Why are "
                          "they still hiding? Who or what woke them up? How "
                          "long have they been awake for?")

                elif nav_threat > 0:
                    print("You still wonder what is the reason you woke up? "
                          "Was it all because of the navigational error? Was"
                          " I the only one who could have fixed the system "
                          "or was this just another error from the failing "
                          "system? Will I succeed at is?")

                else:
                    print("You still wonder what is the reason you woke up? "
                          "Who or what woke you up form your hibernation pod?"
                          "What is the whole purpose of this?")

                print("\nSo many questions running through your mind.")
                print("Once again you push your running thoughts from your "
                      "head, maybe you will encounter them, to ask them all"
                      " those questions, but for now you decide to continue"
                      " on your way.")
                print("You step in front of the sealed door that leads to the "
                      "Airlock, press your palm against the sensor lock")
                print("The sensor beeps, opening the door with a soft hiss of "
                      "compressed air. As you step through the threshold, you"
                      " find yourself in a small room with another door at the"
                      " far end, leading into the airlock. The room is "
                      "well-lit, and you notice a control panel to your right "
                      "with several buttons and switches, while the space "
                      "suits hang in rainbow of colours to your left.")
                print("\nYou also notice a odd smell in the air, a mixture of "
                      "metallic tang and sterile cleanliness. It's clear that "
                      "you're now in a different section of the facility. The "
                      "door behind hisses closed, sealing you in the room.")

                while True:
                    space_suit_choice = input("\nWould you like to put the "
                                              "space suit on?\n[y]yes \n[n]no"
                                              "\n> ").lower()

                    if space_suit_choice == "end":
                        restart_game_choice()
                    if space_suit_choice == "y" or space_suit_choice == "yes":
                        print("\nYou put on the space suit and get ready to "
                              "walk into the airlock.")
                        print("You look out the small window and check the "
                              "screen, making sure there is no malfunctions "
                              "in the Airlock system.")
                        print("All of the systems look good and there is no "
                              "visual malfunctions inside the Airlock.")
                        print("You use the screen to locate and check all of "
                              "the instructions for navigation reboot. You "
                              "memorize the detailed instructions on how to "
                              "get to the navigation reboot panel and proceed "
                              "to follow them  carefully.")
                        print("One sentence grabs your attention as you read "
                              "through, 'Reboot Code is generated by the "
                              "computer for each error, code should have been "
                              "written on the error report.'")
                        print("You remember seeing an error report earlier in "
                              "the ship's Control Bay. It contained the reboot"
                              " code needed to fix the navigation system.")
                        print("You scratch your head hoping you can remember "
                              "it by the time you reach the navigation panel.")
                        space_suit = True
                        airlock()

                    elif space_suit_choice == "n" or space_suit_choice == "no":
                        print("In your hurry to leave, you neglect the "
                              "spacesuit, thinking it might slow you down. ")
                        space_suit = False
                        airlock()
                    else:
                        print("Invalid input, your choices are [y]yes or "
                              "[n]no")
                        print('You can end the game by typing "end"')
                        print(f'\nYou typed in "{space_suit_choice}"\n')

        else:
            print("Invalid input, your choices are [y]yes or [n]no")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{engineering_bay_path_options}"\n')

    if shadow_figure is True:
        print("\nAs you step into the Engineering Bay, you think back "
              "to a shadowy figure running from the broken vase.")
        print("You wonder who they might be, and where are they directing "
              "you to, why don't they just aproach you, to help with this "
              "situation we find ourselves in.")
        print("The questions keep running through your head, but you can't"
              " stop now. You continue on.")
    else:
        print("You step into the Engineering Bay, excited to discover what "
              "glorious treasures you might find.")

    print("\nYou enter the room and find yourself surrounded by a magnificent "
          "array of computers, intricate crafting stations, precision "
          "constructors, and deconstructors, each humming with purpose.")
    print("\nYou can imagine all of the tinkering that could be done in here.")
    print("You always loved to build machines that could better the life as "
          "we know today.")
    print("Maybe that was the reason you were awoken.\n")

    while True:
        explore_engineering_bay = input("\nWould you like to explore the "
                                        "Engineering bay?\n[y]yes\n[n]no.\n> ")
        if explore_engineering_bay == "end":
            restart_game_choice()
        if explore_engineering_bay == "y" or explore_engineering_bay == "yes":
            print("\nYou start exploring and walking around. You are as exited"
                  " as a lettle kid in a chocolate factory.")

            while True:
                explore_choice = input("\nWhich machine would you like to "
                                       "explore?\n"
                                       "[a] Approach the crafting station.\n"
                                       "[b] Examine the constructors and "
                                       "deconstructors.\n"
                                       "[c] Investigate the mysterious old "
                                       "computer in the corner "
                                       "of the room.\n"
                                       "[d] Decide to stop exploring and "
                                       "continue on your way.\n\n> ")
                if explore_choice == "end":
                    restart_game_choice()

                if navigation_fault.nav_threat > 0:
                    navigation_fault.navigation_failure()
                    # Updates the navigation threat

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

                elif (explore_choice == "b" or explore_choice == "constructors"
                      or explore_choice == "deconstructors"):
                    print("\nYou find yourself irresistibly drawn to the "
                          "constructors and deconstructors.\nThese "
                          "sophisticated devices are marvels of engineering, "
                          "capable of creating and disassembling objects down "
                          "to their fundamental atomic components. ")
                    print("As you approach, you can't help but marvel at the "
                          "precision and complexity involved for such machines"
                          "to function.")
                    print("You are mesmerised with these machines that "
                          "represent a power that only few can understand.")
                    print("\nYou turn your attention to the constructor. As "
                          "you play around with it, you see the magic of "
                          "creation unfolding before your eyes.")
                    print("You select a blueprint and start the process. "
                          "You decided to start with a simple item, a mug.")
                    print("Slowly, the machine assembles the raw materials "
                          "from its storage and weaves them together, atom "
                          "by atom, into a tangible, functional object.")
                    print("It takes mere seconds for selected item to be "
                          "completed. Given the amazing feat you just "
                          "witnessed you have to test the possibilities "
                          "the deconstructor has to offer.")
                    print("You place your freshly constructed mug and place "
                          "it inside of the deconstructor. You press the "
                          "start button and it only takes a second or two "
                          "for the item to dissapear into nothingness.")
                    print("You are left at awe and you're thrilled by "
                          "the thought of all the possibilities these "
                          "machines hold both together and apart.")
                    print("You can't help but think of all of the ways "
                          "this ingenuity will help reshape your life on "
                          "Terra Novus, and smile.")
                    print("After hours spend tinkering with the machines"
                          " you decide to continue on exploring.")

                elif (explore_choice == "c" or explore_choice == "mystery"
                      or explore_choice == "computer"):
                    print("\nThe ancient computer sits silently in the corner,"
                          " a stark contrast of a simple machine next to the"
                          " gleaming technology that surrounds it.")
                    print("Its bulk form, which you would expect to covered in"
                          " a layer of dust and neglect, in a relic store, "
                          "somewhere on Earth, as it tells a story of a "
                          "completly different era.")
                    print("It's an enigma in this otherwise cutting-edge "
                          "environment, but you can't help but be intrigued "
                          "by its presence in this room.")
                    print("\nAs you come closer, you notice that the computer "
                          "hasn't been interacted with for a very long time.")
                    print("At the press of a single button the screen flickers"
                          " to life.")
                    print("The interface is ancient, a far cry from the "
                          "holographic displays and advanced AI systems you "
                          "have been interacting with your whole life.")
                    ancient_computer_message = "Updating systems...".upper()
                    print(ancient_computer_message)
                    print("The system update will finish on: "
                          f"{update_end_date}")
                    print(f"The update will take: {rand_number} years")
                    print("\nThat seems as a long time to wait for an "
                          "update, you continue to explore further.")
                elif (explore_choice == "d" or explore_choice == "stop"
                      or explore_choice == "continue"):
                    print("\nYou have decided to continue on with your "
                          "adventure.")
                    print("As you walk down the dimly lit corridor, you"
                          " can't help but wonder what else hides on this "
                          "spaceship in its mysterious depths.")
                    print("You continue your journey with a sense of "
                          "anticipation. What other secrets and surprises are"
                          " waiting for you on this interstellar expedition?")
                    engineering_bay_path_choice()
                else:
                    print("Invalid input, your choices are [a]crafting, "
                          "[b]constructors, [c]computer, [d]stop or continue")
                    print('You can end the game by typing "end"')
                    print(f'\nYou typed in "{explore_choice}"\n')

        elif explore_engineering_bay == "n" or explore_engineering_bay == "no":
            print("\nYou have decided to continue on with your "
                  "adventure.")
            print("As you walk down the dimly lit corridor, you"
                  " can't help but wonder what else hides on this "
                  "spaceship in its mysterious depths.")
            print("You continue your journey with a sense of "
                  "anticipation. What other secrets and surprises are"
                  " waiting for you on this interstellar expedition?")
            engineering_bay_path_choice()
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
    player_health.take_damage()
    # Updates the health state

    if navigation_fault.nav_threat > 0:
        navigation_fault.navigation_failure()
        # Updates the navigation threat

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
    player_health.take_damage()
    # Updates the health state

    print("Only few seconds pass before the elevator stops.\n")
    print("The doors swing open, and you find yourself in a state "
          "of awe.")
    print("As you look around, you notice a numerous escape pods, "
          "each with its own unique design, waiting to be explored.\n"
          "The soft, pulsating glow of their control panels and the "
          "promise of safety within them beckon you closer.")

    if navigation_fault is True:
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

    while True:
        escape_pod_option = input("Do you: \n[a]give into the feeling and "
                                  "escape \n[b] turn around and go back to"
                                  " try and save everyone?\n> ")

        if escape_pod_option == "end":
            restart_game_choice()

        if escape_pod_option == "a" or escape_pod_option == "escape":

            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
            if navigation_fault is True:
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
            if navigation_fault is True:
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
            restart_game_choice()
        elif escape_pod_option == "b" or escape_pod_option == "save":
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
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
    global shadow_figure

    player_health.take_damage()
    # Updates the health state

    print("\nAs you start to leave, a large Egyptian vase falls in "
          "the distance. \nYou jump, startled out of your mind, you "
          "run in the direction of the fallen vase.\n")
    print("You explore the rubble and realise that the vase couldn't"
          " have fallen on it's own. \nYou see a shadow running away "
          "from you.")
    print("You decide to follow, but soon find yourself at the cross "
          "section.")

    shadow_figure = True

    while True:
        cargo_hold_path_options = input("\nWhich way do you follow? \n[a] left"
                                        " into the suspiciously old and "
                                        "unmarked lift that takes you down a "
                                        "level\n[b] right into the Engineering"
                                        " Bay\n> ").lower()

        if cargo_hold_path_options == "end":
            restart_game_choice()

        if (cargo_hold_path_options == "a" or
                cargo_hold_path_options == "left"):
            print("\nYou step into the mysterious elevator, its metal doors "
                  "creak and slide shut as it whisks you away to a lower "
                  "level.\n")
            print("Riding the elevator, you realise you don't know where "
                  "you are going, you start to doubt whether it was a "
                  "smart idea just to jump in like that...\n")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
            escape_pods()
        elif (cargo_hold_path_options == "b" or
              cargo_hold_path_options == "right"):
            print("\nYou decide to follow to the Engineering Bay, hoping "
                  "your mind is not playing tricks on you, or worse "
                  "you have started loosing your mind and are becoming"
                  " delirious.")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
            print("You run as fast as your legs can carry you. But "
                  "can't seem to catch up.")
            engineering_bay()
        else:
            print("Invalid input, your choices are [a]left or [b]right")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{cargo_hold_path_options}"\n')


def cargo_hold():
    """
    Handles the player's actions and choices when they reach the Cargo Hold.
    After a user reaches Control Room they can choose to explore the Cargo
    Hold, or continue on exploring the ship.
    """
    player_health.take_damage()
    # Updates the health state

    print("\nAs you continue your exploration, you eventually reach "
          "the massive Cargo Hold.\n")
    print("The Cargo Hold is filled with an array of cargo: stacked "
          "boxes, vital supplies, sturdy containers, various vehicles, "
          "reserves of fuel, an assortment of spare parts, live animal "
          "specimens in their own special cryo-hibernation chambers and more.")

    while True:
        cargo_hold_options = input("\nWhich part of the Cargo Hold "
                                   "would you like to explore?\n"
                                   "[a] boxes and supplies\n"
                                   "[b] vehicles\n"
                                   "[c] specimens\n"
                                   "[d] continue on/ don't explore"
                                   "\n> ").lower()

        if cargo_hold_options == "end":
            restart_game_choice()

        if cargo_hold_options == "a" or cargo_hold_options == "boxes":
            print("\nYou start reading the signs on all of the boxes "
                  "and containers")
            print("You have been searching through boxes for hours...")
            print("You have discovered various Ancient Relics, Rare Minerals, "
                  "advanced holo communicators...")
            print("After after a while you reached a "
                  "heavily armoured cage containing various advanced "
                  "weaponry and ammunition, mining and building "
                  "tools, it is locked.")
            print("You decide to stop exploring the supply boxes "
                  "and containers and continue on...")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat

        elif (cargo_hold_options == "b" or
                cargo_hold_options == "vehicles"):
            print("\nYou continue walking among all of the advanced "
                  "and antique vehicles and machinery.")
            print("You are awed by the vast array before your sight.")
            print("\nThere are numerous hover crafts, flying saucers, "
                  "antique cars, excavators, diggers, but also "
                  "the all mighty Structure Synthesizers and "
                  "Instant Fabricators.")
            print("You remember the first time you saw Structure "
                  "Synthesizer at work. It managed to construct "
                  "the whole ten story building in a matter of "
                  "seconds.\n")
            print("After hours of exploring you decide to stop "
                  "exploring the vehicles that The Collective "
                  "Government supplied us with and continue on...")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat

        elif (cargo_hold_options == "c" or
                cargo_hold_options == "specimens"):
            print("\nYou choose to examine the collection of live "
                  "animal specimens that were sent with us on this "
                  "journey to Terra Novus.")
            print("You find yourself at a loss for words, completely "
                  "captivated by the magnificent sight.\n")
            print("All the specimens lay within specialized cryo-hibernation "
                  "chambers, in a peaceful slumber awaiting our arrival to "
                  "the new world, our new home.")
            print("We were equipped with an extensive array of livestock, "
                  "mammals, a variety of avian species, as well as insects "
                  "and critters, and new variety of spicies that scientist "
                  "managed to create just for this expedition all intended "
                  "to populate our new world.")
            print("You could continue exploring the animal specimens for "
                  "days, but you know it is time to continue on...")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat

        elif (cargo_hold_options == "d" or
                cargo_hold_options == "continue"):
            print("\nYou made a decision to continue exploring the ship.")
            print("Who knows what you might find next...")
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
            cargo_hold_path_choice()

        else:
            print("Invalid input, your choices are [a]boxes, [b]vehicles, "
                  "[c]specimens or [d]continue")
            print('You can end the game by typing "end"')
            print(f'\nYou typed in "{cargo_hold_options}"\n')


def control_room_choose_path():
    """
    Handles the player's actions and choices which
    way they would like to go from the Control Room.
    User is located in the Control Room and needs
    to choose which way they would like to continue going.
    """
    print("You find yourself at the cross section.")

    while True:
        control_path_choice = input("\nYour options are: \n[a]Go left "
                                    "into the Cargo Hold \n[b]Go right "
                                    "into the Engineering Bay"
                                    "\n> ").lower()
        if control_path_choice == "end":
            restart_game_choice()

        if control_path_choice == "a" or control_path_choice == "left":
            player_health.take_damage()
            # Updates the health state
            print("\nYou head left towards the Cargo Hold.")

            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat

            cargo_hold()

        elif control_path_choice == "b" or control_path_choice == "right":
            player_health.take_damage()
            # Updates the health state

            print("\nYou head right towards the Engineering Bay. Wondering"
                  " what might you find there.")

            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat

            engineering_bay()

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
    player_health.take_damage()
    # Updates the health state

    print("\nYou reach the Control Room.")
    print("You are fascinated by all of the screens "
          "and blinking lights in this room.")

    while True:
        control_room_options = input("Do you \n[a]explore the screens "
                                     "\n[b]continue on"
                                     "\n> ").lower()

        if control_room_options == "end":
            restart_game_choice()

        if control_room_options == "explore" or control_room_options == "a":
            print("\nYou look at all of the screens. You reach one "
                  "that is blinking with multiple error messages.")
            print("You start reading the messages, but one catches "
                  "your eye.\n")
            print(("Imminent threat!!! Navigation failure! Manual "
                  "reboot necessary to recalibrate system.\n").upper())
            print("...you must find the airlock, leave the spaceship and "
                  "manually reboot the system from the outside.")
            reboot_message = f"\nSystem reboot code: {reboot_code}".upper()
            print(reboot_message + "\nMemorise this code. It is important!")
            navigation_fault.navigation_error = True
            navigation_fault.navigation_failure()
            # Updates the navigation threat
            break

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

    print("\nScanning the wound...\n")
    print("Decontamination...\n")
    print("Tissue Regeneration...\n")
    print("Cellular Rejuvenation...\n")
    print("Healing complete\n".upper())
    print("Specimen returned to optimum health.\n")
    player_health.bleeding = False
    # Set bleeding back to False
    # Stops any damage effect active


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
    restart_game_choice()


def med_bay_choose_path():
    """
    Handles the player's actions and choices when in the Med Bay.
    The user can choose to continue exploring the spaceship and continue
    moving through the rest of the rooms left to explore.
    """
    global shadow_figure
    player_health.take_damage()
    # Updates the health state

    print("You walk through the Med Bay exploring.")
    print("You pass around the Regenesis Chamber 3000 and "
          "reach two corridors.\n")

    while True:
        print("To your left you can see the long winding corridor "
              "that will take you to the Observation Deck[a]")
        print("To your right you have a straight path into the Library[b]\n")

        med_bay_path_choice = input("What would you like to explore? "
                                    "\n[a]left \n[b]right \n> ").lower()

        if med_bay_path_choice == "end":
            restart_game_choice()

        if bleeding is False:
            clear()

        if med_bay_path_choice == "a" or med_bay_path_choice == "left":
            print("\nYou take the long winding corridor towards the "
                  "Observation Deck.")
            print("You turn the corner and find yourself rendered speechless"
                  " by the most breathtaking sight you ever witnessed.\n")
            print("The room is an enormous, circular cascading staircase, "
                  "offering a panoramic view of a brilliant tapestry of stars"
                  " and planets gracing throught the glass wall.\n")
            print("⨯ . ⁺ ✦ ⊹ ꙳ ⁺ * ꙳ ✦ ✦ ⊹ . * ꙳ ✦ ⊹ ⨯ .  ☁︎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒ ⁺ ✦ "
                  "⊹ ꙳ ⁺ ‧ ⨯. ⁺ ✦ ⊹ . * ꙳ ✦ ⊹⊹ ꙳ ⁺ ‧ ⨯")
            print("☆࿐ཽ༵༆༒ ☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・"
                  "☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆°☆ ༒༆࿐ཽ༵☆")
            print("🪐　* .🌒  ⛧ .　 ˚　. ⭑ ⛧ . ＊ 🌍   ⭑ ⁎ ⭑ ⛧ .🌒　˚　　 . ✦ ⛧ ꙳ ⭒ "
                  "　˚　　. 🪐  ⛧ ＊ ⛧ ꙳ ☪︎　˚　.🌍 . ✦")
            print("⋆ 。゜⁎ ⭑ ⛧ ꙳ ⭒ ☁︎ 。⋆ 。゜☾゜。⋆⋆ ⋆⁺₊⋆  ☪︎ ⭒ ꙳ ⛧ ＊ ⭑ ⁎ ☀︎ ⋆⁺₊⋆"
                  " ⋆⋆ 。゜☁︎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒  。⋆ 。゜☾")
            print("゜。⋆ ꙳ 🌍 ⛧ .　 ˚　. ✦　˚　⭑ ⛧ . ＊ ⭑ ⁎ ⭑ ⛧ ꙳ ⭒ 　˚　　.🪐　* ."
                  " 　˚˚　　. 　˚　　.　*　. ⭑ ⛧ ✦")
            print("☪︎ ⭒ ꙳ ⛧ ＊ ⭑ ⁎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒ ꙳ ⛧ ＊ ⭑ ⁎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒ ꙳ ⛧ ＊ "
                  "⭑ ⁎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒ ꙳ ⛧ ＊ ⛧ ꙳ ☪︎ ⭒ ꙳ ⛧ ＊")
            print("˚ 　. ✦˚　 .　 ˚　. ✦　　˚　.🌒　˚　　 . ✦ 　.   　˚　 　*　🌍　 "
                  "　✦　　.　 .　　  . 　˚　  . ")
            print("⨯ . ⁺ ✦ ⊹ ꙳ ⁺ * ꙳ ✦ ✦ ⊹ . * ꙳ ✦ ⊹ ⨯ .  ☁︎ ⭑ ⛧ ꙳ ⭒ ☪︎ ⭒ ⁺ ✦ "
                  "⊹ ꙳ ⁺ ‧ ⨯. ⁺ ✦ ⊹ . * ꙳ ✦ ⊹⊹ ꙳ ⁺ ‧ ⨯")
            # Symbols and stars taken from https://text-art.top/

            print("You sit down, taking in the view, feeling humbled and small"
                  " in the vastness of the universe that surrounds you.")
            print("You feel at home. As if you were meant to be there.\n")
            print("Time stretches on, but you decide it is time to continue "
                  "your exploration. \nYou silently promise yourself to return"
                  " to this place.")
            observation_deck_option = input("\nWould you like to: \n[a]"
                                            "continue on into the Engineering"
                                            " Bay  \n[b]go back into the Med "
                                            "Bay?\n> ")

            if observation_deck_option == "end":
                restart_game_choice()

            if (observation_deck_option == "a" or
                    observation_deck_option == "Engineering Bay"):
                print("\nYou go down the long halway heading into Engineering "
                      "Bay still thinking about the beautiful sight you have"
                      " just experienced.")
                engineering_bay()
            elif (observation_deck_option == "b" or
                  observation_deck_option == "Med Bay"):
                print("\nYou turn around to explore the Medical Bay further.")
                med_bay_choose_path()

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

            shadow_figure = True

            shout = ("Hello, is there anybody here??").upper()
            print(f"You shout: {shout}. \n But nobody answers. "
                  "\nYou are left intrigued. \nWho left that book?!\n")
            print("You explore the room further, but you don't find the owner "
                  "of the open book...")
            print("You spent some time looking and reading through some books."
                  "\nAs the time starts dragging on you decide it is time to "
                  "continue with your exploration of the ship.")
            print("You turn around to go back into the Medical Bay and see a "
                  "mystery shadowy figure looking at you, you start running "
                  "after them, but they disappeare.")
            print("You find yourself at the same cross section.")

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
    player_health.take_damage()
    # Updates the health state

    print("You enter the Med Bay. Straight away you notice "
          "all of the medical supplies. You are mesmerised "
          "by the size of it, you couldn\'t even imagine "
          "something like that would fit onto the ship.\n")

    print("Amongst the sea of medical supplies, you notice a "
          "machine in the middle of the room. You approach it.")
    print("\nRegenesis Chamber 3000. It still sounds so majestic.\n")
    print("You remember all of the advertising the collective "
          "government made, trying to sell them for at "
          "home use back in the day.\n")
    while True:
        healing_chamber = input("Would you like to test your health? "
                                "\n[y]yes \n[n]no \n> ").lower()

        if healing_chamber == "end":
            restart_game_choice()

        if healing_chamber == "y" or healing_chamber == "yes":
            print("\nScanning...\n")
            print("Scan complete!")
            if player_health.bleeding:
                print("Anomaly detected.")
                print("Wound detected on the left forearm.")
                heal_wound = input("\nWould you like to heal the wound? "
                                   "\n[y]yes \n[n]no \n> ").lower()

                if heal_wound == "y" or heal_wound == "yes":
                    healing_procedure()

                elif heal_wound == "n" or heal_wound == "no":
                    forceful_healing_procedure()

                if healing_chamber == "end":
                    restart_game_choice()

            else:
                print("No anomalies detected.")
                print("\nYou are a healthy specimen.\n")
            print("Thank you for using Regenesis Chamber 3000\n")
            med_bay_choose_path()

        elif healing_chamber == "n" or healing_chamber == "no":
            player_health.take_damage()
            # Updates the health state
            med_bay_choose_path()

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

    print("You see two paths, you can either go "
          "straight towards the Control Room[a] "
          "or to the right towards the Med Bay.[b]\n")

    while True:
        path_choice = input("Which path would you like to "
                            "take? \n[a]straight \n[b]right \n> ").lower()

        if path_choice == "end":
            restart_game_choice()

        if (path_choice == "a" or path_choice == "straight"
                and fall_decision == "a"):
            print("You head straight towards the Control Room.")
            print("Eager to continue exploring.\n")
            control_room()

        elif (path_choice == "a" or path_choice == "straight"
              and fall_decision == "c"):
            clear()
            print("You head straight towards the Control Room.\n")
            control_room()

        elif (path_choice == "b" or path_choice == "right"
              and fall_decision == "a"):
            clear()
            print("You head right towards the Med Bay.")
            print("Eager to continue exploring.")
            med_bay()

        elif (path_choice == "b" or path_choice == "right"
              and fall_decision == "c"):
            clear()
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
