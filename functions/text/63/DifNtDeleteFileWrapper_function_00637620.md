# DifNtDeleteFileWrapper

- RVA: `0x00637620`–`0x0063777F` (길이 `351` bytes)
- VA: `0x0000000140637620`
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
- `0x0063764F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00637677` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006376A5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006376CC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006376E5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006376ED` → [NtDeleteFile](../../page/A9/NtDeleteFile_function_00A97B20.md) (function, `0x00A97B20`)
- `0x0063771A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637741` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063775A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00637689` → RVA `0x00F048B8` (`.data`; read)
- `0x00637692` → RVA `0x00F04980` (`.data`; read)
- `0x0063769E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006376ED` → [NtDeleteFile](../../page/A9/NtDeleteFile_function_00A97B20.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00637620  4C 8B DC                        mov r11, rsp
00637623  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00637627  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063762B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063762F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00637633  41 56                           push r14
00637635  48 83 EC 40                     sub rsp, 0x40
00637639  33 C0                           xor eax, eax
0063763B  0F 57 C0                        xorps xmm0, xmm0
0063763E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00637643  48 8B E9                        mov rbp, rcx
00637646  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063764A  B9 CF 00 00 00                  mov ecx, 0xcf
0063764F  E8 E0 E3 E5 FF                  call 0x140495a34
00637654  48 8B F0                        mov rsi, rax
00637657  48 85 C0                        test rax, rax
0063765A  0F 84 8A 00 00 00               je 0x1406376ea
00637660  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00637663  A8 18                           test al, 0x18
00637665  74 0C                           je 0x140637673
00637667  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063766C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00637671  EB 0E                           jmp 0x140637681
00637673  A8 04                           test al, 4
00637675  74 0A                           je 0x140637681
00637677  E8 8C C5 E9 FF                  call 0x1404d3c08
0063767C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00637681  40 32 FF                        xor dil, dil
00637684  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00637689  40 38 3D 28 D2 8C 00            cmp byte ptr [rip + 0x8cd228], dil
00637690  75 0C                           jne 0x14063769e
00637692  F7 05 E4 D2 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd2e4], 0x800
0063769C  74 13                           je 0x1406376b1
0063769E  48 8D 0D DB C7 8C 00            lea rcx, [rip + 0x8cc7db]
006376A5  E8 76 EF BD FF                  call 0x140216620
006376AA  40 8A F8                        mov dil, al
006376AD  84 C0                           test al, al
006376AF  74 39                           je 0x1406376ea
006376B1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006376B5  49 8B 1E                        mov rbx, qword ptr [r14]
006376B8  EB 1A                           jmp 0x1406376d4
006376BA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006376BE  48 85 C0                        test rax, rax
006376C1  74 0E                           je 0x1406376d1
006376C3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006376C7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006376CC  E8 FF 33 08 00                  call 0x1406baad0
006376D1  48 8B 1B                        mov rbx, qword ptr [rbx]
006376D4  49 3B DE                        cmp rbx, r14
006376D7  75 E1                           jne 0x1406376ba
006376D9  40 84 FF                        test dil, dil
006376DC  74 0C                           je 0x1406376ea
006376DE  48 8D 0D 9B C7 8C 00            lea rcx, [rip + 0x8cc79b]
006376E5  E8 96 27 D1 FF                  call 0x140349e80
006376EA  48 8B CD                        mov rcx, rbp
006376ED  E8 2E 04 46 00                  call 0x140a97b20
006376F2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006376F6  48 85 F6                        test rsi, rsi
006376F9  74 64                           je 0x14063775f
006376FB  40 32 FF                        xor dil, dil
006376FE  40 38 3D B3 D1 8C 00            cmp byte ptr [rip + 0x8cd1b3], dil
00637705  75 0C                           jne 0x140637713
00637707  F7 05 6F D2 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd26f], 0x800
00637711  74 13                           je 0x140637726
00637713  48 8D 0D 66 C7 8C 00            lea rcx, [rip + 0x8cc766]
0063771A  E8 01 EF BD FF                  call 0x140216620
0063771F  40 8A F8                        mov dil, al
00637722  84 C0                           test al, al
00637724  74 39                           je 0x14063775f
00637726  48 83 C6 30                     add rsi, 0x30
0063772A  48 8B 1E                        mov rbx, qword ptr [rsi]
0063772D  EB 1A                           jmp 0x140637749
0063772F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637733  48 85 C0                        test rax, rax
00637736  74 0E                           je 0x140637746
00637738  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063773C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00637741  E8 8A 33 08 00                  call 0x1406baad0
00637746  48 8B 1B                        mov rbx, qword ptr [rbx]
00637749  48 3B DE                        cmp rbx, rsi
0063774C  75 E1                           jne 0x14063772f
0063774E  40 84 FF                        test dil, dil
00637751  74 0C                           je 0x14063775f
00637753  48 8D 0D 26 C7 8C 00            lea rcx, [rip + 0x8cc726]
0063775A  E8 21 27 D1 FF                  call 0x140349e80
0063775F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00637763  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00637768  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063776D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00637772  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00637777  48 83 C4 40                     add rsp, 0x40
0063777B  41 5E                           pop r14
0063777D  C3                              ret
0063777E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifNtDeleteFileWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(207, a2, a3, a4);
    if (result == 0) goto loc_006376EA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00637673;
    v_stack_m28 = v_stack_p0;
    goto loc_00637681;
