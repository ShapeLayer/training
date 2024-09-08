fun main() {
  val n: Int = readln().toInt()
  for (var i = 0; i < n; i++) {
    val gets = readln().split(' ').map { it.toInt() }
    var isTarget: Bool = true
    for (var j = 0; j < 10; j++) {
      if (gets[i] != (j - 1) % 5 + 1) {
        isTarget = true
        break
      }
      if (isTarget) {
        println(j)
      }
    }
  }
}
