# BBf (Better Brainfuck)

BBf is a Esotheric Programming Language created in 2022 by Staubfinger aka. Staubfcoding aka. Popaulol.
It is meant to be a more powerful version of [brainfuck](https://esolangs.org/wiki/Brainfuck) with support for arbritary syscalls and more.
Its name is the acronym for `Better Brainfuck`.
It *should* run any valid Brainfuck Program, that doesn't contain any of the characters used by the language for its own pourpuses.

## Instruction Set´
**DISCLAIMER: This is by no means final**

The Instruction set is the same as regular brainfuck with a multitude of added features and commands.
In Addition to the standard bf Tape, this language adds 6 registers, ABCDEF, used for the syscall command and for a bit simpler Storage.
They are named ABCDEFG.

| instruction | available in standard brainfuck | Explenation 
|-------------|---------------------------------|-------------
| >           | :heavy_check_mark:              | Move the pointer to the right
| <           | :heavy_check_mark:	            | Move the pointer to the left
| +           | :heavy_check_mark:	            | Increment the memory cell at the pointer
| -           | :heavy_check_mark:	            | Decrement the memory cell at the pointer
| .           | :heavy_check_mark:	            | Output the character signified by the cell at the pointer
| ,           | :heavy_check_mark:	            | Input a character and store it in the cell at the pointer
| [           | :heavy_check_mark:	            | Jump past the matching ] if the cell at the pointer is 0
| ]           | :heavy_check_mark: 	            | Jump back to the matching [ if the cell at the pointer is nonzero
| #           | :white_check_mark:              | Output the value of the cell at the pointer as a Base 16 Integer
| A           | :white_check_mark:              | Put the value inside the cell at the pointer into register A
| B           | :white_check_mark:              | Put the value inside the cell at the pointer into register B
| C           | :white_check_mark:              | Put the value inside the cell at the pointer into register C
| D           | :white_check_mark:              | Put the value inside the cell at the pointer into register D
| E           | :white_check_mark:              | Put the value inside the cell at the pointer into register E
| F           | :white_check_mark:              | Put the value inside the cell at the pointer into register F
| G           | :white_check_mark:              | Put the value inside the cell at the pointer into register G
| a           | :white_check_mark:              | Load the value from register A into the cell at the pointer
| b           | :white_check_mark:              | Load the value from register b into the cell at the pointer
| c           | :white_check_mark:              | Load the value from register c into the cell at the pointer
| d           | :white_check_mark:              | Load the value from register d into the cell at the pointer
| e           | :white_check_mark:              | Load the value from register e into the cell at the pointer
| f           | :white_check_mark:              | Load the value from register f into the cell at the pointer
| g           | :white_check_mark:              | Put the value inside the cell at the pointer into register G
| \|          | :white_check_mark:              | Put the Position of the pointer ito register A
| ^           | :white_check_mark:              | Move the pointer to the Cell indicated by register A
| (           | :white_check_mark:	            | Jump past the matching ) if the cell in register A is 0
| )           | :white_check_mark: 	            | Jump back to the matching ( if the cell in register A is nonzero
| {           | :white_check_mark:              | Starts a function (function are explained a bit later in this Document)
| }           | :white_check_mark:              | Ends a function (function are explained a bit later in this Document)
| !           | :white_check_mark:              | Calls the function with the ID represented in the cell at the pointer by using local lookup
| ?           | :white_check_mark:              | Calls the function with the ID represented in the cell at the pointer by using global lookup
| &           | :white_check_mark:              | Calls the function with the ID represented in register A by using local lookup
| %           | :white_check_mark:              | Calls the function with the ID represented in register A by using global lookup
| §           | :white_check_mark:              | Invokes a (linux/unix) syscall with the ID represented by the cell at the pointer with the six arguments being the registers A through F

### Functions
Functions are a construct made for code reuse but since this is meant to be an esolang though a not so hard one, functions come with a bit of a caveat.
A Function is a collection of instuctions inside curly braces. Every function gets a numeric ID starting with 0, depending on the order they are defined in.
When local functions are created they will override the ID's starting at 0 again from the outer function scope but you are still able to access functions on the global level using the = and % instructions.
If a empty function {} is written, it will increment the counter of current functions but won't override the function at the current value.
Calling A undefined function should yield a runtime error.

### Syscalls
When the syscall instruction § is invoked it will call the syscall with the ID in the A register followed by the Arguments 6 for the registers B through G.
When the syscall expects a pointer to a struct, you can pass the Address of a cell on the Tape, which will then be treated as a pointer. If its meant to be a string it will just read the characters one cell at a time starting from the specified one. If there is an explicit count it will stop there otherwise it will go to the next cell containing 0.
The way structs will be handled will be defined later.

## Contributions

Pull requests and Issues are very appriceated.
But be aware that I might reject a PR for Any Reason, especially if it comes to adding features.
