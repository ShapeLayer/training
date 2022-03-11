sc = []
for i in 1..4 do
  sc += [gets.to_i]
end
li = []
for i in 1..2 do
  li += [gets.to_i]
end
puts sc.sum - sc.min + li.max