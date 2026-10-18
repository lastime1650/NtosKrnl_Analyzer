# DifMmProtectMdlSystemAddressWrapper

- RVA: `0x00636710`–`0x00636874` (길이 `356` bytes)
- VA: `0x0000000140636710`
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
- `0x0063673E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00636766` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00636799` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006367C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006367D9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006367E4` → [MmProtectMdlSystemAddress](../22/MmProtectMdlSystemAddress_function_00227B50.md) (function, `0x00227B50`)
- `0x00636811` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00636838` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00636851` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00636778` → RVA `0x00F048B8` (`.data`; read)
- `0x00636786` → RVA `0x00F04980` (`.data`; read)
- `0x00636792` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636710  48 8B C4                        mov rax, rsp
00636713  48 89 58 08                     mov qword ptr [rax + 8], rbx
00636717  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063671B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063671F  57                              push rdi
00636720  41 56                           push r14
00636722  41 57                           push r15
00636724  48 83 EC 40                     sub rsp, 0x40
00636728  0F 57 C0                        xorps xmm0, xmm0
0063672B  4C 8B F9                        mov r15, rcx
0063672E  B9 B8 01 00 00                  mov ecx, 0x1b8
00636733  44 8B F2                        mov r14d, edx
00636736  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063673A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063673E  E8 F1 F2 E5 FF                  call 0x140495a34
00636743  48 8B F0                        mov rsi, rax
00636746  48 85 C0                        test rax, rax
00636749  0F 84 8F 00 00 00               je 0x1406367de
0063674F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00636752  A8 18                           test al, 0x18
00636754  74 0C                           je 0x140636762
00636756  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063675B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00636760  EB 0E                           jmp 0x140636770
00636762  A8 04                           test al, 4
00636764  74 0A                           je 0x140636770
00636766  E8 9D D4 E9 FF                  call 0x1404d3c08
0063676B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00636770  40 32 ED                        xor bpl, bpl
00636773  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00636778  40 38 2D 39 E1 8C 00            cmp byte ptr [rip + 0x8ce139], bpl
0063677F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00636784  75 0C                           jne 0x140636792
00636786  F7 05 F0 E1 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce1f0], 0x800
00636790  74 13                           je 0x1406367a5
00636792  48 8D 0D E7 D6 8C 00            lea rcx, [rip + 0x8cd6e7]
00636799  E8 82 FE BD FF                  call 0x140216620
0063679E  40 8A E8                        mov bpl, al
006367A1  84 C0                           test al, al
006367A3  74 39                           je 0x1406367de
006367A5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006367A9  48 8B 1F                        mov rbx, qword ptr [rdi]
006367AC  EB 1A                           jmp 0x1406367c8
006367AE  48 8D 43 F0                     lea rax, [rbx - 0x10]
006367B2  48 85 C0                        test rax, rax
006367B5  74 0E                           je 0x1406367c5
006367B7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006367BB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006367C0  E8 0B 43 08 00                  call 0x1406baad0
006367C5  48 8B 1B                        mov rbx, qword ptr [rbx]
006367C8  48 3B DF                        cmp rbx, rdi
006367CB  75 E1                           jne 0x1406367ae
006367CD  40 84 ED                        test bpl, bpl
006367D0  74 0C                           je 0x1406367de
006367D2  48 8D 0D A7 D6 8C 00            lea rcx, [rip + 0x8cd6a7]
006367D9  E8 A2 36 D1 FF                  call 0x140349e80
006367DE  41 8B D6                        mov edx, r14d
006367E1  49 8B CF                        mov rcx, r15
006367E4  E8 67 13 BF FF                  call 0x140227b50
006367E9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
006367ED  48 85 F6                        test rsi, rsi
006367F0  74 64                           je 0x140636856
006367F2  40 32 FF                        xor dil, dil
006367F5  40 38 3D BC E0 8C 00            cmp byte ptr [rip + 0x8ce0bc], dil
006367FC  75 0C                           jne 0x14063680a
006367FE  F7 05 78 E1 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce178], 0x800
00636808  74 13                           je 0x14063681d
0063680A  48 8D 0D 6F D6 8C 00            lea rcx, [rip + 0x8cd66f]
00636811  E8 0A FE BD FF                  call 0x140216620
00636816  40 8A F8                        mov dil, al
00636819  84 C0                           test al, al
0063681B  74 39                           je 0x140636856
0063681D  48 83 C6 30                     add rsi, 0x30
00636821  48 8B 1E                        mov rbx, qword ptr [rsi]
00636824  EB 1A                           jmp 0x140636840
00636826  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063682A  48 85 C0                        test rax, rax
0063682D  74 0E                           je 0x14063683d
0063682F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00636833  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00636838  E8 93 42 08 00                  call 0x1406baad0
0063683D  48 8B 1B                        mov rbx, qword ptr [rbx]
00636840  48 3B DE                        cmp rbx, rsi
00636843  75 E1                           jne 0x140636826
00636845  40 84 FF                        test dil, dil
00636848  74 0C                           je 0x140636856
0063684A  48 8D 0D 2F D6 8C 00            lea rcx, [rip + 0x8cd62f]
00636851  E8 2A 36 D1 FF                  call 0x140349e80
00636856  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0063685A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063685F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00636864  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00636869  48 83 C4 40                     add rsp, 0x40
0063686D  41 5F                           pop r15
0063686F  41 5E                           pop r14
00636871  5F                              pop rdi
00636872  C3                              ret
00636873  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmProtectMdlSystemAddressWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(440, a2, a3, a4);
    if (result == 0) goto loc_006367DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00636762;
    v_stack_m38 = v_stack_p0;
    goto loc_00636770;
loc_00636762:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9232697)) != 0) goto loc_00636792;
    if (((*(unsigned int *)(v_rip + 9232880)) & (0x800ULL)) == 0) goto loc_006367A5;
loc_00636792:
    result = ExAcquireRundownProtection(v_rip + 9230055, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006367DE;
loc_006367A5:
    goto loc_006367C8;
loc_006367AE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006367C8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006367AE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9229991;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmProtectMdlSystemAddress(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00636856;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9232572)) != 0) goto loc_0063680A;
    if (((*(unsigned int *)(v_rip + 9232760)) & (0x800ULL)) == 0) goto loc_0063681D;
loc_0063680A:
    result = ExAcquireRundownProtection(v_rip + 9229935, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00636856;
loc_0063681D:
    v_rsi = (result) + (48);
    goto loc_00636840;
loc_00636826:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00636840:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00636826;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9229871;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifMmProtectMdlSystemAddressWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(440, Arg2, a3, a4);
    if (result == 0) goto loc_006367DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00636762;
    v_stack_m38 = v_stack_p0;
    goto loc_00636770;
loc_00636762:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8CE139)) != 0) goto loc_00636792;
    if (((*(uint32_t *)(v_rip + 0x8CE1F0)) & (0x800ULL)) == 0) goto loc_006367A5;
loc_00636792:
    result = ExAcquireRundownProtection(v_rip + 9230055, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006367DE;
loc_006367A5:
    goto loc_006367C8;
loc_006367AE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006367C8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006367AE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9229991;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = MmProtectMdlSystemAddress(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00636856;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CE0BC)) != 0) goto loc_0063680A;
    if (((*(uint32_t *)(v_rip + 0x8CE178)) & (0x800ULL)) == 0) goto loc_0063681D;
loc_0063680A:
    result = ExAcquireRundownProtection(v_rip + 9229935, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00636856;
loc_0063681D:
    local_rsi = (result) + (48);
    goto loc_00636840;
loc_00636826:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_00636840:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00636826;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9229871;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636710[BB_00636710]
  bb_0063674F[BB_0063674F]
  bb_00636756[BB_00636756]
  bb_00636762[BB_00636762]
  bb_00636766[BB_00636766]
  bb_00636770[BB_00636770]
  bb_00636786[BB_00636786]
  bb_00636792[BB_00636792]
  bb_006367A5[BB_006367A5]
  bb_006367AE[BB_006367AE]
  bb_006367B7[BB_006367B7]
  bb_006367C5[BB_006367C5]
  bb_006367C8[BB_006367C8]
  bb_006367CD[BB_006367CD]
  bb_006367D2[BB_006367D2]
  bb_006367DE[BB_006367DE]
  bb_006367F2[BB_006367F2]
  bb_006367FE[BB_006367FE]
  bb_0063680A[BB_0063680A]
  bb_0063681D[BB_0063681D]
  bb_00636826[BB_00636826]
  bb_0063682F[BB_0063682F]
  bb_0063683D[BB_0063683D]
  bb_00636840[BB_00636840]
  bb_00636845[BB_00636845]
  bb_0063684A[BB_0063684A]
  bb_00636856[BB_00636856]
  bb_00636873[BB_00636873]
  bb_00636710 -->|branch| bb_006367DE
  bb_00636710 -->|fallthrough| bb_0063674F
  bb_0063674F -->|branch| bb_00636762
  bb_0063674F -->|fallthrough| bb_00636756
  bb_00636756 -->|branch| bb_00636770
  bb_00636762 -->|branch| bb_00636770
  bb_00636762 -->|fallthrough| bb_00636766
  bb_00636766 -->|flow| bb_00636770
  bb_00636770 -->|branch| bb_00636792
  bb_00636770 -->|fallthrough| bb_00636786
  bb_00636786 -->|branch| bb_006367A5
  bb_00636786 -->|fallthrough| bb_00636792
  bb_00636792 -->|branch| bb_006367DE
  bb_00636792 -->|fallthrough| bb_006367A5
  bb_006367A5 -->|branch| bb_006367C8
  bb_006367AE -->|branch| bb_006367C5
  bb_006367AE -->|fallthrough| bb_006367B7
  bb_006367B7 -->|flow| bb_006367C5
  bb_006367C5 -->|flow| bb_006367C8
  bb_006367C8 -->|branch| bb_006367AE
  bb_006367C8 -->|fallthrough| bb_006367CD
  bb_006367CD -->|branch| bb_006367DE
  bb_006367CD -->|fallthrough| bb_006367D2
  bb_006367D2 -->|flow| bb_006367DE
  bb_006367DE -->|branch| bb_00636856
  bb_006367DE -->|fallthrough| bb_006367F2
  bb_006367F2 -->|branch| bb_0063680A
  bb_006367F2 -->|fallthrough| bb_006367FE
  bb_006367FE -->|branch| bb_0063681D
  bb_006367FE -->|fallthrough| bb_0063680A
  bb_0063680A -->|branch| bb_00636856
  bb_0063680A -->|fallthrough| bb_0063681D
  bb_0063681D -->|branch| bb_00636840
  bb_00636826 -->|branch| bb_0063683D
  bb_00636826 -->|fallthrough| bb_0063682F
  bb_0063682F -->|flow| bb_0063683D
  bb_0063683D -->|flow| bb_00636840
  bb_00636840 -->|branch| bb_00636826
  bb_00636840 -->|fallthrough| bb_00636845
  bb_00636845 -->|branch| bb_00636856
  bb_00636845 -->|fallthrough| bb_0063684A
  bb_0063684A -->|flow| bb_00636856
```
