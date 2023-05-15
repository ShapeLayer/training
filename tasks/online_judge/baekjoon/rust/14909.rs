use std::io;

fn compute(arr: Vec<i32>) -> i32 {
  let mut result: i32 = 0;
  for n in arr {
    if n > 0 {
      result += 1
    }
  }
  result
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let arr: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  println!("{}", compute(arr));
}
