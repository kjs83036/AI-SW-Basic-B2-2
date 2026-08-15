# 🛠️ Git Troubleshooting Log (트러블슈팅 실습 기록)

팀 협업 및 개발 중 발생할 수 있는 주요 Git 실수와 문제 상황 4가지를 재현하고, 이를 안전하게 해결한 과정을 기록합니다.

---

## 시나리오 1: `git commit --amend` (최근 커밋 수정)

### 👥 참여자
- **실행자:** 팀원 A (Kim)
- **검토자:** 팀원 B (Lee)

### 📌 문제 상황
- `math_ops.py`에 제곱 연산 함수를 추가하고 `feat: add power function`으로 로컬 커밋을 완료했으나, 함수에 필수 docstring과 타입 힌트를 누락한 것을 뒤늦게 발견함.
- 아직 원격 저장소(`origin`)에 push하기 전이므로 불필요하게 커밋을 하나 더 쌓지 않고 기존 커밋에 수정을 덮어씌우고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
# 1. 파일 수정 (docstring 및 타입 힌트 추가)
# 2. 수정한 파일 스테이징
git add src/utils/math_ops.py

# 3. 최근 커밋에 포함시키며 커밋 메시지도 명확하게 수정
git commit --amend -m "feat: add power function with type annotations and docstring"

# 4. 히스토리 검증
git log -n 1
```

### 🎯 결과 및 주의점
- 불필요한 "fix: add docstring" 커밋 없이 깔끔하게 단일 커밋으로 수정 완료됨.
- **주의점:** 이미 `origin`에 push된 커밋에 대해 `amend`를 수행하면 히스토리가 변조되어 강제 푸시(`--force`)가 필요해지고 다른 팀원과의 브랜치가 꼬이므로, **반드시 로컬에만 존재하는 커밋에 한하여 사용**해야 함.

---

## 시나리오 2: `git reset --soft HEAD~1` (로컬 커밋 취소 및 변경사항 보존)

### 👥 참여자
- **실행자:** 팀원 B (Lee)
- **검토자:** 팀원 C (Park)

### 📌 문제 상황
- 팀원 B가 문자열 소문자 변환 함수(`to_lower`)와 완전히 별개의 작업인 날짜 유틸 문서 수정(`docs/date.md`)을 실수로 하나의 커밋(`feat: update string and docs`)으로 한 번에 묶어서 커밋해버림.
- 커밋 단위를 "단일 책임 원칙"에 맞게 분리하기 위해, 작성한 코드 변경사항은 작업 트리에 그대로 살려둔 채 커밋만 취소하고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
# 1. 변경사항을 Staging Area에 남겨두고 커밋만 직전 상태로 취소
git reset --soft HEAD~1

# 2. 스테이징 상태 확인
git status

# 3. 첫 번째 작업(문자열 기능)만 선택적 스테이징 및 커밋
git reset HEAD docs/date.md
git add src/utils/string_ops.py
git commit -m "feat: add to_lower string utility"

# 4. 두 번째 작업(문서) 스테이징 및 커밋
git add docs/date.md
git commit -m "docs: update date utility documentation"
```

### 🎯 결과 및 왜 이 방법을 선택했는가
- `--hard` 대신 `--soft`를 사용하여 힘들게 작성한 코드가 삭제되는 일 없이 커밋 단위를 성공적으로 둘로 쪼갤 수 있었음.

---

## 시나리오 3: `git revert` (원격에 push된 잘못된 커밋 취소)

### 👥 참여자
- **실행자:** 팀원 C (Park)
- **검토자:** 팀원 A (Kim)

### 📌 문제 상황
- 팀원 C가 날짜 포맷 변환기에 특정 서드파티 라이브러리에 의존하는 코드를 작성하여 `main` 브랜치에 머지/푸시함.
- 이로 인해 CI 빌드에서 `ModuleNotFoundError`가 발생하며 배포가 깨지는 긴급 상황이 발생함.
- 공유 브랜치(`main`)이므로 히스토리를 강제로 되돌리는 `reset`을 쓰면 다른 팀원들의 저장소와 동기화 문제가 발생하므로 안전하게 되돌리는 새로운 커밋을 만들어야 함.

### 🛠️ 시도한 명령 및 절차
```bash
# 1. 취소하고자 하는 커밋 해시 확인
git log --oneline -n 3
# d4e5f6a feat: add experimental timezone parser

# 2. 해당 커밋의 변경사항을 정반대로 취소하는 신규 커밋 생성
git revert d4e5f6a --no-edit

# 3. 원격 main으로 안전하게 푸시
git push origin main
```

### 🎯 결과 및 왜 이 방법을 선택했는가
- 원격 저장소의 히스토리를 지우거나 강제 푸시(`--force`)하지 않고, "되돌렸다"는 명확한 이력(`Revert "feat: add experimental timezone parser"`)을 남기며 빌드 정상화를 달성함. 협업 환경에서는 `reset` 대신 `revert`가 원칙임을 확인함.

---

## 시나리오 4: `git stash` & `git stash pop` (작업 임시 보관 및 전환)

### 👥 참여자
- **실행자:** 팀원 A (Kim) & 팀원 C (Park)

### 📌 문제 상황
- 팀원 A가 `feature/kim-math-utils` 브랜치에서 복잡한 통계 계산 함수를 반쯤 작성하던 중(커밋하기에는 완성도가 부족한 미완성 상태), 팀원 C로부터 `main` 브랜치에 긴급 확인이 필요한 버그가 있다는 요청을 받음.
- 미완성 코드를 임시 커밋으로 지저분하게 남기지 않고 작업 트리를 깨끗하게 보관한 뒤 브랜치를 전환하고자 함.

### 🛠️ 시도한 명령 및 절차
```bash
# 1. 현재 작업 중인 변경사항을 Stash 스택에 안전하게 보관
git stash save "WIP: working on statistics calculation"

# 2. 작업 트리가 깨끗해진 것을 확인 후 main 브랜치로 전환하여 버그 확인
git status
git checkout main
# (main 브랜치에서 이슈 확인 및 피드백 전달 완료)

# 3. 다시 작업 중이던 기능 브랜치로 복귀
git checkout feature/kim-math-utils

# 4. 보관해두었던 작업 내용 복원 및 스택에서 제거
git stash pop

# 5. 기존 작업 이어 진행
git status
```

### 🎯 결과 및 이점
- 브랜치를 오가면서도 쓰레기 커밋(temp commit)을 남기지 않고 유연하게 컨텍스트 스위칭을 수행할 수 있음을 입증함.
