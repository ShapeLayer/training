$N, $M = 0, 0
$PARENT, $KNOWS = [], []

def find(n)
  return n == $PARENT[n] ? n : find($PARENT[n])
end

def merge(a, b)
  a, b = find(a), find(b)
  if $KNOWS[a] == true && $KNOWS[b] == true then return end
  if $KNOWS[a] == true then $KNOWS[b] = true
  elsif $KNOWS[b] == true then $KNOWS[a] = true
  end

  if a < b then $PARENT[a] = b
  else $PARENT[b] = a
  end
end

if __FILE__ == $0 then
  $N, $M = gets.split.map(&:to_i)
  $PARENT = Array.new($N + 1) {|i| i}
  $KNOWS = Array.new($N + 1, false)
  knows = gets.split.map(&:to_i)
  parties = []
  for i in 1..knows[0]
    $KNOWS[knows[i]] = true
  end
  for _i in 1..$M
    people = gets.split.map(&:to_i) # 0 is info
    for i in 1..people[0] - 1
      merge(people[i], people[i + 1])
    end
    parties.append(people)
  end

  res = 0
  parties.each do |party|
    party_people_knows = false
    for i in 1..party[0]
      if $KNOWS[find(party[i])] == true then
        party_people_knows = true
        break
      end
    end
    unless party_people_knows then
      res += 1
    end
  end
  puts res
end
