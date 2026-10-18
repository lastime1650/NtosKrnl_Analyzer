# DifZwCloseWrapper

- RVA: `0x0063EF90`–`0x0063F0EF` (길이 `351` bytes)
- VA: `0x000000014063EF90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063EFBF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063EFE7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063F015` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F03C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F055` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063F05D` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0063F08A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F0B1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F0CA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063EFF9` → RVA `0x00F048B8` (`.data`; read)
- `0x0063F002` → RVA `0x00F04980` (`.data`; read)
- `0x0063F00E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063EF90  4C 8B DC                        mov r11, rsp
0063EF93  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0063EF97  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063EF9B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063EF9F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0063EFA3  41 56                           push r14
0063EFA5  48 83 EC 40                     sub rsp, 0x40
0063EFA9  33 C0                           xor eax, eax
0063EFAB  0F 57 C0                        xorps xmm0, xmm0
0063EFAE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0063EFB3  48 8B E9                        mov rbp, rcx
0063EFB6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063EFBA  B9 83 00 00 00                  mov ecx, 0x83
0063EFBF  E8 70 6A E5 FF                  call 0x140495a34
0063EFC4  48 8B F0                        mov rsi, rax
0063EFC7  48 85 C0                        test rax, rax
0063EFCA  0F 84 8A 00 00 00               je 0x14063f05a
0063EFD0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063EFD3  A8 18                           test al, 0x18
0063EFD5  74 0C                           je 0x14063efe3
0063EFD7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063EFDC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063EFE1  EB 0E                           jmp 0x14063eff1
0063EFE3  A8 04                           test al, 4
0063EFE5  74 0A                           je 0x14063eff1
0063EFE7  E8 1C 4C E9 FF                  call 0x1404d3c08
0063EFEC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063EFF1  40 32 FF                        xor dil, dil
0063EFF4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0063EFF9  40 38 3D B8 58 8C 00            cmp byte ptr [rip + 0x8c58b8], dil
0063F000  75 0C                           jne 0x14063f00e
0063F002  F7 05 74 59 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5974], 0x800
0063F00C  74 13                           je 0x14063f021
0063F00E  48 8D 0D 6B 4E 8C 00            lea rcx, [rip + 0x8c4e6b]
0063F015  E8 06 76 BD FF                  call 0x140216620
0063F01A  40 8A F8                        mov dil, al
0063F01D  84 C0                           test al, al
0063F01F  74 39                           je 0x14063f05a
0063F021  4C 8D 76 20                     lea r14, [rsi + 0x20]
0063F025  49 8B 1E                        mov rbx, qword ptr [r14]
0063F028  EB 1A                           jmp 0x14063f044
0063F02A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F02E  48 85 C0                        test rax, rax
0063F031  74 0E                           je 0x14063f041
0063F033  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F037  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063F03C  E8 8F BA 07 00                  call 0x1406baad0
0063F041  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F044  49 3B DE                        cmp rbx, r14
0063F047  75 E1                           jne 0x14063f02a
0063F049  40 84 FF                        test dil, dil
0063F04C  74 0C                           je 0x14063f05a
0063F04E  48 8D 0D 2B 4E 8C 00            lea rcx, [rip + 0x8c4e2b]
0063F055  E8 26 AE D0 FF                  call 0x140349e80
0063F05A  48 8B CD                        mov rcx, rbp
0063F05D  E8 4E E2 06 00                  call 0x1406ad2b0
0063F062  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0063F066  48 85 F6                        test rsi, rsi
0063F069  74 64                           je 0x14063f0cf
0063F06B  40 32 FF                        xor dil, dil
0063F06E  40 38 3D 43 58 8C 00            cmp byte ptr [rip + 0x8c5843], dil
0063F075  75 0C                           jne 0x14063f083
0063F077  F7 05 FF 58 8C 00 00 08 00 00   test dword ptr [rip + 0x8c58ff], 0x800
0063F081  74 13                           je 0x14063f096
0063F083  48 8D 0D F6 4D 8C 00            lea rcx, [rip + 0x8c4df6]
0063F08A  E8 91 75 BD FF                  call 0x140216620
0063F08F  40 8A F8                        mov dil, al
0063F092  84 C0                           test al, al
0063F094  74 39                           je 0x14063f0cf
0063F096  48 83 C6 30                     add rsi, 0x30
0063F09A  48 8B 1E                        mov rbx, qword ptr [rsi]
0063F09D  EB 1A                           jmp 0x14063f0b9
0063F09F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F0A3  48 85 C0                        test rax, rax
0063F0A6  74 0E                           je 0x14063f0b6
0063F0A8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F0AC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063F0B1  E8 1A BA 07 00                  call 0x1406baad0
0063F0B6  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F0B9  48 3B DE                        cmp rbx, rsi
0063F0BC  75 E1                           jne 0x14063f09f
0063F0BE  40 84 FF                        test dil, dil
0063F0C1  74 0C                           je 0x14063f0cf
0063F0C3  48 8D 0D B6 4D 8C 00            lea rcx, [rip + 0x8c4db6]
0063F0CA  E8 B1 AD D0 FF                  call 0x140349e80
0063F0CF  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0063F0D3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0063F0D8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063F0DD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0063F0E2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0063F0E7  48 83 C4 40                     add rsp, 0x40
0063F0EB  41 5E                           pop r14
0063F0ED  C3                              ret
0063F0EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCloseWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(131, a2, a3, a4);
    if (result == 0) goto loc_0063F05A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063EFE3;
    v_stack_m28 = v_stack_p0;
    goto loc_0063EFF1;
