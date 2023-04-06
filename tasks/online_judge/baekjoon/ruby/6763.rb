limit, record = gets.to_i, gets.to_i
res = limit - record
if res >= 0 then
  puts 'Congratulations, you are within the speed limit!'
elsif res >= -20 then
  puts 'You are speeding and your fine is $100.'
elsif res >= -30 then
  puts 'You are speeding and your fine is $270.'
else
  puts 'You are speeding and your fine is $500.'
end