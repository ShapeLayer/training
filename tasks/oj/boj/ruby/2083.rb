while true
  name, age, weight = gets.split()
  age, weight = age.to_i, weight.to_i
  if name == '#' && age == 0 && weight == 0 then
    break
  elsif age > 17 || weight >= 80 then
    puts '%s Senior' % [name]
  else
    puts '%s Junior' % [name]
  end
end