# DifMmAllocateNonCachedMemoryWrapper

- RVA: `0x00634720`–`0x00634881` (길이 `353` bytes)
- VA: `0x0000000140634720`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063474F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00634777` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006347A5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006347CC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006347E5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006347ED` → [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) (function, `0x007FBB60`)
- `0x0063481B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634842` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063485B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00634789` → RVA `0x00F048B8` (`.data`; read)
- `0x00634792` → RVA `0x00F04980` (`.data`; read)
- `0x0063479E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006347ED` → [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00634720  4C 8B DC                        mov r11, rsp
00634723  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00634727  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063472B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063472F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00634733  41 56                           push r14
00634735  48 83 EC 40                     sub rsp, 0x40
00634739  33 C0                           xor eax, eax
0063473B  0F 57 C0                        xorps xmm0, xmm0
0063473E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00634743  48 8B E9                        mov rbp, rcx
00634746  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063474A  B9 E7 00 00 00                  mov ecx, 0xe7
0063474F  E8 E0 12 E6 FF                  call 0x140495a34
00634754  48 8B F0                        mov rsi, rax
00634757  48 85 C0                        test rax, rax
0063475A  0F 84 8A 00 00 00               je 0x1406347ea
00634760  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00634763  A8 18                           test al, 0x18
00634765  74 0C                           je 0x140634773
00634767  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063476C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00634771  EB 0E                           jmp 0x140634781
00634773  A8 04                           test al, 4
00634775  74 0A                           je 0x140634781
00634777  E8 8C F4 E9 FF                  call 0x1404d3c08
0063477C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00634781  40 32 FF                        xor dil, dil
00634784  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00634789  40 38 3D 28 01 8D 00            cmp byte ptr [rip + 0x8d0128], dil
00634790  75 0C                           jne 0x14063479e
00634792  F7 05 E4 01 8D 00 00 08 00 00   test dword ptr [rip + 0x8d01e4], 0x800
0063479C  74 13                           je 0x1406347b1
0063479E  48 8D 0D DB F6 8C 00            lea rcx, [rip + 0x8cf6db]
006347A5  E8 76 1E BE FF                  call 0x140216620
006347AA  40 8A F8                        mov dil, al
006347AD  84 C0                           test al, al
006347AF  74 39                           je 0x1406347ea
006347B1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006347B5  49 8B 1E                        mov rbx, qword ptr [r14]
006347B8  EB 1A                           jmp 0x1406347d4
006347BA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006347BE  48 85 C0                        test rax, rax
006347C1  74 0E                           je 0x1406347d1
006347C3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006347C7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006347CC  E8 FF 62 08 00                  call 0x1406baad0
006347D1  48 8B 1B                        mov rbx, qword ptr [rbx]
006347D4  49 3B DE                        cmp rbx, r14
006347D7  75 E1                           jne 0x1406347ba
006347D9  40 84 FF                        test dil, dil
006347DC  74 0C                           je 0x1406347ea
006347DE  48 8D 0D 9B F6 8C 00            lea rcx, [rip + 0x8cf69b]
006347E5  E8 96 56 D1 FF                  call 0x140349e80
006347EA  48 8B CD                        mov rcx, rbp
006347ED  E8 6E 73 1C 00                  call 0x1407fbb60
006347F2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
006347F7  48 85 F6                        test rsi, rsi
006347FA  74 64                           je 0x140634860
006347FC  40 32 FF                        xor dil, dil
006347FF  40 38 3D B2 00 8D 00            cmp byte ptr [rip + 0x8d00b2], dil
00634806  75 0C                           jne 0x140634814
00634808  F7 05 6E 01 8D 00 00 08 00 00   test dword ptr [rip + 0x8d016e], 0x800
00634812  74 13                           je 0x140634827
00634814  48 8D 0D 65 F6 8C 00            lea rcx, [rip + 0x8cf665]
0063481B  E8 00 1E BE FF                  call 0x140216620
00634820  40 8A F8                        mov dil, al
00634823  84 C0                           test al, al
00634825  74 39                           je 0x140634860
00634827  48 83 C6 30                     add rsi, 0x30
0063482B  48 8B 1E                        mov rbx, qword ptr [rsi]
0063482E  EB 1A                           jmp 0x14063484a
00634830  48 8D 43 F0                     lea rax, [rbx - 0x10]
00634834  48 85 C0                        test rax, rax
00634837  74 0E                           je 0x140634847
00634839  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063483D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00634842  E8 89 62 08 00                  call 0x1406baad0
00634847  48 8B 1B                        mov rbx, qword ptr [rbx]
0063484A  48 3B DE                        cmp rbx, rsi
0063484D  75 E1                           jne 0x140634830
0063484F  40 84 FF                        test dil, dil
00634852  74 0C                           je 0x140634860
00634854  48 8D 0D 25 F6 8C 00            lea rcx, [rip + 0x8cf625]
0063485B  E8 20 56 D1 FF                  call 0x140349e80
00634860  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00634865  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0063486A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063486F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00634874  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00634879  48 83 C4 40                     add rsp, 0x40
0063487D  41 5E                           pop r14
0063487F  C3                              ret
00634880  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocateNonCachedMemoryWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
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
    result = DifGetAPIThunkContextById(231, a2, a3, a4);
    if (result == 0) goto loc_006347EA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00634773;
    v_stack_m28 = v_stack_p0;
    goto loc_00634781;
loc_00634773:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9240872)) != 0) goto loc_0063479E;
    if (((*(unsigned int *)(v_rip + 9241060)) & (0x800ULL)) == 0) goto loc_006347B1;
loc_0063479E:
    result = ExAcquireRundownProtection(v_rip + 9238235, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006347EA;
loc_006347B1:
    goto loc_006347D4;
loc_006347BA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006347D4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006347BA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9238171;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmAllocateNonCachedMemory(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00634860;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9240754)) != 0) goto loc_00634814;
    if (((*(unsigned int *)(v_rip + 9240942)) & (0x800ULL)) == 0) goto loc_00634827;
loc_00634814:
    result = ExAcquireRundownProtection(v_rip + 9238117, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00634860;
loc_00634827:
    v_rsi = (result) + (48);
    goto loc_0063484A;
loc_00634830:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063484A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00634830;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9238053;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocateNonCachedMemoryWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(231, a2, a3, a4);
    if (result == 0) goto loc_006347EA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00634773;
    v_stack_m28 = v_stack_p0;
    goto loc_00634781;
loc_00634773:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D0128)) != 0) goto loc_0063479E;
    if (((*(uint32_t *)(v_rip + 0x8D01E4)) & (0x800ULL)) == 0) goto loc_006347B1;
loc_0063479E:
    result = ExAcquireRundownProtection(v_rip + 9238235, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006347EA;
loc_006347B1:
    goto loc_006347D4;
loc_006347BA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006347D4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006347BA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9238171;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = MmAllocateNonCachedMemory(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00634860;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D00B2)) != 0) goto loc_00634814;
    if (((*(uint32_t *)(v_rip + 0x8D016E)) & (0x800ULL)) == 0) goto loc_00634827;
loc_00634814:
    result = ExAcquireRundownProtection(v_rip + 9238117, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00634860;
loc_00634827:
    local_rsi = (result) + (48);
    goto loc_0063484A;
loc_00634830:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063484A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00634830;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9238053;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00634720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00634720[BB_00634720]
  bb_00634760[BB_00634760]
  bb_00634767[BB_00634767]
  bb_00634773[BB_00634773]
  bb_00634777[BB_00634777]
  bb_00634781[BB_00634781]
  bb_00634792[BB_00634792]
  bb_0063479E[BB_0063479E]
  bb_006347B1[BB_006347B1]
  bb_006347BA[BB_006347BA]
  bb_006347C3[BB_006347C3]
  bb_006347D1[BB_006347D1]
  bb_006347D4[BB_006347D4]
  bb_006347D9[BB_006347D9]
  bb_006347DE[BB_006347DE]
  bb_006347EA[BB_006347EA]
  bb_006347FC[BB_006347FC]
  bb_00634808[BB_00634808]
  bb_00634814[BB_00634814]
  bb_00634827[BB_00634827]
  bb_00634830[BB_00634830]
  bb_00634839[BB_00634839]
  bb_00634847[BB_00634847]
  bb_0063484A[BB_0063484A]
  bb_0063484F[BB_0063484F]
  bb_00634854[BB_00634854]
  bb_00634860[BB_00634860]
  bb_00634880[BB_00634880]
  bb_00634720 -->|branch| bb_006347EA
  bb_00634720 -->|fallthrough| bb_00634760
  bb_00634760 -->|branch| bb_00634773
  bb_00634760 -->|fallthrough| bb_00634767
  bb_00634767 -->|branch| bb_00634781
  bb_00634773 -->|branch| bb_00634781
  bb_00634773 -->|fallthrough| bb_00634777
  bb_00634777 -->|flow| bb_00634781
  bb_00634781 -->|branch| bb_0063479E
  bb_00634781 -->|fallthrough| bb_00634792
  bb_00634792 -->|branch| bb_006347B1
  bb_00634792 -->|fallthrough| bb_0063479E
  bb_0063479E -->|branch| bb_006347EA
  bb_0063479E -->|fallthrough| bb_006347B1
  bb_006347B1 -->|branch| bb_006347D4
  bb_006347BA -->|branch| bb_006347D1
  bb_006347BA -->|fallthrough| bb_006347C3
  bb_006347C3 -->|flow| bb_006347D1
  bb_006347D1 -->|flow| bb_006347D4
  bb_006347D4 -->|branch| bb_006347BA
  bb_006347D4 -->|fallthrough| bb_006347D9
  bb_006347D9 -->|branch| bb_006347EA
  bb_006347D9 -->|fallthrough| bb_006347DE
  bb_006347DE -->|flow| bb_006347EA
  bb_006347EA -->|branch| bb_00634860
  bb_006347EA -->|fallthrough| bb_006347FC
  bb_006347FC -->|branch| bb_00634814
  bb_006347FC -->|fallthrough| bb_00634808
  bb_00634808 -->|branch| bb_00634827
  bb_00634808 -->|fallthrough| bb_00634814
  bb_00634814 -->|branch| bb_00634860
  bb_00634814 -->|fallthrough| bb_00634827
  bb_00634827 -->|branch| bb_0063484A
  bb_00634830 -->|branch| bb_00634847
  bb_00634830 -->|fallthrough| bb_00634839
  bb_00634839 -->|flow| bb_00634847
  bb_00634847 -->|flow| bb_0063484A
  bb_0063484A -->|branch| bb_00634830
  bb_0063484A -->|fallthrough| bb_0063484F
  bb_0063484F -->|branch| bb_00634860
  bb_0063484F -->|fallthrough| bb_00634854
  bb_00634854 -->|flow| bb_00634860
```
