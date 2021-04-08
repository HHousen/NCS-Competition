import hashlib
import string
import itertools
from tqdm import tqdm

for idx in tqdm(itertools.permutations(string.ascii_lowercase, 8)):
    idx = "".join(idx)
    hashed = hashlib.md5(("e361bfc569ba48dc" + str(idx)).encode('utf-8')).hexdigest()
    # Starts with `0e` and everything else is a digit
    if hashed.startswith("0e") and hashed[2:].isdigit():
        print("Hash: %s" % hashed)
        print("Password: %s" % idx)
        break
