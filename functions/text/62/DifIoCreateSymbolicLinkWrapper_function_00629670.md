# DifIoCreateSymbolicLinkWrapper

- RVA: `0x00629670`–`0x006297D4` (길이 `356` bytes)
- VA: `0x0000000140629670`
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
- `0x0062969E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006296C6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006296F9` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629720` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629739` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00629744` → [IoCreateSymbolicLink](../../page/A3/IoCreateSymbolicLink_function_00A33760.md) (function, `0x00A33760`)
- `0x00629771` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629798` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006297B1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006296D8` → RVA `0x00F048B8` (`.data`; read)
- `0x006296E6` → RVA `0x00F04980` (`.data`; read)
- `0x006296F2` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00629744` → [IoCreateSymbolicLink](../../page/A3/IoCreateSymbolicLink_function_00A33760.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00629670  48 8B C4                        mov rax, rsp
00629673  48 89 58 08                     mov qword ptr [rax + 8], rbx
00629677  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062967B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062967F  57                              push rdi
00629680  41 56                           push r14
00629682  41 57                           push r15
00629684  48 83 EC 40                     sub rsp, 0x40
00629688  0F 57 C0                        xorps xmm0, xmm0
0062968B  4C 8B F9                        mov r15, rcx
0062968E  B9 5E 01 00 00                  mov ecx, 0x15e
00629693  4C 8B F2                        mov r14, rdx
00629696  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062969A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062969E  E8 91 C3 E6 FF                  call 0x140495a34
006296A3  48 8B F0                        mov rsi, rax
006296A6  48 85 C0                        test rax, rax
006296A9  0F 84 8F 00 00 00               je 0x14062973e
006296AF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006296B2  A8 18                           test al, 0x18
006296B4  74 0C                           je 0x1406296c2
006296B6  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006296BB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006296C0  EB 0E                           jmp 0x1406296d0
006296C2  A8 04                           test al, 4
006296C4  74 0A                           je 0x1406296d0
006296C6  E8 3D A5 EA FF                  call 0x1404d3c08
006296CB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006296D0  40 32 ED                        xor bpl, bpl
006296D3  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
006296D8  40 38 2D D9 B1 8D 00            cmp byte ptr [rip + 0x8db1d9], bpl
006296DF  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006296E4  75 0C                           jne 0x1406296f2
006296E6  F7 05 90 B2 8D 00 00 08 00 00   test dword ptr [rip + 0x8db290], 0x800
006296F0  74 13                           je 0x140629705
006296F2  48 8D 0D 87 A7 8D 00            lea rcx, [rip + 0x8da787]
006296F9  E8 22 CF BE FF                  call 0x140216620
006296FE  40 8A E8                        mov bpl, al
00629701  84 C0                           test al, al
00629703  74 39                           je 0x14062973e
00629705  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00629709  48 8B 1F                        mov rbx, qword ptr [rdi]
0062970C  EB 1A                           jmp 0x140629728
0062970E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629712  48 85 C0                        test rax, rax
00629715  74 0E                           je 0x140629725
00629717  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062971B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629720  E8 AB 13 09 00                  call 0x1406baad0
00629725  48 8B 1B                        mov rbx, qword ptr [rbx]
00629728  48 3B DF                        cmp rbx, rdi
0062972B  75 E1                           jne 0x14062970e
0062972D  40 84 ED                        test bpl, bpl
00629730  74 0C                           je 0x14062973e
00629732  48 8D 0D 47 A7 8D 00            lea rcx, [rip + 0x8da747]
00629739  E8 42 07 D2 FF                  call 0x140349e80
0062973E  49 8B D6                        mov rdx, r14
00629741  49 8B CF                        mov rcx, r15
00629744  E8 17 A0 40 00                  call 0x140a33760
00629749  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0062974D  48 85 F6                        test rsi, rsi
00629750  74 64                           je 0x1406297b6
00629752  40 32 FF                        xor dil, dil
00629755  40 38 3D 5C B1 8D 00            cmp byte ptr [rip + 0x8db15c], dil
0062975C  75 0C                           jne 0x14062976a
0062975E  F7 05 18 B2 8D 00 00 08 00 00   test dword ptr [rip + 0x8db218], 0x800
00629768  74 13                           je 0x14062977d
0062976A  48 8D 0D 0F A7 8D 00            lea rcx, [rip + 0x8da70f]
00629771  E8 AA CE BE FF                  call 0x140216620
00629776  40 8A F8                        mov dil, al
00629779  84 C0                           test al, al
0062977B  74 39                           je 0x1406297b6
0062977D  48 83 C6 30                     add rsi, 0x30
00629781  48 8B 1E                        mov rbx, qword ptr [rsi]
00629784  EB 1A                           jmp 0x1406297a0
00629786  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062978A  48 85 C0                        test rax, rax
0062978D  74 0E                           je 0x14062979d
0062978F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629793  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629798  E8 33 13 09 00                  call 0x1406baad0
0062979D  48 8B 1B                        mov rbx, qword ptr [rbx]
006297A0  48 3B DE                        cmp rbx, rsi
006297A3  75 E1                           jne 0x140629786
006297A5  40 84 FF                        test dil, dil
006297A8  74 0C                           je 0x1406297b6
006297AA  48 8D 0D CF A6 8D 00            lea rcx, [rip + 0x8da6cf]
006297B1  E8 CA 06 D2 FF                  call 0x140349e80
006297B6  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
006297BA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006297BF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006297C4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006297C9  48 83 C4 40                     add rsp, 0x40
006297CD  41 5F                           pop r15
006297CF  41 5E                           pop r14
006297D1  5F                              pop rdi
006297D2  C3                              ret
006297D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoCreateSymbolicLinkWrapper(__int64 a1, __int64 a2)
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
    result = DifGetAPIThunkContextById(350, a2, a3, a4);
    if (result == 0) goto loc_0062973E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006296C2;
    v_stack_m38 = v_stack_p0;
    goto loc_006296D0;
loc_006296C2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9286105)) != 0) goto loc_006296F2;
    if (((*(unsigned int *)(v_rip + 9286288)) & (0x800ULL)) == 0) goto loc_00629705;
