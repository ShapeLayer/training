use std::{io, collections::VecDeque};

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let t = gets.trim().parse::<i32>().unwrap();
  for _i in 0..t {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let (_n, m) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let mut queue: VecDeque<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    let mut pointer = m;
    let mut counts = 0;
    while !queue.is_empty() {
      let max = *queue.iter().max().unwrap();
      let now = queue.pop_front().unwrap();
      if now == max {
        counts += 1;
        if pointer == 0 {
          println!("{}", counts);
          break;
        }
      } else {
        queue.push_back(now);
      }
      pointer -= 1;
      if pointer < 0 {
        pointer = queue.len() as i32 - 1;
      }
    }
  }
}