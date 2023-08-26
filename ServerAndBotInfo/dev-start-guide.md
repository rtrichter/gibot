# Getting Started With Gibot Development

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
