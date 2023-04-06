use std::{io, cmp};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let arr: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let mut dp: Vec<i32> = vec![-1001; n as usize];
  dp[0] = arr[0];
  for i in 1..n {
    if dp[(i-1) as usize] > 0 && arr[i as usize] + dp[(i-1) as usize] > 0 {
      dp[i as usize] = arr[i as usize] + dp[(i-1) as usize];
    } else {
      dp[i as usize] = arr[i as usize];
    }
  }
  println!("{}", dp.iter().max().unwrap());
}