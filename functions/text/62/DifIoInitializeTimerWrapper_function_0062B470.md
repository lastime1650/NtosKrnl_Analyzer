# DifIoInitializeTimerWrapper

- RVA: `0x0062B470`–`0x0062B5E7` (길이 `375` bytes)
- VA: `0x000000014062B470`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062B4AE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062B4D4` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062B508` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B52E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B547` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062B555` → [IoInitializeTimer](../../page/71/IoInitializeTimer_function_0071D5B0.md) (function, `0x0071D5B0`)
- `0x0062B581` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062B5A7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062B5C0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062B4E4` → RVA `0x00F048B8` (`.data`; read)
- `0x0062B4F5` → RVA `0x00F04980` (`.data`; read)
- `0x0062B501` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062B555` → [IoInitializeTimer](../../page/71/IoInitializeTimer_function_0071D5B0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062B470  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0062B475  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0062B47A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0062B47F  55                              push rbp
0062B480  41 54                           push r12
0062B482  41 55                           push r13
0062B484  41 56                           push r14
0062B486  41 57                           push r15
0062B488  48 8B EC                        mov rbp, rsp
0062B48B  48 83 EC 50                     sub rsp, 0x50
0062B48F  0F 57 C0                        xorps xmm0, xmm0
0062B492  33 C0                           xor eax, eax
0062B494  4C 8B E9                        mov r13, rcx
0062B497  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062B49B  B9 49 01 00 00                  mov ecx, 0x149
0062B4A0  4D 8B F8                        mov r15, r8
0062B4A3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062B4A7  4C 8B E2                        mov r12, rdx
0062B4AA  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062B4AE  E8 81 A5 E6 FF                  call 0x140495a34
0062B4B3  48 8B F0                        mov rsi, rax
0062B4B6  48 85 C0                        test rax, rax
0062B4B9  0F 84 8D 00 00 00               je 0x14062b54c
0062B4BF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062B4C2  A8 18                           test al, 0x18
0062B4C4  74 0A                           je 0x14062b4d0
0062B4C6  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062B4CA  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062B4CE  EB 0D                           jmp 0x14062b4dd
0062B4D0  A8 04                           test al, 4
0062B4D2  74 09                           je 0x14062b4dd
0062B4D4  E8 2F 87 EA FF                  call 0x1404d3c08
0062B4D9  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062B4DD  45 32 F6                        xor r14b, r14b
0062B4E0  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0062B4E4  44 38 35 CD 93 8D 00            cmp byte ptr [rip + 0x8d93cd], r14b
0062B4EB  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0062B4EF  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062B4F3  75 0C                           jne 0x14062b501
0062B4F5  F7 05 81 94 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9481], 0x800
0062B4FF  74 13                           je 0x14062b514
0062B501  48 8D 0D 78 89 8D 00            lea rcx, [rip + 0x8d8978]
0062B508  E8 13 B1 BE FF                  call 0x140216620
0062B50D  44 8A F0                        mov r14b, al
0062B510  84 C0                           test al, al
0062B512  74 38                           je 0x14062b54c
0062B514  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062B518  48 8B 1F                        mov rbx, qword ptr [rdi]
0062B51B  EB 19                           jmp 0x14062b536
0062B51D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B521  48 85 C0                        test rax, rax
0062B524  74 0D                           je 0x14062b533
0062B526  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B52A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062B52E  E8 9D F5 08 00                  call 0x1406baad0
0062B533  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B536  48 3B DF                        cmp rbx, rdi
0062B539  75 E2                           jne 0x14062b51d
0062B53B  45 84 F6                        test r14b, r14b
0062B53E  74 0C                           je 0x14062b54c
0062B540  48 8D 0D 39 89 8D 00            lea rcx, [rip + 0x8d8939]
0062B547  E8 34 E9 D1 FF                  call 0x140349e80
0062B54C  4D 8B C7                        mov r8, r15
0062B54F  49 8B D4                        mov rdx, r12
0062B552  49 8B CD                        mov rcx, r13
0062B555  E8 56 20 0F 00                  call 0x14071d5b0
0062B55A  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0062B55D  48 85 F6                        test rsi, rsi
0062B560  74 63                           je 0x14062b5c5
0062B562  40 32 FF                        xor dil, dil
0062B565  40 38 3D 4C 93 8D 00            cmp byte ptr [rip + 0x8d934c], dil
0062B56C  75 0C                           jne 0x14062b57a
0062B56E  F7 05 08 94 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9408], 0x800
0062B578  74 13                           je 0x14062b58d
0062B57A  48 8D 0D FF 88 8D 00            lea rcx, [rip + 0x8d88ff]
0062B581  E8 9A B0 BE FF                  call 0x140216620
0062B586  40 8A F8                        mov dil, al
0062B589  84 C0                           test al, al
0062B58B  74 38                           je 0x14062b5c5
0062B58D  48 83 C6 30                     add rsi, 0x30
0062B591  48 8B 1E                        mov rbx, qword ptr [rsi]
0062B594  EB 19                           jmp 0x14062b5af
0062B596  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062B59A  48 85 C0                        test rax, rax
0062B59D  74 0D                           je 0x14062b5ac
0062B59F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062B5A3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062B5A7  E8 24 F5 08 00                  call 0x1406baad0
0062B5AC  48 8B 1B                        mov rbx, qword ptr [rbx]
0062B5AF  48 3B DE                        cmp rbx, rsi
0062B5B2  75 E2                           jne 0x14062b596
0062B5B4  40 84 FF                        test dil, dil
0062B5B7  74 0C                           je 0x14062b5c5
0062B5B9  48 8D 0D C0 88 8D 00            lea rcx, [rip + 0x8d88c0]
0062B5C0  E8 BB E8 D1 FF                  call 0x140349e80
0062B5C5  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0062B5C8  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062B5CD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0062B5D1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0062B5D5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0062B5D9  49 8B E3                        mov rsp, r11
0062B5DC  41 5F                           pop r15
0062B5DE  41 5E                           pop r14
0062B5E0  41 5D                           pop r13
0062B5E2  41 5C                           pop r12
0062B5E4  5D                              pop rbp
0062B5E5  C3                              ret
0062B5E6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoInitializeTimerWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(329, a2, a3, a4);
    if (result == 0) goto loc_0062B54C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062B4D0;
    v_stack_m58 = v_stack_p0;
    goto loc_0062B4DD;
