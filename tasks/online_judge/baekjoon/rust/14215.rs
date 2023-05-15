use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (a, b, c): (i32, i32, i32) = {
    let mut split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    split.sort();
    (split[0], split[1], split[2])
  };
  let z = a + b - 1;
  let result: i32 = a + b + if c < z { c } else { z };
  println!("{}", result);
}
