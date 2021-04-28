# Dataframe
df <- data.frame(name=c('Jihoon', 'Ahnju'), age=c(32, 28))
df

id <- c('F1', 'F2', 'F3')
name <- c('Seongsu', 'Shinyoung', 'Jiwoong')
age <- c(32, 28, 22)
isMarried <- c(TRUE, FALSE, TRUE)
df <- data.frame(id, name, age, isMarried)
df
str(df)

## Data Access
df[1, 2] # [1] 32
df[c(1, 2)]
df[c(1, 2), ]
df[c(1, 2), c(3, 1)]
df[, c('name', 'age')]
df$name # [1] "Seongsu"   "Shinyoung" "Jiwoong"
df$name[2:3] # [1] "Shinyoung" "Jiwoong"  
# df[row: vector, column: vector]

## Mass Data Processing (with iris)
head(iris, 3)
tail(iris)
summary(iris)
min(iris$Sepal.Length)
max(iris$Sepal.Length)
median(iris$Petal.Width)
mean(iris$Petal.Width)
quantile(iris$Sepal.Length)
View(iris)
## # subset(x: dataframe, condition, select: numeric)
subset(iris, Sepal.Length > 7)
subset(iris, Sepal.Length > 7 | Petal.Length >= 6.5)

longley[longley$GNP > 200 & longley$Population >= 109 & longley$Year > 1960 & longley$Employed > 50, ]
sum(longley$GNP + longley$GNP.deflator + longley$Unemployed + longley$Population)

# P.84