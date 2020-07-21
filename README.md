# Neuro P1 : 보돈

# 1. 보돈

## 1.1 기능

### 1.1.1 회원
#### 1. 회원가입
#### 2. 로그인
#### 3. 회원정보 수정


## 1.2 기술 스택

* Django Rest Framework


## 1.3 API 문서
**사용자 정보 조회**
----
사용자 정보를 요청하는 부분입니다.
* **URL**

  /api/users/me

* **Method : ** `GET` | `POST` | `DELETE` | `PUT`

*  **Header Params**

   Authorization 에 로그인 시 얻은 토큰을 넣어줍니다.
   
   Authorization : JWT <_jwt token>
  
*  **URL Params**

   **Required:** none
   
   **Optional:** none
* **Data Params**

  ```json
  {
    "phone": "01011111111",
    "password": "!ejrqo401"
  }
  ```

* **Success Response:**
  
  * **Code:** 201
  
    **Content:**
    ```json
    {
        "phone": "01011111111",
        "nickname": "test1",
        "uuid": "78cee909-95d9-4ef4-bdda-7f12ac9a4657"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 UNAUTHORIZED
  
    **Content:** `{ error : "Log in" }`


* **Notes:**

  Authorization에 jwt 토큰을 넣어주는 것을 아셔야 합니다.

<br>
**사용자 정보 수정**
----
사용자 정보를 요청하는 부분입니다.
* **URL**

  /api/users/me

* **Method : ** `GET` | `POST` | `DELETE` | `PUT`

*  **Header Params**

   Authorization 에 로그인 시 얻은 토큰을 넣어줍니다.
   
   Authorization : JWT <_jwt token>
  
*  **URL Params**

   **Required:** none
   
   **Optional:** none
* **Data Params**

  ```json
  {
    "phone": "01011111111",
    "password": "!ejrqo401"
  }
  ```

* **Success Response:**
  
  * **Code:** 201
  
    **Content:**
    ```json
    {
        "phone": "01011111111",
        "nickname": "test1",
        "uuid": "78cee909-95d9-4ef4-bdda-7f12ac9a4657"
    }
    ```
 
* **Error Response:**

  * **Code:** 400 UNAUTHORIZED
  
    **Content:** `{ error : "Log in" }`


* **Notes:**

  Authorization에 jwt 토큰을 넣어주는 것을 아셔야 합니다.

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


## Postman Collection

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ece08e0c9b1f5eca0acb)



## License

This software is distributed under [MIT license](https://github.com/apertureless/vue-parallax/blob/master/LICENSE.txt).



## Written with

* [StackEdit](https://stackedit.io/).
