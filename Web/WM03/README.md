# WM03 - 250pts

## Briefing

> Visit the site at <https://cfta-wm03.allyourbases.co> and find a way to bypass the password check.

## Solution

1. The source code for the HTML index has a PHP snippet that shows how the site validates the password:

    ```php
    <!--
    TODO: remove, taken from OSS project, login contains:
    -->
    return function ($event) {
        require_once("flag.php");
        $hash = "0e747135815419029880333118591372";
        $salt = "e361bfc569ba48dc";
        if (isset($event['password']) && is_string($event['password'])) {
            if (md5($salt . $event['password']) == $hash) {
                return $flag;
            }
        }
        return "Incorrect";
    };
    ```

2. I tried bruteforcing the salt and hash using `hashcat`, but that did not succeed.

3. The bug is that the hash of the salt and password is compared to the saved hash using `==` (double equals) instead of `===` (Triple equals). PHP interprets strings with only numbers and an `e` in them as float number format strings (numerical strings). If you use `==` in php, when you compare a number with a string or the comparison involves numerical strings, then each string is converted to a number and the comparison is performed numerically.

4. If we can find a password that when salted hashes to `0e` followed by only digits then when it is compared to the stored hash, it will evaluate to true. Both of the strings are converted to `0` when compared with `==`. If you want to compare them as strings, you should use `===` (strict comparison) instead. More info: https://stackoverflow.com/a/22140266

5. There might be a better way, but I simply wrote a bruteforce algorithm to try all the permutations of 8 ascii lowercase letters, prepend the salt, hash the string, and then check if the hash starts wth `0e` and contains only digits after that. It took about 3 minutes 30 seconds to find a valid password doing about 600,000 to 700,000 attempts per second. The discovered password was `acpgvxjy` and entering it into the site displays the flag.

### Flag

`theLOOSEtheMATH&theTRUTHY`
