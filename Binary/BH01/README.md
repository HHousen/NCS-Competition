# BH01 - 500pts

## Briefing

> Download the file and find a way to get the flag. Contents: program

Challenge Files:

* [bh01.zip](./bh01.zip)

## Solution

1. Inputting some random letters into the program prints some of the flag:

    ```
    What is the magic word?
    djyawthvdbhgsajdghytwilhqypdoasgdbhwgdytqvdkbfuhgyabkhsj
    Flag: aLittLeObfuScatIo������uF?9��
    Did you understand that?
    ```

    However, the amount of the flag that is printed changes each time we run the program using the same input. There appears to be 4 different variations so a random number generator is involved. Using an input that consists of a single character seems to always produce the same output.

2. We can decompile the binary using Ghidra to see what the program does:

    `main` function:

    ```c++
    undefined8 FUN_00101209(void)

    {
        byte bVar1;
        byte bVar2;
        int iVar3;
        uint uVar4;
        time_t tVar5;
        long in_FS_OFFSET;
        uint local_90;
        time_t local_88;
        undefined4 local_7d;
        undefined local_79;
        undefined8 local_78;
        undefined8 local_70;
        undefined8 local_68;
        undefined8 local_60;
        undefined4 local_58;
        undefined8 local_48;
        undefined8 local_40;
        undefined8 local_38;
        undefined8 local_30;
        undefined8 local_28;
        undefined2 local_20;
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        tVar5 = time(&local_88);
        srand((uint)tVar5);
        local_48 = 0;
        local_40 = 0;
        local_38 = 0;
        local_30 = 0;
        local_28 = 0;
        local_20 = 0;
        local_7d = 0x16120a05;
        local_79 = 0x18;
        puts("What is the magic word?");
        fflush(stdout);
        fgets((char *)&local_48,0x28,stdin);
        local_78 = 0x103f4f6c803a05b6;
        local_70 = 0x9f2abbb5f5e62364;
        local_68 = 0x982b00094580efba;
        local_60 = 0x3f4675fb93f9dfb2;
        local_58 = 0x1afcba39;
        iVar3 = rand();
        uVar4 = (int)*(char *)((long)&local_48 + (long)(int)*(char *)((long)&local_7d + (long)(iVar3 % 5))
                                ) - 0x5a;
        local_90 = 0;
        while (local_90 < uVar4) {
            bVar1 = ~*(byte *)((long)&local_78 + (ulong)local_90) + 0x2f;
            bVar2 = (byte)local_90;
            bVar1 = (~(~(0x57 - (~(bVar1 * -0x80 | bVar1 >> 1) - 0x33)) - 0x3f) ^ bVar2) + 0x4e ^ bVar2;
            bVar1 = ~((bVar1 * '\x02' | bVar1 >> 7) + 0x3d) ^ bVar2;
            bVar1 = ~(bVar1 << 3 | bVar1 >> 5);
            if ((int)uVar4 < 0) break;
            bVar1 = ~((bVar1 << 5 | bVar1 >> 3) - bVar2) - 0x17;
            bVar1 = ~((bVar1 * -0x80 | bVar1 >> 1) - bVar2);
            bVar1 = 0xad - ((bVar1 << 3 | bVar1 >> 5) + 0x3c);
            bVar1 = (bVar1 * ' ' | bVar1 >> 3) + bVar2;
            bVar1 = (bVar1 * '\b' | bVar1 >> 5) - bVar2;
            bVar1 = ~(bVar1 * -0x80 | bVar1 >> 1) ^ bVar2;
            bVar2 = (bVar1 * -0x40 | (byte)-bVar1 >> 2) - bVar2;
            bVar1 = ~(~(~(bVar2 * ' ' | bVar2 >> 3) ^ 0x45) - 8);
            *(byte *)((long)&local_78 + (ulong)local_90) =
                (0xd1 - ((bVar1 << 2 | bVar1 >> 6) ^ 0xef) ^ 0x65) - 0x3a;
            local_90 = local_90 + 1;
        }
        puts((char *)&local_78);
        puts("Did you understand that?");
        if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
            return 0;
        }
                            /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    ```

3. The program picks a random byte from `local_7d` and uses that byte to index the user input to get a single character `uVar4`. Next, a loop runs that prints the flag character by character. However, it only iterates trough the loop `uVar4 - 0x5a` times. Therefore, the letter that is selected from the input has to have an ascii code minus `0x5a` (90) that is greater than the length of the flag.

4. `}` has a large ascii value. If we sent a lot of `}`s into the program, it will print the flag: `python -c "print('}'*50)" | ./program`. This is because the program selects a random character from our input, subtracts 90 from it, and then prints that many characters of the flag. So, `125 - 90 = 35` which means the loop runs 35 times and successfully displays the 29 character flag. We cannot use just one `}` because the program selects a random character from the input and it a character does not exist at the chosen index, it selects `\x00` (a null byte).

    ```
    What is the magic word?
    }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
    Flag: aLittLeObfuScatIonalCharActEr
    Did you understand that?
    ```

### Flag

`aLittLeObfuScatIonalCharActEr`
