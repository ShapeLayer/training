for _i in 1..gets.to_i
  bigo, query = gets.split(/ /, 2)
  n, t, l = query.split().map(&:to_i)
  pass = false
  if bigo == 'O(N)' then
    pass = n * t <= 1e8.to_i * l
  elsif bigo == 'O(N^2)' then
    pass = n * n * t <= 1e8.to_i * l
  elsif bigo == 'O(N^3)' then
    pass = n * n * n * t <= 1e8.to_i * l
  elsif bigo == 'O(2^N)' then
    pass = 2.pow(n) * t <= 1e8.to_i * l
  elsif bigo == 'O(N!)' then
    temp = n
    n -= 1
    while n > 1
      pass = temp * t < 1e8.to_i * l
      if !pass then break end
      temp *= n
      n -= 1
    end
    pass = temp * t < 1e8.to_i * l
  end
  if pass then
    puts 'May Pass.'
  else
    puts 'TLE!'
  end
end