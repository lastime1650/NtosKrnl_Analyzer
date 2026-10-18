# ExtEnvFreeMemory

- RVA: `0x00561320`–`0x00561357` (길이 `55` bytes)
- VA: `0x0000000140561320`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00085914`
- 디코드: `16`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00561339` → [HalpMmIsInsideHalVa](../54/HalpMmIsInsideHalVa_function_00544BE0.md) (function, `0x00544BE0`)
- `0x0056134C` → [HalpMmAllocCtxFree](../3E/HalpMmAllocCtxFree_function_003E1904.md) (function, `0x003E1904`)

### Direct callers
- [IvtFreeScalableModePasidTables](IvtFreeScalableModePasidTables_function_0056F980.md) at `0x0056FAAE`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x00573AE4`
- [HsaAllocateRemappingTableEntry](../57/HsaAllocateRemappingTableEntry_function_00573820.md) at `0x00573AF1`
- [HsaCreateDevice](../57/HsaCreateDevice_function_00573B50.md) at `0x00573C41`
- [HsaCreateDevice](../57/HsaCreateDevice_function_00573B50.md) at `0x00573C49`
- [HsaDeleteDevice](../57/HsaDeleteDevice_function_00573C70.md) at `0x00573C8B`
- [HsaDeleteDevice](../57/HsaDeleteDevice_function_00573C70.md) at `0x00573C93`
- [HsaFreePasidTables](../57/HsaFreePasidTables_function_0057401C.md) at `0x005740E5`
- [HsaFreePasidTables](../57/HsaFreePasidTables_function_0057401C.md) at `0x005740FB`
- [HsaFreePasidTables](../57/HsaFreePasidTables_function_0057401C.md) at `0x0057410F`
- [HsaFreeRemappingTableEntry](../57/HsaFreeRemappingTableEntry_function_00574140.md) at `0x00574258`
- [HalpIvtLegacyProcessDrhdEntry](../57/HalpIvtLegacyProcessDrhdEntry_function_00578C58.md) at `0x005793C7`
- [HalpIvtProcessDrhdEntry](../57/HalpIvtProcessDrhdEntry_function_005794B4.md) at `0x00579CB2`
- [IvtAllocateDevice](../57/IvtAllocateDevice_function_00579D24.md) at `0x00579DA6`
- [IvtAllocateDevice](../57/IvtAllocateDevice_function_00579D24.md) at `0x00579DAE`
- [IvtCreateDevice](../57/IvtCreateDevice_function_00579DE0.md) at `0x00579EA6`
- [IvtCreateDevice](../57/IvtCreateDevice_function_00579DE0.md) at `0x00579EAE`
- [IvtDeleteDevice](../57/IvtDeleteDevice_function_00579ED0.md) at `0x00579EF0`
- [IvtDeleteDevice](../57/IvtDeleteDevice_function_00579ED0.md) at `0x00579EF8`
- [HalpIvtCreateReservedDevice](../57/HalpIvtCreateReservedDevice_function_0057A024.md) at `0x0057A0E5`
- [HalpIvtCreateReservedDevice](../57/HalpIvtCreateReservedDevice_function_0057A024.md) at `0x0057A0F1`
- [DmrFreeRmrrTree](../57/DmrFreeRmrrTree_function_0057AD18.md) at `0x0057AD6B`
- [DmrFreeRmrrTree](../57/DmrFreeRmrrTree_function_0057AD18.md) at `0x0057AD75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00561320  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00561325  48 83 EC 28                     sub rsp, 0x28
00561329  4C 8B D2                        mov r10, rdx
0056132C  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00561331  49 8B CA                        mov rcx, r10
00561334  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00561339  E8 A2 38 FE FF                  call 0x140544be0
0056133E  85 C0                           test eax, eax
00561340  78 0F                           js 0x140561351
00561342  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00561347  75 08                           jne 0x140561351
00561349  49 8B D2                        mov rdx, r10
0056134C  E8 B3 05 E8 FF                  call 0x1403e1904
00561351  48 83 C4 28                     add rsp, 0x28
00561355  C3                              ret
00561356  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExtEnvFreeMemory(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (40);
    v_stack_p8 = 0;
    result = HalpMmIsInsideHalVa(a2, v_stack_p8, a3, a4);
    if (sign_flag) goto loc_00561351;
    if (v_stack_p8 == 0) {
        a2 = a2;
        result = HalpMmAllocCtxFree(a2, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExtEnvFreeMemory(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (40);
    v_stack_p8 = 0;
    result = HalpMmIsInsideHalVa(Arg2, v_stack_p8, a3, a4);
    if (sign_flag) goto loc_00561351;
    if (v_stack_p8 == 0) {
        Arg2 = Arg2;
        result = HalpMmAllocCtxFree(Arg2, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00561320&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00561320[BB_00561320]
  bb_00561342[BB_00561342]
  bb_00561349[BB_00561349]
  bb_00561351[BB_00561351]
  bb_00561356[BB_00561356]
  bb_00561320 -->|branch| bb_00561351
  bb_00561320 -->|fallthrough| bb_00561342
  bb_00561342 -->|branch| bb_00561351
  bb_00561342 -->|fallthrough| bb_00561349
  bb_00561349 -->|flow| bb_00561351
```
