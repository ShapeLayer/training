from sys import stdin
input = stdin.readline

d = {
    'Algorithm': '204',
    'DataAnalysis': '207',
    'ArtificialIntelligence': '302',
    'CyberSecurity': 'B101',
    'Network': '303',
    'Startup': '501',
    'TestStrategy': '105'
}

for _i in range(int(input())):
    print(d[input().strip()])
