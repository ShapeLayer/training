pub mod rest;
use dotenv::dotenv;
#[macro_use]
extern crate dotenv_codegen;

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
    #[test]
    fn load_dotenv() {
        dotenv().ok();
        assert_eq!(dotenv!("AZURE_CLIENT_ID"), String::from("1ce6e35a-126f-48fd-97fb-54d143ac6d45"));
    }
}
