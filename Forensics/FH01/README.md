# FH01 - 500pts

## Briefing

> Download the file and find a way to get the flag.

Challenge Files:

* [fh01.zip](./fh01.zip)

## Solution

1. Looking through the packet capture file we notice there appear to be files sent on `udp.stream == 2`. I tried extracting these files by saving what `192.168.47.129` sends in `udp.stream == 2` as raw bytes and then using `binwalk`, but `binwalk` only extracted corrupted versions of the files. I tried uses a hex editor to manually save the files from the raw bytes, but this failed for the same reason: some files are "corrupted" because they are missing bytes or have extra bytes.

2. The protocol used for these files is unique as far as I know. `192.168.47.129` sends data to `192.168.47.128` in 626 byte chunks. However, this data is not pure data, which causes the aforementioned problems.

3. The protocol works like this:

    1. `192.168.47.128`: Requests the file `get <filename>`

    2. `192.168.47.129`: Sends the file in segments `<segment id (8 bytes)> <op code (8 bytes)> <data>`

    3. `192.168.47.128`: Acknowledges that segment has been received by sending the segment id back `<segment id (8 bytes)>`

    4. Repeat steps 2 and 3 until the entire file is sent.

4. We can extract the data is a more usable format usign `tshark`: `tshark -r fh01.pcapng -T fields -e data --disable-protocol sigcomp --disable-protocol wg --disable-protocol pathport --disable-protocol dcerpc -Y '(ip.src == 192.168.47.129 && frame.len == 626) || (ip.src == 192.168.47.128 && udp)' > udp_stream_2.dmp`

5. We write a Python [script.py](./script.py) to parse through the data and export the files. The [script](./script.py) loops though the lines of `udp_stream_2.dmp`. If the line starts with the word `get` then a new file is being transferred and the program starts storing each segment with length 4129, which is the hexadecimal equivalent of the 626 byte chunks from wireshark.

6. The flag is in the last file `5.zip`. Extract `5.zip` and open `5.jpg` to get the flag.

### Flag

`C4tch1ng_H0n3y_p0Ts_w1TH_a_Sh4rk!`
