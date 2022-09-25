# 이항계수 3: 페르마의 소정리

$mod = 1000000007

def fact(n)
  t = 1
  for i in 2..n
    t = (t * i) % $mod
  end
  return t
end

def proc(n, k)
  if k == 0 then return 1
  elsif k == 1 then return n
  end

  t = proc(n, k/2)
  if k % 2 == 1 then return t * t * n % $mod
  else return t * t % $mod
  end
end

n, k = gets.split.map(&:to_i)

top = fact(n)
bot = fact(n-k) * fact(k) % $mod

puts top * proc(bot, $mod-2) % $mod