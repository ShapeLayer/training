use std::io;
mod solution;
use solution::solution::Solution;
mod param_pos;
use param_pos::param_pos::ParamPos;

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