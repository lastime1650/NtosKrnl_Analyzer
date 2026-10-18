# KiIsrThunk

- RVA: `0x006B4E70`–`0x006B5671` (길이 `2,049` bytes)
- VA: `0x00000001406B4E70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2088`
- 디코드: `769`개 명령, `2,049/2,049` bytes 표시
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
  - `0x006B4E73` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4E7B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4E83` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4E8B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4E93` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4E9B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EA3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EAB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EB3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EBB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EC3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4ECB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4ED3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EDB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EE3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EEB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EF3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4EFB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F03` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F0B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F13` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F1B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F23` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F2B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F33` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F3B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F43` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F4B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F53` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F5B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F63` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F6B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F73` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F7B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F83` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F8B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F93` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4F9B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FA3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FAB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FB3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FBB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FC3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FCB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FD3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FDB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FE3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FEB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FF3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B4FFB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5003` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B500B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5013` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B501B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5023` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B502B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5033` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B503B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5043` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B504B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5053` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B505B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5063` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B506B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5073` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B507B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5083` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B508B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5093` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B509B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B50FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5103` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B510B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5113` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B511B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5123` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B512B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5133` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B513B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5143` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B514B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5153` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B515B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5163` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B516B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5173` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B517B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5183` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B518B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5193` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B519B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B51FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5203` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B520B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5213` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B521B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5223` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B522B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5233` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B523B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5243` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B524B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5253` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B525B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5263` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B526B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5273` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B527B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5283` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B528B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5293` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B529B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B52FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5303` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B530B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5313` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B531B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5323` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B532B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5333` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B533B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5343` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B534B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5353` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B535B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5363` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B536B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5373` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B537B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5383` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B538B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5393` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B539B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B53FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5403` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B540B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5413` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B541B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5423` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B542B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5433` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B543B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5443` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B544B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5453` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B545B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5463` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B546B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5473` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B547B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5483` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B548B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5493` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B549B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B54FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5503` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B550B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5513` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B551B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5523` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B552B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5533` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B553B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5543` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B554B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5553` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B555B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5563` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B556B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5573` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B557B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5583` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B558B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5593` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B559B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55A3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55AB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55B3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55BB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55C3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55CB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55D3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55DB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55E3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55EB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55F3` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B55FB` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5603` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B560B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5613` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B561B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5623` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B562B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5633` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B563B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5643` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B564B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5653` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B565B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B5663` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)
  - `0x006B566B` → [KxIsrLinkage + 0x1](KxIsrLinkage_function_006B5680.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B4E70  6A 00                           push 0
006B4E72  55                              push rbp
006B4E73  E9 09 08 00 00                  jmp 0x1406b5681
006B4E78  6A 01                           push 1
006B4E7A  55                              push rbp
006B4E7B  E9 01 08 00 00                  jmp 0x1406b5681
006B4E80  6A 02                           push 2
006B4E82  55                              push rbp
006B4E83  E9 F9 07 00 00                  jmp 0x1406b5681
006B4E88  6A 03                           push 3
006B4E8A  55                              push rbp
006B4E8B  E9 F1 07 00 00                  jmp 0x1406b5681
006B4E90  6A 04                           push 4
006B4E92  55                              push rbp
006B4E93  E9 E9 07 00 00                  jmp 0x1406b5681
006B4E98  6A 05                           push 5
006B4E9A  55                              push rbp
006B4E9B  E9 E1 07 00 00                  jmp 0x1406b5681
006B4EA0  6A 06                           push 6
006B4EA2  55                              push rbp
006B4EA3  E9 D9 07 00 00                  jmp 0x1406b5681
006B4EA8  6A 07                           push 7
006B4EAA  55                              push rbp
006B4EAB  E9 D1 07 00 00                  jmp 0x1406b5681
006B4EB0  6A 08                           push 8
006B4EB2  55                              push rbp
006B4EB3  E9 C9 07 00 00                  jmp 0x1406b5681
006B4EB8  6A 09                           push 9
006B4EBA  55                              push rbp
006B4EBB  E9 C1 07 00 00                  jmp 0x1406b5681
006B4EC0  6A 0A                           push 0xa
006B4EC2  55                              push rbp
006B4EC3  E9 B9 07 00 00                  jmp 0x1406b5681
006B4EC8  6A 0B                           push 0xb
006B4ECA  55                              push rbp
006B4ECB  E9 B1 07 00 00                  jmp 0x1406b5681
006B4ED0  6A 0C                           push 0xc
006B4ED2  55                              push rbp
006B4ED3  E9 A9 07 00 00                  jmp 0x1406b5681
006B4ED8  6A 0D                           push 0xd
006B4EDA  55                              push rbp
006B4EDB  E9 A1 07 00 00                  jmp 0x1406b5681
006B4EE0  6A 0E                           push 0xe
006B4EE2  55                              push rbp
006B4EE3  E9 99 07 00 00                  jmp 0x1406b5681
006B4EE8  6A 0F                           push 0xf
006B4EEA  55                              push rbp
006B4EEB  E9 91 07 00 00                  jmp 0x1406b5681
006B4EF0  6A 10                           push 0x10
006B4EF2  55                              push rbp
006B4EF3  E9 89 07 00 00                  jmp 0x1406b5681
006B4EF8  6A 11                           push 0x11
006B4EFA  55                              push rbp
006B4EFB  E9 81 07 00 00                  jmp 0x1406b5681
006B4F00  6A 12                           push 0x12
006B4F02  55                              push rbp
006B4F03  E9 79 07 00 00                  jmp 0x1406b5681
006B4F08  6A 13                           push 0x13
006B4F0A  55                              push rbp
006B4F0B  E9 71 07 00 00                  jmp 0x1406b5681
006B4F10  6A 14                           push 0x14
006B4F12  55                              push rbp
006B4F13  E9 69 07 00 00                  jmp 0x1406b5681
006B4F18  6A 15                           push 0x15
006B4F1A  55                              push rbp
006B4F1B  E9 61 07 00 00                  jmp 0x1406b5681
006B4F20  6A 16                           push 0x16
006B4F22  55                              push rbp
006B4F23  E9 59 07 00 00                  jmp 0x1406b5681
006B4F28  6A 17                           push 0x17
006B4F2A  55                              push rbp
006B4F2B  E9 51 07 00 00                  jmp 0x1406b5681
006B4F30  6A 18                           push 0x18
006B4F32  55                              push rbp
006B4F33  E9 49 07 00 00                  jmp 0x1406b5681
006B4F38  6A 19                           push 0x19
006B4F3A  55                              push rbp
006B4F3B  E9 41 07 00 00                  jmp 0x1406b5681
006B4F40  6A 1A                           push 0x1a
006B4F42  55                              push rbp
006B4F43  E9 39 07 00 00                  jmp 0x1406b5681
006B4F48  6A 1B                           push 0x1b
006B4F4A  55                              push rbp
006B4F4B  E9 31 07 00 00                  jmp 0x1406b5681
006B4F50  6A 1C                           push 0x1c
006B4F52  55                              push rbp
006B4F53  E9 29 07 00 00                  jmp 0x1406b5681
006B4F58  6A 1D                           push 0x1d
006B4F5A  55                              push rbp
006B4F5B  E9 21 07 00 00                  jmp 0x1406b5681
006B4F60  6A 1E                           push 0x1e
006B4F62  55                              push rbp
006B4F63  E9 19 07 00 00                  jmp 0x1406b5681
006B4F68  6A 1F                           push 0x1f
006B4F6A  55                              push rbp
006B4F6B  E9 11 07 00 00                  jmp 0x1406b5681
006B4F70  6A 20                           push 0x20
006B4F72  55                              push rbp
006B4F73  E9 09 07 00 00                  jmp 0x1406b5681
006B4F78  6A 21                           push 0x21
006B4F7A  55                              push rbp
006B4F7B  E9 01 07 00 00                  jmp 0x1406b5681
006B4F80  6A 22                           push 0x22
006B4F82  55                              push rbp
006B4F83  E9 F9 06 00 00                  jmp 0x1406b5681
006B4F88  6A 23                           push 0x23
006B4F8A  55                              push rbp
006B4F8B  E9 F1 06 00 00                  jmp 0x1406b5681
006B4F90  6A 24                           push 0x24
006B4F92  55                              push rbp
006B4F93  E9 E9 06 00 00                  jmp 0x1406b5681
006B4F98  6A 25                           push 0x25
006B4F9A  55                              push rbp
006B4F9B  E9 E1 06 00 00                  jmp 0x1406b5681
006B4FA0  6A 26                           push 0x26
006B4FA2  55                              push rbp
006B4FA3  E9 D9 06 00 00                  jmp 0x1406b5681
006B4FA8  6A 27                           push 0x27
006B4FAA  55                              push rbp
006B4FAB  E9 D1 06 00 00                  jmp 0x1406b5681
006B4FB0  6A 28                           push 0x28
006B4FB2  55                              push rbp
006B4FB3  E9 C9 06 00 00                  jmp 0x1406b5681
006B4FB8  6A 29                           push 0x29
006B4FBA  55                              push rbp
006B4FBB  E9 C1 06 00 00                  jmp 0x1406b5681
006B4FC0  6A 2A                           push 0x2a
006B4FC2  55                              push rbp
006B4FC3  E9 B9 06 00 00                  jmp 0x1406b5681
006B4FC8  6A 2B                           push 0x2b
006B4FCA  55                              push rbp
006B4FCB  E9 B1 06 00 00                  jmp 0x1406b5681
006B4FD0  6A 2C                           push 0x2c
006B4FD2  55                              push rbp
006B4FD3  E9 A9 06 00 00                  jmp 0x1406b5681
006B4FD8  6A 2D                           push 0x2d
006B4FDA  55                              push rbp
006B4FDB  E9 A1 06 00 00                  jmp 0x1406b5681
006B4FE0  6A 2E                           push 0x2e
006B4FE2  55                              push rbp
006B4FE3  E9 99 06 00 00                  jmp 0x1406b5681
006B4FE8  6A 2F                           push 0x2f
006B4FEA  55                              push rbp
006B4FEB  E9 91 06 00 00                  jmp 0x1406b5681
006B4FF0  6A 30                           push 0x30
006B4FF2  55                              push rbp
006B4FF3  E9 89 06 00 00                  jmp 0x1406b5681
006B4FF8  6A 31                           push 0x31
006B4FFA  55                              push rbp
006B4FFB  E9 81 06 00 00                  jmp 0x1406b5681
006B5000  6A 32                           push 0x32
006B5002  55                              push rbp
006B5003  E9 79 06 00 00                  jmp 0x1406b5681
006B5008  6A 33                           push 0x33
006B500A  55                              push rbp
006B500B  E9 71 06 00 00                  jmp 0x1406b5681
006B5010  6A 34                           push 0x34
006B5012  55                              push rbp
006B5013  E9 69 06 00 00                  jmp 0x1406b5681
006B5018  6A 35                           push 0x35
006B501A  55                              push rbp
006B501B  E9 61 06 00 00                  jmp 0x1406b5681
006B5020  6A 36                           push 0x36
006B5022  55                              push rbp
006B5023  E9 59 06 00 00                  jmp 0x1406b5681
006B5028  6A 37                           push 0x37
006B502A  55                              push rbp
006B502B  E9 51 06 00 00                  jmp 0x1406b5681
006B5030  6A 38                           push 0x38
006B5032  55                              push rbp
006B5033  E9 49 06 00 00                  jmp 0x1406b5681
006B5038  6A 39                           push 0x39
006B503A  55                              push rbp
006B503B  E9 41 06 00 00                  jmp 0x1406b5681
006B5040  6A 3A                           push 0x3a
006B5042  55                              push rbp
006B5043  E9 39 06 00 00                  jmp 0x1406b5681
006B5048  6A 3B                           push 0x3b
006B504A  55                              push rbp
006B504B  E9 31 06 00 00                  jmp 0x1406b5681
006B5050  6A 3C                           push 0x3c
006B5052  55                              push rbp
006B5053  E9 29 06 00 00                  jmp 0x1406b5681
006B5058  6A 3D                           push 0x3d
006B505A  55                              push rbp
006B505B  E9 21 06 00 00                  jmp 0x1406b5681
006B5060  6A 3E                           push 0x3e
006B5062  55                              push rbp
006B5063  E9 19 06 00 00                  jmp 0x1406b5681
006B5068  6A 3F                           push 0x3f
006B506A  55                              push rbp
006B506B  E9 11 06 00 00                  jmp 0x1406b5681
006B5070  6A 40                           push 0x40
006B5072  55                              push rbp
006B5073  E9 09 06 00 00                  jmp 0x1406b5681
006B5078  6A 41                           push 0x41
006B507A  55                              push rbp
006B507B  E9 01 06 00 00                  jmp 0x1406b5681
006B5080  6A 42                           push 0x42
006B5082  55                              push rbp
006B5083  E9 F9 05 00 00                  jmp 0x1406b5681
006B5088  6A 43                           push 0x43
006B508A  55                              push rbp
006B508B  E9 F1 05 00 00                  jmp 0x1406b5681
006B5090  6A 44                           push 0x44
006B5092  55                              push rbp
006B5093  E9 E9 05 00 00                  jmp 0x1406b5681
006B5098  6A 45                           push 0x45
006B509A  55                              push rbp
006B509B  E9 E1 05 00 00                  jmp 0x1406b5681
006B50A0  6A 46                           push 0x46
006B50A2  55                              push rbp
006B50A3  E9 D9 05 00 00                  jmp 0x1406b5681
006B50A8  6A 47                           push 0x47
006B50AA  55                              push rbp
006B50AB  E9 D1 05 00 00                  jmp 0x1406b5681
006B50B0  6A 48                           push 0x48
006B50B2  55                              push rbp
006B50B3  E9 C9 05 00 00                  jmp 0x1406b5681
006B50B8  6A 49                           push 0x49
006B50BA  55                              push rbp
006B50BB  E9 C1 05 00 00                  jmp 0x1406b5681
006B50C0  6A 4A                           push 0x4a
006B50C2  55                              push rbp
006B50C3  E9 B9 05 00 00                  jmp 0x1406b5681
006B50C8  6A 4B                           push 0x4b
006B50CA  55                              push rbp
006B50CB  E9 B1 05 00 00                  jmp 0x1406b5681
006B50D0  6A 4C                           push 0x4c
006B50D2  55                              push rbp
006B50D3  E9 A9 05 00 00                  jmp 0x1406b5681
006B50D8  6A 4D                           push 0x4d
006B50DA  55                              push rbp
006B50DB  E9 A1 05 00 00                  jmp 0x1406b5681
006B50E0  6A 4E                           push 0x4e
006B50E2  55                              push rbp
006B50E3  E9 99 05 00 00                  jmp 0x1406b5681
006B50E8  6A 4F                           push 0x4f
006B50EA  55                              push rbp
006B50EB  E9 91 05 00 00                  jmp 0x1406b5681
006B50F0  6A 50                           push 0x50
006B50F2  55                              push rbp
006B50F3  E9 89 05 00 00                  jmp 0x1406b5681
006B50F8  6A 51                           push 0x51
006B50FA  55                              push rbp
006B50FB  E9 81 05 00 00                  jmp 0x1406b5681
006B5100  6A 52                           push 0x52
006B5102  55                              push rbp
006B5103  E9 79 05 00 00                  jmp 0x1406b5681
006B5108  6A 53                           push 0x53
006B510A  55                              push rbp
006B510B  E9 71 05 00 00                  jmp 0x1406b5681
006B5110  6A 54                           push 0x54
006B5112  55                              push rbp
006B5113  E9 69 05 00 00                  jmp 0x1406b5681
006B5118  6A 55                           push 0x55
006B511A  55                              push rbp
006B511B  E9 61 05 00 00                  jmp 0x1406b5681
006B5120  6A 56                           push 0x56
006B5122  55                              push rbp
006B5123  E9 59 05 00 00                  jmp 0x1406b5681
006B5128  6A 57                           push 0x57
006B512A  55                              push rbp
006B512B  E9 51 05 00 00                  jmp 0x1406b5681
006B5130  6A 58                           push 0x58
006B5132  55                              push rbp
006B5133  E9 49 05 00 00                  jmp 0x1406b5681
006B5138  6A 59                           push 0x59
006B513A  55                              push rbp
006B513B  E9 41 05 00 00                  jmp 0x1406b5681
006B5140  6A 5A                           push 0x5a
006B5142  55                              push rbp
006B5143  E9 39 05 00 00                  jmp 0x1406b5681
006B5148  6A 5B                           push 0x5b
006B514A  55                              push rbp
006B514B  E9 31 05 00 00                  jmp 0x1406b5681
006B5150  6A 5C                           push 0x5c
006B5152  55                              push rbp
006B5153  E9 29 05 00 00                  jmp 0x1406b5681
006B5158  6A 5D                           push 0x5d
006B515A  55                              push rbp
006B515B  E9 21 05 00 00                  jmp 0x1406b5681
006B5160  6A 5E                           push 0x5e
006B5162  55                              push rbp
006B5163  E9 19 05 00 00                  jmp 0x1406b5681
006B5168  6A 5F                           push 0x5f
006B516A  55                              push rbp
006B516B  E9 11 05 00 00                  jmp 0x1406b5681
006B5170  6A 60                           push 0x60
006B5172  55                              push rbp
006B5173  E9 09 05 00 00                  jmp 0x1406b5681
006B5178  6A 61                           push 0x61
006B517A  55                              push rbp
006B517B  E9 01 05 00 00                  jmp 0x1406b5681
006B5180  6A 62                           push 0x62
006B5182  55                              push rbp
006B5183  E9 F9 04 00 00                  jmp 0x1406b5681
006B5188  6A 63                           push 0x63
006B518A  55                              push rbp
006B518B  E9 F1 04 00 00                  jmp 0x1406b5681
006B5190  6A 64                           push 0x64
006B5192  55                              push rbp
006B5193  E9 E9 04 00 00                  jmp 0x1406b5681
006B5198  6A 65                           push 0x65
006B519A  55                              push rbp
006B519B  E9 E1 04 00 00                  jmp 0x1406b5681
006B51A0  6A 66                           push 0x66
006B51A2  55                              push rbp
006B51A3  E9 D9 04 00 00                  jmp 0x1406b5681
006B51A8  6A 67                           push 0x67
006B51AA  55                              push rbp
006B51AB  E9 D1 04 00 00                  jmp 0x1406b5681
006B51B0  6A 68                           push 0x68
006B51B2  55                              push rbp
006B51B3  E9 C9 04 00 00                  jmp 0x1406b5681
006B51B8  6A 69                           push 0x69
006B51BA  55                              push rbp
006B51BB  E9 C1 04 00 00                  jmp 0x1406b5681
006B51C0  6A 6A                           push 0x6a
006B51C2  55                              push rbp
006B51C3  E9 B9 04 00 00                  jmp 0x1406b5681
006B51C8  6A 6B                           push 0x6b
006B51CA  55                              push rbp
006B51CB  E9 B1 04 00 00                  jmp 0x1406b5681
006B51D0  6A 6C                           push 0x6c
006B51D2  55                              push rbp
006B51D3  E9 A9 04 00 00                  jmp 0x1406b5681
006B51D8  6A 6D                           push 0x6d
006B51DA  55                              push rbp
006B51DB  E9 A1 04 00 00                  jmp 0x1406b5681
006B51E0  6A 6E                           push 0x6e
006B51E2  55                              push rbp
006B51E3  E9 99 04 00 00                  jmp 0x1406b5681
006B51E8  6A 6F                           push 0x6f
006B51EA  55                              push rbp
006B51EB  E9 91 04 00 00                  jmp 0x1406b5681
006B51F0  6A 70                           push 0x70
006B51F2  55                              push rbp
006B51F3  E9 89 04 00 00                  jmp 0x1406b5681
006B51F8  6A 71                           push 0x71
006B51FA  55                              push rbp
006B51FB  E9 81 04 00 00                  jmp 0x1406b5681
006B5200  6A 72                           push 0x72
006B5202  55                              push rbp
006B5203  E9 79 04 00 00                  jmp 0x1406b5681
006B5208  6A 73                           push 0x73
006B520A  55                              push rbp
006B520B  E9 71 04 00 00                  jmp 0x1406b5681
006B5210  6A 74                           push 0x74
006B5212  55                              push rbp
006B5213  E9 69 04 00 00                  jmp 0x1406b5681
006B5218  6A 75                           push 0x75
006B521A  55                              push rbp
006B521B  E9 61 04 00 00                  jmp 0x1406b5681
006B5220  6A 76                           push 0x76
006B5222  55                              push rbp
006B5223  E9 59 04 00 00                  jmp 0x1406b5681
006B5228  6A 77                           push 0x77
006B522A  55                              push rbp
006B522B  E9 51 04 00 00                  jmp 0x1406b5681
006B5230  6A 78                           push 0x78
006B5232  55                              push rbp
006B5233  E9 49 04 00 00                  jmp 0x1406b5681
006B5238  6A 79                           push 0x79
006B523A  55                              push rbp
006B523B  E9 41 04 00 00                  jmp 0x1406b5681
006B5240  6A 7A                           push 0x7a
006B5242  55                              push rbp
006B5243  E9 39 04 00 00                  jmp 0x1406b5681
006B5248  6A 7B                           push 0x7b
006B524A  55                              push rbp
006B524B  E9 31 04 00 00                  jmp 0x1406b5681
006B5250  6A 7C                           push 0x7c
006B5252  55                              push rbp
006B5253  E9 29 04 00 00                  jmp 0x1406b5681
006B5258  6A 7D                           push 0x7d
006B525A  55                              push rbp
006B525B  E9 21 04 00 00                  jmp 0x1406b5681
006B5260  6A 7E                           push 0x7e
006B5262  55                              push rbp
006B5263  E9 19 04 00 00                  jmp 0x1406b5681
006B5268  6A 7F                           push 0x7f
006B526A  55                              push rbp
006B526B  E9 11 04 00 00                  jmp 0x1406b5681
006B5270  6A 80                           push -0x80
006B5272  55                              push rbp
006B5273  E9 09 04 00 00                  jmp 0x1406b5681
006B5278  6A 81                           push -0x7f
006B527A  55                              push rbp
006B527B  E9 01 04 00 00                  jmp 0x1406b5681
006B5280  6A 82                           push -0x7e
006B5282  55                              push rbp
006B5283  E9 F9 03 00 00                  jmp 0x1406b5681
006B5288  6A 83                           push -0x7d
006B528A  55                              push rbp
006B528B  E9 F1 03 00 00                  jmp 0x1406b5681
006B5290  6A 84                           push -0x7c
006B5292  55                              push rbp
006B5293  E9 E9 03 00 00                  jmp 0x1406b5681
006B5298  6A 85                           push -0x7b
006B529A  55                              push rbp
006B529B  E9 E1 03 00 00                  jmp 0x1406b5681
006B52A0  6A 86                           push -0x7a
006B52A2  55                              push rbp
006B52A3  E9 D9 03 00 00                  jmp 0x1406b5681
006B52A8  6A 87                           push -0x79
006B52AA  55                              push rbp
006B52AB  E9 D1 03 00 00                  jmp 0x1406b5681
006B52B0  6A 88                           push -0x78
006B52B2  55                              push rbp
006B52B3  E9 C9 03 00 00                  jmp 0x1406b5681
006B52B8  6A 89                           push -0x77
006B52BA  55                              push rbp
006B52BB  E9 C1 03 00 00                  jmp 0x1406b5681
006B52C0  6A 8A                           push -0x76
006B52C2  55                              push rbp
006B52C3  E9 B9 03 00 00                  jmp 0x1406b5681
006B52C8  6A 8B                           push -0x75
006B52CA  55                              push rbp
006B52CB  E9 B1 03 00 00                  jmp 0x1406b5681
006B52D0  6A 8C                           push -0x74
006B52D2  55                              push rbp
006B52D3  E9 A9 03 00 00                  jmp 0x1406b5681
006B52D8  6A 8D                           push -0x73
006B52DA  55                              push rbp
006B52DB  E9 A1 03 00 00                  jmp 0x1406b5681
006B52E0  6A 8E                           push -0x72
006B52E2  55                              push rbp
006B52E3  E9 99 03 00 00                  jmp 0x1406b5681
006B52E8  6A 8F                           push -0x71
006B52EA  55                              push rbp
006B52EB  E9 91 03 00 00                  jmp 0x1406b5681
006B52F0  6A 90                           push -0x70
006B52F2  55                              push rbp
006B52F3  E9 89 03 00 00                  jmp 0x1406b5681
006B52F8  6A 91                           push -0x6f
006B52FA  55                              push rbp
006B52FB  E9 81 03 00 00                  jmp 0x1406b5681
006B5300  6A 92                           push -0x6e
006B5302  55                              push rbp
006B5303  E9 79 03 00 00                  jmp 0x1406b5681
006B5308  6A 93                           push -0x6d
006B530A  55                              push rbp
006B530B  E9 71 03 00 00                  jmp 0x1406b5681
006B5310  6A 94                           push -0x6c
006B5312  55                              push rbp
006B5313  E9 69 03 00 00                  jmp 0x1406b5681
006B5318  6A 95                           push -0x6b
006B531A  55                              push rbp
006B531B  E9 61 03 00 00                  jmp 0x1406b5681
006B5320  6A 96                           push -0x6a
006B5322  55                              push rbp
006B5323  E9 59 03 00 00                  jmp 0x1406b5681
006B5328  6A 97                           push -0x69
006B532A  55                              push rbp
006B532B  E9 51 03 00 00                  jmp 0x1406b5681
006B5330  6A 98                           push -0x68
006B5332  55                              push rbp
006B5333  E9 49 03 00 00                  jmp 0x1406b5681
006B5338  6A 99                           push -0x67
006B533A  55                              push rbp
006B533B  E9 41 03 00 00                  jmp 0x1406b5681
006B5340  6A 9A                           push -0x66
006B5342  55                              push rbp
006B5343  E9 39 03 00 00                  jmp 0x1406b5681
006B5348  6A 9B                           push -0x65
006B534A  55                              push rbp
006B534B  E9 31 03 00 00                  jmp 0x1406b5681
006B5350  6A 9C                           push -0x64
006B5352  55                              push rbp
006B5353  E9 29 03 00 00                  jmp 0x1406b5681
006B5358  6A 9D                           push -0x63
006B535A  55                              push rbp
006B535B  E9 21 03 00 00                  jmp 0x1406b5681
006B5360  6A 9E                           push -0x62
006B5362  55                              push rbp
006B5363  E9 19 03 00 00                  jmp 0x1406b5681
006B5368  6A 9F                           push -0x61
006B536A  55                              push rbp
006B536B  E9 11 03 00 00                  jmp 0x1406b5681
006B5370  6A A0                           push -0x60
006B5372  55                              push rbp
006B5373  E9 09 03 00 00                  jmp 0x1406b5681
006B5378  6A A1                           push -0x5f
006B537A  55                              push rbp
006B537B  E9 01 03 00 00                  jmp 0x1406b5681
006B5380  6A A2                           push -0x5e
006B5382  55                              push rbp
006B5383  E9 F9 02 00 00                  jmp 0x1406b5681
006B5388  6A A3                           push -0x5d
006B538A  55                              push rbp
006B538B  E9 F1 02 00 00                  jmp 0x1406b5681
006B5390  6A A4                           push -0x5c
006B5392  55                              push rbp
006B5393  E9 E9 02 00 00                  jmp 0x1406b5681
006B5398  6A A5                           push -0x5b
006B539A  55                              push rbp
006B539B  E9 E1 02 00 00                  jmp 0x1406b5681
006B53A0  6A A6                           push -0x5a
006B53A2  55                              push rbp
006B53A3  E9 D9 02 00 00                  jmp 0x1406b5681
006B53A8  6A A7                           push -0x59
006B53AA  55                              push rbp
006B53AB  E9 D1 02 00 00                  jmp 0x1406b5681
006B53B0  6A A8                           push -0x58
006B53B2  55                              push rbp
006B53B3  E9 C9 02 00 00                  jmp 0x1406b5681
006B53B8  6A A9                           push -0x57
006B53BA  55                              push rbp
006B53BB  E9 C1 02 00 00                  jmp 0x1406b5681
006B53C0  6A AA                           push -0x56
006B53C2  55                              push rbp
006B53C3  E9 B9 02 00 00                  jmp 0x1406b5681
006B53C8  6A AB                           push -0x55
006B53CA  55                              push rbp
006B53CB  E9 B1 02 00 00                  jmp 0x1406b5681
006B53D0  6A AC                           push -0x54
006B53D2  55                              push rbp
006B53D3  E9 A9 02 00 00                  jmp 0x1406b5681
006B53D8  6A AD                           push -0x53
006B53DA  55                              push rbp
006B53DB  E9 A1 02 00 00                  jmp 0x1406b5681
006B53E0  6A AE                           push -0x52
006B53E2  55                              push rbp
006B53E3  E9 99 02 00 00                  jmp 0x1406b5681
006B53E8  6A AF                           push -0x51
006B53EA  55                              push rbp
006B53EB  E9 91 02 00 00                  jmp 0x1406b5681
006B53F0  6A B0                           push -0x50
006B53F2  55                              push rbp
006B53F3  E9 89 02 00 00                  jmp 0x1406b5681
006B53F8  6A B1                           push -0x4f
006B53FA  55                              push rbp
006B53FB  E9 81 02 00 00                  jmp 0x1406b5681
006B5400  6A B2                           push -0x4e
006B5402  55                              push rbp
006B5403  E9 79 02 00 00                  jmp 0x1406b5681
006B5408  6A B3                           push -0x4d
006B540A  55                              push rbp
006B540B  E9 71 02 00 00                  jmp 0x1406b5681
006B5410  6A B4                           push -0x4c
006B5412  55                              push rbp
006B5413  E9 69 02 00 00                  jmp 0x1406b5681
006B5418  6A B5                           push -0x4b
006B541A  55                              push rbp
006B541B  E9 61 02 00 00                  jmp 0x1406b5681
006B5420  6A B6                           push -0x4a
006B5422  55                              push rbp
006B5423  E9 59 02 00 00                  jmp 0x1406b5681
006B5428  6A B7                           push -0x49
006B542A  55                              push rbp
006B542B  E9 51 02 00 00                  jmp 0x1406b5681
006B5430  6A B8                           push -0x48
006B5432  55                              push rbp
006B5433  E9 49 02 00 00                  jmp 0x1406b5681
006B5438  6A B9                           push -0x47
006B543A  55                              push rbp
006B543B  E9 41 02 00 00                  jmp 0x1406b5681
006B5440  6A BA                           push -0x46
006B5442  55                              push rbp
006B5443  E9 39 02 00 00                  jmp 0x1406b5681
006B5448  6A BB                           push -0x45
006B544A  55                              push rbp
006B544B  E9 31 02 00 00                  jmp 0x1406b5681
006B5450  6A BC                           push -0x44
006B5452  55                              push rbp
006B5453  E9 29 02 00 00                  jmp 0x1406b5681
006B5458  6A BD                           push -0x43
006B545A  55                              push rbp
006B545B  E9 21 02 00 00                  jmp 0x1406b5681
006B5460  6A BE                           push -0x42
006B5462  55                              push rbp
006B5463  E9 19 02 00 00                  jmp 0x1406b5681
006B5468  6A BF                           push -0x41
006B546A  55                              push rbp
006B546B  E9 11 02 00 00                  jmp 0x1406b5681
006B5470  6A C0                           push -0x40
006B5472  55                              push rbp
006B5473  E9 09 02 00 00                  jmp 0x1406b5681
006B5478  6A C1                           push -0x3f
006B547A  55                              push rbp
006B547B  E9 01 02 00 00                  jmp 0x1406b5681
006B5480  6A C2                           push -0x3e
006B5482  55                              push rbp
006B5483  E9 F9 01 00 00                  jmp 0x1406b5681
006B5488  6A C3                           push -0x3d
006B548A  55                              push rbp
006B548B  E9 F1 01 00 00                  jmp 0x1406b5681
006B5490  6A C4                           push -0x3c
006B5492  55                              push rbp
006B5493  E9 E9 01 00 00                  jmp 0x1406b5681
006B5498  6A C5                           push -0x3b
006B549A  55                              push rbp
006B549B  E9 E1 01 00 00                  jmp 0x1406b5681
006B54A0  6A C6                           push -0x3a
006B54A2  55                              push rbp
006B54A3  E9 D9 01 00 00                  jmp 0x1406b5681
006B54A8  6A C7                           push -0x39
006B54AA  55                              push rbp
006B54AB  E9 D1 01 00 00                  jmp 0x1406b5681
006B54B0  6A C8                           push -0x38
006B54B2  55                              push rbp
006B54B3  E9 C9 01 00 00                  jmp 0x1406b5681
006B54B8  6A C9                           push -0x37
006B54BA  55                              push rbp
006B54BB  E9 C1 01 00 00                  jmp 0x1406b5681
006B54C0  6A CA                           push -0x36
006B54C2  55                              push rbp
006B54C3  E9 B9 01 00 00                  jmp 0x1406b5681
006B54C8  6A CB                           push -0x35
006B54CA  55                              push rbp
006B54CB  E9 B1 01 00 00                  jmp 0x1406b5681
006B54D0  6A CC                           push -0x34
006B54D2  55                              push rbp
006B54D3  E9 A9 01 00 00                  jmp 0x1406b5681
006B54D8  6A CD                           push -0x33
006B54DA  55                              push rbp
006B54DB  E9 A1 01 00 00                  jmp 0x1406b5681
006B54E0  6A CE                           push -0x32
006B54E2  55                              push rbp
006B54E3  E9 99 01 00 00                  jmp 0x1406b5681
006B54E8  6A CF                           push -0x31
006B54EA  55                              push rbp
006B54EB  E9 91 01 00 00                  jmp 0x1406b5681
006B54F0  6A D0                           push -0x30
006B54F2  55                              push rbp
006B54F3  E9 89 01 00 00                  jmp 0x1406b5681
006B54F8  6A D1                           push -0x2f
006B54FA  55                              push rbp
006B54FB  E9 81 01 00 00                  jmp 0x1406b5681
006B5500  6A D2                           push -0x2e
006B5502  55                              push rbp
006B5503  E9 79 01 00 00                  jmp 0x1406b5681
006B5508  6A D3                           push -0x2d
006B550A  55                              push rbp
006B550B  E9 71 01 00 00                  jmp 0x1406b5681
006B5510  6A D4                           push -0x2c
006B5512  55                              push rbp
006B5513  E9 69 01 00 00                  jmp 0x1406b5681
006B5518  6A D5                           push -0x2b
006B551A  55                              push rbp
006B551B  E9 61 01 00 00                  jmp 0x1406b5681
006B5520  6A D6                           push -0x2a
006B5522  55                              push rbp
006B5523  E9 59 01 00 00                  jmp 0x1406b5681
006B5528  6A D7                           push -0x29
006B552A  55                              push rbp
006B552B  E9 51 01 00 00                  jmp 0x1406b5681
006B5530  6A D8                           push -0x28
006B5532  55                              push rbp
006B5533  E9 49 01 00 00                  jmp 0x1406b5681
006B5538  6A D9                           push -0x27
006B553A  55                              push rbp
006B553B  E9 41 01 00 00                  jmp 0x1406b5681
006B5540  6A DA                           push -0x26
006B5542  55                              push rbp
006B5543  E9 39 01 00 00                  jmp 0x1406b5681
006B5548  6A DB                           push -0x25
006B554A  55                              push rbp
006B554B  E9 31 01 00 00                  jmp 0x1406b5681
006B5550  6A DC                           push -0x24
006B5552  55                              push rbp
006B5553  E9 29 01 00 00                  jmp 0x1406b5681
006B5558  6A DD                           push -0x23
006B555A  55                              push rbp
006B555B  E9 21 01 00 00                  jmp 0x1406b5681
006B5560  6A DE                           push -0x22
006B5562  55                              push rbp
006B5563  E9 19 01 00 00                  jmp 0x1406b5681
006B5568  6A DF                           push -0x21
006B556A  55                              push rbp
006B556B  E9 11 01 00 00                  jmp 0x1406b5681
006B5570  6A E0                           push -0x20
006B5572  55                              push rbp
006B5573  E9 09 01 00 00                  jmp 0x1406b5681
006B5578  6A E1                           push -0x1f
006B557A  55                              push rbp
006B557B  E9 01 01 00 00                  jmp 0x1406b5681
006B5580  6A E2                           push -0x1e
006B5582  55                              push rbp
006B5583  E9 F9 00 00 00                  jmp 0x1406b5681
006B5588  6A E3                           push -0x1d
006B558A  55                              push rbp
006B558B  E9 F1 00 00 00                  jmp 0x1406b5681
006B5590  6A E4                           push -0x1c
006B5592  55                              push rbp
006B5593  E9 E9 00 00 00                  jmp 0x1406b5681
006B5598  6A E5                           push -0x1b
006B559A  55                              push rbp
006B559B  E9 E1 00 00 00                  jmp 0x1406b5681
006B55A0  6A E6                           push -0x1a
006B55A2  55                              push rbp
006B55A3  E9 D9 00 00 00                  jmp 0x1406b5681
006B55A8  6A E7                           push -0x19
006B55AA  55                              push rbp
006B55AB  E9 D1 00 00 00                  jmp 0x1406b5681
006B55B0  6A E8                           push -0x18
006B55B2  55                              push rbp
006B55B3  E9 C9 00 00 00                  jmp 0x1406b5681
006B55B8  6A E9                           push -0x17
006B55BA  55                              push rbp
006B55BB  E9 C1 00 00 00                  jmp 0x1406b5681
006B55C0  6A EA                           push -0x16
006B55C2  55                              push rbp
006B55C3  E9 B9 00 00 00                  jmp 0x1406b5681
006B55C8  6A EB                           push -0x15
006B55CA  55                              push rbp
006B55CB  E9 B1 00 00 00                  jmp 0x1406b5681
006B55D0  6A EC                           push -0x14
006B55D2  55                              push rbp
006B55D3  E9 A9 00 00 00                  jmp 0x1406b5681
006B55D8  6A ED                           push -0x13
006B55DA  55                              push rbp
006B55DB  E9 A1 00 00 00                  jmp 0x1406b5681
006B55E0  6A EE                           push -0x12
006B55E2  55                              push rbp
006B55E3  E9 99 00 00 00                  jmp 0x1406b5681
006B55E8  6A EF                           push -0x11
006B55EA  55                              push rbp
006B55EB  E9 91 00 00 00                  jmp 0x1406b5681
006B55F0  6A F0                           push -0x10
006B55F2  55                              push rbp
006B55F3  E9 89 00 00 00                  jmp 0x1406b5681
006B55F8  6A F1                           push -0xf
006B55FA  55                              push rbp
006B55FB  E9 81 00 00 00                  jmp 0x1406b5681
006B5600  6A F2                           push -0xe
006B5602  55                              push rbp
006B5603  E9 79 00 00 00                  jmp 0x1406b5681
006B5608  6A F3                           push -0xd
006B560A  55                              push rbp
006B560B  E9 71 00 00 00                  jmp 0x1406b5681
006B5610  6A F4                           push -0xc
006B5612  55                              push rbp
006B5613  E9 69 00 00 00                  jmp 0x1406b5681
006B5618  6A F5                           push -0xb
006B561A  55                              push rbp
006B561B  E9 61 00 00 00                  jmp 0x1406b5681
006B5620  6A F6                           push -0xa
006B5622  55                              push rbp
006B5623  E9 59 00 00 00                  jmp 0x1406b5681
006B5628  6A F7                           push -9
006B562A  55                              push rbp
006B562B  E9 51 00 00 00                  jmp 0x1406b5681
006B5630  6A F8                           push -8
006B5632  55                              push rbp
006B5633  E9 49 00 00 00                  jmp 0x1406b5681
006B5638  6A F9                           push -7
006B563A  55                              push rbp
006B563B  E9 41 00 00 00                  jmp 0x1406b5681
006B5640  6A FA                           push -6
006B5642  55                              push rbp
006B5643  E9 39 00 00 00                  jmp 0x1406b5681
006B5648  6A FB                           push -5
006B564A  55                              push rbp
006B564B  E9 31 00 00 00                  jmp 0x1406b5681
006B5650  6A FC                           push -4
006B5652  55                              push rbp
006B5653  E9 29 00 00 00                  jmp 0x1406b5681
006B5658  6A FD                           push -3
006B565A  55                              push rbp
006B565B  E9 21 00 00 00                  jmp 0x1406b5681
006B5660  6A FE                           push -2
006B5662  55                              push rbp
006B5663  E9 19 00 00 00                  jmp 0x1406b5681
006B5668  6A FF                           push -1
006B566A  55                              push rbp
006B566B  E9 11 00 00 00                  jmp 0x1406b5681
006B5670  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiIsrThunk(void)
{
}
```

## 5. (Beta) C Style

```c
void KiIsrThunk(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B4E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
