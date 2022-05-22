use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (n, k) = {
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1])
  };
  gets.clear();
  for i in 0..n {
    io::stdin().read_line(&mut gets).ok();
  }
  let var: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let mut dp: Vec<i32> = vec![0; (k+1) as usize];
  dp[0] = 1;
  for i in 0..n {
    for j in var[i as usize]..k+1 {
      dp[j as usize] += dp[(j-var[i as usize]) as usize];
    }
  }
  println!("{}", dp[k as usize]);
}
