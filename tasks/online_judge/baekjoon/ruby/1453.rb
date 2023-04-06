arr = Array.new(1001)
n = gets.to_i
input = gets.split().map(&:to_i)
outs = 0
for i in input do
  if !arr[i] then
    arr[i] = true
  else
    outs += 1
  end
end
puts outs