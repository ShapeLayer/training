// https://4legs-study.tistory.com/121
use std::{io::{BufRead, BufWriter, Write}};

struct Solution {
  conns: Vec<Vec<i32>>,
  parents: Vec<i32>,
  level: Vec<i32>
}

impl Solution {
  pub fn new(conns: Vec<Vec<i32>>, size: i32) -> Solution {
    let mut solution: Solution = Solution { conns: conns, parents: vec![-1; (size+1) as usize], level: vec![-1; (size+1) as usize] };
    solution.parents[1] = 0;
    solution.level[1] = 0;
    solution.dfs(1, 0);
    solution
  }
  
  fn dfs(&mut self, prev: i32, prev_lv: i32) {
    for i in 0..self.conns[prev as usize].iter().count() {
      if self.parents[self.conns[prev as usize][i as usize] as usize] == -1 {
        self.parents[self.conns[prev as usize][i as usize] as usize] = prev;
        self.level[self.conns[prev as usize][i as usize] as usize] = prev_lv + 1;
        self.dfs(self.conns[prev as usize][i as usize] as i32, prev_lv + 1);
      }
    }
  }

  fn lca(&mut self, mut dots: Vec<i32>) -> i32 {
    if self.level[dots[0] as usize] < self.level[dots[1] as usize] {
      let tmp = dots[1];
      dots[1] = dots[0];
      dots[0] = tmp;
    }
    while self.level[dots[0] as usize] != self.level[dots[1] as usize] {
      dots[0] = self.parents[dots[0] as usize];
    }
    while dots[0] != dots[1] {
      dots[0] = self.parents[dots[0] as usize];
      dots[1] = self.parents[dots[1] as usize];
    }
    dots[0]
  }
}

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();
  stdin.read_line(&mut gets).ok();
  let n = gets.trim().parse::<i32>().unwrap();
  let mut conns: Vec<Vec<i32>> = vec![Vec::new(); (n+1) as usize];
  for _i in 0..(n-1) as usize {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    conns[split[0] as usize].append(&mut vec![split[1]]);
    conns[split[1] as usize].append(&mut vec![split[0]]);
  }
  let mut solution: Solution = Solution::new(conns, n);
  gets.clear();
  stdin.read_line(&mut gets).ok();
  let m = gets.trim().parse::<i32>().unwrap();
  for _i in 0..m {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let dots: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    writeln!(stdout, "{}", solution.lca(dots)).ok();
  }
}
