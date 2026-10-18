# DifKeSetTimerWrapper

- RVA: `0x00632C30`–`0x00632DAF` (길이 `383` bytes)
- VA: `0x0000000140632C30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE68C`
- 디코드: `110`개 명령, `383/383` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00632C6E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00632C94` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00632CC8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632CEE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00632D07` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00632D1D` → [KiSetTimerEx](../23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)
- `0x00632D49` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632D6F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00632D88` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00632CA4` → RVA `0x00F048B8` (`.data`; read)
- `0x00632CB5` → RVA `0x00F04980` (`.data`; read)
- `0x00632CC1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00632C30  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00632C35  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00632C3A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00632C3F  55                              push rbp
00632C40  41 54                           push r12
00632C42  41 55                           push r13
00632C44  41 56                           push r14
00632C46  41 57                           push r15
00632C48  48 8B EC                        mov rbp, rsp
00632C4B  48 83 EC 60                     sub rsp, 0x60
00632C4F  0F 57 C0                        xorps xmm0, xmm0
00632C52  33 C0                           xor eax, eax
00632C54  4C 8B E9                        mov r13, rcx
00632C57  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00632C5B  B9 F8 00 00 00                  mov ecx, 0xf8
00632C60  4D 8B E0                        mov r12, r8
00632C63  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00632C67  48 8B DA                        mov rbx, rdx
00632C6A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00632C6E  E8 C1 2D E6 FF                  call 0x140495a34
00632C73  48 8B F0                        mov rsi, rax
00632C76  48 85 C0                        test rax, rax
00632C79  0F 84 8D 00 00 00               je 0x140632d0c
00632C7F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00632C82  A8 18                           test al, 0x18
00632C84  74 0A                           je 0x140632c90
00632C86  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00632C8A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00632C8E  EB 0D                           jmp 0x140632c9d
00632C90  A8 04                           test al, 4
00632C92  74 09                           je 0x140632c9d
00632C94  E8 6F 0F EA FF                  call 0x1404d3c08
00632C99  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00632C9D  45 32 FF                        xor r15b, r15b
00632CA0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00632CA4  44 38 3D 0D 1C 8D 00            cmp byte ptr [rip + 0x8d1c0d], r15b
00632CAB  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
00632CAF  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00632CB3  75 0C                           jne 0x140632cc1
00632CB5  F7 05 C1 1C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d1cc1], 0x800
00632CBF  74 13                           je 0x140632cd4
00632CC1  48 8D 0D B8 11 8D 00            lea rcx, [rip + 0x8d11b8]
00632CC8  E8 53 39 BE FF                  call 0x140216620
00632CCD  44 8A F8                        mov r15b, al
00632CD0  84 C0                           test al, al
00632CD2  74 38                           je 0x140632d0c
00632CD4  4C 8D 76 20                     lea r14, [rsi + 0x20]
00632CD8  49 8B 3E                        mov rdi, qword ptr [r14]
00632CDB  EB 19                           jmp 0x140632cf6
00632CDD  48 8D 47 F0                     lea rax, [rdi - 0x10]
00632CE1  48 85 C0                        test rax, rax
00632CE4  74 0D                           je 0x140632cf3
00632CE6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632CEA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00632CEE  E8 DD 7D 08 00                  call 0x1406baad0
00632CF3  48 8B 3F                        mov rdi, qword ptr [rdi]
00632CF6  49 3B FE                        cmp rdi, r14
00632CF9  75 E2                           jne 0x140632cdd
00632CFB  45 84 FF                        test r15b, r15b
00632CFE  74 0C                           je 0x140632d0c
00632D00  48 8D 0D 79 11 8D 00            lea rcx, [rip + 0x8d1179]
00632D07  E8 74 71 D1 FF                  call 0x140349e80
00632D0C  45 33 C9                        xor r9d, r9d
00632D0F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00632D14  45 33 C0                        xor r8d, r8d
00632D17  48 8B D3                        mov rdx, rbx
00632D1A  49 8B CD                        mov rcx, r13
00632D1D  E8 8E FF BF FF                  call 0x140232cb0
00632D22  88 45 F0                        mov byte ptr [rbp - 0x10], al
00632D25  48 85 F6                        test rsi, rsi
00632D28  74 63                           je 0x140632d8d
00632D2A  40 32 FF                        xor dil, dil
00632D2D  40 38 3D 84 1B 8D 00            cmp byte ptr [rip + 0x8d1b84], dil
00632D34  75 0C                           jne 0x140632d42
00632D36  F7 05 40 1C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d1c40], 0x800
00632D40  74 13                           je 0x140632d55
00632D42  48 8D 0D 37 11 8D 00            lea rcx, [rip + 0x8d1137]
00632D49  E8 D2 38 BE FF                  call 0x140216620
00632D4E  40 8A F8                        mov dil, al
00632D51  84 C0                           test al, al
00632D53  74 38                           je 0x140632d8d
00632D55  48 83 C6 30                     add rsi, 0x30
00632D59  48 8B 1E                        mov rbx, qword ptr [rsi]
00632D5C  EB 19                           jmp 0x140632d77
00632D5E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00632D62  48 85 C0                        test rax, rax
00632D65  74 0D                           je 0x140632d74
00632D67  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632D6B  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00632D6F  E8 5C 7D 08 00                  call 0x1406baad0
00632D74  48 8B 1B                        mov rbx, qword ptr [rbx]
00632D77  48 3B DE                        cmp rbx, rsi
00632D7A  75 E2                           jne 0x140632d5e
00632D7C  40 84 FF                        test dil, dil
00632D7F  74 0C                           je 0x140632d8d
00632D81  48 8D 0D F8 10 8D 00            lea rcx, [rip + 0x8d10f8]
00632D88  E8 F3 70 D1 FF                  call 0x140349e80
00632D8D  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
00632D90  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00632D95  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00632D99  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00632D9D  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00632DA1  49 8B E3                        mov rsp, r11
00632DA4  41 5F                           pop r15
00632DA6  41 5E                           pop r14
00632DA8  41 5D                           pop r13
00632DAA  41 5C                           pop r12
00632DAC  5D                              pop rbp
00632DAD  C3                              ret
00632DAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeSetTimerWrapper(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(248, a2, a3, a4);
    if (result == 0) goto loc_00632D0C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00632C90;
    v_stack_m58 = v_stack_p0;
    goto loc_00632C9D;
loc_00632C90:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r15 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9247757)) != 0) goto loc_00632CC1;
    if (((*(unsigned int *)(v_rip + 9247937)) & (0x800ULL)) == 0) goto loc_00632CD4;
