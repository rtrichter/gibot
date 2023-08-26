# Standards for the Gibson Discord Server Project

1. Follow [pep-8](https://peps.python.org/pep-0008/) when writing python code (close enough is good enough. Don't worry about it being perfect) 
2. File naming: snake_case  
(always include extensions even if your OS doesn't require it).  
ie. "server_overview.md"
3. Folders use CamelCase.  
ie. ServerAndBotInfo  
Using different standards for files and folders make them easier to tell apart in the command line  
Some exceptions (like README.md and .gitignore are fine)
4. Everything should be an independent subsystem if possible.  
This makes the code easier to develop and maintain, prevents conflicts between developers working on different subsystems, and more. Just make subsystems.  
(Subsystems should be split into files that are combined into a module and included by a main file)
5. 



## Units
When making variable names, always append the units as a suffix  
Use common abbreviations when possible. If the units don't have a common abbreviation, add them here



### Units Chart
Notice that metric prefixes are allowed on unit suffixes
Avoid uncommon metric prefixes. (milli (m), nano (n), micro (u), kilo (K), mega (M), giga (G), tera (T), peta (P))  
| Unit | Suffix | Example | 
| ---- | ------ | ------- | 
| seconds | _s | loop_period_ms | 
| minutes | _min | command_slow_mode_limit_min |
| Byte | _B | max_storage_space_GB |


