from ast import literal_eval

def decrypt(keymap_raw: str, key: str, encrypted: str) -> str:
    keymap = literal_eval(keymap_raw)
    keysum = sum([ord(char) for char in key])
    dict_ = {str(keymap[key]-keysum): chr(key-keysum) for key in keymap}
    res = ''.join([dict_[val] for val in encrypted.split(',')[:-1]])
    return res

if __name__ == '__main__':
    flag = True
    while flag:
        keymap_raw, key, encrypted = input('Input encrypted secret codes: '), input('Input password: '), input('Input encrypted text: ')
        print(decrypt(keymap_raw, key, encrypted))
        user_ctrl = input('Do you want to proceed to the next text decryption? (y) ')
        flag = user_ctrl and user_ctrl in 'yY'