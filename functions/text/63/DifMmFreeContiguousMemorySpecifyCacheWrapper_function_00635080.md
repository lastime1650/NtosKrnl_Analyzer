# DifMmFreeContiguousMemorySpecifyCacheWrapper

- RVA: `0x00635080`–`0x006351E3` (길이 `355` bytes)
- VA: `0x0000000140635080`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `355/355` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006350B2` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006350DA` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00635111` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00635138` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00635151` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00635159` → [MmFreeContiguousMemory](../3F/MmFreeContiguousMemory_function_003F6F60.md) (function, `0x003F6F60`)
- `0x00635182` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006351A9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006351C2` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006350EC` → RVA `0x00F048B8` (`.data`; read)
- `0x006350FE` → RVA `0x00F04980` (`.data`; read)
- `0x0063510A` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00635080  48 8B C4                        mov rax, rsp
00635083  48 89 58 08                     mov qword ptr [rax + 8], rbx
00635087  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063508B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063508F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00635093  41 56                           push r14
00635095  48 83 EC 40                     sub rsp, 0x40
00635099  0F 57 C0                        xorps xmm0, xmm0
0063509C  4C 8B F1                        mov r14, rcx
0063509F  B9 D3 01 00 00                  mov ecx, 0x1d3
006350A4  41 8B D8                        mov ebx, r8d
006350A7  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006350AB  48 8B FA                        mov rdi, rdx
006350AE  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
006350B2  E8 7D 09 E6 FF                  call 0x140495a34
006350B7  48 8B F0                        mov rsi, rax
006350BA  48 85 C0                        test rax, rax
006350BD  0F 84 93 00 00 00               je 0x140635156
006350C3  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006350C6  A8 18                           test al, 0x18
006350C8  74 0C                           je 0x1406350d6
006350CA  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006350CF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006350D4  EB 0E                           jmp 0x1406350e4
006350D6  A8 04                           test al, 4
006350D8  74 0A                           je 0x1406350e4
006350DA  E8 29 EB E9 FF                  call 0x1404d3c08
006350DF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006350E4  40 32 ED                        xor bpl, bpl
006350E7  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
006350EC  40 38 2D C5 F7 8C 00            cmp byte ptr [rip + 0x8cf7c5], bpl
006350F3  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
006350F8  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
006350FC  75 0C                           jne 0x14063510a
006350FE  F7 05 78 F8 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf878], 0x800
00635108  74 13                           je 0x14063511d
0063510A  48 8D 0D 6F ED 8C 00            lea rcx, [rip + 0x8ced6f]
00635111  E8 0A 15 BE FF                  call 0x140216620
00635116  40 8A E8                        mov bpl, al
00635119  84 C0                           test al, al
0063511B  74 39                           je 0x140635156
0063511D  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00635121  48 8B 1F                        mov rbx, qword ptr [rdi]
00635124  EB 1A                           jmp 0x140635140
00635126  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063512A  48 85 C0                        test rax, rax
0063512D  74 0E                           je 0x14063513d
0063512F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00635133  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00635138  E8 93 59 08 00                  call 0x1406baad0
0063513D  48 8B 1B                        mov rbx, qword ptr [rbx]
00635140  48 3B DF                        cmp rbx, rdi
00635143  75 E1                           jne 0x140635126
00635145  40 84 ED                        test bpl, bpl
00635148  74 0C                           je 0x140635156
0063514A  48 8D 0D 2F ED 8C 00            lea rcx, [rip + 0x8ced2f]
00635151  E8 2A 4D D1 FF                  call 0x140349e80
00635156  49 8B CE                        mov rcx, r14
00635159  E8 02 1E DC FF                  call 0x1403f6f60
0063515E  48 85 F6                        test rsi, rsi
00635161  74 64                           je 0x1406351c7
00635163  40 32 FF                        xor dil, dil
00635166  40 38 3D 4B F7 8C 00            cmp byte ptr [rip + 0x8cf74b], dil
0063516D  75 0C                           jne 0x14063517b
0063516F  F7 05 07 F8 8C 00 00 08 00 00   test dword ptr [rip + 0x8cf807], 0x800
00635179  74 13                           je 0x14063518e
0063517B  48 8D 0D FE EC 8C 00            lea rcx, [rip + 0x8cecfe]
00635182  E8 99 14 BE FF                  call 0x140216620
00635187  40 8A F8                        mov dil, al
0063518A  84 C0                           test al, al
0063518C  74 39                           je 0x1406351c7
0063518E  48 83 C6 30                     add rsi, 0x30
00635192  48 8B 1E                        mov rbx, qword ptr [rsi]
00635195  EB 1A                           jmp 0x1406351b1
00635197  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063519B  48 85 C0                        test rax, rax
0063519E  74 0E                           je 0x1406351ae
006351A0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006351A4  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006351A9  E8 22 59 08 00                  call 0x1406baad0
006351AE  48 8B 1B                        mov rbx, qword ptr [rbx]
006351B1  48 3B DE                        cmp rbx, rsi
006351B4  75 E1                           jne 0x140635197
006351B6  40 84 FF                        test dil, dil
006351B9  74 0C                           je 0x1406351c7
006351BB  48 8D 0D BE EC 8C 00            lea rcx, [rip + 0x8cecbe]
006351C2  E8 B9 4C D1 FF                  call 0x140349e80
006351C7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006351CC  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006351D1  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006351D6  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006351DB  48 83 C4 40                     add rsp, 0x40
006351DF  41 5E                           pop r14
006351E1  C3                              ret
006351E2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmFreeContiguousMemorySpecifyCacheWrapper(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
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
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(467, a2, a3, a4);
    if (result == 0) goto loc_00635156;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006350D6;
    v_stack_m28 = v_stack_p0;
    goto loc_006350E4;
loc_006350D6:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rbp = 0;
    v_stack_m10 = a1;
    v_stack_m18 = a2;
    v_stack_m20 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9238469)) != 0) goto loc_0063510A;
    if (((*(unsigned int *)(v_rip + 9238648)) & (0x800ULL)) == 0) goto loc_0063511D;