loc_006296F2:
    result = ExAcquireRundownProtection(v_rip + 9283463, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062973E;
loc_00629705:
    goto loc_00629728;
loc_0062970E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629728:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062970E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9283399;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoCreateSymbolicLink(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_006297B6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9285980)) != 0) goto loc_0062976A;
    if (((*(unsigned int *)(v_rip + 9286168)) & (0x800ULL)) == 0) goto loc_0062977D;
loc_0062976A:
    result = ExAcquireRundownProtection(v_rip + 9283343, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006297B6;
loc_0062977D:
    v_rsi = (result) + (48);
    goto loc_006297A0;
loc_00629786:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006297A0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00629786;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9283279;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoCreateSymbolicLinkWrapper(int64_t Arg1, int64_t Arg2)
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
    result = DifGetAPIThunkContextById(350, Arg2, a3, a4);
    if (result == 0) goto loc_0062973E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006296C2;
    v_stack_m38 = v_stack_p0;
    goto loc_006296D0;
loc_006296C2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8DB1D9)) != 0) goto loc_006296F2;
    if (((*(uint32_t *)(v_rip + 0x8DB290)) & (0x800ULL)) == 0) goto loc_00629705;
loc_006296F2:
    result = ExAcquireRundownProtection(v_rip + 9283463, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062973E;
loc_00629705:
    goto loc_00629728;
loc_0062970E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00629728:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062970E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9283399;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoCreateSymbolicLink(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_006297B6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DB15C)) != 0) goto loc_0062976A;
    if (((*(uint32_t *)(v_rip + 0x8DB218)) & (0x800ULL)) == 0) goto loc_0062977D;
