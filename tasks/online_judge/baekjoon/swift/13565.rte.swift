import Foundation

func compute(_ n: Int, _ m: Int, _ map: inout [[Int]]) -> Bool {
  var queue = [(Int, Int)]()
  for i in 0...(n - 1) {
    if map[0][i] == 0 {
      map[0][i] = 2
      queue.append((0, i))
    }
  }
  while queue.count > 0 {
    let (y, x) = queue[0]
    queue.removeFirst()
    for (dy, dx) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
      let (ny, nx) = (y + dy, x + dx)
      if !(0 <= ny && ny < n && 0 <= nx && nx < n) { continue }
      if map[ny][nx] != 0 { continue }
      map[ny][nx] = 2
      queue.append((ny, nx))
    }
  }
  for i in 0...(n - 1) {
    if map[n - 1][i] == 2 {
      return true
    }
  }
  return false
}

func main() {
  var gets = [String]()
  gets = readLine()!.components(separatedBy: " ")
  let (n, m) = (Int(gets[0])!, Int(gets[1])!)
  var map = [[Int]]()
  if n == 0 { return }
  for _ in 1...n {
    let gets = readLine()!.map { String($0) }
    var row = [Int]()
    for j in 0...(n - 1) {
      row.append(Int(gets[j])!)
    }
    map.append(row)
  }
  print(compute(n, m, &map) ? "YES" : "NO")
}

main()
