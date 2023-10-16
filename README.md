# [SpaceShip Adventure](https://github.com/LukaB25/spaceship-adventure)

## Introduction

- The SpaceShip Adventure is a text based game that was inspired by "retro" games of similar style
- The SpaceShip Adventure is targeted to all of the fans of text based games that are on a quest for a new adventure
- The SpaceShip Adventure offers it's users a fun and interactive adventure that plays out the outcomes depending on their choices.
- There are multiple ways to survive, but also to die. The game will keep track of all of the users and the progress they made by storing the data inside of google sheets.

## Wireframes - [Lucid](https://lucid.app/)
![Lucid basic game progress mind map](images/lucid_mind_map.avif)
### Mind map
- The mind map is just a basic starting plan that was used to plan out the progress of the game

#### Game start
- On game start the player can see ASCII picture and a "Welcome to your spaceship adventure!" message.
- The player is prompted to input their username and can not proceed without it.
- The game loads the starting messages, first one explaining the features and how to access them, and the second message that offer the player a backstory into the game which sets up the scene.

#### Hibernation pod
- Gives player choice to get out of the pod or stay.
- Once they decide to leave the pod they are prompted that they are falling.
- Player can choose to grab the door [get away safely], grab the cord hanging from ceiling [get electricuted and die], or to risk falling [resulting in injury and they are bleeding = player has 5 moves before they bleed out, need to reach Med Bay to be healed]
- After which they are offered a choice to go to the Control room [straight] or Medical Bay [right]

#### Control room
- The user walks in and is taken back by all of the flashing lights on the control panels, they can choose to either check the panels or to continue on their way.
- If player examines the panels they discover the critical navigation error that forces them to find their way and get out of the spaceship to fix the fault
- If they ignore the panels, they continue with the story without looming threat.
- The player can proceed to the Cargo Hold[left] or Engineering Bay[right]

#### Medical Bay/Med Bay
- The player walks in the Med Bay and is speechless from the amount of various healing machines. In the middle of the room they can see a Regenesis Chamber 3000, a special healing machine that can heal any wound.
- They can choose to get examined by the machine or to ignore it and walk by it. 
- If they choose to check the wound from earlier, they can either choose to heal it or not, the healing does just that, but if they choose not to heal the wound, the machine tries to heal them forcefully and use a amnesia serum on them, to forget about it, but there is an error and the machine ends up killing you[you die]
- Once you are healed the bleeding effect is removed. 
- You can choose the next path, onto the Observation Deck or into the Library.

#### The Library
- When you walk into the library you are left in awe of such place. You look around, and find a mysterious single book that is open on a table in the middle of the room.
- As you look at the book, you notice a shadowy figure looking at you from across the room. You run after them but find yourself at the same cross section inside the Med Bay

#### Observation Deck
- As you go down the long winding hallway you reach the Observation Deck, you are speechless at the sight in this room. You sit, take some time and enjoy the view in this place.
- After a while you decide to continue your exploration, you have a choice to go back to the Med Bay or proceed to Engineering Bay

#### Cargo Hold
- Inside the Cargo Hold you can explore the cargo that was sent with you on the expedition or walk through.
- As they are leaving the shadowy figure knocks down a anique vase which attracts your attention, but when they follow them they come to the cross section, where they have to choose to proceed down with a mistery old elevator[unmarked Escape Pods] or to the Engineering Bay.

#### Escape Pods
- Player reaches the Escape Pods level and they can see rows on rows of Escape Pods.
- They can choose to either use the Escape Pods and save themselves or go back to save everyone.
- If they choose to save themselves the game will end and give them ending messages
- If they choose to stay and save everyone, they will go into the old elevator which will end up malfunctioning and killing them.

#### Engineering Bay
- Inside the Engineering Bay the user can explore and look around or continue on throught.
- If they choose to explore they will learn about futuristic tech, but will also discover an old antique computer in the corner, which  I had a plan to extend the game and offer multiple games within the adventure game, but due to lack of time decided to leave for future endeavours.
- after they proceed they can choose to turn around and stay or proceed into the Airlock

#### Airlock 
- Lets player make a choice whether they would like to put on a suit or not, which will proceed with the stoy if they put it on, but kill them if they decide not to put it on.

