$ORD = "A".ord - 1
for _i in 1..gets.to_i
  n, t = gets.split
  n = n.to_i
  if t == "C" then
    ord = gets.split.map(&:ord)
    ord.each do |char|
      print "%d " % (char - $ORD)
    end
    puts
  else
    ord = gets.split.map(&:to_i)
    ord.each do |char|
      print "%s " % [(char + $ORD)].pack("U")
    end
    puts
  end
end