loc_00637673:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9228840)) != 0) goto loc_0063769E;
    if (((*(unsigned int *)(v_rip + 9229028)) & (0x800ULL)) == 0) goto loc_006376B1;
loc_0063769E:
    result = ExAcquireRundownProtection(v_rip + 9226203, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006376EA;
loc_006376B1:
    goto loc_006376D4;
loc_006376BA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006376D4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006376BA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9226139;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = NtDeleteFile(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0063775F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9228723)) != 0) goto loc_00637713;
    if (((*(unsigned int *)(v_rip + 9228911)) & (0x800ULL)) == 0) goto loc_00637726;
loc_00637713:
    result = ExAcquireRundownProtection(v_rip + 9226086, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063775F;
loc_00637726:
    v_rsi = (result) + (48);
    goto loc_00637749;
loc_0063772F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00637749:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063772F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9226022;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifNtDeleteFileWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(207, a2, a3, a4);
    if (result == 0) goto loc_006376EA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00637673;
    v_stack_m28 = v_stack_p0;
    goto loc_00637681;
loc_00637673:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8CD228)) != 0) goto loc_0063769E;
    if (((*(uint32_t *)(v_rip + 0x8CD2E4)) & (0x800ULL)) == 0) goto loc_006376B1;
loc_0063769E:
    result = ExAcquireRundownProtection(v_rip + 9226203, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006376EA;
loc_006376B1:
    goto loc_006376D4;
loc_006376BA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006376D4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006376BA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9226139;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = NtDeleteFile(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0063775F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CD1B3)) != 0) goto loc_00637713;
    if (((*(uint32_t *)(v_rip + 0x8CD26F)) & (0x800ULL)) == 0) goto loc_00637726;
loc_00637713:
    result = ExAcquireRundownProtection(v_rip + 9226086, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063775F;
loc_00637726:
    local_rsi = (result) + (48);
    goto loc_00637749;
loc_0063772F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00637749:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063772F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9226022;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00637620&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00637620[BB_00637620]
  bb_00637660[BB_00637660]
  bb_00637667[BB_00637667]
  bb_00637673[BB_00637673]
  bb_00637677[BB_00637677]
  bb_00637681[BB_00637681]
  bb_00637692[BB_00637692]
  bb_0063769E[BB_0063769E]
  bb_006376B1[BB_006376B1]
  bb_006376BA[BB_006376BA]
  bb_006376C3[BB_006376C3]
  bb_006376D1[BB_006376D1]
  bb_006376D4[BB_006376D4]
  bb_006376D9[BB_006376D9]
  bb_006376DE[BB_006376DE]
  bb_006376EA[BB_006376EA]
  bb_006376FB[BB_006376FB]
  bb_00637707[BB_00637707]
  bb_00637713[BB_00637713]
  bb_00637726[BB_00637726]
  bb_0063772F[BB_0063772F]
  bb_00637738[BB_00637738]
  bb_00637746[BB_00637746]
  bb_00637749[BB_00637749]
  bb_0063774E[BB_0063774E]
  bb_00637753[BB_00637753]
  bb_0063775F[BB_0063775F]
  bb_0063777E[BB_0063777E]
  bb_00637620 -->|branch| bb_006376EA
  bb_00637620 -->|fallthrough| bb_00637660
  bb_00637660 -->|branch| bb_00637673
  bb_00637660 -->|fallthrough| bb_00637667
  bb_00637667 -->|branch| bb_00637681
  bb_00637673 -->|branch| bb_00637681
  bb_00637673 -->|fallthrough| bb_00637677
  bb_00637677 -->|flow| bb_00637681
  bb_00637681 -->|branch| bb_0063769E
  bb_00637681 -->|fallthrough| bb_00637692
  bb_00637692 -->|branch| bb_006376B1
  bb_00637692 -->|fallthrough| bb_0063769E
  bb_0063769E -->|branch| bb_006376EA
  bb_0063769E -->|fallthrough| bb_006376B1
  bb_006376B1 -->|branch| bb_006376D4
  bb_006376BA -->|branch| bb_006376D1
  bb_006376BA -->|fallthrough| bb_006376C3
  bb_006376C3 -->|flow| bb_006376D1
  bb_006376D1 -->|flow| bb_006376D4
  bb_006376D4 -->|branch| bb_006376BA
  bb_006376D4 -->|fallthrough| bb_006376D9
  bb_006376D9 -->|branch| bb_006376EA
  bb_006376D9 -->|fallthrough| bb_006376DE
  bb_006376DE -->|flow| bb_006376EA
  bb_006376EA -->|branch| bb_0063775F
  bb_006376EA -->|fallthrough| bb_006376FB
  bb_006376FB -->|branch| bb_00637713
  bb_006376FB -->|fallthrough| bb_00637707
  bb_00637707 -->|branch| bb_00637726
  bb_00637707 -->|fallthrough| bb_00637713
  bb_00637713 -->|branch| bb_0063775F
  bb_00637713 -->|fallthrough| bb_00637726
  bb_00637726 -->|branch| bb_00637749
  bb_0063772F -->|branch| bb_00637746
  bb_0063772F -->|fallthrough| bb_00637738
  bb_00637738 -->|flow| bb_00637746
  bb_00637746 -->|flow| bb_00637749
  bb_00637749 -->|branch| bb_0063772F
  bb_00637749 -->|fallthrough| bb_0063774E
  bb_0063774E -->|branch| bb_0063775F
  bb_0063774E -->|fallthrough| bb_00637753
  bb_00637753 -->|flow| bb_0063775F
```
