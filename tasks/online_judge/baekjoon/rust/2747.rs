use std::io;

struct Solution {
  dp: Vec<i32>
}
impl Solution {
  fn main(&mut self) {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let n = puts.trim().parse::<i32>().unwrap();
    self.dp = vec![-1; (n+1) as usize];
    self.dp[0] = 0;
    self.dp[1] = 1;
    println!("{}", self.fibo(n));
  }
  
  fn fibo(&mut self, n: i32) -> i32 {
    if self.dp[n as usize] == -1 {
      self.dp[n as usize] = self.fibo(n-1) + self.fibo(n-2);
    }
    self.dp[n as usize]
  }
}

fn main() {
  let mut solution = Solution {
    dp: Vec::new()
  };
  solution.main();
}