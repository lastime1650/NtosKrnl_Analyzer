# DifMmMapIoSpaceWrapper

- RVA: `0x00635BE0`–`0x00635D59` (길이 `377` bytes)
- VA: `0x0000000140635BE0`
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
- `0x00635C1E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00635C44` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00635C78` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635C9E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635CB7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00635CC5` → [MmMapIoSpace](../48/MmMapIoSpace_function_00488A20.md) (function, `0x00488A20`)
- `0x00635CF2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635D18` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635D31` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00635C54` → RVA `0x00F048B8` (`.data`; read)
- `0x00635C65` → RVA `0x00F04980` (`.data`; read)
- `0x00635C71` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635BE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00635BE5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00635BEA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00635BEF  55                              push rbp
00635BF0  41 54                           push r12
00635BF2  41 55                           push r13
00635BF4  41 56                           push r14
00635BF6  41 57                           push r15
00635BF8  48 8B EC                        mov rbp, rsp
00635BFB  48 83 EC 50                     sub rsp, 0x50
00635BFF  0F 57 C0                        xorps xmm0, xmm0
00635C02  33 C0                           xor eax, eax
00635C04  48 8B D9                        mov rbx, rcx
00635C07  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00635C0B  B9 DD 00 00 00                  mov ecx, 0xdd
00635C10  45 8B E0                        mov r12d, r8d
00635C13  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00635C17  4C 8B EA                        mov r13, rdx
00635C1A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00635C1E  E8 11 FE E5 FF                  call 0x140495a34
00635C23  48 8B F0                        mov rsi, rax
00635C26  48 85 C0                        test rax, rax
00635C29  0F 84 8D 00 00 00               je 0x140635cbc
00635C2F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00635C32  A8 18                           test al, 0x18
00635C34  74 0A                           je 0x140635c40
00635C36  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00635C3A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00635C3E  EB 0D                           jmp 0x140635c4d
00635C40  A8 04                           test al, 4
00635C42  74 09                           je 0x140635c4d
00635C44  E8 BF DF E9 FF                  call 0x1404d3c08
00635C49  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00635C4D  45 32 FF                        xor r15b, r15b
00635C50  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00635C54  44 38 3D 5D EC 8C 00            cmp byte ptr [rip + 0x8cec5d], r15b
00635C5B  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
00635C5F  44 89 65 D8                     mov dword ptr [rbp - 0x28], r12d
00635C63  75 0C                           jne 0x140635c71
00635C65  F7 05 11 ED 8C 00 00 08 00 00   test dword ptr [rip + 0x8ced11], 0x800
00635C6F  74 13                           je 0x140635c84
00635C71  48 8D 0D 08 E2 8C 00            lea rcx, [rip + 0x8ce208]
00635C78  E8 A3 09 BE FF                  call 0x140216620
00635C7D  44 8A F8                        mov r15b, al
00635C80  84 C0                           test al, al
00635C82  74 38                           je 0x140635cbc
00635C84  4C 8D 76 20                     lea r14, [rsi + 0x20]
00635C88  49 8B 3E                        mov rdi, qword ptr [r14]
00635C8B  EB 19                           jmp 0x140635ca6
00635C8D  48 8D 47 F0                     lea rax, [rdi - 0x10]
00635C91  48 85 C0                        test rax, rax
00635C94  74 0D                           je 0x140635ca3
00635C96  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635C9A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00635C9E  E8 2D 4E 08 00                  call 0x1406baad0
00635CA3  48 8B 3F                        mov rdi, qword ptr [rdi]
00635CA6  49 3B FE                        cmp rdi, r14
00635CA9  75 E2                           jne 0x140635c8d
00635CAB  45 84 FF                        test r15b, r15b
00635CAE  74 0C                           je 0x140635cbc
00635CB0  48 8D 0D C9 E1 8C 00            lea rcx, [rip + 0x8ce1c9]
00635CB7  E8 C4 41 D1 FF                  call 0x140349e80
00635CBC  45 8B C4                        mov r8d, r12d
00635CBF  49 8B D5                        mov rdx, r13
00635CC2  48 8B CB                        mov rcx, rbx
00635CC5  E8 56 2D E5 FF                  call 0x140488a20
00635CCA  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00635CCE  48 85 F6                        test rsi, rsi
00635CD1  74 63                           je 0x140635d36
00635CD3  40 32 FF                        xor dil, dil
00635CD6  40 38 3D DB EB 8C 00            cmp byte ptr [rip + 0x8cebdb], dil
00635CDD  75 0C                           jne 0x140635ceb
00635CDF  F7 05 97 EC 8C 00 00 08 00 00   test dword ptr [rip + 0x8cec97], 0x800
00635CE9  74 13                           je 0x140635cfe
00635CEB  48 8D 0D 8E E1 8C 00            lea rcx, [rip + 0x8ce18e]
00635CF2  E8 29 09 BE FF                  call 0x140216620
00635CF7  40 8A F8                        mov dil, al
00635CFA  84 C0                           test al, al
00635CFC  74 38                           je 0x140635d36
00635CFE  48 83 C6 30                     add rsi, 0x30
00635D02  48 8B 1E                        mov rbx, qword ptr [rsi]
00635D05  EB 19                           jmp 0x140635d20
00635D07  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635D0B  48 85 C0                        test rax, rax
00635D0E  74 0D                           je 0x140635d1d
00635D10  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635D14  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00635D18  E8 B3 4D 08 00                  call 0x1406baad0
00635D1D  48 8B 1B                        mov rbx, qword ptr [rbx]
00635D20  48 3B DE                        cmp rbx, rsi
00635D23  75 E2                           jne 0x140635d07
00635D25  40 84 FF                        test dil, dil
00635D28  74 0C                           je 0x140635d36
00635D2A  48 8D 0D 4F E1 8C 00            lea rcx, [rip + 0x8ce14f]
00635D31  E8 4A 41 D1 FF                  call 0x140349e80
00635D36  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00635D3A  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00635D3F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00635D43  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00635D47  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00635D4B  49 8B E3                        mov rsp, r11
00635D4E  41 5F                           pop r15
00635D50  41 5E                           pop r14
00635D52  41 5D                           pop r13
00635D54  41 5C                           pop r12
00635D56  5D                              pop rbp
00635D57  C3                              ret
00635D58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmMapIoSpaceWrapper(__int64 a1, __int64 a2, int a3)
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
    unsigned int v_stack_m50;
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
    result = DifGetAPIThunkContextById(221, a2, a3, a4);
    if (result == 0) goto loc_00635CBC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00635C40;
    v_stack_m58 = v_stack_p0;
    goto loc_00635C4D;
