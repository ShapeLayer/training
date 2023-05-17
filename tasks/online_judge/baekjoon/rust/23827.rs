use std::{io::{BufRead, BufWriter, Write}};

fn compute(n: i64, nums: Vec<i64>) -> i64 {
  let mut part_sum: Vec<i64> = vec![0; n as usize];
  let mut result: i64 = 0;
  
  part_sum[0] = nums[0];
  for i in 1..n {
    part_sum[i as usize] = part_sum[(i - 1) as usize] + nums[i as usize];
  }
  for i in 0..((n - 1) as usize) {
    result += nums[i as usize] * (part_sum[(n - 1) as usize] - part_sum[i as usize]);
    result %= 1000000007;
  }
  result
}

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();

  stdin.read_line(&mut gets).ok();
  let n: i64 = gets.trim().parse().unwrap();
  gets.clear();
  stdin.read_line(&mut gets).ok();
  let nums: Vec<i64> = gets.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  let result: i64 = compute(n, nums);
  writeln!(stdout, "{}", result).ok();
}
