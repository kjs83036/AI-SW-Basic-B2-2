# 💥 Conflict Resolution Log (충돌 해결 기록)

우리 팀이 프로젝트 협업 과정에서 마주친 충돌 상황과 이를 해결한 절차 및 학습 내용을 기록합니다.

---

## 충돌 기록 #1: `src/utils/__init__.py` 동시 수정 (Hunk 충돌)

### 👥 참여자
- **작성자 (해결 담당):** 팀원 B (Lee)
- **상대 작업자:** 팀원 A (Kim)

### 📌 상황 (What happened)
- 팀원 A가 PR #1에서 `math_ops` 모듈을 추가하며 `src/utils/__init__.py`의 `__all__` 리스트와 import 문을 `main`에 먼저 병합함.
- 팀원 B가 PR #2에서 `string_ops` 모듈을 추가하며 동일한 `src/utils/__init__.py`의 같은 라인 범위를 수정함.
- 팀원 B가 `main` 브랜치를 자신의 브랜치에 merge하는 과정에서 동일 라인 수정으로 인한 Git Hunk 충돌이 발생함.

### 🔍 충돌 내용 (Conflict markers)
```python
<<<<<<< HEAD
from src.utils.string_ops import capitalize_words, reverse_string, strip_all_whitespace

__all__ = ["capitalize_words", "reverse_string", "strip_all_whitespace"]
=======
from src.utils.math_ops import add, divide, multiply, subtract

__all__ = ["add", "subtract", "multiply", "divide"]
>>>>>>> origin/main
```

### 🛠️ 해결 과정 (How)
1. **해결 전략 (Keep Both):** 두 팀원의 변경 사항이 서로 배타적인 것이 아니라 각자의 유틸리티 함수를 export해야 하는 상황이므로 두 import 및 `__all__` 항목을 모두 보존하고 알파벳 순으로 정렬하기로 합의함.
2. **실행 절차:**
   ```bash
   git checkout feature/lee-string-utils
   git merge origin/main
   # CONFLICT (content): Merge conflict in src/utils/__init__.py
   # 편집기로 충돌 마커 제거 후 두 모듈 모두 임포트하도록 병합
   git add src/utils/__init__.py
   git commit -m "fix: resolve import export conflict in __init__.py"
   git push origin feature/lee-string-utils
   ```

### 🎯 결과 (Outcome)
- `src/utils/__init__.py`에 `math_ops`와 `string_ops`의 모든 함수가 정상 export되어 PR #2가 성공적으로 병합됨.
- 관련 PR: PR #2 (`feature/lee-string-utils`)

### 💡 배운 점 (Learnings)
- 공통 진입점(`__init__.py`)이나 설정 파일은 여러 팀원이 동시에 건드리기 쉬우므로, 신규 기능 추가 시 import 순서나 정렬 규칙(isort 등)을 사전에 정의해두면 충돌을 최소화할 수 있음을 체득함.

---

## 충돌 기록 #2: 파일 리팩토링(이동/이름변경) vs 기능 추가 (비자명 충돌 - Rename vs Modify)

### 👥 참여자
- **작성자 (해결 담당):** 팀원 B (Lee)
- **상대 작업자:** 팀원 A (Kim)

### 📌 상황 (What happened)
- 팀원 A가 PR #4에서 패키지 구조를 정리하면서 `src/string_utils.py` 파일을 `src/utils/string_ops.py`로 디렉토리 이동 및 이름 변경(Rename/Refactor)하여 `main`에 병합함.
- 동시에 팀원 B는 로컬에서 최신 `main`을 pull받지 않은 채 기존 경로인 `src/string_utils.py`에 새로운 고급 파싱 함수(`slugify`, `truncate_words`)를 추가하고 커밋함.
- 팀원 B가 `main`과 병합을 시도할 때 한쪽은 파일 삭제/이동, 다른 쪽은 기존 파일 수정을 수행하여 Git에서 파일 추적 충돌(Modify/Delete or Rename Conflict)이 발생함.

### 🔍 충돌 내용 (Conflict markers / Status)
```bash
$ git merge origin/main
CONFLICT (modify/delete): src/string_utils.py deleted in origin/main and modified in HEAD. Version HEAD of src/string_utils.py left in tree.
Auto-merging src/utils/string_ops.py
```

### 🛠️ 해결 과정 (How)
1. **해결 전략 (Migrate to Renamed Path):** 팀원 A의 리팩토링 방향(새 디렉토리 구조 `src/utils/string_ops.py`)이 올바른 방향임을 확인하고, 팀원 B가 기존 `src/string_utils.py`에 추가했던 신규 함수(`slugify`, `truncate_words`)를 새로운 파일 `src/utils/string_ops.py`로 이관하기로 합의.
2. **실행 절차:**
   ```bash
   # 1. 새 파일 경로에 팀원 B의 신규 함수 로직 병합
   # 2. 구버전 레거시 파일 삭제
   git rm src/string_utils.py
   # 3. 새 파일 스테이징
   git add src/utils/string_ops.py
   # 4. 테스트 실행으로 정상 동작 확인
   pytest tests/
   # 5. 충돌 해결 커밋 및 푸시
   git commit -m "refactor: migrate advanced string functions to new utils path"
   git push origin feature/lee-advanced-strings
   ```

### 🎯 결과 (Outcome)
- 레거시 파일 경로 충돌을 완전히 제거하고, 신규 함수들이 정상적으로 `src/utils/string_ops.py` 및 테스트 스위트에 통합됨.
- 관련 PR: PR #5 (`feature/lee-advanced-strings`)

### 💡 배운 점 (Learnings)
- 대규모 리팩토링이나 디렉토리 이동 작업은 브랜치를 오래 유지하지 않고 팀원들과 사전 공유 후 최우선으로 병합해야 팀원들의 불필요한 비자명 충돌 비용을 아낄 수 있음을 깊이 깨달음.
