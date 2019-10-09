ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ENCKEY = "nmlkjihgfedcbazyxwvutsrqpo"
DECKEY = "zyxwvutsrqponmlkjihgfedcba"

def encrypt(MESSAGE):
    encryptedMessage = ""

    for letter in MESSAGE:
        encIndex = 0
        
        if letter in ALPHABET:
            encIndex = ENCKEY.index(letter)
            encryptedMessage += ALPHABET[encIndex]
        else:
            encryptedMessage += letter
    
    print(encryptedMessage)

def decrypt(MESSAGE):
    decryptedMessage = ""

    for letter in MESSAGE:
        decIndex = 0

        if letter.isupper() and letter.lower() in DECKEY:
            decIndex = DECKEY.index(letter.lower())
            decryptedMessage += ALPHABET[decIndex].upper()
        
        elif letter in DECKEY:
            decIndex = DECKEY.index(letter)
            decryptedMessage += ALPHABET[decIndex]

        else:
            decryptedMessage += letter

    print(decryptedMessage)


MODE = ""
def mode(MODE):
    MODE = input("(E)ncrypt or (D)ecrypt: ").lower()    

    if MODE[0] is "e":
        MESSAGE = input("Enter a message to decrypt: ")
        encrypt(MESSAGE)
    
    elif MODE[0] is "d":
        MESSAGE = input("Enter a message to encrypt: ")
        decrypt(MESSAGE)
    
    else:
        mode(MODE)
mode(MODE) 