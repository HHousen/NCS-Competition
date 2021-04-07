# BM02 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: program

Challenge Files:

* [bm02.zip](./bm02.zip)

## Solution

1. Running the program simply outputs `I'm not going to make it that easy for you.`.

2. Decompiling the binary using Ghidra reveals a `printFlag()` function that prints the flag if it is called with `0x539` as an argument.

    `printFlag` function:

    ```c++
    void printFlag(int param_1)

    {
        byte bVar1;
        byte bVar2;
        long in_FS_OFFSET;
        uint local_2c;
        byte local_28 [24];
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        if (param_1 == 0x539) {
            local_28[0] = 0x15;
            local_28[1] = 0x70;
            local_28[2] = 0xe5;
            local_28[3] = 100;
            local_28[4] = 0x7a;
            local_28[5] = 0xd4;
            local_28[6] = 0x6d;
            local_28[7] = 0x75;
            local_28[8] = 0xeb;
            local_28[9] = 0xf4;
            local_28[10] = 0x6a;
            local_28[11] = 0xd1;
            local_28[12] = 0xfa;
            local_28[13] = 0xd1;
            local_28[14] = 0xf9;
            local_28[15] = 0xe8;
            local_28[16] = 0x9d;
            local_28[17] = 0x7c;
            local_28[18] = 0x41;
            local_2c = 0;
            while (local_2c < 0x13) {
            bVar2 = (byte)local_2c;
            bVar1 = ~-((~local_28[local_2c] + bVar2 ^ 0x48) - bVar2);
            bVar2 = ((bVar1 << 3 | bVar1 >> 5) - bVar2 ^ 0x5d) - 0x23 ^ bVar2;
            bVar1 = (bVar2 * '\x02' | bVar2 >> 7) + 0xbf;
            local_28[local_2c] = (bVar1 * ' ' | bVar1 >> 3) ^ 0x65;
            local_2c = local_2c + 1;
            }
            puts((char *)local_28);
        }
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return;
    }
    ```

3. We run the program using GDB and do the following:

    1. Breakpoint at `puts`: `b puts`

    2. Run: `r`

    3. Call `printFlag` with the correct argument: `call (char *) printFlag(0x539)`

    4. The flag is shown as `Flag: patchItFixIt`.

### Flag

`patchItFixIt`
