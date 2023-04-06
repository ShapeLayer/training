n = gets.to_i
s = gets.split.map(&:to_i)
sorted = s.sort
for i in 0..n-1
  unless Integer.sqrt(s[i] * sorted[i]).pow(2) == s[i] * sorted[i] then
    puts "NO"
    exit
  end
end
puts "YES"
