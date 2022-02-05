use std::{io, collections::VecDeque, cmp};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let t: i32 = puts.trim().parse::<i32>().unwrap();
  for _ in 0..t {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    let (n, k) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    println!("k {}", k);
    // map = key: previous, value: next
    let mut map: Vec<Vec<i32>> = vec![Vec::new(); (n+1) as usize];
    // during
    let mut puts = String::from("0 ");
    io::stdin().read_line(&mut puts).unwrap();
    let during: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    println!("{:?}", during);
    // incomes = key: next
    let mut incomes: Vec<i32> = vec![0; (n+1) as usize];
    for j in 0..k {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).unwrap();
      let (prev, next) = {
        let split: Vec<i32> = puts.split_whitespace()
          .map(|x| x.parse::<i32>().unwrap())
          .collect();
        (split[0], split[1])
      };
      map[prev as usize].append(&mut vec![next]);
      incomes[next as usize] += 1;
      println!("_ {}", j);
    }
    println!("{:?}", map);
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    // target = terminal point
    let target: i32 = puts.trim().parse::<i32>().unwrap();
    let mut queue: VecDeque<i32> = VecDeque::new();
    // Processing (init)
    let mut elapsed_time: Vec<i32> = vec![0; (n+1) as usize];
    for i in 1..n+1 {
      if incomes[i as usize] == 0 {
        queue.push_back(i);
      }
    }
    // Processing (main)
    while queue.len() != 0 {
      let now = queue.pop_front().unwrap();
      if incomes[now as usize] != 0 {
        continue;
      }
      elapsed_time[now as usize] = during[now as usize];
      println!("elapsed_time {:?} queue {:?}", elapsed_time, queue);
      for i in 1..map.len() {
        println!("i: {}, map[i]: {:?}", i, map[i]);
        if map[i as usize].contains(&now) {
          elapsed_time[now as usize] = cmp::max(elapsed_time[now as usize], elapsed_time[now as usize] + elapsed_time[i as usize]);
        }
      }
      println!("elapsed_time {:?} queue {:?}", elapsed_time, queue);
      for item in &map[now as usize] {
        incomes[*item as usize] -= 1;
        queue.push_back(*item);
      }
    }
    println!("{:?}", elapsed_time);
  }
}