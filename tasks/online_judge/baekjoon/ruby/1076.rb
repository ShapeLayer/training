colors = {}

colors["black"] = [0, 1]
colors["brown"] = [1, 10]
colors["red"] = [2, 100]
colors["orange"] = [3, 1000]
colors["yellow"] = [4, 10000]
colors["green"] = [5, 100000]
colors["blue"] = [6, 1000000]
colors["violet"] = [7, 10000000]
colors["grey"] = [8, 100000000]
colors["white"] = [9, 1000000000]

puts (colors[gets.strip!][0] * 10 + colors[gets.strip!][0]) * colors[gets.strip!][1]