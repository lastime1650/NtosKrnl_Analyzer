# DifExIsFastResourceHeldExclusiveWrapper

- RVA: `0x006213A0`–`0x006214FF` (길이 `351` bytes)
- VA: `0x00000001406213A0`
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
- `0x006213CF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006213F7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00621425` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062144C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621465` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062146D` → [ExIsFastResourceHeldExclusive](../21/ExIsFastResourceHeldExclusive_function_00213450.md) (function, `0x00213450`)
- `0x0062149A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006214C1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006214DA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621409` → RVA `0x00F048B8` (`.data`; read)
- `0x00621412` → RVA `0x00F04980` (`.data`; read)
- `0x0062141E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006213A0  4C 8B DC                        mov r11, rsp
006213A3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006213A7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006213AB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006213AF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006213B3  41 56                           push r14
006213B5  48 83 EC 40                     sub rsp, 0x40
006213B9  33 C0                           xor eax, eax
006213BB  0F 57 C0                        xorps xmm0, xmm0
006213BE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006213C3  48 8B E9                        mov rbp, rcx
006213C6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006213CA  B9 CC 01 00 00                  mov ecx, 0x1cc
006213CF  E8 60 46 E7 FF                  call 0x140495a34
006213D4  48 8B F0                        mov rsi, rax
006213D7  48 85 C0                        test rax, rax
006213DA  0F 84 8A 00 00 00               je 0x14062146a
006213E0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006213E3  A8 18                           test al, 0x18
006213E5  74 0C                           je 0x1406213f3
006213E7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006213EC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006213F1  EB 0E                           jmp 0x140621401
006213F3  A8 04                           test al, 4
006213F5  74 0A                           je 0x140621401
006213F7  E8 0C 28 EB FF                  call 0x1404d3c08
006213FC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00621401  40 32 FF                        xor dil, dil
00621404  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00621409  40 38 3D A8 34 8E 00            cmp byte ptr [rip + 0x8e34a8], dil
00621410  75 0C                           jne 0x14062141e
00621412  F7 05 64 35 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3564], 0x800
0062141C  74 13                           je 0x140621431
0062141E  48 8D 0D 5B 2A 8E 00            lea rcx, [rip + 0x8e2a5b]
00621425  E8 F6 51 BF FF                  call 0x140216620
0062142A  40 8A F8                        mov dil, al
0062142D  84 C0                           test al, al
0062142F  74 39                           je 0x14062146a
00621431  4C 8D 76 20                     lea r14, [rsi + 0x20]
00621435  49 8B 1E                        mov rbx, qword ptr [r14]
00621438  EB 1A                           jmp 0x140621454
0062143A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062143E  48 85 C0                        test rax, rax
00621441  74 0E                           je 0x140621451
00621443  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621447  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062144C  E8 7F 96 09 00                  call 0x1406baad0
00621451  48 8B 1B                        mov rbx, qword ptr [rbx]
00621454  49 3B DE                        cmp rbx, r14
00621457  75 E1                           jne 0x14062143a
00621459  40 84 FF                        test dil, dil
0062145C  74 0C                           je 0x14062146a
0062145E  48 8D 0D 1B 2A 8E 00            lea rcx, [rip + 0x8e2a1b]
00621465  E8 16 8A D2 FF                  call 0x140349e80
0062146A  48 8B CD                        mov rcx, rbp
0062146D  E8 DE 1F BF FF                  call 0x140213450
00621472  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00621476  48 85 F6                        test rsi, rsi
00621479  74 64                           je 0x1406214df
0062147B  40 32 FF                        xor dil, dil
0062147E  40 38 3D 33 34 8E 00            cmp byte ptr [rip + 0x8e3433], dil
00621485  75 0C                           jne 0x140621493
00621487  F7 05 EF 34 8E 00 00 08 00 00   test dword ptr [rip + 0x8e34ef], 0x800
00621491  74 13                           je 0x1406214a6
00621493  48 8D 0D E6 29 8E 00            lea rcx, [rip + 0x8e29e6]
0062149A  E8 81 51 BF FF                  call 0x140216620
0062149F  40 8A F8                        mov dil, al
006214A2  84 C0                           test al, al
006214A4  74 39                           je 0x1406214df
006214A6  48 83 C6 30                     add rsi, 0x30
006214AA  48 8B 1E                        mov rbx, qword ptr [rsi]
006214AD  EB 1A                           jmp 0x1406214c9
006214AF  48 8D 43 F0                     lea rax, [rbx - 0x10]
006214B3  48 85 C0                        test rax, rax
006214B6  74 0E                           je 0x1406214c6
006214B8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006214BC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006214C1  E8 0A 96 09 00                  call 0x1406baad0
006214C6  48 8B 1B                        mov rbx, qword ptr [rbx]
006214C9  48 3B DE                        cmp rbx, rsi
006214CC  75 E1                           jne 0x1406214af
006214CE  40 84 FF                        test dil, dil
006214D1  74 0C                           je 0x1406214df
006214D3  48 8D 0D A6 29 8E 00            lea rcx, [rip + 0x8e29a6]
006214DA  E8 A1 89 D2 FF                  call 0x140349e80
006214DF  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
006214E3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006214E8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006214ED  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006214F2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006214F7  48 83 C4 40                     add rsp, 0x40
006214FB  41 5E                           pop r14
006214FD  C3                              ret
006214FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsFastResourceHeldExclusiveWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(460, a2, a3, a4);
    if (result == 0) goto loc_0062146A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006213F3;
    v_stack_m28 = v_stack_p0;
    goto loc_00621401;
loc_006213F3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9319592)) != 0) goto loc_0062141E;
    if (((*(unsigned int *)(v_rip + 9319780)) & (0x800ULL)) == 0) goto loc_00621431;
loc_0062141E:
    result = ExAcquireRundownProtection(v_rip + 9316955, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062146A;
loc_00621431:
    goto loc_00621454;
loc_0062143A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621454:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062143A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316891;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExIsFastResourceHeldExclusive(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_006214DF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9319475)) != 0) goto loc_00621493;
    if (((*(unsigned int *)(v_rip + 9319663)) & (0x800ULL)) == 0) goto loc_006214A6;
loc_00621493:
    result = ExAcquireRundownProtection(v_rip + 9316838, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006214DF;
loc_006214A6:
    v_rsi = (result) + (48);
    goto loc_006214C9;
loc_006214AF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006214C9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006214AF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316774;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsFastResourceHeldExclusiveWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(460, a2, a3, a4);
    if (result == 0) goto loc_0062146A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006213F3;
    v_stack_m28 = v_stack_p0;
    goto loc_00621401;
loc_006213F3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E34A8)) != 0) goto loc_0062141E;
    if (((*(uint32_t *)(v_rip + 0x8E3564)) & (0x800ULL)) == 0) goto loc_00621431;
loc_0062141E:
    result = ExAcquireRundownProtection(v_rip + 9316955, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062146A;
loc_00621431:
    goto loc_00621454;
loc_0062143A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621454:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062143A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316891;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExIsFastResourceHeldExclusive(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_006214DF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E3433)) != 0) goto loc_00621493;
    if (((*(uint32_t *)(v_rip + 0x8E34EF)) & (0x800ULL)) == 0) goto loc_006214A6;
loc_00621493:
    result = ExAcquireRundownProtection(v_rip + 9316838, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006214DF;
loc_006214A6:
    local_rsi = (result) + (48);
    goto loc_006214C9;
loc_006214AF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006214C9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006214AF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316774;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006213A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006213A0[BB_006213A0]
  bb_006213E0[BB_006213E0]
  bb_006213E7[BB_006213E7]
  bb_006213F3[BB_006213F3]
  bb_006213F7[BB_006213F7]
  bb_00621401[BB_00621401]
  bb_00621412[BB_00621412]
  bb_0062141E[BB_0062141E]
  bb_00621431[BB_00621431]
  bb_0062143A[BB_0062143A]
  bb_00621443[BB_00621443]
  bb_00621451[BB_00621451]
  bb_00621454[BB_00621454]
  bb_00621459[BB_00621459]
  bb_0062145E[BB_0062145E]
  bb_0062146A[BB_0062146A]
  bb_0062147B[BB_0062147B]
  bb_00621487[BB_00621487]
  bb_00621493[BB_00621493]
  bb_006214A6[BB_006214A6]
  bb_006214AF[BB_006214AF]
  bb_006214B8[BB_006214B8]
  bb_006214C6[BB_006214C6]
  bb_006214C9[BB_006214C9]
  bb_006214CE[BB_006214CE]
  bb_006214D3[BB_006214D3]
  bb_006214DF[BB_006214DF]
  bb_006214FE[BB_006214FE]
  bb_006213A0 -->|branch| bb_0062146A
  bb_006213A0 -->|fallthrough| bb_006213E0
  bb_006213E0 -->|branch| bb_006213F3
  bb_006213E0 -->|fallthrough| bb_006213E7
  bb_006213E7 -->|branch| bb_00621401
  bb_006213F3 -->|branch| bb_00621401
  bb_006213F3 -->|fallthrough| bb_006213F7
  bb_006213F7 -->|flow| bb_00621401
  bb_00621401 -->|branch| bb_0062141E
  bb_00621401 -->|fallthrough| bb_00621412
  bb_00621412 -->|branch| bb_00621431
  bb_00621412 -->|fallthrough| bb_0062141E
  bb_0062141E -->|branch| bb_0062146A
  bb_0062141E -->|fallthrough| bb_00621431
  bb_00621431 -->|branch| bb_00621454
  bb_0062143A -->|branch| bb_00621451
  bb_0062143A -->|fallthrough| bb_00621443
  bb_00621443 -->|flow| bb_00621451
  bb_00621451 -->|flow| bb_00621454
  bb_00621454 -->|branch| bb_0062143A
  bb_00621454 -->|fallthrough| bb_00621459
  bb_00621459 -->|branch| bb_0062146A
  bb_00621459 -->|fallthrough| bb_0062145E
  bb_0062145E -->|flow| bb_0062146A
  bb_0062146A -->|branch| bb_006214DF
  bb_0062146A -->|fallthrough| bb_0062147B
  bb_0062147B -->|branch| bb_00621493
  bb_0062147B -->|fallthrough| bb_00621487
  bb_00621487 -->|branch| bb_006214A6
  bb_00621487 -->|fallthrough| bb_00621493
  bb_00621493 -->|branch| bb_006214DF
  bb_00621493 -->|fallthrough| bb_006214A6
  bb_006214A6 -->|branch| bb_006214C9
  bb_006214AF -->|branch| bb_006214C6
  bb_006214AF -->|fallthrough| bb_006214B8
  bb_006214B8 -->|flow| bb_006214C6
  bb_006214C6 -->|flow| bb_006214C9
  bb_006214C9 -->|branch| bb_006214AF
  bb_006214C9 -->|fallthrough| bb_006214CE
  bb_006214CE -->|branch| bb_006214DF
  bb_006214CE -->|fallthrough| bb_006214D3
  bb_006214D3 -->|flow| bb_006214DF
```
