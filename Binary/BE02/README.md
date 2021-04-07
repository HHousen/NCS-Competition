# BE02 - 100pts

## Briefing

> Download the file and find a way to get the flag. Contents: rot13

Challenge Files:

* [be02.zip](./be02.zip)

## Solution

1. We could decompile the binary using Ghidra to understand how it works, but trial and error is faster for this challenge.

2. Sending a large number of characters as input (a >32 character string) causes a segmentation fault and prints the flag.

3. We can use 33 `a`'s as input to get the flag: `python -c "print('a'*33)" | ./rot13`.

### Flag

`luckyNumber13`
