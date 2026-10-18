# MiDecommitSystemPageTables

- RVA: `0x002C1054`–`0x002C1107` (길이 `179` bytes)
- VA: `0x00000001402C1054`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E698`
- 디코드: `46`개 명령, `179/179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C10C5` → [MiSystemVaTypeToVm](../28/MiSystemVaTypeToVm_function_0028EB50.md) (function, `0x0028EB50`)
- `0x002C10E6` → [MiDeleteSystemPageTables](MiDeleteSystemPageTables_function_002C1110.md) (function, `0x002C1110`)
- `0x002C10FD` → [MiGetAnyMultiplexedVm](../44/MiGetAnyMultiplexedVm_function_00448BD0.md) (function, `0x00448BD0`)

### Direct callers
- [MiReturnSystemVa](../23/MiReturnSystemVa_function_002394C4.md) at `0x00239546`
- [MiReleaseDriverPtes](../../page/A7/MiReleaseDriverPtes_function_00A7F1B4.md) at `0x00A7F3B8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C1054  40 53                           push rbx
002C1056  48 83 EC 30                     sub rsp, 0x30
002C105A  4C 8B D1                        mov r10, rcx
002C105D  45 8B D8                        mov r11d, r8d
002C1060  49 C1 EA 09                     shr r10, 9
002C1064  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
002C106E  4C 23 D1                        and r10, rcx
002C1071  4C 8B CA                        mov r9, rdx
002C1074  48 B8 FF 0F 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000fff
002C107E  49 C1 E9 09                     shr r9, 9
002C1082  4C 03 D0                        add r10, rax
002C1085  48 C7 C2 00 F0 FF FF            mov rdx, 0xfffffffffffff000
002C108C  4C 23 C9                        and r9, rcx
002C108F  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
002C1099  4C 23 D2                        and r10, rdx
002C109C  48 8B C1                        mov rax, rcx
002C109F  4C 03 C8                        add r9, rax
002C10A2  4C 23 CA                        and r9, rdx
002C10A5  48 8B C1                        mov rax, rcx
002C10A8  48 C1 E0 19                     shl rax, 0x19
002C10AC  41 8B C8                        mov ecx, r8d
002C10AF  49 C1 E2 19                     shl r10, 0x19
002C10B3  49 C1 E1 19                     shl r9, 0x19
002C10B7  4C 2B D0                        sub r10, rax
002C10BA  4C 2B C8                        sub r9, rax
002C10BD  49 C1 FA 10                     sar r10, 0x10
002C10C1  49 C1 F9 10                     sar r9, 0x10
002C10C5  E8 86 DA FC FF                  call 0x14028eb50
002C10CA  48 8B D8                        mov rbx, rax
002C10CD  48 85 C0                        test rax, rax
002C10D0  74 26                           je 0x1402c10f8
002C10D2  49 FF C9                        dec r9
002C10D5  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
002C10DD  4D 8B C2                        mov r8, r10
002C10E0  41 8B D3                        mov edx, r11d
002C10E3  48 8B CB                        mov rcx, rbx
002C10E6  E8 25 00 00 00                  call 0x1402c1110
002C10EB  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
002C10F1  48 83 C4 30                     add rsp, 0x30
002C10F5  5B                              pop rbx
002C10F6  C3                              ret
002C10F7  CC                              int3
002C10F8  B9 06 00 00 00                  mov ecx, 6
002C10FD  E8 CE 7A 18 00                  call 0x140448bd0
002C1102  48 8B D8                        mov rbx, rax
002C1105  EB CB                           jmp 0x1402c10d2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitSystemPageTables(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_r10 = (a1) >> (9);
    v_r10 = (v_r10) & (a1);
    a4 = (a2) >> (9);
    v_r10 = (v_r10) + (result);
    a4 = (a4) & (a1);
    v_r10 = (v_r10) & (0xFFFFFFFFFFFFF000ULL);
    a4 = (a4) + (a1);
    a4 = (a4) & (0xFFFFFFFFFFFFF000ULL);
    result = (a1) << (25);
    v_r10 = (v_r10) << (25);
    a4 = (a4) << (25);
    v_r10 = (v_r10) - (result);
    a4 = (a4) - (result);
    v_r10 = (v_r10) >> (16);
    a4 = (a4) >> (16);
    result = MiSystemVaTypeToVm((unsigned int)(a3), 0xFFFFFFFFFFFFF000ULL, a3, a4);
    if (result == 0) goto loc_002C10F8;
loc_002C10D2:
    a4 = (a4) - 1;
    v_stack_m18 = 1;
    result = MiDeleteSystemPageTables(result, (unsigned int)((unsigned int)((unsigned int)(a3))), v_r10, a4);
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(result + 184));
loc_002C10F8:
    result = MiGetAnyMultiplexedVm(6, (unsigned int)((unsigned int)((unsigned int)(a3))), v_r10, a4);
    goto loc_002C10D2;
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitSystemPageTables(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    local_r10 = (Arg1) >> (9);
    local_r10 = (local_r10) & (Arg1);
    a4 = (Arg2) >> (9);
    local_r10 = (local_r10) + (result);
    a4 = (a4) & (Arg1);
    local_r10 = (local_r10) & (0xFFFFFFFFFFFFF000ULL);
    a4 = (a4) + (Arg1);
    a4 = (a4) & (0xFFFFFFFFFFFFF000ULL);
    result = (Arg1) << (25);
    local_r10 = (local_r10) << (25);
    a4 = (a4) << (25);
    local_r10 = (local_r10) - (result);
    a4 = (a4) - (result);
    local_r10 = (local_r10) >> (16);
    a4 = (a4) >> (16);
    result = MiSystemVaTypeToVm((uint32_t)(Arg3), 0xFFFFFFFFFFFFF000ULL, Arg3, a4);
    if (result == 0) goto loc_002C10F8;
loc_002C10D2:
    a4 = (a4) - 1;
    v_stack_m18 = 1;
    result = MiDeleteSystemPageTables(result, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r10, a4);
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(result + 0xB8));
loc_002C10F8:
    result = MiGetAnyMultiplexedVm(6, (uint32_t)((uint32_t)((uint32_t)(Arg3))), local_r10, a4);
    goto loc_002C10D2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C1054&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C1054[BB_002C1054]
  bb_002C10D2[BB_002C10D2]
  bb_002C10F7[BB_002C10F7]
  bb_002C10F8[BB_002C10F8]
  bb_002C1054 -->|branch| bb_002C10F8
  bb_002C1054 -->|fallthrough| bb_002C10D2
  bb_002C10F7 -->|flow| bb_002C10F8
  bb_002C10F8 -->|branch| bb_002C10D2
```