loc_00632CC1:
    result = ExAcquireRundownProtection(v_rip + 9245112, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00632D0C;
loc_00632CD4:
    goto loc_00632CF6;
loc_00632CDD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632CF6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00632CDD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9245049;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a4 = 0;
    v_stack_m68 = a3;
    a3 = 0;
    result = KiSetTimerEx(a1, a2, a3, a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_00632D8D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9247620)) != 0) goto loc_00632D42;
    if (((*(unsigned int *)(v_rip + 9247808)) & (0x800ULL)) == 0) goto loc_00632D55;
loc_00632D42:
    result = ExAcquireRundownProtection(v_rip + 9244983, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00632D8D;
loc_00632D55:
    v_rsi = (result) + (48);
    goto loc_00632D77;
loc_00632D5E:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632D77:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00632D5E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9244920;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeSetTimerWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(248, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00632D0C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00632C90;
    v_stack_m58 = v_stack_p0;
    goto loc_00632C9D;
loc_00632C90:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r15 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D1C0D)) != 0) goto loc_00632CC1;
    if (((*(uint32_t *)(v_rip + 0x8D1CC1)) & (0x800ULL)) == 0) goto loc_00632CD4;
loc_00632CC1:
    result = ExAcquireRundownProtection(v_rip + 9245112, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00632D0C;
loc_00632CD4:
    goto loc_00632CF6;
loc_00632CDD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00632CF6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00632CDD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9245049;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    v_stack_m68 = Arg3;
    Arg3 = 0;
    result = KiSetTimerEx(Arg1, Arg2, Arg3, Arg4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_00632D8D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D1B84)) != 0) goto loc_00632D42;
    if (((*(uint32_t *)(v_rip + 0x8D1C40)) & (0x800ULL)) == 0) goto loc_00632D55;
