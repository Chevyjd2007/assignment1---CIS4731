# assignment1---CIS4731
 Assignment 1 for Fundamentals of BlockChain Technologies

 1. (30 points) Using Python's hashlib library, find a meaningful English word whose ASCII encoding has the following SHA-256 hex digest:

69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7

Hint: use hashlib.sha256(word.encode("ascii", "ignore")).hexdigest() to get the hex digest of the ASCII encoding of a given word. List of all meaningful English words is here. See the following video giving you some help for Q1 and Q3:



 

2. (35 points) Consider that we want to design a hash function for a type of message made of a sequence of integers like this 
. The proposed hash function is this:


where 
, 
 can be any positive integer, and 
 is a pre-defined positive integer.

a) Does this hash function satisfy any of the requirements for a crypto-hash function listed below? Explain your answer:

variable input size
fixed output size
efficiency (time-space complexity)
first and second pre-image resistance
strong collision resistance
pseudo-randomness (unpredictability of the output)
b) Repeat part (a) for the following hash function:


c) Calculate the hash function of part (b) for M = (189, 632, 900, 722, 349) and n = 989.

3. (35 points) The following Python function encrypt implements the following symmetric encryption algorithm which accepts a shared 8-bit key (integer from 0-255):

breaks the plaintext into a list of characters
places the ASCII code of every four consecutive characters of the plaintext into a single word (4-bytes) packet
If the length of plaintext is not divisible by 4, it adds white-space characters at the end to make the total length divisible by 4
encrypt each packet by finding the bit-wise exclusive-or of the packet and the given key after extending the key. For example, if the key is 0x4b, the extended key is 0x4b4b4b4b
each packet gets encrypted separately, but the results of encrypting packets are concatenated together to generate the ciphertext.
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

a) implement the decrypt function that gets the ciphertext and the key as input and returns the plaintext as output.

b) If we know that the following ciphertext is the result of encrypting a single meaningful English word with some key, find the key and the word:

10170d1c0b17180d10161718151003180d101617

Submission

You need to submit a single zip file compressing the following items:

q1.py containing the python code for the first question
q3.py containing the python code for the third question
report.pdf containing:
The meaningful English word found in part 1
Answer to q2
The key and the English word found in part 3
