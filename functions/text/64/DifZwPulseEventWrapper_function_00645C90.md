# DifZwPulseEventWrapper

- RVA: `0x00645C90`–`0x00645DF4` (길이 `356` bytes)
- VA: `0x0000000140645C90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00645CBE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00645CE6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645D19` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645D40` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645D59` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00645D64` → [ZwPulseEvent](../6A/ZwPulseEvent_function_006AF9F0.md) (function, `0x006AF9F0`)
- `0x00645D91` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645DB8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645DD1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645CF8` → RVA `0x00F048B8` (`.data`; read)
- `0x00645D06` → RVA `0x00F04980` (`.data`; read)
- `0x00645D12` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645C90  48 8B C4                        mov rax, rsp
00645C93  48 89 58 08                     mov qword ptr [rax + 8], rbx
00645C97  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00645C9B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00645C9F  57                              push rdi
00645CA0  41 56                           push r14
00645CA2  41 57                           push r15
00645CA4  48 83 EC 40                     sub rsp, 0x40
00645CA8  0F 57 C0                        xorps xmm0, xmm0
00645CAB  4C 8B F9                        mov r15, rcx
00645CAE  B9 3E 00 00 00                  mov ecx, 0x3e
00645CB3  4C 8B F2                        mov r14, rdx
00645CB6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00645CBA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00645CBE  E8 71 FD E4 FF                  call 0x140495a34
00645CC3  48 8B F0                        mov rsi, rax
00645CC6  48 85 C0                        test rax, rax
00645CC9  0F 84 8F 00 00 00               je 0x140645d5e
00645CCF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00645CD2  A8 18                           test al, 0x18
00645CD4  74 0C                           je 0x140645ce2
00645CD6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00645CDB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00645CE0  EB 0E                           jmp 0x140645cf0
00645CE2  A8 04                           test al, 4
00645CE4  74 0A                           je 0x140645cf0
00645CE6  E8 1D DF E8 FF                  call 0x1404d3c08
00645CEB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00645CF0  40 32 ED                        xor bpl, bpl
00645CF3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00645CF8  40 38 2D B9 EB 8B 00            cmp byte ptr [rip + 0x8bebb9], bpl
00645CFF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00645D04  75 0C                           jne 0x140645d12
00645D06  F7 05 70 EC 8B 00 00 08 00 00   test dword ptr [rip + 0x8bec70], 0x800
00645D10  74 13                           je 0x140645d25
00645D12  48 8D 0D 67 E1 8B 00            lea rcx, [rip + 0x8be167]
00645D19  E8 02 09 BD FF                  call 0x140216620
00645D1E  40 8A E8                        mov bpl, al
00645D21  84 C0                           test al, al
00645D23  74 39                           je 0x140645d5e
00645D25  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00645D29  48 8B 1F                        mov rbx, qword ptr [rdi]
00645D2C  EB 1A                           jmp 0x140645d48
00645D2E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645D32  48 85 C0                        test rax, rax
00645D35  74 0E                           je 0x140645d45
00645D37  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645D3B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645D40  E8 8B 4D 07 00                  call 0x1406baad0
00645D45  48 8B 1B                        mov rbx, qword ptr [rbx]
00645D48  48 3B DF                        cmp rbx, rdi
00645D4B  75 E1                           jne 0x140645d2e
00645D4D  40 84 ED                        test bpl, bpl
00645D50  74 0C                           je 0x140645d5e
00645D52  48 8D 0D 27 E1 8B 00            lea rcx, [rip + 0x8be127]
00645D59  E8 22 41 D0 FF                  call 0x140349e80
00645D5E  49 8B D6                        mov rdx, r14
00645D61  49 8B CF                        mov rcx, r15
00645D64  E8 87 9C 06 00                  call 0x1406af9f0
00645D69  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00645D6D  48 85 F6                        test rsi, rsi
00645D70  74 64                           je 0x140645dd6
00645D72  40 32 FF                        xor dil, dil
00645D75  40 38 3D 3C EB 8B 00            cmp byte ptr [rip + 0x8beb3c], dil
00645D7C  75 0C                           jne 0x140645d8a
00645D7E  F7 05 F8 EB 8B 00 00 08 00 00   test dword ptr [rip + 0x8bebf8], 0x800
00645D88  74 13                           je 0x140645d9d
00645D8A  48 8D 0D EF E0 8B 00            lea rcx, [rip + 0x8be0ef]
00645D91  E8 8A 08 BD FF                  call 0x140216620
00645D96  40 8A F8                        mov dil, al
00645D99  84 C0                           test al, al
00645D9B  74 39                           je 0x140645dd6
00645D9D  48 83 C6 30                     add rsi, 0x30
00645DA1  48 8B 1E                        mov rbx, qword ptr [rsi]
00645DA4  EB 1A                           jmp 0x140645dc0
00645DA6  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645DAA  48 85 C0                        test rax, rax
00645DAD  74 0E                           je 0x140645dbd
00645DAF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645DB3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00645DB8  E8 13 4D 07 00                  call 0x1406baad0
00645DBD  48 8B 1B                        mov rbx, qword ptr [rbx]
00645DC0  48 3B DE                        cmp rbx, rsi
00645DC3  75 E1                           jne 0x140645da6
00645DC5  40 84 FF                        test dil, dil
00645DC8  74 0C                           je 0x140645dd6
00645DCA  48 8D 0D AF E0 8B 00            lea rcx, [rip + 0x8be0af]
00645DD1  E8 AA 40 D0 FF                  call 0x140349e80
00645DD6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00645DDA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00645DDF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00645DE4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00645DE9  48 83 C4 40                     add rsp, 0x40
00645DED  41 5F                           pop r15
00645DEF  41 5E                           pop r14
00645DF1  5F                              pop rdi
00645DF2  C3                              ret
00645DF3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwPulseEventWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(62, a2, a3, a4);
    if (result == 0) goto loc_00645D5E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00645CE2;
    v_stack_m38 = v_stack_p0;
    goto loc_00645CF0;
