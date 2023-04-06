$N, $M = 0, 0
$ARR = []
$RES = []

def proc(cnt, init)
  if cnt == $M then
    for i in 0..$M-1
      print "%d " % $RES[i]
    end
    puts
    return
  end

  prev = nil
  for i in init..$N-1
    if prev != $ARR[i] then
      $RES[cnt] = $ARR[i]
      prev = $ARR[i]
      proc(cnt+1, i)
    end
  end
end

if __FILE__ == $0 then
  $N, $M = gets.split.map(&:to_i)
  $ARR = gets.split.map(&:to_i).sort
  proc(0, 0)
end
