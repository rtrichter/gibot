# Gibot
RIT Gibson Hall Discord Server! (not affiliated with RIT)  
This readme includes information about the Gibson Hall server in addition to Gibot info

# TOC
- [Hosting the Bot](#hosting-gibot)
- [Getting Started with Developing Gibot](#getting-started-with-developing-gibot)
- [Architecture](#architecture)
- [Blacklisting](#blacklisting)
- [Roles](#roles)
- [Interests](#interests)
- [Information](#info)
- []

## Hosting Gibot
A temporary solution is that I can host the bot locally from my desktop PC in my dorm.  
I don't want this to be a permanent solution though because I would like to be able to turn off my PC, move it when I go home for holidays, etc. 

## Getting Started with Developing Gibot
1. Clone the repository "git clone https://github.com/ryanrichter028/gibot"  
2. Set your config information:  
`git config --local user.name "YOUR_NAME"`   
`git config --local user.email "YOUR_EMAIL"`  
NOTE: using local is to ensure that you don't affect your other repositories.  
Using global will likely affect other repos and I personally don't want to change all of my repos to my RIT email and I don't want to share my personal email.  
This info is in case anyone has questions about someone else's changes, we can find who made that change. 
3. For development we will use a "test_token" to prevent possible leaks of the primary token of Gibot.   
How development testing will work is not yet defined.  
I expect to have each developer responsible for making their own test bot and test server, however I am not yet sure
4. Remember to do good git things and don't do bad git things.  
Use branches. Don't make a pull request to main. Stuff like that.  
If you don't know how git works go learn before you start developing and ask questions when you need to.  
I'd rather answer a question that you might think is stupid than have to fix a problem down the road.  

## Architecture  
Systems should be divided into subsystems

## Roles
- [Colors](#colors)
- [Floor](#floor)


### Colors:
The server contains several standard colors that can be assigned via a reaction role system  
The colors we will use are:
- red

**The Rainbow Role:**  
Rainbow Role relies on Gibot.  
Rainbow Role uses a role just like the other color roles
Every hour, Gibot will run a command that assigns a random color to the rainbow role. 

### Floor
Members can assign a number that represents their floor number
This is limited to one of the roles at a time

### Interests
Members can choose certain interests that they like to partake in  
This is a high level branch system:
1. The first layer separates interests like "music", "art", "video games", "athletics", etc
2. The second layer will further divide these interests.  
For example athletics can be split into 

## Info
This gives members an option to store and share their information with other users.  
 
By storing information (such as real name, email, phone number, room number, etc).  

All information stored is optional.  
Any member can opt out of having their information shared if they choose to store it.  
Any information can be deleted at any time
