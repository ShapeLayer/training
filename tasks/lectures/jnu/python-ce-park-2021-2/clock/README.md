# Clock
기초프로그래밍및실습 과목 프로젝트 과제

> 어떠한 방법으로든 아날로그 시계와 달력을 파이썬으로 구현하라.

---
기초프로그래밍및실습 과목은 파이썬 과목이나, 과제에 제시된 제약 사항이 없어 최근 개발된 [Brython](https://brython.info/)(파이썬의 브라우저 이식판)을 사용하였습니다.

## 시작하기
### 의존성 모듈 설치
본 프로젝트는 Brython을 활용하고 있습니다. 하지만 이 프로젝트를 실행하는데 있어 Brython을 따로 설치할 필요는 없습니다.  
Brython은 프론트엔드에서 동작하므로, Brython 실행 환경은 브라우저 상에서 자바스크립트를 통해 이미 구성되어 있습니다. 즉 Brython 런타임 JS코드는 브라우저를 통해 실행됩니다.  

### HTTP 서버 시작
로컬호스트에 애플리케이션을 호스트합니다. 포트 사용 기본값은 `8000`입니다.  
```sh
python -m http.server
```

### 로컬호스트에 접속
[http://localhost:8000](http://localhost:8000)에 접속합니다.

## Code Structure
```
- src (Static Resources)
  - css (CSS)
  - js (JavaScript)
- app (Python)
- index.html
```

## 라이선스
### 외부 리소스 라이선스
#### Brython
이 저장소가 포함하고 있는 Brython은 BSD 3-Clause로 보호되고 있습니다. 자세한 내용은 [brython 저장소의 라이선스 파일](https://github.com/brython-dev/brython/blob/master/LICENCE.txt)을 참조하세요.
