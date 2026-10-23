# HAL DLL 분석

> Windows System32의 hal.dll과 정확히 일치하는 Microsoft PDB를 확인하고, HAL Export가 실제 구현으로 전달되는 경로를 정리했습니다.

## 빠른 열기

- **[인터랙티브 분석 패널](control-panel.html)** — 91개 Export 검색, 전달 그래프, 커널 RVA, 기존 ntoskrnl 함수 분석 연결
- **[분석 요약](HAL-ANALYSIS.md)** — PE/PDB 증거와 분석 범위
- **[전체 JSON 인벤토리](data/hal-analysis.json)** — Export별 전달 대상 및 ntoskrnl RVA
- **[원본 심볼 분석 결과](source-analysis/README.md)** — CSV와 PDB 열거 결과
- **[일치 PDB](symbols/hal.pdb)** — Microsoft Symbol Server에서 받은 hal.pdb

## 확인된 내용

| 항목 | 결과 |
|---|---:|
| 대상 파일 | C:\Windows\System32\hal.dll |
| 파일 버전 | 10.0.26100.1 |
| 일치 PDB | hal.pdb · GUID ff0f78af-4301-9c3e-04c0-84da6e04995f · Age 1 |
| Export | 91개, 모두 ntoskrnl.<이름> 형식의 forwarder |
| 현재 시스템 ntoskrnl.exe와 매칭 | 91 / 91 |
| ntoskrnl 분석 문서 연결 | 89 / 91 |
| Import / 실행 코드 섹션 / 함수 본문 | 0 / 0 / 0 |
| HAL PDB 심볼 | 1개 (실행 함수 심볼 0개) |

**중요:** 이 hal.dll에는 디스어셈블할 실행 함수 본문이 없습니다. Export RVA는 실행 코드 주소가 아니라 PE Export 디렉터리의 forwarder 문자열 위치입니다. 그래서 HAL 함수의 C 복원 결과를 만들어 내지 않고, 실제 코드가 있는 ntoskrnl.exe의 분석으로 연결했습니다.

## 폴더 구성

- functions/ — Export 하나당 전달 경로 Markdown 91개
- source-analysis/ — Export/Import/PDB CSV와 실행 함수 인벤토리
- symbols/hal.pdb — 일치 PDB 복사본
- data/hal-analysis.json — UI와 문서가 사용하는 정규 데이터
- control-panel.html — 검색 가능한 단일 페이지 패널
- tools/build_hal_analysis.py — 생성 스크립트

Microsoft는 Windows 디버깅 심볼을 공개 심볼 서버에서 제공합니다. 이 분석은 PE의 RSDS GUID/Age로 정확한 파일을 요청하고, MSF 7.0 형식과 Windows DbgHelp 로딩 결과를 확인했습니다. [Microsoft symbol server 사용법](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/using-a-symbol-server)
