n, w, h = gets.split.map(&:to_i)
for i in 1..n
  b = gets.to_i
  if b <= w || b <= h then puts "YES"
  elsif b <= Integer.sqrt((w * w) + (h * h)) then puts "YES"
  else puts "NO"
  end
end
