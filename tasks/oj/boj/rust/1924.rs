use std::io;

fn main() {
  let mut gets = String::new();
  let dates: Vec<i32> = vec![31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let weekdays: Vec<&str> = vec!["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"];
  io::stdin().read_line(&mut gets).unwrap();
  let (x, y): (i32, i32) = {
    let splited: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (splited[0], splited[1])
  };
  let mut date = 0;
  for month in 0..(x-1) {
    date += dates[month as usize];
  }
  date += y - 1;
  println!("{}", weekdays[(date % 7) as usize]);
}