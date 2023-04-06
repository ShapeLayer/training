puts 'Gnomes:'
for i in 1..gets.to_i
  arr = gets.split.map(&:to_i)
  if arr[0] <= arr[1] && arr[1] <= arr[2] then
    puts 'Ordered'
  elsif arr[0] >= arr[1] && arr[1] >= arr[2] then
    puts 'Ordered'
  else
    puts 'Unordered'
  end
end