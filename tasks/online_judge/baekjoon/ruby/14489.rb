d = gets.split(' ').map(&:to_i).sum
p = gets.to_i
if p*2 <= d then
  puts d - p*2
else
  puts d
end