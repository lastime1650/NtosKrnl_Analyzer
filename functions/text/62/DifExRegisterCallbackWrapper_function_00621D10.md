# DifExRegisterCallbackWrapper

- RVA: `0x00621D10`–`0x00621E89` (길이 `377` bytes)
- VA: `0x0000000140621D10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `377/377` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00621D4E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00621D74` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00621DA8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621DCE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621DE7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00621DF5` → [ExRegisterCallback](../4B/ExRegisterCallback_function_004BDFC0.md) (function, `0x004BDFC0`)
- `0x00621E22` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621E48` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621E61` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621D84` → RVA `0x00F048B8` (`.data`; read)
- `0x00621D95` → RVA `0x00F04980` (`.data`; read)
- `0x00621DA1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00621D10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00621D15  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00621D1A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00621D1F  55                              push rbp
00621D20  41 54                           push r12
00621D22  41 55                           push r13
00621D24  41 56                           push r14
00621D26  41 57                           push r15
00621D28  48 8B EC                        mov rbp, rsp
00621D2B  48 83 EC 50                     sub rsp, 0x50
00621D2F  0F 57 C0                        xorps xmm0, xmm0
00621D32  33 C0                           xor eax, eax
00621D34  4C 8B E9                        mov r13, rcx
00621D37  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00621D3B  B9 87 01 00 00                  mov ecx, 0x187
00621D40  4D 8B F8                        mov r15, r8
00621D43  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00621D47  4C 8B E2                        mov r12, rdx
00621D4A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00621D4E  E8 E1 3C E7 FF                  call 0x140495a34
00621D53  48 8B F0                        mov rsi, rax
00621D56  48 85 C0                        test rax, rax
00621D59  0F 84 8D 00 00 00               je 0x140621dec
00621D5F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621D62  A8 18                           test al, 0x18
00621D64  74 0A                           je 0x140621d70
00621D66  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00621D6A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00621D6E  EB 0D                           jmp 0x140621d7d
00621D70  A8 04                           test al, 4
00621D72  74 09                           je 0x140621d7d
00621D74  E8 8F 1E EB FF                  call 0x1404d3c08
00621D79  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00621D7D  45 32 F6                        xor r14b, r14b
00621D80  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00621D84  44 38 35 2D 2B 8E 00            cmp byte ptr [rip + 0x8e2b2d], r14b
00621D8B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00621D8F  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00621D93  75 0C                           jne 0x140621da1
00621D95  F7 05 E1 2B 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2be1], 0x800
00621D9F  74 13                           je 0x140621db4
00621DA1  48 8D 0D D8 20 8E 00            lea rcx, [rip + 0x8e20d8]
00621DA8  E8 73 48 BF FF                  call 0x140216620
00621DAD  44 8A F0                        mov r14b, al
00621DB0  84 C0                           test al, al
00621DB2  74 38                           je 0x140621dec
00621DB4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00621DB8  48 8B 1F                        mov rbx, qword ptr [rdi]
00621DBB  EB 19                           jmp 0x140621dd6
00621DBD  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621DC1  48 85 C0                        test rax, rax
00621DC4  74 0D                           je 0x140621dd3
00621DC6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621DCA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00621DCE  E8 FD 8C 09 00                  call 0x1406baad0
00621DD3  48 8B 1B                        mov rbx, qword ptr [rbx]
00621DD6  48 3B DF                        cmp rbx, rdi
00621DD9  75 E2                           jne 0x140621dbd
00621DDB  45 84 F6                        test r14b, r14b
00621DDE  74 0C                           je 0x140621dec
00621DE0  48 8D 0D 99 20 8E 00            lea rcx, [rip + 0x8e2099]
00621DE7  E8 94 80 D2 FF                  call 0x140349e80
00621DEC  4D 8B C7                        mov r8, r15
00621DEF  49 8B D4                        mov rdx, r12
00621DF2  49 8B CD                        mov rcx, r13
00621DF5  E8 C6 C1 E9 FF                  call 0x1404bdfc0
00621DFA  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00621DFE  48 85 F6                        test rsi, rsi
00621E01  74 63                           je 0x140621e66
00621E03  40 32 FF                        xor dil, dil
00621E06  40 38 3D AB 2A 8E 00            cmp byte ptr [rip + 0x8e2aab], dil
00621E0D  75 0C                           jne 0x140621e1b
00621E0F  F7 05 67 2B 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2b67], 0x800
00621E19  74 13                           je 0x140621e2e
00621E1B  48 8D 0D 5E 20 8E 00            lea rcx, [rip + 0x8e205e]
00621E22  E8 F9 47 BF FF                  call 0x140216620
00621E27  40 8A F8                        mov dil, al
00621E2A  84 C0                           test al, al
00621E2C  74 38                           je 0x140621e66
00621E2E  48 83 C6 30                     add rsi, 0x30
00621E32  48 8B 1E                        mov rbx, qword ptr [rsi]
00621E35  EB 19                           jmp 0x140621e50
00621E37  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621E3B  48 85 C0                        test rax, rax
00621E3E  74 0D                           je 0x140621e4d
00621E40  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621E44  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00621E48  E8 83 8C 09 00                  call 0x1406baad0
00621E4D  48 8B 1B                        mov rbx, qword ptr [rbx]
00621E50  48 3B DE                        cmp rbx, rsi
00621E53  75 E2                           jne 0x140621e37
00621E55  40 84 FF                        test dil, dil
00621E58  74 0C                           je 0x140621e66
00621E5A  48 8D 0D 1F 20 8E 00            lea rcx, [rip + 0x8e201f]
00621E61  E8 1A 80 D2 FF                  call 0x140349e80
00621E66  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00621E6A  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00621E6F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00621E73  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00621E77  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00621E7B  49 8B E3                        mov rsp, r11
00621E7E  41 5F                           pop r15
00621E80  41 5E                           pop r14
00621E82  41 5D                           pop r13
00621E84  41 5C                           pop r12
00621E86  5D                              pop rbp
00621E87  C3                              ret
00621E88  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExRegisterCallbackWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(391, a2, a3, a4);
    if (result == 0) goto loc_00621DEC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00621D70;
    v_stack_m58 = v_stack_p0;
    goto loc_00621D7D;
loc_00621D70:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9317165)) != 0) goto loc_00621DA1;
    if (((*(unsigned int *)(v_rip + 9317345)) & (0x800ULL)) == 0) goto loc_00621DB4;
loc_00621DA1:
    result = ExAcquireRundownProtection(v_rip + 9314520, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621DEC;
loc_00621DB4:
    goto loc_00621DD6;
loc_00621DBD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621DD6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00621DBD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9314457;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExRegisterCallback(a1, a2, a3, a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00621E66;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9317035)) != 0) goto loc_00621E1B;
    if (((*(unsigned int *)(v_rip + 9317223)) & (0x800ULL)) == 0) goto loc_00621E2E;
loc_00621E1B:
    result = ExAcquireRundownProtection(v_rip + 9314398, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621E66;
loc_00621E2E:
    v_rsi = (result) + (48);
    goto loc_00621E50;
loc_00621E37:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621E50:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00621E37;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9314335;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifExRegisterCallbackWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(391, Arg2, Arg3, a4);
    if (result == 0) goto loc_00621DEC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00621D70;
    v_stack_m58 = v_stack_p0;
    goto loc_00621D7D;
loc_00621D70:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8E2B2D)) != 0) goto loc_00621DA1;
    if (((*(uint32_t *)(v_rip + 0x8E2BE1)) & (0x800ULL)) == 0) goto loc_00621DB4;
loc_00621DA1:
    result = ExAcquireRundownProtection(v_rip + 9314520, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621DEC;
loc_00621DB4:
    goto loc_00621DD6;
loc_00621DBD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00621DD6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00621DBD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9314457;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ExRegisterCallback(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00621E66;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E2AAB)) != 0) goto loc_00621E1B;
    if (((*(uint32_t *)(v_rip + 0x8E2B67)) & (0x800ULL)) == 0) goto loc_00621E2E;
loc_00621E1B:
    result = ExAcquireRundownProtection(v_rip + 9314398, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621E66;
loc_00621E2E:
    local_rsi = (result) + (48);
    goto loc_00621E50;
loc_00621E37:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00621E50:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00621E37;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9314335;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00621D10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00621D10[BB_00621D10]
  bb_00621D5F[BB_00621D5F]
  bb_00621D66[BB_00621D66]
  bb_00621D70[BB_00621D70]
  bb_00621D74[BB_00621D74]
  bb_00621D7D[BB_00621D7D]
  bb_00621D95[BB_00621D95]
  bb_00621DA1[BB_00621DA1]
  bb_00621DB4[BB_00621DB4]
  bb_00621DBD[BB_00621DBD]
  bb_00621DC6[BB_00621DC6]
  bb_00621DD3[BB_00621DD3]
  bb_00621DD6[BB_00621DD6]
  bb_00621DDB[BB_00621DDB]
  bb_00621DE0[BB_00621DE0]
  bb_00621DEC[BB_00621DEC]
  bb_00621E03[BB_00621E03]
  bb_00621E0F[BB_00621E0F]
  bb_00621E1B[BB_00621E1B]
  bb_00621E2E[BB_00621E2E]
  bb_00621E37[BB_00621E37]
  bb_00621E40[BB_00621E40]
  bb_00621E4D[BB_00621E4D]
  bb_00621E50[BB_00621E50]
  bb_00621E55[BB_00621E55]
  bb_00621E5A[BB_00621E5A]
  bb_00621E66[BB_00621E66]
  bb_00621E88[BB_00621E88]
  bb_00621D10 -->|branch| bb_00621DEC
  bb_00621D10 -->|fallthrough| bb_00621D5F
  bb_00621D5F -->|branch| bb_00621D70
  bb_00621D5F -->|fallthrough| bb_00621D66
  bb_00621D66 -->|branch| bb_00621D7D
  bb_00621D70 -->|branch| bb_00621D7D
  bb_00621D70 -->|fallthrough| bb_00621D74
  bb_00621D74 -->|flow| bb_00621D7D
  bb_00621D7D -->|branch| bb_00621DA1
  bb_00621D7D -->|fallthrough| bb_00621D95
  bb_00621D95 -->|branch| bb_00621DB4
  bb_00621D95 -->|fallthrough| bb_00621DA1
  bb_00621DA1 -->|branch| bb_00621DEC
  bb_00621DA1 -->|fallthrough| bb_00621DB4
  bb_00621DB4 -->|branch| bb_00621DD6
  bb_00621DBD -->|branch| bb_00621DD3
  bb_00621DBD -->|fallthrough| bb_00621DC6
  bb_00621DC6 -->|flow| bb_00621DD3
  bb_00621DD3 -->|flow| bb_00621DD6
  bb_00621DD6 -->|branch| bb_00621DBD
  bb_00621DD6 -->|fallthrough| bb_00621DDB
  bb_00621DDB -->|branch| bb_00621DEC
  bb_00621DDB -->|fallthrough| bb_00621DE0
  bb_00621DE0 -->|flow| bb_00621DEC
  bb_00621DEC -->|branch| bb_00621E66
  bb_00621DEC -->|fallthrough| bb_00621E03
  bb_00621E03 -->|branch| bb_00621E1B
  bb_00621E03 -->|fallthrough| bb_00621E0F
  bb_00621E0F -->|branch| bb_00621E2E
  bb_00621E0F -->|fallthrough| bb_00621E1B
  bb_00621E1B -->|branch| bb_00621E66
  bb_00621E1B -->|fallthrough| bb_00621E2E
  bb_00621E2E -->|branch| bb_00621E50
  bb_00621E37 -->|branch| bb_00621E4D
  bb_00621E37 -->|fallthrough| bb_00621E40
  bb_00621E40 -->|flow| bb_00621E4D
  bb_00621E4D -->|flow| bb_00621E50
  bb_00621E50 -->|branch| bb_00621E37
  bb_00621E50 -->|fallthrough| bb_00621E55
  bb_00621E55 -->|branch| bb_00621E66
  bb_00621E55 -->|fallthrough| bb_00621E5A
  bb_00621E5A -->|flow| bb_00621E66
```
