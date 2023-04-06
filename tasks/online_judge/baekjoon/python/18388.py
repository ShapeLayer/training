keymap = {
    'Q': 'W',
    'W': 'E',
    'E': 'R',
    'R': 'T',
    'T': 'Y',
    'Y': 'U',
    'U': 'I',
    'I': 'O',
    'O': 'P',
    'A': 'S',
    'S': 'D',
    'D': 'F',
    'F': 'G',
    'G': 'H',
    'H': 'J',
    'J': 'K',
    'K': 'L',
    'Z': 'X',
    'X': 'C',
    'C': 'V',
    'V': 'B',
    'B': 'N',
    'N': 'M'
}

puts = list(input())
for i in range(len(puts)):
    if 65 <= ord(puts[i]) <= 90:
        puts[i] = keymap[puts[i]]
print(''.join(puts))