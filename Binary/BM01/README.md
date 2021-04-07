# BM01 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: program

Challenge Files:

* [bm01.zip](./bm01.zip)

## Solution

1. Running the program shows strange text. We can paste this into Google Translate to find that it is Russian. `Какой пароль？` translates to `What password?`. Entering some input produces `неверный`, which translates to `incorrect`.

2. Let's decompile the binary using Ghidra.

    `main` function:

    ```c++
    undefined8 main(void)

    {
        byte bVar1;
        byte bVar2;
        int iVar3;
        long in_FS_OFFSET;
        uint local_74;
        byte local_67 [15];
        char local_58 [72];
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        puts("\x1b[36mКакой пароль？\x1b[0m");
        printf("> ");
        fgets(local_58,0x3c,stdin);
        iVar3 = strcmp("молоток123\n",local_58);
        if (iVar3 == 0) {
            local_67[0] = 0xe4;
            local_67[1] = 100;
            local_67[2] = 0xa6;
            local_67[3] = 0x90;
            local_67[4] = 0x7c;
            local_67[5] = 0xa6;
            local_67[6] = 0x75;
            local_67[7] = 0xb8;
            local_67[8] = 0xa4;
            local_67[9] = 0xd;
            local_67[10] = 0xc;
            local_67[11] = 0x7f;
            local_67[12] = 0x7e;
            local_67[13] = 0xf3;
            local_67[14] = 1;
            local_74 = 0;
            while (local_74 < 0xf) {
            bVar2 = (byte)local_74;
            bVar1 = ~(~(~-((local_67[local_74] ^ 0xa5) - bVar2 ^ bVar2) ^ 0x8d) - 0xb);
            local_67[local_74] = (((bVar1 << 5 | bVar1 >> 3) + 0x37 ^ 0xe5) - 7 ^ bVar2) - 0x39;
            local_74 = local_74 + 1;
            }
            printf("\x1b[32mверный!\x1b[0m\n\n\x1b[33mфлаг: %s\x1b[0m\n",local_67);
        }
        else {
            puts("\x1b[31mневерный.\x1b[0m");
        }
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return 0;
    }
    ```

    The program compares the user input to `молоток123`, which translates to `hammer123`.

3. Running the program and entering `молоток123` outputs `верный! флаг: wh1te%BluE$R3d` (Translation: `Right! Flag:` wh1te%BluE$R3d), which is the flag.

### Flag

`wh1te%BluE$R3d`
