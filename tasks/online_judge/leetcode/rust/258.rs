struct Solution {
}
impl Solution {
  pub fn add_digits(num: i32) -> i32 {
    let mut sum = Solution::process(num);
    while sum >= 10 {
      sum = Solution::process(sum);
    }
    sum
  }

  pub fn process(num: i32) -> i32 {
    let sum: i32 = num.to_string().chars()
      .map(|x| (x as u32) as i32 - 48)
      .collect::<Vec<i32>>()
      .iter()
      .sum();
    sum
  }
}

fn main() {
  println!("{}", Solution::add_digits(38));
  println!("{}", Solution::add_digits(0));
}