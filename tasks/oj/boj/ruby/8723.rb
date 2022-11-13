arr = gets.split.map(&:to_i).sort
if arr[0] == arr[1] && arr[1] == arr[2] then puts 2
elsif arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2] then puts 1
else puts 0
end
