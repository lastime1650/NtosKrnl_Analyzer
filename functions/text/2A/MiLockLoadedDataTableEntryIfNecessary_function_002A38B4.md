# MiLockLoadedDataTableEntryIfNecessary

- RVA: `0x002A38B4`–`0x002A38EB` (길이 `55` bytes)
- VA: `0x00000001402A38B4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `15`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002A38D6` → [MiLockLoadedDataTableEntry](MiLockLoadedDataTableEntry_function_002A38F4.md) (function, `0x002A38F4`)
- `0x002A38E4` → [MmFindDataTableEntryByAddress](MmFindDataTableEntryByAddress_function_002A3C0C.md) (function, `0x002A3C0C`)

### Direct callers
- [MmProtectDriverSection](../67/MmProtectDriverSection_function_00670A80.md) at `0x00670B2D`
- [FsRtlSetDriverBacking](../../page/71/FsRtlSetDriverBacking_function_00716310.md) at `0x00716336`
- [MmResetDriverPaging](../../page/A4/MmResetDriverPaging_function_00A4ADB0.md) at `0x00A4ADDC`
- [MmPageEntireDriver](../../page/A4/MmPageEntireDriver_function_00A4BBB0.md) at `0x00A4BBDC`
- [MmLockPagableSectionByHandle](../../page/A4/MmLockPagableSectionByHandle_function_00A4D1E0.md) at `0x00A4D209`
- [MmChangeImageProtection](../../page/A5/MmChangeImageProtection_function_00A565F0.md) at `0x00A56668`
- [MmLockPagableDataSection](../../page/A7/MmLockPagableDataSection_function_00A73E80.md) at `0x00A73EB0`
- [MmIsDriverVerifyingByAddress](../../pagevrfy/BB/MmIsDriverVerifyingByAddress_function_00BB6320.md) at `0x00BB6344`

### Static image references
- `0x002A38C1` → RVA `0x00E2D910` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A38B4  48 83 EC 28                     sub rsp, 0x28
002A38B8  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
002A38C1  48 8B 05 48 A0 B8 00            mov rax, qword ptr [rip + 0xb8a048]
002A38C8  49 3B C0                        cmp rax, r8
002A38CB  74 14                           je 0x1402a38e1
002A38CD  B8 01 00 00 00                  mov eax, 1
002A38D2  89 02                           mov dword ptr [rdx], eax
002A38D4  8B D0                           mov edx, eax
002A38D6  E8 19 00 00 00                  call 0x1402a38f4
002A38DB  48 83 C4 28                     add rsp, 0x28
002A38DF  C3                              ret
002A38E0  CC                              int3
002A38E1  83 22 00                        and dword ptr [rdx], 0
002A38E4  E8 23 03 00 00                  call 0x1402a3c0c
002A38E9  EB F0                           jmp 0x1402a38db
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockLoadedDataTableEntryIfNecessary(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int64 *)(v_rip + 12099656)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_002A38E1;
    *(unsigned int *)(a2) = 1;
    result = MiLockLoadedDataTableEntry(a1, 1, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
loc_002A38DB:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A38E1:
    result = MmFindDataTableEntryByAddress(a1, 1, *(unsigned __int64 *)(gs_base + (0 + 392)), a4);
    goto loc_002A38DB;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockLoadedDataTableEntryIfNecessary(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint64_t *)(v_rip + 0xB8A048)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_002A38E1;
    *(uint32_t *)(arg2) = 1;
    result = MiLockLoadedDataTableEntry(Arg1, 1, *(uint64_t *)(gs_base + (0 + 0x188)), a4);
loc_002A38DB:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A38E1:
    result = MmFindDataTableEntryByAddress(Arg1, 1, *(uint64_t *)(gs_base + (0 + 0x188)), a4);
    goto loc_002A38DB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A38B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A38B4[BB_002A38B4]
  bb_002A38CD[BB_002A38CD]
  bb_002A38DB[BB_002A38DB]
  bb_002A38E0[BB_002A38E0]
  bb_002A38E1[BB_002A38E1]
  bb_002A38B4 -->|branch| bb_002A38E1
  bb_002A38B4 -->|fallthrough| bb_002A38CD
  bb_002A38CD -->|flow| bb_002A38DB
  bb_002A38E0 -->|flow| bb_002A38E1
  bb_002A38E1 -->|branch| bb_002A38DB
```
