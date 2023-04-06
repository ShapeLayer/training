t = gets.to_i

for i in 0..t-1 do
  j, n = gets.split.map(&:to_i)
  boxes = Array.new(n)
  for k in 0..n-1 do
    r, c = gets.split.map(&:to_i)
    boxes[k] = r*c
  end
  boxes = boxes.sort.reverse
  out = 0
  for k in 0..n-1 do
    if j <= 0
      out = k
      break
    end
    j -= boxes[k]
  end
  puts out
end