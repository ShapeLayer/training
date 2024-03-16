import gleam/io.{println}
import gleam/result.{unwrap}
import gleam/erlang.{get_line}
import gleam/int.{parse, to_string}
import gleam/string.{split, trim}
import gleam/list.{at, map}

pub fn main() {
  let gets =
    map(
      split(
        trim(
          get_line("")
          |> unwrap(""),
        ),
        on: " ",
      ),
      with: fn(n) { unwrap(parse(n), -1) },
    )
  println(to_string(unwrap(at(gets, 0), 0) + unwrap(at(gets, 1), 0)))
}
