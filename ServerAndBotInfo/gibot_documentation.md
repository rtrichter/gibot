# Gibot Docs
KEEP THESE UPDATED PLEASE!!!!  
Pull requests will not be accepted without documentation.  
Documentation ensures that another developer can understand and maintain your code

# TOC
- [rainbow_role.py](#rainbow_rolepy)
  - [previous_color](#previous_color)
  - [rainbow_role_update()](#rainbow_role_update)
  - [rainbow_role_update_loop()](#rainbow_role_update_loop)
- [constants.py](#constantspy)
  - [DATA](#data)
  - [get_config](#get_config)
  - [get_role](#get_role)
- [bot.py](#botpy)
  - [intents](#intents)
  - [bot](#bot)
  - [guild](#guild)
- [\_\_main\_\_](#__main__py)
  - [on_ready()](#on_ready)
  - [token and run](#token_and_run)

# rainbow_role.py
### previous_color
previous_color stores an integer associated with the hex value of a color  
When a new color is selected, we check against the previous color to ensure that the color changes every time [rainbow_role_update](#rainbow_role_update) runs  

### rainbow_role_update()
definition:
```python
async def rainbow_role_update():
```

Usage:  
This function will change the color of the rainbow role.  
This function should not be called frequently!  
Discord will rate limit the bot if this function runs too often.  
For safety, do not call this function other than a SINGLE instance of the [rainbow_role_update_loop()](#rainbow_role_update_loop)  

Details:
The same color will never be selected twice in a row  

### rainbow_role_update_loop()
definition:
```python
async def rainbow_role_update_loop()
```

Usage:
This function is a wrapper for [rainbow_role_update()](#rainbow_role_update).  
The function will ensure that rainbow_role_update() runs periodically (at intervals defined by config.json -> rainbow_role_update_period_s)

Details:
This function should only be called ONCE!!!
Running the update too often will result in rate limiting of the bot

# constants.py
### DATA
A path to the Data directory

### get_config()
definition:
```python
def get_config(key: str):
```
Parameters:
key: str -> name of the key in config.json that you wish to retrieve

Return Value:
The value stored at the key passed to the function in config.json

Usage:  
pass in a key and get the config value for that key.  

### get_role()
NOTE: I expect this function to change at some point but its usage should remain the same. (only the internals change, but input and output remain the same)
definition:
```python
def get_role(guild, role_name: str) -> discord.Role:
```

Parameters:
guild -> a discord.Guild object, because Gibot only uses one server this is the guild defined in __main\__.py and bot.py
name: str -> name of the role that you wish to access

Return Value:
discord.Role object 

Usage:
Pass the guild and name of the role you would like to get to receive a discord.Role object  
Roles must be loaded into config.json -> role_ids to be accessed using this function

# bot.py
### intents  
contains the intents given to Gibot (currently using Intents.all(). This may change)
### bot  
used for pretty much everything. This is how you access servers, members, roles, etc.  
For those who have used discord.Client before, this is an extension of client. All functionality available to clients are available to bot. 
### guild  
Contains information about the server.  
It is initially assigned to None and updated in on_ready in __main\__.py

### Loops and Background Tasks
Honestly idk what happened with loops.  
I tried to get them working for a few hours and ended up giving up on them.  
discord.py has built in task scheduling but I couldn't get it working.  
Instead, I decided to use a recursive structure to keep loops running:  
Write a wrapper function for any task. Here is an example:
```python
async def rainbow_role_update_loop():
    # wait until the bot is ready
    await bot.bot.wait_until_ready()

    rainbow_role_update()

    # delay until the next loop
    await asyncio.sleep(constants.get_config("rainbow_role_update_period_s"))
    # idk what's going on with the loops so after the 
    # delay just call the function again
    # IMPORTANT!!! Call the wrapper NOT the function being wrapped
    await rainbow_role_update_loop() 
```

# \_\_main\_\_.py
## on_ready()
Runs after the bot is initialized  
1. Print to the console to indicate that the bot is ready
2. update the guild defined in bot.py
3. start any loops

## token and run
The token is stored in a separate file so that it will not be shared through the source code.  
The token will only be available to the owner of the bot, who must add the token file to any deployed instance of the bot.  
(My plan is to make a development server that is a clone of the main server, any developer can load their own bot with their own token into that server for testing)  
(Hopefully we can automate loading templates in case the dev server ever needs to be reset)