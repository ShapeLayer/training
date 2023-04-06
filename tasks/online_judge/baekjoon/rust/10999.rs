use std::io;

struct Solution {
  arr: Vec<i64>,
  tree: Vec<i64>,
  lazy: Vec<i64>
}

impl Solution {
  pub fn new(arr: Vec<i64>) -> Solution {
    let len: i64 = arr.len() as i64;
    let mut solution = Solution { arr: arr, tree: vec![-1; (len*4) as usize], lazy: vec![0; (len*4) as usize] };
    solution.init(0, len-1, 1);
    solution
  }

  fn init(&mut self, start: i64, end: i64, index: i64) -> i64 {
    if start == end {
      self.tree[index as usize] = self.arr[start as usize];
      return self.tree[index as usize];
    }
    let mid: i64 = (start + end) / 2;
    self.tree[index as usize] = self.init(start, mid, index * 2) + self.init(mid + 1, end, index * 2 + 1);
    self.tree[index as usize]
  }

  fn get_sums(&mut self, start: i64, end: i64, index: i64, left: i64, right: i64) -> i64 {
    self.update_lazy(start, end, index);
    if left > end || right < start { return 0; }
    if left <= start && right >= end { return self.tree[index as usize]; }
    let mid: i64 = (start + end) / 2;
    self.get_sums(start, mid, index * 2, left, right) + self.get_sums(mid + 1, end, index * 2 + 1, left, right)
  }

  fn update_range(&mut self, start: i64, end: i64, index: i64, left: i64, right: i64, delta: i64) {
    self.update_lazy(start, end, index);
    if left > end || right < start { return; }
    if left <= start && right >= end {
      self.tree[index as usize] += (end - start + 1) * delta;
      if start != end {
        self.lazy[(2 * index) as usize] += delta;
        self.lazy[(2 * index + 1) as usize] += delta;
      }
      return;
    }
    let mid: i64 = (start + end) / 2;
    self.update_range(start, mid, index * 2, left, right, delta);
    self.update_range(mid + 1, end, index * 2 + 1, left, right, delta);
    self.tree[index as usize] = self.tree[(2 * index) as usize] + self.tree[(2 * index + 1) as usize];
  }

  fn update_lazy(&mut self, start: i64, end: i64, index: i64) {
    if self.lazy[index as usize] != 0 {
      self.tree[index as usize] += (end - start + 1) * self.lazy[index as usize];
      if start != end {
        self.lazy[(2 * index) as usize] += self.lazy[index as usize];
        self.lazy[(2 * index + 1) as usize] += self.lazy[index as usize];
      }
      self.lazy[index as usize] = 0;
    }
  }
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (n, m, k) = {
    let split: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  let mut arr: Vec<i64> = vec![-1; n as usize];
  for i in 0..n {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    arr[i as usize] = gets.trim().parse::<i64>().unwrap();
  }
  let mut solution = Solution::new(arr);
  for _i in 0..(m+k) {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let split: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    if split[0] == 1 {
      solution.update_range(0, n-1, 1, split[1]-1, split[2]-1, split[3]);
    } else if split[0] == 2 {
      println!("{}", solution.get_sums(0, n-1, 1, split[1]-1, split[2]-1));
    }
  }
}