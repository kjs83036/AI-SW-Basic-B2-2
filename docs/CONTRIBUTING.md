# 🤝 Contributing Guide (협업 가이드)

우리 팀의 일관되고 안전한 Git 협업 및 코드 품질 유지를 위한 가이드라인입니다. 모든 팀원은 아래 규칙을 준수하여 작업합니다.

---

## 1. 브랜치 전략 (GitHub Flow)

우리 팀은 간결하고 빠른 배포 주기와 협업 피드백을 위해 **GitHub Flow**를 적용합니다.

### 💡 GitHub Flow 채택 이유 (3줄 요약)
1. 복잡한 릴리즈/핫픽스 브랜치 분기 없이 `main`과 `feature` 브랜치만으로 직관적이고 가벼운 워크플로우를 유지할 수 있습니다.
2. 모든 작업이 PR(Pull Request)을 거치므로 코드 리뷰와 자동화 테스트를 통한 사전 품질 검증이 확실합니다.
3. `main` 브랜치를 항상 배포 가능한 안정 상태로 유지함으로써 팀 전체의 병합 충돌과 병목을 최소화합니다.

### 브랜치 구성
- `main` : 항상 안정적이고 테스트를 통과한 배포 가능 상태 (직접 push 금지, PR 병합 필수)
- `feature/*` : 새로운 기능 개발 또는 개선 작업 단위 브랜치
- `refactor/*` : 코드 구조 개선 및 파일 재배치 브랜치
- `fix/*` : 버그 수정 브랜치

---

## 2. 브랜치 네이밍 규칙

브랜치 이름은 작업 목적과 작업자를 명확히 식별할 수 있도록 아래 규칙을 따릅니다.

`형식: <type>/<member_name>-<feature-name>`

### 예시:
- `feature/kim-math-utils` (팀원 Kim이 수학 유틸 개발)
- `feature/lee-string-utils` (팀원 Lee가 문자열 유틸 개발)
- `feature/park-date-utils` (팀원 Park이 날짜 유틸 개발)
- `refactor/kim-package-structure` (팀원 Kim이 패키지 구조 리팩토링)
- `fix/lee-strip-edge-case` (팀원 Lee가 공백 제거 엣지케이스 수정)

---

## 3. 커밋 메시지 컨벤션

커밋 메시지는 변경 사항의 의도와 범위를 명확히 전달해야 합니다.

### 기본 형식
`type: subject`

### Type 태그 정의
- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `docs:` 문서 수정 (README, docs 등)
- `refactor:` 코드 리팩토링 (기능 변경 없는 구조 개선)
- `test:` 테스트 코드 추가 또는 수정
- `chore:` 빌드, 패키지 매니저, 기타 설정 변경

### ⚠️ 금지되는 무의미한 커밋 메시지 (엄격 금지)
아래와 같이 변경 대상이나 목적이 모호한 커밋 메시지는 반려 대상입니다:
- `update`, `fix`, `temp`, `wip`, `final`, `asdf`
- `edit file`, `bug fix`, `modify code` (구체적인 대상 및 이유 누락)

---

## 4. PR (Pull Request) 작성 규칙

모든 작업은 PR을 통해 `main` 브랜치로 병합됩니다.

1. **이슈 연동 필수**: PR 본문 첫 줄에 반드시 `Closes #<이슈번호>` 또는 `Fixes #<이슈번호>`를 명시합니다.
2. **템플릿 준수**: `.github/pull_request_template.md`의 구조(What, Why, How)에 맞추어 성실히 작성합니다.
3. **병합 요건**:
   - 최소 1명 이상의 팀원 승인(Approve) 필수
   - 로컬 테스트(`pytest`) 전원 통과 확인
   - 미해결된 Review Conversation이 없을 것

---

## 5. 코드 리뷰 최소 품질 기준

단순한 승인이 아닌, 실질적인 코드 품질 향상을 목표로 리뷰합니다.

1. **"LGTM / 확인했습니다" 단독 작성 금지**:
   - 반드시 특정 코드 라인(Line-by-line)을 지정하여 피드백을 남깁니다.
   - 예외 처리 제안, 함수 네이밍, 타입 힌트, 성능/가독성 개선안, 엣지 케이스 등을 구체적으로 언급합니다.
2. **상호작용 및 피드백 반영 기록**:
   - PR 작성자는 리뷰어의 코멘트에 답글을 달고, 코드 수정 커밋을 추가하여 반영 내역을 증빙합니다.

---

## 6. 충돌 (Conflict) 대응 흐름

병합 중 충돌이 발생할 경우 다음 절차를 따릅니다.

1. **상황 공유**: 슬랙/디스코드/GitHub 코멘트를 통해 충돌 대상 팀원에게 상황을 알립니다.
2. **로컬 해결**:
   ```bash
   git checkout feature/내브랜치
   git fetch origin
   git merge origin/main
   # 충돌 파일 수동 편집 (충돌 마커 정리)
   git add <충돌해결파일>
   git commit -m "fix: resolve merge conflict with main"
   git push origin feature/내브랜치
   ```
3. **기록 남기기**: 충돌 해결 즉시 `docs/conflict-resolution.md`에 충돌 상황, 마커 내용, 해결 전략을 문서화합니다.
