import Foundation

let n = Int(readLine()!)!
for _ in 1...n {
  let gets = readLine()!.components(separatedBy: "-")
  var first = 0
  for (idx, char) in gets[0].enumerated() {
    first += Int(char.asciiValue!-65) * (pow(26, gets[0].count-idx-1) as NSDecimalNumber).intValue
  }
  let second = Int(gets[1])!
  let d = abs(first-second)
  if d <= 100 { print("nice") }
  else { print("not nice") }
}