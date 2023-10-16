import os                      # Import to enable terminal clear
import gspread                 # Import gspread for google sheets
from google.oauth2.service_account import Credentials    # access
from datetime import datetime  # Import for date and time
import pytz                    # Import for timezones
import random                  # Import for randomness


# Sets up Google Sheets API authentication, connect and access the
# 'spaceship_adventure' spreadsheet, and retrieve data from 'victims'
# and 'survivors' worksheets.
# Used Code Institute lesson to create the gspread
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('spaceship_adventure')

victims = SHEET.worksheet('victims')
survivors = SHEET.worksheet('survivors')

victims_data = victims.get_all_values()
survivors_data = survivors.get_all_values()

# Initial setup and values to start the game:
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

# Initial variables and values
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

ending_reasons = ["Electrical cord", "Bleed out", "Spaceship collision"
                  " with asteroid", "Forced healing", "Elevator "
                  "malfunction", "Frozen in space"]

surviving_ending_reasons = ["Escape pod - saved themselves",
                            "Saved everyone - master reboot",
                            "Saved everyone - system bypass"]


def update_victims_list(username, possible_ending):
    """
    Updates the victims google worksheet, adds a new username and
    updates the reason of death from possible_ending.
    """
    # Create a new row starting with the username and input "X" if the
    # user's game ending reason matches any of the ending reasons.
    new_row = [username]
    for reason in ending_reasons:
        if possible_ending == reason:
            new_row.append("X")
        else:
            new_row.append("")

    # Get the number of rows in the victims_data (excluding the header row)
    num_rows = len(victims_data)

    # Insert a new row at the end (remember that row numbering starts from 1)
    victims.insert_rows([new_row], row=num_rows + 1, value_input_option='RAW')


def update_survivors_list(username, possible_ending):
    """
    Updates the victims google worksheet, adds new username and
    updates the reason of death from possible_ending().
    """
    # Create a new row starting with the username and input "X" if the
    # user's game ending reason matches any of the surviving reasons.
    new_row = [username]
    for reason in surviving_ending_reasons:
        if possible_ending == reason:
            new_row.append("X")
        else:
            new_row.append("")

    # Get the number of rows in the survivors_data (excluding the header row)
    num_rows = len(survivors_data)

    # Insert a new row at the end (remember that row numbering starts from 1)
    survivors.insert_rows([new_row], row=num_rows + 1,
                          value_input_option='RAW')


def progress_tracker():
    """
    Extracts progress data from 'victims_data' and 'survivors_data' variables
    and organizes it into a dictionary containing information about the
    username and the game ending reasons.
    """
    # Create an empty dictionary to store the progress_values
    progress_values = {"victims": [], "survivors": []}

    # Runs through the victims_data rows, and extracts last 5 entries
    for row in victims_data[-5:]:
        username = row[0]  # Sets first row as username/header
        user_progress = []

        # runs through ending_reasons and check for "X"
        for i, reason in enumerate(ending_reasons):
            if row[i + 1] == "X":
                user_progress.append(reason)

        progress_values["victims"].append({"username": username, "ending":
                                           user_progress})

    # Runs through survivors_data rows and extracts last 5 entries
    for row in survivors_data[-5:]:
        username = row[0]  # # Sets first row as username/header
        user_progress = []

        # Runs through your survivor reasons and check for "X"
        # Updates the surviving_ending_reasons list
        for i, reason in enumerate(surviving_ending_reasons):
            if row[i + 1] == "X":
                user_progress.append(reason)

        progress_values["survivors"].append({"username": username, "ending":
                                             user_progress})

    return progress_values


def show_progress_score():
    """
    Retrieves and displays the progress report of game endings for 'victims'
    and 'survivors'.
    """
    # Clears the terminal and displays current score progress
    # Displayed scores show who were the victims and survivors of the game
    # i.e. users that managed to finish the game by death or survival
    clear()
    print("██ ██ ███ ███ ██ ██▄ ███ ███ ███ ██▄\n"
          "█▄ █╬ █╬█ █▄╬ █▄ █▄█ █╬█ █▄█ █▄╬ █╬█\n"
          "▄█ ██ █▄█ █╬█ █▄ █▄█ █▄█ █╬█ █╬█ ███")
    progress_values = progress_tracker()
    for worksheet, users in progress_values.items():
        print(f"\n\nProgress report: {worksheet}\n")
        for user in users:
            print(f"Username: {user['username']} \nEnding met by: "
                  f"{', '.join(user['ending'])}\n")


def clear():
    """
    Clears the terminal before continuing with the code.
    Code was taken and implemented from Dante Lee's video tutorial:
    https://www.youtube.com/watch?v=lI6S2-icPHE&t=57s
    """
    # Clear the terminal screen. Use 'cls' for Windows ('nt') and
    # 'clear' for other operating systems.

    os.system('cls' if os.name == 'nt' else 'clear')


def end_game():
    """
    Ends the game as part of user's choices to restart teh game or not.
    """
    print("Thank you for playing.")
    print("Good Luck on your future voyage.")
    quit()


def request_username():
    """
    Get the player's username as input to use later on in the game to
    save the game outcome. Whether the user has survived or not.
    """
    while True:
        # Removes leading and trailing whitespace
        username = input("\nPlease enter your username: \n> ").strip()

        # Runs restart_game_choice if user types in end which offers them to
        # start from the beginning or to end the program
        if username == "end":
            restart_game_choice()

        # Returns username only if input is not empty
        # Prevents using only whitespace
        elif (username and not username.isspace() and not
                username.isnumeric()):
            return username

        # Prevents entry of numeric values
        elif username.isnumeric():
            print("\nUsername cannot consist of only numbers. Please "
                  "try again.")

        # Handles incorrect input
        else:
            print("\nUsername cannot be empty or consist of only whitespace."
                  "Please try again.")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')


class HealthState:
    """
    Handles te effect of users choice to fall and deals damage until user
    either goes into the Medical Bay or reaches critical state.
    If there is no bleeding effect it clears the termial to make space
    for new prompts.
    """
    def __init__(self):
        """
        Initialize the player's health state with 50 health
        and no bleeding effect.
        """
        self.health = 50
        self.bleeding = False

    def set_bleeding_state(self, bleeding):
        """
        Sets player's bleeding status.
        """
        self.bleeding = bleeding

    def take_damage(self):
        """
        Inflict damage on the player if they are bleeding.
        If the player's health reaches zero, the player dies.
        """
        if self.bleeding:
            damage_amount = 10
            self.health -= damage_amount
            if self.health <= 0:
                # Player reached critical state and didn't reach the
                # Med Bay.
                print(f"\nYou reached critical state. "
                      "You didn't reach Med Bay.")
                print(f"Health state: |{'_' * 50}| 0% X___X")
                print("You died.\n")
                print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
                      "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
                      "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

                # Set game outcome variables
                survived = False
                possible_ending = "Bleed out"
                game_outcome_tracker.set_possible_ending(possible_ending)
                game_outcome_tracker.set_survival_status(survived)
                # Updates the victims google sheet by adding the username
                # and the ending type
                update_victims_list(game_outcome_tracker.username,
                                    possible_ending)
                # Offers user an option to restart the game
                restart_game_choice()
            else:
                # Player is slowly bleeding out.
                # To heal they need to reach Med Bay
                print("\nYou are slowly bleeding out, "
                      "find some bandages quickly.")
                print(f"You are hurt, reach the Med Bay.\n")
                print(f"Health state: |{'█' * self.health}"
                      f"{'_' * (50 - self.health)}| "
                      f"{self.health * 2}% *___*")


