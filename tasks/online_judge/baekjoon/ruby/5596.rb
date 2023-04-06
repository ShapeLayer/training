scores = [0, 0]
for i in 0..1
  scores[i] = gets.split().map(&:to_i).sum
end
puts scores.max