use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let mut n: i32 = gets.trim().parse::<i32>().unwrap();
  n %= 8;
  let result = match n {
    1 => 1,
    2 | 0 => 2,
    3 | 7 => 3,
    4 | 6 => 4,
    5 => 5,
    _ => -1
  };
  println!("{}", result);
}
