use std::io::{BufRead, BufWriter, Write};

fn tadd(a: (i64, i64), b: (i64, i64)) -> (i64, i64) {
  (a.0 + b.0, a.1 + b.1)
}

struct SegTree {
  n: i64,
  arr: Vec<i64>,
  tree: Vec<(i64, i64)> // odd, even
}
impl SegTree {
  pub fn new(n: i64, arr: Vec<i64>) -> SegTree {
    let mut segTree = SegTree { n: n, arr: arr.clone(), tree: vec![(0, 0); (n * 4) as usize] };
    segTree.init(0, n - 1, 1);
    segTree
  }
  fn init(&mut self, s: i64, e: i64, idx: i64) -> (i64, i64) {
    if s == e {
      self.tree[idx as usize] = if self.arr[s as usize] % 2 == 1 { (1, 0) } else { (0, 1) };
      return self.tree[idx as usize];
    }
    let m: i64 = (s + e) / 2;
    let lr = self.init(s, m, idx * 2);
    let rr = self.init(m + 1, e, idx * 2 + 1);
    self.tree[idx as usize] = tadd(lr, rr);
    self.tree[idx as usize]
  }
  fn get_res(&mut self, s: i64, e: i64, idx: i64, l: i64, r: i64) -> (i64, i64) {
    if l > e || r < s { return (0, 0); }
    if l <= s && r >= e { return self.tree[idx as usize]; }
    let m = (s + e) / 2;
    tadd(self.get_res(s, m, idx * 2, l, r), self.get_res(m + 1, e, idx * 2 + 1, l, r))
  }
  fn update(&mut self, s: i64, e: i64, idx: i64, target: i64, dt: (i64, i64)) {
    if target < s || target > e { return; }
    self.tree[idx as usize] = tadd(self.tree[idx as usize], dt);
    if s == e { return; }
    let m = (s + e) / 2;
    self.update(s, m, idx * 2, target, dt);
    self.update(m + 1, e, idx * 2 + 1, target, dt);
  }
}

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();
  stdin.read_line(&mut gets).ok();
  let n: i64 = gets.trim().parse::<i64>().unwrap();
  gets.clear();
  stdin.read_line(&mut gets).ok();
  let arr: Vec<i64> = gets.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  gets.clear();
  stdin.read_line(&mut gets).ok();
  let mut segTree = SegTree::new(n, arr);
  //writeln!(stdout, "{:?}", segTree.tree);
  let m: i64 = gets.trim().parse::<i64>().unwrap();
  for _i in 0..m {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let (q, a, b) = {
      let split: Vec<i64> = gets.split_whitespace()
        .map(|x| x.parse::<i64>().unwrap())
        .collect();
      (split[0], split[1], split[2])
    };
    if q == 1 {
      let legacy = segTree.arr[(a-1) as usize];
      segTree.arr[(a-1) as usize] = b;
      if legacy % 2 != b % 2 {
        let delta = (-(legacy % 2) + (b % 2), -((legacy + 1) % 2) + ((b + 1) % 2));
        segTree.update(1, segTree.n, 1, a, delta);
      }
    }
    else if q >= 2 {
      let res = segTree.get_res(1, segTree.n, 1, a, b);
      if q == 2 { writeln!(stdout, "{}", res.1); }
      else { writeln!(stdout, "{}", res.0); }
    }
    //writeln!(stdout, "{:?}", segTree.tree);
  }
}