# MiInitializePfnsForValidMappings

- RVA: `0x00C6267C`–`0x00C627A2` (길이 `294` bytes)
- VA: `0x0000000140C6267C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D79B8`
- 디코드: `63`개 명령, `294/294` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C626A6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C626F6` → [MxCreatePfnsForPtes](MxCreatePfnsForPtes_function_00C635B0.md) (function, `0x00C635B0`)
- `0x00C626FF` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x00C62709` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (function, `0x00314110`)
- `0x00C62727` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x00C6276D` → [MiLockPageInline](../../text/31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00C62787` → [MiUnlockPage](../../text/31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)

### Direct callers
- [MiInitNucleus](../C5/MiInitNucleus_function_00C5FD38.md) at `0x00C600A1`

### Static image references
- `0x00C626D2` → RVA `0x00C635B0` (`MxCreatePfnsForPtes`; read)
- `0x00C62720` → RVA `0x00FC6A88` (`ALMOSTRO`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00C626A6` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C626FF` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (`INIT` → `.text`)
  - `0x00C62709` → [MI_FLUSH_ENTIRE_TB](../../text/31/MI_FLUSH_ENTIRE_TB_function_00314110.md) (`INIT` → `.text`)
  - `0x00C62727` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (`INIT` → `.text`)
  - `0x00C6276D` → [MiLockPageInline](../../text/31/MiLockPageInline_function_0031A340.md) (`INIT` → `.text`)
  - `0x00C62787` → [MiUnlockPage](../../text/31/MiUnlockPage_function_0031A3E0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6267C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00C62681  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C62686  55                              push rbp
00C62687  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00C6268C  48 81 EC F0 00 00 00            sub rsp, 0xf0
00C62693  83 65 93 00                     and dword ptr [rbp - 0x6d], 0
00C62697  48 8B D9                        mov rbx, rcx
00C6269A  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00C6269E  33 D2                           xor edx, edx
00C626A0  41 B8 C0 00 00 00               mov r8d, 0xc0
00C626A6  E8 95 45 A6 FF                  call 0x1406c6c40
00C626AB  48 83 4D C7 FF                  or qword ptr [rbp - 0x39], 0xffffffffffffffff
00C626B0  48 8D 45 87                     lea rax, [rbp - 0x79]
00C626B4  48 89 45 4F                     mov qword ptr [rbp + 0x4f], rax
00C626B8  BE 01 00 00 00                  mov esi, 1
00C626BD  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00C626C7  C7 45 97 00 26 02 00            mov dword ptr [rbp - 0x69], 0x22600
00C626CE  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
00C626D2  48 8D 05 D7 0E 00 00            lea rax, [rip + 0xed7]
00C626D9  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
00C626DD  48 89 5D 87                     mov qword ptr [rbp - 0x79], rbx
00C626E1  89 75 8F                        mov dword ptr [rbp - 0x71], esi
00C626E4  48 BA 68 DF BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbedf68
00C626EE  44 8D 46 02                     lea r8d, [rsi + 2]
00C626F2  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00C626F6  E8 B5 0E 00 00                  call 0x140c635b0
00C626FB  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00C626FF  E8 0C 00 66 FF                  call 0x1402c2710
00C62704  83 CA FF                        or edx, 0xffffffff
00C62707  33 C9                           xor ecx, ecx
00C62709  E8 02 1A 6B FF                  call 0x140314110
00C6270E  83 65 8F 00                     and dword ptr [rbp - 0x71], 0
00C62712  48 8D 4D 97                     lea rcx, [rbp - 0x69]
00C62716  48 B8 00 00 00 00 80 00 00 00   movabs rax, 0x8000000000
00C62720  48 09 05 61 43 36 00            or qword ptr [rip + 0x364361], rax
00C62727  E8 E4 FF 65 FF                  call 0x1402c2710
00C6272C  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00C62736  48 B9 00 00 00 C0 7B 00 00 00   movabs rcx, 0x7bc0000000
00C62740  48 8B 04 08                     mov rax, qword ptr [rax + rcx]
00C62744  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00C6274E  48 C1 E8 0C                     shr rax, 0xc
00C62752  48 23 C1                        and rax, rcx
00C62755  48 8D 1C 40                     lea rbx, [rax + rax*2]
00C62759  48 C1 E3 04                     shl rbx, 4
00C6275D  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00C62767  48 03 D8                        add rbx, rax
00C6276A  48 8B CB                        mov rcx, rbx
00C6276D  E8 CE 7B 6B FF                  call 0x14031a340
00C62772  8B 53 20                        mov edx, dword ptr [rbx + 0x20]
00C62775  48 8B CB                        mov rcx, rbx
00C62778  89 55 67                        mov dword ptr [rbp + 0x67], edx
00C6277B  66 01 75 67                     add word ptr [rbp + 0x67], si
00C6277F  8B 55 67                        mov edx, dword ptr [rbp + 0x67]
00C62782  89 53 20                        mov dword ptr [rbx + 0x20], edx
00C62785  8A D0                           mov dl, al
00C62787  E8 54 7C 6B FF                  call 0x14031a3e0
00C6278C  4C 8D 9C 24 F0 00 00 00         lea r11, [rsp + 0xf0]
00C62794  49 8B 5B 18                     mov rbx, qword ptr [r11 + 0x18]
00C62798  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
00C6279C  49 8B E3                        mov rsp, r11
00C6279F  5D                              pop rbp
00C627A0  C3                              ret
00C627A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializePfnsForValidMappings(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (240);
    a2 = 0;
    result = memset(v_stack_mC8, a2, 192, a4);
    v_stack_m10 = v_stack_mD8;
    v_stack_mC8 = 0x22600ULL;
    v_stack_mA0 = v_stack_mD8;
    v_stack_m20 = v_rip + 3799;
    v_stack_mD8 = a1;
    v_stack_mD0 = 1;
    result = MxCreatePfnsForPtes(v_stack_mC8, a2, 1 + 2, a4);
    result = MiWalkPageTables(v_stack_mC8, a2, 1 + 2, a4);
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    a1 = 0;
    result = MI_FLUSH_ENTIRE_TB(a1, a2, 1 + 2, a4);
    result = MiWalkPageTables(v_stack_mC8, a2, 1 + 2, a4);
    result = (*(unsigned __int64 *)(result + v_stack_mC8 * 1)) >> (12);
    result = (result) & (v_stack_mC8);
    v_rbx = (result + result * 2) << (4);
    v_rbx = (v_rbx) + (result);
    result = MiLockPageInline(v_rbx, a2, 1 + 2, a4);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = MiUnlockPage(v_rbx, (unsigned __int8)(result), 1 + 2, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializePfnsForValidMappings(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m20;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m8;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (240);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 192, a4);
    v_stack_m10 = v_stack_mD8;
    v_stack_mC8 = 0x22600ULL;
    v_stack_mA0 = v_stack_mD8;
    v_stack_m20 = v_rip + 3799;
    v_stack_mD8 = Arg1;
    v_stack_mD0 = 1;
    result = MxCreatePfnsForPtes(v_stack_mC8, Arg2, 1 + 2, a4);
    result = MiWalkPageTables(v_stack_mC8, Arg2, 1 + 2, a4);
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    Arg1 = 0;
    result = MI_FLUSH_ENTIRE_TB(Arg1, Arg2, 1 + 2, a4);
    result = MiWalkPageTables(v_stack_mC8, Arg2, 1 + 2, a4);
    result = (*(uint64_t *)(result + v_stack_mC8 * 1)) >> (12);
    result = (result) & (v_stack_mC8);
    local_rbx = (result + result * 2) << (4);
    local_rbx = (local_rbx) + (result);
    result = MiLockPageInline(local_rbx, Arg2, 1 + 2, a4);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = MiUnlockPage(local_rbx, (uint8_t)(result), 1 + 2, a4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6267C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6267C[BB_00C6267C]
  bb_00C627A1[BB_00C627A1]
```
