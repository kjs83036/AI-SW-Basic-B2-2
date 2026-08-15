# 🐍 Team Python Utils (3인 협업 실습 저장소)

친구 3~5명과 함께 프로그램 만드는 법(B2-2) 연습을 위한 Python 유틸리티 라이브러리 협업 프로젝트입니다.

---

## 👥 팀원 및 역할

- **팀원 A (Kim - 팀 리드)**: 수학 유틸리티 (`math_ops.py`), 패키지 리팩토링, `amend` & `stash` 트러블슈팅
- **팀원 B (Lee)**: 문자열 유틸리티 (`string_ops.py`), 충돌 해결 2건(Hunk/Rename), `reset --soft` 트러블슈팅
- **팀원 C (Park)**: 날짜/시간 유틸리티 (`date_ops.py`), 종합 테스트 스위트 통합, `revert` 트러블슈팅

---

## 🛠️ 프로젝트 구조

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── docs/
│   ├── CONTRIBUTING.md
│   ├── conflict-resolution.md
│   └── troubleshooting-log.md
├── src/
│   └── utils/
│       ├── __init__.py
│       ├── math_ops.py
│       ├── string_ops.py
│       └── date_ops.py
├── tests/
│   ├── __init__.py
│   ├── test_math_ops.py
│   ├── test_string_ops.py
│   └── test_date_ops.py
├── README.md
└── SUBMISSION.md
```

---

## 🚀 브랜치 전략 (GitHub Flow)
우리 팀은 빠른 피드백과 안정적인 배포를 위해 **GitHub Flow**를 적용합니다. 자세한 협업 규칙은 [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)를 참고하세요.
