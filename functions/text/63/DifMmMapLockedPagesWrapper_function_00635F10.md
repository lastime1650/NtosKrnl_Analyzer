# DifMmMapLockedPagesWrapper

- RVA: `0x00635F10`–`0x0063608D` (길이 `381` bytes)
- VA: `0x0000000140635F10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EE78`
- 디코드: `103`개 명령, `381/381` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00635F3E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00635F66` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00635F99` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635FC0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635FD9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00635FFA` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x00636028` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063604F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636068` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00635F78` → RVA `0x00F048B8` (`.data`; read)
- `0x00635F86` → RVA `0x00F04980` (`.data`; read)
- `0x00635F92` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635F10  48 8B C4                        mov rax, rsp
00635F13  48 89 58 08                     mov qword ptr [rax + 8], rbx
00635F17  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00635F1B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00635F1F  57                              push rdi
00635F20  41 56                           push r14
00635F22  41 57                           push r15
00635F24  48 83 EC 50                     sub rsp, 0x50
00635F28  0F 57 C0                        xorps xmm0, xmm0
00635F2B  4C 8B F9                        mov r15, rcx
00635F2E  B9 DC 00 00 00                  mov ecx, 0xdc
00635F33  44 8A F2                        mov r14b, dl
00635F36  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00635F3A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00635F3E  E8 F1 FA E5 FF                  call 0x140495a34
00635F43  48 8B F0                        mov rsi, rax
00635F46  48 85 C0                        test rax, rax
00635F49  0F 84 8F 00 00 00               je 0x140635fde
00635F4F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00635F52  A8 18                           test al, 0x18
00635F54  74 0C                           je 0x140635f62
00635F56  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00635F5B  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00635F60  EB 0E                           jmp 0x140635f70
00635F62  A8 04                           test al, 4
00635F64  74 0A                           je 0x140635f70
00635F66  E8 9D DC E9 FF                  call 0x1404d3c08
00635F6B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00635F70  40 32 ED                        xor bpl, bpl
00635F73  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
00635F78  40 38 2D 39 E9 8C 00            cmp byte ptr [rip + 0x8ce939], bpl
00635F7F  44 88 74 24 38                  mov byte ptr [rsp + 0x38], r14b
00635F84  75 0C                           jne 0x140635f92
00635F86  F7 05 F0 E9 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce9f0], 0x800
00635F90  74 13                           je 0x140635fa5
00635F92  48 8D 0D E7 DE 8C 00            lea rcx, [rip + 0x8cdee7]
00635F99  E8 82 06 BE FF                  call 0x140216620
00635F9E  40 8A E8                        mov bpl, al
00635FA1  84 C0                           test al, al
00635FA3  74 39                           je 0x140635fde
00635FA5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00635FA9  48 8B 1F                        mov rbx, qword ptr [rdi]
00635FAC  EB 1A                           jmp 0x140635fc8
00635FAE  48 8D 43 F0                     lea rax, [rbx - 0x10]
00635FB2  48 85 C0                        test rax, rax
00635FB5  74 0E                           je 0x140635fc5
00635FB7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635FBB  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00635FC0  E8 0B 4B 08 00                  call 0x1406baad0
00635FC5  48 8B 1B                        mov rbx, qword ptr [rbx]
00635FC8  48 3B DF                        cmp rbx, rdi
00635FCB  75 E1                           jne 0x140635fae
00635FCD  40 84 ED                        test bpl, bpl
00635FD0  74 0C                           je 0x140635fde
00635FD2  48 8D 0D A7 DE 8C 00            lea rcx, [rip + 0x8cdea7]
00635FD9  E8 A2 3E D1 FF                  call 0x140349e80
00635FDE  41 B8 01 00 00 00               mov r8d, 1
00635FE4  C7 44 24 28 20 00 00 00         mov dword ptr [rsp + 0x28], 0x20
00635FEC  45 33 C9                        xor r9d, r9d
00635FEF  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
00635FF4  41 8A D6                        mov dl, r14b
00635FF7  49 8B CF                        mov rcx, r15
00635FFA  E8 01 28 CE FF                  call 0x140318800
00635FFF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00636004  48 85 F6                        test rsi, rsi
00636007  74 64                           je 0x14063606d
00636009  40 32 FF                        xor dil, dil
0063600C  40 38 3D A5 E8 8C 00            cmp byte ptr [rip + 0x8ce8a5], dil
00636013  75 0C                           jne 0x140636021
00636015  F7 05 61 E9 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce961], 0x800
0063601F  74 13                           je 0x140636034
00636021  48 8D 0D 58 DE 8C 00            lea rcx, [rip + 0x8cde58]
00636028  E8 F3 05 BE FF                  call 0x140216620
0063602D  40 8A F8                        mov dil, al
00636030  84 C0                           test al, al
00636032  74 39                           je 0x14063606d
00636034  48 83 C6 30                     add rsi, 0x30
00636038  48 8B 1E                        mov rbx, qword ptr [rsi]
0063603B  EB 1A                           jmp 0x140636057
0063603D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00636041  48 85 C0                        test rax, rax
00636044  74 0E                           je 0x140636054
00636046  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063604A  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0063604F  E8 7C 4A 08 00                  call 0x1406baad0
00636054  48 8B 1B                        mov rbx, qword ptr [rbx]
00636057  48 3B DE                        cmp rbx, rsi
0063605A  75 E1                           jne 0x14063603d
0063605C  40 84 FF                        test dil, dil
0063605F  74 0C                           je 0x14063606d
00636061  48 8D 0D 18 DE 8C 00            lea rcx, [rip + 0x8cde18]
00636068  E8 13 3E D1 FF                  call 0x140349e80
0063606D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00636072  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00636077  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
0063607B  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
0063607F  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
00636083  49 8B E3                        mov rsp, r11
00636086  41 5F                           pop r15
00636088  41 5E                           pop r14
0063608A  5F                              pop rdi
0063608B  C3                              ret
0063608C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmMapLockedPagesWrapper(__int64 a1, unsigned __int8 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(220, a2, a3, a4);
    if (result == 0) goto loc_00635FDE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00635F62;
    v_stack_m38 = v_stack_p0;
    goto loc_00635F70;
loc_00635F62:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9234745)) != 0) goto loc_00635F92;
    if (((*(unsigned int *)(v_rip + 9234928)) & (0x800ULL)) == 0) goto loc_00635FA5;