loc_00632D42:
    result = ExAcquireRundownProtection(v_rip + 9244983, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00632D8D;
loc_00632D55:
    local_rsi = (result) + (48);
    goto loc_00632D77;
loc_00632D5E:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00632D77:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00632D5E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9244920;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00632C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00632C30[BB_00632C30]
  bb_00632C7F[BB_00632C7F]
  bb_00632C86[BB_00632C86]
  bb_00632C90[BB_00632C90]
  bb_00632C94[BB_00632C94]
  bb_00632C9D[BB_00632C9D]
  bb_00632CB5[BB_00632CB5]
  bb_00632CC1[BB_00632CC1]
  bb_00632CD4[BB_00632CD4]
  bb_00632CDD[BB_00632CDD]
  bb_00632CE6[BB_00632CE6]
  bb_00632CF3[BB_00632CF3]
  bb_00632CF6[BB_00632CF6]
  bb_00632CFB[BB_00632CFB]
  bb_00632D00[BB_00632D00]
  bb_00632D0C[BB_00632D0C]
  bb_00632D2A[BB_00632D2A]
  bb_00632D36[BB_00632D36]
  bb_00632D42[BB_00632D42]
  bb_00632D55[BB_00632D55]
  bb_00632D5E[BB_00632D5E]
  bb_00632D67[BB_00632D67]
  bb_00632D74[BB_00632D74]
  bb_00632D77[BB_00632D77]
  bb_00632D7C[BB_00632D7C]
  bb_00632D81[BB_00632D81]
  bb_00632D8D[BB_00632D8D]
  bb_00632DAE[BB_00632DAE]
  bb_00632C30 -->|branch| bb_00632D0C
  bb_00632C30 -->|fallthrough| bb_00632C7F
  bb_00632C7F -->|branch| bb_00632C90
  bb_00632C7F -->|fallthrough| bb_00632C86
  bb_00632C86 -->|branch| bb_00632C9D
  bb_00632C90 -->|branch| bb_00632C9D
  bb_00632C90 -->|fallthrough| bb_00632C94
  bb_00632C94 -->|flow| bb_00632C9D
  bb_00632C9D -->|branch| bb_00632CC1
  bb_00632C9D -->|fallthrough| bb_00632CB5
  bb_00632CB5 -->|branch| bb_00632CD4
  bb_00632CB5 -->|fallthrough| bb_00632CC1
  bb_00632CC1 -->|branch| bb_00632D0C
  bb_00632CC1 -->|fallthrough| bb_00632CD4
  bb_00632CD4 -->|branch| bb_00632CF6
  bb_00632CDD -->|branch| bb_00632CF3
  bb_00632CDD -->|fallthrough| bb_00632CE6
  bb_00632CE6 -->|flow| bb_00632CF3
  bb_00632CF3 -->|flow| bb_00632CF6
  bb_00632CF6 -->|branch| bb_00632CDD
  bb_00632CF6 -->|fallthrough| bb_00632CFB
  bb_00632CFB -->|branch| bb_00632D0C
  bb_00632CFB -->|fallthrough| bb_00632D00
  bb_00632D00 -->|flow| bb_00632D0C
  bb_00632D0C -->|branch| bb_00632D8D
  bb_00632D0C -->|fallthrough| bb_00632D2A
  bb_00632D2A -->|branch| bb_00632D42
  bb_00632D2A -->|fallthrough| bb_00632D36
  bb_00632D36 -->|branch| bb_00632D55
  bb_00632D36 -->|fallthrough| bb_00632D42
  bb_00632D42 -->|branch| bb_00632D8D
  bb_00632D42 -->|fallthrough| bb_00632D55
  bb_00632D55 -->|branch| bb_00632D77
  bb_00632D5E -->|branch| bb_00632D74
  bb_00632D5E -->|fallthrough| bb_00632D67
  bb_00632D67 -->|flow| bb_00632D74
  bb_00632D74 -->|flow| bb_00632D77
  bb_00632D77 -->|branch| bb_00632D5E
  bb_00632D77 -->|fallthrough| bb_00632D7C
  bb_00632D7C -->|branch| bb_00632D8D
  bb_00632D7C -->|fallthrough| bb_00632D81
  bb_00632D81 -->|flow| bb_00632D8D
```
