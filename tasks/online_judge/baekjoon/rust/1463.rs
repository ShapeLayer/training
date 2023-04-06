use std::{io, cmp};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  let mut dp: Vec<i32> = vec![0; (n+1) as usize];
  for i in 2..n+1 {
    if i % 6 == 0 {
      dp[i as usize] = cmp::min(dp[(i-1) as usize] + 1, cmp::min(dp[(i/2) as usize] + 1, dp[(i/3) as usize] + 1));
    } else if i % 3 == 0 {
      dp[i as usize] = cmp::min(dp[(i-1) as usize] + 1, dp[(i/3) as usize] + 1);
    } else if i % 2 == 0 {
      dp[i as usize] = cmp::min(dp[(i-1) as usize] + 1, dp[(i/2) as usize] + 1);
    } else {
      dp[i as usize] = dp[(i-1) as usize] + 1;
    }
  }
  println!("{}", dp[n as usize]);
}