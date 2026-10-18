# DifKeTryToAcquireQueuedSpinLockWrapper

- RVA: `0x00633220`–`0x00633384` (길이 `356` bytes)
- VA: `0x0000000140633220`
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
- `0x0063324E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00633276` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006332A9` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006332D0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006332E9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006332F4` → [KeTryToAcquireQueuedSpinLock](../5B/KeTryToAcquireQueuedSpinLock_function_005BD470.md) (function, `0x005BD470`)
- `0x00633321` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00633348` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633361` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00633288` → RVA `0x00F048B8` (`.data`; read)
- `0x00633296` → RVA `0x00F04980` (`.data`; read)
- `0x006332A2` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00633220  48 8B C4                        mov rax, rsp
00633223  48 89 58 08                     mov qword ptr [rax + 8], rbx
00633227  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063322B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063322F  57                              push rdi
00633230  41 56                           push r14
00633232  41 57                           push r15
00633234  48 83 EC 40                     sub rsp, 0x40
00633238  0F 57 C0                        xorps xmm0, xmm0
0063323B  4C 8B F9                        mov r15, rcx
0063323E  B9 F4 00 00 00                  mov ecx, 0xf4
00633243  4C 8B F2                        mov r14, rdx
00633246  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063324A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063324E  E8 E1 27 E6 FF                  call 0x140495a34
00633253  48 8B F0                        mov rsi, rax
00633256  48 85 C0                        test rax, rax
00633259  0F 84 8F 00 00 00               je 0x1406332ee
0063325F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00633262  A8 18                           test al, 0x18
00633264  74 0C                           je 0x140633272
00633266  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063326B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00633270  EB 0E                           jmp 0x140633280
00633272  A8 04                           test al, 4
00633274  74 0A                           je 0x140633280
00633276  E8 8D 09 EA FF                  call 0x1404d3c08
0063327B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00633280  40 32 ED                        xor bpl, bpl
00633283  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00633288  40 38 2D 29 16 8D 00            cmp byte ptr [rip + 0x8d1629], bpl
0063328F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00633294  75 0C                           jne 0x1406332a2
00633296  F7 05 E0 16 8D 00 00 08 00 00   test dword ptr [rip + 0x8d16e0], 0x800
006332A0  74 13                           je 0x1406332b5
006332A2  48 8D 0D D7 0B 8D 00            lea rcx, [rip + 0x8d0bd7]
006332A9  E8 72 33 BE FF                  call 0x140216620
006332AE  40 8A E8                        mov bpl, al
006332B1  84 C0                           test al, al
006332B3  74 39                           je 0x1406332ee
006332B5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006332B9  48 8B 1F                        mov rbx, qword ptr [rdi]
006332BC  EB 1A                           jmp 0x1406332d8
006332BE  48 8D 43 F0                     lea rax, [rbx - 0x10]
006332C2  48 85 C0                        test rax, rax
006332C5  74 0E                           je 0x1406332d5
006332C7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006332CB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006332D0  E8 FB 77 08 00                  call 0x1406baad0
006332D5  48 8B 1B                        mov rbx, qword ptr [rbx]
006332D8  48 3B DF                        cmp rbx, rdi
006332DB  75 E1                           jne 0x1406332be
006332DD  40 84 ED                        test bpl, bpl
006332E0  74 0C                           je 0x1406332ee
006332E2  48 8D 0D 97 0B 8D 00            lea rcx, [rip + 0x8d0b97]
006332E9  E8 92 6B D1 FF                  call 0x140349e80
006332EE  49 8B D6                        mov rdx, r14
006332F1  49 8B CF                        mov rcx, r15
006332F4  E8 77 A1 F8 FF                  call 0x1405bd470
006332F9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
006332FD  48 85 F6                        test rsi, rsi
00633300  74 64                           je 0x140633366
00633302  40 32 FF                        xor dil, dil
00633305  40 38 3D AC 15 8D 00            cmp byte ptr [rip + 0x8d15ac], dil
0063330C  75 0C                           jne 0x14063331a
0063330E  F7 05 68 16 8D 00 00 08 00 00   test dword ptr [rip + 0x8d1668], 0x800
00633318  74 13                           je 0x14063332d
0063331A  48 8D 0D 5F 0B 8D 00            lea rcx, [rip + 0x8d0b5f]
00633321  E8 FA 32 BE FF                  call 0x140216620
00633326  40 8A F8                        mov dil, al
00633329  84 C0                           test al, al
0063332B  74 39                           je 0x140633366
0063332D  48 83 C6 30                     add rsi, 0x30
00633331  48 8B 1E                        mov rbx, qword ptr [rsi]
00633334  EB 1A                           jmp 0x140633350
00633336  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063333A  48 85 C0                        test rax, rax
0063333D  74 0E                           je 0x14063334d
0063333F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633343  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00633348  E8 83 77 08 00                  call 0x1406baad0
0063334D  48 8B 1B                        mov rbx, qword ptr [rbx]
00633350  48 3B DE                        cmp rbx, rsi
00633353  75 E1                           jne 0x140633336
00633355  40 84 FF                        test dil, dil
00633358  74 0C                           je 0x140633366
0063335A  48 8D 0D 1F 0B 8D 00            lea rcx, [rip + 0x8d0b1f]
00633361  E8 1A 6B D1 FF                  call 0x140349e80
00633366  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0063336A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063336F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00633374  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00633379  48 83 C4 40                     add rsp, 0x40
0063337D  41 5F                           pop r15
0063337F  41 5E                           pop r14
00633381  5F                              pop rdi
00633382  C3                              ret
00633383  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeTryToAcquireQueuedSpinLockWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(244, a2, a3, a4);
    if (result == 0) goto loc_006332EE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00633272;
    v_stack_m38 = v_stack_p0;
    goto loc_00633280;
loc_00633272:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9246249)) != 0) goto loc_006332A2;
    if (((*(unsigned int *)(v_rip + 9246432)) & (0x800ULL)) == 0) goto loc_006332B5;
loc_006332A2:
    result = ExAcquireRundownProtection(v_rip + 9243607, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006332EE;
loc_006332B5:
    goto loc_006332D8;
loc_006332BE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006332D8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006332BE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9243543;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeTryToAcquireQueuedSpinLock(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00633366;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9246124)) != 0) goto loc_0063331A;
    if (((*(unsigned int *)(v_rip + 9246312)) & (0x800ULL)) == 0) goto loc_0063332D;
loc_0063331A:
    result = ExAcquireRundownProtection(v_rip + 9243487, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00633366;
loc_0063332D:
    v_rsi = (result) + (48);
    goto loc_00633350;
loc_00633336:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633350:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00633336;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9243423;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifKeTryToAcquireQueuedSpinLockWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(244, Arg2, a3, a4);
    if (result == 0) goto loc_006332EE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00633272;
    v_stack_m38 = v_stack_p0;
    goto loc_00633280;
loc_00633272:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D1629)) != 0) goto loc_006332A2;
    if (((*(uint32_t *)(v_rip + 0x8D16E0)) & (0x800ULL)) == 0) goto loc_006332B5;
loc_006332A2:
    result = ExAcquireRundownProtection(v_rip + 9243607, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006332EE;
loc_006332B5:
    goto loc_006332D8;
loc_006332BE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006332D8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006332BE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9243543;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = KeTryToAcquireQueuedSpinLock(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00633366;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D15AC)) != 0) goto loc_0063331A;
    if (((*(uint32_t *)(v_rip + 0x8D1668)) & (0x800ULL)) == 0) goto loc_0063332D;
loc_0063331A:
    result = ExAcquireRundownProtection(v_rip + 9243487, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00633366;
loc_0063332D:
    local_rsi = (result) + (48);
    goto loc_00633350;
loc_00633336:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00633350:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00633336;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9243423;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00633220&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00633220[BB_00633220]
  bb_0063325F[BB_0063325F]
  bb_00633266[BB_00633266]
  bb_00633272[BB_00633272]
  bb_00633276[BB_00633276]
  bb_00633280[BB_00633280]
  bb_00633296[BB_00633296]
  bb_006332A2[BB_006332A2]
  bb_006332B5[BB_006332B5]
  bb_006332BE[BB_006332BE]
  bb_006332C7[BB_006332C7]
  bb_006332D5[BB_006332D5]
  bb_006332D8[BB_006332D8]
  bb_006332DD[BB_006332DD]
  bb_006332E2[BB_006332E2]
  bb_006332EE[BB_006332EE]
  bb_00633302[BB_00633302]
  bb_0063330E[BB_0063330E]
  bb_0063331A[BB_0063331A]
  bb_0063332D[BB_0063332D]
  bb_00633336[BB_00633336]
  bb_0063333F[BB_0063333F]
  bb_0063334D[BB_0063334D]
  bb_00633350[BB_00633350]
  bb_00633355[BB_00633355]
  bb_0063335A[BB_0063335A]
  bb_00633366[BB_00633366]
  bb_00633383[BB_00633383]
  bb_00633220 -->|branch| bb_006332EE
  bb_00633220 -->|fallthrough| bb_0063325F
  bb_0063325F -->|branch| bb_00633272
  bb_0063325F -->|fallthrough| bb_00633266
  bb_00633266 -->|branch| bb_00633280
  bb_00633272 -->|branch| bb_00633280
  bb_00633272 -->|fallthrough| bb_00633276
  bb_00633276 -->|flow| bb_00633280
  bb_00633280 -->|branch| bb_006332A2
  bb_00633280 -->|fallthrough| bb_00633296
  bb_00633296 -->|branch| bb_006332B5
  bb_00633296 -->|fallthrough| bb_006332A2
  bb_006332A2 -->|branch| bb_006332EE
  bb_006332A2 -->|fallthrough| bb_006332B5
  bb_006332B5 -->|branch| bb_006332D8
  bb_006332BE -->|branch| bb_006332D5
  bb_006332BE -->|fallthrough| bb_006332C7
  bb_006332C7 -->|flow| bb_006332D5
  bb_006332D5 -->|flow| bb_006332D8
  bb_006332D8 -->|branch| bb_006332BE
  bb_006332D8 -->|fallthrough| bb_006332DD
  bb_006332DD -->|branch| bb_006332EE
  bb_006332DD -->|fallthrough| bb_006332E2
  bb_006332E2 -->|flow| bb_006332EE
  bb_006332EE -->|branch| bb_00633366
  bb_006332EE -->|fallthrough| bb_00633302
  bb_00633302 -->|branch| bb_0063331A
  bb_00633302 -->|fallthrough| bb_0063330E
  bb_0063330E -->|branch| bb_0063332D
  bb_0063330E -->|fallthrough| bb_0063331A
  bb_0063331A -->|branch| bb_00633366
  bb_0063331A -->|fallthrough| bb_0063332D
  bb_0063332D -->|branch| bb_00633350
  bb_00633336 -->|branch| bb_0063334D
  bb_00633336 -->|fallthrough| bb_0063333F
  bb_0063333F -->|flow| bb_0063334D
  bb_0063334D -->|flow| bb_00633350
  bb_00633350 -->|branch| bb_00633336
  bb_00633350 -->|fallthrough| bb_00633355
  bb_00633355 -->|branch| bb_00633366
  bb_00633355 -->|fallthrough| bb_0063335A
  bb_0063335A -->|flow| bb_00633366
```