class NavigationFailure:
    """
    Handles the consequences to the users's actions and choices after they
    decide to explore the screens in the Control Room.
    The user will have certain amount of steps to reach the Airlock and to
    repair the ships navigation controls within 5 steps or they will meet
    their end.
    """
    def __init__(self):
        """
        Initialize the navigation failure state without the threat and
        navigation error.
        """
        self.nav_threat = 0
        self.navigation_error = False

    def navigation_failure(self):
        """
        Handle navigation failure and its consequences.
        If navigation error is True and active, the threat level increases.
        Depending on the threat level, different messages are displayed.
        If the threat level becomes critical, the game over handling is called.
        """
        if self.navigation_error:
            threat_amount = 10
            self.nav_threat += threat_amount
            if self.nav_threat <= 20:
                print("\nNavigation failure! Approaching a critical "
                      "level."
                      f"\nThreat Level: |{'█' * self.nav_threat}"
                      f"{'_' * (50 - self.nav_threat)}|  "
                      f"{self.nav_threat * 2}%")
                print("Manual reboot necessary.\n")
            elif self.nav_threat <= 40:
                print("\nNavigation failure! Critical state "
                      "is imminent. "
                      f"\nThreat Level: |{'█' * self.nav_threat}"
                      f"{'_' * (50 - self.nav_threat)}|  "
                      f"{self.nav_threat * 2}%")
                print("Manual reboot necessary.\n")
            else:
                self.handle_game_over()

    def handle_game_over(self):
        """
        Game over scenario when navigation failure reaches a critical state.
        This method clears the screen, displays game over messages, and sets
        the necessary game outcome details.
        """
        clear()  # Clear the screen for a fresh display of the ending
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
        print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
              "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
              "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

        # Set game outcome variables
        survived = False
        possible_ending = "Spaceship collision with asteroid"
        game_outcome_tracker.set_possible_ending(possible_ending)
        game_outcome_tracker.set_survival_status(survived)
        # Updates the victims google sheet by adding the username
        # and the ending type
        update_victims_list(game_outcome_tracker.username,
                            possible_ending)
        # Offers user an option to restart the game
        restart_game_choice()


class GameOutcomeTracker:
    """
    Tracks the outcome and status of the game for a specific player.
    """
    def __init__(self):
        """
        Initializes a GameOutcomeTracker instance.
        """
        # Player's username
        self.username = None
        # Player's survival status (True if survived, False if not)
        self.survived = None
        # The reason for the game ending
        self.possible_ending = None

    def set_username(self, username):
        """
        Set the player's username.
        """
        self.username = username

    def set_survival_status(self, survived):
        """
        Set the player's survival status.
        """
        self.survived = survived

    def set_possible_ending(self, possible_ending):
        """
        Set the reason for the game ending.
        """
        self.possible_ending = possible_ending

    def get_ending_status(self):
        """
        Get the player's ending status.
        Returns "Survived" if the player survived, "Died" if not,
        or "Unknown" if not set.
        """
        if self.survived is not None:
            return "Survived" if self.survived else "Died"
        return "Unknown"

    def get_possible_ending(self):
        """
        Get the reason for the game ending.
        """
        return self.possible_ending

    def __str__(self):
        """
        Return a string representation of the GameOutcomeTracker.
        """
        return (f"Username: {self.username}, Ending Status: "
                f"{self.get_ending_status}, Ending reason:"
                f"{self.get_possible_ending}")


# Create a HealthState instance for the player's health
player_health = HealthState()
# Create a NavigationFailure instance for navigation issues
navigation_fault = NavigationFailure()
# Create a GameOutcomeTracker instance for tracking game outcomes
game_outcome_tracker = GameOutcomeTracker()


def reset_initial_values():
    """
    Resets all of the values to the initial state to prepare for the complete
    restart of the game, so user can start from the beginning.
    """
    # Reset all values to initial state
    global fall_decision, navigation_fault, game_outcome_tracker
    global shadow_figure, space_suit, player_health
    fall_decision = None
    shadow_figure = False
    space_suit = False
    player_health = HealthState()
    navigation_fault = NavigationFailure()
    game_outcome_tracker = GameOutcomeTracker()

    # Re-fetch the worksheet data
    global victims_data, survivors_data
    victims_data = victims.get_all_values()
    survivors_data = survivors.get_all_values()


def restart_game():
    """
    Restarts the game and starts from the beginning.
    Resets the game values to initial state, clears the screen to provide
    clean view and runs the main() function to start the game again.
    """
    reset_initial_values()
    clear()
    main()


def restart_game_choice():
    """
    Gives user a choice to either restart the game or to end the game.
    If user decides to restart it resets values to initial state and
    starts from the beginning.
    If user decides to end the game, the game will print the end game
    message and quit the program.
    """
    restart_choice = input("\nDo you want to restart the game from the"
                           " beginning? \n[y]yes \n[n]no \n[]type "
                           "anything to cancel\n> ").lower()

    # Restarts the game if player selects yes/y
    if restart_choice == "y" or restart_choice == "yes":
        print("\nRestarting game...\n")
        restart_game()

    #  Ends game completely if player selects no/n
    elif restart_choice == "n" or restart_choice == "no":
        print("\nEnding the game...")
        end_game()


