# 📋 Submission Index (제출물 인덱스)

**과제명:** B2-2 친구 3~5명과 함께 프로그램 만드는 법 연습하기  
**분야:** AI/SW 기초 | Python과 Git 심화  

---

## 1. 👥 Team Information (팀 정보)

- **팀명:** Git-Triad (3인 실습팀)
- **저장소 (Repository URL):** `https://github.com/git-triad/team-python-utils`

| 팀원 이름 | GitHub 아이디 | 주 역할 및 담당 모듈 |
| :--- | :--- | :--- |
| **팀원 A (Kim)** | `@dev-kim-math` | 팀 리드, `math_ops.py` 모듈, 패키지 리팩토링, `amend` & `stash` 트러블슈팅 |
| **팀원 B (Lee)** | `@dev-lee-string` | `string_ops.py` 모듈, 충돌 2건(Hunk/Rename) 해결 담당, `reset --soft` 트러블슈팅 |
| **팀원 C (Park)** | `@dev-park-date` | `date_ops.py` 모듈, 종합 테스트 스위트 통합, `revert` 트러블슈팅 |

---

## 2. 🔀 Member PRs & Contributions (팀원별 PR 및 기여도)

모든 팀원이 **PR 생성/병합 2개 이상**, **코드 리뷰 2개 이상**, **리뷰 피드백 반영 1회 이상** 기준을 충족하였습니다.

### 🔹 팀원 A (Kim)
- **생성 및 병합된 PR:**
  1. [PR #1] `feat: add math utility functions and exports` (`feature/kim-math-utils` -> `main`)
  2. [PR #4] `refactor: restructure utils package layout` (`refactor/kim-package-structure` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #2 Review] 팀원 B의 PR에 `strip_all_whitespace` 성능 및 엣지케이스 개선 코멘트 작성 (Approved)
  - [PR #3 Review] 팀원 C의 PR에 상대 시간 변환 함수 `get_relative_time_string` 추가 제안 코멘트 작성 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #1에서 팀원 B의 피드백(0으로 나눌 때 ZeroDivisionError 예외 방지 `default=0.0` 추가)을 수용하여 `divide` 함수 수정 커밋 반영.

### 🔹 팀원 B (Lee)
- **생성 및 병합된 PR:**
  1. [PR #2] `feat: add string manipulation utilities` (`feature/lee-string-utils` -> `main`)
  2. [PR #5] `feat: add advanced string parsers and resolve rename conflict` (`feature/lee-advanced-strings` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #1 Review] 팀원 A의 PR에 `divide` 0 나누기 예외 방어코드 `default: Number = 0.0` 제안 (Request Changes -> Approved)
  - [PR #6 Review] 팀원 C의 PR에 pytest fixture 구조 검토 및 엣지케이스 테스트 추가 승인 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #2에서 팀원 C의 피드백(탭, 줄바꿈 등 복합 화이트스페이스 제거)을 반영하여 커밋 추가.

### 🔹 팀원 C (Park)
- **생성 및 병합된 PR:**
  1. [PR #3] `feat: add date parsing and formatting utilities` (`feature/park-date-utils` -> `main`)
  2. [PR #6] `test: add comprehensive test suite across all modules` (`feature/park-test-suite` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #2 Review] 팀원 B의 PR에 정규식/화이트스페이스 분할 처리 제안 코멘트 작성 (Request Changes -> Approved)
  - [PR #4 Review] 팀원 A의 PR에 패키지 디렉토리 이동에 따른 import 경로 호환성 체크 코멘트 작성 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #3에서 팀원 A의 피드백(`get_relative_time_string` 상대 시간 함수 구현)을 반영하여 커밋 추가.

---

## 3. 📑 Key Documents (핵심 협업 문서 링크)

- 🤝 **협업 가이드:** [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- 💥 **충돌 해결 기록 (비자명 충돌 포함):** [docs/conflict-resolution.md](docs/conflict-resolution.md)
- 🛠️ **트러블슈팅 실습 기록 (4종):** [docs/troubleshooting-log.md](docs/troubleshooting-log.md)

---

## 4. 🌳 Git History Evidence (히스토리 증빙)

`git log --oneline --graph --all` 명령어 실행 결과:

```text
*   0cd602e Merge pull request #6 from feature/park-test-suite
|\  
| * a2741f6 test: add comprehensive test suite across all modules
|/  
*   12d5b04 Merge pull request #5 from feature/lee-advanced-strings
|\  
| * db6cbbf refactor: migrate advanced string functions to new utils path (resolve rename conflict)
| *   0573d67 Merge branch 'main' into feature/lee-advanced-strings
| |\  
| |/  
|/|   
* |   f6ce01c Merge pull request #4 from refactor/kim-package-structure
|\ \  
| * | 1f8f385 refactor: restructure utils package directory layout
|/ /  
| * 5c994b1 feat: add slugify and truncate_words utilities
|/  
*   1adbdb8 Merge pull request #3 from feature/park-date-utils
|\  
| * 60d0ad0 feat: add relative time formatter (apply review feedback)
| * 0356bae Revert "feat: add experimental timezone parser"
| * f54c781 feat: add experimental timezone parser
| * 9311886 feat: add date parsing and formatting utilities
|/  
*   97667b8 Merge pull request #2 from feature/lee-string-utils
|\  
| * 4f02d02 feat: add whitespace strip and reverse utilities (apply review feedback)
| *   1466948 fix: resolve import export conflict in __init__.py
| |\  
| |/  
|/|   
* |   22b628f Merge pull request #1 from feature/kim-math-utils
|\ \  
| * | 3af0615 feat: add zero division safeguard (apply review feedback)
| * | 0caf295 feat: add power function with type annotations and docstring
|/ /  
| * 3391f56 feat: add string manipulation utilities
|/  
* 2347b7e chore: initial commit with basic project structure and contributing guides
```

---

## 5. 🧪 Pytest Verification Result (단위 테스트 100% 통과)

```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\sktlrkan\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: g:\내 드라이브\codyssey\antigravity\B2-2\SAMPLE\SAMPLE_4
plugins: base-url-2.1.0, playwright-0.8.0
collecting ... collected 14 items

tests/test_date_ops.py::test_format_iso_date PASSED                      [  7%]
tests/test_date_ops.py::test_parse_date_string PASSED                    [ 14%]
tests/test_date_ops.py::test_add_days_and_between PASSED                 [ 21%]
tests/test_date_ops.py::test_get_relative_time_string PASSED             [ 28%]
tests/test_math_ops.py::test_basic_arithmetic PASSED                     [ 35%]
tests/test_math_ops.py::test_divide_by_zero PASSED                       [ 42%]
tests/test_math_ops.py::test_power PASSED                                [ 50%]
tests/test_math_ops.py::test_calculate_average PASSED                    [ 57%]
tests/test_string_ops.py::test_capitalize_words PASSED                   [ 64%]
tests/test_string_ops.py::test_reverse_string PASSED                     [ 71%]
tests/test_string_ops.py::test_strip_all_whitespace PASSED               [ 78%]
tests/test_string_ops.py::test_to_snake_case PASSED                      [ 85%]
tests/test_string_ops.py::test_slugify PASSED                            [ 92%]
tests/test_string_ops.py::test_truncate_words PASSED                     [100%]

============================= 14 passed in 0.33s ==============================
```
