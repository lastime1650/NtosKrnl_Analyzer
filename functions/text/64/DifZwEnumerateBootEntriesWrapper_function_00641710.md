# DifZwEnumerateBootEntriesWrapper

- RVA: `0x00641710`–`0x00641874` (길이 `356` bytes)
- VA: `0x0000000140641710`
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
- `0x0064173E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641766` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641799` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006417C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006417D9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006417E4` → [ZwEnumerateBootEntries](../6A/ZwEnumerateBootEntries_function_006AEDB0.md) (function, `0x006AEDB0`)
- `0x00641811` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641838` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641851` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641778` → RVA `0x00F048B8` (`.data`; read)
- `0x00641786` → RVA `0x00F04980` (`.data`; read)
- `0x00641792` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641710  48 8B C4                        mov rax, rsp
00641713  48 89 58 08                     mov qword ptr [rax + 8], rbx
00641717  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064171B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064171F  57                              push rdi
00641720  41 56                           push r14
00641722  41 57                           push r15
00641724  48 83 EC 40                     sub rsp, 0x40
00641728  0F 57 C0                        xorps xmm0, xmm0
0064172B  4C 8B F9                        mov r15, rcx
0064172E  B9 6A 00 00 00                  mov ecx, 0x6a
00641733  4C 8B F2                        mov r14, rdx
00641736  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0064173A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0064173E  E8 F1 42 E5 FF                  call 0x140495a34
00641743  48 8B F0                        mov rsi, rax
00641746  48 85 C0                        test rax, rax
00641749  0F 84 8F 00 00 00               je 0x1406417de
0064174F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00641752  A8 18                           test al, 0x18
00641754  74 0C                           je 0x140641762
00641756  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0064175B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00641760  EB 0E                           jmp 0x140641770
00641762  A8 04                           test al, 4
00641764  74 0A                           je 0x140641770
00641766  E8 9D 24 E9 FF                  call 0x1404d3c08
0064176B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00641770  40 32 ED                        xor bpl, bpl
00641773  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00641778  40 38 2D 39 31 8C 00            cmp byte ptr [rip + 0x8c3139], bpl
0064177F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00641784  75 0C                           jne 0x140641792
00641786  F7 05 F0 31 8C 00 00 08 00 00   test dword ptr [rip + 0x8c31f0], 0x800
00641790  74 13                           je 0x1406417a5
00641792  48 8D 0D E7 26 8C 00            lea rcx, [rip + 0x8c26e7]
00641799  E8 82 4E BD FF                  call 0x140216620
0064179E  40 8A E8                        mov bpl, al
006417A1  84 C0                           test al, al
006417A3  74 39                           je 0x1406417de
006417A5  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006417A9  48 8B 1F                        mov rbx, qword ptr [rdi]
006417AC  EB 1A                           jmp 0x1406417c8
006417AE  48 8D 43 F0                     lea rax, [rbx - 0x10]
006417B2  48 85 C0                        test rax, rax
006417B5  74 0E                           je 0x1406417c5
006417B7  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006417BB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006417C0  E8 0B 93 07 00                  call 0x1406baad0
006417C5  48 8B 1B                        mov rbx, qword ptr [rbx]
006417C8  48 3B DF                        cmp rbx, rdi
006417CB  75 E1                           jne 0x1406417ae
006417CD  40 84 ED                        test bpl, bpl
006417D0  74 0C                           je 0x1406417de
006417D2  48 8D 0D A7 26 8C 00            lea rcx, [rip + 0x8c26a7]
006417D9  E8 A2 86 D0 FF                  call 0x140349e80
006417DE  49 8B D6                        mov rdx, r14
006417E1  49 8B CF                        mov rcx, r15
006417E4  E8 C7 D5 06 00                  call 0x1406aedb0
006417E9  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
006417ED  48 85 F6                        test rsi, rsi
006417F0  74 64                           je 0x140641856
006417F2  40 32 FF                        xor dil, dil
006417F5  40 38 3D BC 30 8C 00            cmp byte ptr [rip + 0x8c30bc], dil
006417FC  75 0C                           jne 0x14064180a
006417FE  F7 05 78 31 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3178], 0x800
00641808  74 13                           je 0x14064181d
0064180A  48 8D 0D 6F 26 8C 00            lea rcx, [rip + 0x8c266f]
00641811  E8 0A 4E BD FF                  call 0x140216620
00641816  40 8A F8                        mov dil, al
00641819  84 C0                           test al, al
0064181B  74 39                           je 0x140641856
0064181D  48 83 C6 30                     add rsi, 0x30
00641821  48 8B 1E                        mov rbx, qword ptr [rsi]
00641824  EB 1A                           jmp 0x140641840
00641826  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064182A  48 85 C0                        test rax, rax
0064182D  74 0E                           je 0x14064183d
0064182F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641833  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00641838  E8 93 92 07 00                  call 0x1406baad0
0064183D  48 8B 1B                        mov rbx, qword ptr [rbx]
00641840  48 3B DE                        cmp rbx, rsi
00641843  75 E1                           jne 0x140641826
00641845  40 84 FF                        test dil, dil
00641848  74 0C                           je 0x140641856
0064184A  48 8D 0D 2F 26 8C 00            lea rcx, [rip + 0x8c262f]
00641851  E8 2A 86 D0 FF                  call 0x140349e80
00641856  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0064185A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0064185F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00641864  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00641869  48 83 C4 40                     add rsp, 0x40
0064186D  41 5F                           pop r15
0064186F  41 5E                           pop r14
00641871  5F                              pop rdi
00641872  C3                              ret
00641873  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwEnumerateBootEntriesWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(106, a2, a3, a4);
    if (result == 0) goto loc_006417DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641762;
    v_stack_m38 = v_stack_p0;
    goto loc_00641770;
loc_00641762:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9187641)) != 0) goto loc_00641792;
    if (((*(unsigned int *)(v_rip + 9187824)) & (0x800ULL)) == 0) goto loc_006417A5;
loc_00641792:
    result = ExAcquireRundownProtection(v_rip + 9184999, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006417DE;
loc_006417A5:
    goto loc_006417C8;
loc_006417AE:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006417C8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006417AE;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184935;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwEnumerateBootEntries(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_00641856;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9187516)) != 0) goto loc_0064180A;
    if (((*(unsigned int *)(v_rip + 9187704)) & (0x800ULL)) == 0) goto loc_0064181D;
loc_0064180A:
    result = ExAcquireRundownProtection(v_rip + 9184879, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641856;
loc_0064181D:
    v_rsi = (result) + (48);
    goto loc_00641840;
loc_00641826:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641840:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00641826;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184815;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwEnumerateBootEntriesWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(106, Arg2, a3, a4);
    if (result == 0) goto loc_006417DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641762;
    v_stack_m38 = v_stack_p0;
    goto loc_00641770;
loc_00641762:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8C3139)) != 0) goto loc_00641792;
    if (((*(uint32_t *)(v_rip + 0x8C31F0)) & (0x800ULL)) == 0) goto loc_006417A5;
loc_00641792:
    result = ExAcquireRundownProtection(v_rip + 9184999, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006417DE;
loc_006417A5:
    goto loc_006417C8;
loc_006417AE:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006417C8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006417AE;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184935;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ZwEnumerateBootEntries(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_00641856;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C30BC)) != 0) goto loc_0064180A;
    if (((*(uint32_t *)(v_rip + 0x8C3178)) & (0x800ULL)) == 0) goto loc_0064181D;
loc_0064180A:
    result = ExAcquireRundownProtection(v_rip + 9184879, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00641856;
loc_0064181D:
    local_rsi = (result) + (48);
    goto loc_00641840;
loc_00641826:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00641840:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00641826;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184815;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641710[BB_00641710]
  bb_0064174F[BB_0064174F]
  bb_00641756[BB_00641756]
  bb_00641762[BB_00641762]
  bb_00641766[BB_00641766]
  bb_00641770[BB_00641770]
  bb_00641786[BB_00641786]
  bb_00641792[BB_00641792]
  bb_006417A5[BB_006417A5]
  bb_006417AE[BB_006417AE]
  bb_006417B7[BB_006417B7]
  bb_006417C5[BB_006417C5]
  bb_006417C8[BB_006417C8]
  bb_006417CD[BB_006417CD]
  bb_006417D2[BB_006417D2]
  bb_006417DE[BB_006417DE]
  bb_006417F2[BB_006417F2]
  bb_006417FE[BB_006417FE]
  bb_0064180A[BB_0064180A]
  bb_0064181D[BB_0064181D]
  bb_00641826[BB_00641826]
  bb_0064182F[BB_0064182F]
  bb_0064183D[BB_0064183D]
  bb_00641840[BB_00641840]
  bb_00641845[BB_00641845]
  bb_0064184A[BB_0064184A]
  bb_00641856[BB_00641856]
  bb_00641873[BB_00641873]
  bb_00641710 -->|branch| bb_006417DE
  bb_00641710 -->|fallthrough| bb_0064174F
  bb_0064174F -->|branch| bb_00641762
  bb_0064174F -->|fallthrough| bb_00641756
  bb_00641756 -->|branch| bb_00641770
  bb_00641762 -->|branch| bb_00641770
  bb_00641762 -->|fallthrough| bb_00641766
  bb_00641766 -->|flow| bb_00641770
  bb_00641770 -->|branch| bb_00641792
  bb_00641770 -->|fallthrough| bb_00641786
  bb_00641786 -->|branch| bb_006417A5
  bb_00641786 -->|fallthrough| bb_00641792
  bb_00641792 -->|branch| bb_006417DE
  bb_00641792 -->|fallthrough| bb_006417A5
  bb_006417A5 -->|branch| bb_006417C8
  bb_006417AE -->|branch| bb_006417C5
  bb_006417AE -->|fallthrough| bb_006417B7
  bb_006417B7 -->|flow| bb_006417C5
  bb_006417C5 -->|flow| bb_006417C8
  bb_006417C8 -->|branch| bb_006417AE
  bb_006417C8 -->|fallthrough| bb_006417CD
  bb_006417CD -->|branch| bb_006417DE
  bb_006417CD -->|fallthrough| bb_006417D2
  bb_006417D2 -->|flow| bb_006417DE
  bb_006417DE -->|branch| bb_00641856
  bb_006417DE -->|fallthrough| bb_006417F2
  bb_006417F2 -->|branch| bb_0064180A
  bb_006417F2 -->|fallthrough| bb_006417FE
  bb_006417FE -->|branch| bb_0064181D
  bb_006417FE -->|fallthrough| bb_0064180A
  bb_0064180A -->|branch| bb_00641856
  bb_0064180A -->|fallthrough| bb_0064181D
  bb_0064181D -->|branch| bb_00641840
  bb_00641826 -->|branch| bb_0064183D
  bb_00641826 -->|fallthrough| bb_0064182F
  bb_0064182F -->|flow| bb_0064183D
  bb_0064183D -->|flow| bb_00641840
  bb_00641840 -->|branch| bb_00641826
  bb_00641840 -->|fallthrough| bb_00641845
  bb_00641845 -->|branch| bb_00641856
  bb_00641845 -->|fallthrough| bb_0064184A
  bb_0064184A -->|flow| bb_00641856
```
