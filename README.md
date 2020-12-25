# mecab_install_fabric
install mecab with fabric library

#### **실행환경: ubuntu 18.04**

### 1. fabric 패키지를 설치 합니다.

**$ pip install -r requirement.txt** 

## 2. ip address 확인 

> $ hostname -i

터미널에서 ip address 를 확인한뒤 데스크탑의 **계정명@inet값** 을 입력해주세요.

## 3. fabfile 실행

**$ fab deploy:host=계정ID@inet값 -p '계정비밀번호'**

mecab 형태소 분석기는 전역에 설치됩니다.

