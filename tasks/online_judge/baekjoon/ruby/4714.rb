while true
  x = gets.to_f
  if x == -1 then break
  end
  puts 'Objects weighing %.2f on Earth will weigh %.2f on the moon.' % [x, x*0.167]
end