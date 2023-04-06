t = gets.to_i

dic = Hash.new

for i in 0..t-1 do
  n = gets.to_i
  if dic[n]
    dic[n] += 1
  else
    dic[n] = 1
  end
end

max = dic.values.sort.reverse[0]
idx = dic.key(max)
for key in dic.keys
  if dic[key] == max && idx > key
    idx = key
  end
end
puts idx