x, k = gets.split.map(&:to_i)
if k * 7 <= x then puts k * 7000
elsif k * 3.5 <= x then puts k * 3500
elsif k * 1.75 <= x then puts k * 1750
else puts 0
end
