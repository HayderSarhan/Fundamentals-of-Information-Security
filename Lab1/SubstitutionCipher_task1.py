import string

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
alphabet = string.ascii_letters

# defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc
key = 4
new_alphabet = []
for i in range(len(alphabet)):
    new_alphabet.append(alphabet[(i+key)%len(alphabet)])

message = "Hello there"
encrypted_message = ""

for i in range(len(message)):
    for j in range(len(alphabet)):
        if message[i] == alphabet[j]:
            encrypted_message += new_alphabet[j]
            break
        elif message[i] != alphabet[j] and j == len(alphabet)-1:
            encrypted_message += message[i]
            break

print("Encrypted message:", encrypted_message)

decrypted_message = ""

for i in range(len(encrypted_message)):
    for j in range(len(new_alphabet)):
        if encrypted_message[i] == new_alphabet[j]:
            decrypted_message += alphabet[j]
            break
        elif encrypted_message[i] != new_alphabet[j] and j == len(new_alphabet)-1:
            decrypted_message += encrypted_message[i]
            break

print("Decrypted message:", decrypted_message)