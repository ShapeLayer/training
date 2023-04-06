use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (e, s, m) = {
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  let mut y = 1;
  while (y - e) % 15 != 0 || (y - s) % 28 != 0 || (y - m) % 19 != 0 {
    y += 1;
  }
  println!("{}", y);
}