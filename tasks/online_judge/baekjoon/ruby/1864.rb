map = {}
map["-"] = 0
map["\\"] = 1
map["("] = 2
map["@"] = 3
map["?"] = 4
map[">"] = 5
map["&"] = 6
map["%"] = 7
map["/"] = -1
while true do
  input = gets.strip
  if input == "#" then
    break
  end
  arr = input.split("")
  sums = 0
  for i in 0..(arr.length-1) do
    sums += map[arr[i]] * (8 ** (arr.length - i - 1))
  end
  puts sums
end