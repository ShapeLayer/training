from sys import stdin, stdout
input = stdin.readline

def interact_wrapper(n: int):
    result = compute(n)
    for each in result:
        print(f'? {each}')
        interact_result: list[str] = input().strip()
        if interact_result[0] == 'Y':
            print(f'! {each}')
            break
        stdout.flush()
    
def compute(n: int) -> list[int]:
    return [i for i in range(1, n + 1)]

if __name__ == '__main__':
    n = int(input())
    interact_wrapper(n)