#### Space
- Depending on the state of the game, the game will either end here, unless the navigation error is active, which proceed with the story to offer the player options on how to save the mission by fixing the navigation with a previously given reboot code, or will they bypass the system error and send the spaceship towards the unknown course which will leave uncertain future for the player and fellow travellers.

#### Endings
- The game has 9 possible endings: 6 death and 3 survival endings.
- Depending on the ending the user reaches, they will get the outcome of the story and their progress will be saved in google sheets.

## About the build:

- I started the project by creating the github repository using the [Code Institute](https://codeinstitute.net/ie/) template and creating the new workspace on [CodeAnywhere](https://app.codeanywhere.com/) and opening the workspace.
- As part of my initial commit I created a ope_hibernation_pod() function that was intended to be the start of the game. Later on I decided to expand the story further and added multiple functions that work together to set up the story.
- I kept adding more functions to improve and manage the player's experience. I kept working on the story and adding more intricate options. 
- Given that the project is contained within a terminal, I made a decision to add couple of ASCII/text art to offer some graphics and design to attract the users.

## Features

### Google sheets

#### Download
- As soon as the game loads it imports the data from the google sheets and saves to the application, to be used at the users request.
- The data is stored in the two variables victims - for people that lost the game previously, and survivors - for people that won the game previously.

#### Upload
- Once the game ends, either by player dying by one of six death options or reaching one of three surviving endings, the data is automatically being stored in the google sheet and can be accessed again.

### ASCII art images

- The game contains couple of ASCII art and signs to offer better experience to the user
![ASCII Rocket image and SpaceShip Adventure logo sign](images/spaceship_adventure_ascii_art.avif)
- The rocket image was taken from [TextArt](https://textart.sh/topic/rocket), and improved on to have desired design.
- The sign was created and taken from [TextArtGenerator](https://www.textartgenerator.net/), and combined with the rocket image.

### Username

- On load the game asks for a username input and saves it until the game is finished, reset or ended.
- The username can not be whitespace or numbers, but it can be variation of letters, whitespace and numbers.

### Start

- As soon as the username is input the story starts to unfold.
- The starting message is displayed and gives player an insight into the backstory and lets them know what is going on
- The game starts from the player's viewpoint of waking up in their hibernation pod, also know as cryogenic sleep pod and their unfolds from there with their every choice.

### Choices

- Throughout the whole game the player has countless choices that will effect their playthrough and the final ending. The various playthrough will let users play the game multiple times to discover all of the possible scenarios.

### Input

- Throughout the game various input is available, the player gets detailed directions on which choices they can choose and all inputs will accept variety of inputs as correct answer, to make choices easier, the player can input single letters as y/n/a/b/c/d but also has available key words that can be accepted.
- Each input field is supplied with a prompt in case user wants to end the game or check the scoreboard

#### End/Restart
- By typing in "end" inside the input field the game will run a restart choice function that lets user either restart the game from the beginning with all settings and variables being set to initital state, or to end the game completely which force quits the program.

#### Scoreboard/Progress Board
- By typing in either "progress" or "score" inside the input field the game will use previously extracted score values from the google sheets as variables vicims_data and survivors_data and display the last 5 entries for each as a scoreboard entries.

### Health

- The player starts with the full health at 100, if a user makes a wrong choice at the start and injure themselves they will lose 20 points with each step they make. 
- To heal the wound the player will need to reach the Med Bay and undergo a healing procedure.

### Navigation error

- The player will have an opportunity to discover a navigational error that is throwing the ship off course and they need to fix it.
- The player will have 5 steps to reach the navigation panel on the outside of the ship, otherwise the ship will enter an asteroid field and be destroyed.

### Ways to die

- Electrical cord - player makes a wrong choice and gets electricuted
- Health - player takes damage and doesn't reach Med Bay to be healed
- Navigation Error - player doesn't fix the navigation system and the ship steers off course and explodes in asteroid field
- Forceful Healing - player refuses to be healed by the regeneration machine and gets killed in the process
- Elevator Collision - The user decides to use the old elevator and falls to their death
- Freeze in Space - player forgets to put on the space suit and dies by freezing

### Ways to survive

- Escape Pod - player uses an escape pod and saves themselves, leaving the fellow travellers behind.
- Save Everyone/master reboot -player uses reboot code provided at the start of navigational error and save all travellers and continue on your way
- Save Everyone/system bypass - player bypasses the error and restores power to navigational panel, which causes the direction to change and send the ship and it's travellers onto the unknown path

### Open ending

- If player survives the game, they get an open ending message, leaveing space for any updates, expansions and possible sequels to the story

### Features left to implement

- separate handler if user doesn't activate bleeding or navigation error, but puts on a space suit before exiting the spaceship. Missing ending handling

***Future features:***
- More ASCII art
- Expand possible endings, especially surviving endings
- Add more backstory and post saving the ship storyline
- Discovery of the shadow figure
- In debth exploration of each room on the ship
- Addition of new rooms
- Continuation to the mystery old computer story by adding games within game to it
- ...

## Testing

|           Action            |        Expectation                           | Outcome |
| :-------------------------: |   :-------------------------------------:    | :-----: |
|           Game start        |   The game starts when program is run        |  Pass   |
|      Terminal clears        |         Any old messages are cleared         |  Pass   |
|       ASCII image and sign  |         ASCII image loads properly           |  Pass   |
|       Username input        |  Username input shows, waits for input       |  Pass   |
|  Username input/whitespace  | If only whitespace is enetered- error msg    |  Pass   |
|  Username input/numbers     |  If only numbers are enetered- error msg     |  Pass   |
|  Username input -correct    |    If name is entered it lets user pass      |  Pass   |
|       Features message      |  Provide information on game features        |  Pass   |
|    Story information        |    Provide information on storyline          |  Pass   |
|          Input "end"        | Offers user a choice to restart or end game  |  Pass   |
|   Input "progress"/"score"  | Display the scoreboard of victims/survivors  |  Pass   |
|    Leave hibernation pod    | If "no" writes message and loops back again  |  Pass   |
|          Grab door          |      Gets away safely without any damage     |  Pass   |
|    Grab cord           |   Grabbed electical cord, got electricuted. Died  |  Pass   |
|      Risk fall      | starts bleeding effect on fall from hibernation pod  |  Pass   |
|   Input - answer      | Progresses through the story depending on choice   |  Pass   |
|    Control room  |   Can choose to explore or continue through the ship.   |  Pass   |
|  Examine control panel  | activates navigation error on explore selection  |  Pass   |
|    Continue past control panel    |    Continues the story with no error   |  Pass   |
|   Control room choice     |    can go to Cargo Hold or Engineering Bay     |  Pass   |
|    Cargo Hold  |  can explore or continue on to escape pods or engineering |  Pass   |
|    Escape Pods |  Can use escape pod or go back to cargo hold via old lift |  Pass   |
|    Escape   |    Saved themselves, left everyone else behind, Survived     |  Pass   |
|    Go back/old lift   |    The lift malfunctions and kills player, dead    |  Pass   |
|   Med Bay/not hurt    |  Gets scanned and nothing happens, story continues |  Pass   |
|  Med Bay/hurt/heal      |    Gets scanned, not wounded, healed, continue   |  Pass   |
| Med Bay/hurt/don't heal |    Scanned, wonded, refused heal, forced heal    |  Pass   |
|   Forced healing   |    Error occurs and the machine killes player, dead   |  Pass   |
|  Med Bay Path choice        |     can go to Library or Observation Deck    |  Pass   |
|     Explore Library  |  Looks around, finds open book, sees shadow person  |  Pass   |
| Explore Observation Deck |   Looks around, can go on or go back to Med Bay |  Pass   |
|    Engineering Bay    |    Can explore the engineering bay or continue     |  Pass   |
|   Explore engineering  |   Discovers a lot of nice and interesting stuff   |  Pass   |
|   Engineering continue  |       Can stay or continue into Airlock          |  Pass   |
|        Airlock      |        can choose to put on space suit or not        |  Pass   |
|   Space suit/not on  | Step into airlock, realise mistake but too late, died  |  Pass   |
|  Space suit/on  |  Step into airlock and exit outside the ship. Runs through scenario and ends if the navigation error is not active, otherwise continue. Survived |  Pass   |
|   Space suit/on nav. error    |  Continues the story and makes player choose to either fix navigation failure with reboot code provided at start or bypass system  |  Pass   |
|   Master Reboot   |    If reboot code correct, runs special ending scene, survived     |  Pass   |
|   System bypass  |    Runs the ending scene, without master reboot, future uncertain, survived     |  Pass   |
|   Restart on game end   |    Offers to restart the game from beginning     |  Pass   |


## Troubleshooting

- During the build process I encountered some errors that I managed to fix by watching some tutorials and looking up online issues I encountered.
- One of the issues I had as I started coding, was the fact that I didn't understand what do I need to put around my line of code if it is going into the second row, after a little bit of googling and searching I found out that all I had to do was wrap each line in "".
- I had an error with an infinite loop in control_room() which I corrected after discovering I haven't created a while loop correctly, as I forgot to input the break keyword in my if statements, so the output couldn't reach the control_room_choice_path() function outside the while loop
- I had couple of small errors due to not closing parentheses or the spacing being 4 spaces..
- I struggled and it took me quite a while, watching love sandwiches and looking up online to find a proper way to import and export the values to the and from the google sheets.
- Fixed error message that was showing up when scoreboard was accessed, the issue was happening because the input response was not connected as an elif statement variation, but as a separate if statement which was activating the else method everytime input was put in.
- Corrected the bleeding effect, by using a proper method of assignment, added a set_bleeding_state function to control whether the statement is True or False
- Added another message to error handler to print a message on how to access scoreboard.

### Unfixed bugs:

- As far as I am aware, there are no unfixed bugs.

## Validator testing

- I ran an internal testing using pycodestyle and no errors were returned or found.

## Deployment

### Create a list of requirements
- in terminal write command: pip3 freeze > requirements.txt
- requirements.txt is updated. 
- commit changes and push to github

### Login or Create account with Heroku
- Signup - fill out the form, as a role select student
- Confirm your email
- Login - enter login details

### Create new app
- select create new app button
- select the name, name has to be unique
- select region, Europe for me

#### Settings
- go to Config Vars: as key type in "CREDS"; for value copy the contents from creds.json file. Click Add button
- for second Config Var: the key will be "PORT" and the value needs to be "8000". Click Add button again
- go to buildpacks section, select Add buildpack button, select python, then repeat process and select NodeJS. First one needs to be Python and NodeJS second

#### Deploy
- go down to Deployment method section, select GitHub as a method
- copy the name of your repository, click on search button
- click on connect button to link up the repository
- scroll down to automatic deploys, select it to enable automatic deployment of any changes made to GitHub repository
- in Manual deploy section, click on Deploy Branch button.
- the app will run the logs while creating
- when the app is created the app was successfully deployed message and the  view button will appear
- the app is built, open the app and test it to make sure there are no errors.
- if connected correctly the data should be updated in the google spreadsheets.

## Credits

- Prior to starting with the project I watched multiple video tutorials for inspiration and guidance, some of which are:
- [Shaun Halverson](https://www.youtube.com/watch?v=ORsJn-71__0&t=90s)
- [LeMaster Tech](https://www.youtube.com/watch?v=u8X6TiJA8as&t=273s)
- [Dante Lee](https://www.youtube.com/watch?v=lI6S2-icPHE&t=144s)
- [Tech With Tim](https://www.youtube.com/watch?v=DEcFCn2ubSg&t=107s)
- [Programming with Mosh](https://www.youtube.com/watch?v=kqtD5dpn9C8)
- [Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=7s)
- [Tech With Tim](https://www.youtube.com/watch?v=p15xzjzR9j0)
- [Free Code Camp](https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=of%20the%20datetime.-,now()%20Function,second%20of%20the%20current%20date.)
- [CodeInstitute Lessons](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/58d3e90f9a2043908c62f31e51c15deb/)
- [Real Python](https://realpython.com/python-enumerate/)

- [Taylor Swift playlist](https://www.youtube.com/watch?v=IdneKLhsWOQ&list=PLMEZyDHJojxNYSVgRCPt589DI5H7WT1ZK) and countless hours of music playlists that kept me company


### Media

- The rocket image was taken from [TextArt](https://textart.sh/topic/rocket), and improved on to have desired design.
- The SpaceShip Adventure, The End and Scoreboard signs were created and taken from [TextArtGenerator](https://www.textartgenerator.net/)

### Content

- Few lines of code were taken from[StackOverflow](https://stackoverflow.com/questions/72047933/accessing-a-value-by-index-in-enumerate-for-loop)
- Starting steps and few lines of code came from  lessons and Love Sandwiches