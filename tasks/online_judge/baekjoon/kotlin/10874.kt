fun main() {
  val n: Int = readln().toInt()
  for (i in 1..n) {
    val gets = readln().split(' ').map { it.toInt() }
    var isTarget = true
    for (j in 0 until 10) {
      if (gets[j] != j % 5 + 1) {
        isTarget = false
        break
      }
    }
    if (isTarget) {
      println(i)
    }
  }
}