def start_game_message():
    """
    Displays an ASCII art rocket and Space Adventure sign.
    Prints out the welcome message and some details to set the scene.
    Requests the player's username and sets it in GameOutcomeTracker class.
    Provides an overview of the game's features and how to check scores or
    end the game.
    Offers some insight in the game for the user by setting up the backstory
    and the player's role in the game.
    """
    # Print ASCII art (rocket and sign) to give some graphics to the game.
    print("                                                *★                "
          "\n"
          "            *★   ░░                     ░░                  ░░     "
          "\n"
          "██ ███ ███ ██ ██ ██ █╬█ █ ███ ╬╬ ███ ██▄ █▄█ ██ █╬╬█ ███ █╬█ ███ ██"
          "\n"
          "█▄ █▄█ █▄█ █╬ █▄ █▄ █▄█ █ █▄█ ╬╬ █▄█ █╬█ ███ █▄ ██▄█ ╬█╬ █╬█ █▄╬ █▄"
          "\n"
          "▄█ █╬╬ █╬█ ██ █▄ ▄█ █╬█ █ █╬╬ ╬╬ █╬█ ███ ╬█╬ █▄ █╬██ ╬█╬ ███ █╬█ █▄"
          "\n"
          "            ░░           ░░   *☆*★                 ░░              "
          "\n"
          "                   ░░                   ░░                         "
          "\n"
          "        ░░                    ░░  ██        ░░                     "
          "\n"
          "  ░░         *                    ██        *✩‧₊˚       ░░░░       "
          "\n"
          "                   ░░             ██                               "
          "\n"
          "                                ▓▓▓▓▓▓                             "
          "\n"
          "    :*.  °★*                  ▓▓▓▓▓▓▓▓▓▓           ₊˚*             "
          "\n"
          "     ✩      ▒▒          ░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                         "
          "\n"
          " ✩              ✩           ▓▓▒▒▓▓▓▓▒▒▓▓▓▓         ▒▒    *☆*       "
          "\n"
          "           :*               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ░░                  "
          "\n"
          "    ▒▒       ░░             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ✩‧₊      :*     ░░    "
          "\n"
          " :*                         ░░░░▒▒░░░░░░░░                         "
          "\n"
          "   * ✩     ▒▒       ✩‧₊     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ░░             "
          "\n"
          "         ░░                 ▓▓▒▒▒▒▓▓▒▒▒▒▓▓   ▒▒                    "
          "\n"
          "     ▒▒             ░░      ▓▓▒▒▒▒██▒▒▒▒▓▓            ░░           "
          "\n"
          "            ✩‧₊           ████▓▓▓▓▓▓██▓▓▓▓██      ░░        ✩‧₊    "
          "\n"
          "         ▒▒     *☆       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█           ✩‧₊        "
          "\n"
          "  ✩‧₊                   ▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█    ✩‧₊         ▒▒   "
          "\n"
          "           ✩‧₊         ▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         ₊˚*        "
          "\n"
          "  ▒▒     *☆     ▒▒    ██▓▓▒▒▒▒██▓▓▓▓██▓▓▒▒▒▒▓▓██                   "
          "\n"
          "                 ₊˚*  ▓██▓▒▒▒▒▓██▓▓▓▓██▓▒▒▒▒▓▓██      ▒▒   *☆      "
          "\n"
          "           ✩‧₊        ▓▓██▓▓▓▓▓▒▒▒▒▒▒▒▒█▓▓▓▓▓▓██                   "
          "\n"
          "                      ▓▓▓██▓▓▓▓▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓                   "
          "\n"
          "               ░░     ▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ░░         "
          "\n"
          "   ░░     ✩‧₊         ▓▓▓▓▓▓░░████████████░░████              ░░   "
          "\n"
          "                      ▓▓    ▓▓░░░░░░▓▓░░░░    ▓▓   ░░              "
          "\n"
          "  ✩‧₊                ░░  ▒▒               ▒▓░░ ▒▒      *☆*★        "
          "\n"
          "                    ▒▒▓░▓▓▒▒             ░░ ▓▓▒▒                   "
          "\n"
          "      *☆*★           ░░▓▒▒                ▒▒▓▒░░                   "
          "\n"
          "            ✩‧₊.      ▒ ▓░░               ░░▒▓▒                    "
          "\n"
          "                       ░░                   ░░                     "
          "\n"
          "               ▒▒                ▒▒    ▒▒          ▒▒    ▒▒        "
          "\n")
    # The rocket was taken from https://textart.sh/topic/rocket
    # The sign was created and taken from https://www.textartgenerator.net/

    # Welcome message and ask player for their username.
    print("\nWelcome to your spaceship adventure!\n")
    username = request_username()
    game_outcome_tracker.set_username(username)

    # Provide information on game features and controls.
    print('\nIn case you want to check out the scoreboards, you can do so by '
          'typing "progress" or "scores" at any point through the game. \n'
          'Once you reach one of possible nine endings to the story your '
          'progress will be automatically saved.')
    print('If for any reason you decide to end the game, you can do so by '
          'writing "end" into any input field at any stage of the game.\n')

    # Introduce the game's storyline and context.
    print("It is a year 3076. You are an interplanetary traveler, "
          "at least that is what they said you will be. \n")
    print("Due to an overpopulation on our home planet Earth"
          "The Collective Government devised a plan to send three million "
          "people to the newly discovered habitable planet 'Terra Novus'.")
    print("You have left your planet for a long trip "
          "through the vast space in search of a better life.\n")
    # Continue with the game's narrative...
    print("You are suddenly awoken. You woke up before all other travellers, "
          "and you need to find out what is going on.")


def fall_choice():
    """
    Handles the player's actions and choices when getting out of the
    hibernation pod and falling.
    The player has to make a choice while falling and the game will respond
    to their decision.

    If user chooses to grab the door, they will regain balance and continue
    exploring the room.
    If they grab the cord they get electrocuted, it ends the game and runs its
    processes.
    If the risk injury and fall, they get hurt and the game informs them they
    need to find bandages to cover the wound.
    Invalid input is handled with an error message.
    """
    while True:
        fall_decision = input("As you are falling, you decide to: \n"
                              "[a] grab onto the pod door \n"
                              "[b] grab a cord hanging from the ceiling \n"
                              "[c] risk injury from the fall \n> ").lower()

        # Player grabs the pod door and continues
        if fall_decision == "a":
            print("\nYou managed to grab onto the pod door")
            print("You regained your balance and start exploring. You are "
                  "in the room containing hibernation pods.")

            choose_path(fall_decision)

        # Player grabs the cord and gets electrocuted (game over)
        elif fall_decision == "b":
            print("\nYou accidentally grabbed the electrical cord "
                  "and got electrocuted.")
            print("You died.")
            print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
                  "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
                  "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

            # Set game outcome variables
            survived = False
            possible_ending = "Electrical cord"
            game_outcome_tracker.set_possible_ending(possible_ending)
            game_outcome_tracker.set_survival_status(survived)
            # Updates the victims google sheet by adding the username
            # and the ending type
            update_victims_list(game_outcome_tracker.username,
                                possible_ending)
            # Offers user an option to restart the game
            restart_game_choice()

        # Player's risks the fall, resulting in injury and bleeding
        elif fall_decision == "c":
            print("\nYou fell and cut your hand; you are bleeding.")
            print("You should find some bandages to cover the wound.")

            # Sets bleeding to True and starts inflicting damage to the
            # player each time take_damage is called while True
            bleeding = True
            player_health.set_bleeding_state(bleeding)
            player_health.take_damage()

            print("You start exploring the room.\n")

            choose_path(fall_decision)

        # Runs show_progress_score if user types in "progress" or "score" which
        # displays the scoreboard
        elif fall_decision == "progress" or fall_decision == "score":
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers them to
        # start from the beginning or to end the program
        elif fall_decision == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("\nInvalid input. Try again.")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
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

        # Handles player's choice to leave the hibernation pod
        if pod_choice == "yes" or pod_choice == "y":
            print("\nWith a little bit of struggle, the pod creaks open.")
            print("You step out but your legs falter, you start falling.\n")
            fall_choice()

        # Handles player's choice to stay in the hibernation pod
        elif pod_choice == "no" or pod_choice == "n":
            print("\nYou chose not to open the hibernation pod.")
            print("You fell asleep. \n")
            print("(-, –)｡｡zZ💤💤💤\n")
            print("Let's try again.")

        # Runs show_progress_score if user types in "progress" or "score" which
        # displays the scoreboard
        elif pod_choice == "progress" or pod_choice == "score":
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers them to
        # start from the beginning or to end the program
        elif pod_choice == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("\nInvalid input. Please choose either [y]yes or [n]no")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{pod_choice}"\n')


def the_end_message():
    """
    Prints out the endgame message and some details to set the scene.
    Offers an open ending with a possibility of expanding the game or
    creating a sequel in the future.
    """
    # Display a message based on the player's choices up until this point
    print("\nAs you contemplate the vastness of space and your uncertain "
          "journey, you realize that every choice you made has "
          "consequences.\n")

    # Check for a navigation fault and print messages if True
    if navigation_fault is True:
        print("The fate of the mission and its crew now rests in your hands.")
        print("You've overcome adversity, saved the mission from disaster, "
              "and made tough decisions. But the mysteries of space remain,"
              " and your story is far from over.\n")

        # Check for a bypass_system and print message if value is True
        if bypass_system is True:
            print("The ship, now set on an unknown path, drifting through the "
                  "cosmos.")

    # Print in case the if statement is not True
    else:
        print("You think about how far you have already come and the great "
              "distance you traveled to get to here. And you can't help but"
              " smile at the thought of everything that awaits you on your "
              "new planet Terra Novus, with all of the fellow travellers.\n")
    print("The future is still uncertain, but one thing is clear: your "
          "journey has only just begun.")

    # Offer possible sequel or updates for the story's continuation
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

    # Set game outcome variables
    survived = True
    if bypass_system is True:
        possible_ending = "Saved everyone - system bypass"
    else:
        possible_ending = "Saved everyone - master reboot"
    game_outcome_tracker.set_possible_ending(possible_ending)
    game_outcome_tracker.set_survival_status(survived)
    # Updates the survivors google sheet by adding the username
    # and the ending type
    update_survivors_list(game_outcome_tracker.username,
                          possible_ending)
    # Offers user an option to restart the game
    restart_game_choice()


