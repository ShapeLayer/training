import Foundation

var parent = [Int]()
var parents = [Int]()

func ccw(_ p1: (Int, Int), _ p2: (Int, Int), _ p3: (Int, Int)) -> Int {
  let op = (p1.0*p2.1 + p2.0*p3.1 + p3.0*p1.1) - (p1.0*p3.1 + p2.0*p1.1 + p3.0*p2.1)
  if op > 0 { return 1}
  else if op < 0 { return -1 }
  else { return 0 }
}

func isIntersect(_ p1: inout (Int, Int), _ p2: inout (Int, Int), _ p3: inout (Int, Int), _ p4: inout (Int, Int)) -> Bool {
  let p1p2 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
  let p3p4 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
  if p1p2 == 0 && p3p4 == 0 {
    if p1 > p2 {
      (p1, p2) = (p2, p1)
    }
    if p3 > p4 {
      (p3, p4) = (p4, p3)
    }
    return p3 <= p2 && p1 <= p4
  }
  return p1p2 <= 0 && p3p4 <= 0
}

func find(_ n: Int) -> Int {
  if n == parent[n] { return n }
  return find(parent[n])
}

func merge(_ a: Int, _ b: Int) {
  let (pa, pb) = (find(a), find(b))
  if pa < pb {
    parent[b] = pa
    parent[pb] = pa
  } else if pa > pb {
    parent[a] = pb
    parent[pa] = pb
  }
}

let n = Int(readLine()!)!
var dots = [((Int, Int), (Int, Int))]()
var gets = [String]()
for i in 0...n+1 { parent += [i] }
for i in 1...n+1 {
  gets = readLine()!.components(separatedBy: " ")
  dots += [((Int(gets[0])!, Int(gets[1])!), (Int(gets[2])!, Int(gets[3])!))]
  if i == 1 {
    parents += [i]
    continue
  }
  for p in parents {
    var dotP = dots[p-1]
    var dotN = dots[i-1]
    let res = isIntersect(&dotP.0, &dotP.1, &dotN.0, &dotN.1)
    if res {
      merge(p, i)
      break
    } else {
      parents += [p]
    }
  }
}