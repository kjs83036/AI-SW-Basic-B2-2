# 🛠️ Git Troubleshooting Log (트러블슈팅 실습 기록)

팀 협업 및 개발 중 발생할 수 있는 주요 Git 실수와 문제 상황 4가지를 재현하고, 이를 안전하게 해결한 과정을 기록합니다.

---

## 시나리오 1: `git commit --amend` (최근 커밋 수정)

### 👥 참여자
- **실행자:** 팀원 A (Kim)
- **검토자:** 팀원 B (Lee)

### 📌 문제 상황
- `math_ops.py`에 제곱 연산 함수를 추가하고 `feat: add basic math utility functions`로 로컬 커밋을 완료했으나, 필수 docstring과 타입 힌트를 누락한 것을 뒤늦게 발견함.
- 아직 원격에 공유하기 전이므로 불필요하게 커밋을 하나 더 쌓지 않고 기존 커밋에 수정을 덮어씌우고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
git add src/utils/math_ops.py
git commit --amend -m "feat: add power function with type annotations and docstring"
git log -n 1
```

### 🎯 결과 및 주의점
- 불필요한 커밋 없이 깔끔하게 단일 커밋으로 수정 완료됨.
- **주의점:** 이미 push된 커밋에 대해 `amend`를 수행하면 강제 푸시가 필요해지고 다른 팀원의 브랜치가 꼬이므로 로컬 커밋에만 사용해야 함.

---

## 시나리오 2: `git reset --soft HEAD~1` (로컬 커밋 취소 및 변경사항 보존)

### 👥 참여자
- **실행자:** 팀원 B (Lee)
- **검토자:** 팀원 C (Park)

### 📌 문제 상황
- 팀원 B가 문자열 함수 추가(`string_utils.py`)와 문서 수정(`docs/date.md`)을 실수로 하나의 커밋(`feat: add slugify and update docs`)으로 한 번에 커밋함.
- "단일 책임 원칙"에 맞게 분리하기 위해 작업 트리는 그대로 살려둔 채 커밋만 취소하고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
git reset --soft HEAD~1
git reset HEAD docs/date.md
git add src/utils/string_ops.py
git commit -m "feat: add slugify and truncate_words utilities"
```

### 🎯 결과 및 왜 이 방법을 선택했는가
- `--hard` 대신 `--soft`를 사용하여 작성한 코드가 삭제되는 일 없이 커밋 단위를 성공적으로 둘로 쪼갤 수 있었음.

---

## 시나리오 3: `git revert` (원격에 push된 잘못된 커밋 취소)

### 👥 참여자
- **실행자:** 팀원 C (Park)
- **검토자:** 팀원 A (Kim)

### 📌 문제 상황
- 팀원 C가 날짜 포맷 변환기에 특정 서드파티 라이브러리에 의존하는 실험적 코드를 작성하여 머지/푸시함.
- 공유 브랜치이므로 히스토리를 강제로 되돌리는 `reset` 대신 안전하게 되돌리는 새로운 커밋을 만들어야 함.

### 🛠️ 시도한 명령 및 절차
```bash
git log --oneline -n 3
git revert HEAD --no-edit
```

### 🎯 결과 및 왜 이 방법을 선택했는가
- 히스토리를 지우지 않고 `Revert "feat: add experimental timezone parser"`라는 명확한 이력을 남기며 빌드 정상화를 달성함.

---

## 시나리오 4: `git stash` & `git stash pop` (작업 임시 보관 및 전환)

### 👥 참여자
- **실행자:** 팀원 A (Kim) & 팀원 C (Park)

### 📌 문제 상황
- `feature/park-date-utils` 브랜치에서 작업하던 중, 메인 브랜치의 긴급 이슈 검토 요청을 받음.
- 미완성 코드를 임시 커밋으로 남기지 않고 작업 트리를 깨끗하게 보관한 뒤 브랜치를 전환하고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
git stash save "WIP: date utils relative time"
git checkout main
# (검토 완료)
git checkout feature/park-date-utils
git stash pop
```

### 🎯 결과 및 이점
- 브랜치를 오가면서도 쓰레기 커밋을 남기지 않고 유연하게 컨텍스트 스위칭을 수행함.
