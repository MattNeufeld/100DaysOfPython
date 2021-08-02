nameF = open("Input/Names/invited_names.txt")
names = nameF.readlines()

nameF.close()

file = open("C:/Users/user/Desktop/100DaysOfPython/Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt")
defaultLetter = file.read()
file.close()

for n in names:
    n = n.replace("\n", "")
    print(n)
    newLetter = defaultLetter.replace("[name]", n)
    with open(f"Output/ReadyToSend/{n}.txt", "w+") as nFile:
        nFile.write(newLetter)