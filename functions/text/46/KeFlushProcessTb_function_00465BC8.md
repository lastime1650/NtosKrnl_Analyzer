# KeFlushProcessTb

- RVA: `0x00465BC8`–`0x00465BF2` (길이 `42` bytes)
- VA: `0x0000000140465BC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068370`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00465BEB` → [KiFlushAddressSpaceTb](../30/KiFlushAddressSpaceTb_function_00308F50.md) (function, `0x00308F50`)

### Direct callers
- [KeSwapDirectoryTableBase](KeSwapDirectoryTableBase_function_0046590C.md) at `0x00465977`
- [MiDeleteFinalPageTables](MiDeleteFinalPageTables_function_004659AC.md) at `0x00465B10`
- [MiDeleteProcessShadow](MiDeleteProcessShadow_function_00465BF8.md) at `0x00465D3B`
- [sub_006E82CE](../6E/Unknown_function_006E82CE.md) at `0x006E83A4`
- [sub_006E82CE](../6E/Unknown_function_006E82CE.md) at `0x006E83B9`

### Static image references
- `0x00465BCC` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00465BC8  48 83 EC 28                     sub rsp, 0x28
00465BCC  8B 05 E6 0E B6 00               mov eax, dword ptr [rip + 0xb60ee6]
00465BD2  A8 01                           test al, 1
00465BD4  75 06                           jne 0x140465bdc
00465BD6  48 83 C4 28                     add rsp, 0x28
00465BDA  C3                              ret
00465BDB  CC                              int3
00465BDC  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00465BE3  45 33 C9                        xor r9d, r9d
00465BE6  45 33 C0                        xor r8d, r8d
00465BE9  33 D2                           xor edx, edx
00465BEB  E8 60 33 EA FF                  call 0x140308f50
00465BF0  EB E4                           jmp 0x140465bd6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeFlushProcessTb(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11931366)))) & (1)) != 0) goto loc_00465BDC;
loc_00465BD6:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(v_rip + 11931366));
loc_00465BDC:
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KiFlushAddressSpaceTb(a1, a2, a3, a4);
    goto loc_00465BD6;
}
```

## 5. (Beta) C Style

```c
int64_t KeFlushProcessTb(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB60EE6)))) & (1)) != 0) goto loc_00465BDC;
loc_00465BD6:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB60EE6));
loc_00465BDC:
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KiFlushAddressSpaceTb(Arg1, Arg2, Arg3, Arg4);
    goto loc_00465BD6;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00465BC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00465BC8[BB_00465BC8]
  bb_00465BD6[BB_00465BD6]
  bb_00465BDB[BB_00465BDB]
  bb_00465BDC[BB_00465BDC]
  bb_00465BC8 -->|branch| bb_00465BDC
  bb_00465BC8 -->|fallthrough| bb_00465BD6
  bb_00465BDB -->|flow| bb_00465BDC
  bb_00465BDC -->|branch| bb_00465BD6
```
