# Gibot Docs
KEEP THESE UPDATED PLEASE!!!!  
Pull requests will not be accepted without documentation.  
Documentation ensures that another developer can understand and maintain your code

# TOC


## Hikari things...
[This guy has some super helpful tutorials](https://www.youtube.com/@Carberra)
[Hikari (bot api) docs](https://docs.hikari-py.dev/en/latest/)
[Lightbulb (command handler) docs](https://hikari-lightbulb.readthedocs.io/en/latest/index.html)


## File Structure
GibotPy
|---extensions  
|------\_\_init\__.py  
|------rainbow_role.py  
|---utils  
|------\_\_init\__.py  
|------config.py  
|---\_\_init\__.py  
|---\_\_main__.py  
|---bot.py  

From what I can tell now there should be nothing other than \_\_main__, \_\_init__, and bot.py in the top-level package.  
Everything else should be in utils or extensions (or maybe a plugin directory but I haven't learned how those work yet. Hopefully I remember to update this when I do find out how they work)

## Extensions
Extensions are used to keep our code organized.  
Think of an extension as a file that contains a set of features.  
Packages are ok if you are working with a large set of _related_ features. Unrelated features should remain in their own files.  
(For example everything related to reaction handling will likely be handled in either one file or one package depending on the level of organization necessary)

### Rules for Extensions: 
All extensions must include an initialize() function.  
This may not be necessary by hikari's standards HOWEVER, some files may require an initialization and for consistency I would like to have one in every extension.  
This will make debugging easier. You can check if an extension was initialized by checking the part of \__main__ that contains all extension initializations.  
This also forces whoever develops an extension to thoroughly check all of their code is being initialized properly.  
Some features will initialize themselves (for example tasks have an autostart parameter that we DO NOT USE). Explicit initialization of the tasks is important for the reason above. 
It will be easier to check for all initializations in one place rather than checking each function for their auto_start parameter. 
Additionally, include a print statement that indicates that the function was run. 

This explanation may have been confusing but feel free to ask questions about it. The general idea is don't rely on hikari to automatically start anything unless it does so by default.  

All of this will help to prevent imports from not being accessed, it will make debugging easier, and will make all extensions consistent with each other.  

## \_\_main__.py
First, import bot.py from the top level package. This will run at the end of this file.  
Next, import and initialize all extensions.  (maybe plugins too but idk yet)  
Finally, run the bot. This is protected so that it only runs if you run the GibotPy package.  
If you ever need any of this code for your own project you could import the package without running anything related to Gibot.  

## bot.py
The token is kept in a separate file to keep it secret. Eventually we will have a better method of distributing a test token on a test server.  
After getting the token, we load the bot.  
Then load the tasks. (honestly I'm not sure what exactly this does but its needed for tasks)  

Then we have a command and a listener that can be used to ensure that the bot is working properly if something else is going wrong.  
/say will just echo whatever you tell it to say in the text option  
ping will send pong to the channel that you send the ping in (when you ping @Gibot)  

Finally, we define the run function (which is run from \_\_main__.py).  

## rainbow_role.py
using lightbulb.ext.tasks to schedule the change_rainbow_color() function.  
Repeats every hour  

### change_rainbow_color()
1. gets colors from config
2. gets a new random color (repeats until the random color is different from the previous color)
3. edit the rainbow role's color

### initialize()
Starts the rainbow role task


## config.py
Makes it easier to load stuff from Data/config.json

### get_config(key)
use get_config and pass the key from config.json that you are looking for.  






## token and run
The token is stored in a separate file so that it will not be shared through the source code.  
The token will only be available to the owner of the bot, who must add the token file to any deployed instance of the bot.  
(My plan is to make a development server that is a clone of the main server, any developer can load their own bot with their own token into that server for testing)  
(Hopefully we can automate loading templates in case the dev server ever needs to be reset)