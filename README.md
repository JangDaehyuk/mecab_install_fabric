# mecab_install_fabric
install mecab with fabric library

### 우분투 리눅스에서 형태소 분석기 mecab 을 쉽게 설치하도록 도와주는 프로젝트입니다.
### 아래 설명을 따라서 진행해주시면 됩니다.
#### **실행환경: ubuntu 18.04**

### 1. fabric 패키지를 설치 합니다.

**$ pip install -r requirement.txt** 

___  

## 2. ip address 확인 

**$ hostname -i**

터미널에서 ip address 를 확인한뒤 3번 실행문에서 **계정명@inet값** 을 입력해주세요.

___  

## 3. fabfile 실행

**$ fab deploy:host=계정ID@inet값 -p '계정비밀번호'**

**mecab 형태소 분석기는 전역에 설치됩니다.**

___  

> ### **설치하기 전 형태소 분석기 확인**   

![설치하기 전](https://github.com/JangDaehyuk/mecab_install_fabric/blob/main/image/mecab_0_before_install.png)



> ### **설치 완료**    
![설치 완료](https://github.com/JangDaehyuk/mecab_install_fabric/blob/main/image/mecab_installed_%EB%8F%99%EC%9E%91_%ED%99%95%EC%9D%B8.jpg)

___  

>**mecab 형태소 분석기 테스트**    
![mecab 테스트](https://github.com/JangDaehyuk/mecab_install_fabric/blob/main/image/install_test_1.png)

> ### **주의사항**   
![ssh_동작_active](https://github.com/JangDaehyuk/mecab_install_fabric/blob/main/image/ssh_%EC%9E%91%EB%8F%99%ED%99%95%EC%9D%B8_2.jpg)

**코드를 실행하기 전에 ssh 가 활성화되어 있어야 합니다.** 

