# FM02 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: IRC-cap-vpn.pcapng

Challenge Files:

* [fm02.zip](./fm02.zip)

## Solution

1. We can open the packet capture file in `wireshark` and apply the `irc` filter since the name of the file mentions irc.

2. Right click and follow the TCP stream to get the following ASCII output:

    ```
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :Hey man, How's it going?
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    PRIVMSG RiotCard851 :All good, how are you? 
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :yeah Doing good, been working on something recently.  Wanna check it out?
    PRIVMSG RiotCard851 :Sure, What is it? 
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :See if you can work it out first. I've hidden the flag in it. ;)
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :.DCC SEND "Flag.7z" 3232247681 35289 3466.
    ISON RiotCard85 
    :orwell.freenode.net 303 RandumbHero1 :
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :here you go! 
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :Password on it,  using the trick as usual. 
    PING 1604473558
    ISON RiotCard85 
    :orwell.freenode.net PONG orwell.freenode.net :1604473558
    :orwell.freenode.net 303 RandumbHero1 :
    :RiotCard851!~luke@82.102.19.124 PRIVMSG RandumbHero1 :TWFyaW9SdWxlejE5ODU=
    PING 1604488778
    ISON RiotCard85 
    :orwell.freenode.net PONG orwell.freenode.net :1604488778
    :orwell.freenode.net 303 RandumbHero1 :
    PRIVMSG RiotCard851 :Awesome, I'll go check it out now. 
    ```

3. A file called `file.7z` and a password `TWFyaW9SdWxlejE5ODU=` are sent. The password is base64 for `MarioRulez1985`.

4. We can search each TCP stream for the `7z` magic bytes, which are `37 7a bc af 27 1c` according to the [Wikipedia List of File Signatures](https://en.wikipedia.org/wiki/List_of_file_signatures), to find which steam contains the file. `tcp.stream eq 79` contains the flag. We can follow the steam, change the "Show and save data as" option to `Raw`, and then save the content to `file.7z`.

5. Next, we extract `file.7z` using the password we found earlier, `MarioRulez1985`.

6. Finally, run `strings Flag.nes` to get the flag.

### Flag

`NESted_in_a_PCAP`
