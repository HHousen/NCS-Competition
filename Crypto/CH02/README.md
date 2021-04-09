# CH02 - 500pts

## Briefing

> Below are 4 messages, 2 of them are insecure... find the flag! `2e310d15730618003c27392502592f1b016e1b1c364505191302` `27271e1d6f3935381618340a740404152d0063160106490a0a050d013d2e` `313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04` `1b060c2749020b354105271616532f27772f1c204811111745320b10021717`

## Solution

1. First, we guess that the cipher being used is a [one-time pad](https://en.wikipedia.org/wiki/One-time_pad) since two of the hexadecimal strings are the same length.

2. So we have cipher text one `2e310d15730618003c27392502592f1b016e1b1c364505191302` and cipher text two `313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04` that were both encrypted using the same one-time pad key. If the key for a one-time pad is used twice, it can be broken using [crib dragging](https://samwho.dev/blog/toying-with-cryptography-crib-dragging/).

3. Basically, XORing the cipher texts gives you the same result as XORing the original messages. The math works out as follows (from [this crib dragging article](https://samwho.dev/blog/toying-with-cryptography-crib-dragging/)):

    ```
    cipher1 = msg1 ^ key
    cipher2 = msg2 ^ key
    cipher1 ^ cipher2 = (msg1 ^ key) ^ (msg2 ^ key)
    cipher1 ^ cipher2 = msg1 ^ msg2 ^ key ^ key
    cipher1 ^ cipher2 = msg1 ^ msg2 ^ 0
    cipher1 ^ cipher2 = msg1 ^ msg2
    ```

    This is useful because XORing the two cipher texts removes the key from the problem.

4. We can XOR the two cipher texts using [CyberChef (click for recipe)](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04'%7D,'Standard',false)To_Hex('None',0)&input=MmUzMTBkMTU3MzA2MTgwMDNjMjczOTI1MDI1OTJmMWIwMTZlMWIxYzM2NDUwNTE5MTMwMg) to get `1f0d0050460b1402531a1a4e34480f021f5927000c4d0b153806`. This hexadecimal string is equal to the two messages XORed together. Therefore, we can start guessing parts of a message to decode both cipher texts and get the flag. [SpiderLabs/cribdrag](https://github.com/SpiderLabs/cribdrag) makes this easy.

5. `python2 cribdrag.py 1f0d0050460b1402531a1a4e34480f021f5927000c4d0b153806`:

    ```
    Your message is currently:
    0	__________________________
    Your key is currently:
    0	__________________________
    Please enter your crib: flag
    *** 0: "yaa7"
    *** 1: "kl1!"
    2: "f<'l"
    3: "6*js"
    *** 4: " gue"
    *** 5: "mxc4"
    6: "rn2}"
    7: "d?{}"
    8: "5v{)"
    9: "|v/S"
    10: "|"U/"
    11: "(X)h"
    12: "R$ne"
    *** 13: ".ccx"
    14: "in~>"
    15: "ds8@"
    *** 16: "y5Fg"
    *** 17: "?Kak"
    18: "Alm*"
    19: "f`,l"
    *** 20: "j!jr"
    21: "+gt_"
    *** 22: "myYa"
    Enter the correct position, 'none' for no match, or 'end' to quit: 4
    Is this crib part of the message or key? Please enter 'message' or 'key': message
    Your message is currently:
    0	____flag__________________
    Your key is currently:
    0	____ gue__________________
    Please enter your crib: the 
    *** 0: "keep"
    *** 1: "yh5f"
    2: "t8#+"
    3: "$.n4"
    *** 4: "2cq""
    5: "|gs"
    6: "`j6:"
    7: "v;:"
    8: "'rn"
    9: "nr+"
    10: "n&Qh"
    11: ":\-/"
    12: "@ j""
    13: "<gg?"
    14: "{jzy"
    15: "vw<"
    *** 16: "k1B "
    17: "-Oe,"
    *** 18: "Shim"
    19: "td(+"
    20: "x%n5"
    21: "9cp"
    22: "}]&"
    Enter the correct position, 'none' for no match, or 'end' to quit: 0
    Is this crib part of the message or key? Please enter 'message' or 'key': message
    Your message is currently:
    0	the flag__________________
    Your key is currently:
    0	keep gue__________________
    Please enter your crib:  is        
    *** 0: "?dsp"
    1: "-i#f"
    2: " 95+"
    3: "p/x4"
    *** 4: "fbg""
    5: "+}qs"
    *** 6: "4k :"
    *** 7: "":i:"
    *** 8: "ssin"
    9: ":s="
    *** 10: ":'Gh"
    11: "n];/"
    12: "!|""
    *** 13: "hfq?"
    14: "/kly"
    15: ""v*"
    *** 16: "?0T "
    *** 17: "yNs,"
    18: "im"
    19: " e>+"
    20: ",$x5"
    21: "mbf"
    22: "+|K&"
    Enter the correct position, 'none' for no match, or 'end' to quit: 8
    Is this crib part of the message or key? Please enter 'message' or 'key': message
    Your message is currently:
    0	the flag is ______________
    Your key is currently:
    0	keep guessin______________
    Please enter your crib: g for
    0: "x-f?4"
    1: "j 6)y"
    *** 2: "gp df"
    3: "7fm{p"
    4: "!+rm!"
    5: "l4d<h"
    *** 6: "s"5uh"
    7: "es|u<"
    8: "4:|!F"
    9: "}:([:"
    10: "}nR'}"
    11: ").`p"
    *** 12: "Shimm"
    13: "//dp+"
    *** 14: "h"y6U"
    *** 15: "e??Hr"
    16: "xyAo~"
    17: ">fc?"
    18: "@ j"y"
    19: "g,+dg"
    *** 20: "kmmzJ"
    21: "*+sWt"
    Enter the correct position, 'none' for no match, or 'end' to quit: 12
    Is this crib part of the message or key? Please enter 'message' or 'key': key
    Your message is currently:
    0	the flag is Shimm_________
    Your key is currently:
    0	keep guessing for_________
    Please enter your crib: the flag
    *** 0: "keep gue"
    *** 1: "yh5fmxc4"
    2: "t8#+rn2}"
    3: "$.n4d?{}"
    4: "2cq"5v{)"
    5: "|gs|v/S"
    6: "`j6:|"U/"
    7: "v;:(X)h"
    8: "'rnR$ne"
    9: "nr+.ccx"
    10: "n&Qhin~>"
    11: ":\-/ds8@"
    12: "@ j"y5Fg"
    13: "<gg??Kak"
    14: "{jzyAlm*"
    15: "vw<f`,l"
    *** 16: "k1B j!jr"
    17: "-Oe,+gt_"
    *** 18: "ShimmyYa"
    Enter the correct position, 'none' for no match, or 'end' to quit: 18
    Is this crib part of the message or key? Please enter 'message' or 'key': key
    Your message is currently:
    0	the flag is Shimm_ShimmyYa
    Your key is currently:
    0	keep guessing for_the flag
    Please enter your crib: for the flag
    0: "ybrp2cq"5v{)"
    1: "ko"f|gs|v/S"
    2: "f?4+`j6:|"U/"
    3: "6)y4v;:(X)h"
    4: " df"'rnR$ne"
    5: "m{psnr+.ccx"
    6: "rm!:n&Qhin~>"
    7: "d<h::\-/ds8@"
    8: "5uhn@ j"y5Fg"
    9: "|u<<gg??Kak"
    10: "|!Fh{jzyAlm*"
    11: "([:/vw<f`,l"
    12: "R'}"k1B j!jr"
    13: ".`p?-Oe,+gt_"
    *** 14: "immyShimmyYa"
    Enter the correct position, 'none' for no match, or 'end' to quit: 14
    Is this crib part of the message or key? Please enter 'message' or 'key': key
    Your message is currently:
    0	the flag is ShimmyShimmyYa
    Your key is currently:
    0	keep guessing for the flag
    ```

### Flag

`ShimmyShimmyYa`
