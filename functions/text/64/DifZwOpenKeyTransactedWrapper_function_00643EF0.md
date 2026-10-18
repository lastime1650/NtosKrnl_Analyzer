# DifZwOpenKeyTransactedWrapper

- RVA: `0x00643EF0`–`0x00644075` (길이 `389` bytes)
- VA: `0x0000000140643EF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00643F30` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00643F56` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00643F92` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00643FB8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00643FD1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00643FE3` → [ZwOpenKeyTransacted](../6A/ZwOpenKeyTransacted_function_006AF670.md) (function, `0x006AF670`)
- `0x0064400F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644035` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064404E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00643F66` → RVA `0x00F048B8` (`.data`; read)
- `0x00643F7F` → RVA `0x00F04980` (`.data`; read)
- `0x00643F8B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00643EF0  48 8B C4                        mov rax, rsp
00643EF3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00643EF7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00643EFB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00643EFF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00643F03  55                              push rbp
00643F04  41 54                           push r12
00643F06  41 55                           push r13
00643F08  41 56                           push r14
00643F0A  41 57                           push r15
00643F0C  48 8B EC                        mov rbp, rsp
00643F0F  48 83 EC 50                     sub rsp, 0x50
00643F13  0F 57 C0                        xorps xmm0, xmm0
00643F16  B9 51 00 00 00                  mov ecx, 0x51
00643F1B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00643F1F  4D 8B F9                        mov r15, r9
00643F22  4D 8B E0                        mov r12, r8
00643F25  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00643F29  44 8B EA                        mov r13d, edx
00643F2C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00643F30  E8 FF 1A E5 FF                  call 0x140495a34
00643F35  48 8B F0                        mov rsi, rax
00643F38  48 85 C0                        test rax, rax
00643F3B  0F 84 95 00 00 00               je 0x140643fd6
00643F41  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00643F44  A8 18                           test al, 0x18
00643F46  74 0A                           je 0x140643f52
00643F48  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00643F4C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00643F50  EB 0D                           jmp 0x140643f5f
00643F52  A8 04                           test al, 4
00643F54  74 09                           je 0x140643f5f
00643F56  E8 AD FC E8 FF                  call 0x1404d3c08
00643F5B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00643F5F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00643F63  45 32 F6                        xor r14b, r14b
00643F66  44 38 35 4B 09 8C 00            cmp byte ptr [rip + 0x8c094b], r14b
00643F6D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00643F71  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00643F75  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00643F79  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00643F7D  75 0C                           jne 0x140643f8b
00643F7F  F7 05 F7 09 8C 00 00 08 00 00   test dword ptr [rip + 0x8c09f7], 0x800
00643F89  74 13                           je 0x140643f9e
00643F8B  48 8D 0D EE FE 8B 00            lea rcx, [rip + 0x8bfeee]
00643F92  E8 89 26 BD FF                  call 0x140216620
00643F97  44 8A F0                        mov r14b, al
00643F9A  84 C0                           test al, al
00643F9C  74 38                           je 0x140643fd6
00643F9E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00643FA2  48 8B 1F                        mov rbx, qword ptr [rdi]
00643FA5  EB 19                           jmp 0x140643fc0
00643FA7  48 8D 43 F0                     lea rax, [rbx - 0x10]
00643FAB  48 85 C0                        test rax, rax
00643FAE  74 0D                           je 0x140643fbd
00643FB0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00643FB4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00643FB8  E8 13 6B 07 00                  call 0x1406baad0
00643FBD  48 8B 1B                        mov rbx, qword ptr [rbx]
00643FC0  48 3B DF                        cmp rbx, rdi
00643FC3  75 E2                           jne 0x140643fa7
00643FC5  45 84 F6                        test r14b, r14b
00643FC8  74 0C                           je 0x140643fd6
00643FCA  48 8D 0D AF FE 8B 00            lea rcx, [rip + 0x8bfeaf]
00643FD1  E8 AA 5E D0 FF                  call 0x140349e80
00643FD6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00643FDA  4D 8B CF                        mov r9, r15
00643FDD  4D 8B C4                        mov r8, r12
00643FE0  41 8B D5                        mov edx, r13d
00643FE3  E8 88 B6 06 00                  call 0x1406af670
00643FE8  89 45 F8                        mov dword ptr [rbp - 8], eax
00643FEB  48 85 F6                        test rsi, rsi
00643FEE  74 63                           je 0x140644053
00643FF0  40 32 FF                        xor dil, dil
00643FF3  40 38 3D BE 08 8C 00            cmp byte ptr [rip + 0x8c08be], dil
00643FFA  75 0C                           jne 0x140644008
00643FFC  F7 05 7A 09 8C 00 00 08 00 00   test dword ptr [rip + 0x8c097a], 0x800
00644006  74 13                           je 0x14064401b
00644008  48 8D 0D 71 FE 8B 00            lea rcx, [rip + 0x8bfe71]
0064400F  E8 0C 26 BD FF                  call 0x140216620
00644014  40 8A F8                        mov dil, al
00644017  84 C0                           test al, al
00644019  74 38                           je 0x140644053
0064401B  48 83 C6 30                     add rsi, 0x30
0064401F  48 8B 1E                        mov rbx, qword ptr [rsi]
00644022  EB 19                           jmp 0x14064403d
00644024  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644028  48 85 C0                        test rax, rax
0064402B  74 0D                           je 0x14064403a
0064402D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644031  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644035  E8 96 6A 07 00                  call 0x1406baad0
0064403A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064403D  48 3B DE                        cmp rbx, rsi
00644040  75 E2                           jne 0x140644024
00644042  40 84 FF                        test dil, dil
00644045  74 0C                           je 0x140644053
00644047  48 8D 0D 32 FE 8B 00            lea rcx, [rip + 0x8bfe32]
0064404E  E8 2D 5E D0 FF                  call 0x140349e80
00644053  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00644056  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064405B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064405F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00644063  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00644067  49 8B E3                        mov rsp, r11
0064406A  41 5F                           pop r15
0064406C  41 5E                           pop r14
0064406E  41 5D                           pop r13
00644070  41 5C                           pop r12
00644072  5D                              pop rbp
00644073  C3                              ret
00644074  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenKeyTransactedWrapper(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(81, a2, a3, a4);
    if (result == 0) goto loc_00643FD6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00643F52;
    v_stack_m58 = v_stack_p0;
    goto loc_00643F5F;
loc_00643F52:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9177419)) != 0) goto loc_00643F8B;
    if (((*(unsigned int *)(v_rip + 9177591)) & (0x800ULL)) == 0) goto loc_00643F9E;
loc_00643F8B:
    result = ExAcquireRundownProtection(v_rip + 9174766, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00643FD6;
loc_00643F9E:
    goto loc_00643FC0;
loc_00643FA7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00643FC0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00643FA7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9174703;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenKeyTransacted(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00644053;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9177278)) != 0) goto loc_00644008;
    if (((*(unsigned int *)(v_rip + 9177466)) & (0x800ULL)) == 0) goto loc_0064401B;
loc_00644008:
    result = ExAcquireRundownProtection(v_rip + 9174641, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644053;
loc_0064401B:
    v_rsi = (result) + (48);
    goto loc_0064403D;
loc_00644024:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064403D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00644024;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9174578;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenKeyTransactedWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(81, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00643FD6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00643F52;
    v_stack_m58 = v_stack_p0;
    goto loc_00643F5F;
loc_00643F52:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C094B)) != 0) goto loc_00643F8B;
    if (((*(uint32_t *)(v_rip + 0x8C09F7)) & (0x800ULL)) == 0) goto loc_00643F9E;
loc_00643F8B:
    result = ExAcquireRundownProtection(v_rip + 9174766, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00643FD6;
loc_00643F9E:
    goto loc_00643FC0;
loc_00643FA7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00643FC0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00643FA7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9174703;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwOpenKeyTransacted(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00644053;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C08BE)) != 0) goto loc_00644008;
    if (((*(uint32_t *)(v_rip + 0x8C097A)) & (0x800ULL)) == 0) goto loc_0064401B;
loc_00644008:
    result = ExAcquireRundownProtection(v_rip + 9174641, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00644053;
loc_0064401B:
    local_rsi = (result) + (48);
    goto loc_0064403D;
loc_00644024:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0064403D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00644024;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9174578;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00643EF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00643EF0[BB_00643EF0]
  bb_00643F41[BB_00643F41]
  bb_00643F48[BB_00643F48]
  bb_00643F52[BB_00643F52]
  bb_00643F56[BB_00643F56]
  bb_00643F5F[BB_00643F5F]
  bb_00643F7F[BB_00643F7F]
  bb_00643F8B[BB_00643F8B]
  bb_00643F9E[BB_00643F9E]
  bb_00643FA7[BB_00643FA7]
  bb_00643FB0[BB_00643FB0]
  bb_00643FBD[BB_00643FBD]
  bb_00643FC0[BB_00643FC0]
  bb_00643FC5[BB_00643FC5]
  bb_00643FCA[BB_00643FCA]
  bb_00643FD6[BB_00643FD6]
  bb_00643FF0[BB_00643FF0]
  bb_00643FFC[BB_00643FFC]
  bb_00644008[BB_00644008]
  bb_0064401B[BB_0064401B]
  bb_00644024[BB_00644024]
  bb_0064402D[BB_0064402D]
  bb_0064403A[BB_0064403A]
  bb_0064403D[BB_0064403D]
  bb_00644042[BB_00644042]
  bb_00644047[BB_00644047]
  bb_00644053[BB_00644053]
  bb_00644074[BB_00644074]
  bb_00643EF0 -->|branch| bb_00643FD6
  bb_00643EF0 -->|fallthrough| bb_00643F41
  bb_00643F41 -->|branch| bb_00643F52
  bb_00643F41 -->|fallthrough| bb_00643F48
  bb_00643F48 -->|branch| bb_00643F5F
  bb_00643F52 -->|branch| bb_00643F5F
  bb_00643F52 -->|fallthrough| bb_00643F56
  bb_00643F56 -->|flow| bb_00643F5F
  bb_00643F5F -->|branch| bb_00643F8B
  bb_00643F5F -->|fallthrough| bb_00643F7F
  bb_00643F7F -->|branch| bb_00643F9E
  bb_00643F7F -->|fallthrough| bb_00643F8B
  bb_00643F8B -->|branch| bb_00643FD6
  bb_00643F8B -->|fallthrough| bb_00643F9E
  bb_00643F9E -->|branch| bb_00643FC0
  bb_00643FA7 -->|branch| bb_00643FBD
  bb_00643FA7 -->|fallthrough| bb_00643FB0
  bb_00643FB0 -->|flow| bb_00643FBD
  bb_00643FBD -->|flow| bb_00643FC0
  bb_00643FC0 -->|branch| bb_00643FA7
  bb_00643FC0 -->|fallthrough| bb_00643FC5
  bb_00643FC5 -->|branch| bb_00643FD6
  bb_00643FC5 -->|fallthrough| bb_00643FCA
  bb_00643FCA -->|flow| bb_00643FD6
  bb_00643FD6 -->|branch| bb_00644053
  bb_00643FD6 -->|fallthrough| bb_00643FF0
  bb_00643FF0 -->|branch| bb_00644008
  bb_00643FF0 -->|fallthrough| bb_00643FFC
  bb_00643FFC -->|branch| bb_0064401B
  bb_00643FFC -->|fallthrough| bb_00644008
  bb_00644008 -->|branch| bb_00644053
  bb_00644008 -->|fallthrough| bb_0064401B
  bb_0064401B -->|branch| bb_0064403D
  bb_00644024 -->|branch| bb_0064403A
  bb_00644024 -->|fallthrough| bb_0064402D
  bb_0064402D -->|flow| bb_0064403A
  bb_0064403A -->|flow| bb_0064403D
  bb_0064403D -->|branch| bb_00644024
  bb_0064403D -->|fallthrough| bb_00644042
  bb_00644042 -->|branch| bb_00644053
  bb_00644042 -->|fallthrough| bb_00644047
  bb_00644047 -->|flow| bb_00644053
```
