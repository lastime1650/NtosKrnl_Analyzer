# IpmiHwContextInitialized

- RVA: `0x006A64DC`–`0x006A64F0` (길이 `20` bytes)
- VA: `0x00000001406A64DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeBugCheck2](../5B/KeBugCheck2_function_005B27D0.md) at `0x005B30F3`
- [WheaSelLogError](../65/WheaSelLogError_function_0065D8A8.md) at `0x0065D918`
- [WheapSelLogSetNtSchedulerAvailabilityNoLock](../65/WheapSelLogSetNtSchedulerAvailabilityNoLock_function_0065DBB4.md) at `0x0065DBBF`
- [IpmiHwInitializeContext](IpmiHwInitializeContext_function_006A64F8.md) at `0x006A6508`
- [IpmiHwInitializeContext](IpmiHwInitializeContext_function_006A64F8.md) at `0x006A65B7`
- [IpmiLibAddSelBugcheckRecord](IpmiLibAddSelBugcheckRecord_function_006A6A40.md) at `0x006A6A7F`
- [IpmiLibAddSelCheckpointRecord](IpmiLibAddSelCheckpointRecord_function_006A6B7C.md) at `0x006A6B9B`
- [IpmiLibAddSelErrorRecord](IpmiLibAddSelErrorRecord_function_006A6BEC.md) at `0x006A6C0B`
- [IpmiLibpAddSelRawData](IpmiLibpAddSelRawData_function_006A6D10.md) at `0x006A6D4A`
- [WheaQuerySystemInformation](../../page/7D/WheaQuerySystemInformation_function_007D67A0.md) at `0x007D67B1`
- [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) at `0x007D6870`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A64DC  33 D2                           xor edx, edx
006A64DE  48 85 C9                        test rcx, rcx
006A64E1  74 09                           je 0x1406a64ec
006A64E3  33 C0                           xor eax, eax
006A64E5  F0 0F B0 51 58                  lock cmpxchg byte ptr [rcx + 0x58], dl
006A64EA  C3                              ret
006A64EB  CC                              int3
006A64EC  32 C0                           xor al, al
006A64EE  C3                              ret
006A64EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IpmiHwContextInitialized(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    if (a1 == 0) goto loc_006A64EC;
    result = 0;
    return result;
loc_006A64EC:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IpmiHwContextInitialized(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    if (Arg1 == 0) goto loc_006A64EC;
    result = 0;
    return result;
loc_006A64EC:
    result = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A64DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A64DC[BB_006A64DC]
  bb_006A64E3[BB_006A64E3]
  bb_006A64EB[BB_006A64EB]
  bb_006A64EC[BB_006A64EC]
  bb_006A64EF[BB_006A64EF]
  bb_006A64DC -->|branch| bb_006A64EC
  bb_006A64DC -->|fallthrough| bb_006A64E3
  bb_006A64EB -->|flow| bb_006A64EC
```
