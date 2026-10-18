# DifZwCommitEnlistmentWrapper

- RVA: `0x0063F100`–`0x0063F264` (길이 `356` bytes)
- VA: `0x000000014063F100`
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
- `0x0063F12E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063F156` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063F189` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F1B0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F1C9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063F1D4` → [ZwCommitEnlistment](../6A/ZwCommitEnlistment_function_006AE430.md) (function, `0x006AE430`)
- `0x0063F201` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F228` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F241` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063F168` → RVA `0x00F048B8` (`.data`; read)
- `0x0063F176` → RVA `0x00F04980` (`.data`; read)
- `0x0063F182` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063F100  48 8B C4                        mov rax, rsp
0063F103  48 89 58 08                     mov qword ptr [rax + 8], rbx
0063F107  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063F10B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063F10F  57                              push rdi
0063F110  41 56                           push r14
0063F112  41 57                           push r15
0063F114  48 83 EC 40                     sub rsp, 0x40
0063F118  0F 57 C0                        xorps xmm0, xmm0
0063F11B  4C 8B F9                        mov r15, rcx
0063F11E  B9 81 00 00 00                  mov ecx, 0x81
0063F123  4C 8B F2                        mov r14, rdx
0063F126  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063F12A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063F12E  E8 01 69 E5 FF                  call 0x140495a34
0063F133  48 8B F0                        mov rsi, rax
0063F136  48 85 C0                        test rax, rax
0063F139  0F 84 8F 00 00 00               je 0x14063f1ce
0063F13F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063F142  A8 18                           test al, 0x18
0063F144  74 0C                           je 0x14063f152
0063F146  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063F14B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063F150  EB 0E                           jmp 0x14063f160
0063F152  A8 04                           test al, 4
0063F154  74 0A                           je 0x14063f160
0063F156  E8 AD 4A E9 FF                  call 0x1404d3c08
0063F15B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063F160  40 32 ED                        xor bpl, bpl
0063F163  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0063F168  40 38 2D 49 57 8C 00            cmp byte ptr [rip + 0x8c5749], bpl
0063F16F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0063F174  75 0C                           jne 0x14063f182
0063F176  F7 05 00 58 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5800], 0x800
0063F180  74 13                           je 0x14063f195
0063F182  48 8D 0D F7 4C 8C 00            lea rcx, [rip + 0x8c4cf7]
0063F189  E8 92 74 BD FF                  call 0x140216620
0063F18E  40 8A E8                        mov bpl, al
0063F191  84 C0                           test al, al
0063F193  74 39                           je 0x14063f1ce
0063F195  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063F199  48 8B 1F                        mov rbx, qword ptr [rdi]
0063F19C  EB 1A                           jmp 0x14063f1b8
0063F19E  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F1A2  48 85 C0                        test rax, rax
0063F1A5  74 0E                           je 0x14063f1b5
0063F1A7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F1AB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063F1B0  E8 1B B9 07 00                  call 0x1406baad0
0063F1B5  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F1B8  48 3B DF                        cmp rbx, rdi
0063F1BB  75 E1                           jne 0x14063f19e
0063F1BD  40 84 ED                        test bpl, bpl
0063F1C0  74 0C                           je 0x14063f1ce
0063F1C2  48 8D 0D B7 4C 8C 00            lea rcx, [rip + 0x8c4cb7]
0063F1C9  E8 B2 AC D0 FF                  call 0x140349e80
0063F1CE  49 8B D6                        mov rdx, r14
0063F1D1  49 8B CF                        mov rcx, r15
0063F1D4  E8 57 F2 06 00                  call 0x1406ae430
0063F1D9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0063F1DD  48 85 F6                        test rsi, rsi
0063F1E0  74 64                           je 0x14063f246
0063F1E2  40 32 FF                        xor dil, dil
0063F1E5  40 38 3D CC 56 8C 00            cmp byte ptr [rip + 0x8c56cc], dil
0063F1EC  75 0C                           jne 0x14063f1fa
0063F1EE  F7 05 88 57 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5788], 0x800
0063F1F8  74 13                           je 0x14063f20d
0063F1FA  48 8D 0D 7F 4C 8C 00            lea rcx, [rip + 0x8c4c7f]
0063F201  E8 1A 74 BD FF                  call 0x140216620
0063F206  40 8A F8                        mov dil, al
0063F209  84 C0                           test al, al
0063F20B  74 39                           je 0x14063f246
0063F20D  48 83 C6 30                     add rsi, 0x30
0063F211  48 8B 1E                        mov rbx, qword ptr [rsi]
0063F214  EB 1A                           jmp 0x14063f230
0063F216  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F21A  48 85 C0                        test rax, rax
0063F21D  74 0E                           je 0x14063f22d
0063F21F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F223  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063F228  E8 A3 B8 07 00                  call 0x1406baad0
0063F22D  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F230  48 3B DE                        cmp rbx, rsi
0063F233  75 E1                           jne 0x14063f216
0063F235  40 84 FF                        test dil, dil
0063F238  74 0C                           je 0x14063f246
0063F23A  48 8D 0D 3F 4C 8C 00            lea rcx, [rip + 0x8c4c3f]
0063F241  E8 3A AC D0 FF                  call 0x140349e80
0063F246  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0063F24A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063F24F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063F254  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063F259  48 83 C4 40                     add rsp, 0x40
0063F25D  41 5F                           pop r15
0063F25F  41 5E                           pop r14
0063F261  5F                              pop rdi
0063F262  C3                              ret
0063F263  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCommitEnlistmentWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(129, a2, a3, a4);
    if (result == 0) goto loc_0063F1CE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063F152;
    v_stack_m38 = v_stack_p0;
    goto loc_0063F160;
loc_0063F152:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9197385)) != 0) goto loc_0063F182;
    if (((*(unsigned int *)(v_rip + 9197568)) & (0x800ULL)) == 0) goto loc_0063F195;
loc_0063F182:
    result = ExAcquireRundownProtection(v_rip + 9194743, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F1CE;
loc_0063F195:
    goto loc_0063F1B8;
loc_0063F19E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F1B8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063F19E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9194679;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCommitEnlistment(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_0063F246;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9197260)) != 0) goto loc_0063F1FA;
    if (((*(unsigned int *)(v_rip + 9197448)) & (0x800ULL)) == 0) goto loc_0063F20D;
loc_0063F1FA:
    result = ExAcquireRundownProtection(v_rip + 9194623, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F246;
loc_0063F20D:
    v_rsi = (result) + (48);
    goto loc_0063F230;
loc_0063F216:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F230:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063F216;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9194559;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCommitEnlistmentWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(129, Arg2, a3, a4);
    if (result == 0) goto loc_0063F1CE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063F152;
    v_stack_m38 = v_stack_p0;
    goto loc_0063F160;
loc_0063F152:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C5749)) != 0) goto loc_0063F182;
    if (((*(uint32_t *)(v_rip + 0x8C5800)) & (0x800ULL)) == 0) goto loc_0063F195;
loc_0063F182:
    result = ExAcquireRundownProtection(v_rip + 9194743, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F1CE;
loc_0063F195:
    goto loc_0063F1B8;
loc_0063F19E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063F1B8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063F19E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9194679;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwCommitEnlistment(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_0063F246;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C56CC)) != 0) goto loc_0063F1FA;
    if (((*(uint32_t *)(v_rip + 0x8C5788)) & (0x800ULL)) == 0) goto loc_0063F20D;
loc_0063F1FA:
    result = ExAcquireRundownProtection(v_rip + 9194623, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063F246;
loc_0063F20D:
    local_rsi = (result) + (48);
    goto loc_0063F230;
loc_0063F216:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063F230:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063F216;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9194559;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063F100&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063F100[BB_0063F100]
  bb_0063F13F[BB_0063F13F]
  bb_0063F146[BB_0063F146]
  bb_0063F152[BB_0063F152]
  bb_0063F156[BB_0063F156]
  bb_0063F160[BB_0063F160]
  bb_0063F176[BB_0063F176]
  bb_0063F182[BB_0063F182]
  bb_0063F195[BB_0063F195]
  bb_0063F19E[BB_0063F19E]
  bb_0063F1A7[BB_0063F1A7]
  bb_0063F1B5[BB_0063F1B5]
  bb_0063F1B8[BB_0063F1B8]
  bb_0063F1BD[BB_0063F1BD]
  bb_0063F1C2[BB_0063F1C2]
  bb_0063F1CE[BB_0063F1CE]
  bb_0063F1E2[BB_0063F1E2]
  bb_0063F1EE[BB_0063F1EE]
  bb_0063F1FA[BB_0063F1FA]
  bb_0063F20D[BB_0063F20D]
  bb_0063F216[BB_0063F216]
  bb_0063F21F[BB_0063F21F]
  bb_0063F22D[BB_0063F22D]
  bb_0063F230[BB_0063F230]
  bb_0063F235[BB_0063F235]
  bb_0063F23A[BB_0063F23A]
  bb_0063F246[BB_0063F246]
  bb_0063F263[BB_0063F263]
  bb_0063F100 -->|branch| bb_0063F1CE
  bb_0063F100 -->|fallthrough| bb_0063F13F
  bb_0063F13F -->|branch| bb_0063F152
  bb_0063F13F -->|fallthrough| bb_0063F146
  bb_0063F146 -->|branch| bb_0063F160
  bb_0063F152 -->|branch| bb_0063F160
  bb_0063F152 -->|fallthrough| bb_0063F156
  bb_0063F156 -->|flow| bb_0063F160
  bb_0063F160 -->|branch| bb_0063F182
  bb_0063F160 -->|fallthrough| bb_0063F176
  bb_0063F176 -->|branch| bb_0063F195
  bb_0063F176 -->|fallthrough| bb_0063F182
  bb_0063F182 -->|branch| bb_0063F1CE
  bb_0063F182 -->|fallthrough| bb_0063F195
  bb_0063F195 -->|branch| bb_0063F1B8
  bb_0063F19E -->|branch| bb_0063F1B5
  bb_0063F19E -->|fallthrough| bb_0063F1A7
  bb_0063F1A7 -->|flow| bb_0063F1B5
  bb_0063F1B5 -->|flow| bb_0063F1B8
  bb_0063F1B8 -->|branch| bb_0063F19E
  bb_0063F1B8 -->|fallthrough| bb_0063F1BD
  bb_0063F1BD -->|branch| bb_0063F1CE
  bb_0063F1BD -->|fallthrough| bb_0063F1C2
  bb_0063F1C2 -->|flow| bb_0063F1CE
  bb_0063F1CE -->|branch| bb_0063F246
  bb_0063F1CE -->|fallthrough| bb_0063F1E2
  bb_0063F1E2 -->|branch| bb_0063F1FA
  bb_0063F1E2 -->|fallthrough| bb_0063F1EE
  bb_0063F1EE -->|branch| bb_0063F20D
  bb_0063F1EE -->|fallthrough| bb_0063F1FA
  bb_0063F1FA -->|branch| bb_0063F246
  bb_0063F1FA -->|fallthrough| bb_0063F20D
  bb_0063F20D -->|branch| bb_0063F230
  bb_0063F216 -->|branch| bb_0063F22D
  bb_0063F216 -->|fallthrough| bb_0063F21F
  bb_0063F21F -->|flow| bb_0063F22D
  bb_0063F22D -->|flow| bb_0063F230
  bb_0063F230 -->|branch| bb_0063F216
  bb_0063F230 -->|fallthrough| bb_0063F235
  bb_0063F235 -->|branch| bb_0063F246
  bb_0063F235 -->|fallthrough| bb_0063F23A
  bb_0063F23A -->|flow| bb_0063F246
```
