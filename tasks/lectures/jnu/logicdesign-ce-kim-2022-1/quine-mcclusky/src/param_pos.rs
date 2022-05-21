pub mod param_pos {
  use std::fmt;

  #[derive(Clone)]
  pub struct ParamPos {
    n: i64, // Number of major parameter
    binary_size: i64, // Bit size of input parameters (number of input parameters)
    binary: Vec<i8>, // 2bit conversions of parameters value
    n1: i64 // Number of ones
  }

  impl ParamPos {
    pub fn new(n: i64, binary_size: i64) -> ParamPos {
      let mut paramPos: ParamPos = ParamPos { n: n, binary_size: binary_size, binary: vec![0; binary_size as usize], n1: 0 };
      paramPos.init();
      paramPos
    }
    
    fn init(&mut self) {
      let mut n = self.n;
      for i in 0..self.binary_size {
        if n % 2 == 1 { self.binary[i as usize] = 1; self.n1 += 1; }
        else { self.binary[i as usize] = 0; }
        n /= 2;
      }
      self.binary.reverse();
    }
  }

  impl fmt::Display for ParamPos {
    fn fmt(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
      formatter.pad(format!("{}: ({}) {:?}", self.n, self.n1, self.binary).as_str())
    }
  }
}