import string

def convert_to_unicode(test_str):
    return ''.join(r'\u{:04X}'.format(ord(c)) for c in test_str)

with open("cm02.txt", "r") as file:
    emojis = file.read()

emojis_unicode = convert_to_unicode(emojis)
# `ord(x) > 300` removes any ascii characters and ensures `emojis_ords` contains
# only the emojis.
emojis_ords = [ord(x) for x in emojis if ord(x) > 300]

emojis_ord_mapping = dict(zip(set(emojis_ords), list(string.ascii_lowercase)))
substitution_cipher = [emojis_ord_mapping[ord(x)] if ord(x) > 300 else x for x in emojis]

print("".join(substitution_cipher))
