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
## # attach(x: dataframe)
## # : Attachs local object to global
## # detach(x: dataframe)
## # : Detachs attached local object from global
attach(longley)
longley[GNP > 200 & Population >= 109 & Year > 1960 & Employed > 50, ]
detach(longley)

df_pimm <- data.frame(
  id = c(1, 2, 3, 4, 5),
  name = c('Jonghyeon', 'Jemin', 'Minseo', 'Jeongsuk', 'Hyejin'),
  grade = c(1, 3, 2, 4, 3),
  major = c('CE', 'CE', 'DS', 'SW', 'SW')
)
df_pimm
df_pimm[c(3, 4), c('name', 'grade')] # row. 3, 4 / name, grade
df_pimm[c(T, F, T, T, F), c(F, T, F, T)] # row. 1, 3, 4 / name, major
df_pimm[df_pimm$grade < 3, ]  # Jonghyeon, Minseo
df_pimm[df_pimm$grade < 3]    # !?
df_pimm[df_pimm$grade]        # !?
order(df_pimm$grade)
df_pimm[order(df_pimm$grade), ]  # order() Returns Position Vector (Numeric)
df_pimm[sort(df_pimm$grade)]     # sort() Returns Arrayed Vector
df_pimm[order(df_pimm$grade, df_pimm$name, decreasing=T), ]
df_pimm[order(df_pimm$grade, decreasing=T), ]
df_pimm[order()]
## # aggregate(formula, data: dataframe, FUN: function)
## # rbind => Combine Rows
## # cbind => Combine Columns
aggregate(grade ~ major, df_pimm, mean) # grade mean by major
df_pimm$points <- c(1000, 800, 600, 900, 1200)
aggregate(cbind(df_pimm$grade, df_pimm$points), df_pimm, sum)  # !?
aggregate(cbind(df_pimm$grade, df_pimm$points) ~ major, df_pimm, sum)
