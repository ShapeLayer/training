input = gets.strip
word_counts = [0, 0]
for i in 0..(input.length-3)
  word_flag = -1
  if input[i] == 'I' || input[i] == 'J' then
    if input[i] == 'J' then word_flag = 0
    else word_flag = 1
    end
    unless input[i + 1] == 'O' && input[i + 2] == 'I' then
      word_flag = -1
    end
  end
  if word_flag != -1 then
    word_counts[word_flag] += 1
  end
end
puts word_counts[0]
puts word_counts[1]
