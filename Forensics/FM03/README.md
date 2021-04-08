# FM03

## Briefing

> Download the Veracrypt volume and find a way to get the flag. Contents: dir_volume

Challenge Files:

* [fm03.zip](./fm03.zip)

## Solution

1. During the competition, a hint was emailed out that said the file for this challenge is a VeraCrypt encrypted volume since no one had solved the challenge after 24 hours.

2. We can try a brute force approach to decrypt the volume since no other files are provided, such as a memory dump of the system that could contain the password. More information about potential attacks can be found in the [VeraCrypt User Manual](https://www.veracrypt.fr/code/VeraCrypt/plain/src/Release/Setup%20Files/VeraCrypt%20User%20Guide.pdf?id=e6ebc63c665dfd38802f63ad8882f573e66cd208) ([Internet Archive Link](https://web.archive.org/web/20210408232357/https://www.veracrypt.fr/code/VeraCrypt/plain/src/Release/Setup%20Files/VeraCrypt%20User%20Guide.pdf?id=e6ebc63c665dfd38802f63ad8882f573e66cd208)).

3. Brutefocing this volume is possible because the password is early in the [`rockyou.txt` password list](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz). My GTX 1060 Mobile GPU can do about 150 H/s without any configuration changes to `hashcat`.

4. The following modes are available in `hashcat`:

    ```
    137XY | VeraCrypt                                        | Full-Disk Encryption (FDE)
       X  | 1 = PBKDF2-HMAC-RIPEMD160                        | Full-Disk Encryption (FDE)
       X  | 2 = PBKDF2-HMAC-SHA512                           | Full-Disk Encryption (FDE)
       X  | 3 = PBKDF2-HMAC-Whirlpool                        | Full-Disk Encryption (FDE)
       X  | 4 = PBKDF2-HMAC-RIPEMD160 + boot-mode            | Full-Disk Encryption (FDE)
       X  | 5 = PBKDF2-HMAC-SHA256                           | Full-Disk Encryption (FDE)
       X  | 6 = PBKDF2-HMAC-SHA256 + boot-mode               | Full-Disk Encryption (FDE)
       X  | 7 = PBKDF2-HMAC-Streebog-512                     | Full-Disk Encryption (FDE)
        Y | 1 = XTS  512 bit pure AES                        | Full-Disk Encryption (FDE)
        Y | 1 = XTS  512 bit pure Serpent                    | Full-Disk Encryption (FDE)
        Y | 1 = XTS  512 bit pure Twofish                    | Full-Disk Encryption (FDE)
        Y | 1 = XTS  512 bit pure Camellia                   | Full-Disk Encryption (FDE)
        Y | 1 = XTS  512 bit pure Kuznyechik                 | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit pure AES                        | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit pure Serpent                    | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit pure Twofish                    | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit pure Camellia                   | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit pure Kuznyechik                 | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded AES-Twofish            | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Camellia-Kuznyechik    | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Camellia-Serpent       | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Kuznyechik-AES         | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Kuznyechik-Twofish     | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Serpent-AES            | Full-Disk Encryption (FDE)
        Y | 2 = XTS 1024 bit cascaded Twofish-Serpent        | Full-Disk Encryption (FDE)
        Y | 3 = XTS 1536 bit all                             | Full-Disk Encryption (FDE)
    ```

5. Let's try mode `13722` since that is the default in VeraCrypt. Starting cracking with: `hashcat -a 0 -m 13722 dir_volume /usr/share/wordlists/rockyou.txt`.

    `hashcat` output:

    ```
    dir_volume:redwings                              

    Session..........: hashcat
    Status...........: Cracked
    Hash.Type........: VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit
    Hash.Target......: dir_volume
    Time.Started.....: Thu Apr  8 18:43:44 2021 (4 mins, 34 secs)
    Time.Estimated...: Thu Apr  8 18:48:18 2021 (0 secs)
    Guess.Base.......: File (/home/hhhgohn/Downloads/rockyou.txt)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........:      149 H/s (8.48ms) @ Accel:64 Loops:16 Thr:64 Vec:1
    Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
    Progress.........: 40960/14344384 (0.29%)
    Rejected.........: 0/40960 (0.00%)
    Restore.Point....: 0/14344384 (0.00%)
    Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:499984-499999
    Candidates.#1....: 123456 -> loser69
    Hardware.Mon.#1..: Temp: 87c Util:100% Core:1835MHz Mem:3802MHz Bus:16

    Started: Thu Apr  8 18:42:40 2021
    Stopped: Thu Apr  8 18:48:20 2021
    ```

    The password `redwings` is shown in the `hashcat` output.

6. We can mount the volume using VeraCrypt's GUI with password `redwings`. The flag is in `Flag/flag.txt`.

### Flag

`Us3_5tr0ng_P@55w0Rds!`
