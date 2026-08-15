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
`형식: <type>/<member_name>-<feature-name>`
- `feature/kim-math-utils`
- `feature/lee-string-utils`
- `feature/park-date-utils`
- `refactor/kim-package-structure`
- `feature/lee-advanced-strings`
- `feature/park-test-suite`

---

## 3. 커밋 메시지 컨벤션
`type: subject` (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`)
