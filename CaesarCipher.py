import string
def caesarCipher(shift, word):
    encode = ""
    for char in word:
        if char in string.ascii_lowercase:
            encode += chr((ord(char)+shift-96)%26 + 96)
        elif char in string.ascii_uppercase:
            encode += chr((ord(char)+shift-64)%26 + 64)
        else:
            encode += char
    return encode
    
print caesarCipher(1,"A cat is a cat ? ")

