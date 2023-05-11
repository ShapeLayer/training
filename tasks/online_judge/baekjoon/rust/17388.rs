use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (s, k, h) = {
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  if s + k + h >= 100 {
    println!("OK");
  } else {
    if s < k && s < h {
      println!("Soongsil");
    } else if k < s && k < h {
      println!("Korea");
    } else {
      println!("Hanyang")
    }
  }
}