loc_00635C40:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r15 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9235549)) != 0) goto loc_00635C71;
    if (((*(unsigned int *)(v_rip + 9235729)) & (0x800ULL)) == 0) goto loc_00635C84;
loc_00635C71:
    result = ExAcquireRundownProtection(v_rip + 9232904, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635CBC;
loc_00635C84:
    goto loc_00635CA6;
loc_00635C8D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635CA6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635C8D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9232841;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmMapIoSpace(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00635D36;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9235419)) != 0) goto loc_00635CEB;
    if (((*(unsigned int *)(v_rip + 9235607)) & (0x800ULL)) == 0) goto loc_00635CFE;
loc_00635CEB:
    result = ExAcquireRundownProtection(v_rip + 9232782, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635D36;
loc_00635CFE:
    v_rsi = (result) + (48);
    goto loc_00635D20;
loc_00635D07:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00635D20:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00635D07;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9232719;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmMapIoSpaceWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
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
    uint32_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(221, Arg2, Arg3, a4);
    if (result == 0) goto loc_00635CBC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00635C40;
    v_stack_m58 = v_stack_p0;
    goto loc_00635C4D;
loc_00635C40:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r15 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8CEC5D)) != 0) goto loc_00635C71;
    if (((*(uint32_t *)(v_rip + 0x8CED11)) & (0x800ULL)) == 0) goto loc_00635C84;
loc_00635C71:
    result = ExAcquireRundownProtection(v_rip + 9232904, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00635CBC;
loc_00635C84:
    goto loc_00635CA6;
loc_00635C8D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00635CA6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635C8D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9232841;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = MmMapIoSpace(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00635D36;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CEBDB)) != 0) goto loc_00635CEB;
    if (((*(uint32_t *)(v_rip + 0x8CEC97)) & (0x800ULL)) == 0) goto loc_00635CFE;
