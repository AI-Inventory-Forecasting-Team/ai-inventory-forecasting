# 물류 기술 블로그 및 재고 예측 서비스

## 목차
  * [1. 목표와 기능](#1-목표와-기능)
    + [1.1 목표](#11-목표)
    + [1.2 기능](#12-기능)
    + [1.3 팀 구성](#13-팀-구성)
  * [2. 개발 환경 및 배포 URL](#2-개발-환경-및-배포-url)
    + [2.1 개발 기술](#21-개발-기술)
    + [2.2 개발 환경](#22-개발-환경)
    + [2.3 배포 URL](#23-배포-url)
    + [2.4 URL 구조](#24-url-구조)
  * [3. 요구사항 명세와 기능 명세](#3-요구사항-명세와-기능-명세)
    + [3.1 요구사항 명세](#31-요구사항-명세)
    + [3.2 기능 명세](#32-기능-명세)
  * [4. 프로젝트 구조와 개발 일정](#4-프로젝트-구조와-개발-일정)
    + [4.1 프로젝트 구조](#41-프로젝트-구조)
    + [4.2 개발 일정](#42-개발-일정)
  * [5. 와이어프레임 및 화면 설계](#5-와이어프레임-및-화면-설계)
    + [5.1 와이어프레임](#51-와이어프레임)
    + [5.2 화면 설계](#52-화면-설계)
  * [6. 데이터베이스 모델링](#6-데이터베이스-모델링)
  * [7. Architecture](#7-architecture)
  * [8. 트러블슈팅](#8-트러블슈팅)
  * [9. 개발하며 느낀점](#9-개발하며-느낀점)

## 1. 목표와 기능

### 1.1 목표
- 반복적으로 재고 수량 오차가 발생하는 물류 회사의 재고 수량을 사전 예측하는 
가상의 인공지능 개발사 랜딩 페이지와 블로그 기능 개발
- 인공지능 개발사 랜딩 페이지 물류 챗봇 연동

### 1.2 기능
- 공통
    - 헤더 - 로그인 / 로그아웃
    - 헤더 - 프로필
    - 헤더 - About, Services, Pricing, Contact 페이지
    - 헤더 - 네비게이션(홈 링크)
- 메인 화면
    - 검색
    - 물류 챗봇 질의
- 서비스 화면
    - 게시글 Create, Read
- 상세 화면
    - 게시글 Update, Delete
    - 제목, 작성자, 조회수, 작성 시간, 수정 시간, 카테고리
    - 이미지, 본문, 파일 다운로드, 댓글 CRUD, 대댓글 CRUD
- 로그인 화면
    - 일반 로그인
    - 회원가입
- 프로필 화면
    - 프로필 이미지
    - 프로필 편집
- 프로필 편집 화면
    - 이름, 성, 닉네임, 프로필사진, 비밀번호 수정

### 1.3 팀 구성
<table>
	<tr>
		<th>박주형</th>
		<th>이재원</th>
		<th>기준하</th>
		<th>김민규</th>
		<th>한승일</th>
	</tr>
 	<tr>
		<td>개발 리드</td>
		<td>기획</td>
		<td>인공지능 챗봇 개발</td>
		<td>댓글 기능 개발</td>
		<td>유저 기능 개발</td>
	</tr>
</table>

<div align="right">

[목차](#목차)

</div>

## 2. 개발 환경 및 배포 URL
### 2.1 개발 기술

**[기술 - FE]**
</br>
</br>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
 <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</br>
</br>
**[기술 - BE]**
</br>
</br>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</br>
</br>
**[기술 - DB]**
</br>
</br>
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/postgresql-3776AB?style=for-the-badge&logo=postgresql&logoColor=white">
</br>
</br>

### 2.2 개발 환경
<img src="https://img.shields.io/badge/Lightsail-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"> <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"> <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">

### 2.3 배포 URL
- URL
- 테스트용 계정
  ```
  id : test
  pw : test1234!
  ```

### 2.4 URL 구조

- accounts 앱
  
| app:accounts      | HTTP Method | 설명           | 로그인 권한 필요 | 작성자 권한 필요 |
|-------------------|-------------|----------------|------------------|------------------|
| profile/          | GET         | 프로필 조회     | ✅               | ✅               |
| profile/delete/   | DELETE      | 프로필 삭제     | ✅               | ✅               |
| profile/update/   | PUT         | 프로필 전체 수정 | ✅               | ✅               |
| profile/update/   | PATCH       | 프로필 부분 수정 | ✅               | ✅               |
| signup/           | POST        | 회원가입        |                  |                  |
| token/            | POST        | 로그인 토큰 발급 |                  |                  |
| token/refresh/    | POST        | 만료 토큰 재발급 |                  |                  |


- posts 앱
  
| app:posts          | HTTP Method | 설명               | 로그인 권한 필요 | 작성자 권한 필요 |
|--------------------|-------------|---------------------|------------------|------------------|
| {id}/              | GET         | 게시물 상세 조회    |                  |                  |
| {id}/delete/       | DELETE      | 게시물 삭제         | ✅               | ✅               |
| {id}/like/         | POST        | 게시물 좋아요       | ✅               |                  |
| {id}/unlike/       | DELETE      | 게시물 좋아요 취소   | ✅               |                  |
| {id}/update/       | PUT         | 게시물 수정         | ✅               | ✅               |
| {id}/update/       | PATCH       | 게시물 부분 수정    | ✅               | ✅               |
| create/            | POST        | 게시물 작성         | ✅               |                  |
| list/              | GET         | 게시판 리스트 조회  |                  |                  |
| bookmarks/         | GET         | 북마크 조회          | ✅               |                  |
| bookmarks/{id}/    | DELETE      | 북마크 삭제          | ✅               |                  |
| bookmarks/create/  | POST        | 북마크 생성          | ✅               |                  |
| categories/        | GET         | 카테고리 조회        |                  |                  |

- comments 앱

| app:comments | HTTP Method | 설명                     | 로그인 권한 필요 | 작성자 권한 필요 |
|--------------|-------------|---------------------------|------------------|-------------------|
| comments     | GET         | /api/posts/{post_id}/comments/ | 게시물 댓글 조회 |                |   |
| comments     | GET         | /api/posts/{post_id}/comments/{id}/ | 댓글 상세 조회 |              |   |
| comments     | PUT         | /api/posts/{post_id}/comments/{id}/ | 댓글 수정 | ✅            | ✅ |
| comments     | PATCH       | /api/posts/{post_id}/comments/{id}/ | 댓글 부분 수정 | ✅         | ✅ |
| comments     | DELETE      | /api/posts/{post_id}/comments/{id}/ | 댓글 삭제 | ✅            | ✅ |
| comments     | POST        | /api/posts/{post_id}/comments/create/ | 댓글 작성 | ✅           |   |

- schema 앱
  
|app:schema|HTTP Method|설명|로그인 권한 필요|작성자 권한 필요|
|:-|:-|:-|:-:|:-:|
|schema/|GET|API 스키마 조회|||

<div align="right">

[목차](#목차)

</div>

## 3. 요구사항 명세와 기능 명세
### 3.1 요구사항 명세
- **(필수)인공지능 개발사 랜딩 페이지:**
    - 회사 소개, 서비스 소개, 연락처 등의 기본 정보를 제공
        - 재고 수량 예측 서비스의 특징과 이점 설명
        - 사용자가 문의할 수 있는 연락처 정보와 양식 제공
        - 반응형 웹 디자인(부트스트랩)을 적용하여 다양한 기기에서 접근 가능
- **(필수)블로그 기능:**
    - 물류 산업 동향, 재고 관리 팁, 회사 소식 등 관련 콘텐츠를 게시할 수 있는 블로그 기능 구현
        - 게시물 작성, 수정, 삭제 기능 제공
        - 카테고리, 태그 등을 활용하여 게시물을 분류 및 검색
        - 사용자 댓글 기능을 통해 방문자와의 소통을 활성화
- **(챌린지)데이터 처리 및 예측:**
    - 사용자가 제공한 1년 연간 재고 수량 데이터를 처리하고 분석할 수 있는 챗봇 기능 구현
        - 사용자의 연간 주문량 엑슬 워크시트 입력 데이터를 기반으로 재고 수량 예측 결과를 사용자에게 제공
- (**필수)보안 및 개인정보 보호:**
    - 사용자의 개인정보와 데이터를 안전하게 보호할 수 있는 보안 체계 마련
        - 데이터 암호화, 접근 제어, 로그 관리 등의 보안 조치 적용
        - 개인정보 처리 방침을 수립하고 이를 사용자에게 공개



### 3.2 기능 명세

```mermaid
classDiagram
  class Profile {
    +GET /api/accounts/profile/
    +DELETE /api/accounts/profile/delete/
    +PUT /api/accounts/profile/update/
    +PATCH /api/accounts/profile/update/
  }

  class Signup {
    +POST /api/accounts/signup/
  }

  class Token {
    +POST /api/accounts/token/
    +POST /api/accounts/token/refresh/
  }

  class Post {
    +GET /api/posts/id/
    +DELETE /api/posts/id/delete/
    +POST /api/posts/id/like/
    +DELETE /api/posts/id/unlike/
    +PUT /api/posts/id/update/
    +PATCH /api/posts/id/update/
    +POST /api/posts/create/
    +GET /api/posts/list/
  }

  class Bookmark {
    +GET /api/posts/bookmarks/
    +DELETE /api/posts/bookmarks/id/
    +POST /api/posts/bookmarks/create/
  }

  class Category {
    +GET /api/posts/categories/
  }

  class Comment {
    +GET /api/posts/post_id/comments/
    +GET /api/posts/post_id/comments/id/
    +PUT /api/posts/post_id/comments/id/
    +PATCH /api/posts/post_id/comments/id/
    +DELETE /api/posts/post_id/comments/id/
    +POST /api/posts/post_id/comments/create/
  }

  class Schema {
    +GET /api/schema/
  }

  Profile --> Signup : Uses
  Profile --> Token : Uses
  Post --> Comment : Contains
  Post --> Bookmark : Contains
  Post --> Category : Categorized by
  Profile --> Post : Creates/Interacts with
  Token --> Profile : Authenticates


```

<div align="right">

[목차](#목차)

</div>

## 4. 프로젝트 구조와 개발 일정
### 4.1 프로젝트 구조
```
📦ai-inventory-forecasting
┣ 📂.github
 ┃ ┣ 📂ISSUE_TEMPLATE
 ┃ ┃ ┣ 📜bug_report.md
 ┃ ┃ ┣ 📜custom.md
 ┃ ┃ ┗ 📜feature_request.md
 ┃ ┗ 📜PULL_REQUEST_TEMPLATE.md
 ┣ 📂.vscode
 ┃ ┗ 📜settings.json
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂comments
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂config
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
┣ 📂posts
 ┃ ┣ 📂migrations
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜factories.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.flake8
 ┣ 📜.gitignore
 ┣ 📜.pre-commit-config.yaml
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜pyproject.toml
 ┣ 📜REA및 UI
```

## 4.2 개발 일정
```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title 팀 프로젝트 개발 및 배포 일정 계획
    excludes weekends

    section 기획
    전체 구조 설계 및 모델링 :des1, 2024-03-29, 2d
    기획 수정 : 2024-04-08, 2d

    section 개발 환경
    개발 환경 세팅 :set1, 2024-03-29, 2d

    section DRF 학습
    DRF 학습::des1, 2024-04-02, 2d

    section 앱 개발
    accounts 앱 구현 :acc1, 2024-04-01, 7d
    posts 앱 구현 :pos1, 2024-04-01, 7d
    comments 앱 구현 :com1, 2024-04-01, 7d

    section 랜딩 페이지
    레이아웃 :lan1, 2024-04-01, 7d

    section 추가 기능
    추가 기능 : 2024-04-10, 4d

    section 챗봇 개발
    챗봇 기획 및 설계 :chat1, 2024-04-05, 2d
    챗봇 개발 :chat2, 2024-04-07, 8d
    

    section 테스트
    테스트 : 2024-04-05, 1d
    테스트 : 2024-04-12, 1d
    버그 수정 및 최적화 : 2024-04-14, 2d

    section 배포
    배포 준비 :deploy1, 2024-04-15, 1d
    배포 :deploy2, after deploy1, 2d
    
    section 문서화
    요구사항 : 2024-03-29, 1.5d
    기술 : 2024-03-30, 2d
    README : 2024-04-02, 2d
    README : doc1, 2024-04-16, 1d
```

<div align="right">

[목차](#목차)

</div>

## 5. 와이어프레임 및 화면 설계
### 5.1 와이어프레임
<table>
    <tbody>
        <tr>
            <td>랜딩 페이지</td>
            <td>로그인 랜딩 페이지</td>
        </tr>
        <tr>
            <td>
		<img src="samples/main.png" width="100%">
            </td>
            <td>
                <img src="samples/main_login.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>로그인</td>
            <td>소개 페이지</td>
        </tr>
        <tr>
            <td>
                <img src="samples/login_form.png" width="90%">
            </td>
            <td>
                <img src="samples/about.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>서비스 페이지</td>
        </tr>
        <tr>
            <td>
                <img src="samples/services.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

### 5.2 화면 설계

<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
		<img src="picture/main.gif" width="100%" >
            </td>
            <td>
                <img src="picture/login.gif" width="100%">
            </td>
        </tr>
        <tr>
            <td>회원가입</td>
            <td>정보수정</td>
        </tr>
        <tr>
            <td>
                <img src="picture/sign_up.gif" width="100%" >
            </td>
            <td>
                <img src="picture/profile.gif" width="100%" >
            </td>
        </tr>
        <tr>
            <td>검색</td>
            <td>번역</td>
        </tr>
        <tr>
            <td>
                <img src="ui3.png" width="100%">
            </td>
            <td>
                <img src="ui3.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>선택삭제</td>
            <td>글쓰기</td>
        </tr>
        <tr>
            <td>
	        <img src="ui3.png" width="100%">
            </td>
            <td>
                <img src="picture/post.gif" width="100%">
            </td>
        </tr>
        <tr>
            <td>글 상세보기</td>
            <td>댓글</td>
        </tr>
        <tr>
            <td>
                <img src="ui3.png" width="100%">
            </td>
            <td>
                <img src="ui3.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

<div align="right">

[목차](#목차)

</div>

## 6. 데이터베이스 모델링
![Untitled (6)](https://github.com/AI-Inventory-Forecasting-Team/ai-inventory-forecasting/assets/113663639/c90d4f37-70b7-43aa-93c2-4e134bf3e9ea)


<div align="right">

[목차](#목차)

</div>

## 7. Architecture

```mermaid

graph TD;
    CI[GitHub CI/CD] -->|Deploys| LS[AWS Lightsail];
    A[Django Application] -->|Uses| DRF[Django REST Framework];
    A -->|Connects to| DB[sqlite3];
    FE[Frontend] -->|Deployed on| LS;
    LS -->|Hosts| A;
    LS -->|Hosts| FE;

    classDef framework fill:#f9f,stroke:#333,stroke-width:2px;
    classDef aws fill:#ff9,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5;
    classDef ci fill:#9cf,stroke:#33f,stroke-width:2px;
    
    class A,DRF framework;
    class LS,S3 aws;
    class CI ci;
```


<div align="right">

[목차](#목차)

</div>

## 8. 트러블슈팅
### 8.1 버그 이름
#### 8.1.1 문제 원인
```
코드
```

- 문제 발생.. 
#### 8.1.2 해결 방법
```
```
- 이렇게 해서 해결했습니다.


<div align="right">

[목차](#목차)

</div>

## 9. 개발하며 느낀점
### 👩🏻‍💻 기준하
#### 부제
```

```

#### 부제
```

```

#### 부제
```

```


### 👩🏻‍💻 김민규
#### 부제
```

```

#### 부제
```

```

#### 부제
```

```

### 👩🏻‍💻 박주형
#### 도전의 연속
```
이번 프로젝트는 제게 첫 팀장 경험이었으며, 모든 팀원이 개발 경험이 전무한 상태에서 시작했습니다. 막막하고 어려운 도전이었지만, 매일 아침 커피챗을 통해 진행 상황을 공유하며 함께 학습하고 성장해나갔습니다. 조금이라도 도움이 되고 싶다는 의지를 갖고 계셔서 마무리가 가능했다고 생각합니다.
```

#### 동기부여
```

```

#### 지식 공유
```

```

### 👩🏻‍💻 한승일
#### 시작이 반이다
```
처음에는 제 실력으로 따라갈 수 있을까 팀원들을 방해할까 봐 걱정이 많았고 때론 포기하고 싶었던 순간도 있었습니다. 다행히도 좋은 팀장님과 팀원들을 만나서 함께 기본적인 기능이라도 구현해보는 시간을 가질 수 있었던 것이 너무 좋았습니다. 함께 노력하고 배우며 성장할 수 있는 환경이었기에 유의미한 시간이었습니다.
```

#### 부제
```

```

#### 부제
```

```
<div align="right">

[목차](#목차)

</div>
