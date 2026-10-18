# MmUnlockLoadedDataTableEntry

- RVA: `0x002A3C98`–`0x002A3CC9` (길이 `49` bytes)
- VA: `0x00000001402A3C98`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `13`개 명령, `49/49` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A3C9E` → [MiUnlockLoaderEntry](MiUnlockLoaderEntry_function_002A3E28.md) (function, `0x002A3E28`)
- `0x002A3CB3` → [MiReleaseLoadLock](MiReleaseLoadLock_function_002A3CD0.md) (function, `0x002A3CD0`)

### Direct callers
- [KeSetTracepoint](../../page/74/KeSetTracepoint_function_00747F80.md) at `0x0074859F`
- [MmGetSectionRange](../../page/7F/MmGetSectionRange_function_007F9408.md) at `0x007F949A`
- [MmCompactServiceTable](../../page/80/MmCompactServiceTable_function_0080C7E8.md) at `0x0080C813`
- [MiLogPinDriverAddress](../../page/A4/MiLogPinDriverAddress_function_00A442B4.md) at `0x00A444DA`
- [MmResetDriverPaging](../../page/A4/MmResetDriverPaging_function_00A4ADB0.md) at `0x00A4AE14`
- [MmPageEntireDriver](../../page/A4/MmPageEntireDriver_function_00A4BBB0.md) at `0x00A4BC51`
- [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) at `0x00A4D231`
- [MmChangeImageProtection](../../page/A5/MmChangeImageProtection_function_00A565F0.md) at `0x00A566EA`
- [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) at `0x00A73F1E`
- [MmIsDriverVerifyingByAddress](../../pagevrfy/BB/MmIsDriverVerifyingByAddress_function_00BB6320.md) at `0x00BB6369`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A3C98  48 83 EC 28                     sub rsp, 0x28
002A3C9C  33 D2                           xor edx, edx
002A3C9E  E8 85 01 00 00                  call 0x1402a3e28
002A3CA3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002A3CAC  48 85 C9                        test rcx, rcx
002A3CAF  74 0D                           je 0x1402a3cbe
002A3CB1  33 D2                           xor edx, edx
002A3CB3  E8 18 00 00 00                  call 0x1402a3cd0
002A3CB8  48 83 C4 28                     add rsp, 0x28
002A3CBC  C3                              ret
002A3CBD  CC                              int3
002A3CBE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002A3CC7  EB E8                           jmp 0x1402a3cb1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmUnlockLoadedDataTableEntry(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = MiUnlockLoaderEntry(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_002A3CBE;
loc_002A3CB1:
    a2 = 0;
    result = MiReleaseLoadLock(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A3CBE:
    goto loc_002A3CB1;
}
```

## 5. (Beta) C Style

```c
int64_t MmUnlockLoadedDataTableEntry(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = MiUnlockLoaderEntry(Arg1, Arg2, a3, a4);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_002A3CBE;
loc_002A3CB1:
    Arg2 = 0;
    result = MiReleaseLoadLock(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A3CBE:
    goto loc_002A3CB1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A3C98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A3C98[BB_002A3C98]
  bb_002A3CB1[BB_002A3CB1]
  bb_002A3CBD[BB_002A3CBD]
  bb_002A3CBE[BB_002A3CBE]
  bb_002A3C98 -->|branch| bb_002A3CBE
  bb_002A3C98 -->|fallthrough| bb_002A3CB1
  bb_002A3CBD -->|flow| bb_002A3CBE
  bb_002A3CBE -->|branch| bb_002A3CB1
```
