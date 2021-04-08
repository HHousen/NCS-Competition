# FM01 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: fm01.jpg

Challenge Files:

* [fm01.zip](./fm01.zip)

## Solution

1. The flag is embedded in the metadata of the image. This can be easily solved by finding strings in `fm01.jpg` and searching for `flag`: `strings fm01.jpg | grep Flag` to find `flag: tr4il3r_p4rk` in the metadata for a Photoshop layer name.

2. Alternatively, simply use `exiftool` to see the flag in a nice layout of the metadata by running `exiftool fm01.jpg`:

    ```
    ...
    History Software Agent          : Adobe Photoshop 22.2 (Windows), Adobe Photoshop 22.2 (Windows)
    History Changed                 : /, /
    Text Layer Name                 : flag: tr4il3r_p4rk
    Text Layer Text                 : flag: tr4il3r_p4rk
    Document Ancestors              : E25BCF5D355B2F2CE5EB55EC6B67C7AF
    Image Width                     : 1920
    ...
    ```

### Flag

`tr4il3r_p4rk`
