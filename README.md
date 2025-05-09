![img](docs/logo.jpg)

# 📧 이메일 클라이언트 프로젝트

| 구분 | GITHUB 주소 |
|--------------|-----------------|
| FRONTEND | https://github.com/ellen24k/mail-client |
| BACKEND  | https://github.com/ellen24k/mail-client-api |


## 📝 프로젝트 개요
이 프로젝트는 IMAP 프로토콜을 사용하여 지정된 메일 서버에서 이메일을 가져와 사용자에게 보여주고, SMTP 프로토콜을 통해 이메일을 발송할 수 있는 웹 기반 메일 클라이언트 및 해당 기능을 제공하는 API 서버입니다. <br/>
사용자는 웹 인터페이스를 통해 이메일 목록을 확인하고, 각 이메일의 내용을 열람하며, 제목, 발신자, 본문 내용으로 이메일을 검색하고, 새로운 이메일을 작성하여 발송할 수 있습니다.

## ✨ 주요 기능

### 프론트엔드 (Web Client)
-   **이메일 수신 및 목록 표시**: 백엔드 API를 통해 IMAP 이메일 데이터를 가져와 목록 형태로 표시합니다.
-   **이메일 상세 내용 확인**: 각 수신 이메일 항목을 클릭(아코디언 확장)하여 상세 내용을 확인할 수 있습니다. (발신자, 날짜, 본문)
-   **실시간 검색 (수신 메일)**: 제목, 발신자, 본문 내용 기준으로 수신된 이메일을 필터링하여 검색할 수 있습니다.
-   **새로고침 기능 (수신 메일)**: 최신 이메일 데이터를 다시 불러올 수 있습니다.
-   **이메일 발송 (SMTP)**: 사용자 입력을 받아 백엔드 API를 통해 SMTP 이메일을 발송합니다.
    -   발신자, 수신자 이메일 주소 선택/입력
    -   제목 및 내용 작성
-   **로딩 상태 표시**: 데이터 로딩 또는 이메일 발송 중임을 사용자에게 시각적으로 안내합니다.
-   **오류 처리 및 알림**: 데이터 로딩 실패 또는 이메일 발송 실패/성공 시 사용자에게 토스트 메시지로 알립니다.

### 백엔드 (API Server)
-   **이메일 송신 API**: 지정된 발신자(Gmail/Naver)를 통해 수신자(Gmail/Naver)에게 이메일을 전송하는 API를 제공합니다.
-   **이메일 수신 API**: 지정된 수신자(Gmail/Naver)의 받은 편지함에서 최근 5개의 이메일을 가져오는 API를 제공합니다.

## 🛠️ 기술 스택

### 프론트엔드
<p>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS"/>
  <img src="https://img.shields.io/badge/shadcn/ui-000000?style=for-the-badge&logo=shadcnui&logoColor=white" alt="shadcn/ui"/>
  <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" alt="Axios"/>
</p>

### 백엔드
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
</p>

## 🖼️ 실행 화면
<!-- 실행 화면 GIF를 여기에 추가하세요 -->
![실행 화면 GIF](docs/demo.gif)

## 🖥️ 프론트 화면구성
| 컴포넌트        | 파일 경로                                        | 설명                                                                             |
|-------------|----------------------------------------------|--------------------------------------------------------------------------------|
| `TabOne`    | `src/components/TabOne.tsx`                  | SMTP를 이용한 이메일 발송 기능을 담당하는 컴포넌트. 발신자, 수신자, 제목, 내용 입력 및 전송 처리.                   |
| `ImapTab`   | `src/components/Imap.tsx`                    | IMAP 메일 목록을 표시하고 관리하는 주 컴포넌트. 검색, 새로고침 기능 포함.                                  |
| `TabTwo`    | `src/components/TabTwo.tsx`                  | `ImapTab` 컴포넌트를 특정 API URL (`http://localhost:8000/imap/gmail`)로 렌더링하는 탭 컴포넌트. |
| `TabThree`  | `src/components/TabThree.tsx`                | `ImapTab` 컴포넌트를 특정 API URL (`http://localhost:8000/imap/naver`)로 렌더링하는 탭 컴포넌트. |
| `Input`     | `src/components/ui/input.tsx`                | shadcn/ui 기반의 커스텀 Input 컴포넌트.                                                  |
| `Button`    | `src/components/ui/button.tsx`               | shadcn/ui 기반의 커스텀 Button 컴포넌트.                                                 |
| `Card`      | `src/components/ui/card.tsx`                 | shadcn/ui 기반의 Card 레이아웃 컴포넌트.                                                  |
| `Accordion` | `src/components/ui/accordion.tsx`            | shadcn/ui 기반의 Accordion 컴포넌트로 IMAP 메일 내용 표시에 사용.                               |
| `Select`    | (HTML 기본 `select` 또는 shadcn/ui `Select`)     | 발신/수신 이메일 계정 선택에 사용. (`TabOne.tsx` 내)                                          |
| `Textarea`  | (HTML 기본 `textarea` 또는 shadcn/ui `Textarea`) | 이메일 본문 내용 입력에 사용. (`TabOne.tsx` 내)                                             |