loc_0063EFE3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9197752)) != 0) goto loc_0063F00E;
    if (((*(unsigned int *)(v_rip + 9197940)) & (0x800ULL)) == 0) goto loc_0063F021;
loc_0063F00E:
    result = ExAcquireRundownProtection(v_rip + 9195115, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F05A;
loc_0063F021:
    goto loc_0063F044;
loc_0063F02A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F044:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063F02A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9195051;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwClose(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0063F0CF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9197635)) != 0) goto loc_0063F083;
    if (((*(unsigned int *)(v_rip + 9197823)) & (0x800ULL)) == 0) goto loc_0063F096;
loc_0063F083:
    result = ExAcquireRundownProtection(v_rip + 9194998, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F0CF;
loc_0063F096:
    v_rsi = (result) + (48);
    goto loc_0063F0B9;
loc_0063F09F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F0B9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063F09F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9194934;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCloseWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(131, a2, a3, a4);
    if (result == 0) goto loc_0063F05A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063EFE3;
    v_stack_m28 = v_stack_p0;
    goto loc_0063EFF1;
loc_0063EFE3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C58B8)) != 0) goto loc_0063F00E;
    if (((*(uint32_t *)(v_rip + 0x8C5974)) & (0x800ULL)) == 0) goto loc_0063F021;
loc_0063F00E:
    result = ExAcquireRundownProtection(v_rip + 9195115, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F05A;
loc_0063F021:
    goto loc_0063F044;
loc_0063F02A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063F044:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063F02A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9195051;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwClose(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0063F0CF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C5843)) != 0) goto loc_0063F083;
    if (((*(uint32_t *)(v_rip + 0x8C58FF)) & (0x800ULL)) == 0) goto loc_0063F096;
