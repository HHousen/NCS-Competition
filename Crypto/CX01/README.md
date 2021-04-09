# CX01 - 1000pts

## Briefing

> Complete the missing BIP39 mnemonic seed phrase and get address 3 at BIP32 derivation path m/0'/0 as the flag. `nature midnight buzz toe sleep fence kiwi ivory excuse system ____ ______`. You will need to make use of this, as the start of the 128 char BIP39 seed: `131c553f7fb4127e7b2b346991dd92`

## Solution

1. BIP stands for Bitcoin Improvement Protocol. BIP39 "describes the implementation of a mnemonic code or mnemonic sentence -- a group of easy to remember words -- for the generation of deterministic wallets" ([Source](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)).

2. We can download the list of all possible BIP39 words from <https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt>. We can install `bip-utils` by running `pip install bip-utils` and then write a Python [script](./script.py) to try every possible combination of words.

3. The [script.py](./script.py) opens the list of possible words and creates two lists: one of words with length 4 and the other with words of length 6, since that is the number of underscores in the seed phrase provided in the challenge briefing. After that we use a nested loop structure to try every possible word combination. For each combination, we make sure the mnemonic is valid and if it is we generate the seed. Next, we verify that the seed starts with the hexadecimal string provided in the challenge briefing. If both checks pass then we print the discovered mnemonic. The full mnemonic is `nature midnight buzz toe sleep fence kiwi ivory excuse system exit filter`

4. Finally, we need "address 3 at BIP32 derivation path m/0'/0". This [Ethereum StackExchange answer](https://ethereum.stackexchange.com/a/70029) explains what derivation paths are. Searching online for "bip39 mnemonic" finds <https://iancoleman.io/bip39/>, which lets us paste in our mnemonic and look at the derivation paths. Switching to "BIP32" under "Derivation Path" we can enter `m/0'/0` in "BIP32 Derivation Path" and scroll down to see the addresses. Address 3 under `m/0'/0` is `1BvBytaskgTZkJEEUEkBxv6kDWbAKabnmK`, which is the flag.

### Flag

`1BvBytaskgTZkJEEUEkBxv6kDWbAKabnmK`