### `TabOne` 컴포넌트 상세 (SMTP 발송)
-   **상태 (State)**:
    -   `selectedSender`: 선택된 발신자 이메일 (문자열)
    -   `to_email`: 수신자 이메일 (문자열)
    -   `subject`: 이메일 제목 (문자열)
    -   `content`: 이메일 내용 (문자열)
    -   `loading`: 이메일 발송 중 로딩 상태 (boolean)
-   **주요 함수**:
    -   `sendSmtp`: 입력된 정보를 바탕으로 SMTP API를 호출하여 이메일을 발송합니다. 입력 값 유효성 검사, API 호출, 성공/실패 알림 처리.
-   **UI 요소**:
    -   발신 이메일 선택 (`select`): `EMAILS` 목록에서 발신 계정 선택
    -   수신 이메일 선택 (`select`): `EMAILS` 목록에서 수신 계정 선택
    -   제목 입력 (`Input`): 이메일 제목 작성
    -   내용 입력 (`textarea`): 이메일 본문 작성
    -   전송 버튼 (`Button`): `sendSmtp` 함수 호출, 로딩 상태에 따라 UI 변경

### `ImapTab` 컴포넌트 상세 (IMAP 수신) - TabTwo, TabThree에서 apiUrl 만 변경해서 사용. 
-   **상태 (State)**:
    -   `mails`: 원본 메일 목록 배열
    -   `loading`: 데이터 로딩 상태 (boolean)
    -   `search`: 검색어 문자열
    -   `filtered`: 검색 결과가 반영된 필터링된 메일 목록 배열
-   **주요 함수**:
    -   `fetchMails`: `apiUrl` props로 전달받은 주소에서 메일 데이터를 비동기적으로 가져옵니다.
-   **UI 요소**:
    -   검색창 (`Input`): 메일 검색 기능 제공
    -   새로고침 버튼 (`Button`): `fetchMails` 함수 호출
    -   메일 목록 (`Accordion`): 필터링된 메일들을 아코디언 형태로 표시
        -   `AccordionTrigger`: 메일 제목 표시
        -   `AccordionContent`: 메일 상세 내용 (발신자, 날짜, 본문) 표시

## ⚙️ 백엔드 API
| Endpoint                                              | 설명                                     | 요청 파라미터 (URL Path)                                  | 응답 (성공 시)                                                                |
 |:------------------------------------------------------| :--------------------------------------- | :-------------------------------------------------------- |:-------------------------------------------------------------------------|
| `/smtp/` <br/> `{sender}/` <br/> `{receiver}/` <br/> `{title}/` <br/> `{content}` | SMTP를 통해 이메일을 발송합니다.           | `sender`: (str) gmail 또는 naver<br>`receiver`: (str) gmail 또는 naver<br>`title`: (str) 메일 제목 (URL 인코딩 필요)<br>`content`: (str) 메일 내용 (URL 인코딩 필요) | 메일 전송 성공 또는 실패 메시지                                                       |
| `/imap/` <br/> `{receiver}`                                    | 지정된 메일박스에서 IMAP 이메일 목록을 가져옵니다. | `receiver`: (str) gmail 또는 naver                        | `Mail[]` (아래 데이터 구조 참조) - 최근 5개 이메일 목록 또는 오류 메시지                         |

**API 호출 예시:**
-   **메일 송신 (프론트엔드에서 Axios 사용 시)**:
    ```javascript
    // title과 content는 URL 인코딩 필요
    const encodedTitle = encodeURIComponent("안녕하세요");
    const encodedContent = encodeURIComponent("테스트 메일입니다.");
    axios.get(`http://localhost:8000/smtp/gmail/naver/${encodedTitle}/${encodedContent}`);
    ```
-   **메일 수신 (프론트엔드에서 Axios 사용 시)**:
    ```javascript
    axios.get("http://localhost:8000/imap/naver");
    ```
*IMAP API URL은 `apiUrl` prop을 통해 `ImapTab` 컴포넌트에 전달됩니다. (예: `http://localhost:8000/imap/naver`)*
*SMTP API URL은 `TabOne.tsx` 내에서 직접 구성되어 호출됩니다.*

## 🔗 배치 다이어그램
![deploy](docs/deploy.png)

## 📊 데이터 구조

### `Mail` 타입 (IMAP 수신 메일 - 프론트엔드)
메일 한 개의 정보를 나타내는 타입입니다.
```typescript
type Mail = {
    from: string;    // 발신자
    title: string;   // 메일 제목
    date: string;    // 수신 날짜 (문자열 형식)
    content: string; // 메일 본문 내용
};
```
| 필드      | 타입   | 설명                                   | 예시                               |
| --------- | ------ | -------------------------------------- | ---------------------------------- |
| `from`    | `string` | 이메일 발신자 주소 또는 이름           | `"sender@example.com"`             |
| `title`   | `string` | 이메일 제목                            | `"중요 공지사항"`                  |
| `date`    | `string` | 이메일 수신 날짜 및 시간 | `"Date : Thu, 08 May 2025 00:02:17 -0700 (PDT)"`           |
| `content` | `string` | 이메일 본문     | `"안녕하세요. 메일 내용입니다..."` |

