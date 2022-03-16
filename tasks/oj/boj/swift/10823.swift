import Foundation

var sum = 0
var body = ""
while let line = readLine() {
  body += line
}
body = body.replacingOccurrences(of: "\n", with: "")
let split = body.components(separatedBy: ",").map { Int($0) != nil ? Int($0)! : 0 }
sum += split.reduce(0, +)
print(sum)