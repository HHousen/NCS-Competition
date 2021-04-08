# FE03 - 100pts

## Briefing

> Download the file and find a way to get the flag from the docker image. Contents: fe03.tar.gz

Challenge Files:

* [fe03.zip](./fe03.zip)

## Solution

1. Run `tar -xf fe03.tar.gz` to extract the GZIP TAR file. The contents are a docker container.

2. The `c46eb315a38f7abc53c600748ca1bb022b571acb74e5d6d6efe16a79914742bf.json` file lists that one stage of the build script is the following: `{"created":"2021-03-14T14:22:31.349307153Z","created_by":"/bin/sh -c #(nop) ADD file:9ae478ef983cfd7a1762156ecbf2c745eb4f54af8480753e39fcbc4296bc2cdb in /home/secret/flag.txt "}`.

3. We can go though each folder and extract the corresponding `layer.tar` file. Check to see if the path `/home/secret/flag.txt` exists in each extracted `layer.tar` folder. This is faster than writing a script to do it since there are only 14 layers.

4. The flag is in the `20f27a62bd4b6360e6d71ee3b6e3d4e23d27f8316853b5f115134dc496b76921/layer.tar` file. Read the `flag.txt` file to get the flag.

### Flag

`8191-SiMpLeFilESysTemForens1Cs`
