# DifKeRemoveQueueDpcWrapper

- RVA: `0x00632370`–`0x006324D1` (길이 `353` bytes)
- VA: `0x0000000140632370`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063239F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006323C7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006323F5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063241C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00632435` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063243F` → [KeRemoveQueueDpcEx](../46/KeRemoveQueueDpcEx_function_0046CDC0.md) (function, `0x0046CDC0`)
- `0x0063246C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632493` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006324AC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006323D9` → RVA `0x00F048B8` (`.data`; read)
- `0x006323E2` → RVA `0x00F04980` (`.data`; read)
- `0x006323EE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00632370  4C 8B DC                        mov r11, rsp
00632373  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00632377  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063237B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063237F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00632383  41 56                           push r14
00632385  48 83 EC 40                     sub rsp, 0x40
00632389  33 C0                           xor eax, eax
0063238B  0F 57 C0                        xorps xmm0, xmm0
0063238E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00632393  48 8B E9                        mov rbp, rcx
00632396  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063239A  B9 FD 00 00 00                  mov ecx, 0xfd
0063239F  E8 90 36 E6 FF                  call 0x140495a34
006323A4  48 8B F0                        mov rsi, rax
006323A7  48 85 C0                        test rax, rax
006323AA  0F 84 8A 00 00 00               je 0x14063243a
006323B0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006323B3  A8 18                           test al, 0x18
006323B5  74 0C                           je 0x1406323c3
006323B7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006323BC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006323C1  EB 0E                           jmp 0x1406323d1
006323C3  A8 04                           test al, 4
006323C5  74 0A                           je 0x1406323d1
006323C7  E8 3C 18 EA FF                  call 0x1404d3c08
006323CC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006323D1  40 32 FF                        xor dil, dil
006323D4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006323D9  40 38 3D D8 24 8D 00            cmp byte ptr [rip + 0x8d24d8], dil
006323E0  75 0C                           jne 0x1406323ee
006323E2  F7 05 94 25 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2594], 0x800
006323EC  74 13                           je 0x140632401
006323EE  48 8D 0D 8B 1A 8D 00            lea rcx, [rip + 0x8d1a8b]
006323F5  E8 26 42 BE FF                  call 0x140216620
006323FA  40 8A F8                        mov dil, al
006323FD  84 C0                           test al, al
006323FF  74 39                           je 0x14063243a
00632401  4C 8D 76 20                     lea r14, [rsi + 0x20]
00632405  49 8B 1E                        mov rbx, qword ptr [r14]
00632408  EB 1A                           jmp 0x140632424
0063240A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063240E  48 85 C0                        test rax, rax
00632411  74 0E                           je 0x140632421
00632413  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632417  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063241C  E8 AF 86 08 00                  call 0x1406baad0
00632421  48 8B 1B                        mov rbx, qword ptr [rbx]
00632424  49 3B DE                        cmp rbx, r14
00632427  75 E1                           jne 0x14063240a
00632429  40 84 FF                        test dil, dil
0063242C  74 0C                           je 0x14063243a
0063242E  48 8D 0D 4B 1A 8D 00            lea rcx, [rip + 0x8d1a4b]
00632435  E8 46 7A D1 FF                  call 0x140349e80
0063243A  33 D2                           xor edx, edx
0063243C  48 8B CD                        mov rcx, rbp
0063243F  E8 7C A9 E3 FF                  call 0x14046cdc0
00632444  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00632448  48 85 F6                        test rsi, rsi
0063244B  74 64                           je 0x1406324b1
0063244D  40 32 FF                        xor dil, dil
00632450  40 38 3D 61 24 8D 00            cmp byte ptr [rip + 0x8d2461], dil
00632457  75 0C                           jne 0x140632465
00632459  F7 05 1D 25 8D 00 00 08 00 00   test dword ptr [rip + 0x8d251d], 0x800
00632463  74 13                           je 0x140632478
00632465  48 8D 0D 14 1A 8D 00            lea rcx, [rip + 0x8d1a14]
0063246C  E8 AF 41 BE FF                  call 0x140216620
00632471  40 8A F8                        mov dil, al
00632474  84 C0                           test al, al
00632476  74 39                           je 0x1406324b1
00632478  48 83 C6 30                     add rsi, 0x30
0063247C  48 8B 1E                        mov rbx, qword ptr [rsi]
0063247F  EB 1A                           jmp 0x14063249b
00632481  48 8D 43 F0                     lea rax, [rbx - 0x10]
00632485  48 85 C0                        test rax, rax
00632488  74 0E                           je 0x140632498
0063248A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063248E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00632493  E8 38 86 08 00                  call 0x1406baad0
00632498  48 8B 1B                        mov rbx, qword ptr [rbx]
0063249B  48 3B DE                        cmp rbx, rsi
0063249E  75 E1                           jne 0x140632481
006324A0  40 84 FF                        test dil, dil
006324A3  74 0C                           je 0x1406324b1
006324A5  48 8D 0D D4 19 8D 00            lea rcx, [rip + 0x8d19d4]
006324AC  E8 CF 79 D1 FF                  call 0x140349e80
006324B1  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
006324B5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006324BA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006324BF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006324C4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006324C9  48 83 C4 40                     add rsp, 0x40
006324CD  41 5E                           pop r14
006324CF  C3                              ret
006324D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeRemoveQueueDpcWrapper(__int64 a1, int a2)
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
    result = DifGetAPIThunkContextById(253, a2, a3, a4);
    if (result == 0) goto loc_0063243A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006323C3;
    v_stack_m28 = v_stack_p0;
    goto loc_006323D1;
