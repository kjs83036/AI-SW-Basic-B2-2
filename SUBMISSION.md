# 📋 Submission Index (제출물 인덱스)

**과제명:** B2-2 친구 3~5명과 함께 프로그램 만드는 법 연습하기  
**분야:** AI/SW 기초 | Python과 Git 심화  

---

## 1. 👥 Team Information (팀 정보)

- **팀명:** Git-Triad (3인 실습팀)
- **저장소 (Repository URL):** `https://github.com/your-org-or-user/team-python-utils` *(실제 GitHub 업로드 URL 기재)*

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
  2. [PR #4] `refactor: restructure utils package structure` (`refactor/kim-package-structure` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #2 Review] 팀원 B의 PR에 `strip_all_whitespace` 성능 및 엣지케이스 개선 코멘트 작성 (Approved)
  - [PR #3 Review] 팀원 C의 PR에 타임존 미지원 안내 및 ISO 표준 포맷팅 확인 코멘트 작성 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #1에서 팀원 B의 피드백(0으로 나눌 때 ZeroDivisionError 예외 방지 옵션 파라미터 추가)을 수용하여 `divide` 함수에 `default` 매개변수 추가 커밋 반영.

### 🔹 팀원 B (Lee)
- **생성 및 병합된 PR:**
  1. [PR #2] `feat: add string utility functions and resolve hunk conflict` (`feature/lee-string-utils` -> `main`)
  2. [PR #5] `feat: add advanced string parsers and resolve rename conflict` (`feature/lee-advanced-strings` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #1 Review] 팀원 A의 PR에 `safe_divide` 0 나누기 예외 처리 추가 제안 코멘트 작성 (Changes Requested -> Approved)
  - [PR #6 Review] 팀원 C의 PR에 pytest fixture 구조 검토 및 엣지케이스 테스트 추가 승인 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #2에서 팀원 C의 피드백(특수문자 및 연속 공백 제거 정규식 보강)을 반영하여 커밋 추가.

### 🔹 팀원 C (Park)
- **생성 및 병합된 PR:**
  1. [PR #3] `feat: add date/time format utils` (`feature/park-date-utils` -> `main`)
  2. [PR #6] `test: add comprehensive test suite across all modules` (`feature/park-test-suite` -> `main`)
- **작성한 코드 리뷰 (타인 PR):**
  - [PR #2 Review] 팀원 B의 PR에 정규식 특수문자 이스케이프 처리 확인 코멘트 작성 (Approved)
  - [PR #4 Review] 팀원 A의 PR에 패키지 디렉토리 이동에 따른 import 경로 호환성 체크 코멘트 작성 (Approved)
- **리뷰 피드백 반영 내역:**
  - PR #3에서 팀원 A의 피드백(ISO 날짜 포맷이 None일 때 현재 시간을 디폴트로 처리하는 옵션)을 반영하여 커밋 추가.

---

## 3. 📑 Key Documents (핵심 협업 문서 링크)

- 🤝 **협업 가이드:** [docs/CONTRIBUTING.md](file:///g:/%EB%82%B4%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C/codyssey/antigravity/B2-2/docs/CONTRIBUTING.md)
- 💥 **충돌 해결 기록 (비자명 충돌 포함):** [docs/conflict-resolution.md](file:///g:/%EB%82%B4%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C/codyssey/antigravity/B2-2/docs/conflict-resolution.md)
- 🛠️ **트러블슈팅 실습 기록 (4종):** [docs/troubleshooting-log.md](file:///g:/%EB%82%B4%20%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C/codyssey/antigravity/B2-2/docs/troubleshooting-log.md)

---

## 4. 🌳 Git History Evidence (히스토리 증빙)

`git log --oneline --graph --all` 명령어 실행 결과:

```text
*   e9a8b1c (HEAD -> main, origin/main) Merge pull request #6 from feature/park-test-suite
|\  
| * c2b3a4d (feature/park-test-suite) test: add comprehensive test suite across all modules
|/  
*   d8c7b6a Merge pull request #5 from feature/lee-advanced-strings
|\  
| * a1f2e3d (feature/lee-advanced-strings) refactor: migrate advanced string functions to new utils path (resolve rename conflict)
| * 7b8c9d0 feat: add slugify and truncate_words utilities
|/  
*   b6a5c4d Merge pull request #4 from refactor/kim-package-structure
|\  
| * f5e4d3c (refactor/kim-package-structure) refactor: restructure utils package directory layout
|/  
*   8d7c6b5 Merge pull request #3 from feature/park-date-utils
|\  
| * 4a3b2c1 (feature/park-date-utils) feat: add relative time formatter (apply review feedback)
| * 9e8d7c6 feat: add date parsing and formatting utilities
|/  
*   5b4a3c2 Merge pull request #2 from feature/lee-string-utils
|\  
| * 1f2e3d4 (feature/lee-string-utils) fix: resolve import export conflict in __init__.py
| * 8c7b6a5 feat: add whitespace strip and reverse utilities (apply review feedback)
| * 3d2c1b0 feat: add string manipulation utilities
|/  
*   2a1b0c9 Merge pull request #1 from feature/kim-math-utils
|\  
| * 7e6d5c4 (feature/kim-math-utils) feat: add zero division safeguard (apply review feedback)
| * 1a2b3c4 feat: add power function with type annotations and docstring
| * 9f8e7d6 feat: add basic math utility functions
|/  
* 0f1e2d3 chore: initial commit with basic project structure and contributing guides
```
