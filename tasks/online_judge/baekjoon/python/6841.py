from sys import stdin
input = stdin.readline

def compute(shorts: str) -> str:
    transtable = {
        'CU': 'see you',
        ':-)': 'I’m happy',
        ':-(': 'I’m unhappy',
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': 'you’re welcome',
        'TTYL': 'talk to you later'
    }
    return transtable[shorts] if shorts in transtable else shorts

if __name__ == '__main__':
    gets: str = ''
    while True:
        try:
            gets = input()
        except EOFError:
            break
        gets = gets.strip()
        if not gets:
            break
        print(compute(gets))
