use std::{io, cmp};

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n: i32 = gets.trim().parse().unwrap();
  let mut damages: Vec<i32> = Vec::new();
  let mut greetings: Vec<i32> = Vec::new();
  let mut states: Vec<Vec<i32>> = vec![vec![0; (n+1) as usize]; 100 as usize];
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  damages = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  greetings = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  for damage in 1..100 {
    for grt in 1..n+1 {
      if damages[(grt-1) as usize] <= damage {
        states[damage as usize][grt as usize] = cmp::max(
          states[(damage-damages[(grt-1) as usize]) as usize][(grt-1) as usize] + greetings[(grt-1) as usize],
          states[damage as usize][(grt-1) as usize]
        );
      } else {
        states[damage as usize][grt as usize] = states[damage as usize][(grt-1) as usize];
      }
    }
  }
  println!("{}", states[99][n as usize]);
}