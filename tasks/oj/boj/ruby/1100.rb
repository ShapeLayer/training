sums = 0
for i in 0..7 do
  row = gets.split("")
  for j in 0..7 do
    if (i % 2 == 0 && j % 2 == 0) || (i % 2 == 1 && j % 2 == 1) then
      if row[j] == "F" then
        sums += 1
      end
    end
  end
end
puts sums