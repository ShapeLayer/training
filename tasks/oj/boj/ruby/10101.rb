angles = []
for i in 0..2 do
  angles.append(gets.to_i)
end
if angles.sum != 180 then
  puts "Error"
elsif angles[1] == angles[2] && angles[2] == angles[0] && angles[0] == angles[1] then
  puts "Equilateral"
elsif angles[1] != angles[2] && angles[2] != angles[0] && angles[0] != angles[1] then
  puts "Scalene"
else
  puts "Isosceles"
end