get = gets.strip
if get.length == 2 then
  puts get.chars.map(&:to_i).sum
elsif get.length == 3 then
  if get[1] == '0' then
    puts (get[0]+get[1]).to_i + get[2].to_i
  else
    puts get[0].to_i + (get[1]+get[2]).to_i
  end
else
  puts (get[0]+get[1]).to_i + (get[2]+get[3]).to_i
end