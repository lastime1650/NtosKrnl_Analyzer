# MiConvertHiberPhasePages

- RVA: `0x00B73E24`–`0x00B73EAD` (길이 `137` bytes)
- VA: `0x0000000140B73E24`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B78D0`
- 디코드: `29`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B73E3D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B73E5E` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)
- `0x00B73E8F` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x00B73E9E` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (function, `0x00314110`)

### Direct callers
- [PopMarkComponentsBootPhase](../B6/PopMarkComponentsBootPhase_function_00B6E0E4.md) at `0x00B6E437`
- [PopInvokeSystemStateHandler](PopInvokeSystemStateHandler_function_00B76A6C.md) at `0x00B76F5A`

### Static image references
- `0x00B73E42` → RVA `0x00B79520` (`MiConvertHiberPhasePte`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00B73E3D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGELK` → `.text`)
  - `0x00B73E5E` → [MiGetAnyMultiplexedVm](../../text/44/MiGetAnyMultiplexedVm_function_00448BD0.md) (`PAGELK` → `.text`)
  - `0x00B73E8F` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (`PAGELK` → `.text`)
  - `0x00B73E9E` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B73E24  40 53                           push rbx
00B73E26  48 81 EC E0 00 00 00            sub rsp, 0xe0
00B73E2D  48 8B D9                        mov rbx, rcx
00B73E30  33 D2                           xor edx, edx
00B73E32  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B73E37  41 B8 C0 00 00 00               mov r8d, 0xc0
00B73E3D  E8 FE 2D B5 FF                  call 0x1406c6c40
00B73E42  48 8D 05 D7 56 00 00            lea rax, [rip + 0x56d7]
00B73E49  C7 44 24 20 01 23 00 00         mov dword ptr [rsp + 0x20], 0x2301
00B73E51  B9 04 00 00 00                  mov ecx, 4
00B73E56  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00B73E5E  E8 6D 4D 8D FF                  call 0x140448bd0
00B73E63  48 83 4C 24 50 FF               or qword ptr [rsp + 0x50], 0xffffffffffffffff
00B73E69  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00B73E6E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B73E73  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00B73E7D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B73E82  C6 44 24 29 11                  mov byte ptr [rsp + 0x29], 0x11
00B73E87  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
00B73E8F  E8 7C E8 74 FF                  call 0x1402c2710
00B73E94  48 85 DB                        test rbx, rbx
00B73E97  74 0A                           je 0x140b73ea3
00B73E99  83 CA FF                        or edx, 0xffffffff
00B73E9C  33 C9                           xor ecx, ecx
00B73E9E  E8 6D 02 7A FF                  call 0x140314110
00B73EA3  48 81 C4 E0 00 00 00            add rsp, 0xe0
00B73EAA  5B                              pop rbx
00B73EAB  C3                              ret
00B73EAC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiConvertHiberPhasePages(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mBF;
    unsigned __int64 v_stack_mC8;

    v_rsp = (v_rsp) - (224);
    a2 = 0;
    result = memset(v_stack_mC8, a2, 192, a4);
    v_stack_mC8 = 0x2301ULL;
    v_stack_m20 = v_rip + 22231;
    result = MiGetAnyMultiplexedVm(4, a2, 192, a4);
    v_stack_mA8 = result;
    v_stack_mA0 = result;
    v_stack_mBF = 17;
    v_stack_m10 = a1;
    result = MiWalkPageTables(v_stack_mC8, a2, 192, a4);
    if (a1 != 0) {
        a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
        a1 = 0;
        result = MI_FLUSH_ENTIRE_TB(a1, a2, 192, a4);
    }
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiConvertHiberPhasePages(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m20;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mBF;
    uint64_t v_stack_mC8;

    local_rsp = (local_rsp) - (224);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 192, a4);
    v_stack_mC8 = 0x2301ULL;
    v_stack_m20 = v_rip + 22231;
    result = MiGetAnyMultiplexedVm(4, Arg2, 192, a4);
    v_stack_mA8 = result;
    v_stack_mA0 = result;
    v_stack_mBF = 17;
    v_stack_m10 = Arg1;
    result = MiWalkPageTables(v_stack_mC8, Arg2, 192, a4);
    if (Arg1 != 0) {
        Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
        Arg1 = 0;
        result = MI_FLUSH_ENTIRE_TB(Arg1, Arg2, 192, a4);
    }
    local_rsp = (local_rsp) + (224);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B73E24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B73E24[BB_00B73E24]
  bb_00B73E99[BB_00B73E99]
  bb_00B73EA3[BB_00B73EA3]
  bb_00B73EAC[BB_00B73EAC]
  bb_00B73E24 -->|branch| bb_00B73EA3
  bb_00B73E24 -->|fallthrough| bb_00B73E99
  bb_00B73E99 -->|flow| bb_00B73EA3
```
