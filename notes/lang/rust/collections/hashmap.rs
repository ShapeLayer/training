use std::collections::HashMap;

fn main() {
  let mut hm = HashMap::new();
  
  hm.insert(
    1, 3,
  );
  
  if hm.contains_key(&1) {
    println!("{}", hm.get(&1).unwrap());
  }
  /*
  match book_reviews.get(book) {
    Some(review) => println!("{}: {}", book, review),
    None => println!("{} is unreviewed.", book)
  }
  */
}