def outer_space():
    """
    Handles the player's actions and choices when they leave the
    Airlock and 'step' into the vastness of space.
    After putting on the space suit in the Airlock the user can decide
    to exit the space ship and explore the outside of it.
    """
    global bypass_system
    # Updates the health state
    player_health.take_damage()

    print("\nAs you step outside the Airlock, you are immediately struck"
          " by the breathtaking view of the cosmos. Countless stars "
          "twinkle in the distance, and you're surrounded by the void of"
          " space.")
    print("\nThe silence is eerie, and you feel a strange mix of awe and"
          " vulnerability.")

    # If there's a navigation fault, guide the player to the navigation panel
    if navigation_fault is True:
        print("\nAfter a few minutes of floating through the emptiness of"
              " space, you head to find the navigation panel. As you "
              "finally reach the designated area. \nThe navigation reboot "
              "panel is in sight, and it's your only hope to set things "
              "right.")
        print("You follow the instructions step by step and reach the reboot "
              "panel. You open it and notice that the power source seems to "
              "be malfunctioning, which is likely the cause of the ship's "
              "navigation error.")

        # Lets player choose to repair or bypass the navigation system
        while True:
            outer_space_choice = input("You have two options: \n[a]"
                                       "repair the power source "
                                       "\n[b]bypass it \n> ").lower()

            # Handles player's choice to repair the power source
            if outer_space_choice == "a" or outer_space_choice == "repair":
                reboot_attempt = 0
                # Runs while the users attempts are less than max attempts
                # Current max attempts are 3 and the code was provided
                # at the start of the game. It is 29137
                while reboot_attempt < max_reboot_attempts:
                    # Clears the terminal
                    clear()
                    print("Please enter in the reboot code to initialise the "
                          "repair port: ")
                    print(f"(Attempt: {reboot_attempt + 1})")
                    # Request for the player to enter the reboot code to
                    # repair the power source
                    try:
                        reboot_code_input = int(input("\n> "))
                    # Handle an invalid input (non-integer input)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                    # Handles correct input
                    if reboot_code_input == reboot_code:
                        print("You are in, the reboot code was correct! "
                              "\nWell done!!")
                        print("\nYou carefully start repairing the power "
                              "source. After some time and with your steady"
                              " hands, you manage to fix it. The navigation "
                              "system comes back online, and the ship's "
                              "trajectory is corrected.")
                        print("\nCongratulations! You've successfully saved "
                              "the mission, and the ship is now back on "
                              "track. \nThe travellers will one day find out "
                              "about your heroics and appreciate everything "
                              "you did for them, complete strangers, on this"
                              " faraway voyage into unknown.")
                        the_end_message()
                    # Handles incorrect input and continues with the loop
                    else:
                        print("Incorrect code. Please try again.")
                        reboot_attempt += 1
                # Handles outcome when maximum attempts are crossed
                else:
                    print("\nMaximum number of attempts reached. The "
                          "navigation malfunction remains unrepaired.")
                    if navigation_fault.nav_threat > 0:
                        navigation_fault.navigation_failure()
                        # Updates the navigation threat

            # Handles player's choice to bypass the power source
            elif outer_space_choice == "b" or outer_space_choice == "bypass":
                clear()
                print("\nYou decide to bypass the malfunctioning power source "
                      "as it's too risky to repair it without proper tools. "
                      "\nThe navigation system reboots, but you notice that "
                      "the course is set for an unknown destination.")
                print("\nYou have a sinking feeling that your actions might "
                      "have dire consequences, but for now, you've "
                      "successfully fixed the immediate issue. The future of "
                      "the mission remains uncertain.")
                print("\nWe are on an unknown path now, we will weave our own"
                      " destiny.")
                print("Maybe one day we will manage to get to our planet "
                      "Terra Novus, but for now we will drift through space,"
                      " until we find our way home.")
                # Sets the bypass_system to True which effects the outcome
                bypass_system = True
                # Runs through the end scenario where player survived
                the_end_message()

            # Runs show_progress_score if user types in "progress" or "score"
            # which displays the scoreboard
            elif (outer_space_choice == "progress" or
                  outer_space_choice == "score"):
                show_progress_score()

            # Runs restart_game_choice if user types in "end" which offers them
            # to start from the beginning or to end the program
            elif outer_space_choice == "end":
                restart_game_choice()

            # Handles incorrect input and continues with the loop
            else:
                print("\nYou're paralyzed by the weight of the decision. Time "
                      "is running out. The navigation system awaits your "
                      "choice.")
                print("Invalid input, your choices are [a]repair or [b]bypass")
                print('You can end the game by typing "end"')
                print('You can check the scoreboard by typing "progress"'
                      ' or "score"')
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
    # Updates the health state
    player_health.take_damage()

    # Checks the space_suit state and runs through the scenario depaning
    # on the space_suit state
    if space_suit is True:
        print("\nYou approach the Airlock hatch and secure your spacesuit.")
        print("The hatch opens smoothly, and you step into the airlock "
              "chamber.")
        print("You feel the rush of air leaving the chamber as it "
              "depressurizes.")
        print("\nOnce the process is complete, the outer airlock door opens, "
              "revealing the vastness of space.")
        print("You're now ready to continue your journey into the unknown.")

        if navigation_fault.nav_threat > 0:
            # Updates the navigation threat
            navigation_fault.navigation_failure()

        # Starts the outer_space scenario
        outer_space()

    # Runs a scenario where player didn't put on the space suit and handles
    # its outcome
    else:
        print("\nYou approach the Airlock hatch and begin to turn the "
              "wheel to open it. The hatch, however, seems much"
              " heavier than expected.\n")
        print("\nWith a lot of effort, you manage to turn the wheel "
              "and start opening the hatch, but as you do, you feel"
              " the air pressure in the chamber drop rapidly. The "
              "alarm sirens begin to blare, and you realize your "
              "mistake.\n")
        print("\nThe airlock chamber starts depressurizing rapidly,"
              " causing extreme discomfort as you struggle to "
              "breathe. Panic sets in as you realize you won't "
              "survive in the vacuum of space without a "
              "spacesuit.\n")
        print("\nDesperation takes over as you scramble to put on the "
              "nearby spacesuit, but it's too late. The airlock door "
              "to space opens, and you're sucked out into the cold, "
              "unforgiving void.\n")

        # Checks if the shadow_figure is true and displays additional
        # message for the story continuation
        if shadow_figure is True:
            print("\nAs you slowly freeze and your vision darkens, the"
                  "very last thing you see is a dark shadow looming "
                  "over you.\n")
            print("You can't make out any features, just a vague, "
                  "unsettling silhouette.")
            print("\nFear and regret wash over you as you wonder who "
                  "or what this shadow is and why it's watching you"
                  " in your final moments. But it's too late, and your"
                  " consciousness fades into nothingness in the void "
                  "of space.\n")

        print("You died.")
        print("Your adventure ends here.")
        print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
              "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
              "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

        # Set game outcome variables
        survived = False
        possible_ending = "Froze in space"
        game_outcome_tracker.set_possible_ending(possible_ending)
        game_outcome_tracker.set_survival_status(survived)
        # Updates the victims google sheet by adding the username
        # and the ending type
        update_victims_list(game_outcome_tracker.username,
                            possible_ending)
        # Offers user an option to restart the game
        restart_game_choice()


