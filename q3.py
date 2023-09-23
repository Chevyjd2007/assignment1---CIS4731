def make_block(lst):
    return (ord(lst[0])<<24) + (ord(lst[1])<<16) + (ord(lst[2])<<8) + ord(lst[3])

def encrypt(message, key):
    rv = ""
    l = list(message)
    n = len(message)
    blocks = []
    for i in range(0,n,4):# break message into 4-character blocks
        if i+4 <= n:
            blocks.append(make_block(l[i: i+4]))
        else:# pad end of message with white-space if the lenght is not divisible by 4
            end = l[i:n]
            end.extend((i+4-n)*[' '])
            blocks.append(make_block(end))
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    for block in blocks:#encrypt each  block separately
        encrypted = str(hex(block ^ extended_key))[2:]
        for i in range(8 - len(encrypted)):
            rv += '0'
        rv += encrypted
    return rv


def from_hex_to_block(hex_str):
    # We convert a 8-character hex string back into a 4-byte block (integer)
    return int(hex_str, 16)

def block_to_str(block):
    # We convert a 4-byte block back into 4 characters
    chars = [
        chr((block >> 24) & 0xFF),
        chr((block >> 16) & 0xFF),
        chr((block >> 8) & 0xFF),
        chr(block & 0xFF)
    ]
    return ''.join(chars)

def decrypt(ciphertext, key):
    rv = ""
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key) 

    # We split ciphertext into blocks of 8 characters
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]

    #We decrypt the blocks and then convert the block to string to add to plaintext
    for block in blocks:
        decrypted_block = from_hex_to_block(block) ^ extended_key
        rv += block_to_str(decrypted_block) 

    return rv.rstrip()  # We return the plaintext, possibly removing the padding (trailing spaces)

# Testing
key = 0x4b
plaintext = "hello"
encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)
print(decrypted) 


def brute_force_decrypt(ciphertext):
    for key in range(256):  # 8-bit key has 256 possibilities
        decrypted_text = decrypt(ciphertext, key)
        
        if decrypted_text.isalpha():
            return key, decrypted_text

    return None, None

# Testing
ciphertext = "10170d1c0b17180d10161718151003180d101617"
key, word = brute_force_decrypt(ciphertext)
print(f"Key: {key}, Word: {word}")
