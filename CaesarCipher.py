import string
def caesarCipher(shift, word):
    encode = ""
    for char in word:
        if char in string.ascii_lowercase:
            encode += chr((ord(char)+shift-97)%26 + 97)
        elif char in string.ascii_uppercase:
            encode += chr((ord(char)+shift-65)%26 + 65)
        else:
            encode += char
    return encode
    
print caesarCipher(1,"A cat is a zebra ? ")

def decodeCaesar(shift, word):
    decode = ""
    for char in word:
        if char in string.ascii_lowercase: 
            decode += chr((ord(char) - shift - 97 + 26)%26 + 97)
    return decode
    
print decodeCaesar(1, "B dbu jt b afcsb ?")
            
            
            
            
            