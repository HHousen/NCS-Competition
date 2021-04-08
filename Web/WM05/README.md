# WM05 - 250pts

## Briefing

> Access the site at <https://cfta-wm05.allyourbases.co>, then find and read the contents of the flag file, to get the flag.

## Solution

1. Note that using Burp Suite's repeater functionality makes editing and sending the requests for this challenge much easier.

2. This is a [command injection](https://book.hacktricks.xyz/pentesting-web/command-injection) challenge. [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection)'s page about Command Injection is very helpful here.

3. Sending an `&&ls` command to list the current directory works and shows us that there is a file called `lambda_function.py` that likely contains the logic of the AWS lambda function. However, trying to use `cat` to display the file by running `cat lambda_function.py` doesn't work and instead returns `Error: Invalid Character Detected`.

4. Assuming the script filters spaces we can use the "Bypass without space" section from [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection#bypass-without-space)'s page about Command Injection and format our command like so `&&{cat,lambda_function.py}`. This successfully leaks the server logic, which we saved to [lambda_function.py](./lambda_function.py).

5. Pass `&&{ls,-a}` as the `path` argument in the JSON request to print all files, including hidden files in the current directory. There is a folder called `...`.

6. Use `&&{ls,-a,...}` to list the contents of the `...` folder, which contains a file named `.flag.txt`.

7. Run `&&cat<.../.flag.txt` to get the flag.

### Flag

`bh%3kx9j75%3k2*7!n`
