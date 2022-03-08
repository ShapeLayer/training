m, d = gets.to_i, gets.to_i
if m < 2 || m == 2 && d < 18 then
  puts "Before"
elsif m == 2 && d == 18 then
  puts "Special"
else
  puts "After"
end