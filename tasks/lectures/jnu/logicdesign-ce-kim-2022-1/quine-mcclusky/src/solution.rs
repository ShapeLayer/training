pub mod solution {
  use std::fmt;
  use crate::param_pos::param_pos::ParamPos;

  #[derive(Clone)]
  pub struct Solution {
    n: i64, // Number of input parameters
    nm: i64, // Number of M parameters
    nd: i64, // Number of don't care parameters
    params: Vec<String>, // Array of Parameters
    majors: Vec<i64>, // Array of major parameters' number
    dontcares: Vec<i64>, // Array of don't care parameters' number
    param_vals: Vec<ParamPos>
  }
  
  impl Solution {
    pub fn new(n: i64, params: Vec<String>, nm: i64, nd: i64, majors: Vec<i64>, dontcares: Vec<i64>) -> Solution {
      let param_vals = Vec::new();
      let mut solution: Solution = Solution { n: n, nm: nm, nd: nd, params: params, majors: majors, dontcares: dontcares, param_vals: param_vals };
      solution.init();
      solution
    }
  
    fn init(&mut self) {
      for i in 0..self.nm {
        self.param_vals.append(&mut vec![ParamPos::new(self.majors[i as usize], self.n)]);
      }
      for i in 0..self.nd {
        self.param_vals.append(&mut vec![ParamPos::new(self.dontcares[i as usize], self.n)]);
      }
    }
  
    fn solve(&mut self) {
      let all_param_vals: Vec<Vec<ParamPos>> = vec![Vec::new(); self.n as usize];
    }
  }
  
  impl fmt::Display for Solution {
    fn fmt(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
      formatter.pad(format!(
        "({}) {:?} - majors: {} {:?}, dontcares: {} {:?}\nlist\n{}",
      self.n, self.params, self.nm, self.majors, self.nd, self.dontcares, {
        let mut body = String::new();
        for i in 0..(self.nm+self.nd) {
          body += format!("{}\n", self.param_vals[i as usize]).as_str();
        }
        body
      }).as_str())
    }
  }
  
}