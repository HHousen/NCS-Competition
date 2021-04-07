# BM03 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: flag

Challenge Files:

* [bm03.zip](./bm03.zip)

## Solution

1. Decompiling the binary shows an `output()` function and a line in `output()` that stops printing the flag if the `rows` argument is less than `6`.

    `output` function:

    ```c++
    void output(int rows,int cols)

    {
        long lVar1;
        undefined8 *puVar2;
        undefined8 *puVar3;
        long in_FS_OFFSET;
        int i;
        int j;
        int flag [6] [85];
        char flagChars [11];
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        lVar1 = 0xff;
        puVar2 = &DAT_00100a00;
        puVar3 = (undefined8 *)flag;
        while (lVar1 != 0) {
            lVar1 = lVar1 + -1;
            *puVar3 = *puVar2;
            puVar2 = puVar2 + 1;
            puVar3 = puVar3 + 1;
        }
        flagChars[0] = ' ';
        flagChars[1] = '_';
        flagChars[2] = '/';
        flagChars[3] = '\\';
        flagChars[4] = '(';
        flagChars[5] = ')';
        flagChars[6] = '`';
        flagChars[7] = ',';
        flagChars[8] = '|';
        flagChars[9] = '.';
        flagChars[10] = '\0';
        i = 0;
        while (i < rows) {
            j = 0;
            while (j < cols) {
            putchar((int)flagChars[flag[(long)i * 0x55 + (long)j] / 100]);
            j = j + 1;
            }
            putchar(10);
            i = i + 1;
        }
        if (rows < 6) {
            puts("\x1b[31m Error displaying rest of flag\x1b[0m");
        }
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return;
    }
    ```

2. Launch the program in GDB then do the following:

    1. Breakpoint at `output`: `b output`

    2. Call `output` but will the `rows` argument set to `6`: `call output(6,0x55)`

    3. Continue past the breakpoint: `c`

    4. The flag is printed:

    ```
           __       __                          _                      ____ __           
      ____/ /___   / /_   __  __ ____ _ ____ _ (_)____   ____ _       / __// /_ _      __
     / __  // _ \ / __ \ / / / // __ `// __ `// // __ \ / __ `/      / /_ / __/| | /| / /
    / /_/ //  __// /_/ // /_/ // /_/ // /_/ // // / / // /_/ /      / __// /_  | |/ |/ / 
    \__,_/ \___//_.___/ \__,_/ \__, / \__, //_//_/ /_/ \__, /______/_/   \__/  |__/|__/  
                              /____/ /____/           /____//_____/                      
    ```

### Flag

`debugging_ftw`
