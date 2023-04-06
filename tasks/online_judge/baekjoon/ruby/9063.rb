n = gets.to_i
x, y = gets.split().map(&:to_i)
minx, maxx, maxy, miny = x, x, y, y
for _i in 2..n
  x, y = gets.split().map(&:to_i)
  if minx > x then minx = x end
  if maxx < x then maxx = x end
  if miny > y then miny = y end
  if maxy < y then maxy = y end
end
puts (maxx - minx) * (maxy - miny)
