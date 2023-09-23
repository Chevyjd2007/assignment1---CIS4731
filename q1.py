import hashlib
from typing import Optional

#Function will return string or None value
def find_word(target: str) -> Optional[str]:
    #Opening file containing english words
    with open('./dict.txt', 'r') as f:
        words = f.readlines()

    #We iterate through words and check if the hash value mathces the target
    for word in words:
        stripped_words = word.strip()
        
        hash_value = hashlib.sha256(stripped_words.encode("ascii", "ignore")).hexdigest()

        if hash_value == target:
            return word

    return None

#Testing
target = '69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7'
answer = find_word(target)

#ravishingly
print(answer)