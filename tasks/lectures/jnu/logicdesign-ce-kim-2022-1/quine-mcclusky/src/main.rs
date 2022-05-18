use std::{io, fmt};

struct Solution {
  n: i64, 
  nm: i64, 
  nd: i64,
  params: Vec<String>,
  majors: Vec<i64>,
  dontcares: Vec<i64>
}

impl Solution {
  pub fn new(n: i64, params: Vec<String>, nm: i64, nd: i64, majors: Vec<i64>, dontcares: Vec<i64>) -> Solution {
    let mut solution: Solution = Solution { n: n, nm: nm, nd: nd, params: params, majors: majors, dontcares: dontcares };
    solution.init();
    solution
  }

  fn init(&mut self) {

  }
}

impl fmt::Display for Solution {
  fn fmt(&self, &mut fmt::Formatter<'_>) -> fmt::Result {
    write!(f, "{}(bin: {}): {}", self.n, self.binary_size, self.binary)
  }
}

struct ParamPos {
  n: i64,
  binary_size: i64,
  binary: Vec<bool>
}

impl ParamPos {
  pub fn new(n: i64) -> ParamPos {
    let mut paramPos: ParamPos = ParamPos { n: n, binary_size: binary_size, binary: vec![false; n as usize] };
    paramPos.init();
    paramPos
  }
  
  fn init(&mut self) {
    let mut n = self.n;
    for i in 0..binary_size {
      self.binary[i as usize] = n % 2;
      n /= 2;
    }
  }
}

impl fmt::Display for ParamPos {
  fn fmt(&self, &mut fmt::Formatter<'_>) -> fmt::Result {
    write!(f, "{}(bin: {}): {}", self.n, self.binary_size, self.binary)
  }
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n: i64 = gets.trim().parse().unwrap();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let params: Vec<String> = gets.split_whitespace()
    .map(|x| String::from(x))
    .collect();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let (nm, nd): (i64, i64) = {
    let splitted: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    (splitted[0], splitted[1])
  };
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let majors: Vec<i64> = gets.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let dontcares: Vec<i64> = gets.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  let mut solution: Solution = Solution::new(n, params, nm, nd, majors, dontcares);
  println!("{}", solution);
}