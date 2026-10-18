# MmUnlockPhysicalPagesByVa

- RVA: `0x007FBA3C`–`0x007FBB54` (길이 `280` bytes)
- VA: `0x00000001407FBA3C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7B84`
- 디코드: `70`개 명령, `280/280` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007FBAB8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007FBAF6` → [MiLockWorkingSetShared](../../text/27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x007FBB06` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)
- `0x007FBB10` → [MiUnlockWorkingSetShared](../../text/27/MiUnlockWorkingSetShared_function_0027D690.md) (function, `0x0027D690`)
- `0x007FBB40` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiProbeAndLockPages](../../text/23/MiProbeAndLockPages_function_0023B4F0.md) at `0x0023B7E4`
- [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) at `0x0023BB2F`
- [MiProbeAndLockComplete](../../text/49/MiProbeAndLockComplete_function_0049A18C.md) at `0x0049A22E`
- [VmpPinMemoryRange](../../text/64/VmpPinMemoryRange_function_0064CCD0.md) at `0x0064D0D0`
- [VmpUnpinMemoryRangeHelper](../../text/64/VmpUnpinMemoryRangeHelper_function_0064D370.md) at `0x0064D51A`

### Static image references
- `0x007FBA4F` → RVA `0x00E0A740` (`.data`; read)
- `0x007FBAD0` → RVA `0x00673EB0` (`MiUnlockPhysicalPageByVa`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x007FBAB8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007FBAF6` → [MiLockWorkingSetShared](../../text/27/MiLockWorkingSetShared_function_0027CBF0.md) (`PAGE` → `.text`)
  - `0x007FBB06` → [MiWalkPageTables](../../text/2C/MiWalkPageTables_function_002C2710.md) (`PAGE` → `.text`)
  - `0x007FBB10` → [MiUnlockWorkingSetShared](../../text/27/MiUnlockWorkingSetShared_function_0027D690.md) (`PAGE` → `.text`)
  - `0x007FBB40` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FBA3C  40 55                           push rbp
007FBA3E  53                              push rbx
007FBA3F  56                              push rsi
007FBA40  57                              push rdi
007FBA41  41 56                           push r14
007FBA43  48 8D 6C 24 C9                  lea rbp, [rsp - 0x37]
007FBA48  48 81 EC 00 01 00 00            sub rsp, 0x100
007FBA4F  48 8B 05 EA EC 60 00            mov rax, qword ptr [rip + 0x60ecea]
007FBA56  48 33 C4                        xor rax, rsp
007FBA59  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
007FBA5D  48 8B F1                        mov rsi, rcx
007FBA60  33 C0                           xor eax, eax
007FBA62  89 45 1B                        mov dword ptr [rbp + 0x1b], eax
007FBA65  81 E6 FF 0F 00 00               and esi, 0xfff
007FBA6B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007FBA74  48 8B D9                        mov rbx, rcx
007FBA77  48 81 C6 FF 0F 00 00            add rsi, 0xfff
007FBA7E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007FBA83  48 03 F2                        add rsi, rdx
007FBA86  41 B8 C0 00 00 00               mov r8d, 0xc0
007FBA8C  48 C1 EE 0C                     shr rsi, 0xc
007FBA90  33 D2                           xor edx, edx
007FBA92  4C 8B B0 B8 00 00 00            mov r14, qword ptr [rax + 0xb8]
007FBA99  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
007FBAA0  48 83 65 1B 00                  and qword ptr [rbp + 0x1b], 0
007FBAA5  83 65 23 00                     and dword ptr [rbp + 0x23], 0
007FBAA9  44 89 4D 17                     mov dword ptr [rbp + 0x17], r9d
007FBAAD  49 8D BE 00 04 00 00            lea rdi, [r14 + 0x400]
007FBAB4  48 89 75 27                     mov qword ptr [rbp + 0x27], rsi
007FBAB8  E8 83 B1 EC FF                  call 0x1406c6c40
007FBABD  48 8D 45 17                     lea rax, [rbp + 0x17]
007FBAC1  C7 44 24 20 27 00 00 00         mov dword ptr [rsp + 0x20], 0x27
007FBAC9  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
007FBACD  48 8B CF                        mov rcx, rdi
007FBAD0  48 8D 05 D9 83 E7 FF            lea rax, [rip - 0x187c27]
007FBAD7  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
007FBADC  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007FBAE0  48 8B C6                        mov rax, rsi
007FBAE3  48 C1 E0 0C                     shl rax, 0xc
007FBAE7  48 FF C8                        dec rax
007FBAEA  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007FBAEF  48 03 C3                        add rax, rbx
007FBAF2  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
007FBAF6  E8 F5 10 A8 FF                  call 0x14027cbf0
007FBAFB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007FBB00  88 44 24 29                     mov byte ptr [rsp + 0x29], al
007FBB04  8A D8                           mov bl, al
007FBB06  E8 05 6C AC FF                  call 0x1402c2710
007FBB0B  8A D3                           mov dl, bl
007FBB0D  48 8B CF                        mov rcx, rdi
007FBB10  E8 7B 1B A8 FF                  call 0x14027d690
007FBB15  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
007FBB1D  48 F7 DE                        neg rsi
007FBB20  48 D1 E8                        shr rax, 1
007FBB23  83 E0 03                        and eax, 3
007FBB26  48 83 C0 08                     add rax, 8
007FBB2A  48 C1 E0 06                     shl rax, 6
007FBB2E  49 03 86 10 04 00 00            add rax, qword ptr [r14 + 0x410]
007FBB35  F0 48 01 30                     lock add qword ptr [rax], rsi
007FBB39  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
007FBB3D  48 33 CC                        xor rcx, rsp
007FBB40  E8 FB 0A EB FF                  call 0x1406ac640
007FBB45  48 81 C4 00 01 00 00            add rsp, 0x100
007FBB4C  41 5E                           pop r14
007FBB4E  5F                              pop rdi
007FBB4F  5E                              pop rsi
007FBB50  5B                              pop rbx
007FBB51  5D                              pop rbp
007FBB52  C3                              ret
007FBB53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmUnlockPhysicalPagesByVa(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int8 v_stack_mFF;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 6352106)) ^ (v_rsp);
    v_stack_m30 = result;
    result = 0;
    v_stack_m44 = 0;
    v_rsi = (unsigned int)((a1) & (0xFFFULL));
    v_rsi = (v_rsi) + (0xFFFULL);
    v_rsi = (v_rsi) + (a2);
    v_rsi = (v_rsi) >> (12);
    a2 = 0;
    v_rbx = (a1) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m48 = a4;
    v_stack_m38 = v_rsi;
    result = memset(v_stack_m108, a2, 192, a4);
    v_stack_m108 = 39;
    v_stack_m50 = v_stack_m48;
    v_stack_mE0 = v_rbx;
    v_stack_m60 = v_rip - 1604647;
    result = (v_rsi) << (12);
    result = (result) - 1;
    v_stack_mE8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    result = (result) + (v_rbx);
    v_stack_mD8 = result;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, 192, a4);
    v_stack_mFF = (unsigned __int8)(result);
    result = MiWalkPageTables(v_stack_m108, a2, 192, a4);
    result = MiUnlockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned __int8)((unsigned __int8)(result)), 192, a4);
    v_rsi = -(v_rsi);
    result = ((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))) >> (1);
    result = (unsigned int)((result) & (3));
    result = (result) + (8);
    result = (result) << (6);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040));
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned __int8)((unsigned __int8)(result)), 192, a4);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmUnlockPhysicalPagesByVa(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint8_t v_stack_mFF;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x60ECEA)) ^ (local_rsp);
    v_stack_m30 = result;
    result = 0;
    v_stack_m44 = 0;
    local_rsi = (uint32_t)((Arg1) & (0xFFFULL));
    local_rsi = (local_rsi) + (0xFFFULL);
    local_rsi = (local_rsi) + (Arg2);
    local_rsi = (local_rsi) >> (12);
    Arg2 = 0;
    local_rbx = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m48 = Arg4;
    v_stack_m38 = local_rsi;
    result = memset(v_stack_m108, Arg2, 192, Arg4);
    v_stack_m108 = 39;
    v_stack_m50 = v_stack_m48;
    v_stack_mE0 = local_rbx;
    v_stack_m60 = v_rip - 1604647;
    result = (local_rsi) << (12);
    result = (result) - 1;
    v_stack_mE8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    result = (result) + (local_rbx);
    v_stack_mD8 = result;
    result = MiLockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, 192, Arg4);
    v_stack_mFF = (uint8_t)(result);
    result = MiWalkPageTables(v_stack_m108, Arg2, 192, Arg4);
    result = MiUnlockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint8_t)((uint8_t)(result)), 192, Arg4);
    local_rsi = -(local_rsi);
    result = ((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))) >> (1);
    result = (uint32_t)((result) & (3));
    result = (result) + (8);
    result = (result) << (6);
    result = (result) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410));
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint8_t)((uint8_t)(result)), 192, Arg4);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FBA3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007FBA3C[BB_007FBA3C]
  bb_007FBB53[BB_007FBB53]
```
