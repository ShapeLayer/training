n = gets.to_i
if n == 1 then
  puts 1
elsif n % 2 == 1 then
  puts -1
else
  res = Array.new
  l, r = n, 1
  loop do
    res.append(l)
    l -= 2
    if res.length == n then break end
    res.append(r)
    r += 2
    if res.length == n then break end
  end
  puts res.join(" ")  
end
