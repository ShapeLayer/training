n = gets.to_i
t = []
for _i in 1..n
  t.append(gets.split.map(&:to_i))
end
for i in 1..n - 1
  for j in 0..i
    if j == 0 then t[i][0] += t[i - 1][0]
    elsif j == i then t[i][j] += t[i - 1][j - 1]
    else t[i][j] += t[i - 1][j - 1] > t[i - 1][j] ? t[i - 1][j - 1] : t[i - 1][j]
    end
  end
end
puts t[n-1].max
