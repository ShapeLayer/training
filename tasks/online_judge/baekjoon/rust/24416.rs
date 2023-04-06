use std::io;

struct Solution {
  code1_runs: i32,
  code2_runs: i32,
  f: Vec<i32>
}
impl Solution {
  fn main(&mut self) {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let n = puts.trim().parse::<i32>().unwrap();
    self.f = vec![0; (n+1) as usize];
    self.f[1] = 1;
    self.f[2] = 1;
    self.fib(n);
    self.fibonacci(n);
    println!("{} {}", self.code1_runs, self.code2_runs);
  }
  
  fn fib(&mut self, n: i32) -> i32 {
    self.code1_runs += 1;
    if n == 1 || n == 2 {
      return 1
    }
    self.fib(n-1) + self.fib(n-2)
  }

  fn fibonacci(&mut self, n: i32) -> i32 {
    self.code2_runs += 1;
    for i in 3..n+1 {
      self.f[i as usize] = self.f[(i-1) as usize] + self.f[(i-2) as usize];
    }
    self.f[n as usize]
  }
}

fn main() {
  let mut solution = Solution { code1_runs: 0, code2_runs: 0, f: Vec::new() };
  solution.main();
}