def engineering_bay():
    """
    Handles the player's actions and choices when they arrive to the
    Engineering Bay.
    The user can choose to explore the Engineering Bay or continue
    on their way to explore the rest of the ship.
    """

    def engineering_bay_path_choice():
        """
        Handles the player's actions and choices when they decide to leave the
        Engineering Bay.
        The user can choose stay insideof the engineering bay and continue to "
        "explore orleave towards the Airlock, and continue the story."
        """
        global space_suit

        # Updates the health state
        player_health.take_damage()

        print("As you head on out to leave you stop for a second.")

        # Lets player choose if they wish to stay in Engineering Bay or
        # continue into the Airlock
        while True:
            engineering_bay_path_options = input("Do you:\n[a]stay and explore"
                                                 " the Engineering Bay further"
                                                 "\n[b]leave to explore the "
                                                 "Airlock\n> ").lower()

            # Handles player's choice to stay in the Engineering Bay
            if (engineering_bay_path_options == "a" or
                    engineering_bay_path_options == "stay"):
                clear()
                print("\nYou are certain you didn't discover all of the secret"
                      " within the Engineering Bay, you decide to continue "
                      "exploring it.")

                if navigation_fault.nav_threat > 0:
                    # Updates the navigation threat
                    navigation_fault.navigation_failure()

                # Runs the Engineering Bay function again
                engineering_bay()

            # Handles player's choice to leave the Engineering Bay
            elif (engineering_bay_path_options == "b" or
                    engineering_bay_path_options == "leave"):
                clear()
                print("\nYou feel the time has come to continue exploring "
                      "further.")

                if navigation_fault.nav_threat > 0:
                    # Updates the navigation threat
                    navigation_fault.navigation_failure()

                # Checks if shadow_figure is True and prints a message if True
                if shadow_figure is True:
                    print("You are still curious why you haven't encountered "
                          "the shadowy figure from earlier. You are completly "
                          "confounded as to why the person wouldn't help you. "
                          "\nWere they the reason why you woke up? Why are "
                          "they still hiding? Who or what woke them up? How "
                          "long have they been awake for?")

                # Checks if navigation fault is active and prints a message
                # if True
                elif navigation_fault is True:
                    print("You still wonder what is the reason you woke up? "
                          "Was it all because of the navigational error? Was"
                          " I the only one who could have fixed the system "
                          "or was this just another error from the failing "
                          "system? Will I succeed at is?")

                # Handles output if shadow_figure and navigation threat are
                # both false
                else:
                    print("You still wonder what is the reason you woke up? "
                          "Who or what woke you up form your hibernation pod?"
                          "What is the whole purpose of this?")

                print("\nSo many questions running through your mind.")
                print("Once again you push your running thoughts from your "
                      "head, maybe you will encounter them, to ask them all"
                      " those questions, but for now you decide to continue"
                      " on your way.")
                print("\nYou step in front of the sealed door that leads to "
                      "the Airlock, press your palm against the sensor lock")
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

                # Lets player choose whether they will put the space suit on or
                # not. Gives different output depending on the answer
                while True:
                    space_suit_choice = input("\nWould you like to put the "
                                              "space suit on?\n[y]yes \n[n]no"
                                              "\n> ").lower()

                    # Handles player's choice if they choose yes
                    if space_suit_choice == "y" or space_suit_choice == "yes":
                        # Clears the terminal
                        clear()
                        print("\nYou put on the space suit and get ready to "
                              "walk into the airlock.")
                        print("You look out the small window and check the "
                              "screen, making sure there is no malfunctions "
                              "in the Airlock system.")
                        print("All of the systems look good and there is no "
                              "visual malfunctions inside the Airlock.")

                        # Checks if navigation threat is active and prints a
                        # message if True
                        if navigation_fault is True:
                            print("\nYou use the screen to locate and check "
                                  "all of the instructions for navigation "
                                  "reboot. You memorize the detailed instruc"
                                  "tions on how to get to the navigation "
                                  "reboot panel and proceed to follow them  "
                                  "carefully.")
                            print("One sentence grabs your attention as you "
                                  "read through, 'Reboot Code is generated by "
                                  "the computer for each error, code should "
                                  "have been written on the error report.'")
                            print("You remember seeing an error report earlier"
                                  " in the ship's Control Bay. It contained "
                                  "the reboot code needed to fix the "
                                  "navigation system.")
                            print("You scratch your head hoping you can "
                                  "remember it by the time you reach the "
                                  "navigation panel.\n")
                        # Sets space_suit to True
                        space_suit = True
                        # Runs the airlock scenario
                        airlock()

                    # Handles player's choice if they choose yes
                    elif space_suit_choice == "n" or space_suit_choice == "no":
                        clear()
                        print("In your hurry to leave, you neglect the "
                              "space suit, thinking it might slow you down. ")
                        # Sets space_suit to False
                        space_suit = False
                        # Runs the airlock scenario
                        airlock()

                    # Runs show_progress_score if user types in "progress"
                    # or "score" which displays the scoreboard
                    elif (space_suit_choice == "progress" or
                          space_suit_choice == "score"):
                        show_progress_score()

                    # Runs restart_game_choice if user types in "end" which
                    # offers them to start from the beginning or to
                    # end the program
                    elif space_suit_choice == "end":
                        restart_game_choice()

                    # Handles incorrect input and continues with the loop
                    else:
                        print("Invalid input, your choices are [y]yes or "
                              "[n]no")
                        print('You can end the game by typing "end"')
                        print('You can check the scoreboard by typing '
                              '"progress" or "score"')
                        print(f'\nYou typed in "{space_suit_choice}"\n')

            # Runs show_progress_score if user types in "progress" or "score"
            # which displays the scoreboard
            elif (engineering_bay_path_options == "progress" or
                  engineering_bay_path_options == "score"):
                show_progress_score()

            # Runs restart_game_choice if user types in "end" which offers
            # them to start from the beginning or to end the program
            elif engineering_bay_path_options == "end":
                restart_game_choice()

            # Handles incorrect input and continues with the loop
            else:
                print("Invalid input, your choices are [y]yes or [n]no")
                print('You can end the game by typing "end"')
                print('You can check the scoreboard by typing "progress"'
                      ' or "score"')
                print(f'\nYou typed in "{engineering_bay_path_options}"\n')

    # Handles output if shadow_figure is True
    if shadow_figure is True:
        print("\nAs you step into the Engineering Bay, you think back "
              "to a shadowy figure running from the broken vase.")
        print("You wonder who they might be, and where are they directing "
              "you to, why don't they just aproach you, to help with this "
              "situation we find ourselves in.")
        print("The questions keep running through your head, but you can't"
              " stop now. You continue on.")
    # Handles output if shadow_figure is False
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

    # Lets player choose whether they want to explore Engineering Bay or not
    while True:
        explore_engineering_bay = input("\nWould you like to explore the "
                                        "Engineering bay?\n[y]yes\n[n]no.\n> ")

        # Handles player's choice if they choose yes
        if explore_engineering_bay == "y" or explore_engineering_bay == "yes":
            print("\nYou start exploring and walking around. You are as exited"
                  " as a lettle kid in a chocolate factory.")

            # Lets player choose which part of Engineering Bay would they like
            # to explore
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

                # Handles player's choice to explore crafting
                if explore_choice == "a" or explore_choice == "crafting":
                    # Clears the terminal
                    clear()
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

                # Handles player's choice to explore constructors
                elif (explore_choice == "b" or explore_choice == "constructors"
                      or explore_choice == "deconstructors"):
                    # Clears the terminal
                    clear()
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

                # Handles player's choice to explore mystery computer in the
                # corner of the room
                # This sets and opens up a posibility to add games within the
                # adventure game
                elif (explore_choice == "c" or explore_choice == "mystery"
                      or explore_choice == "computer"):
                    # Clears the terminal
                    clear()
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

                # Handles player's choice to continue with their adventure
                elif (explore_choice == "d" or explore_choice == "stop"
                      or explore_choice == "continue"):
                    # Clears the terminal
                    clear()
                    print("\nYou have decided to continue on with your "
                          "adventure.")
                    print("As you walk down the dimly lit corridor, you"
                          " can't help but wonder what else hides on this "
                          "spaceship in its mysterious depths.")
                    print("You continue your journey with a sense of "
                          "anticipation. What other secrets and surprises are"
                          " waiting for you on this interstellar expedition?")
                    # Runs engineering_bay_path_choice scenario
                    engineering_bay_path_choice()

                # Runs show_progress_score if user types in "progress" or
                # "score" which displays the scoreboard
                elif explore_choice == "progress" or explore_choice == "score":
                    show_progress_score()

                # Runs restart_game_choice if user types in "end" which
                # offers them to start from the beginning or to end
                # the program
                elif explore_choice == "end":
                    restart_game_choice()

                # Handles incorrect input and continues with the loop
                else:
                    print("Invalid input, your choices are [a]crafting, "
                          "[b]constructors, [c]computer, [d]stop or continue")
                    print('You can end the game by typing "end"')
                    print('You can check the scoreboard by typing "progress"'
                          ' or "score"')
                    print(f'\nYou typed in "{explore_choice}"\n')

        # Handles player's choice if they choose no
        elif explore_engineering_bay == "n" or explore_engineering_bay == "no":
            # Clears the terminal
            clear()
            print("\nYou have decided to continue on with your "
                  "adventure.")
            print("As you walk down the dimly lit corridor, you"
                  " can't help but wonder what else hides on this "
                  "spaceship in its mysterious depths.")
            print("You continue your journey with a sense of "
                  "anticipation. What other secrets and surprises are"
                  " waiting for you on this interstellar expedition?")
            # Runs engineering_bay_path_choice scenario
            engineering_bay_path_choice()

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif fall_decision == "progress" or fall_decision == "score":
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif fall_decision == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input, your choices are [y]yes or [n]no")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{explore_engineering_bay}"\n')


