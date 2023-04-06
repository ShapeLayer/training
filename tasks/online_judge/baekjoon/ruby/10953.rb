n = gets.to_i
for i in 1..n do
  a, b = gets.split(',').map(&:to_i)
  puts a + b
end