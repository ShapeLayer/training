# High Text

[Unicode Converter](https://www.branah.com/unicode-converter)  

ค็็็็็็็็็็็็็็็็็ 같은 문자가 어떻게 입력되는지 궁금해 유니코드 컨버터로 뜯어봤다.  

```
\xe0\xb8\x84\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87\xe0\xb9\x87
```
하나의 문자인줄 알았으나 여러 문자가 함께 겹쳐있었다.  
이것도 장평이라고 해야될지는 모르겠으나.. 장평이 매우 좁아서 복사할 때 한문자처럼 복사되는것 같다.  
실제로 파이썬에서 `len()`함수를 사용하니 결과가 1로 나오지 않는다.

```python
>>> len('ค็็็็็็็็็็็็็็็็็')
18
```

`\xe0\xb9\x87`을 뒤에 더 추가하니 문자가 더 길어지는 것을 알 수 있다.