loc_0062B4D0:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9278413)) != 0) goto loc_0062B501;
    if (((*(unsigned int *)(v_rip + 9278593)) & (0x800ULL)) == 0) goto loc_0062B514;
loc_0062B501:
    result = ExAcquireRundownProtection(v_rip + 9275768, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062B54C;
loc_0062B514:
    goto loc_0062B536;
loc_0062B51D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062B536:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062B51D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9275705;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoInitializeTimer(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0062B5C5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9278284)) != 0) goto loc_0062B57A;
    if (((*(unsigned int *)(v_rip + 9278472)) & (0x800ULL)) == 0) goto loc_0062B58D;
loc_0062B57A:
    result = ExAcquireRundownProtection(v_rip + 9275647, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062B5C5;
loc_0062B58D:
    v_rsi = (result) + (48);
    goto loc_0062B5AF;
loc_0062B596:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062B5AF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062B596;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9275584;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoInitializeTimerWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(329, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062B54C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062B4D0;
    v_stack_m58 = v_stack_p0;
    goto loc_0062B4DD;
loc_0062B4D0:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D93CD)) != 0) goto loc_0062B501;
    if (((*(uint32_t *)(v_rip + 0x8D9481)) & (0x800ULL)) == 0) goto loc_0062B514;
loc_0062B501:
    result = ExAcquireRundownProtection(v_rip + 9275768, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062B54C;
loc_0062B514:
    goto loc_0062B536;
loc_0062B51D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062B536:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062B51D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9275705;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoInitializeTimer(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0062B5C5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D934C)) != 0) goto loc_0062B57A;
    if (((*(uint32_t *)(v_rip + 0x8D9408)) & (0x800ULL)) == 0) goto loc_0062B58D;
