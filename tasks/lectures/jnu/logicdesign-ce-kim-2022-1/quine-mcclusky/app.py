class Solution:
    binary_size: int   # Number of input parameters
    nm: int  # Number of M parameters
    nd: int  # Number of don't care parameters
    params: list[str]    # Array of Parameters
    majors: list[int]    # Array of major parameters' number
    dontcares: list[str] # Array of don't care parameters' number
    param_vals: list = []

    def __init__(self, binary_size: int, params: list[str], nm: int, nd: int, majors: list[int], dontcares: list[int]):
        self.binary_size = binary_size
        self.params = params
        self.nm = nm
        self.nd = nd
        self.majors = majors
        self.dontcares = dontcares
        self.param_vals += [[EachParam(majors[i], binary_size) for i in range(nm)] + [EachParam(dontcares[i], binary_size) for i in range(nd)]]
    
    def __str__(self):
        return f'''({self.binary_size}) {self.params}
        Majors: ({self.nm}) {self.majors}
        Dontcares: ({self.nd}) {self.dontcares}
        ParamList:
        {self.param_vals}'''

class EachParam:
    n: int              # Parameter Number
    binary_size: int    # Parameters' processing bits
    binary: list        # Parameters' bits
    n1: int = 0         # Number of ones

    def __init__(self, n: int, binary_size: int):
        self.n = n
        self.binary_size = binary_size
        self.binary = [-1] * n
        num = n
        for i in range(binary_size):
            if num % 2:
                self.binary[n-i-1] = 1
                n1 += 1
            else:
                self.binary[n-i-1] = 0
            num //= 2

    def __str__(self):
        return f'{self.n}: ({self.n1}) {self.binary}'

if __name__ == '__main__':
    np = int(input())
    params = input().split()
    nm, nd = map(int, input().split())
    majors = list(map(int, input().split()))
    dontcares = list(map(int, input().split()))
    solution: Solution = Solution(np, params, nm, nd, majors, dontcares)
    print(solution)
