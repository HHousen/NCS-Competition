# CH01 - 500pts

## Briefing

> Download the files and find a way to retrieve the encrypted data. Contents: 1.pub, 2.pub, m1.enc, m2.enc

Challenge Files:

* [ch01.zip](./ch01.zip)

## Solution

1. Searching for "rsa two messages different exponents" finds [this Crypto StackExchange answer](https://crypto.stackexchange.com/a/62042) which links to [this other Crypto StackExchange answer](https://crypto.stackexchange.com/a/16285) which mentions a "common modulus attack."

2. [Mathematical Attacks on RSA Cryptosystem](https://thescipub.com/pdf/jcssp.2006.665.671.pdf) states: "A Common Modulus attack can be used to recover the plaintext when the same message is encrypted to two RSA keys that use the same modulus. This algorithm works if and only if message sends with the same modulus and relatively prime encryption exponents." You can learn more by reading this article [RSA Attacks: Common Modulus](https://infosecwriteups.com/rsa-attacks-common-modulus-7bdb34f331a5).

3. Searching for a Python script to conduct this attack finds [HexPandaa/RSA-Common-Modulus-Attack](https://github.com/HexPandaa/RSA-Common-Modulus-Attack).

4. We can run this tool using `python3 rsa-cm.py -c1 ch01/m1.enc -c2 ch01/m2.enc -k1 ch01/1.pub -k2 ch01/2.pub` to get the flag: `Flag: shaRinGisCaRinG-010`.

### Flag

`shaRinGisCaRinG-010`
