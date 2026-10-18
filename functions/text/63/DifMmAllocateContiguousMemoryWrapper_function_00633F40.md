# DifMmAllocateContiguousMemoryWrapper

- RVA: `0x00633F40`–`0x006340A6` (길이 `358` bytes)
- VA: `0x0000000140633F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00633F6E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00633F96` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00633FC9` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00633FF0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634009` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00634014` → [MmAllocateContiguousMemory](../67/MmAllocateContiguousMemory_function_006744C0.md) (function, `0x006744C0`)
- `0x00634042` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634069` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634082` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00633FA8` → RVA `0x00F048B8` (`.data`; read)
- `0x00633FB6` → RVA `0x00F04980` (`.data`; read)
- `0x00633FC2` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00633F40  48 8B C4                        mov rax, rsp
00633F43  48 89 58 08                     mov qword ptr [rax + 8], rbx
00633F47  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00633F4B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00633F4F  57                              push rdi
00633F50  41 56                           push r14
00633F52  41 57                           push r15
00633F54  48 83 EC 40                     sub rsp, 0x40
00633F58  0F 57 C0                        xorps xmm0, xmm0
00633F5B  4C 8B F9                        mov r15, rcx
00633F5E  B9 EE 00 00 00                  mov ecx, 0xee
00633F63  48 8B DA                        mov rbx, rdx
00633F66  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00633F6A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00633F6E  E8 C1 1A E6 FF                  call 0x140495a34
00633F73  48 8B F0                        mov rsi, rax
00633F76  48 85 C0                        test rax, rax
00633F79  0F 84 8F 00 00 00               je 0x14063400e
00633F7F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00633F82  A8 18                           test al, 0x18
00633F84  74 0C                           je 0x140633f92
00633F86  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00633F8B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00633F90  EB 0E                           jmp 0x140633fa0
00633F92  A8 04                           test al, 4
00633F94  74 0A                           je 0x140633fa0
00633F96  E8 6D FC E9 FF                  call 0x1404d3c08
00633F9B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00633FA0  40 32 ED                        xor bpl, bpl
00633FA3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00633FA8  40 38 2D 09 09 8D 00            cmp byte ptr [rip + 0x8d0909], bpl
00633FAF  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00633FB4  75 0C                           jne 0x140633fc2
00633FB6  F7 05 C0 09 8D 00 00 08 00 00   test dword ptr [rip + 0x8d09c0], 0x800
00633FC0  74 13                           je 0x140633fd5
00633FC2  48 8D 0D B7 FE 8C 00            lea rcx, [rip + 0x8cfeb7]
00633FC9  E8 52 26 BE FF                  call 0x140216620
00633FCE  40 8A E8                        mov bpl, al
00633FD1  84 C0                           test al, al
00633FD3  74 39                           je 0x14063400e
00633FD5  4C 8D 76 20                     lea r14, [rsi + 0x20]
00633FD9  49 8B 3E                        mov rdi, qword ptr [r14]
00633FDC  EB 1A                           jmp 0x140633ff8
00633FDE  48 8D 47 F0                     lea rax, [rdi - 0x10]
00633FE2  48 85 C0                        test rax, rax
00633FE5  74 0E                           je 0x140633ff5
00633FE7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633FEB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00633FF0  E8 DB 6A 08 00                  call 0x1406baad0
00633FF5  48 8B 3F                        mov rdi, qword ptr [rdi]
00633FF8  49 3B FE                        cmp rdi, r14
00633FFB  75 E1                           jne 0x140633fde
00633FFD  40 84 ED                        test bpl, bpl
00634000  74 0C                           je 0x14063400e
00634002  48 8D 0D 77 FE 8C 00            lea rcx, [rip + 0x8cfe77]
00634009  E8 72 5E D1 FF                  call 0x140349e80
0063400E  48 8B D3                        mov rdx, rbx
00634011  49 8B CF                        mov rcx, r15
00634014  E8 A7 04 04 00                  call 0x1406744c0
00634019  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0063401E  48 85 F6                        test rsi, rsi
00634021  74 64                           je 0x140634087
00634023  40 32 FF                        xor dil, dil
00634026  40 38 3D 8B 08 8D 00            cmp byte ptr [rip + 0x8d088b], dil
0063402D  75 0C                           jne 0x14063403b
0063402F  F7 05 47 09 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0947], 0x800
00634039  74 13                           je 0x14063404e
0063403B  48 8D 0D 3E FE 8C 00            lea rcx, [rip + 0x8cfe3e]
00634042  E8 D9 25 BE FF                  call 0x140216620
00634047  40 8A F8                        mov dil, al
0063404A  84 C0                           test al, al
0063404C  74 39                           je 0x140634087
0063404E  48 83 C6 30                     add rsi, 0x30
00634052  48 8B 1E                        mov rbx, qword ptr [rsi]
00634055  EB 1A                           jmp 0x140634071
00634057  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063405B  48 85 C0                        test rax, rax
0063405E  74 0E                           je 0x14063406e
00634060  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634064  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00634069  E8 62 6A 08 00                  call 0x1406baad0
0063406E  48 8B 1B                        mov rbx, qword ptr [rbx]
00634071  48 3B DE                        cmp rbx, rsi
00634074  75 E1                           jne 0x140634057
00634076  40 84 FF                        test dil, dil
00634079  74 0C                           je 0x140634087
0063407B  48 8D 0D FE FD 8C 00            lea rcx, [rip + 0x8cfdfe]
00634082  E8 F9 5D D1 FF                  call 0x140349e80
00634087  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0063408C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00634091  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00634096  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063409B  48 83 C4 40                     add rsp, 0x40
0063409F  41 5F                           pop r15
006340A1  41 5E                           pop r14
006340A3  5F                              pop rdi
006340A4  C3                              ret
006340A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocateContiguousMemoryWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
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
    result = DifGetAPIThunkContextById(238, a2, a3, a4);
    if (result == 0) goto loc_0063400E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00633F92;
    v_stack_m38 = v_stack_p0;
    goto loc_00633FA0;
