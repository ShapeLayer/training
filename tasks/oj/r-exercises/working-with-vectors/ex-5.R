u <- 3
v <- 4

# Part a
w <- u + v
w <- w / 2
w <- w + u
print(w)

# Part b
w1 <- u ^ 3
w2 <- u - v
w <- w1 / w2
print(w)

# Part a and Part b can be made with a single expression.
# Park a
w <- (u + v) / 2 + u
print(w)

# Park b
w <- u ^ 3 / (u - v)
print(w)