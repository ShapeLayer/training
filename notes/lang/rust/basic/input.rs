use std::io;

fn print_type_of<T>(_: &T) {
  println!("{}", std::any::type_name::<T>());
}

fn main() {
  let mut line = String::new();

  io::stdin().read_line(&mut line)
    .expect("Failed to read line.");
  
  // 스플릿하기
  let puts = line.split(" ");
  print_type_of(&puts); // core::str::iter::Split<&str>

  // 접근하기
  /*
  let puts: Vec<str> = line.split_whitespace().collect();
  => error[E0277]: the size for values of type `str` cannot be known at compilation time
  => doesn't have a size known at compile-time
  */
  let puts: Vec<&str> = line.split_whitespace().collect();
  /*
  println!("{}", puts);
  => error[E0277]: `Vec<&str>` doesn't implement `std::fmt::Display`
  => `Vec<&str>` cannot be formatted with the default formatter
  */
  println!("{:?}", puts);

  // 형변환하기
  let puts: Vec<i32> = line.split_whitespace().map(|i| i.parse::<i32>().unwrap()).collect();
  print_type_of(&puts);
  println!("{:?}", puts);

  // 이게 뭐시여..ㅠㅠ
}