loc_0063510A:
    result = ExAcquireRundownProtection(v_rip + 9235823, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00635156;
loc_0063511D:
    goto loc_00635140;
loc_00635126:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00635140:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00635126;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9235759;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmFreeContiguousMemory(a1, a2, a3, a4);
    if (result == 0) goto loc_006351C7;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9238347)) != 0) goto loc_0063517B;
    if (((*(unsigned int *)(v_rip + 9238535)) & (0x800ULL)) == 0) goto loc_0063518E;
loc_0063517B:
    result = ExAcquireRundownProtection(v_rip + 9235710, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006351C7;
loc_0063518E:
    v_rsi = (result) + (48);
    goto loc_006351B1;
loc_00635197:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006351B1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00635197;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9235646;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmFreeContiguousMemorySpecifyCacheWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
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
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(467, Arg2, Arg3, a4);
    if (result == 0) goto loc_00635156;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006350D6;
    v_stack_m28 = v_stack_p0;
    goto loc_006350E4;
loc_006350D6:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m28 = result;
    }
    local_rbp = 0;
    v_stack_m10 = Arg1;
    v_stack_m18 = Arg2;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8CF7C5)) != 0) goto loc_0063510A;
    if (((*(uint32_t *)(v_rip + 0x8CF878)) & (0x800ULL)) == 0) goto loc_0063511D;
loc_0063510A:
    result = ExAcquireRundownProtection(v_rip + 9235823, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00635156;
loc_0063511D:
    goto loc_00635140;
loc_00635126:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00635140:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00635126;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9235759;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = MmFreeContiguousMemory(Arg1, Arg2, Arg3, a4);
    if (result == 0) goto loc_006351C7;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CF74B)) != 0) goto loc_0063517B;
    if (((*(uint32_t *)(v_rip + 0x8CF807)) & (0x800ULL)) == 0) goto loc_0063518E;
