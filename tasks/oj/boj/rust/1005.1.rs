// BFS: TimeOver
use std::{io::{BufRead, BufWriter, Write}, collections::VecDeque};

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  // Input testcase (t)
  let mut puts = String::new();
  stdin.read_line(&mut puts).ok();
  let t: i32 = puts.trim().parse::<i32>().unwrap();
  for _ in 0..t {
    // Input n(number of buildings), k(number of order of buildings)
    puts.clear();
    stdin.read_line(&mut puts).ok();
    let (n, k) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    // Input times of during building buildings
    puts = String::from("0 ");
    stdin.read_line(&mut puts).ok();
    let during: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    // Input order of buildings
    let mut incomes: Vec<i32> = vec![0; (n+1) as usize];
     // map[key: prev] = value: vec![next]
    let mut map: Vec<Vec<i32>> = vec![Vec::new(); (n+1) as usize];
     // requirements[key: next] = value: vec![prev]
    let mut requirements: Vec<Vec<i32>> = vec![Vec::new(); (n+1) as usize];
    for __ in 0..k {
      puts.clear();
      stdin.read_line(&mut puts).ok();
      let (prev, next) = {
        let split: Vec<i32> = puts.split_whitespace()
          .map(|x| x.parse::<i32>().unwrap())
          .collect();
        (split[0], split[1])
      };
      map[prev as usize].append(&mut vec![next]);
      requirements[next as usize].append(&mut vec![prev]);
      incomes[next as usize] += 1;
    }
    // Input target building(terminal point)
    puts.clear();
    stdin.read_line(&mut puts).ok();
    let target: i32 = puts.trim().parse::<i32>().unwrap();
    // Init queue
    let mut queue: VecDeque<i32> = VecDeque::new();
    for i in 1..n+1 {
      if incomes[i as usize] == 0 {
        queue.push_back(i);
      }
    }
    // Process queue
    let mut elapsed_time: Vec<i32> = vec![0; (n+1) as usize];
    while !queue.is_empty() {
      let now = queue.pop_front().unwrap();
      if incomes[now as usize] != 0 { continue; }
      // Update queue
      for dot in &map[now as usize] {
        queue.push_back(*dot);
        if incomes[*dot as usize] != 0 {
          incomes[*dot as usize] -= 1;
        }
      }
      let mut prev_elapsed_times: Vec<i32> = Vec::new();
      for prev in &requirements[now as usize] {
        prev_elapsed_times.append(&mut vec![elapsed_time[*prev as usize]])
      }
      let mut prev_elapsed_time = 0;
      match prev_elapsed_times.iter().max() {
        Some(x) => prev_elapsed_time = *x,
        None => prev_elapsed_time = 0
      };
      elapsed_time[now as usize] = during[now as usize] + prev_elapsed_time;
    }
    writeln!(stdout, "{}", elapsed_time[target as usize]).ok();
  }
}