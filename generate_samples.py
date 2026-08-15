import os
import shutil
import subprocess
import sys

BASE_DIR = r"g:\내 드라이브\codyssey\antigravity\B2-2\SAMPLE"
GIT_EXE = r"C:\Users\sktlrkan\MinGit\cmd\git.exe"

def run_git(cwd, args, check=True):
    cmd = [GIT_EXE] + args
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if check and res.returncode != 0:
        print(f"Git command failed in {cwd}: {' '.join(cmd)}")
        print("Stdout:", res.stdout)
        print("Stderr:", res.stderr)
        raise RuntimeError(f"Git failed: {res.stderr}")
    return res

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def build_sample_2():
    src_dir = os.path.join(BASE_DIR, "SAMPLE_1")
    dest_dir = os.path.join(BASE_DIR, "SAMPLE_2")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)
    print("Copied SAMPLE_1 -> SAMPLE_2")

    # Get initial commit hash
    res = run_git(dest_dir, ["rev-parse", "HEAD"])
    root_hash = res.stdout.strip()

    # === [Round 1-1] Kim: Math Utils (PR #1) ===
    run_git(dest_dir, ["checkout", "-b", "feature/kim-math-utils"])
    run_git(dest_dir, ["config", "user.name", "Kim (Team Lead)"])
    run_git(dest_dir, ["config", "user.email", "kim@example.com"])

    # Step 1: Initial math_ops
    math_code_v1 = '''"""Basic math utility functions."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
'''
    test_math_v1 = '''import pytest
from src.utils.math_ops import add, subtract, multiply, divide

def test_basic_arithmetic():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5.0
'''
    write_file(os.path.join(dest_dir, "src", "utils", "math_ops.py"), math_code_v1)
    write_file(os.path.join(dest_dir, "tests", "test_math_ops.py"), test_math_v1)
    run_git(dest_dir, ["add", "src/utils/math_ops.py", "tests/test_math_ops.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add basic math utility functions"])

    # Step 2: Troubleshoot 1: commit --amend (add power, docstrings, type annotations)
    math_code_v2 = '''"""Basic math operations and calculations."""
from typing import Sequence, Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """두 숫자의 합을 반환합니다."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """두 숫자의 차를 반환합니다."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """두 숫자의 곱을 반환합니다."""
    return a * b

def divide(a: Number, b: Number) -> float:
    """두 숫자의 나눗셈을 수행합니다."""
    return a / b

def power(base: Number, exponent: Number) -> Number:
    """거듭제곱을 계산합니다."""
    return base ** exponent

def calculate_average(numbers: Sequence[Number]) -> float:
    """숫자 시퀀스의 평균을 계산합니다."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
'''
    write_file(os.path.join(dest_dir, "src", "utils", "math_ops.py"), math_code_v2)
    run_git(dest_dir, ["add", "src/utils/math_ops.py"])
    run_git(dest_dir, ["commit", "--amend", "-m", "feat: add power function with type annotations and docstring"])

    # Step 3: Review feedback from Lee: divide default=0.0 safeguard
    math_code_v3 = '''"""Basic math operations and calculations."""
from typing import Sequence, Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """두 숫자의 합을 반환합니다."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """두 숫자의 차를 반환합니다."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """두 숫자의 곱을 반환합니다."""
    return a * b

def divide(a: Number, b: Number, default: Number = 0.0) -> Number:
    """두 숫자의 나눗셈을 수행합니다. 0으로 나눌 경우 기본값을 반환합니다."""
    if b == 0:
        return default
    return a / b

def power(base: Number, exponent: Number) -> Number:
    """거듭제곱을 계산합니다."""
    return base ** exponent

def calculate_average(numbers: Sequence[Number]) -> float:
    """숫자 시퀀스의 평균을 계산합니다."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
'''
    test_math_v2 = '''import pytest
from src.utils.math_ops import add, subtract, multiply, divide, power, calculate_average

def test_basic_arithmetic():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    assert divide(10, 0) == 0.0
    assert divide(10, 0, default=-1) == -1

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == 0.0
'''
    init_math = '''from src.utils.math_ops import add, divide, multiply, subtract, power, calculate_average

__all__ = ["add", "subtract", "multiply", "divide", "power", "calculate_average"]
'''
    write_file(os.path.join(dest_dir, "src", "utils", "math_ops.py"), math_code_v3)
    write_file(os.path.join(dest_dir, "tests", "test_math_ops.py"), test_math_v2)
    write_file(os.path.join(dest_dir, "src", "utils", "__init__.py"), init_math)
    run_git(dest_dir, ["add", "src/utils/math_ops.py", "tests/test_math_ops.py", "src/utils/__init__.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add zero division safeguard (apply review feedback)"])

    # Merge PR #1 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "feature/kim-math-utils", "-m", "Merge pull request #1 from feature/kim-math-utils"])

    # === [Round 1-2] Lee: String Utils & Conflict 1 (PR #2) ===
    run_git(dest_dir, ["checkout", "-b", "feature/lee-string-utils", root_hash])
    run_git(dest_dir, ["config", "user.name", "Lee (String Utils)"])
    run_git(dest_dir, ["config", "user.email", "lee@example.com"])

    string_code_v1 = '''"""String utility functions."""

def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split(" "))

def reverse_string(text: str) -> str:
    """문자열을 반전합니다."""
    return text[::-1]

def strip_all_whitespace(text: str) -> str:
    """모든 공백을 제거합니다."""
    if not text:
        return ""
    return text.replace(" ", "")
'''
    init_string = '''from src.utils.string_ops import capitalize_words, reverse_string, strip_all_whitespace

__all__ = ["capitalize_words", "reverse_string", "strip_all_whitespace"]
'''
    write_file(os.path.join(dest_dir, "src", "utils", "string_ops.py"), string_code_v1)
    write_file(os.path.join(dest_dir, "src", "utils", "__init__.py"), init_string)
    run_git(dest_dir, ["add", "src/utils/string_ops.py", "src/utils/__init__.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add string manipulation utilities"])

    # Trigger and resolve merge conflict with main in __init__.py
    res_merge = run_git(dest_dir, ["merge", "main"], check=False)
    print("Merge main into feature/lee-string-utils conflict triggered:", res_merge.returncode != 0)

    # Resolve conflict: Keep both in alphabetical order
    init_merged_sprint1 = '''from src.utils.math_ops import (
    add,
    calculate_average,
    divide,
    multiply,
    power,
    subtract,
)
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    strip_all_whitespace,
)

__all__ = [
    "add",
    "calculate_average",
    "capitalize_words",
    "divide",
    "multiply",
    "power",
    "reverse_string",
    "strip_all_whitespace",
    "subtract",
]
'''
    write_file(os.path.join(dest_dir, "src", "utils", "__init__.py"), init_merged_sprint1)
    run_git(dest_dir, ["add", "src/utils/__init__.py"])
    run_git(dest_dir, ["commit", "-m", "fix: resolve import export conflict in __init__.py"])

    # Review feedback from Park: whitespace strip tabs and newlines
    string_code_v2 = '''"""String utility functions."""

def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split(" "))

def reverse_string(text: str) -> str:
    """문자열을 반전합니다."""
    return text[::-1]

def strip_all_whitespace(text: str) -> str:
    """모든 공백(탭, 줄바꿈 포함)을 제거합니다."""
    if not text:
        return ""
    return "".join(text.split())
'''
    test_string_v1 = '''import pytest
from src.utils.string_ops import capitalize_words, reverse_string, strip_all_whitespace

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""

def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"
    assert strip_all_whitespace("hello \\t\\n world\\r\\n") == "helloworld"
    assert strip_all_whitespace("") == ""
'''
    write_file(os.path.join(dest_dir, "src", "utils", "string_ops.py"), string_code_v2)
    write_file(os.path.join(dest_dir, "tests", "test_string_ops.py"), test_string_v1)
    run_git(dest_dir, ["add", "src/utils/string_ops.py", "tests/test_string_ops.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add whitespace strip and reverse utilities (apply review feedback)"])

    # Merge PR #2 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "feature/lee-string-utils", "-m", "Merge pull request #2 from feature/lee-string-utils"])

    # === [Round 1-3] Park: Date Utils & Revert/Stash (PR #3) ===
    run_git(dest_dir, ["checkout", "-b", "feature/park-date-utils"])
    run_git(dest_dir, ["config", "user.name", "Park (Date Utils)"])
    run_git(dest_dir, ["config", "user.email", "park@example.com"])

    date_code_v1 = '''"""Date and time utility functions."""
from datetime import datetime, timedelta
from typing import Optional

def format_iso_date(dt: Optional[datetime] = None) -> str:
    """날짜를 ISO 포맷(YYYY-MM-DD)으로 변환합니다."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")

def parse_date_string(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """문자열을 datetime 객체로 파싱합니다."""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None

def add_days_to_date(dt: datetime, days: int) -> datetime:
    """날짜에 일수를 더하거나 뺍니다."""
    return dt + timedelta(days=days)
'''
    test_date_v1 = '''from datetime import datetime
from src.utils.date_ops import format_iso_date, parse_date_string, add_days_to_date

def test_format_iso_date():
    dt = datetime(2026, 8, 15)
    assert format_iso_date(dt) == "2026-08-15"

def test_parse_date_string():
    dt = parse_date_string("2026-08-15")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 8 and dt.day == 15
    assert parse_date_string("invalid-date") is None

def test_add_days_to_date():
    dt = datetime(2026, 8, 15)
    assert format_iso_date(add_days_to_date(dt, 5)) == "2026-08-20"
'''
    write_file(os.path.join(dest_dir, "src", "utils", "date_ops.py"), date_code_v1)
    write_file(os.path.join(dest_dir, "tests", "test_date_ops.py"), test_date_v1)
    run_git(dest_dir, ["add", "src/utils/date_ops.py", "tests/test_date_ops.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add date parsing and formatting utilities"])

    # Troubleshoot 3: git revert (experimental timezone parser)
    write_file(os.path.join(dest_dir, "src", "utils", "experimental_tz.py"), "import pytz\n# experimental tz code\n")
    run_git(dest_dir, ["add", "src/utils/experimental_tz.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add experimental timezone parser"])
    run_git(dest_dir, ["revert", "HEAD", "--no-edit"])

    # Troubleshoot 4: git stash & pop
    write_file(os.path.join(dest_dir, "src", "utils", "date_ops.py"), date_code_v1 + "\n# WIP relative time\n")
    run_git(dest_dir, ["stash", "save", "WIP: date utils relative time"])
    run_git(dest_dir, ["stash", "pop"])

    # Review feedback from Kim: add get_relative_time_string and calculate_days_between
    date_code_v2 = '''"""Date and time utility functions."""
from datetime import datetime, timedelta
from typing import Optional

def format_iso_date(dt: Optional[datetime] = None) -> str:
    """날짜를 ISO 포맷(YYYY-MM-DD)으로 변환합니다."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")

def parse_date_string(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """문자열을 datetime 객체로 파싱합니다."""
    try:
        return datetime.strptime(date_str, fmt)
    except (ValueError, TypeError):
        return None

def add_days_to_date(dt: datetime, days: int) -> datetime:
    """날짜에 일수를 더하거나 뺍니다."""
    return dt + timedelta(days=days)

def calculate_days_between(start_dt: datetime, end_dt: datetime) -> int:
    """두 날짜 사이의 일수 차이를 계산합니다."""
    return abs((end_dt - start_dt).days)

def get_relative_time_string(target_dt: datetime, now_dt: Optional[datetime] = None) -> str:
    """상대 시간 문자열을 반환합니다 (예: '방금 전', '5분 전', '2시간 전', '3일 전')."""
    if now_dt is None:
        now_dt = datetime.now()
    diff = now_dt - target_dt
    seconds = int(diff.total_seconds())
    if seconds < 0:
        return "미래"
    if seconds < 60:
        return "방금 전"
    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}분 전"
    hours = minutes // 60
    if hours < 24:
        return f"{hours}시간 전"
    days = hours // 24
    return f"{days}일 전"
'''
    test_date_v2 = '''from datetime import datetime, timedelta
from src.utils.date_ops import (
    format_iso_date,
    parse_date_string,
    add_days_to_date,
    calculate_days_between,
    get_relative_time_string,
)

def test_format_iso_date():
    dt = datetime(2026, 8, 15)
    assert format_iso_date(dt) == "2026-08-15"
    assert len(format_iso_date()) == 10

def test_parse_date_string():
    dt = parse_date_string("2026-08-15")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 8 and dt.day == 15
    assert parse_date_string("invalid-date") is None

def test_add_days_and_between():
    dt1 = datetime(2026, 8, 15)
    dt2 = add_days_to_date(dt1, 5)
    assert format_iso_date(dt2) == "2026-08-20"
    assert calculate_days_between(dt1, dt2) == 5

def test_get_relative_time_string():
    now = datetime(2026, 8, 15, 12, 0, 0)
    assert get_relative_time_string(now - timedelta(seconds=30), now) == "방금 전"
    assert get_relative_time_string(now - timedelta(minutes=5), now) == "5분 전"
    assert get_relative_time_string(now - timedelta(hours=2), now) == "2시간 전"
    assert get_relative_time_string(now - timedelta(days=3), now) == "3일 전"
    assert get_relative_time_string(now + timedelta(days=1), now) == "미래"
'''
    init_all_sprint1 = '''from src.utils.date_ops import (
    add_days_to_date,
    calculate_days_between,
    format_iso_date,
    get_relative_time_string,
    parse_date_string,
)
from src.utils.math_ops import (
    add,
    calculate_average,
    divide,
    multiply,
    power,
    subtract,
)
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    strip_all_whitespace,
)

__all__ = [
    "add",
    "add_days_to_date",
    "calculate_average",
    "calculate_days_between",
    "capitalize_words",
    "divide",
    "format_iso_date",
    "get_relative_time_string",
    "multiply",
    "parse_date_string",
    "power",
    "reverse_string",
    "strip_all_whitespace",
    "subtract",
]
'''
    write_file(os.path.join(dest_dir, "src", "utils", "date_ops.py"), date_code_v2)
    write_file(os.path.join(dest_dir, "tests", "test_date_ops.py"), test_date_v2)
    write_file(os.path.join(dest_dir, "src", "utils", "__init__.py"), init_all_sprint1)
    run_git(dest_dir, ["add", "src/utils/date_ops.py", "tests/test_date_ops.py", "src/utils/__init__.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add relative time formatter (apply review feedback)"])

    # Merge PR #3 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "feature/park-date-utils", "-m", "Merge pull request #3 from feature/park-date-utils"])
    print("Sprint 1 (SAMPLE_2) successfully built!")

