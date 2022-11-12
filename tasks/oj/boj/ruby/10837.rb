k, c = gets.to_i, gets.to_i
for _i in 1..c
  m, n = gets.split.map(&:to_i)
  if m - n == 0 then
    puts 1
    next
  end
  remain_turns = k - ((m > n) ? m : n)
  dt = m - n > 0 ? m - n : n - m
  if m > n then
    if dt - remain_turns <= 2 then
      puts 1
    else
      puts 0
    end
  else
    if dt - remain_turns <= 1 then
      puts 1
    else 
      puts 0
    end
  end
end
