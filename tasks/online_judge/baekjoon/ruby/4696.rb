while true
  get = gets.to_f
  if get == 0 then
    break
  else
    puts '%.2f' % [1 + get + get**2 + get**3 + get**4]
  end
end