# box-sizing
박스의 크기를 화면에 표시하는 방식을 변경할 수 있음. 단순히 테두리를 바깥에 꺼낼 것인지 안으로 넣을 것인지로 생각하면 편할듯
```css
element {
    box-sizing: border-box;
}
```

## Example
```html
<!doctype html>
<html>
<head>
    <style>
        *{
            box-sizing:border-box;
        }
        div{
            margin:10px;
            width:150px;
        }
        #small{
            border:10px solid black;
        }
        #large{
            border:30px solid black;
        }
    </style>
</head>
<body>
       <div id="small">Hello</div>
       <div id="large">Hello</div>
</body>
</html>
```
## Reference
* https://opentutorials.org/course/2418/13405