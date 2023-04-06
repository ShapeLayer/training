n, m = gets.to_i, gets.to_i
arr = gets.split.map(&:to_i).sort
cnt, i, j = 0, 0, n - 1
while i < j
  if arr[i] + arr[j] == m then
    cnt += 1
    i += 1
    j -= 1
  elsif arr[i] + arr[j] < m then
    i += 1
  else
    j -= 1
  end
end
puts cnt
