cases = {
    'fdsajkl;': 'in-out',
    'jkl;fdsa': 'in-out',
    'asdf;lkj': 'out-in',
    ';lkjasdf': 'out-in',
    'asdfjkl;': 'stairs',
    ';lkjfdsa': 'reverse'
}

if __name__ == '__main__':
    gets = input()
    print(cases[gets] if gets in cases else 'molu')
