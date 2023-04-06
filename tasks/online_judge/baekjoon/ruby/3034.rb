n, w, h = gets.split.map(&:to_i)
for i in 1..n
  b = gets.to_i
  if b <= w || b <= h then puts "DA"
  elsif b <= Integer.sqrt((w * w) + (h * h)) then puts "DA"
  else puts "NE"
  end
end
