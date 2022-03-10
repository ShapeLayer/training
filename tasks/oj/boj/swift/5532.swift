import Foundation

let l = Int(readLine()!)!
let a = Float(readLine()!)!
let b = Float(readLine()!)!
let c = Float(readLine()!)!
let d = Float(readLine()!)!
let kr = Int(ceil(a / c))
let mt = Int(ceil(b / d))
let day = max(kr, mt)
print(l - day)