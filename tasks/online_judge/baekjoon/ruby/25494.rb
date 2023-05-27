for _i in 1..gets.to_i
  a, b, c = gets.split().map(&:to_i)
  res = 0
  for i in 1..a
    for j in 1..b
      for k in 1..c
        if i % j == j % k && j % k == k % i then
          res += 1
        end
      end
    end
  end
  puts res
end