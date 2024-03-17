prev = io.read("*n")
while true do
  now = io.read("*n")
  if now == 999 then break end
  print(string.format("%.2f", now - prev))
  prev = now
end
