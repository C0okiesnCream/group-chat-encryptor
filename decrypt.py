#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports - i don't think we need any for this one either but if you do find somewhere that would be better to have one, go ahead and add one
#vars
c = 0
dummy = []
#key_file open
key_file = open("key_file.txt", "r")
#grabs key from key_file
key = key_file.readline(85)
#close key_file
key_file.close()

message = input('encrypted message here >')
deMessage = 0
KEYBASE = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    '-',
    '=',
    '[',
    ']',
    ';',
    #the double backslash below this is because it gives an error with just one as you are cancelling the quotation mark
    '\\',
    ',',
    '.',
    '/',
    '`',
    '~',
    '~',
    '_',
    '+',
    '{',
    '}',
    ':',
    '|',
    '<',
    '>',
    '?',
    ' '
]

#turning key into an array for easier use
for i in key:
 dummy.append(i)
key = dummy

dummy = []

#doing the same for message
for i in message:
 dummy.append(i)
message = dummy

#this unscrambles the message
while c < len(message):
    for i in range(83):
        if message[c] == key[i]:
            message[c] = KEYBASE[i]
            break
 
    c += 1

dummy = ""
message = dummy.join(message)
print('message >>>',message)