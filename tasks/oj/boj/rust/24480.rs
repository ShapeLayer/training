use std::io;

struct Solution {
  map: Vec<Vec<i32>>,
  visited: Vec<i32>,
  counts: i32
}
impl Solution {
  fn main(&mut self) {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (n, m, r) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1], split[2])
    };
    self.map = vec![Vec::new(); (n+1) as usize];
    for _i in 0..m {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).ok();
      let (u, v) = {
        let split: Vec<i32> = puts.split_whitespace()
          .map(|x| x.parse::<i32>().unwrap())
          .collect();
        (split[0], split[1])
      };
      self.map[u as usize].append(&mut vec![v]);
      self.map[v as usize].append(&mut vec![u]);
    }
    self.visited = vec![0; (n+1) as usize];
    self.dfs(r);
    println!("{}", self.visited[1..].iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" "));
  }

  fn dfs(&mut self, r: i32) {
    self.counts += 1;
    self.visited[r as usize] = self.counts;
    self.map[r as usize].sort();
    self.map[r as usize].reverse();
    for i in 0..self.map[r as usize].len() {
      let v = self.map[r as usize][i as usize];
      if self.visited[v as usize] == 0 {
        self.dfs(v);
      }
    }
  }
}

fn main() {
  let mut solution = Solution {
    map: Vec::new(),
    visited: Vec::new(),
    counts: 0
  };
  solution.main();
}