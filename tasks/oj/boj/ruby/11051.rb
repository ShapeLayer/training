# 이항계수 2: 파스칼의 삼각형
# 이항계수[N_number][K_number] = 이항계수[N_number - 1][K_number-1] + 이항계수[N_number-1][K_number]
n, k = gets.split.map(&:to_i)

dp = Array.new(1001){Array.new(1001, 0)}

for i in 1..n
  for j in 0..n
    if i == j || j == 0 then
      dp[i][j] = 1
    else
      dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10007
    end
  end
end
puts dp[n][k]