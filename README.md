# Neuro P1 : 보돈

# 1. 보돈

## 1.1 기능

### 1.1.1 주문하기(유저) // 기능은 업데이트 예정입니다.
1. 웹사이트를 통해 원하는 카페를 선택
2. 빠르게 테이크아웃만 할 제품들을 선택
3. vue-iamport를 이용한 테스트 결제 후 최근 주문 페이지로 이동

![order](https://user-images.githubusercontent.com/24622029/67506500-1b189a00-f6c8-11e9-9698-f0f4b247395d.gif)



## 1.2 기술 스택

* Django Rest Framework



# 2. 사용법


## 2.1 백엔드(p1_api)


### Install Dependencies

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run Tests with pytest module
```
python manage.py makemigrations app
python manage.py migrate
pytest
```


### Run server in dev environment
```
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver
```

## API_URL

https://takeit.run.goorm.io/api 

## Postman Collection

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ece08e0c9b1f5eca0acb)



## License

This software is distributed under [MIT license](https://github.com/apertureless/vue-parallax/blob/master/LICENSE.txt).



## Written with

* [StackEdit](https://stackedit.io/).
