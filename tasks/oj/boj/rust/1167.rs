// WA: Wrong Answer

use std::io;

struct Solution {
  map: Vec<Vec<(i32, i32)>>,
  distance: Vec<i32>,
  max: i32
}
impl Solution {
  fn main(&mut self) {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let v: i32 = puts.trim().parse::<i32>().unwrap();
    self.map = vec![Vec::new(); (v+1) as usize];
    let mut init: Vec<i32> = Vec::new();
    for _i in 0..v {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).ok();
      let (dot, conn): (i32, Vec<(i32, i32)>) = {
        let split: Vec<i32> = puts.split_whitespace()
          .map(|x| x.parse::<i32>().unwrap())
          .collect();
        let mut conn: Vec<(i32, i32)> = Vec::new();
        for i in (1..split.iter().len()-1).step_by(2) {
          conn.append(&mut vec![(split[i], split[i+1])])
        }
        (split[0], conn)
      };
      if conn.iter().len() == 1 {
        init.append(&mut vec![dot]);
      }
      self.map[dot as usize] = conn;
    }
    for i in init {
      self.distance = vec![-1; (v+1) as usize];
      self.distance[i as usize] = 0;
      self.dfs(i, -1, -1);
      let max_dis = *self.distance.iter().max().unwrap();
      if self.max < max_dis {
        self.max = max_dis;
      }
    }
    println!("{}", self.max);
  }

  fn dfs(&mut self, target: i32, prev: i32, distance: i32) {
    let dots: Vec<(i32, i32)> = self.map[target as usize].clone();
    if prev != -1 {
      self.distance[target as usize] = distance + self.distance[prev as usize];
    }
    for i in 0..dots.iter().len() {
      let dot = dots[i as usize].0;
      if self.distance[dot as usize] == -1 {
        self.dfs(dot, target, dots[i as usize].1);
      }
    }
  }
}

fn main() {
  let mut solution = Solution {
    map: Vec::new(),
    distance: Vec::new(),
    max: 0
  };
  solution.main();
}