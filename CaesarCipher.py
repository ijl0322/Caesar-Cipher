import string
def caesarCipher(shift, word):
    
    for char in word:
        
        print chr((ord(char)+shift-96)%26 + 96)
    
caesarCipher(1,"abcdez")
print string.ascii_lowercase