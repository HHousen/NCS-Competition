# CM02 - 250pts

## Briefing

> Download the file and find a way to get the flag. Contents: cm02.txt

Challenge Files:

* [cm02.zip](./cm02.zip)

## Solution

1. There are several methods for encoding text as emojis:

    1. A common one is to simply offset the alphabet by some unicode value so each letter maps to an emoji. This can be detected because the difference between the maximum and minimum unicode values in the supplied string will be 26, or another number (like 34 for ascii lowercase and digits) that makes sense for the alphabet the flag could be using.

    2. Another method is to simply use the last byte of the unicode value as the ascii letter.

    3. Finally, the approach used for this challenge is a substitution cipher.

2. This is a substitution cipher because there are 26 unique emojis. We can use a Python [script.py](./script.py) to map each emoji to a letter in the alphabet and then replace each emoji with its assigned letter. The output of [script.py](./script.py) is in [substitution_cipher.txt](./substitution_cipher.txt).

3. Now that we have transformed the input, we can use a normal substitution solver such as [quipqiup](https://www.quipqiup.com/), [guballa](https://www.guballa.de/substitution-solver), or [Boxentriq](https://www.boxentriq.com/code-breaking/cryptogram) to get the key for the substitution cipher.

4. [guballa](https://www.guballa.de/substitution-solver) finds the key to be `psndvylqigjfzcerhoumxtwakb` and prints the decoded message. This section corresponds to the flag text: `yfpl: yovhxvcmfk_uxsumimxmv_yoewck_ypnv_yeo_uzifvk_ypnv`. It decodes to `flag: frequently_substitute_frowny_face_for_smiley_face`

### Flag

`frequently_substitute_frowny_face_for_smiley_face`
