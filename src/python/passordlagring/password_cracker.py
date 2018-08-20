from hashlib import sha256, pbkdf2_hmac
from binascii import hexlify
from secrets import token_hex
from datetime import timedelta, datetime

# Fra leksjonen om hash-funksjoner
def hash(data):
    h = sha256()
    h.update(data.encode())
    return h.hexdigest()

# Last inn ordlista fra en tekstfil
wordlistf = 'ordliste_aspell.txt'
with open(wordlistf, encoding="utf-8") as f:
    wordlist = f.readlines()

# Lagre en liste over ord, kun små bokstaver
wordlist = [x.strip().lower() for x in wordlist]
# Forbered en liste av hash-ene av alle ordene i ordlista
hashdict = {hash(x): x for x in wordlist}

# Brukere og passord
users = {'olano': 'appelsin',
         'karin': 'høyesterettsjustitiarius',
         'agoei': 'passord',
         'tjesi': 'app3ls1n',
         'marst': 'passord'}