loc_0062976A:
    result = ExAcquireRundownProtection(v_rip + 9283343, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006297B6;
loc_0062977D:
    local_rsi = (result) + (48);
    goto loc_006297A0;
loc_00629786:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006297A0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00629786;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9283279;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00629670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00629670[BB_00629670]
  bb_006296AF[BB_006296AF]
  bb_006296B6[BB_006296B6]
  bb_006296C2[BB_006296C2]
  bb_006296C6[BB_006296C6]
  bb_006296D0[BB_006296D0]
  bb_006296E6[BB_006296E6]
  bb_006296F2[BB_006296F2]
  bb_00629705[BB_00629705]
  bb_0062970E[BB_0062970E]
  bb_00629717[BB_00629717]
  bb_00629725[BB_00629725]
  bb_00629728[BB_00629728]
  bb_0062972D[BB_0062972D]
  bb_00629732[BB_00629732]
  bb_0062973E[BB_0062973E]
  bb_00629752[BB_00629752]
  bb_0062975E[BB_0062975E]
  bb_0062976A[BB_0062976A]
  bb_0062977D[BB_0062977D]
  bb_00629786[BB_00629786]
  bb_0062978F[BB_0062978F]
  bb_0062979D[BB_0062979D]
  bb_006297A0[BB_006297A0]
  bb_006297A5[BB_006297A5]
  bb_006297AA[BB_006297AA]
  bb_006297B6[BB_006297B6]
  bb_006297D3[BB_006297D3]
  bb_00629670 -->|branch| bb_0062973E
  bb_00629670 -->|fallthrough| bb_006296AF
  bb_006296AF -->|branch| bb_006296C2
  bb_006296AF -->|fallthrough| bb_006296B6
  bb_006296B6 -->|branch| bb_006296D0
  bb_006296C2 -->|branch| bb_006296D0
  bb_006296C2 -->|fallthrough| bb_006296C6
  bb_006296C6 -->|flow| bb_006296D0
  bb_006296D0 -->|branch| bb_006296F2
  bb_006296D0 -->|fallthrough| bb_006296E6
  bb_006296E6 -->|branch| bb_00629705
  bb_006296E6 -->|fallthrough| bb_006296F2
  bb_006296F2 -->|branch| bb_0062973E
  bb_006296F2 -->|fallthrough| bb_00629705
  bb_00629705 -->|branch| bb_00629728
  bb_0062970E -->|branch| bb_00629725
  bb_0062970E -->|fallthrough| bb_00629717
  bb_00629717 -->|flow| bb_00629725
  bb_00629725 -->|flow| bb_00629728
  bb_00629728 -->|branch| bb_0062970E
  bb_00629728 -->|fallthrough| bb_0062972D
  bb_0062972D -->|branch| bb_0062973E
  bb_0062972D -->|fallthrough| bb_00629732
  bb_00629732 -->|flow| bb_0062973E
  bb_0062973E -->|branch| bb_006297B6
  bb_0062973E -->|fallthrough| bb_00629752
  bb_00629752 -->|branch| bb_0062976A
  bb_00629752 -->|fallthrough| bb_0062975E
  bb_0062975E -->|branch| bb_0062977D
  bb_0062975E -->|fallthrough| bb_0062976A
  bb_0062976A -->|branch| bb_006297B6
  bb_0062976A -->|fallthrough| bb_0062977D
  bb_0062977D -->|branch| bb_006297A0
  bb_00629786 -->|branch| bb_0062979D
  bb_00629786 -->|fallthrough| bb_0062978F
  bb_0062978F -->|flow| bb_0062979D
  bb_0062979D -->|flow| bb_006297A0
  bb_006297A0 -->|branch| bb_00629786
  bb_006297A0 -->|fallthrough| bb_006297A5
  bb_006297A5 -->|branch| bb_006297B6
  bb_006297A5 -->|fallthrough| bb_006297AA
  bb_006297AA -->|flow| bb_006297B6
```
