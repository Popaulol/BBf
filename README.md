# BBf (Better Brainfuck)

BBf is a Esotheric Programming Language created in 2022 by Staubfinger aka. Staubfcoding aka. Popaulol.
It is meant to be a more powerful version of [brainfuck](https://esolangs.org/wiki/Brainfuck) with support for arbritary syscalls and more.
Its name is the acronym for `Better Brainfuck`.
It *should* run any valid Brainfuck Program, that doesn't contain any of the characters used by the language for its own pourpuses.

## Instruction Set

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

<!-- TODO: Add the new Instructions -->

## Contributions

Pull requests and Issues are very appriceated.
But be aware that I might reject a PR for Any Reason, especially if it comes to adding features.
