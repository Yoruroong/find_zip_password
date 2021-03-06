<h1 align="center">환영합니다👋</h1>

> 이 레포지토리에 있는 코드를 써서 일어나는 일의 모든 책임은 이용자에게 있습니다.

# 기능 소개
이 코드는 압축 파일의 암호를 잊어버린 경우, 암호를 무차별 대입하여 암호를 찾아주는 코드입니다.

## 사용 방법
### install 
```
git clone https://github.com/Yoruroong/zip_password_recovery
```
소스코드를 다운받으셔도 무방합니다.
### 실행
`py main.py`

![1](https://yoru.pe.kr/githubimage/1.png)
1. 압축해제할 파일명을 입력합니다

![2](https://yoru.pe.kr/githubimage/2.png)

2. 무차별 대입할 문자를 선택합니다

![3](https://yoru.pe.kr/githubimage/3.png)

3. 암호를 찾았습니다


# 예상되는 시간 (소문자, 대문자, 특수문자, 숫자)
> i5-9400f 기준
- 1자리 : 1초 미만
- 2자리 : 5초 미만
- 3자리 : 150초 미만
- 4자리 : 20000초 미만

## 샘플 파일
> 테스트를 위한 샘플 파일입니다. samples폴더에 위치해 있으며, 각각의 압축 파일의 암호는 파일명에 포함되어 있습니다. Skylake 가상 코어 기준입니다. 조합 : 소문자+대문자+숫자
- Z.zip : 1초 이하
- ZZ.zip : 3초 이하
- ASD.zip : 55초 이하
- 1234.zip : 195초 이하
- asdf.zip : 990초 이하

### 리스트로 암호찾기
67번째 줄에 있는 코드의 주석을 해제하고 69번째 줄에 있는 코드에 주석을 달면 됩니다.

# 제한 사항
- 싱글 코어만 사용합니다.
- zip 파일만 지원합니다

# 업데이트 예정
1. 멀티코어 지원

# List
[https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou-75.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou-75.txt)
