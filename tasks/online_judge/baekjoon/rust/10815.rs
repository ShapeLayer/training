// WA: Wrong Answer
use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let _m = puts.trim().parse::<i32>().unwrap();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let gets: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let n = puts.trim().parse::<i32>().unwrap();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let tofind: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let mut find: Vec<i32> = vec![0; n as usize];
  for i in 0..n {
    for card in &gets {
      if tofind[i as usize] == *card { find[i as usize] = 1; }
    }
  }
  println!("{}", find.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" "));
}