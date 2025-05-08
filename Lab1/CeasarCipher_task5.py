import string

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
alphabet = string.ascii_letters

# defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc
keys = 20
for key in range(1, keys):
    print(f'===================={key}====================')
    new_alphabet = []
    for i in range(len(alphabet)):
        new_alphabet.append(alphabet[(i+key)%len(alphabet)])

    encrypted_message = "Vwrwbu gcas roho wg ybckb og sbqfmdhwcb. Kvsb dzowb hslh wg sbqfmdhsr wh psqcasg ibfsoropzs obr wg ybckb og qwdvsfhslh. Wb o Gipghwhihwcb qwdvsf, obm qvofoqhsf ct dzowb hslh tfca hvs uwjsb twlsr gsh ct qvofoqhsfg wg gipghwhihsr pm gcas chvsf qvofoqhsf tfca hvs goas gsh rsdsbrwbu cb o ysm. Tcf sloadzs kwhv o gvwth ct 1, O kcizr ps fsdzoqsr pm P, P kcizr psqcas Q, obr gc cb."
    decrypted_message = ""

    for i in range(len(encrypted_message)):
        for j in range(len(new_alphabet)):
            if encrypted_message[i] == new_alphabet[j]:
                decrypted_message += alphabet[j]
                break
            elif encrypted_message[i] != new_alphabet[j] and j == len(new_alphabet)-1:
                decrypted_message += encrypted_message[i]
                break
    print(decrypted_message)