loc_0063F083:
    result = ExAcquireRundownProtection(v_rip + 9194998, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F0CF;
loc_0063F096:
    local_rsi = (result) + (48);
    goto loc_0063F0B9;
loc_0063F09F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063F0B9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063F09F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9194934;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063EF90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063EF90[BB_0063EF90]
  bb_0063EFD0[BB_0063EFD0]
  bb_0063EFD7[BB_0063EFD7]
  bb_0063EFE3[BB_0063EFE3]
  bb_0063EFE7[BB_0063EFE7]
  bb_0063EFF1[BB_0063EFF1]
  bb_0063F002[BB_0063F002]
  bb_0063F00E[BB_0063F00E]
  bb_0063F021[BB_0063F021]
  bb_0063F02A[BB_0063F02A]
  bb_0063F033[BB_0063F033]
  bb_0063F041[BB_0063F041]
  bb_0063F044[BB_0063F044]
  bb_0063F049[BB_0063F049]
  bb_0063F04E[BB_0063F04E]
  bb_0063F05A[BB_0063F05A]
  bb_0063F06B[BB_0063F06B]
  bb_0063F077[BB_0063F077]
  bb_0063F083[BB_0063F083]
  bb_0063F096[BB_0063F096]
  bb_0063F09F[BB_0063F09F]
  bb_0063F0A8[BB_0063F0A8]
  bb_0063F0B6[BB_0063F0B6]
  bb_0063F0B9[BB_0063F0B9]
  bb_0063F0BE[BB_0063F0BE]
  bb_0063F0C3[BB_0063F0C3]
  bb_0063F0CF[BB_0063F0CF]
  bb_0063F0EE[BB_0063F0EE]
  bb_0063EF90 -->|branch| bb_0063F05A
  bb_0063EF90 -->|fallthrough| bb_0063EFD0
  bb_0063EFD0 -->|branch| bb_0063EFE3
  bb_0063EFD0 -->|fallthrough| bb_0063EFD7
  bb_0063EFD7 -->|branch| bb_0063EFF1
  bb_0063EFE3 -->|branch| bb_0063EFF1
  bb_0063EFE3 -->|fallthrough| bb_0063EFE7
  bb_0063EFE7 -->|flow| bb_0063EFF1
  bb_0063EFF1 -->|branch| bb_0063F00E
  bb_0063EFF1 -->|fallthrough| bb_0063F002
  bb_0063F002 -->|branch| bb_0063F021
  bb_0063F002 -->|fallthrough| bb_0063F00E
  bb_0063F00E -->|branch| bb_0063F05A
  bb_0063F00E -->|fallthrough| bb_0063F021
  bb_0063F021 -->|branch| bb_0063F044
  bb_0063F02A -->|branch| bb_0063F041
  bb_0063F02A -->|fallthrough| bb_0063F033
  bb_0063F033 -->|flow| bb_0063F041
  bb_0063F041 -->|flow| bb_0063F044
  bb_0063F044 -->|branch| bb_0063F02A
  bb_0063F044 -->|fallthrough| bb_0063F049
  bb_0063F049 -->|branch| bb_0063F05A
  bb_0063F049 -->|fallthrough| bb_0063F04E
  bb_0063F04E -->|flow| bb_0063F05A
  bb_0063F05A -->|branch| bb_0063F0CF
  bb_0063F05A -->|fallthrough| bb_0063F06B
  bb_0063F06B -->|branch| bb_0063F083
  bb_0063F06B -->|fallthrough| bb_0063F077
  bb_0063F077 -->|branch| bb_0063F096
  bb_0063F077 -->|fallthrough| bb_0063F083
  bb_0063F083 -->|branch| bb_0063F0CF
  bb_0063F083 -->|fallthrough| bb_0063F096
  bb_0063F096 -->|branch| bb_0063F0B9
  bb_0063F09F -->|branch| bb_0063F0B6
  bb_0063F09F -->|fallthrough| bb_0063F0A8
  bb_0063F0A8 -->|flow| bb_0063F0B6
  bb_0063F0B6 -->|flow| bb_0063F0B9
  bb_0063F0B9 -->|branch| bb_0063F09F
  bb_0063F0B9 -->|fallthrough| bb_0063F0BE
  bb_0063F0BE -->|branch| bb_0063F0CF
  bb_0063F0BE -->|fallthrough| bb_0063F0C3
  bb_0063F0C3 -->|flow| bb_0063F0CF
```