loc_00633F92:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9242889)) != 0) goto loc_00633FC2;
    if (((*(unsigned int *)(v_rip + 9243072)) & (0x800ULL)) == 0) goto loc_00633FD5;
loc_00633FC2:
    result = ExAcquireRundownProtection(v_rip + 9240247, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063400E;
loc_00633FD5:
    goto loc_00633FF8;
loc_00633FDE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633FF8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00633FDE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9240183;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmAllocateContiguousMemory(a1, a2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00634087;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9242763)) != 0) goto loc_0063403B;
    if (((*(unsigned int *)(v_rip + 9242951)) & (0x800ULL)) == 0) goto loc_0063404E;
loc_0063403B:
    result = ExAcquireRundownProtection(v_rip + 9240126, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00634087;
loc_0063404E:
    v_rsi = (result) + (48);
    goto loc_00634071;
loc_00634057:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00634071:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00634057;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9240062;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocateContiguousMemoryWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
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
    result = DifGetAPIThunkContextById(238, Arg2, a3, a4);
    if (result == 0) goto loc_0063400E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00633F92;
    v_stack_m38 = v_stack_p0;
    goto loc_00633FA0;
loc_00633F92:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D0909)) != 0) goto loc_00633FC2;
    if (((*(uint32_t *)(v_rip + 0x8D09C0)) & (0x800ULL)) == 0) goto loc_00633FD5;
loc_00633FC2:
    result = ExAcquireRundownProtection(v_rip + 9240247, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063400E;
loc_00633FD5:
    goto loc_00633FF8;
loc_00633FDE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00633FF8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00633FDE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9240183;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = MmAllocateContiguousMemory(Arg1, Arg2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00634087;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D088B)) != 0) goto loc_0063403B;
    if (((*(uint32_t *)(v_rip + 0x8D0947)) & (0x800ULL)) == 0) goto loc_0063404E;
