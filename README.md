
## My Shop

카페를 운영하는 사장님이 상품을 등록해서 가게를 운영할 수 있는 서비스의 REST API 

</br>

## 목차

- [My Shop](#my-shop)
- [사용 기술](#사용-기술)
- [설계사항](#설계사항)
  * [데이터베이스 모델링](#데이터베이스-모델링)
      - [전체(시스템 포함)](#전체시스템-포함)
      - [앱(시스템 제외)](#앱시스템-제외)
  * [구조 및 아키텍처](#구조-및-아키텍처)
  * [API 엔드포인트](#api-엔드포인트)
  * [Pytest를 이용한 테스트 코드](#pytest를-이용한-테스트-코드)
  * [권한 설정](#권한-설정)
- [구현사항](#구현사항)


</br>

## 사용 기술

-   **Back-End**  : Python, Django, Django REST Framework, Crontab
-   **Database**  : MySQL
-   **ETC**  : Git, Github,

</br>

## 설계사항

### 데이터베이스 모델링
##### 전체(시스템 포함) 

![my_project_visualized](https://github.com/song-hee-1/my-shop/assets/83492367/86ab93fe-f5cd-40b3-9431-328454453ff4)


##### 앱(시스템 제외)
![models](https://github.com/song-hee-1/my-shop/assets/83492367/66da6ab9-c71c-4bd9-9771-272f876c70d5)


- 데이터의 추적성 및 관리를 위하여 `created_at`, `updated_at` 을 가지고 있는 `core` 앱에 TimeStampModel을 모듈화
- 무결성을 위해 모델의 chocie들은 Enum 형식 및 string을 value로 가지게 설계 (cf. int: 전체 값이 다 바뀔 위험 존재)
- 요구사항을 토대로 `User` , `Product`, `ProductCategory`  모델 설계
- `Product` 는 status field를 토대로 soft_delete 구현

</br>

### 구조 및 아키텍쳐
 *앱 이름 :복수, 폴더명 : 복수, 파일명 : 단수*


- Custom Render를 설정하여 api response의 구조 통일
	-  `` { "meta":{ "code": 400, "message":"잘못된 상품 사이즈 입니다." }, "data":null }`` 
	 ![image](https://github.com/song-hee-1/my-shop/assets/83492367/9bdaca1e-6061-47a3-94db-541a29198606)

-  core.utils.exception에 APIException 유틸화하여 관리

</br>

**service_layer**
- 유지보수 및 비즈니스 로직 관리를 위하여 view에 service_layer 추가
- 모든 service_layer는 base_service를 상속받아 관리
- service를 기준으로 serializer, views 분리

</br>

**Serializer**
- **효율성 및 확장성의 용이성**을 위하여 basic_serializer를 통하여 외래키를 제외한 필드 관리
	- 해당 모델을 사용하는 serializer는 basic_serializer를 상속받아 필드 관리 (`Meta.fields 이용`)
	- 모델에 새로운 필드가 추가될 경우 basic_serializer에 필드 추가하면 해당 모델의 다른 serializer에도 **자동 적용**
	- 단, Post의 경우 기획사항에 따라 적용될 수 있도록 model serializer 외에 serializer를 적용한 예외도 존재

- *명명규칙* :
	- *Input* : *{service_name}{base_name}Qs{model_name}Serializer*
	- *Output* : *{service_name}{base_name]{http_method_name}Serializer


</br>


### API 엔드포인트



| 엔드포인트                              | 설명                                          | HTTP 메서드 |
| --------------------------------------- | -------------------------------------------- | ----------- |
| `/api/accounts/user/login/`             | 사용자 인증 정보를 전송하여 로그인을 시도합니다. | POST        |
| `/api/accounts/user/logout/`            | 로그아웃을 수행합니다.                        | POST        |
| `/api/accounts/user/signup/`            | 새로운 사용자를 등록합니다.                   | POST        |
| `/api/products/`                        | 등록된 상품 리스트를 조회합니다.               | GET         |
| `/api/products/`                        | 새로운 상품을 생성합니다.                     | POST        |
| `/api/products/pk:int/`                 | 특정 상품의 상세 정보를 조회합니다.           | GET         |
| `/api/products/pk:int/`                 | 기존 상품 정보를 업데이트합니다.              | PUT         |
| `/api/products/pk:int/`                 | 특정 상품을 삭제합니다.                       | DELETE      |
| `/api/products/search?keyword={keyword}`                 | 키워드로 상품을 검색합니다.                      | GET    
| `/api/schema/swagger-ui/`               | API를 문서화한 정보를 제공합니다.             |         |

- drf-spectacular를 이용한 문서화
- local에서 `api/schema/swagger-ui` 로 접속하면 API별 schema 및 Test 가능
</br>


### Pytest를 이용한 테스트 코드 


| Name                                         | Stmts | Miss | Cover |
| -------------------------------------------- | ----- | ---- | ----- |
| tests/conftest.py                            | 32    | 4    | 88%   |
| tests/test_accounts/test_accounts_views.py   | 33    | 0    | 100%  |
| tests/test_products/test_products_views.py   | 51    | 2    | 96%   |
| -------------------------------------------- | ----- | ---- | ----- |
| TOTAL                                        | 573   | 49   | 91%   |


- conftes.py에 자주 사용되는 함수들 fixture를 통해 유틸화
- 91%의 test-coverage

</br>


### 권한 설정
- `products` 앱의 모든 API 엔드포인트는 인증된 사용자 및 본인만 접근 가능하게 권한 설정

</br>


## 구현사항

- 비밀번호 관리
	- Django에서는 기본적으로 **PBKDF2 알고리즘**을 이용하여 비밀번호를 해싱하여 저장
	- 단방향 함수를 사용하여 비밀번호를 변환하여 저장하기 때문애, 원래 비밀번호를 아는 것이 어려움
	- 해싱에 사용되는 SECRET_KEY도 환경변수 처리하여 안전성을 강화
	- PBKDF2의 알고리즘을 보안 전문가들이 인정하는 **Argon2의 알고리즘을 이용하도록 변경**

	
- CursorPagination
	- page_size : 10
	- `id`  기준 정렬
	- query_param은 로직에 맞게 `product` 으로 변경

- 초성 검색 + like 검색
	- like 검색은 `contains look up(SQL like문)`을 이용하여 구현
	- 	 `name_initials` 의 필드를 통한 초성 검색 구현
	- 상품 등록시 자동으로 초성을 추출하여 `name_initials`에 저장
	- 자음과 초성의 일치를 위하여외부 라이브러리([jamo](https://pypi.org/project/jamo/)) 이용
		-	`아이스` 에서 추출한 초성인 `ㅇㅇㅅ` 은 한글 음절의 초성으로 분류되고, 검색 초성인 `ㅇㅇㅅ`의 경우 자음으로 처리되어 한글 음절의 범위에 포함되지 않는 문제 식별
		-  h2j 를 이용하여 한글 음절을 자음과 모음으로 분리한 후, 그 후 j2hcj를 이용하여 초성, 중성, 종성으로 분리하여 초성을 얻는 방식으로 처리

- Docker 기반 처리
	- `DockerFile` , `docker-compose.yaml`를 추가하여 docke를 기반으로 서버 실행 가능하게 처리
	- `docker-compose.yaml` 에 mysql:5.7 버전을 사용하도록 추가

- DDL 파일
     - django에서는 DDL을 migraion 파일을 이용하여 관리한다고 판단
     - django migration 파일 업로드


- JWT Token
	- 사용자 편의성 향상을 위하여 JWT 인증방식의 `Sliding Token`을 이용

> 	Sliding Token : 사용자의 활동이 지속되는 경우 토큰의 만료 시간을 연장 or 갱신하여 로그인 상태 유지

