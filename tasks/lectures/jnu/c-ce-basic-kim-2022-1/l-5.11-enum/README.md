# 열거형

## 코드 가독성을 높여보자
```c
if (date == 1) { 
  // 월요일 처리
}
```

```c
#define MON 1

if (date == MON) {
  // 월요일 처리
}
```

## 정의
```c
enum enumname {
  val1 = init,
  val2..
};
```

### typedef로 별칭이 지정된 익명 열거형 정의
```c
typedef enum _EnumName {
  FirstEnum = 0,
  SecondEnum,
  ThirdEnum,
  FourthEnum,
  FifthEnum
} MyEnum;

MyEnum new_enum;
```

### 익명 열거형에 반복문 도입 아이디어
열거형 마지막에 개수 나타내는 항목을 추가하여 for문 제어

```c
typedef enum _DayOfWeek {
    Sunday = 0, Monday, Tuesday, Wednesday,
    Thursday, Friday, Saturday, DayOfWeekCount
} DayOfWeek;

void main()
{
  for (DayOfWeek i = Sunday; i < DayOfWeekCount; i++) 
    printf("%d\n", i);
  return 0;
}
```

# 참조
* [Visual C++ 열거형 참조](https://docs.microsoft.com/ko-kr/cpp/cpp/enumerations-cpp?view=msvc-170)
* [C언어 코딩 도장](https://dojang.io/mod/page/view.php?id=480)
