# Reactions


## What is the goal of reactions?
Allow for simple creation of reaction commands.  

## What are the types of reaction commands.  
First lets define a few things:  
- There are different execution schemes (what happens when the user interacts)
- There are different usage types (How the user interacts)

The command used will be named after the execution scheme.  
For example you will use one command to make a reaction_role and another to make a poll.  

## Execution Schemes
- Polls (There will be further subdivisions of polls too)
  - Options:
    - message_id
    - reaction
    - \# of chances
    - is_blind
  - One chance voting (allow a user to see what their response was)
  - Most recent voting
  - Blind voting (for either option)
- Reaction Roles
- 




# ok i'm gonna slow down a little...
I will go back and elaborate on the previous definitions but for now let's focus on reaction roles.  
I need to make sure that I can do one thing before I make a plan for everything (find out what works, what doesn't, how it works, etc. )


How to store the function and arguments?

Add a func and kwargs member to the ReactionCommand object
func will end up being the execution scheme.  
The usage scheme will ALWAYS be passed to the execution scheme function

For exmaple: (for reaction role)  
kwargs = {"role_id": 0}
func = reaction_role_execution_scheme(usage_scheme, role_id)


# The stuff above this isn't working... 
I got ahead of myself and started coding so I'm going to go back and plan more.  

# Execution Schemes
These are the functions that will run when a reaction command is activated (when someone reacts)

There is no reason to have a ReactionCommandGroup.  
The only advantage would be having more than one execution/usage type on a given message but many of the usage types that are in my head will rely on all of the commands associated with a message being the same execution/usage type.  

Each execution type will have its own class (this may be refactored to use inherited subclasses but to start I will just code the reaction roles part)

# What moderation tools should a reaction role command have?
1. init (message_id, usage_scheme) maybe later init can be used to specify execution_scheme and then you can edit any reaction command using the same commands
This will make a message available to have roles associated with specific reactions
2. add  (message_id emoji, role)  
This will add a reaction role to the message
3. rm  (message_id, emoji)  
This will remove a reaction role when given a message_id and emoji
4. reset  
delete an entire set of reaction roles