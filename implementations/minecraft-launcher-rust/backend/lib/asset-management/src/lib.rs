pub mod fs;
pub mod definitions;
use serde::{Serialize, Deserialize};

pub fn add(left: usize, right: usize) -> usize {
  left + right
}

pub struct AssetManager {}
impl AssetManager {}


#[cfg(test)]
mod tests {
  use super::*;

  #[derive(Serialize, Deserialize, Debug)]
  struct T(u8, f64, bool, String);

  #[test]
  fn serde_serialize() {
    let t = T(10u8, 3.14159, true, "Hello".to_owned());
    let s = serde_json::to_string(&t).unwrap();
    // `s` represented as `[10, 3.14159, true, "Hello"]`
    println!("{}", s);

    // deserialization
    let d: T = serde_json::from_str(r#"[10, 3.14159, true, "Hello"]"#).unwrap();
    // `d` is `T(10u8, 3.14159, true, "Hello".to_owned())`;
    println!("{:?}", d);
  }
}
