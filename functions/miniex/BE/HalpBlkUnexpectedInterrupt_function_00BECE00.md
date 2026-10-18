# HalpBlkUnexpectedInterrupt

- RVA: `0x00BECE00`–`0x00BED600` (길이 `2,048` bytes)
- VA: `0x0000000140BECE00`
- 실행 섹션: `MINIEX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFD88`
- 디코드: `768`개 명령, `2,048/2,048` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **256**
  - `0x00BECE02` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE0A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE12` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE1A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE22` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE2A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE32` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE3A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE42` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE4A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE52` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE5A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE62` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE6A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE72` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE7A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE82` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE8A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE92` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECE9A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEA2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEAA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEB2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEBA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEC2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECECA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECED2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEDA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEE2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEEA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEF2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECEFA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF02` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF0A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF12` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF1A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF22` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF2A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF32` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF3A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF42` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF4A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF52` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF5A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF62` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF6A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF72` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF7A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF82` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF8A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF92` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECF9A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFA2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFAA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFB2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFBA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFC2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFCA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFD2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFDA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFE2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFEA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFF2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BECFFA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED002` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED00A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED012` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED01A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED022` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED02A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED032` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED03A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED042` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED04A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED052` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED05A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED062` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED06A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED072` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED07A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED082` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED08A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED092` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED09A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED0FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED102` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED10A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED112` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED11A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED122` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED12A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED132` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED13A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED142` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED14A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED152` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED15A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED162` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED16A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED172` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED17A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED182` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED18A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED192` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED19A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED1FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED202` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED20A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED212` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED21A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED222` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED22A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED232` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED23A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED242` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED24A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED252` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED25A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED262` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED26A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED272` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED27A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED282` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED28A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED292` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED29A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED2FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED302` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED30A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED312` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED31A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED322` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED32A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED332` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED33A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED342` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED34A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED352` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED35A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED362` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED36A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED372` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED37A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED382` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED38A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED392` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED39A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED3FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED402` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED40A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED412` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED41A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED422` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED42A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED432` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED43A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED442` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED44A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED452` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED45A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED462` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED46A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED472` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED47A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED482` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED48A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED492` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED49A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED4FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED502` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED50A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED512` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED51A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED522` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED52A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED532` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED53A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED542` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED54A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED552` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED55A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED562` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED56A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED572` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED57A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED582` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED58A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED592` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED59A` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5A2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5AA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5B2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5BA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5C2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5CA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5D2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5DA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5E2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5EA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5F2` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)
  - `0x00BED5FA` → [HalpBlkUnexpectedInterruptCommon](HalpBlkUnexpectedInterruptCommon_function_00BED600.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BECE00  6A 00                           push 0
00BECE02  E9 F9 07 00 00                  jmp 0x140bed600
00BECE07  90                              nop
00BECE08  6A 01                           push 1
00BECE0A  E9 F1 07 00 00                  jmp 0x140bed600
00BECE0F  90                              nop
00BECE10  6A 02                           push 2
00BECE12  E9 E9 07 00 00                  jmp 0x140bed600
00BECE17  90                              nop
00BECE18  6A 03                           push 3
00BECE1A  E9 E1 07 00 00                  jmp 0x140bed600
00BECE1F  90                              nop
00BECE20  6A 04                           push 4
00BECE22  E9 D9 07 00 00                  jmp 0x140bed600
00BECE27  90                              nop
00BECE28  6A 05                           push 5
00BECE2A  E9 D1 07 00 00                  jmp 0x140bed600
00BECE2F  90                              nop
00BECE30  6A 06                           push 6
00BECE32  E9 C9 07 00 00                  jmp 0x140bed600
00BECE37  90                              nop
00BECE38  6A 07                           push 7
00BECE3A  E9 C1 07 00 00                  jmp 0x140bed600
00BECE3F  90                              nop
00BECE40  6A 08                           push 8
00BECE42  E9 B9 07 00 00                  jmp 0x140bed600
00BECE47  90                              nop
00BECE48  6A 09                           push 9
00BECE4A  E9 B1 07 00 00                  jmp 0x140bed600
00BECE4F  90                              nop
00BECE50  6A 0A                           push 0xa
00BECE52  E9 A9 07 00 00                  jmp 0x140bed600
00BECE57  90                              nop
00BECE58  6A 0B                           push 0xb
00BECE5A  E9 A1 07 00 00                  jmp 0x140bed600
00BECE5F  90                              nop
00BECE60  6A 0C                           push 0xc
00BECE62  E9 99 07 00 00                  jmp 0x140bed600
00BECE67  90                              nop
00BECE68  6A 0D                           push 0xd
00BECE6A  E9 91 07 00 00                  jmp 0x140bed600
00BECE6F  90                              nop
00BECE70  6A 0E                           push 0xe
00BECE72  E9 89 07 00 00                  jmp 0x140bed600
00BECE77  90                              nop
00BECE78  6A 0F                           push 0xf
00BECE7A  E9 81 07 00 00                  jmp 0x140bed600
00BECE7F  90                              nop
00BECE80  6A 10                           push 0x10
00BECE82  E9 79 07 00 00                  jmp 0x140bed600
00BECE87  90                              nop
00BECE88  6A 11                           push 0x11
00BECE8A  E9 71 07 00 00                  jmp 0x140bed600
00BECE8F  90                              nop
00BECE90  6A 12                           push 0x12
00BECE92  E9 69 07 00 00                  jmp 0x140bed600
00BECE97  90                              nop
00BECE98  6A 13                           push 0x13
00BECE9A  E9 61 07 00 00                  jmp 0x140bed600
00BECE9F  90                              nop
00BECEA0  6A 14                           push 0x14
00BECEA2  E9 59 07 00 00                  jmp 0x140bed600
00BECEA7  90                              nop
00BECEA8  6A 15                           push 0x15
00BECEAA  E9 51 07 00 00                  jmp 0x140bed600
00BECEAF  90                              nop
00BECEB0  6A 16                           push 0x16
00BECEB2  E9 49 07 00 00                  jmp 0x140bed600
00BECEB7  90                              nop
00BECEB8  6A 17                           push 0x17
00BECEBA  E9 41 07 00 00                  jmp 0x140bed600
00BECEBF  90                              nop
00BECEC0  6A 18                           push 0x18
00BECEC2  E9 39 07 00 00                  jmp 0x140bed600
00BECEC7  90                              nop
00BECEC8  6A 19                           push 0x19
00BECECA  E9 31 07 00 00                  jmp 0x140bed600
00BECECF  90                              nop
00BECED0  6A 1A                           push 0x1a
00BECED2  E9 29 07 00 00                  jmp 0x140bed600
00BECED7  90                              nop
00BECED8  6A 1B                           push 0x1b
00BECEDA  E9 21 07 00 00                  jmp 0x140bed600
00BECEDF  90                              nop
00BECEE0  6A 1C                           push 0x1c
00BECEE2  E9 19 07 00 00                  jmp 0x140bed600
00BECEE7  90                              nop
00BECEE8  6A 1D                           push 0x1d
00BECEEA  E9 11 07 00 00                  jmp 0x140bed600
00BECEEF  90                              nop
00BECEF0  6A 1E                           push 0x1e
00BECEF2  E9 09 07 00 00                  jmp 0x140bed600
00BECEF7  90                              nop
00BECEF8  6A 1F                           push 0x1f
00BECEFA  E9 01 07 00 00                  jmp 0x140bed600
00BECEFF  90                              nop
00BECF00  6A 20                           push 0x20
00BECF02  E9 F9 06 00 00                  jmp 0x140bed600
00BECF07  90                              nop
00BECF08  6A 21                           push 0x21
00BECF0A  E9 F1 06 00 00                  jmp 0x140bed600
00BECF0F  90                              nop
00BECF10  6A 22                           push 0x22
00BECF12  E9 E9 06 00 00                  jmp 0x140bed600
00BECF17  90                              nop
00BECF18  6A 23                           push 0x23
00BECF1A  E9 E1 06 00 00                  jmp 0x140bed600
00BECF1F  90                              nop
00BECF20  6A 24                           push 0x24
00BECF22  E9 D9 06 00 00                  jmp 0x140bed600
00BECF27  90                              nop
00BECF28  6A 25                           push 0x25
00BECF2A  E9 D1 06 00 00                  jmp 0x140bed600
00BECF2F  90                              nop
00BECF30  6A 26                           push 0x26
00BECF32  E9 C9 06 00 00                  jmp 0x140bed600
00BECF37  90                              nop
00BECF38  6A 27                           push 0x27
00BECF3A  E9 C1 06 00 00                  jmp 0x140bed600
00BECF3F  90                              nop
00BECF40  6A 28                           push 0x28
00BECF42  E9 B9 06 00 00                  jmp 0x140bed600
00BECF47  90                              nop
00BECF48  6A 29                           push 0x29
00BECF4A  E9 B1 06 00 00                  jmp 0x140bed600
00BECF4F  90                              nop
00BECF50  6A 2A                           push 0x2a
00BECF52  E9 A9 06 00 00                  jmp 0x140bed600
00BECF57  90                              nop
00BECF58  6A 2B                           push 0x2b
00BECF5A  E9 A1 06 00 00                  jmp 0x140bed600
00BECF5F  90                              nop
00BECF60  6A 2C                           push 0x2c
00BECF62  E9 99 06 00 00                  jmp 0x140bed600
00BECF67  90                              nop
00BECF68  6A 2D                           push 0x2d
00BECF6A  E9 91 06 00 00                  jmp 0x140bed600
00BECF6F  90                              nop
00BECF70  6A 2E                           push 0x2e
00BECF72  E9 89 06 00 00                  jmp 0x140bed600
00BECF77  90                              nop
00BECF78  6A 2F                           push 0x2f
00BECF7A  E9 81 06 00 00                  jmp 0x140bed600
00BECF7F  90                              nop
00BECF80  6A 30                           push 0x30
00BECF82  E9 79 06 00 00                  jmp 0x140bed600
00BECF87  90                              nop
00BECF88  6A 31                           push 0x31
00BECF8A  E9 71 06 00 00                  jmp 0x140bed600
00BECF8F  90                              nop
00BECF90  6A 32                           push 0x32
00BECF92  E9 69 06 00 00                  jmp 0x140bed600
00BECF97  90                              nop
00BECF98  6A 33                           push 0x33
00BECF9A  E9 61 06 00 00                  jmp 0x140bed600
00BECF9F  90                              nop
00BECFA0  6A 34                           push 0x34
00BECFA2  E9 59 06 00 00                  jmp 0x140bed600
00BECFA7  90                              nop
00BECFA8  6A 35                           push 0x35
00BECFAA  E9 51 06 00 00                  jmp 0x140bed600
00BECFAF  90                              nop
00BECFB0  6A 36                           push 0x36
00BECFB2  E9 49 06 00 00                  jmp 0x140bed600
00BECFB7  90                              nop
00BECFB8  6A 37                           push 0x37
00BECFBA  E9 41 06 00 00                  jmp 0x140bed600
00BECFBF  90                              nop
00BECFC0  6A 38                           push 0x38
00BECFC2  E9 39 06 00 00                  jmp 0x140bed600
00BECFC7  90                              nop
00BECFC8  6A 39                           push 0x39
00BECFCA  E9 31 06 00 00                  jmp 0x140bed600
00BECFCF  90                              nop
00BECFD0  6A 3A                           push 0x3a
00BECFD2  E9 29 06 00 00                  jmp 0x140bed600
00BECFD7  90                              nop
00BECFD8  6A 3B                           push 0x3b
00BECFDA  E9 21 06 00 00                  jmp 0x140bed600
00BECFDF  90                              nop
00BECFE0  6A 3C                           push 0x3c
00BECFE2  E9 19 06 00 00                  jmp 0x140bed600
00BECFE7  90                              nop
00BECFE8  6A 3D                           push 0x3d
00BECFEA  E9 11 06 00 00                  jmp 0x140bed600
00BECFEF  90                              nop
00BECFF0  6A 3E                           push 0x3e
00BECFF2  E9 09 06 00 00                  jmp 0x140bed600
00BECFF7  90                              nop
00BECFF8  6A 3F                           push 0x3f
00BECFFA  E9 01 06 00 00                  jmp 0x140bed600
00BECFFF  90                              nop
00BED000  6A 40                           push 0x40
00BED002  E9 F9 05 00 00                  jmp 0x140bed600
00BED007  90                              nop
00BED008  6A 41                           push 0x41
00BED00A  E9 F1 05 00 00                  jmp 0x140bed600
00BED00F  90                              nop
00BED010  6A 42                           push 0x42
00BED012  E9 E9 05 00 00                  jmp 0x140bed600
00BED017  90                              nop
00BED018  6A 43                           push 0x43
00BED01A  E9 E1 05 00 00                  jmp 0x140bed600
00BED01F  90                              nop
00BED020  6A 44                           push 0x44
00BED022  E9 D9 05 00 00                  jmp 0x140bed600
00BED027  90                              nop
00BED028  6A 45                           push 0x45
00BED02A  E9 D1 05 00 00                  jmp 0x140bed600
00BED02F  90                              nop
00BED030  6A 46                           push 0x46
00BED032  E9 C9 05 00 00                  jmp 0x140bed600
00BED037  90                              nop
00BED038  6A 47                           push 0x47
00BED03A  E9 C1 05 00 00                  jmp 0x140bed600
00BED03F  90                              nop
00BED040  6A 48                           push 0x48
00BED042  E9 B9 05 00 00                  jmp 0x140bed600
00BED047  90                              nop
00BED048  6A 49                           push 0x49
00BED04A  E9 B1 05 00 00                  jmp 0x140bed600
00BED04F  90                              nop
00BED050  6A 4A                           push 0x4a
00BED052  E9 A9 05 00 00                  jmp 0x140bed600
00BED057  90                              nop
00BED058  6A 4B                           push 0x4b
00BED05A  E9 A1 05 00 00                  jmp 0x140bed600
00BED05F  90                              nop
00BED060  6A 4C                           push 0x4c
00BED062  E9 99 05 00 00                  jmp 0x140bed600
00BED067  90                              nop
00BED068  6A 4D                           push 0x4d
00BED06A  E9 91 05 00 00                  jmp 0x140bed600
00BED06F  90                              nop
00BED070  6A 4E                           push 0x4e
00BED072  E9 89 05 00 00                  jmp 0x140bed600
00BED077  90                              nop
00BED078  6A 4F                           push 0x4f
00BED07A  E9 81 05 00 00                  jmp 0x140bed600
00BED07F  90                              nop
00BED080  6A 50                           push 0x50
00BED082  E9 79 05 00 00                  jmp 0x140bed600
00BED087  90                              nop
00BED088  6A 51                           push 0x51
00BED08A  E9 71 05 00 00                  jmp 0x140bed600
00BED08F  90                              nop
00BED090  6A 52                           push 0x52
00BED092  E9 69 05 00 00                  jmp 0x140bed600
00BED097  90                              nop
00BED098  6A 53                           push 0x53
00BED09A  E9 61 05 00 00                  jmp 0x140bed600
00BED09F  90                              nop
00BED0A0  6A 54                           push 0x54
00BED0A2  E9 59 05 00 00                  jmp 0x140bed600
00BED0A7  90                              nop
00BED0A8  6A 55                           push 0x55
00BED0AA  E9 51 05 00 00                  jmp 0x140bed600
00BED0AF  90                              nop
00BED0B0  6A 56                           push 0x56
00BED0B2  E9 49 05 00 00                  jmp 0x140bed600
00BED0B7  90                              nop
00BED0B8  6A 57                           push 0x57
00BED0BA  E9 41 05 00 00                  jmp 0x140bed600
00BED0BF  90                              nop
00BED0C0  6A 58                           push 0x58
00BED0C2  E9 39 05 00 00                  jmp 0x140bed600
00BED0C7  90                              nop
00BED0C8  6A 59                           push 0x59
00BED0CA  E9 31 05 00 00                  jmp 0x140bed600
00BED0CF  90                              nop
00BED0D0  6A 5A                           push 0x5a
00BED0D2  E9 29 05 00 00                  jmp 0x140bed600
00BED0D7  90                              nop
00BED0D8  6A 5B                           push 0x5b
00BED0DA  E9 21 05 00 00                  jmp 0x140bed600
00BED0DF  90                              nop
00BED0E0  6A 5C                           push 0x5c
00BED0E2  E9 19 05 00 00                  jmp 0x140bed600
00BED0E7  90                              nop
00BED0E8  6A 5D                           push 0x5d
00BED0EA  E9 11 05 00 00                  jmp 0x140bed600
00BED0EF  90                              nop
00BED0F0  6A 5E                           push 0x5e
00BED0F2  E9 09 05 00 00                  jmp 0x140bed600
00BED0F7  90                              nop
00BED0F8  6A 5F                           push 0x5f
00BED0FA  E9 01 05 00 00                  jmp 0x140bed600
00BED0FF  90                              nop
00BED100  6A 60                           push 0x60
00BED102  E9 F9 04 00 00                  jmp 0x140bed600
00BED107  90                              nop
00BED108  6A 61                           push 0x61
00BED10A  E9 F1 04 00 00                  jmp 0x140bed600
00BED10F  90                              nop
00BED110  6A 62                           push 0x62
00BED112  E9 E9 04 00 00                  jmp 0x140bed600
00BED117  90                              nop
00BED118  6A 63                           push 0x63
00BED11A  E9 E1 04 00 00                  jmp 0x140bed600
00BED11F  90                              nop
00BED120  6A 64                           push 0x64
00BED122  E9 D9 04 00 00                  jmp 0x140bed600
00BED127  90                              nop
00BED128  6A 65                           push 0x65
00BED12A  E9 D1 04 00 00                  jmp 0x140bed600
00BED12F  90                              nop
00BED130  6A 66                           push 0x66
00BED132  E9 C9 04 00 00                  jmp 0x140bed600
00BED137  90                              nop
00BED138  6A 67                           push 0x67
00BED13A  E9 C1 04 00 00                  jmp 0x140bed600
00BED13F  90                              nop
00BED140  6A 68                           push 0x68
00BED142  E9 B9 04 00 00                  jmp 0x140bed600
00BED147  90                              nop
00BED148  6A 69                           push 0x69
00BED14A  E9 B1 04 00 00                  jmp 0x140bed600
00BED14F  90                              nop
00BED150  6A 6A                           push 0x6a
00BED152  E9 A9 04 00 00                  jmp 0x140bed600
00BED157  90                              nop
00BED158  6A 6B                           push 0x6b
00BED15A  E9 A1 04 00 00                  jmp 0x140bed600
00BED15F  90                              nop
00BED160  6A 6C                           push 0x6c
00BED162  E9 99 04 00 00                  jmp 0x140bed600
00BED167  90                              nop
00BED168  6A 6D                           push 0x6d
00BED16A  E9 91 04 00 00                  jmp 0x140bed600
00BED16F  90                              nop
00BED170  6A 6E                           push 0x6e
00BED172  E9 89 04 00 00                  jmp 0x140bed600
00BED177  90                              nop
00BED178  6A 6F                           push 0x6f
00BED17A  E9 81 04 00 00                  jmp 0x140bed600
00BED17F  90                              nop
00BED180  6A 70                           push 0x70
00BED182  E9 79 04 00 00                  jmp 0x140bed600
00BED187  90                              nop
00BED188  6A 71                           push 0x71
00BED18A  E9 71 04 00 00                  jmp 0x140bed600
00BED18F  90                              nop
00BED190  6A 72                           push 0x72
00BED192  E9 69 04 00 00                  jmp 0x140bed600
00BED197  90                              nop
00BED198  6A 73                           push 0x73
00BED19A  E9 61 04 00 00                  jmp 0x140bed600
00BED19F  90                              nop
00BED1A0  6A 74                           push 0x74
00BED1A2  E9 59 04 00 00                  jmp 0x140bed600
00BED1A7  90                              nop
00BED1A8  6A 75                           push 0x75
00BED1AA  E9 51 04 00 00                  jmp 0x140bed600
00BED1AF  90                              nop
00BED1B0  6A 76                           push 0x76
00BED1B2  E9 49 04 00 00                  jmp 0x140bed600
00BED1B7  90                              nop
00BED1B8  6A 77                           push 0x77
00BED1BA  E9 41 04 00 00                  jmp 0x140bed600
00BED1BF  90                              nop
00BED1C0  6A 78                           push 0x78
00BED1C2  E9 39 04 00 00                  jmp 0x140bed600
00BED1C7  90                              nop
00BED1C8  6A 79                           push 0x79
00BED1CA  E9 31 04 00 00                  jmp 0x140bed600
00BED1CF  90                              nop
00BED1D0  6A 7A                           push 0x7a
00BED1D2  E9 29 04 00 00                  jmp 0x140bed600
00BED1D7  90                              nop
00BED1D8  6A 7B                           push 0x7b
00BED1DA  E9 21 04 00 00                  jmp 0x140bed600
00BED1DF  90                              nop
00BED1E0  6A 7C                           push 0x7c
00BED1E2  E9 19 04 00 00                  jmp 0x140bed600
00BED1E7  90                              nop
00BED1E8  6A 7D                           push 0x7d
00BED1EA  E9 11 04 00 00                  jmp 0x140bed600
00BED1EF  90                              nop
00BED1F0  6A 7E                           push 0x7e
00BED1F2  E9 09 04 00 00                  jmp 0x140bed600
00BED1F7  90                              nop
00BED1F8  6A 7F                           push 0x7f
00BED1FA  E9 01 04 00 00                  jmp 0x140bed600
00BED1FF  90                              nop
00BED200  6A 80                           push -0x80
00BED202  E9 F9 03 00 00                  jmp 0x140bed600
00BED207  90                              nop
00BED208  6A 81                           push -0x7f
00BED20A  E9 F1 03 00 00                  jmp 0x140bed600
00BED20F  90                              nop
00BED210  6A 82                           push -0x7e
00BED212  E9 E9 03 00 00                  jmp 0x140bed600
00BED217  90                              nop
00BED218  6A 83                           push -0x7d
00BED21A  E9 E1 03 00 00                  jmp 0x140bed600
00BED21F  90                              nop
00BED220  6A 84                           push -0x7c
00BED222  E9 D9 03 00 00                  jmp 0x140bed600
00BED227  90                              nop
00BED228  6A 85                           push -0x7b
00BED22A  E9 D1 03 00 00                  jmp 0x140bed600
00BED22F  90                              nop
00BED230  6A 86                           push -0x7a
00BED232  E9 C9 03 00 00                  jmp 0x140bed600
00BED237  90                              nop
00BED238  6A 87                           push -0x79
00BED23A  E9 C1 03 00 00                  jmp 0x140bed600
00BED23F  90                              nop
00BED240  6A 88                           push -0x78
00BED242  E9 B9 03 00 00                  jmp 0x140bed600
00BED247  90                              nop
00BED248  6A 89                           push -0x77
00BED24A  E9 B1 03 00 00                  jmp 0x140bed600
00BED24F  90                              nop
00BED250  6A 8A                           push -0x76
00BED252  E9 A9 03 00 00                  jmp 0x140bed600
00BED257  90                              nop
00BED258  6A 8B                           push -0x75
00BED25A  E9 A1 03 00 00                  jmp 0x140bed600
00BED25F  90                              nop
00BED260  6A 8C                           push -0x74
00BED262  E9 99 03 00 00                  jmp 0x140bed600
00BED267  90                              nop
00BED268  6A 8D                           push -0x73
00BED26A  E9 91 03 00 00                  jmp 0x140bed600
00BED26F  90                              nop
00BED270  6A 8E                           push -0x72
00BED272  E9 89 03 00 00                  jmp 0x140bed600
00BED277  90                              nop
00BED278  6A 8F                           push -0x71
00BED27A  E9 81 03 00 00                  jmp 0x140bed600
00BED27F  90                              nop
00BED280  6A 90                           push -0x70
00BED282  E9 79 03 00 00                  jmp 0x140bed600
00BED287  90                              nop
00BED288  6A 91                           push -0x6f
00BED28A  E9 71 03 00 00                  jmp 0x140bed600
00BED28F  90                              nop
00BED290  6A 92                           push -0x6e
00BED292  E9 69 03 00 00                  jmp 0x140bed600
00BED297  90                              nop
00BED298  6A 93                           push -0x6d
00BED29A  E9 61 03 00 00                  jmp 0x140bed600
00BED29F  90                              nop
00BED2A0  6A 94                           push -0x6c
00BED2A2  E9 59 03 00 00                  jmp 0x140bed600
00BED2A7  90                              nop
00BED2A8  6A 95                           push -0x6b
00BED2AA  E9 51 03 00 00                  jmp 0x140bed600
00BED2AF  90                              nop
00BED2B0  6A 96                           push -0x6a
00BED2B2  E9 49 03 00 00                  jmp 0x140bed600
00BED2B7  90                              nop
00BED2B8  6A 97                           push -0x69
00BED2BA  E9 41 03 00 00                  jmp 0x140bed600
00BED2BF  90                              nop
00BED2C0  6A 98                           push -0x68
00BED2C2  E9 39 03 00 00                  jmp 0x140bed600
00BED2C7  90                              nop
00BED2C8  6A 99                           push -0x67
00BED2CA  E9 31 03 00 00                  jmp 0x140bed600
00BED2CF  90                              nop
00BED2D0  6A 9A                           push -0x66
00BED2D2  E9 29 03 00 00                  jmp 0x140bed600
00BED2D7  90                              nop
00BED2D8  6A 9B                           push -0x65
00BED2DA  E9 21 03 00 00                  jmp 0x140bed600
00BED2DF  90                              nop
00BED2E0  6A 9C                           push -0x64
00BED2E2  E9 19 03 00 00                  jmp 0x140bed600
00BED2E7  90                              nop
00BED2E8  6A 9D                           push -0x63
00BED2EA  E9 11 03 00 00                  jmp 0x140bed600
00BED2EF  90                              nop
00BED2F0  6A 9E                           push -0x62
00BED2F2  E9 09 03 00 00                  jmp 0x140bed600
00BED2F7  90                              nop
00BED2F8  6A 9F                           push -0x61
00BED2FA  E9 01 03 00 00                  jmp 0x140bed600
00BED2FF  90                              nop
00BED300  6A A0                           push -0x60
00BED302  E9 F9 02 00 00                  jmp 0x140bed600
00BED307  90                              nop
00BED308  6A A1                           push -0x5f
00BED30A  E9 F1 02 00 00                  jmp 0x140bed600
00BED30F  90                              nop
00BED310  6A A2                           push -0x5e
00BED312  E9 E9 02 00 00                  jmp 0x140bed600
00BED317  90                              nop
00BED318  6A A3                           push -0x5d
00BED31A  E9 E1 02 00 00                  jmp 0x140bed600
00BED31F  90                              nop
00BED320  6A A4                           push -0x5c
00BED322  E9 D9 02 00 00                  jmp 0x140bed600
00BED327  90                              nop
00BED328  6A A5                           push -0x5b
00BED32A  E9 D1 02 00 00                  jmp 0x140bed600
00BED32F  90                              nop
00BED330  6A A6                           push -0x5a
00BED332  E9 C9 02 00 00                  jmp 0x140bed600
00BED337  90                              nop
00BED338  6A A7                           push -0x59
00BED33A  E9 C1 02 00 00                  jmp 0x140bed600
00BED33F  90                              nop
00BED340  6A A8                           push -0x58
00BED342  E9 B9 02 00 00                  jmp 0x140bed600
00BED347  90                              nop
00BED348  6A A9                           push -0x57
00BED34A  E9 B1 02 00 00                  jmp 0x140bed600
00BED34F  90                              nop
00BED350  6A AA                           push -0x56
00BED352  E9 A9 02 00 00                  jmp 0x140bed600
00BED357  90                              nop
00BED358  6A AB                           push -0x55
00BED35A  E9 A1 02 00 00                  jmp 0x140bed600
00BED35F  90                              nop
00BED360  6A AC                           push -0x54
00BED362  E9 99 02 00 00                  jmp 0x140bed600
00BED367  90                              nop
00BED368  6A AD                           push -0x53
00BED36A  E9 91 02 00 00                  jmp 0x140bed600
00BED36F  90                              nop
00BED370  6A AE                           push -0x52
00BED372  E9 89 02 00 00                  jmp 0x140bed600
00BED377  90                              nop
00BED378  6A AF                           push -0x51
00BED37A  E9 81 02 00 00                  jmp 0x140bed600
00BED37F  90                              nop
00BED380  6A B0                           push -0x50
00BED382  E9 79 02 00 00                  jmp 0x140bed600
00BED387  90                              nop
00BED388  6A B1                           push -0x4f
00BED38A  E9 71 02 00 00                  jmp 0x140bed600
00BED38F  90                              nop
00BED390  6A B2                           push -0x4e
00BED392  E9 69 02 00 00                  jmp 0x140bed600
00BED397  90                              nop
00BED398  6A B3                           push -0x4d
00BED39A  E9 61 02 00 00                  jmp 0x140bed600
00BED39F  90                              nop
00BED3A0  6A B4                           push -0x4c
00BED3A2  E9 59 02 00 00                  jmp 0x140bed600
00BED3A7  90                              nop
00BED3A8  6A B5                           push -0x4b
00BED3AA  E9 51 02 00 00                  jmp 0x140bed600
00BED3AF  90                              nop
00BED3B0  6A B6                           push -0x4a
00BED3B2  E9 49 02 00 00                  jmp 0x140bed600
00BED3B7  90                              nop
00BED3B8  6A B7                           push -0x49
00BED3BA  E9 41 02 00 00                  jmp 0x140bed600
00BED3BF  90                              nop
00BED3C0  6A B8                           push -0x48
00BED3C2  E9 39 02 00 00                  jmp 0x140bed600
00BED3C7  90                              nop
00BED3C8  6A B9                           push -0x47
00BED3CA  E9 31 02 00 00                  jmp 0x140bed600
00BED3CF  90                              nop
00BED3D0  6A BA                           push -0x46
00BED3D2  E9 29 02 00 00                  jmp 0x140bed600
00BED3D7  90                              nop
00BED3D8  6A BB                           push -0x45
00BED3DA  E9 21 02 00 00                  jmp 0x140bed600
00BED3DF  90                              nop
00BED3E0  6A BC                           push -0x44
00BED3E2  E9 19 02 00 00                  jmp 0x140bed600
00BED3E7  90                              nop
00BED3E8  6A BD                           push -0x43
00BED3EA  E9 11 02 00 00                  jmp 0x140bed600
00BED3EF  90                              nop
00BED3F0  6A BE                           push -0x42
00BED3F2  E9 09 02 00 00                  jmp 0x140bed600
00BED3F7  90                              nop
00BED3F8  6A BF                           push -0x41
00BED3FA  E9 01 02 00 00                  jmp 0x140bed600
00BED3FF  90                              nop
00BED400  6A C0                           push -0x40
00BED402  E9 F9 01 00 00                  jmp 0x140bed600
00BED407  90                              nop
00BED408  6A C1                           push -0x3f
00BED40A  E9 F1 01 00 00                  jmp 0x140bed600
00BED40F  90                              nop
00BED410  6A C2                           push -0x3e
00BED412  E9 E9 01 00 00                  jmp 0x140bed600
00BED417  90                              nop
00BED418  6A C3                           push -0x3d
00BED41A  E9 E1 01 00 00                  jmp 0x140bed600
00BED41F  90                              nop
00BED420  6A C4                           push -0x3c
00BED422  E9 D9 01 00 00                  jmp 0x140bed600
00BED427  90                              nop
00BED428  6A C5                           push -0x3b
00BED42A  E9 D1 01 00 00                  jmp 0x140bed600
00BED42F  90                              nop
00BED430  6A C6                           push -0x3a
00BED432  E9 C9 01 00 00                  jmp 0x140bed600
00BED437  90                              nop
00BED438  6A C7                           push -0x39
00BED43A  E9 C1 01 00 00                  jmp 0x140bed600
00BED43F  90                              nop
00BED440  6A C8                           push -0x38
00BED442  E9 B9 01 00 00                  jmp 0x140bed600
00BED447  90                              nop
00BED448  6A C9                           push -0x37
00BED44A  E9 B1 01 00 00                  jmp 0x140bed600
00BED44F  90                              nop
00BED450  6A CA                           push -0x36
00BED452  E9 A9 01 00 00                  jmp 0x140bed600
00BED457  90                              nop
00BED458  6A CB                           push -0x35
00BED45A  E9 A1 01 00 00                  jmp 0x140bed600
00BED45F  90                              nop
00BED460  6A CC                           push -0x34
00BED462  E9 99 01 00 00                  jmp 0x140bed600
00BED467  90                              nop
00BED468  6A CD                           push -0x33
00BED46A  E9 91 01 00 00                  jmp 0x140bed600
00BED46F  90                              nop
00BED470  6A CE                           push -0x32
00BED472  E9 89 01 00 00                  jmp 0x140bed600
00BED477  90                              nop
00BED478  6A CF                           push -0x31
00BED47A  E9 81 01 00 00                  jmp 0x140bed600
00BED47F  90                              nop
00BED480  6A D0                           push -0x30
00BED482  E9 79 01 00 00                  jmp 0x140bed600
00BED487  90                              nop
00BED488  6A D1                           push -0x2f
00BED48A  E9 71 01 00 00                  jmp 0x140bed600
00BED48F  90                              nop
00BED490  6A D2                           push -0x2e
00BED492  E9 69 01 00 00                  jmp 0x140bed600
00BED497  90                              nop
00BED498  6A D3                           push -0x2d
00BED49A  E9 61 01 00 00                  jmp 0x140bed600
00BED49F  90                              nop
00BED4A0  6A D4                           push -0x2c
00BED4A2  E9 59 01 00 00                  jmp 0x140bed600
00BED4A7  90                              nop
00BED4A8  6A D5                           push -0x2b
00BED4AA  E9 51 01 00 00                  jmp 0x140bed600
00BED4AF  90                              nop
00BED4B0  6A D6                           push -0x2a
00BED4B2  E9 49 01 00 00                  jmp 0x140bed600
00BED4B7  90                              nop
00BED4B8  6A D7                           push -0x29
00BED4BA  E9 41 01 00 00                  jmp 0x140bed600
00BED4BF  90                              nop
00BED4C0  6A D8                           push -0x28
00BED4C2  E9 39 01 00 00                  jmp 0x140bed600
00BED4C7  90                              nop
00BED4C8  6A D9                           push -0x27
00BED4CA  E9 31 01 00 00                  jmp 0x140bed600
00BED4CF  90                              nop
00BED4D0  6A DA                           push -0x26
00BED4D2  E9 29 01 00 00                  jmp 0x140bed600
00BED4D7  90                              nop
00BED4D8  6A DB                           push -0x25
00BED4DA  E9 21 01 00 00                  jmp 0x140bed600
00BED4DF  90                              nop
00BED4E0  6A DC                           push -0x24
00BED4E2  E9 19 01 00 00                  jmp 0x140bed600
00BED4E7  90                              nop
00BED4E8  6A DD                           push -0x23
00BED4EA  E9 11 01 00 00                  jmp 0x140bed600
00BED4EF  90                              nop
00BED4F0  6A DE                           push -0x22
00BED4F2  E9 09 01 00 00                  jmp 0x140bed600
00BED4F7  90                              nop
00BED4F8  6A DF                           push -0x21
00BED4FA  E9 01 01 00 00                  jmp 0x140bed600
00BED4FF  90                              nop
00BED500  6A E0                           push -0x20
00BED502  E9 F9 00 00 00                  jmp 0x140bed600
00BED507  90                              nop
00BED508  6A E1                           push -0x1f
00BED50A  E9 F1 00 00 00                  jmp 0x140bed600
00BED50F  90                              nop
00BED510  6A E2                           push -0x1e
00BED512  E9 E9 00 00 00                  jmp 0x140bed600
00BED517  90                              nop
00BED518  6A E3                           push -0x1d
00BED51A  E9 E1 00 00 00                  jmp 0x140bed600
00BED51F  90                              nop
00BED520  6A E4                           push -0x1c
00BED522  E9 D9 00 00 00                  jmp 0x140bed600
00BED527  90                              nop
00BED528  6A E5                           push -0x1b
00BED52A  E9 D1 00 00 00                  jmp 0x140bed600
00BED52F  90                              nop
00BED530  6A E6                           push -0x1a
00BED532  E9 C9 00 00 00                  jmp 0x140bed600
00BED537  90                              nop
00BED538  6A E7                           push -0x19
00BED53A  E9 C1 00 00 00                  jmp 0x140bed600
00BED53F  90                              nop
00BED540  6A E8                           push -0x18
00BED542  E9 B9 00 00 00                  jmp 0x140bed600
00BED547  90                              nop
00BED548  6A E9                           push -0x17
00BED54A  E9 B1 00 00 00                  jmp 0x140bed600
00BED54F  90                              nop
00BED550  6A EA                           push -0x16
00BED552  E9 A9 00 00 00                  jmp 0x140bed600
00BED557  90                              nop
00BED558  6A EB                           push -0x15
00BED55A  E9 A1 00 00 00                  jmp 0x140bed600
00BED55F  90                              nop
00BED560  6A EC                           push -0x14
00BED562  E9 99 00 00 00                  jmp 0x140bed600
00BED567  90                              nop
00BED568  6A ED                           push -0x13
00BED56A  E9 91 00 00 00                  jmp 0x140bed600
00BED56F  90                              nop
00BED570  6A EE                           push -0x12
00BED572  E9 89 00 00 00                  jmp 0x140bed600
00BED577  90                              nop
00BED578  6A EF                           push -0x11
00BED57A  E9 81 00 00 00                  jmp 0x140bed600
00BED57F  90                              nop
00BED580  6A F0                           push -0x10
00BED582  E9 79 00 00 00                  jmp 0x140bed600
00BED587  90                              nop
00BED588  6A F1                           push -0xf
00BED58A  E9 71 00 00 00                  jmp 0x140bed600
00BED58F  90                              nop
00BED590  6A F2                           push -0xe
00BED592  E9 69 00 00 00                  jmp 0x140bed600
00BED597  90                              nop
00BED598  6A F3                           push -0xd
00BED59A  E9 61 00 00 00                  jmp 0x140bed600
00BED59F  90                              nop
00BED5A0  6A F4                           push -0xc
00BED5A2  E9 59 00 00 00                  jmp 0x140bed600
00BED5A7  90                              nop
00BED5A8  6A F5                           push -0xb
00BED5AA  E9 51 00 00 00                  jmp 0x140bed600
00BED5AF  90                              nop
00BED5B0  6A F6                           push -0xa
00BED5B2  E9 49 00 00 00                  jmp 0x140bed600
00BED5B7  90                              nop
00BED5B8  6A F7                           push -9
00BED5BA  E9 41 00 00 00                  jmp 0x140bed600
00BED5BF  90                              nop
00BED5C0  6A F8                           push -8
00BED5C2  E9 39 00 00 00                  jmp 0x140bed600
00BED5C7  90                              nop
00BED5C8  6A F9                           push -7
00BED5CA  E9 31 00 00 00                  jmp 0x140bed600
00BED5CF  90                              nop
00BED5D0  6A FA                           push -6
00BED5D2  EB 2C                           jmp 0x140bed600
00BED5D4  0F 1F 40 00                     nop dword ptr [rax]
00BED5D8  6A FB                           push -5
00BED5DA  EB 24                           jmp 0x140bed600
00BED5DC  0F 1F 40 00                     nop dword ptr [rax]
00BED5E0  6A FC                           push -4
00BED5E2  EB 1C                           jmp 0x140bed600
00BED5E4  0F 1F 40 00                     nop dword ptr [rax]
00BED5E8  6A FD                           push -3
00BED5EA  EB 14                           jmp 0x140bed600
00BED5EC  0F 1F 40 00                     nop dword ptr [rax]
00BED5F0  6A FE                           push -2
00BED5F2  EB 0C                           jmp 0x140bed600
00BED5F4  0F 1F 40 00                     nop dword ptr [rax]
00BED5F8  6A FF                           push -1
00BED5FA  EB 04                           jmp 0x140bed600
00BED5FC  0F 1F 40 00                     nop dword ptr [rax]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall HalpBlkUnexpectedInterrupt(void)
{
}
```

## 5. (Beta) C Style

```c
void HalpBlkUnexpectedInterrupt(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=miniex&rva=0x00BECE00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
