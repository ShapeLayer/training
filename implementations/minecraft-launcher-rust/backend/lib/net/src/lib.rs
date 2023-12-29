use std::net::TcpListener;

pub fn find_port(init: u16, fin: u16) -> Option<u16> {
  for port in init..fin {
    if is_available(port) {
      return Some(port);
    }
  }
  None
}

pub fn is_available(port: u16) -> bool {
  match TcpListener::bind(("127.0.0.1", port)) {
    Ok(_) => true,
    Err(_) => false,
  }
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_find_port() {
    println!("{}", find_port(10000, 20000).unwrap_or(0));
    println!("{}", find_port(10000, 20000).unwrap_or(0));
  }
}
