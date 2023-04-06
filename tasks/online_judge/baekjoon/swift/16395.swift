let gets = readLine()!.split(separator: " ")
let (n, m) = (Int(gets[0])!, Int(gets[1])!)
var dp: [[Int]] = []
for _ in 0...n {
  var puts: [Int] = []
  for j in 0...n {
    if j == 1 { puts += [1] }
    else { puts += [0] }
  }
  dp += [puts]
}
for i in 1...n {
  for j in 1...i {
    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
  }
}
print(dp[n][m])