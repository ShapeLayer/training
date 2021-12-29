use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts);
  let puts: Vec<i32> = puts.split_whitespace()
    .map(|i| i.parse::<i32>().unwrap())
    .collect();
  println!("{}", puts[0]+puts[1]);
  println!("{}", puts[0]-puts[1]);
  println!("{}", puts[0]*puts[1]);
  println!("{}", puts[0]/puts[1]);
  println!("{}", puts[0]%puts[1]);
}