loc_0063403B:
    result = ExAcquireRundownProtection(v_rip + 9240126, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00634087;
loc_0063404E:
    local_rsi = (result) + (48);
    goto loc_00634071;
loc_00634057:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00634071:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00634057;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9240062;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00633F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00633F40[BB_00633F40]
  bb_00633F7F[BB_00633F7F]
  bb_00633F86[BB_00633F86]
  bb_00633F92[BB_00633F92]
  bb_00633F96[BB_00633F96]
  bb_00633FA0[BB_00633FA0]
  bb_00633FB6[BB_00633FB6]
  bb_00633FC2[BB_00633FC2]
  bb_00633FD5[BB_00633FD5]
  bb_00633FDE[BB_00633FDE]
  bb_00633FE7[BB_00633FE7]
  bb_00633FF5[BB_00633FF5]
  bb_00633FF8[BB_00633FF8]
  bb_00633FFD[BB_00633FFD]
  bb_00634002[BB_00634002]
  bb_0063400E[BB_0063400E]
  bb_00634023[BB_00634023]
  bb_0063402F[BB_0063402F]
  bb_0063403B[BB_0063403B]
  bb_0063404E[BB_0063404E]
  bb_00634057[BB_00634057]
  bb_00634060[BB_00634060]
  bb_0063406E[BB_0063406E]
  bb_00634071[BB_00634071]
  bb_00634076[BB_00634076]
  bb_0063407B[BB_0063407B]
  bb_00634087[BB_00634087]
  bb_006340A5[BB_006340A5]
  bb_00633F40 -->|branch| bb_0063400E
  bb_00633F40 -->|fallthrough| bb_00633F7F
  bb_00633F7F -->|branch| bb_00633F92
  bb_00633F7F -->|fallthrough| bb_00633F86
  bb_00633F86 -->|branch| bb_00633FA0
  bb_00633F92 -->|branch| bb_00633FA0
  bb_00633F92 -->|fallthrough| bb_00633F96
  bb_00633F96 -->|flow| bb_00633FA0
  bb_00633FA0 -->|branch| bb_00633FC2
  bb_00633FA0 -->|fallthrough| bb_00633FB6
  bb_00633FB6 -->|branch| bb_00633FD5
  bb_00633FB6 -->|fallthrough| bb_00633FC2
  bb_00633FC2 -->|branch| bb_0063400E
  bb_00633FC2 -->|fallthrough| bb_00633FD5
  bb_00633FD5 -->|branch| bb_00633FF8
  bb_00633FDE -->|branch| bb_00633FF5
  bb_00633FDE -->|fallthrough| bb_00633FE7
  bb_00633FE7 -->|flow| bb_00633FF5
  bb_00633FF5 -->|flow| bb_00633FF8
  bb_00633FF8 -->|branch| bb_00633FDE
  bb_00633FF8 -->|fallthrough| bb_00633FFD
  bb_00633FFD -->|branch| bb_0063400E
  bb_00633FFD -->|fallthrough| bb_00634002
  bb_00634002 -->|flow| bb_0063400E
  bb_0063400E -->|branch| bb_00634087
  bb_0063400E -->|fallthrough| bb_00634023
  bb_00634023 -->|branch| bb_0063403B
  bb_00634023 -->|fallthrough| bb_0063402F
  bb_0063402F -->|branch| bb_0063404E
  bb_0063402F -->|fallthrough| bb_0063403B
  bb_0063403B -->|branch| bb_00634087
  bb_0063403B -->|fallthrough| bb_0063404E
  bb_0063404E -->|branch| bb_00634071
  bb_00634057 -->|branch| bb_0063406E
  bb_00634057 -->|fallthrough| bb_00634060
  bb_00634060 -->|flow| bb_0063406E
  bb_0063406E -->|flow| bb_00634071
  bb_00634071 -->|branch| bb_00634057
  bb_00634071 -->|fallthrough| bb_00634076
  bb_00634076 -->|branch| bb_00634087
  bb_00634076 -->|fallthrough| bb_0063407B
  bb_0063407B -->|flow| bb_00634087
```
