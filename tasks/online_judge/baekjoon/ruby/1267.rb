n = gets.to_i
arr = gets.split().map(&:to_i)

y, m = 0, 0
for i in 0..n-1 do
  y += (arr[i]/30.0).ceil * 10
  if arr[i] % 30 == 0 then y += 10 end
  m += (arr[i]/60.0).ceil * 15
  if arr[i] % 60 == 0 then m += 15 end
end

if y < m then
  puts "Y %d" % y
elsif y > m then
  puts "M %d" % m
else
  puts "Y M %d" % y
end