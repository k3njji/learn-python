
def encode(text, shift):
    new_text = ""
    for i in range(len(text)):
        index = ord(text[i]) - 97
        index = (index+shift) % 26
        new_text += chr(index+97)
    return new_text

def decode(text, shift):
    new_text = ""
    for i in range(len(text)):
        index = ord(text[i]) - 97
        index = (index-shift) % 26
        new_text += chr(index+97)
    return new_text

direction = input('Type "encode" to encrypt, type "decode" to decrypt: ').lower()
text = input("type the text: ")
shift = int(input("how many numbers is shifted: "))

if(direction == 'encode'):
    text = encode(text, shift)
    print("encoded text: ", text)
elif(direction == 'decode'):
    text = decode(text, shift)
    print("encoded text: ", text)