import random
import string

strings =" " + string.punctuation + string.ascii_letters + string.digits

word = list(strings)
key = word[:]
random.shuffle(key)

# Encryption
sentence = input("Enter the message : ")
encrypt_sentense = ""

for letter in sentence:
    index = word.index(letter)
    encrypt_sentense += key[index]

print(f"Message : {sentence}")
print(f"Encrypt : {encrypt_sentense}")

# Decryption
encrypt_sentense = input("Enter the encrypt : ")
sentence = ""

for letter in encrypt_sentense:
    index = key.index(letter)
    sentence += word[index]

print(f"Encrypt : {encrypt_sentense}")
print(f"Message : {sentence}")