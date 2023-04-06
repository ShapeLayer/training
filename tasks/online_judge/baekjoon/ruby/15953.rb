for _i in 1..gets.to_i do
  a, b = gets.split().map(&:to_i)
  price = 0
  if a == 0 then
  elsif a < 2 then
    price += 500
  elsif a < 4 then
    price += 300
  elsif a < 7 then
    price += 200
  elsif a < 11 then
    price += 50
  elsif a < 16 then
    price += 30
  elsif a < 22 then
    price += 10
  end
  if b == 0 then
  elsif b < 2 then
    price += 512
  elsif b < 4 then
    price += 256
  elsif b < 8 then
    price += 128
  elsif b < 16 then
    price += 64
  elsif b < 32 then
    price += 32
  end
  puts price * 10000
end