input = gets
input.gsub!('6', '5')
min = input.split.map(&:to_i).sum
input.gsub!('5', '6')
max = input.split.map(&:to_i).sum
puts "%d %d" % [min, max]
