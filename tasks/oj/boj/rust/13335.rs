use std::{io, collections::VecDeque};

fn main() {
  // Input
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let (n, w, l) = {
    let split: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let a: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  // Process
  let mut bridge: VecDeque<i32> = VecDeque::new();
  let mut truck_pointer: i32 = 0;
  let mut elapsed_time: i32 = 0;
  while truck_pointer < n {
    if bridge.len() == w as usize {
      bridge.pop_front();
    }
    if bridge.iter().sum::<i32>() + a[truck_pointer as usize] <= l {
      bridge.push_back(a[truck_pointer as usize]);
      truck_pointer += 1;
    } else {
      bridge.push_back(0);
    }
    elapsed_time += 1;
  }
  // Print result
  println!("{}", elapsed_time + w);
}