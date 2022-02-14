while true do
  arr = gets.split.map(&:to_i)
  arr.sort
  if arr[0] == 0 && arr[1] == 0 && arr[2] == 0 then
    break
  end
  if arr[2] >= arr[0] + arr[1] then
    puts "Invalid"
  elsif arr[0] == arr[1] && arr[1] == arr[2] then
    puts "Equilateral"
  elsif arr[0] != arr[1] && arr[1] != arr[2] && arr[2] != arr[0] then
    puts "Scalene"
  else
    puts "Isosceles"
  end
end