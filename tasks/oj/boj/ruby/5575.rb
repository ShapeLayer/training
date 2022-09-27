for _i in 1..3
  nh, nm, ns, xh, xm, xs = gets.split().map(&:to_i)
  h, m, s = xh - nh, xm - nm, xs - ns
  if s < 0 then
    s += 60
    m -= 1
  end
  if m < 0 then
    m += 60
    h -= 1
  end
  puts '%d %d %d' % [h, m, s]
end