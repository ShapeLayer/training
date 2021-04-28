# Vector
v <- c(1, 2, 3, 4)
v # [1] 1 2 3 4
v <- c(0, v, 9)
v # [1] 0 1 2 3 4 9
v <- append(v, c(6, 7), 5)
v # [1] 0 1 2 3 4 6 7 9
length(v) # [1] 8
v <- v[-c(2, 8)] # [1] 0 2 3 4 6 7
length(v) # [1] 6
v <- v + c(10, 11)
v 
# # NOT [1] 0 2 3 4 6 7 10 11
# #     [1] 10(0+10) 13(2+11) 13(3+10) 15(4+11) 16(6+10) 18(7+11)
v <- v - c(1, 4)
v # [1] 9(10-1) 9(13-4) 12(13-1) 11(15-4) 15(16-1) 14(18-4)
v <- v * c(1, 2)
v # [1] 9(9*1) 18(9*2) 12(12*1) 22(11*2) 15(15*1) 28(14*2)

## Indexing
v[3] # [1] 12
v[c(1, 2)] # [1] 9 18
v[c(2, 1)] # [1] 18 9
v <- 3:7
v # [1] 3 4 5 6 7

## Conditions
v[c(F, F, T, F, F)] # [1] 5
v[c(T, F, F, T, F)] # [1] 3, 6
v < 4 # [1] TRUE TRUE TRUE FALSE FALSE

## Modifying
v[3] <- 9
v # [1] 3 4 9 6 7
v[c(2, 4)] <- 10
v # [1] 3 10 9 10 7
v[2:4] <- 0
v # [1] 3 0 0 0 7
v[1:length(v)] <- 0
v # [1] 0 0 0 0 0
v <- 1:5
v <- c(0, v)
v # [1] 0 1 2 3 4 5

v_alphabet_1 <- c('A', 'B', 'C', 'F', 'G')
v_alphabet_2 <- c('D', 'E')
append(v_alphabet_1, v_alphabet_2, 3) # [1] "A" "B" "C" "D" "E" "F" "G"
v_alphabet_1 # [1] "A" "B" "C" "F" "G"

v <- 11:20
v[c(1, 3, 5, 7)] # [1] 11 13 15 17
v[-c(1, 3, 5, 7)] # [1] 12 14 16 18 19 20
length(v) # [1] 10

## Factor
## # Similar to Counter() in Python
v_chars <- c('apple', 'pair', 'apple', 'orange', 'apple', 'orange', 'pair')
v_chars # [1] 'apple' 'pair' 'apple' 'orange' 'apple' 'orange' 'pair'
        # factor(x: Vector, levels: Vector, ordered: Logical)
f_chars <- factor(v_chars)
f_chars # [1] apple pair apple orange apple orange pair
        # Levels: apple orange pair
mode(f_chars) # [1] "numeric"
str(f_chars)  # Factor w/ 3 levels "apple", "orange", ..: 1 3 1 2 1 2 3
f_chars__to_char <- as.character(f_chars)
f_chars__to_num  <- as.numeric(f_chars)
f_chars__to_char  # [1] "apple"  "pair"   "apple"  "orange" "apple"  "orange" "pair" 
f_chars__to_num   # [1] 1 3 1 2 1 2 3
f_chars__filter <- factor(v_chars, levels=c('orange', 'apple'))
                # Notice order of which vector's that will be into levels param
f_chars__filter # [1] apple  <NA>   apple  orange apple  orange <NA>  
                # Levels: orange apple
v_order <- c('low', 'middle', 'high')
f_ordered <- factor(v_order, ordered=T)
f_ordered   # [1] low    middle high  
            # Levels: high < low < middle
f_ordered <- factor(v_order, levels=v_order, ordered=T)
f_ordered   # [1] low    middle high  
            # Levels: low < middle < high

## Numeric Factor -> Numeric Vector
v_numeric <- c(1000, 2000, 1000, 2000, 3000, 2000, 3000)
f_numeric <- factor(v_numeric)
f_numeric # [1] 1000 2000 1000 2000 3000 2000 3000
          # Levels: 1000 2000 3000
as.numeric(f_numeric) # [1] 1 2 1 2 3 2 3
v_numeric_char <- as.character(f_numeric)
v_numeric_char  # [1] "1000" "2000" "1000" "2000" "3000" "2000" "3000"
v_numeric_num  <- as.numeric(v_numeric_char)
v_numeric_num   # [1] 1000 2000 1000 2000 3000 2000 3000