use std::io::{BufRead, BufWriter, Write};

struct Solution {
  size: i32,
  parents: Vec<i32>,
  conns: Vec<Vec<i32>>
}

impl Solution {
  pub fn new(size: i32) -> Solution {
    let mut solution = Solution {
      size: size,
      parents: vec![-1; (size+1) as usize],
      conns: vec![Vec::new(); (size+1) as usize]
    };
    for i in 0..(size+1) {
      solution.parents[i as usize] = i;
    }
    solution
  }

  fn dfs(&mut self, now: i32) {
    for i in 0..self.conns[now as usize].len() {
      if self.parents[self.conns[now as usize][i as usize] as usize] == self.conns[now as usize][i as usize] {
        self.parents[self.conns[now as usize][i as usize] as usize] = now;
        self.dfs(self.conns[now as usize][i as usize]);
      }
    }
  }
}

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();
  stdin.read_line(&mut gets).ok();
  let n: i32 = gets.trim().parse::<i32>().unwrap();
  let mut solution = Solution::new(n);
  for _i in 0..(n-1) {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let (a, b) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    solution.conns[a as usize].append(&mut vec![b]);
    solution.conns[b as usize].append(&mut vec![a]);
  }
  solution.dfs(1);
  for i in 2..(n+1) {
    writeln!(stdout, "{}", solution.parents[i as usize]).ok();
  }
}