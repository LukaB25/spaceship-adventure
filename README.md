# [SpaceShip Adventure](https://github.com/LukaB25/spaceship-adventure)

## Introduction

- The SpaceShip Adventure is a text based game that was inspired by "retro" games of similar style
- The SpaceShip Adventure is targeted to all of the fans of text based games that are on a quest for a new adventure
- The SpaceShip Adventure offers it's users a fun and interactive adventure that plays out the outcomes depending on their choices.
- There are multiple ways to survive, but also to die. The game will keep track of all of the users and the progress they made by storing the data inside of google sheets.

## Wireframes - [Lucid](https://lucid.app/)
![Lucid basic game progress mind map](images/lucid_mind_map.avif)
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
![ASCII Rocket image and SpaceShip Adventure logo sign](images/lucid_mind_map.avif)
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

## Troubleshooting

- During the build process I encountered some errors that I managed to fix by watching some tutorials and looking up online issues I encountered.
- One of the issues I had as I started coding, was the fact that I didn't understand what do I need to put around my line of code if it is going into the second row, after a little bit of googling and searching I found out that all I had to do was wrap each line in "".
- I had an error with an infinite loop in control_room() which I corrected after discovering I haven't created a while loop correctly, as I forgot to input the break keyword in my if statements, so the output couldn't reach the control_room_choice_path() function outside the while loop
- I had couple of small errors due to not closing parentheses or the spacing being 4 spaces..
- I struggled and it took me quite a while, watching love sandwiches and looking up online to find a proper way to import and export the values to the and from the google sheets.

### Unfixed bugs:

## Validator testing

### Performance

## Deployment

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

### Content

