a, b = gets.split().map(&:to_i)
if a - b < 0 || (a - b) % 2 != 0 then
  puts -1
else
  res = [(a+b)/2, (a-b)/2]
  res.sort.reverse
  puts "%d %d" % res
end