// TO: Time Out
//  Using UnionFind

use std::io;

struct Solution {
  parents: Vec<i32>
}
impl Solution {
  fn main(&mut self) {
    let mut gets = String::new();
    io::stdin().read_line(&mut gets).ok();
    let n = gets.trim().parse::<i32>().unwrap();
    self.parents = (0..n+1).collect::<Vec<i32>>();
    for _i in 1..n {
      gets.clear();
      io::stdin().read_line(&mut gets).ok();
      let (a, b) = {
        let split: Vec<i32> = gets.split_whitespace()
          .map(|x| x.parse::<i32>().unwrap())
          .collect();
        (split[0], split[1])
      };
      self.merge(a, b);
    }
    for i in 2..n+1 {
      println!("{}", self.parents[i as usize]);
    }
  }

  fn find(&mut self, n: i32) -> i32 {
    if n == self.parents[n as usize] { return n; }
    self.find(self.parents[n as usize])
  }

  fn merge(&mut self, a: i32, b: i32) {
    let (pa, pb) = (self.find(a), self.find(b));
    if pa == 1 {
      self.parents[b as usize] = a;
    } else {
      self.parents[a as usize] = b;
    }
  }
}

fn main() {
  let mut solution = Solution {
    parents: Vec::new()
  };
  solution.main();
}