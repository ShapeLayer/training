# Align
지금까지 세로 정렬은 아래 코드처럼 짰으나, 다른 방법이 있었음
```css
element {
    display: flex;
    justify-content: center;
    flex-direction: column;
}
```

## justify-content
```css
element { justify-content: center; }
```

`display: flex;` 상태에서만 작동함  
구체적인 flex 사용방법에 따라 배치

### 특이 메모사항
주로 가로 가운데 정렬에 사용  

## align-items
```css
element { align-items: center; }
```
Cross Axis 설정에 따라 배치  

### 특이 메모사항
주로 세로 가운데 정렬에 사용  