def escape_pods_lift_ending():
    """
    Handles another possible ending depending on the player's choices so far.
    The game ends in the softer tone, leaving an opening for future additions
    to the game.
    The user can choose to leave the Control Room across the room towards
    the Engineering Bay or to use a lift to go down into Escape Pods.
    """
    # Updates the health state
    player_health.take_damage()

    if navigation_fault.nav_threat > 0:
        # Updates the navigation threat
        navigation_fault.navigation_failure()

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
    print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
          "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
          "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

    # Set game outcome variables
    survived = False
    possible_ending = "Elevator malfunction"
    game_outcome_tracker.set_possible_ending(possible_ending)
    game_outcome_tracker.set_survival_status(survived)
    # Updates the victims google sheet by adding the username
    # and the ending type
    update_victims_list(game_outcome_tracker.username,
                        possible_ending)
    # Offers user an option to restart the game
    restart_game_choice()


def escape_pods():
    """
    Handles the player's actions and choices when they arrive to the
    Escape Pods.
    The user can choose to save themselves or use a lift and go back into
    Cargo Hold and continue to explore the rest of the ship.
    """
    # Updates the health state
    player_health.take_damage()

    print("Only few seconds pass before the elevator stops.\n")
    print("The doors swing open, and you find yourself in a state "
          "of awe.")
    print("As you look around, you notice a numerous escape pods, "
          "each with its own unique design, waiting to be explored.\n"
          "The soft, pulsating glow of their control panels and the "
          "promise of safety within them beckon you closer.")

    # Checks if navigation threat is active and prints a message if True
    if navigation_fault is True:
        print("\nYou can't help but remember the unsettling navigation error "
              "and the looming threat of a critical system failure, which "
              "hangs like a heavy cloud over your thoughts.")
        print("The weight of responsibility presses on your shoulders.")
        print("The stress of it all seems a bit too much to handle.")
        print("Being at this place, you start to feel a nudge towards using "
              "an escape pod.")
    # Handles the output if navigation threat is False
    else:
        print("\nYou can't help but think of all of the mysteries that are "
              "surrounding the whole scenario since you woke up.")
        print("The uncertainty of the whole situation looms over you as "
              "a shadow.\n")

    # Lets player choose whether they use escape pods and save themselves
    # or if they choose to go back and save all of the fellow travalers
    while True:
        escape_pod_option = input("Do you: \n[a]give into the feeling and "
                                  "escape \n[b] turn around and go back to"
                                  " try and save everyone?\n> ")

        # Handles player's choice to escape and save themselves
        if escape_pod_option == "a" or escape_pod_option == "escape":
            clear()
            # Checks if navigation threat is active
            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()
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

            # Checks if navigation fault is True
            if navigation_fault is True:
                print("\nThe road to Terra Novus is uncertain, but at least "
                      "you managed to escape the impending doom.")
            # Output if navigation fault is False
            else:
                print("\nThe road to Terra Novus is unknown, but at least "
                      "you managed to escape the uncertainty.")
            print("\nAs you speed through space, a shadowy figure is staring"
                  " at your escape pod from the ship, their identity and "
                  "intentions veiled in mystery, you get an unsettling "
                  "sense of uncertainty and a feeling of dread that this"
                  " is not completely over.\n")
            print("...\n")
            print("\nThank you for playing")
            print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
                  "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
                  "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

            # Set game outcome variables
            survived = True
            possible_ending = "Escape pod - saved themselves"
            game_outcome_tracker.set_possible_ending(possible_ending)
            game_outcome_tracker.set_survival_status(survived)
            # Updates the survivors google sheet by adding the username
            # and the ending type
            update_survivors_list(game_outcome_tracker.username,
                                  possible_ending)
            # Offers user an option to restart the game
            restart_game_choice()

        # Handles player's choice to stay and save their fellow travellers
        elif escape_pod_option == "b" or escape_pod_option == "save":
            if navigation_fault.nav_threat > 0:
                navigation_fault.navigation_failure()
                # Updates the navigation threat
            clear()
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

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (escape_pod_option == "progress" or
              escape_pod_option == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif escape_pod_option == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input, your choices are [a]escape or [b]go back")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{escape_pod_option}"\n')


def cargo_hold_path_choice():
    """
    Handles the player's actions and choices when they decide to leave
    the Cargo Hold.
    The user can choose to leave the Control Room across the room towards
    the Engineering Bay or to use a lift to go down into Escape Pods.
    """
    global shadow_figure

    # Updates the health state
    player_health.take_damage()

    print("\nAs you start to leave, a large Egyptian vase falls in "
          "the distance. \nYou jump, startled out of your mind, you "
          "run in the direction of the fallen vase.\n")
    print("You explore the rubble and realise that the vase couldn't"
          " have fallen on it's own. \nYou see a shadow running away "
          "from you.")
    print("You decide to follow, but soon find yourself at the cross "
          "section.")

    # Updates shadow_figure to True
    shadow_figure = True

    # Lets player choose which way they would like to follow the shadowy figure
    while True:
        cargo_hold_path_options = input("\nWhich way do you follow? \n[a] left"
                                        " into the suspiciously old and "
                                        "unmarked lift that takes you down a "
                                        "level\n[b] right into the Engineering"
                                        " Bay\n> ").lower()

        # Handles users choice to follow left inside a suspiciously old lift
        # This helps set up the death scenario if they decide to come back from
        # the escape pods section
        if (cargo_hold_path_options == "a" or
                cargo_hold_path_options == "left"):
            # Clears the terminal
            clear()
            print("\nYou step into the mysterious elevator, its metal doors "
                  "creak and slide shut as it whisks you away to a lower "
                  "level.\n")
            print("Riding the elevator, you realise you don't know where "
                  "you are going, you start to doubt whether it was a "
                  "smart idea just to jump in like that...\n")
            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()
            # Runs escape pods scenario
            escape_pods()

        # Handles user choice to follow the figure into Engineering Bay
        # The shadow figure is not relevant to the story line at the moment
        # they are there to offer some suspense
        elif (cargo_hold_path_options == "b" or
              cargo_hold_path_options == "right"):
            # Clears the terminal
            clear()
            print("\nYou decide to follow to the Engineering Bay, hoping "
                  "your mind is not playing tricks on you, or worse "
                  "you have started loosing your mind and are becoming"
                  " delirious.")
            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()
            print("You run as fast as your legs can carry you. But "
                  "can't seem to catch up.")
            # Runs the Engineering Bay scenario
            engineering_bay()

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (cargo_hold_path_options == "progress" or
              cargo_hold_path_options == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif cargo_hold_path_options == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input, your choices are [a]left or [b]right")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{cargo_hold_path_options}"\n')


def cargo_hold():
    """
    Handles the player's actions and choices when they reach the Cargo Hold.
    After a user reaches Control Room they can choose to explore the Cargo
    Hold, or continue on exploring the ship.
    """
    # Updates the health state
    player_health.take_damage()

    print("\nAs you continue your exploration, you eventually reach "
          "the massive Cargo Hold.\n")
    print("The Cargo Hold is filled with an array of cargo: stacked "
          "boxes, vital supplies, sturdy containers, various vehicles, "
          "reserves of fuel, an assortment of spare parts, live animal "
          "specimens in their own special cryo-hibernation chambers and more.")

    # Lets user choose whether they would like to explore the Cargo Hold and
    # various cargo or continue on their way
    while True:
        cargo_hold_options = input("\nWhich part of the Cargo Hold "
                                   "would you like to explore?\n"
                                   "[a] boxes and supplies\n"
                                   "[b] vehicles\n"
                                   "[c] specimens\n"
                                   "[d] continue on/ don't explore"
                                   "\n> ").lower()

        # Handles choice to examine the various boxes.
        if cargo_hold_options == "a" or cargo_hold_options == "boxes":
            clear()
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

        # Handles choice to examine the numerous vehicles
        elif (cargo_hold_options == "b" or
                cargo_hold_options == "vehicles"):
            clear()
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

        # Handles choice to examine the live specimens sent with them
        elif (cargo_hold_options == "c" or
                cargo_hold_options == "specimens"):
            clear()
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

        # Handles choice to continue with exploration of the ship
        elif (cargo_hold_options == "d" or
                cargo_hold_options == "continue"):
            # Clears the terminal
            clear()
            print("\nYou made a decision to continue exploring the ship.")
            print("Who knows what you might find next...")
            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()
            # Starts the cargo_hold_path_choice scenario
            cargo_hold_path_choice()

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (cargo_hold_options == "progress" or
              cargo_hold_options == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif cargo_hold_options == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input, your choices are [a]boxes, [b]vehicles, "
                  "[c]specimens or [d]continue")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{cargo_hold_options}"\n')


def control_room_choose_path():
    """
    Handles the player's actions and choices which
    way they would like to go from the Control Room.
    User is located in the Control Room and needs
    to choose which way they would like to continue going.
    """
    print("You find yourself at the cross section.")

    # Lets player choose which way they would like to proceed
    while True:
        control_path_choice = input("\nYour options are: \n[a]Go left "
                                    "into the Cargo Hold \n[b]Go right "
                                    "into the Engineering Bay"
                                    "\n> ").lower()

        # Handles player's choice to proceed left
        if control_path_choice == "a" or control_path_choice == "left":
            # Clears the terminal
            clear()
            # Updates the health state
            player_health.take_damage()
            print("\nYou head left towards the Cargo Hold.")

            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()

            # Runs cargo_hold scenario
            cargo_hold()

        # Handles player's choice to go right
        elif control_path_choice == "b" or control_path_choice == "right":
            # Clears the terminal
            clear()
            # Updates the health state
            player_health.take_damage()

            print("\nYou head right towards the Engineering Bay. Wondering"
                  " what might you find there.")

            if navigation_fault.nav_threat > 0:
                # Updates the navigation threat
                navigation_fault.navigation_failure()

            # Runs engineering_bay scenario
            engineering_bay()

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (control_path_choice == "progress" or
              control_path_choice == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif control_path_choice == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input, you can go either [a]left or [b]right")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
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
    # Updates the health state
    player_health.take_damage()

    print("\nYou reach the Control Room.")
    print("You are fascinated by all of the screens "
          "and blinking lights in this room.")

    # Lets player choose whether they would like to explore the screens or
    # continue on without checking them out
    while True:
        control_room_options = input("Do you \n[a]explore the screens "
                                     "\n[b]continue on"
                                     "\n> ").lower()

        # Handles player choice to explore the screens where they find out
        # about the navigational fault that starts the threat countdown
        # and directs the ship into asteroid field if not corrected swiftly
        if control_room_options == "explore" or control_room_options == "a":
            # Clears the terminal
            clear()
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

            # Updates the navigation threat to True and starts the failure
            # process
            navigation_fault.navigation_error = True
            navigation_fault.navigation_failure()

            # Breaks out of the loop to continue to control_room_choose_path
            break

        elif control_room_options == "continue" or control_room_options == "b":
            # Clears the terminal
            clear()
            print("You decide to ignore all of the screens and "
                  "continue on your way to explore the ship.")

            # Breaks out of the loop to continue to control_room_choose_path
            break

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (control_room_options == "progress" or
              control_room_options == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif control_room_options == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("Incorrect input, please choose [a]explore or [b]continue")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{control_room_options}"\n')

    # Runs the control_room_choose_path scenario
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
    # Set bleeding to False and changes state in HealthState class
    # Stops damage active effects
    bleeding = False
    player_health.set_bleeding_state(bleeding)


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

    # Runs healing_procedure despite player's choice
    healing_procedure()

    # Kills player as a result of post forceful healing complications
    print("\nInjecting a short term memory loss serum.")
    print("Error.. error..")
    print("Specimen has received the wrong serum.\n")
    print("Regene.. \nCham.. \n30.. shut.. \ndow..")
    print("\n/////////////////\n")
    print("You have received a deadly dose of serum.")
    print("You died.")
    print("\n███ █╬█ ██ ╬╬ ██ █╬╬█ ██▄\n"
          "╬█╬ █▄█ █▄ ╬╬ █▄ ██▄█ █╬█\n"
          "╬█╬ █╬█ █▄ ╬╬ █▄ █╬██ ███\n")

    # Set game outcome variables
    survived = False
    possible_ending = "Forced healing"
    game_outcome_tracker.set_possible_ending(possible_ending)
    game_outcome_tracker.set_survival_status(survived)
    # Updates the victims google sheet by adding the username
    # and the ending type
    update_victims_list(game_outcome_tracker.username,
                        possible_ending)
    # Offers user an option to restart the game
    restart_game_choice()


def med_bay_choose_path():
    """
    Handles the player's actions and choices when in the Med Bay.
    The user can choose to continue exploring the spaceship and continue
    moving through the rest of the rooms left to explore.
    """
    global shadow_figure

    # Updates the health state
    player_health.take_damage()

    print("You walk through the Med Bay exploring.")
    print("You pass around the Regenesis Chamber 3000 and "
          "reach two corridors.\n")

    # Lest player decide whether they want to explore the Observation Deck
    # or the Library
    while True:
        print("To your left you can see the long winding corridor "
              "that will take you to the Observation Deck[a]")
        print("To your right you have a straight path into the Library[b]\n")

        med_bay_path_choice = input("What would you like to explore? "
                                    "\n[a]left \n[b]right \n> ").lower()

        # Handles player's choice to go left
        if med_bay_path_choice == "a" or med_bay_path_choice == "left":
            # Clears the terminal
            clear()
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

            # Handles player's choice to proceed to Engineering Bay
            if (observation_deck_option == "a" or
                    observation_deck_option == "Engineering Bay"):
                # Clears the terminal
                clear()
                print("\nYou go down the long halway heading into Engineering "
                      "Bay still thinking about the beautiful sight you have"
                      " just experienced.")
                # Runs engineering_bay path
                engineering_bay()

            # Handles player's choice to proceed to Medical Bay
            elif (observation_deck_option == "b" or
                  observation_deck_option == "Med Bay"):
                # Clears the terminal
                clear()
                print("\nYou turn around to explore the Medical Bay further.")
                # Runs med_bay_choose_path path
                med_bay_choose_path()

            # Runs show_progress_score if user types in "progress" or "score"
            # which displays the scoreboard
            elif (observation_deck_option == "progress" or
                  observation_deck_option == "score"):
                show_progress_score()

            # Runs restart_game_choice if user types in "end" which offers
            # them to start from the beginning or to end the program
            elif observation_deck_option == "end":
                restart_game_choice()

            # Handles incorrect input and continues with the loop
            else:
                print("\n Invalid input. Please choose [a]left or [b]right")
                print('You can end the game by typing "end"')
                print('You can check the scoreboard by typing "progress"'
                      ' or "score"')
                print(f'\nYou typed in "{observation_deck_option}"\n')

        # Handles player's choice to go right
        elif med_bay_path_choice == "b" or med_bay_path_choice == "right":
            # Clears the terminal
            clear()
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

            # Sets shadow_figure to True
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

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (med_bay_path_choice == "progress" or
              med_bay_path_choice == "score"):
            show_progress_score()

        # Runs restart_game_choice if user types in "end" which offers
        # them to start from the beginning or to end the program
        elif med_bay_path_choice == "end":
            restart_game_choice()

        # Handles incorrect input and continues with the loop
        else:
            print("\n Invalid input. Please choose [a]left or [b]right")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{med_bay_path_choice}"\n')


def med_bay():
    """
    Handles the player's actions and choices when they reach the Med Bay.
    After a user reaches Med Bay they can choose to either check their health,
    heal their wound and stop the bleeding if they were damaged at the start
    or they can continue with their exploration of the spaceship.
    """
    # Updates the health state
    player_health.take_damage()

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

    # Lets player choose do they want to test their health or not
    while True:
        healing_chamber = input("Would you like to test your health? "
                                "\n[y]yes \n[n]no \n> ").lower()

        # Handles player's choice to test their healt
        if healing_chamber == "y" or healing_chamber == "yes":

            print("\nScanning...\n")
            print("Scan complete!")
            # Checks if the bleeding is True and runs a scenario
            # depending on the return
            if player_health.bleeding:
                print("Anomaly detected.")
                print("Wound detected on the left forearm.")
                heal_wound = input("\nWould you like to heal the wound? "
                                   "\n[y]yes \n[n]no \n> ").lower()

                # Handles choice to heal the wound
                if heal_wound == "y" or heal_wound == "yes":
                    # Clears the terminal
                    clear()
                    # Runs the healing procedure
                    healing_procedure()

                # Handles choice not to heal the wound
                elif heal_wound == "n" or heal_wound == "no":
                    # Clears the terminal
                    clear()
                    # Runs the forceful healing procedure
                    forceful_healing_procedure()

                # Runs restart_game_choice if user types in "end" which
                # offers them to start from the beginning or to end the
                # program
                elif heal_wound == "end":
                    restart_game_choice()

                # Runs show_progress_score if user types in "progress"
                # or "score" which displays the scoreboard
                elif (heal_wound == "progress" or
                        heal_wound == "score"):
                    show_progress_score()

                # Handles incorrect input and continues with to loop
                else:
                    print("\nInvalid input. Please choose either yes/y"
                          " or no/n")
                    print('You can end the game by typing "end"')
                    print('You can check the scoreboard by typing "progress"'
                          ' or "score"')
                    print(f'\nYou typed in "{healing_chamber}"\n')

            # Handles the outcome if bleeding is False
            else:
                print("No anomalies detected.")
                print("\nYou are a healthy specimen.\n")
            print("Thank you for using Regenesis Chamber 3000\n")
            # Runs with the med_bay_choose_path scenario
            med_bay_choose_path()

        # Handles player's choice not to test their healt
        elif healing_chamber == "n" or healing_chamber == "no":
            # Runs with the med_bay_choose_path scenario
            med_bay_choose_path()

        # Runs restart_game_choice if user types in "end" which offers them
        # to start from the beginning or to end the program
        elif healing_chamber == "end":
            restart_game_choice()

        # Runs show_progress_score if user types in "progress" or "score"
        # which displays the scoreboard
        elif (healing_chamber == "progress" or healing_chamber == "score"):
            show_progress_score()

        # Handles incorrect input and continues with to loop
        else:
            print("\nInvalid input. Please choose either yes/y or no/n")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
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

    # Offers player a choice which path they would like to take
    while True:
        path_choice = input("Which path would you like to "
                            "take? \n[a]straight \n[b]right \n> ").lower()

        # Checks if user chose path 'a'
        # Runs through the scenario where player proceeds straight
        if path_choice == "a" or path_choice == "straight":
            # Clears the terminal
            clear()
            print("You head straight towards the Control Room.")
            print("Eager to continue exploring.\n")
            # Runs the Control Room scenario
            control_room()

        # Checks if user chose path 'b'
        # Runs through the scenario where player proceeds straight
        elif path_choice == "b" or path_choice == "right":
            # Clears the terminal
            clear()
            print("You head right towards the Med Bay.")
            print("Eager to continue exploring.")
            # Runs the Med Bay scenario
            med_bay()

        # Runs restart_game_choice if user types in "end" which offers them to
        # start from the beginning or to end the program
        elif path_choice == "end":
            restart_game_choice()

        # Runs show_progress_score if user types in "progress" or "score" which
        # displays the scoreboard
        elif (path_choice == "progress" or path_choice == "score"):
            show_progress_score()

        # Handles incorrect input and continues with the loop
        else:
            print("Invalid input. Please choose [a]straight or [b]right")
            print('You can end the game by typing "end"')
            print('You can check the scoreboard by typing "progress"'
                  ' or "score"')
            print(f'\nYou typed in "{path_choice}"\n')


def main():
    """
    Starts the game progress and controls the outcomes depending on the
    initial user choice of what they decided to do in the beginning of
    the game.
    """
    # Clears the terminal
    clear()
    # Runs the start_game_message function
    start_game_message()
    # runs the open_hibernation_pod function
    open_hibernation_pod()


# Runs 'main' function if script is run as the main program
if __name__ == "__main__":
    main()