loc_00645CE2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9169849)) != 0) goto loc_00645D12;
    if (((*(unsigned int *)(v_rip + 9170032)) & (0x800ULL)) == 0) goto loc_00645D25;
loc_00645D12:
    result = ExAcquireRundownProtection(v_rip + 9167207, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645D5E;
loc_00645D25:
    goto loc_00645D48;
loc_00645D2E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645D48:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00645D2E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167143;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwPulseEvent(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00645DD6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9169724)) != 0) goto loc_00645D8A;
    if (((*(unsigned int *)(v_rip + 9169912)) & (0x800ULL)) == 0) goto loc_00645D9D;
loc_00645D8A:
    result = ExAcquireRundownProtection(v_rip + 9167087, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645DD6;
loc_00645D9D:
    v_rsi = (result) + (48);
    goto loc_00645DC0;
loc_00645DA6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645DC0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00645DA6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167023;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwPulseEventWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(62, Arg2, a3, a4);
    if (result == 0) goto loc_00645D5E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00645CE2;
    v_stack_m38 = v_stack_p0;
    goto loc_00645CF0;
loc_00645CE2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8BEBB9)) != 0) goto loc_00645D12;
    if (((*(uint32_t *)(v_rip + 0x8BEC70)) & (0x800ULL)) == 0) goto loc_00645D25;
loc_00645D12:
    result = ExAcquireRundownProtection(v_rip + 9167207, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645D5E;
loc_00645D25:
    goto loc_00645D48;
loc_00645D2E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645D48:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00645D2E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167143;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwPulseEvent(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00645DD6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BEB3C)) != 0) goto loc_00645D8A;
    if (((*(uint32_t *)(v_rip + 0x8BEBF8)) & (0x800ULL)) == 0) goto loc_00645D9D;
