u <- c(8, 9, 10)
v <- c(1, 2, 3)

w <- (2 * u + v) / 10 # is same operations with below:
print(w)
w <- 2 * u
w <- w + v
w <- w / 10
print(w)

w <- (u + 0.5 * v) ^ 2 # is same operations with below:
print(w)
w <- 0.5 * v
w <- u + w
w <- w ^ 2
print(w)

w <- (u + 2) * (u - 5) + v
print(w)
w1 <- u + 2
w2 <- u - 5
w <- w1 * w2
w <- w + v
print(w)

w <- (u + 2) / ((u - 5) * v)
print(w)
w1 <- u + 2
w2 <- u - 5
w2 <- w2 * v
w <- w1 / w2
print(w)