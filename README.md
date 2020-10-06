# Garter
A simple and harmless Python-based computer virus capable of infecting nearby Python files and executing a specific payload.

Anyone is welcome to use code from this repository, but know that I am NOT responsible for any damage done by any modified versions of the code. This repository is for **educational purposes only**.

Note that this code is still in a very early development phase, and as such some functionality is not available. Check back later for improvements.

## To-Do List
- ~~Define the self-replicating region rigidly~~
- ~~Add code so file can read itself and replicate a specific part of the code in other target files~~
- Add a discrete payload section so that users can add an effect to the code on top of self-replication
- Optimize the replication process, as it currently requires storing the entire target file in memory, making larger files harder to infect
- Add a feature to test if files are already infected
- Adjust the code to infect ALL nearby files as opposed to just one arbitrary target
- Add a default payload?
- Add some sort of CLI feedback indicating successful infection?
