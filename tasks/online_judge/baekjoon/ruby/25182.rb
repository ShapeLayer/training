n = gets.to_i
res_2n, res_max = 0, 1
$M = 1e9.to_i + 7
for i in 1..n
  res_2n = (res_2n + ((i * i) % $M) * (i + 1) % $M) % $M
end
for i in 2..n
  res_max = (((res_max * i) % $M) * i) % $M
end
puts "%d %d" % [res_2n, res_max]
