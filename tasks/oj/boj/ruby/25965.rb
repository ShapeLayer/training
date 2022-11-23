for _i in 1..gets.to_i
  m = gets.to_i
  costs = []
  for _j in 1..m
    costs += [gets.split.collect{|x| x.to_i}]
  end
  k, d, a = gets.split.map(&:to_i)
  donate = 0
  for i in 0..m-1
    mission_result = k * costs[i][0] - d * costs[i][1] + a * costs[i][2]
    donate += mission_result > 0 ? mission_result : 0
  end
  puts donate
end
