n = gets.to_i
inputs = gets.bytes.map { |x| x-96 }
sums = 0
for i in 0..n-1 do
  sums += ((31 ** i) * inputs[i]) % 1234567891
end
puts sums % 1234567891