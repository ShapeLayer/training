cycle = 'ABCDEFGHIJKL'

def compute(n: int):
    n = (n - 1984) % 60
    sip_gan_idx = n % 10
    sip_ie_zi_idx = n % 12
    return f'{cycle[sip_ie_zi_idx]}{sip_gan_idx}'

if __name__ == '__main__':
    print(compute(int(input())))
