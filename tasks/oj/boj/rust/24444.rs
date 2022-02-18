use std::{io, collections::VecDeque};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let (n, m, r) = {
    let split: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  let mut map = vec![Vec::new(); (n+1) as usize];
  for _i in 0..m {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (u, v) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    map[u as usize].append(&mut vec![v]);
    map[v as usize].append(&mut vec![u]);
  }
  let mut visited = vec![0; (n+1) as usize];
  let mut counts: i32 = 0;
  let mut queue: VecDeque<i32> = VecDeque::new();
  queue.push_back(r);
  while !queue.is_empty() {
    let now = queue.pop_front().unwrap();
    if visited[now as usize] != 0 { continue; }
    counts += 1;
    visited[now as usize] = counts;
    map[now as usize].sort();
    for n in &map[now as usize] {
      if visited[*n as usize] == 0 {
        queue.push_back(*n);
      }
    }
  }
  println!("{}", visited[1..].iter().map(|x| x.to_string()).collect::<Vec<String>>().join("\n"));
}