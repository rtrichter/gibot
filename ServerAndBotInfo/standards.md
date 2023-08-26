# Standards for the Gibson Discord Server Project

1. Follow [pep-8](https://peps.python.org/pep-0008/) when writing python code  
2. File naming: snake_case (always include extensions even if your OS doesn't require it).  
ie. "server_overview.md"
3. Folders use CamelCase.  
ie. ServerAndBotInfo  
Using different standards for files and folders make them easier to tell apart in the command line  
Some exceptions (like README.md and .gitignore are fine)
4. Everything should be an independent subsystem if possible.  
This make the code easier to develop and maintain, prevents conflicts between developers working on different subsystems, and more. Just make subsystems.  
(Subsystems should be split into files that are combined into a module and included by a main file)
5. 