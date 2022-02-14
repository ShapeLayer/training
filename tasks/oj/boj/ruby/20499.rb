k, d, a = gets.split("/").map(&:to_i)
if d == 0 then
  puts "hasu"
elsif k + a < d then
  puts "hasu"
else
  puts "gosu"
end