loc_006323C3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9250008)) != 0) goto loc_006323EE;
    if (((*(unsigned int *)(v_rip + 9250196)) & (0x800ULL)) == 0) goto loc_00632401;
loc_006323EE:
    result = ExAcquireRundownProtection(v_rip + 9247371, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063243A;
loc_00632401:
    goto loc_00632424;
loc_0063240A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632424:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063240A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9247307;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a2 = 0;
    result = KeRemoveQueueDpcEx(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_006324B1;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9249889)) != 0) goto loc_00632465;
    if (((*(unsigned int *)(v_rip + 9250077)) & (0x800ULL)) == 0) goto loc_00632478;
loc_00632465:
    result = ExAcquireRundownProtection(v_rip + 9247252, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006324B1;
loc_00632478:
    v_rsi = (result) + (48);
    goto loc_0063249B;
loc_00632481:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063249B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00632481;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9247188;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeRemoveQueueDpcWrapper(int64_t Arg1, int32_t Arg2)
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
    result = DifGetAPIThunkContextById(253, Arg2, a3, a4);
    if (result == 0) goto loc_0063243A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006323C3;
    v_stack_m28 = v_stack_p0;
    goto loc_006323D1;
loc_006323C3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D24D8)) != 0) goto loc_006323EE;
    if (((*(uint32_t *)(v_rip + 0x8D2594)) & (0x800ULL)) == 0) goto loc_00632401;
loc_006323EE:
    result = ExAcquireRundownProtection(v_rip + 9247371, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063243A;
loc_00632401:
    goto loc_00632424;
loc_0063240A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00632424:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063240A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9247307;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    result = KeRemoveQueueDpcEx(Arg1, Arg2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_006324B1;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D2461)) != 0) goto loc_00632465;
    if (((*(uint32_t *)(v_rip + 0x8D251D)) & (0x800ULL)) == 0) goto loc_00632478;
loc_00632465:
    result = ExAcquireRundownProtection(v_rip + 9247252, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006324B1;
loc_00632478:
    local_rsi = (result) + (48);
    goto loc_0063249B;
loc_00632481:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063249B:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00632481;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9247188;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00632370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00632370[BB_00632370]
  bb_006323B0[BB_006323B0]
  bb_006323B7[BB_006323B7]
  bb_006323C3[BB_006323C3]
  bb_006323C7[BB_006323C7]
  bb_006323D1[BB_006323D1]
  bb_006323E2[BB_006323E2]
  bb_006323EE[BB_006323EE]
  bb_00632401[BB_00632401]
  bb_0063240A[BB_0063240A]
  bb_00632413[BB_00632413]
  bb_00632421[BB_00632421]
  bb_00632424[BB_00632424]
  bb_00632429[BB_00632429]
  bb_0063242E[BB_0063242E]
  bb_0063243A[BB_0063243A]
  bb_0063244D[BB_0063244D]
  bb_00632459[BB_00632459]
  bb_00632465[BB_00632465]
  bb_00632478[BB_00632478]
  bb_00632481[BB_00632481]
  bb_0063248A[BB_0063248A]
  bb_00632498[BB_00632498]
  bb_0063249B[BB_0063249B]
  bb_006324A0[BB_006324A0]
  bb_006324A5[BB_006324A5]
  bb_006324B1[BB_006324B1]
  bb_006324D0[BB_006324D0]
  bb_00632370 -->|branch| bb_0063243A
  bb_00632370 -->|fallthrough| bb_006323B0
  bb_006323B0 -->|branch| bb_006323C3
  bb_006323B0 -->|fallthrough| bb_006323B7
  bb_006323B7 -->|branch| bb_006323D1
  bb_006323C3 -->|branch| bb_006323D1
  bb_006323C3 -->|fallthrough| bb_006323C7
  bb_006323C7 -->|flow| bb_006323D1
  bb_006323D1 -->|branch| bb_006323EE
  bb_006323D1 -->|fallthrough| bb_006323E2
  bb_006323E2 -->|branch| bb_00632401
  bb_006323E2 -->|fallthrough| bb_006323EE
  bb_006323EE -->|branch| bb_0063243A
  bb_006323EE -->|fallthrough| bb_00632401
  bb_00632401 -->|branch| bb_00632424
  bb_0063240A -->|branch| bb_00632421
  bb_0063240A -->|fallthrough| bb_00632413
  bb_00632413 -->|flow| bb_00632421
  bb_00632421 -->|flow| bb_00632424
  bb_00632424 -->|branch| bb_0063240A
  bb_00632424 -->|fallthrough| bb_00632429
  bb_00632429 -->|branch| bb_0063243A
  bb_00632429 -->|fallthrough| bb_0063242E
  bb_0063242E -->|flow| bb_0063243A
  bb_0063243A -->|branch| bb_006324B1
  bb_0063243A -->|fallthrough| bb_0063244D
  bb_0063244D -->|branch| bb_00632465
  bb_0063244D -->|fallthrough| bb_00632459
  bb_00632459 -->|branch| bb_00632478
  bb_00632459 -->|fallthrough| bb_00632465
  bb_00632465 -->|branch| bb_006324B1
  bb_00632465 -->|fallthrough| bb_00632478
  bb_00632478 -->|branch| bb_0063249B
  bb_00632481 -->|branch| bb_00632498
  bb_00632481 -->|fallthrough| bb_0063248A
  bb_0063248A -->|flow| bb_00632498
  bb_00632498 -->|flow| bb_0063249B
  bb_0063249B -->|branch| bb_00632481
  bb_0063249B -->|fallthrough| bb_006324A0
  bb_006324A0 -->|branch| bb_006324B1
  bb_006324A0 -->|fallthrough| bb_006324A5
  bb_006324A5 -->|flow| bb_006324B1
```
