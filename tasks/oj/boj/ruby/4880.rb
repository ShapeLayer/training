while true do
  a, b, c = gets.split().map(&:to_i)
  if a == 0 && b == 0 && c == 0 then
    break
  end
  if b - a == c - b then
    puts "AP %d" % [c + (b - a)]
  else
    puts "GP %d" % [c * (b / a)]
  end
end