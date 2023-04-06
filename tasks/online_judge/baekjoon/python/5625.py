n = int(input())
std = {}
for i in range(n):
    name, date, month, year = input().split()
    date, month, year = map(int, (date, month, year))
    if year not in std:
        std[year] = {}
    if month not in std[year]:
        std[year][month] = {}
    std[year][month][date] = name
min_year = sorted(std.keys())[-1]
min_month = sorted(std[min_year].keys())[-1]
min_date = sorted(std[min_year][min_month].keys())[-1]
max_year = sorted(std.keys())[0]
max_month = sorted(std[max_year].keys())[0]
max_date = sorted(std[max_year][max_month].keys())[0]
print(std[min_year][min_month][min_date])
print(std[max_year][max_month][max_date])
