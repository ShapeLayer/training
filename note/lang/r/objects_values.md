# Objects / Values
## Objects
R은 변수를 객체(Object)라고 한다. `new Object` 식의 객체가 아니라 그냥 변수다.  
그렇기 때문에 아래 코드에서 `b`는 참조 타입이 아니라 그냥 변수이다.  
```r
a <- 1
b <- a
```

## Values
### Vector (+ chr)
1차원 배열들을 모두 벡터라고 한다. 벡터는 함수 `c`(Combine)을 통해 생성한다.  

```r
vect <- c(1, 2, 3, 4)
str(vect) # 벡터 정보 확인
```

```r
vect <- c(1, "2", 3)
str(vect)
# chr[1:3] "1" "2" "3"
```
#### str
R에서 문자열 타입은 `str`이 아닌 `chr`이다. `str`은 다른 역할을 하는 함수로 정의되어있다.  
데이터 구조, 변수 개수, 변수명, 값 개수, 값 내용을 출력한다.  

#### Indexing
R에서 인덱싱은 0이 아닌 1부터 시작한다.

### Number
* Inf : 무한대(Infinite)
* NaN : Not a Number
  * 숫자로 표현될 수 없는 값

### Logical(Bool)
논리(Logical) 타입은 `TRUE`, `FALSE`, `T`, `F`로 표현한다.  

```r
logical_val <- c(TRUE, FALSE, T, F)
logical_val
# [1] TRUE FALSE TRUE FALSE
```

### Character
문자열(Character, Chr) 타입은 "", ''을 사용해 표현한다.

#### Related Functions
```r
# 문자 개수 출력
nchar(c("123", "456", "789"))
# [1] 3 3 3

# 문자열 슬라이싱
substr("1234567", 2, 5) # 두번째부터 다섯번째까지
# [1] "2345"
## 특정 문자를 기준으로
strsplit("2021/04/26", split="/")
# [[1]]
# [1] 2021 04 26
```