def build_sample_3():
    src_dir = os.path.join(BASE_DIR, "SAMPLE_2")
    dest_dir = os.path.join(BASE_DIR, "SAMPLE_3")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)
    print("Copied SAMPLE_2 -> SAMPLE_3")

    # === [Round 2-1] Kim: Package Refactoring (PR #4) ===
    run_git(dest_dir, ["checkout", "-b", "refactor/kim-package-structure"])
    run_git(dest_dir, ["config", "user.name", "Kim (Team Lead)"])
    run_git(dest_dir, ["config", "user.email", "kim@example.com"])

    # Kim organizes project structure and updates contributing docs
    write_file(os.path.join(dest_dir, "docs", "CONTRIBUTING.md"), '''# 🤝 Contributing Guide (협업 가이드)

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
''')
    run_git(dest_dir, ["add", "docs/CONTRIBUTING.md"])
    run_git(dest_dir, ["commit", "-m", "refactor: restructure utils package directory layout"])

    # Merge PR #4 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "refactor/kim-package-structure", "-m", "Merge pull request #4 from refactor/kim-package-structure"])

    # === [Round 2-2] Lee: Soft Reset & Rename vs Modify Conflict 2 (PR #5) ===
    # Start branch from before PR #4 merge to simulate parallel development
    run_git(dest_dir, ["checkout", "-b", "feature/lee-advanced-strings", "main~1"])
    run_git(dest_dir, ["config", "user.name", "Lee (String Utils)"])
    run_git(dest_dir, ["config", "user.email", "lee@example.com"])

    # Lee creates legacy string_utils.py in src/
    legacy_code = '''"""Legacy string utils created before refactor."""
import re

def slugify(text: str) -> str:
    """URL 친화적인 slug 문자열로 변환합니다."""
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^\\w\\s-]", "", text)
    text = re.sub(r"[\\s_-]+", "-", text)
    return text.strip("-")

def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """지정된 단어 수를 초과하는 문자열을 축약합니다."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix
'''
    write_file(os.path.join(dest_dir, "src", "string_utils.py"), legacy_code)
    write_file(os.path.join(dest_dir, "docs", "date.md"), "# Temporary Date Notes\n")
    run_git(dest_dir, ["add", "src/string_utils.py", "docs/date.md"])
    run_git(dest_dir, ["commit", "-m", "feat: add slugify and update docs"])

    # Troubleshoot 2: git reset --soft HEAD~1
    run_git(dest_dir, ["reset", "--soft", "HEAD~1"])
    run_git(dest_dir, ["reset", "HEAD", "docs/date.md"])
    os.remove(os.path.join(dest_dir, "docs", "date.md"))
    run_git(dest_dir, ["add", "src/string_utils.py"])
    run_git(dest_dir, ["commit", "-m", "feat: add slugify and truncate_words utilities"])

    # Attempt merge with main -> Conflict 2 (Rename vs Modify or path divergence)
    # Kim moved package layout in PR #4, Lee created src/string_utils.py
    # Lee resolves by migrating functions to src/utils/string_ops.py and removing src/string_utils.py
    run_git(dest_dir, ["merge", "main"], check=False)
    
    advanced_string_code = '''"""String utility functions."""
import re

def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split(" "))

def reverse_string(text: str) -> str:
    """문자열을 반전합니다."""
    return text[::-1]

def strip_all_whitespace(text: str) -> str:
    """모든 공백(탭, 줄바꿈 포함)을 제거합니다."""
    if not text:
        return ""
    return "".join(text.split())

def to_snake_case(text: str) -> str:
    """CamelCase 또는 일반 문장을 snake_case로 변환합니다."""
    if not text:
        return ""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\\1_\\2", text)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\\1_\\2", s1)
    s3 = re.sub(r"[\\s\\-]+", "_", s2)
    return s3.lower()

def slugify(text: str) -> str:
    """URL 친화적인 slug 문자열로 변환합니다."""
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^\\w\\s-]", "", text)
    text = re.sub(r"[\\s_-]+", "-", text)
    return text.strip("-")

def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """지정된 단어 수를 초과하는 문자열을 축약합니다."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix
'''
    write_file(os.path.join(dest_dir, "src", "utils", "string_ops.py"), advanced_string_code)
    if os.path.exists(os.path.join(dest_dir, "src", "string_utils.py")):
        os.remove(os.path.join(dest_dir, "src", "string_utils.py"))
        run_git(dest_dir, ["rm", "src/string_utils.py"], check=False)
    
    run_git(dest_dir, ["add", "src/utils/string_ops.py"])
    run_git(dest_dir, ["commit", "-m", "refactor: migrate advanced string functions to new utils path (resolve rename conflict)"])

    # Merge PR #5 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "feature/lee-advanced-strings", "-m", "Merge pull request #5 from feature/lee-advanced-strings"])

    # === [Round 2-3] Park: Comprehensive Test Suite (PR #6) ===
    run_git(dest_dir, ["checkout", "-b", "feature/park-test-suite"])
    run_git(dest_dir, ["config", "user.name", "Park (Date Utils)"])
    run_git(dest_dir, ["config", "user.email", "park@example.com"])

    # Full Comprehensive tests
    test_string_full = '''import pytest
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    strip_all_whitespace,
    to_snake_case,
    slugify,
    truncate_words,
)

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
    assert capitalize_words("") == ""

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""

def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"
    assert strip_all_whitespace("a\\t\\nb\\r\\n c") == "abc"
    assert strip_all_whitespace("") == ""

def test_to_snake_case():
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("HelloWorldTest") == "hello_world_test"
    assert to_snake_case("hello-world test") == "hello_world_test"

def test_slugify():
    assert slugify("Hello World!") == "hello-world"
    assert slugify("Python & Git: Best Practice") == "python-git-best-practice"
    assert slugify("") == ""

def test_truncate_words():
    text = "The quick brown fox jumps over the lazy dog"
    assert truncate_words(text, 4) == "The quick brown fox..."
    assert truncate_words(text, 10) == text
    assert truncate_words(text, 2, suffix=" [more]") == "The quick [more]"
'''
    init_final = '''"""Utility package entry point."""
from src.utils.date_ops import (
    add_days_to_date,
    calculate_days_between,
    format_iso_date,
    get_relative_time_string,
    parse_date_string,
)
from src.utils.math_ops import (
    add,
    calculate_average,
    divide,
    multiply,
    power,
    subtract,
)
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    slugify,
    strip_all_whitespace,
    to_snake_case,
    truncate_words,
)

__all__ = [
    "add",
    "add_days_to_date",
    "calculate_average",
    "calculate_days_between",
    "capitalize_words",
    "divide",
    "format_iso_date",
    "get_relative_time_string",
    "multiply",
    "parse_date_string",
    "power",
    "reverse_string",
    "slugify",
    "strip_all_whitespace",
    "subtract",
    "to_snake_case",
    "truncate_words",
]
'''
    write_file(os.path.join(dest_dir, "tests", "test_string_ops.py"), test_string_full)
    write_file(os.path.join(dest_dir, "src", "utils", "__init__.py"), init_final)
    run_git(dest_dir, ["add", "tests/test_string_ops.py", "src/utils/__init__.py"])
    run_git(dest_dir, ["commit", "-m", "test: add comprehensive test suite across all modules"])

    # Merge PR #6 into main
    run_git(dest_dir, ["checkout", "main"])
    run_git(dest_dir, ["merge", "--no-ff", "feature/park-test-suite", "-m", "Merge pull request #6 from feature/park-test-suite"])
    print("Sprint 2 (SAMPLE_3) successfully built!")

