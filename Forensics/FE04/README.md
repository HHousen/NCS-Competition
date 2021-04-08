# FE04 - 100pts

## Briefing

> Download the file and filter down to the username according to criteria below. The username you are looking for has `x` as the 3rd character, followed immediately by a number from `2` to `6`, it has a `Z` character in it and the last character is `S`. When you have the username, submit it as the flag. Contents: 50k-users.txt

Challenge Files:

* [fe04.zip](./fe04.zip)

## Solution

1. This is a simple data processing challenge that can be solved with a little Python and a basic regular expression.

2. The regular expression is `..x[2-6].*S$` and can be built and tested easily using [RegExr](https://regexr.com/). The first two dots match any character, next the `x` matches an `x`, `[2-6]` matches a number from 2 to 6 inclusive, a dot again can match any character and the star `*` modifies the dot so that an unlimited number of any character can be matched. Finally, the `S` matches an `S` and the `$` ensures that this marks the end of the string being checked. We will handle the "it has a `Z` character in it" criteria later.

3. We can test every username in the `50k-users.txt` file against the regular expression we built using Python. We compile the regular expression and then use `filter` to test it against every username. We then filter all the matches again by checking if they contain a `Z`, thus fullying applying the challenge criteria. The final matching username is printed and is the flag.

### Flag

`YXx52hsi3ZQ5b9rS`
