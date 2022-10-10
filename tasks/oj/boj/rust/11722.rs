use std::io::{BufRead, BufWriter, Write};

struct Solution {
  n: i32,
  a: Vec<i32>,
  d: Vec<i32>
}

impl Solution {
  pub fn new(a: Vec<i32>, n: i32) -> Solution {
    let mut solution = Solution {
      a: a, d: vec![-1; n as usize], n: n
    };
    solution.d[0] = 0;
    solution
  }

  fn proc(&mut self) -> i32 {
    let mut max_len = 1;
    for i in 1..self.n {
      for j in (0..i).rev() {
        if self.a[i as usize] < self.a[j as usize] {
          /* WA 반례
           * 4
           * 6 5 7 3
           * D 테이블의 3에 대한 값을 생성할 때
           * d[i] < d[j] 로 지정하면
           * [1, 2, 1, "2"]로 처리되어 3에 대한 처리가 완료되지 않았음에도
           * [1, 2, 1, "3"]으로 처리될 조건 이 만족되지 않아 (2 < "2") WA 발생함
           */
          if self.d[i as usize] <= self.d[j as usize] { self.d[i as usize] = self.d[j as usize] + 1; }
          if self.d[i as usize] > max_len { max_len = self.d[i as usize]; }
        }
        /* println!("{:?} {} {:?}", (0..i).rev(), j, self.d); */
      }
      if self.d[i as usize] == -1 { self.d[i as usize] = 1; }
    }
    max_len
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
  gets = String::from("0 ");
  stdin.read_line(&mut gets).ok();
  let arr: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let mut solution = Solution::new(arr, n+1);
  write!(stdout, "{}\n", solution.proc());
}