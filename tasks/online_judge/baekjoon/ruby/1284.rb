while true
  n = gets.to_i
  res = 1
  if n == 0 then break end
  while n != 0
    now = n % 10
    n /= 10
    if now == 1 then
      res += 2
    elsif now == 0 then
      res += 4
    else
      res += 3
    end
    res += 1
  end
  puts res
end