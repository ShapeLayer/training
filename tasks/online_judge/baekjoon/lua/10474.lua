while true do
  a = io.read("*n")
  b = io.read("*n")
  if a == b and a == 0 then
    break
  end
  print(string.format("%d %d / %d", a // b, a % b, b))
end