loc_00635CEB:
    result = ExAcquireRundownProtection(v_rip + 9232782, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_00635D36;
loc_00635CFE:
    local_rsi = (result) + (48);
    goto loc_00635D20;
loc_00635D07:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_00635D20:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00635D07;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9232719;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635BE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635BE0[BB_00635BE0]
  bb_00635C2F[BB_00635C2F]
  bb_00635C36[BB_00635C36]
  bb_00635C40[BB_00635C40]
  bb_00635C44[BB_00635C44]
  bb_00635C4D[BB_00635C4D]
  bb_00635C65[BB_00635C65]
  bb_00635C71[BB_00635C71]
  bb_00635C84[BB_00635C84]
  bb_00635C8D[BB_00635C8D]
  bb_00635C96[BB_00635C96]
  bb_00635CA3[BB_00635CA3]
  bb_00635CA6[BB_00635CA6]
  bb_00635CAB[BB_00635CAB]
  bb_00635CB0[BB_00635CB0]
  bb_00635CBC[BB_00635CBC]
  bb_00635CD3[BB_00635CD3]
  bb_00635CDF[BB_00635CDF]
  bb_00635CEB[BB_00635CEB]
  bb_00635CFE[BB_00635CFE]
  bb_00635D07[BB_00635D07]
  bb_00635D10[BB_00635D10]
  bb_00635D1D[BB_00635D1D]
  bb_00635D20[BB_00635D20]
  bb_00635D25[BB_00635D25]
  bb_00635D2A[BB_00635D2A]
  bb_00635D36[BB_00635D36]
  bb_00635D58[BB_00635D58]
  bb_00635BE0 -->|branch| bb_00635CBC
  bb_00635BE0 -->|fallthrough| bb_00635C2F
  bb_00635C2F -->|branch| bb_00635C40
  bb_00635C2F -->|fallthrough| bb_00635C36
  bb_00635C36 -->|branch| bb_00635C4D
  bb_00635C40 -->|branch| bb_00635C4D
  bb_00635C40 -->|fallthrough| bb_00635C44
  bb_00635C44 -->|flow| bb_00635C4D
  bb_00635C4D -->|branch| bb_00635C71
  bb_00635C4D -->|fallthrough| bb_00635C65
  bb_00635C65 -->|branch| bb_00635C84
  bb_00635C65 -->|fallthrough| bb_00635C71
  bb_00635C71 -->|branch| bb_00635CBC
  bb_00635C71 -->|fallthrough| bb_00635C84
  bb_00635C84 -->|branch| bb_00635CA6
  bb_00635C8D -->|branch| bb_00635CA3
  bb_00635C8D -->|fallthrough| bb_00635C96
  bb_00635C96 -->|flow| bb_00635CA3
  bb_00635CA3 -->|flow| bb_00635CA6
  bb_00635CA6 -->|branch| bb_00635C8D
  bb_00635CA6 -->|fallthrough| bb_00635CAB
  bb_00635CAB -->|branch| bb_00635CBC
  bb_00635CAB -->|fallthrough| bb_00635CB0
  bb_00635CB0 -->|flow| bb_00635CBC
  bb_00635CBC -->|branch| bb_00635D36
  bb_00635CBC -->|fallthrough| bb_00635CD3
  bb_00635CD3 -->|branch| bb_00635CEB
  bb_00635CD3 -->|fallthrough| bb_00635CDF
  bb_00635CDF -->|branch| bb_00635CFE
  bb_00635CDF -->|fallthrough| bb_00635CEB
  bb_00635CEB -->|branch| bb_00635D36
  bb_00635CEB -->|fallthrough| bb_00635CFE
  bb_00635CFE -->|branch| bb_00635D20
  bb_00635D07 -->|branch| bb_00635D1D
  bb_00635D07 -->|fallthrough| bb_00635D10
  bb_00635D10 -->|flow| bb_00635D1D
  bb_00635D1D -->|flow| bb_00635D20
  bb_00635D20 -->|branch| bb_00635D07
  bb_00635D20 -->|fallthrough| bb_00635D25
  bb_00635D25 -->|branch| bb_00635D36
  bb_00635D25 -->|fallthrough| bb_00635D2A
  bb_00635D2A -->|flow| bb_00635D36
```
