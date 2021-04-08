# NM01 - 250pts

## Briefing

> Retrieve output from network endpoint at `cfta-nm01.allyourbases.co` port `8017` and figure out how to get the flag.

## Solution

1. Let's connect to the service using `netcat` and see what we're dealing with:

    ```
    $ nc cfta-nm01.allyourbases.co 8017
    \x47\x4A\x52\x57\x5A\x44
    a
    Incorrect
    ```

2. It seems to output some hexadecimal. Let's try again and input the ascii representation:

    ```
    $ nc cfta-nm01.allyourbases.co 8017
    \x55\x45\x57\x45\x4F\x4B
    UEWEOK
    Too slow!
    ```

3. Okay, we need to do it faster. So, let's write a script that connects, converts the hexadecimal to ascii, submits the ascii representation, and then hopefully get the flag.

4. [script.py](./script.py) uses pwntools to do just that. Running the script produces the following output:

    ```
    [+] Opening connection to cfta-nm01.allyourbases.co on port 8017: Done
    Decoded String: YXDKJZ
    [*] Switching to interactive mode
    Correct! - Flag: o[hex]=>i[ascii]=:)
    [*] Got EOF while reading in interactive
    [*] Closed connection to cfta-nm01.allyourbases.co port 8017
    [*] Got EOF while sending in interactive
    ```

### Flag

`o[hex]=>i[ascii]=:)`
