use std::io;

struct Solution {
  parents: Vec<i32>
}
impl Solution {
  fn main(&mut self) {
    let mut gets = String::new();
    io::stdin().read_line(&mut gets).ok();
    let (n, m) = {
      let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
      (split[0], split[1])
    };
    self.parents = (0..n+1).collect::<Vec<i32>>();
    for _i in 0..m {
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
    let mut roots = vec![0; (n+1) as usize];
    for i in 0..n+1 {
      let parent = self.find(i);
      roots[parent as usize] = 1;
    }
    let mut counts = 0;
    for i in 1..n+1 {
      if roots[i as usize] == 1 { counts += 1; }
    }
    println!("{}", counts);
  }
  fn find(&mut self, n: i32) -> i32 {
    if n == self.parents[n as usize] { return n; }
    self.find(self.parents[n as usize])
  }
  fn merge(&mut self, a: i32, b: i32) {
    let (pa, pb) = (self.find(a), self.find(b));
    if pa < pb { self.parents[pb as usize] = pa; }
    else { self.parents[pa as usize] = pb; }
  }
}

fn main() {
  let mut solution = Solution {
    parents: Vec::new()
  };
  solution.main();
}