### `EMAILS` 상수 (프론트엔드 발신/수신 계정 목록)
`TabOne.tsx`에서 사용되는 발신/수신 이메일 계정 목록입니다.
```typescript
const EMAILS = [
    {label: "NAVER", value: "naver"}, // 실제 이메일 주소 또는 식별자로 변경 필요
    {label: "GMAIL", value: "gmail"}, // 실제 이메일 주소 또는 식별자로 변경 필요
];
```

## 🚀 설치 및 실행

### 사전 준비 사항
-   **Node.js 및 npm/yarn/pnpm**: 프론트엔드 실행을 위해 필요합니다. (Node.js LTS 버전 권장)
-   **GMAIL, NAVER의 메일 환경설정 메뉴에서 SMTP, IMAP 사용 허용**
-   **Python**: 백엔드 실행을 위해 필요합니다. (Python 3.x 버전 권장)
-   **Git**: 소스 코드 복제를 위해 필요합니다.
-   **환경 변수 설정 (백엔드)**:
    -   `GMAIL_EMAIL`: Gmail 주소
    -   `GMAIL_PASSWORD`: Gmail 앱 비밀번호 (2단계 인증 사용 시)
    -   `NAVER_EMAIL`: Naver 메일 주소
    -   `NAVER_PASSWORD`: Naver 메일 비밀번호

### 1. 저장소 복제
```bash
git clone https://github.com/ellen24k/mail-client-api.git
git clone https://github.com/ellen24k/mail-client.git
```

### 2. 백엔드 (API 서버) 설치 및 실행
```bash
cd mail-client-api
uv sync
uvicorn main:app --reload --host 0.0.0.0 --port 8000 
```
-   필요시 python, uv 등 설치.
-   API 문서 확인: `http://127.0.0.1:8000/docs`

### 3. 프론트엔드 (웹 클라이언트) 설치 및 실행
```bash
cd mail-client
# 의존성 설치
npm install
# 또는
yarn install
# 또는
pnpm install

# 환경 변수 설정 (필요한 경우)
# .env.local 파일을 생성하고 필요한 환경 변수를 설정합니다.
# 예: NEXT_PUBLIC_API_BASE_URL=http://localhost:8000

# 개발 서버 실행
npm run dev
# 또는
yarn dev
# 또는
pnpm dev
```
-   필요시 nodejs, npm 등 설치.
-   애플리케이션은 `http://localhost:3000` (기본값)에서 실행.


## 📒 용어
| 용어           | 설명                                                                                   |
|:-------------| :------------------------------------------------------------------------------------- |
| SMTP         | Simple Mail Transfer Protocol, 이메일 송신 프로토콜                                      |
| IMAP         | Internet Message Access Protocol, 이메일 수신 프로토콜                                   |
| FastAPI      | Python 기반의 현대적이고 빠른 웹 프레임워크 (백엔드)                                     |
| React        | 사용자 인터페이스 구축을 위한 JavaScript 라이브러리 (프론트엔드)                         |
| Next.js      | React 기반의 서버 사이드 렌더링 및 정적 웹 생성을 위한 프레임워크 (프론트엔드)             |
| TypeScript   | JavaScript에 정적 타입을 추가한 언어 (프론트엔드)                                        |
| Tailwind CSS | 유틸리티 우선 CSS 프레임워크 (프론트엔드)                                                |
| shadcn/ui    | 재사용 가능한 UI 컴포넌트 모음 (프론트엔드)                                              |
| Axios        | Promise 기반 HTTP 클라이언트 (프론트엔드에서 API 호출 시 사용)                            |
| CORS         | Cross-Origin Resource Sharing, 교차 출처 리소스 공유 정책 (백엔드에서 설정 필요)         |
| Sonner,Toast | 사용자에게 간단한 메시지(성공, 실패, 알림 등)를 화면에 잠시 표시하는 UI 요소 (프론트엔드) |

## 📚 레퍼런스
-   [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
-   [Python `smtplib` 문서](https://docs.python.org/3/library/smtplib.html)
-   [Python `imaplib` 문서](https://docs.python.org/3/library/imaplib.html)
-   [Python `email` 모듈 문서](https://docs.python.org/3/library/email.html)
-   [React 공식 문서](https://react.dev/)
-   [Next.js 공식 문서](https://nextjs.org/docs)
-   [Tailwind CSS 공식 문서](https://tailwindcss.com/docs)
-   [shadcn/ui](https://ui.shadcn.com/)
-   [Axios 공식 문서](https://axios-http.com/docs/intro)

