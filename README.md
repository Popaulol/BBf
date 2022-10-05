# BBf (Better Brainfuck)

BBf is a esoteric Programming Language created in 2022 by Staubfinger aka. Staubcoding aka. Popaulol.
It is meant to be a more powerful version of [brainfuck](https://esolangs.org/wiki/Brainfuck) with support for arbritary syscalls and more.
Its name is the acronym for `Better Brainfuck`.
It *should* run any valid Brainfuck Program, that doesn't contain any of the characters used by the language for its own pourpuses.

## Instruction Set
**DISCLAIMER: This is by no means final**

The Instruction set is the same as regular brainfuck with a multitude of added features and commands.
In Addition to the standard bf Tape, this language adds 6 registers, ABCDEFG, used for the syscall command and for a bit simpler Storage.
They are named ABCDEFG.

| instruction | available in standard brainfuck | Explenation 
|-------------|---------------------------------|-------------
| >           | &#9746;                         | Move the pointer to the right
| <           | &#9746;          	            | Move the pointer to the left
| +           | &#9746;          	            | Increment the memory cell at the pointer
| -           | &#9746;          	            | Decrement the memory cell at the pointer
| .           | &#9746;          	            | Output the character signified by the cell at the pointer
| ,           | &#9746;          	            | Input a character and store it in the cell at the pointer
| [           | &#9746;          	            | Jump past the matching ] if the cell at the pointer is 0
| ]           | &#9746;           	            | Jump back to the matching [ if the cell at the pointer is nonzero
| #           | &#9744;                         | Output the value of the cell at the pointer as a Base 16 Integer
| A           | &#9744;                         | Put the value inside the cell at the pointer into register A
| B           | &#9744;                         | Put the value inside the cell at the pointer into register B
| C           | &#9744;                         | Put the value inside the cell at the pointer into register C
| D           | &#9744;                         | Put the value inside the cell at the pointer into register D
| E           | &#9744;                         | Put the value inside the cell at the pointer into register E
| F           | &#9744;                         | Put the value inside the cell at the pointer into register F
| G           | &#9744;                         | Put the value inside the cell at the pointer into register G
| a           | &#9744;                         | Load the value from register A into the cell at the pointer
| b           | &#9744;                         | Load the value from register b into the cell at the pointer
| c           | &#9744;                         | Load the value from register c into the cell at the pointer
| d           | &#9744;                         | Load the value from register d into the cell at the pointer
| e           | &#9744;                         | Load the value from register e into the cell at the pointer
| f           | &#9744;                         | Load the value from register f into the cell at the pointer
| g           | &#9744;                         | Put the value inside the cell at the pointer into register G
| \|          | &#9744;                         | Put the Position of the pointer into register A
| ^           | &#9744;                         | Move the pointer to the Cell indicated by register A
| (           | &#9744;              	        | Jump past the matching ) if the cell in register A is 0
| )           | &#9744;              	        | Jump back to the matching ( if the cell in register A is nonzero
| {           | &#9744;                         | Starts a function (function are explained a bit later in this Document)
| }           | &#9744;                         | Ends a function (function are explained a bit later in this Document)
| !           | &#9744;                         | Calls the function with the ID represented in the cell at the pointer by using local lookup
| ?           | &#9744;                         | Calls the function with the ID represented in the cell at the pointer by using global lookup
| ~           | &#9744;                         | Calls the function with the ID represented in register A by using local lookup
| %           | &#9744;                         | Calls the function with the ID represented in register A by using global lookup
| $           | &#9744;                         | Invokes a (linux/unix) syscall with the ID represented by the cell at the pointer with the six arguments being the registers A through F
| &           | &#9744;                         | Store a pointer to the Cell currently pointed at bei the Pointer into A
| *           | &#9744;                         | Derefence the pointer stored in A onto the current place on the Tape

### Functions
Functions are a construct made for code reuse but since this is meant to be an esolang though a not so hard one, functions come with a bit of a caveat.
A Function is a collection of instuctions inside curly braces. Every function gets a numeric ID starting with 0, depending on the order they are defined in.
When local functions are created they will override the Function IDs starting at 0 again but you are still able to access functions on the global level using the `?` and `%` instructions.
If a empty function `{}` is written, it will increment the counter of current functions but won't override the function at the current value.
Calling a undefined function should yield a runtime error.

### Pointers
The two pointer instructions `&` and `*` shold only be used for interaction with the operating system, since BBF only satisfies a few things in regards to them. Pointers generated by `&` are only garanteed to be valid until are read or write happens to location on the tape that has never been written or read before. When passing pointer to the operating system, you will have to make sure yourself, that any location it may read or write from is an "initialized location" that means some sort of read or write from you code has to have been performed on it. Cells are guranteed to be exactly 1 byte big and arranged next to each other in memory without padding. You can increment or decrement pointers to move around inside the tape.

### Syscalls
When the syscall instruction § is invoked it will call the syscall with the ID in the A register followed by the Arguments 6 for the registers B through G.
When the syscall expects a pointer anything, you will have to create a pointer using the & instruction. Since Cells are garanteed to be 

## Contributions

Pull requests and Issues are very appriceated.
But be aware that I might reject a PR for Any Reason, especially if it comes to adding features.
