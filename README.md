# Rotary Python Interpreter

[Rotary](https://esolangs.org/wiki/Rotary) is an esolang specification found on the [esolang wiki](https://esolangs.org)

The language is "purposefully confusing, lacks the relevant information and is fairly unreadable" and so I thought it would be nice to implement it

It is noted the creator was writing a Ruby interpreter; however, the language page hasnt been updated since 2015. The language just being a specification could mean this the only implementation?

*NB:* Since not all information for this language is available, I have made some of my own guesses sufficed only that cat.rot can run.

#  Running the Interpreter
## Command line:

run: `python3 rotary.py <filelocation>`

## Code Examples:

The interpreter comes with the following files in `/examples/`:
```
helloworld.rot - by Elisia:
---------------------------
A Basic Hello World program inspired by the brainfuck implementation
```

```
truthmachine.rot - by Elisia: 
-----------------------------
A truth machine is a challenge devised by User:Keymaker of esolang wiki

1) it must accept user input
2) it prints one 0 if 0 is entered
3) if 1 is entered it prints one 1 infinitely
```

```
cat.rot - by anonymous::esolangswiki / Elisia:
--------------------
cat.rot is the only program known originally listed for this language 

It is: `A program which copies its input to its output; loops infinitely.`

(My version adds newlines to make the output look nicer)
```

# The Language
## Structure
Each program includes:
1) INPP - Input Pointer -> The tape location for next input
2) OUTP - Output Pointer -> The tape location for next output
3) CIRP - Circle Pointer -> The current circle being run
4) TAPE -> A (pseudo) infinite tape of values
5) STACK -> A stack of values

## Rules:
- All code must be contained within a codecircle (34 tokens in size)
- The codecircles run counterclockwise starting from the third token along the top row
    - `!!!x!!` for example, where x is the first token
- Codecircles must be structured exactly as **below** and have a one line gap between them
- Any tokens outside of the circle will halt the program from running


```     
Here is an example of a NOP circle:

     !!!!!!
  !!!      !!!
 !            !
!              !
!              !
!              !
 !            !
  !!!      !!!
     !!!!!!
```

## List of Instructions:

| Instruction 	| Function                                                                                                  	|
|-------------	|-----------------------------------------------------------------------------------------------------------	|
| >           	| Move the INPP right                                                                                       	|
| <           	| Move the INPP left                                                                                        	|
| /           	| Move the OUTP right                                                                                       	|
| \           	| Move the OUTP left                                                                                        	|
| +           	| Increase the value in the cell under the INPP                                                             	|
| -           	| Decrease the value in the cell under the INPP                                                             	|
| .           	| Output the data in the cell under the OUTP as an 8-bit (0-255) character                                  	|
| ,           	| Get character input and insert the character's decimal representation into the cell under the INPP        	|
| v           	| Increase the circle pointer (*)                                                                           	|
| ^           	| Decrease the circle pointer (*)                                                                           	|
| #           	| Output the data in the cell under the OUTP as a number                                                    	|
| ?           	| Execute the next instruction if the cell under the OUTP is 0, else do nothing (**)                        	|
| *           	| Execute the next instruction if the cell under the OUTP is not 0, else do nothing (**)                    	|
| $           	| Push the value of the cell under the OUTP to the stack                                                    	|
| ~           	| Pop a value off the stack into the INPP; pops 0 if the stack is empty                                     	|
| @           	| Rotate the stack (top becomes bottom)                                                                     	|
| !           	| NOP (do nothing)                                                                                          	|
| r           	| Replace the cell under the INPP with a pseudo-random number between 0 and 255                             	|
| s           	| Pop a number 'n'; then output each cell from OUTP+1 to OUTP+n as a character (***)                        	|
| %           	| Pop a number 'n'; then push > (***)                                                                       	|
| x           	| Pop a number 'n'; then set the circle pointer to that number, ie. jump to the n-minus-one-th circle (***) 	|