loc_00635F92:
    result = ExAcquireRundownProtection(v_rip + 9232103, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635FDE;
loc_00635FA5:
    goto loc_00635FC8;
loc_00635FAE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635FC8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635FAE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9232039;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m40 = 32;
    a4 = 0;
    v_stack_m48 = 1;
    result = MmMapLockedPagesSpecifyCache(a1, a2, 1, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_0063606D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9234597)) != 0) goto loc_00636021;
    if (((*(unsigned int *)(v_rip + 9234785)) & (0x800ULL)) == 0) goto loc_00636034;
loc_00636021:
    result = ExAcquireRundownProtection(v_rip + 9231960, a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063606D;
loc_00636034:
    v_rsi = (result) + (48);
    goto loc_00636057;
loc_0063603D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, 1, a4);
    }
loc_00636057:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063603D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9231896;
        result = ExReleaseRundownProtection(a1, a2, 1, a4);
    }
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmMapLockedPagesWrapper(int64_t Arg1, uint8_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_p0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(220, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00635FDE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00635F62;
    v_stack_m38 = v_stack_p0;
    goto loc_00635F70;
loc_00635F62:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8CE939)) != 0) goto loc_00635F92;
    if (((*(uint32_t *)(v_rip + 0x8CE9F0)) & (0x800ULL)) == 0) goto loc_00635FA5;
loc_00635F92:
    result = ExAcquireRundownProtection(v_rip + 9232103, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00635FDE;
loc_00635FA5:
    goto loc_00635FC8;
loc_00635FAE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00635FC8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635FAE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9232039;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m40 = 32;
    Arg4 = 0;
    v_stack_m48 = 1;
    result = MmMapLockedPagesSpecifyCache(Arg1, Arg2, 1, Arg4);
    v_stack_m20 = result;
    if (result == 0) goto loc_0063606D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CE8A5)) != 0) goto loc_00636021;
    if (((*(uint32_t *)(v_rip + 0x8CE961)) & (0x800ULL)) == 0) goto loc_00636034;