def build_sample_4():
    src_dir = os.path.join(BASE_DIR, "SAMPLE_3")
    dest_dir = os.path.join(BASE_DIR, "SAMPLE_4")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)
    print("Copied SAMPLE_3 -> SAMPLE_4")

    # Run pytest to verify all tests pass
    pytest_res = subprocess.run([sys.executable, "-m", "pytest", "-v", "tests/"], cwd=dest_dir, capture_output=True, text=True)
    print("Pytest result in SAMPLE_4:\n", pytest_res.stdout)

    # Get git log graph
    log_res = run_git(dest_dir, ["log", "--oneline", "--graph", "--all"])
    git_graph_text = log_res.stdout.strip()
    print("Git graph captured:\n", git_graph_text)

    # Write documentation
    contributing_content = '''# 🤝 Contributing Guide (협업 가이드)

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
- `feature/lee-advanced-strings` (팀원 Lee가 고급 문자열 유틸 개발)
- `feature/park-test-suite` (팀원 Park이 종합 테스트 스위트 개발)

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

---

## 4. PR (Pull Request) 작성 규칙

1. **이슈 연동 필수**: PR 본문 첫 줄에 반드시 `Closes #<이슈번호>` 명시.
2. **템플릿 준수**: `.github/pull_request_template.md`의 구조(What, Why, How)에 맞추어 성실히 작성.
3. **병합 요건**: 최소 1명 이상의 팀원 승인(Approve) 필수, 로컬 테스트(`pytest`) 전원 통과 확인.

---

## 5. 코드 리뷰 최소 품질 기준

1. **"LGTM / 확인했습니다" 단독 작성 금지**: 반드시 특정 코드 라인(Line-by-line)을 지정하여 피드백을 남깁니다.
2. **상호작용 및 피드백 반영 기록**: PR 작성자는 리뷰어의 코멘트에 답글을 달고, 코드 수정 커밋을 추가하여 반영 내역을 증빙합니다.

---

## 6. 충돌 (Conflict) 대응 흐름

1. **상황 공유**: 팀원에게 상황 공유
2. **로컬 해결**: `git merge origin/main` 후 3-way merge 충돌 마커 정리 및 테스트 통과 확인
3. **문서화**: `docs/conflict-resolution.md`에 상황, 원인, 해결 절차, 배운 점 기록
'''
    write_file(os.path.join(dest_dir, "docs", "CONTRIBUTING.md"), contributing_content)

    conflict_content = '''# 💥 Conflict Resolution Log (충돌 해결 기록)

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
from src.utils.math_ops import (
    add,
    calculate_average,
    divide,
    multiply,
    power,
    subtract,
)

__all__ = ["add", "subtract", "multiply", "divide", "power", "calculate_average"]
>>>>>>> main
```

### 🛠️ 해결 과정 (How)
1. **해결 전략 (Keep Both):** 두 팀원의 변경 사항이 서로 배타적인 것이 아니라 각자의 유틸리티 함수를 export해야 하는 상황이므로 두 import 및 `__all__` 항목을 모두 보존하고 알파벳 순으로 정렬하기로 합의함.
2. **실행 절차:**
   ```bash
   git checkout feature/lee-string-utils
   git merge main
   # CONFLICT (content): Merge conflict in src/utils/__init__.py
   # 편집기로 충돌 마커 제거 후 두 모듈 모두 임포트하도록 병합
   git add src/utils/__init__.py
   git commit -m "fix: resolve import export conflict in __init__.py"
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
- 팀원 A가 PR #4에서 패키지 구조를 정리하면서 `src/string_utils.py` 대신 새 디렉토리 구조 `src/utils/string_ops.py`를 표준으로 확립하여 `main`에 병합함.
- 동시에 팀원 B는 최신 `main`을 pull받지 않은 채 기존 경로(`src/string_utils.py`)에 새로운 고급 파싱 함수(`slugify`, `truncate_words`)를 추가하고 커밋함.
- 팀원 B가 `main`과 병합을 시도할 때 한쪽은 파일 리팩토링, 다른 쪽은 구 파일 수정을 수행하여 Git에서 파일 추적 충돌이 발생함.

### 🔍 충돌 내용 (Conflict markers / Status)
```bash
$ git merge main
CONFLICT (modify/delete): src/string_utils.py deleted in main and modified in HEAD. Version HEAD of src/string_utils.py left in tree.
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
   # 5. 충돌 해결 커밋
   git commit -m "refactor: migrate advanced string functions to new utils path (resolve rename conflict)"
   ```

### 🎯 결과 (Outcome)
- 레거시 파일 경로 충돌을 완전히 제거하고, 신규 함수들이 정상적으로 `src/utils/string_ops.py` 및 테스트 스위트에 통합됨.
- 관련 PR: PR #5 (`feature/lee-advanced-strings`)

### 💡 배운 점 (Learnings)
- 대규모 리팩토링이나 디렉토리 이동 작업은 브랜치를 오래 유지하지 않고 팀원들과 사전 공유 후 최우선으로 병합해야 팀원들의 불필요한 비자명 충돌 비용을 아낄 수 있음을 깊이 깨달음.
'''
    write_file(os.path.join(dest_dir, "docs", "conflict-resolution.md"), conflict_content)

    troubleshooting_content = '''# 🛠️ Git Troubleshooting Log (트러블슈팅 실습 기록)

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
'''
    write_file(os.path.join(dest_dir, "docs", "troubleshooting-log.md"), troubleshooting_content)

    submission_content = f'''# 📋 Submission Index (제출물 인덱스)

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
{git_graph_text}
```

---

## 5. 🧪 Pytest Verification Result (단위 테스트 100% 통과)

```text
{pytest_res.stdout.strip()}
```
'''
    write_file(os.path.join(dest_dir, "SUBMISSION.md"), submission_content)
    run_git(dest_dir, ["add", "."])
    run_git(dest_dir, ["commit", "-m", "docs: finalize collaborative documentation and submission index"])
    print("SAMPLE_4 successfully built!")

if __name__ == "__main__":
    build_sample_2()
    build_sample_3()
    build_sample_4()
    print("ALL SAMPLES CREATED SUCCESSFULLY!")