loc_00645D8A:
    result = ExAcquireRundownProtection(v_rip + 9167087, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00645DD6;
loc_00645D9D:
    local_rsi = (result) + (48);
    goto loc_00645DC0;
loc_00645DA6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00645DC0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00645DA6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167023;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645C90[BB_00645C90]
  bb_00645CCF[BB_00645CCF]
  bb_00645CD6[BB_00645CD6]
  bb_00645CE2[BB_00645CE2]
  bb_00645CE6[BB_00645CE6]
  bb_00645CF0[BB_00645CF0]
  bb_00645D06[BB_00645D06]
  bb_00645D12[BB_00645D12]
  bb_00645D25[BB_00645D25]
  bb_00645D2E[BB_00645D2E]
  bb_00645D37[BB_00645D37]
  bb_00645D45[BB_00645D45]
  bb_00645D48[BB_00645D48]
  bb_00645D4D[BB_00645D4D]
  bb_00645D52[BB_00645D52]
  bb_00645D5E[BB_00645D5E]
  bb_00645D72[BB_00645D72]
  bb_00645D7E[BB_00645D7E]
  bb_00645D8A[BB_00645D8A]
  bb_00645D9D[BB_00645D9D]
  bb_00645DA6[BB_00645DA6]
  bb_00645DAF[BB_00645DAF]
  bb_00645DBD[BB_00645DBD]
  bb_00645DC0[BB_00645DC0]
  bb_00645DC5[BB_00645DC5]
  bb_00645DCA[BB_00645DCA]
  bb_00645DD6[BB_00645DD6]
  bb_00645DF3[BB_00645DF3]
  bb_00645C90 -->|branch| bb_00645D5E
  bb_00645C90 -->|fallthrough| bb_00645CCF
  bb_00645CCF -->|branch| bb_00645CE2
  bb_00645CCF -->|fallthrough| bb_00645CD6
  bb_00645CD6 -->|branch| bb_00645CF0
  bb_00645CE2 -->|branch| bb_00645CF0
  bb_00645CE2 -->|fallthrough| bb_00645CE6
  bb_00645CE6 -->|flow| bb_00645CF0
  bb_00645CF0 -->|branch| bb_00645D12
  bb_00645CF0 -->|fallthrough| bb_00645D06
  bb_00645D06 -->|branch| bb_00645D25
  bb_00645D06 -->|fallthrough| bb_00645D12
  bb_00645D12 -->|branch| bb_00645D5E
  bb_00645D12 -->|fallthrough| bb_00645D25
  bb_00645D25 -->|branch| bb_00645D48
  bb_00645D2E -->|branch| bb_00645D45
  bb_00645D2E -->|fallthrough| bb_00645D37
  bb_00645D37 -->|flow| bb_00645D45
  bb_00645D45 -->|flow| bb_00645D48
  bb_00645D48 -->|branch| bb_00645D2E
  bb_00645D48 -->|fallthrough| bb_00645D4D
  bb_00645D4D -->|branch| bb_00645D5E
  bb_00645D4D -->|fallthrough| bb_00645D52
  bb_00645D52 -->|flow| bb_00645D5E
  bb_00645D5E -->|branch| bb_00645DD6
  bb_00645D5E -->|fallthrough| bb_00645D72
  bb_00645D72 -->|branch| bb_00645D8A
  bb_00645D72 -->|fallthrough| bb_00645D7E
  bb_00645D7E -->|branch| bb_00645D9D
  bb_00645D7E -->|fallthrough| bb_00645D8A
  bb_00645D8A -->|branch| bb_00645DD6
  bb_00645D8A -->|fallthrough| bb_00645D9D
  bb_00645D9D -->|branch| bb_00645DC0
  bb_00645DA6 -->|branch| bb_00645DBD
  bb_00645DA6 -->|fallthrough| bb_00645DAF
  bb_00645DAF -->|flow| bb_00645DBD
  bb_00645DBD -->|flow| bb_00645DC0
  bb_00645DC0 -->|branch| bb_00645DA6
  bb_00645DC0 -->|fallthrough| bb_00645DC5
  bb_00645DC5 -->|branch| bb_00645DD6
  bb_00645DC5 -->|fallthrough| bb_00645DCA
  bb_00645DCA -->|flow| bb_00645DD6
```
