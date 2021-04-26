# Functions
## print()
R은 print()를 생략할 수 있다. 약간 파이썬의 인터프리터 모드 상태를 보는 것 같다.  
```r
a <- 1
print(a)
# [1] 1
a
# [1] 1
```

## mode()
mode 함수는 변수의 타입을 확인한다. 파이썬의 `type()`과 비슷하다.  
```r
mode(c(T, F))
# [1] "logical"
mode(c("a", "b"))
# [1] "character"
```
### Note
Vecter는 mode로 출력되지 않는 모양이다.