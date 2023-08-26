# Gibot Docs
KEEP THESE UPDATED PLEASE!!!!  
Pull requests will not be accepted without documentation.  
Documentation ensures that another developer can understand and maintain your code


## Loops and Background Tasks
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