alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    phrase = ""
    if direction.lower() == "encode":
        for letter in text:
            index = alphabet.index(letter) + shift
            if index > 25:
                index = index - 25
            phrase = phrase + alphabet[index]
        print(f"The encoded text is {phrase}")
    else:
        for letter in text:
            index = alphabet.index(letter) - shift
            if index < 0:
                index = index + 25
            phrase = phrase + alphabet[index]
        print(f"The decoded text is {phrase}")

end = False

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    endI = input("Would you like to continue? Type 'yes' to continue.")
    if endI != "yes":
        end = True
