# ExpStringFree

- RVA: `0x00702EE8`–`0x00702F01` (길이 `25` bytes)
- VA: `0x0000000140702EE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00702EF6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExpGetDeviceDataInformation](../95/ExpGetDeviceDataInformation_function_0095A300.md) at `0x0095A4A7`
- [ExpGetDeviceDataInformation](../95/ExpGetDeviceDataInformation_function_0095A300.md) at `0x0095A4B4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00702EF6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00702EE8  48 83 EC 28                     sub rsp, 0x28
00702EEC  48 85 C9                        test rcx, rcx
00702EEF  74 0A                           je 0x140702efb
00702EF1  BA 45 58 53 50                  mov edx, 0x50535845
00702EF6  E8 75 F9 47 00                  call 0x140b82870
00702EFB  48 83 C4 28                     add rsp, 0x28
00702EFF  C3                              ret
00702F00  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpStringFree(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) {
        a2 = 0x50535845ULL;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpStringFree(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) {
        a2 = 0x50535845ULL;
        result = ExFreePoolWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00702EE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00702EE8[BB_00702EE8]
  bb_00702EF1[BB_00702EF1]
  bb_00702EFB[BB_00702EFB]
  bb_00702F00[BB_00702F00]
  bb_00702EE8 -->|branch| bb_00702EFB
  bb_00702EE8 -->|fallthrough| bb_00702EF1
  bb_00702EF1 -->|flow| bb_00702EFB
```