loc_00636021:
    result = ExAcquireRundownProtection(v_rip + 9231960, Arg2, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063606D;
loc_00636034:
    local_rsi = (result) + (48);
    goto loc_00636057;
loc_0063603D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, 1, Arg4);
    }
loc_00636057:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063603D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9231896;
        result = ExReleaseRundownProtection(Arg1, Arg2, 1, Arg4);
    }
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635F10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635F10[BB_00635F10]
  bb_00635F4F[BB_00635F4F]
  bb_00635F56[BB_00635F56]
  bb_00635F62[BB_00635F62]
  bb_00635F66[BB_00635F66]
  bb_00635F70[BB_00635F70]
  bb_00635F86[BB_00635F86]
  bb_00635F92[BB_00635F92]
  bb_00635FA5[BB_00635FA5]
  bb_00635FAE[BB_00635FAE]
  bb_00635FB7[BB_00635FB7]
  bb_00635FC5[BB_00635FC5]
  bb_00635FC8[BB_00635FC8]
  bb_00635FCD[BB_00635FCD]
  bb_00635FD2[BB_00635FD2]
  bb_00635FDE[BB_00635FDE]
  bb_00636009[BB_00636009]
  bb_00636015[BB_00636015]
  bb_00636021[BB_00636021]
  bb_00636034[BB_00636034]
  bb_0063603D[BB_0063603D]
  bb_00636046[BB_00636046]
  bb_00636054[BB_00636054]
  bb_00636057[BB_00636057]
  bb_0063605C[BB_0063605C]
  bb_00636061[BB_00636061]
  bb_0063606D[BB_0063606D]
  bb_0063608C[BB_0063608C]
  bb_00635F10 -->|branch| bb_00635FDE
  bb_00635F10 -->|fallthrough| bb_00635F4F
  bb_00635F4F -->|branch| bb_00635F62
  bb_00635F4F -->|fallthrough| bb_00635F56
  bb_00635F56 -->|branch| bb_00635F70
  bb_00635F62 -->|branch| bb_00635F70
  bb_00635F62 -->|fallthrough| bb_00635F66
  bb_00635F66 -->|flow| bb_00635F70
  bb_00635F70 -->|branch| bb_00635F92
  bb_00635F70 -->|fallthrough| bb_00635F86
  bb_00635F86 -->|branch| bb_00635FA5
  bb_00635F86 -->|fallthrough| bb_00635F92
  bb_00635F92 -->|branch| bb_00635FDE
  bb_00635F92 -->|fallthrough| bb_00635FA5
  bb_00635FA5 -->|branch| bb_00635FC8
  bb_00635FAE -->|branch| bb_00635FC5
  bb_00635FAE -->|fallthrough| bb_00635FB7
  bb_00635FB7 -->|flow| bb_00635FC5
  bb_00635FC5 -->|flow| bb_00635FC8
  bb_00635FC8 -->|branch| bb_00635FAE
  bb_00635FC8 -->|fallthrough| bb_00635FCD
  bb_00635FCD -->|branch| bb_00635FDE
  bb_00635FCD -->|fallthrough| bb_00635FD2
  bb_00635FD2 -->|flow| bb_00635FDE
  bb_00635FDE -->|branch| bb_0063606D
  bb_00635FDE -->|fallthrough| bb_00636009
  bb_00636009 -->|branch| bb_00636021
  bb_00636009 -->|fallthrough| bb_00636015
  bb_00636015 -->|branch| bb_00636034
  bb_00636015 -->|fallthrough| bb_00636021
  bb_00636021 -->|branch| bb_0063606D
  bb_00636021 -->|fallthrough| bb_00636034
  bb_00636034 -->|branch| bb_00636057
  bb_0063603D -->|branch| bb_00636054
  bb_0063603D -->|fallthrough| bb_00636046
  bb_00636046 -->|flow| bb_00636054
  bb_00636054 -->|flow| bb_00636057
  bb_00636057 -->|branch| bb_0063603D
  bb_00636057 -->|fallthrough| bb_0063605C
  bb_0063605C -->|branch| bb_0063606D
  bb_0063605C -->|fallthrough| bb_00636061
  bb_00636061 -->|flow| bb_0063606D
```
