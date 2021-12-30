# `unwrap()`

러스트는 잠재적으로 오류가 나타날 수 있는 작업은 모두 결과값과 fallback을 함께 반환한다. 따라서 반환값을 그대로 다른 언어처럼 사용하면 타입 오류가 생긴다.

예시
```
error[E0277]: `Result<i32, ParseIntError>` doesn't implement `std::fmt::Display`
 --> 1010.rs:7:18
  |
7 |   println!("{}", n);
  |                  ^ `Result<i32, ParseIntError>` cannot be formatted with the default formatter
  |
  = help: the trait `std::fmt::Display` is not implemented for `Result<i32, ParseIntError>`
  = note: in format strings you may be able to use `{:?}` (or {:#?} for pretty-print) instead
  = note: this error originates in the macro `$crate::format_args_nl` (in Nightly builds, run with -Z macro-backtrace for more info)
```

이 오류는 `match`를 사용하여 제어하는데, 알고리즘 문제를 풀 때는 코드가 지나치게 길어지는 문제가 있다.

이때 반환값에서 결과값만을 사용하기 위해 사용하는 것이 `unwrap()` 메서드이다.