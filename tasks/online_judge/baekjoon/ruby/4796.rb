i = 0
while true do
  i += 1
  l, p, v = gets.split(' ').map(&:to_i)
  if l == 0 && p == 0 && v == 0 then
    break
  else
    puts "Case %d: %d" % [i, l * (v / p) + [l, v % p].min]
  end
end