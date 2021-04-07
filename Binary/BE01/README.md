# BE01 - 100pts

## Briefing

> Download the file and find a way to get the flag. Contents: chicken.pdf

Challenge Files:

* [be01.zip](./be01.zip)

## Solution

1. First, extract the PDF as a ZIP file. Depending on the extraction tool used, you might need to rename the file so it has a `.zip` extension: `chicken.zip`.

2. Extract the `egg.zip` inside and repeatedly extract the inner ZIP files until you get `egg.pdf`, which contains the flag.

3. The final path of the `egg.pdf` file is `be01/chicken/egg/chicken/egg/chicken/egg.pdf`.

### Flag

`wh1ch_came_f1rst?`
