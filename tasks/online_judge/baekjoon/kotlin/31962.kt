fun main() {
  val (n, x) = readln().split(' ').map { it.toInt() }
  var ans = -1
  for (i in 1..n) {
    val (s, t) = readln().split(' ').map { it.toInt() }
    if (s + t <= x) {
      if (ans < s) {
        ans = s
      }
    }
  }
  println(ans)
}
