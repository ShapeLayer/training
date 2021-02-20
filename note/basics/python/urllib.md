# urllib

> 

## 주 사용 패턴
```python
req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
scrap = urllib.request.urlopen(req).read().decode('utf-8')
# >>> scrap
# <!DOCTYPE HTML>
# ...
```