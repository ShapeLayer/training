$shapes = ['NIL'] * 10
$outer_colors = ['NIL'] * 10
$inner_colors = ['NIL'] * 10

def query(a, b, c)
  results = [false] * 3
  if $shapes[a] == $shapes[b] && $shapes[b] == $shapes[c] then results[0] = true
  elsif $shapes[a] != $shapes[b] && $shapes[b] != $shapes[c] && $shapes[c] != $shapes[a] then results[0] = true 
  end
  
  if $outer_colors[a] == $outer_colors[b] && $outer_colors[b] == $outer_colors[c] then results[1] = true
  elsif $outer_colors[a] != $outer_colors[b] && $outer_colors[b] != $outer_colors[c] && $outer_colors[c] != $outer_colors[a] then results[1] = true 
  end

  if $inner_colors[a] == $inner_colors[b] && $inner_colors[b] == $inner_colors[c] then results[2] = true
  elsif $inner_colors[a] != $inner_colors[b] && $inner_colors[b] != $inner_colors[c] && $inner_colors[c] != $inner_colors[a] then results[2] = true
  end
  
  flag = true
  for i in 0..2
    if !results[i] then flag = false end
  end
  return flag
end

for i in 1..9
  $shapes[i], $outer_colors[i], $inner_colors[i] = gets.split()
end

queried = Array.new(10) { Array.new(10) { Array.new(10, false) } }
remains = 0
for i in 1..9
  for j in 1..9
    for k in 1..9
      if i < j && j < k then
        queried[i][j][k] = query(i, j, k)
        if queried[i][j][k] then remains += 1 end
      else next
      end
    end
  end
end

scores = 0
h_declared = Array.new(10) { Array.new(10) { Array.new(10, false) } }
g_declared = false
for _i in 1..gets.to_i
  query = gets.strip
  if query == 'G' then
    if !g_declared && remains == 0 then
      scores += 3
      g_declared = true
    else
      scores -= 1
    end
  else
    q, vals = query.split(/ /, 2)
    a, b, c = vals.split().map(&:to_i).sort
    if !h_declared[a][b][c] && queried[a][b][c] then
      remains -= 1
      h_declared[a][b][c] = true
      scores += 1
    else
      scores -= 1
    end
  end
end

puts scores