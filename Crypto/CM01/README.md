# CM01 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: code.png, frame.png

Challenge Files:

* [cm01.zip](./cm01.zip)

## Solution

1. This is a bad solution. You have been warned. I'm sure there are quicker methods than this. You have been warned.

2. We can decode `frame.png` using [ZXing](https://zxing.org/w/decode.jspx) to get `Hey, I've put the flag into the other file using the same trick we always use.  You know what to do. :)`.

3. Now, invert the `code.png` file using any method you want (GIMP works great)

4. Next, open the `frame.png` in GIMP and open `code_inverted.png` as a layer. Make sure the `code_inverted.png` layer is on top and set its opacity to 50%. This will reveal a gray QR code.

5. Flatten the layers and then select all the black pixels using the "Select by Color" feature. Use the bucket to fill them with white.

6. We should be able to simply replace all the gray with black and have the QR code, but there are noise pixels. I tried various methods to remove them, but I ended up using the pen tool to draw over all the entire QR code. After that, I selected the black pixels using the magic wand, inverted the selection, and filled the selection with white.

7. Finally, save the image as `answer.png` and decode it using [ZXing](https://zxing.org/w/decode.jspx) to get `FLAG: A_Code_For_A_Code`

### Flag

`A_Code_For_A_Code`