loc_0062B57A:
    result = ExAcquireRundownProtection(v_rip + 9275647, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062B5C5;
loc_0062B58D:
    local_rsi = (result) + (48);
    goto loc_0062B5AF;
loc_0062B596:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062B5AF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062B596;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9275584;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062B470&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062B470[BB_0062B470]
  bb_0062B4BF[BB_0062B4BF]
  bb_0062B4C6[BB_0062B4C6]
  bb_0062B4D0[BB_0062B4D0]
  bb_0062B4D4[BB_0062B4D4]
  bb_0062B4DD[BB_0062B4DD]
  bb_0062B4F5[BB_0062B4F5]
  bb_0062B501[BB_0062B501]
  bb_0062B514[BB_0062B514]
  bb_0062B51D[BB_0062B51D]
  bb_0062B526[BB_0062B526]
  bb_0062B533[BB_0062B533]
  bb_0062B536[BB_0062B536]
  bb_0062B53B[BB_0062B53B]
  bb_0062B540[BB_0062B540]
  bb_0062B54C[BB_0062B54C]
  bb_0062B562[BB_0062B562]
  bb_0062B56E[BB_0062B56E]
  bb_0062B57A[BB_0062B57A]
  bb_0062B58D[BB_0062B58D]
  bb_0062B596[BB_0062B596]
  bb_0062B59F[BB_0062B59F]
  bb_0062B5AC[BB_0062B5AC]
  bb_0062B5AF[BB_0062B5AF]
  bb_0062B5B4[BB_0062B5B4]
  bb_0062B5B9[BB_0062B5B9]
  bb_0062B5C5[BB_0062B5C5]
  bb_0062B5E6[BB_0062B5E6]
  bb_0062B470 -->|branch| bb_0062B54C
  bb_0062B470 -->|fallthrough| bb_0062B4BF
  bb_0062B4BF -->|branch| bb_0062B4D0
  bb_0062B4BF -->|fallthrough| bb_0062B4C6
  bb_0062B4C6 -->|branch| bb_0062B4DD
  bb_0062B4D0 -->|branch| bb_0062B4DD
  bb_0062B4D0 -->|fallthrough| bb_0062B4D4
  bb_0062B4D4 -->|flow| bb_0062B4DD
  bb_0062B4DD -->|branch| bb_0062B501
  bb_0062B4DD -->|fallthrough| bb_0062B4F5
  bb_0062B4F5 -->|branch| bb_0062B514
  bb_0062B4F5 -->|fallthrough| bb_0062B501
  bb_0062B501 -->|branch| bb_0062B54C
  bb_0062B501 -->|fallthrough| bb_0062B514
  bb_0062B514 -->|branch| bb_0062B536
  bb_0062B51D -->|branch| bb_0062B533
  bb_0062B51D -->|fallthrough| bb_0062B526
  bb_0062B526 -->|flow| bb_0062B533
  bb_0062B533 -->|flow| bb_0062B536
  bb_0062B536 -->|branch| bb_0062B51D
  bb_0062B536 -->|fallthrough| bb_0062B53B
  bb_0062B53B -->|branch| bb_0062B54C
  bb_0062B53B -->|fallthrough| bb_0062B540
  bb_0062B540 -->|flow| bb_0062B54C
  bb_0062B54C -->|branch| bb_0062B5C5
  bb_0062B54C -->|fallthrough| bb_0062B562
  bb_0062B562 -->|branch| bb_0062B57A
  bb_0062B562 -->|fallthrough| bb_0062B56E
  bb_0062B56E -->|branch| bb_0062B58D
  bb_0062B56E -->|fallthrough| bb_0062B57A
  bb_0062B57A -->|branch| bb_0062B5C5
  bb_0062B57A -->|fallthrough| bb_0062B58D
  bb_0062B58D -->|branch| bb_0062B5AF
  bb_0062B596 -->|branch| bb_0062B5AC
  bb_0062B596 -->|fallthrough| bb_0062B59F
  bb_0062B59F -->|flow| bb_0062B5AC
  bb_0062B5AC -->|flow| bb_0062B5AF
  bb_0062B5AF -->|branch| bb_0062B596
  bb_0062B5AF -->|fallthrough| bb_0062B5B4
  bb_0062B5B4 -->|branch| bb_0062B5C5
  bb_0062B5B4 -->|fallthrough| bb_0062B5B9
  bb_0062B5B9 -->|flow| bb_0062B5C5
```
