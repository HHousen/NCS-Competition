import binascii
from bip_utils import Bip39MnemonicValidator, Bip39SeedGenerator
from tqdm import tqdm

with open("bip39-english-wordlist.txt", "r") as file:
    wordlist = file.read().split()

incomplete_mnemonic = "nature midnight buzz toe sleep fence kiwi ivory excuse system".split()
seed = binascii.unhexlify("131c553f7fb4127e7b2b346991dd92")

# Only test words that are the correct length (number of underscores in
# provided word list)
wordlist_1 = [x for x in wordlist if len(x) == 4]
wordlist_2 = [x for x in wordlist if len(x) == 6]

for word1 in tqdm(wordlist_1, desc="Finding solution words"):
    for word2 in wordlist_2:
        mnemonic = " ".join(incomplete_mnemonic + [word1, word2])
        # First, make sure the mnemonic is valid and if it is generate the seed.
        # Check that the seed starts with the provided hexadecimal string.
        if (Bip39MnemonicValidator(mnemonic).Validate() and
            Bip39SeedGenerator(mnemonic).Generate().startswith(seed)
        ):
            print("Mnemonic Found: %s" % mnemonic)
            break
    else:
        continue  # only executed if the inner loop did not break
    break