loc_0063517B:
    result = ExAcquireRundownProtection(v_rip + 9235710, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006351C7;
loc_0063518E:
    local_rsi = (result) + (48);
    goto loc_006351B1;
loc_00635197:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_006351B1:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00635197;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9235646;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00635080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00635080[BB_00635080]
  bb_006350C3[BB_006350C3]
  bb_006350CA[BB_006350CA]
  bb_006350D6[BB_006350D6]
  bb_006350DA[BB_006350DA]
  bb_006350E4[BB_006350E4]
  bb_006350FE[BB_006350FE]
  bb_0063510A[BB_0063510A]
  bb_0063511D[BB_0063511D]
  bb_00635126[BB_00635126]
  bb_0063512F[BB_0063512F]
  bb_0063513D[BB_0063513D]
  bb_00635140[BB_00635140]
  bb_00635145[BB_00635145]
  bb_0063514A[BB_0063514A]
  bb_00635156[BB_00635156]
  bb_00635163[BB_00635163]
  bb_0063516F[BB_0063516F]
  bb_0063517B[BB_0063517B]
  bb_0063518E[BB_0063518E]
  bb_00635197[BB_00635197]
  bb_006351A0[BB_006351A0]
  bb_006351AE[BB_006351AE]
  bb_006351B1[BB_006351B1]
  bb_006351B6[BB_006351B6]
  bb_006351BB[BB_006351BB]
  bb_006351C7[BB_006351C7]
  bb_006351E2[BB_006351E2]
  bb_00635080 -->|branch| bb_00635156
  bb_00635080 -->|fallthrough| bb_006350C3
  bb_006350C3 -->|branch| bb_006350D6
  bb_006350C3 -->|fallthrough| bb_006350CA
  bb_006350CA -->|branch| bb_006350E4
  bb_006350D6 -->|branch| bb_006350E4
  bb_006350D6 -->|fallthrough| bb_006350DA
  bb_006350DA -->|flow| bb_006350E4
  bb_006350E4 -->|branch| bb_0063510A
  bb_006350E4 -->|fallthrough| bb_006350FE
  bb_006350FE -->|branch| bb_0063511D
  bb_006350FE -->|fallthrough| bb_0063510A
  bb_0063510A -->|branch| bb_00635156
  bb_0063510A -->|fallthrough| bb_0063511D
  bb_0063511D -->|branch| bb_00635140
  bb_00635126 -->|branch| bb_0063513D
  bb_00635126 -->|fallthrough| bb_0063512F
  bb_0063512F -->|flow| bb_0063513D
  bb_0063513D -->|flow| bb_00635140
  bb_00635140 -->|branch| bb_00635126
  bb_00635140 -->|fallthrough| bb_00635145
  bb_00635145 -->|branch| bb_00635156
  bb_00635145 -->|fallthrough| bb_0063514A
  bb_0063514A -->|flow| bb_00635156
  bb_00635156 -->|branch| bb_006351C7
  bb_00635156 -->|fallthrough| bb_00635163
  bb_00635163 -->|branch| bb_0063517B
  bb_00635163 -->|fallthrough| bb_0063516F
  bb_0063516F -->|branch| bb_0063518E
  bb_0063516F -->|fallthrough| bb_0063517B
  bb_0063517B -->|branch| bb_006351C7
  bb_0063517B -->|fallthrough| bb_0063518E
  bb_0063518E -->|branch| bb_006351B1
  bb_00635197 -->|branch| bb_006351AE
  bb_00635197 -->|fallthrough| bb_006351A0
  bb_006351A0 -->|flow| bb_006351AE
  bb_006351AE -->|flow| bb_006351B1
  bb_006351B1 -->|branch| bb_00635197
  bb_006351B1 -->|fallthrough| bb_006351B6
  bb_006351B6 -->|branch| bb_006351C7
  bb_006351B6 -->|fallthrough| bb_006351BB
  bb_006351BB -->|flow| bb_006351C7
```
