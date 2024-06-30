sentence = input('Enter a sentence: ')
key = int(input('Enter a key: '))

def decode(sentence, key):
    new_sentence = ""
    for letter in sentence:
        if letter == " ":
            new_sentence += " "
        elif 1 <= key <= 26:
            new_ascii_letter = ord(letter) - key
            if new_ascii_letter < 97:
                new_ascii_letter = new_ascii_letter + 26

            new_letter = chr(new_ascii_letter)
            new_sentence += new_letter

    return new_sentence

def encode(sentence, key):
    new_sentence = ""
    for letter in sentence:
        if letter == " ":
            new_sentence += " "
        elif 1 <= key <= 26:
            new_ascii_letter = ord(letter) + key
            if new_ascii_letter > 122:
                new_ascii_letter = new_ascii_letter - 26        # x,y,z->a,b,c

            new_letter = chr(new_ascii_letter)
            new_sentence += new_letter

    return new_sentence

decode_or_encode = input('do you want to decode your sentence or encode it? (d/e):')
if decode_or_encode == 'd':
    print(decode(sentence, key))
else:
    print(encode(sentence, key))