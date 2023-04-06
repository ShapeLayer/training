use std::{io::{BufRead, BufWriter, Write}, cmp};

struct Solution {
  arr: Vec<i64>,
  tree: Vec<i64>
}

impl Solution {
  pub fn new(arr: Vec<i64>) -> Solution {
    let len: i64 = arr.len() as i64;
    let mut solution = Solution {
      arr: arr,
      tree: vec![2e10 as i64; (len * 4) as usize]
    };
    solution.init(0, len-1, 1);
    solution
  }

  fn init(&mut self, start: i64, end: i64, index: i64) -> i64 {
    if start == end {
      self.tree[index as usize] = self.arr[start as usize];
      return self.tree[index as usize];
    }
    let mid: i64 = (start + end) / 2;
    self.tree[index as usize] = cmp::min(self.init(start, mid, index * 2), self.init(mid+1, end, index * 2 + 1));
    self.tree[index as usize]
  }

  fn get_mins(&mut self, start: i64, end: i64, index: i64, left: i64, right: i64) -> i64 {
    if left > end || right < start { return 2e10 as i64; }
    if left <= start && right >= end { return self.tree[index as usize] };
    let mid: i64 = (start + end) / 2;
    cmp::min(self.get_mins(start, mid, index * 2, left, right), self.get_mins(mid + 1, end, index * 2 + 1, left, right))
  }
}

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();
  stdin.read_line(&mut gets).ok();
  let (n, m) = {
    let split: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    (split[0], split[1])
  };
  let mut arr: Vec<i64> = vec![-1; n as usize];
  for i in 0..n {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    arr[i as usize] = gets.trim().parse::<i64>().unwrap();
  }
  let mut solution = Solution::new(arr);
  for _i in 0..m {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let split: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    writeln!(stdout, "{}", solution.get_mins(0, n-1, 1, split[0]-1, split[1]-1)).ok();
  }
}