Symbolfuck
a programming language

This is a modified version of brainfuck, but with just add some more syntax and change all syntax to symbolsax
version: 1062020
syntax:
! will make the cell the poniter is pointing to increase 1
@ will make the cell the poniter is pointing to decrease 1
$ will make the poniter go left
# will make the poniter go leftright
& will get the input and assign it to the cell that the pointer is pointing at
* will output the value of the cell that is being pointed as a character
? will make a new cell
; will delete the cell that the pointer is pointing at cell
/ will make the pointer go to the first cell
' will make the pointer go to the last cell
