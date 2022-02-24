def encrypt (text):
    new_text = ''
    for i in text:
        if ord(i)>64 and ord(i)<91:
            # ord to convert a character into its unicode code, subtracting unicode of 'A' i.e. 65 from it to get the character's index
            num = ord(i)-65
            # adding the Ceaser shift of 3 to char index and taking its mod to get correct index of encrypted char, re-adding with the unicode code of 'A' and then decoding new text
            new_text += chr(((num+3)%26)+65)
        else:
            new_text += i
    return new_text