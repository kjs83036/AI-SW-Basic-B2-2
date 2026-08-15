# 🛠️ Team Python Utility Toolkit

팀 협업 및 Git 워크플로우(GitHub Flow, Issue-PR 연동, 코드 리뷰, 충돌 해결, 트러블슈팅) 실습을 위해 구축된 다목적 Python 유틸리티 라이브러리입니다.

---

## 📌 GitHub Flow 채택 이유 (3줄 요약)

1. `main` 브랜치를 항상 배포 가능한 안정 상태로 유지하여 배포 및 릴리즈 주기를 단순화합니다.
2. 기능별 `feature/*` 브랜치와 PR을 통해 상호 코드 리뷰 및 자동화 검증을 필수로 거치도록 강제합니다.
3. 복잡한 다단계 브랜치(Git Flow 등) 대비 협업 진입 장벽이 낮고 병합 충돌을 빠르게 감지하여 해결할 수 있습니다.

---

## 🚀 주요 기능 모듈

| 모듈명 | 주요 기능 및 함수 | 담당자 |
| :--- | :--- | :---: |
| **`src.utils.math_ops`** | 기본 사칙연산, 예외 안전 나눗셈(`divide`), 거듭제곱(`power`), 산술 평균(`calculate_average`) | 팀원 A (Kim) |
| **`src.utils.string_ops`** | 첫 글자 대문자화(`capitalize_words`), 문자열 뒤집기(`reverse_string`), 공백 제거, `to_snake_case`, `slugify`, `truncate_words` | 팀원 B (Lee) |
| **`src.utils.date_ops`** | ISO 날짜 포맷팅(`format_iso_date`), 날짜 파싱(`parse_date_string`), 일자 덧셈/계산, 상대 시간 표현(`get_relative_time_string`) | 팀원 C (Park) |

---

## 💻 개발 및 테스트 환경

- **언어:** Python 3.10+ (현재 테스트 환경: Python 3.12)
- **테스트 프레임워크:** `pytest`

### 테스트 실행 방법
```bash
# 전체 단위 테스트 실행
pytest tests/

# 상세 결과 출력
pytest -v tests/
```

---

## 📁 디렉토리 구조

```text
B2-2/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── feature_request.md     # 작업 이슈 템플릿
│   └── pull_request_template.md   # PR What/Why/How 템플릿
├── docs/
│   ├── CONTRIBUTING.md            # 브랜치/커밋/PR/리뷰 협업 규칙
│   ├── conflict-resolution.md     # 비자명 충돌 포함 2건 해결 기록
│   └── troubleshooting-log.md     # Git 4종(amend/reset/revert/stash) 트러블슈팅 로그
├── src/
│   └── utils/
│       ├── __init__.py            # 통합 패키지 진입점
│       ├── date_ops.py            # 날짜/시간 유틸
│       ├── math_ops.py            # 수학 연산 유틸
│       └── string_ops.py          # 문자열 처리 유틸
├── tests/
│   ├── __init__.py
│   ├── test_date_ops.py           # 날짜 유틸 단위 테스트
│   ├── test_math_ops.py           # 수학 유틸 단위 테스트
│   └── test_string_ops.py         # 문자열 유틸 단위 테스트
├── B2-2_실행_가이드_플레이북.md       # 팀원 3인을 위한 실습 시나리오 & 명령어 대본
├── README.md                      # 프로젝트 소개 및 가이드
└── SUBMISSION.md                  # 최종 과제 제출 인덱스 문서
```

---

## 👥 팀원 및 협업 규칙
상세한 협업 규칙과 브랜치 전략은 [docs/CONTRIBUTING.md](file:///g:/%EB%82%B4%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C/codyssey/antigravity/B2-2/docs/CONTRIBUTING.md)를 참고하세요.
