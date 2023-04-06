while true
  nums = [0] * 10
  line = gets
  if line.strip == '0' then break end
  n_str, arr_str = line.split(/ /, 2)
  n = n_str.to_i
  arr = arr_str.split().map(&:to_i).sort
  min = 0
  for item in arr
    nums[item] += 1
    if min == 0 then min = item end
  end
  res = 0
  suspend = -1
  ptr = 1
  offset = 1
  init = -1
  if n % 2 == 1 then
    nums[min] -= 1
    init = min
  end
  while ptr < 10
    if nums[ptr] <= 0 then
      ptr += 1
      next
    end
    if (res != 0 || (res == 0 && n % 2 == 1)) && nums[0] > 0 then
      if suspend == -1 then
        suspend = 0
        nums[0] -= 1
        next
      end
    end
    if suspend == -1 then
      nums[ptr] -= 1
      suspend = ptr
      next
    end
    a, b = suspend, -1
    if res != 0 && nums[0] > 0 then
      b = 0
      nums[0] -= 1
    else
      b = ptr
      nums[ptr] -= 1
    end
    res = res * 10 + a + b
    offset *= 10
    suspend = -1
  end
  if init != -1 then
    res += init * offset
  end
  puts res
  puts init
end

'''
WA Sidecase
input:                      output:
10 9 8 7 6 5 0 1 2 3 4      34047
0

refer:
https://www.acmicpc.net/board/view/58156
'''