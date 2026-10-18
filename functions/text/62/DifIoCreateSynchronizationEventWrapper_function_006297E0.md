# DifIoCreateSynchronizationEventWrapper

- RVA: `0x006297E0`–`0x00629946` (길이 `358` bytes)
- VA: `0x00000001406297E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062980E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00629836` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00629869` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629890` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006298A9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006298B4` → [IoCreateSynchronizationEvent](../../page/71/IoCreateSynchronizationEvent_function_0071D2C0.md) (function, `0x0071D2C0`)
- `0x006298E2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629909` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629922` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00629848` → RVA `0x00F048B8` (`.data`; read)
- `0x00629856` → RVA `0x00F04980` (`.data`; read)
- `0x00629862` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006298B4` → [IoCreateSynchronizationEvent](../../page/71/IoCreateSynchronizationEvent_function_0071D2C0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006297E0  48 8B C4                        mov rax, rsp
006297E3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006297E7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006297EB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006297EF  57                              push rdi
006297F0  41 56                           push r14
006297F2  41 57                           push r15
006297F4  48 83 EC 40                     sub rsp, 0x40
006297F8  0F 57 C0                        xorps xmm0, xmm0
006297FB  4C 8B F9                        mov r15, rcx
006297FE  B9 5D 01 00 00                  mov ecx, 0x15d
00629803  4C 8B F2                        mov r14, rdx
00629806  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062980A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062980E  E8 21 C2 E6 FF                  call 0x140495a34
00629813  48 8B F0                        mov rsi, rax
00629816  48 85 C0                        test rax, rax
00629819  0F 84 8F 00 00 00               je 0x1406298ae
0062981F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00629822  A8 18                           test al, 0x18
00629824  74 0C                           je 0x140629832
00629826  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062982B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00629830  EB 0E                           jmp 0x140629840
00629832  A8 04                           test al, 4
00629834  74 0A                           je 0x140629840
00629836  E8 CD A3 EA FF                  call 0x1404d3c08
0062983B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00629840  40 32 ED                        xor bpl, bpl
00629843  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00629848  40 38 2D 69 B0 8D 00            cmp byte ptr [rip + 0x8db069], bpl
0062984F  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00629854  75 0C                           jne 0x140629862
00629856  F7 05 20 B1 8D 00 00 08 00 00   test dword ptr [rip + 0x8db120], 0x800
00629860  74 13                           je 0x140629875
00629862  48 8D 0D 17 A6 8D 00            lea rcx, [rip + 0x8da617]
00629869  E8 B2 CD BE FF                  call 0x140216620
0062986E  40 8A E8                        mov bpl, al
00629871  84 C0                           test al, al
00629873  74 39                           je 0x1406298ae
00629875  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00629879  48 8B 1F                        mov rbx, qword ptr [rdi]
0062987C  EB 1A                           jmp 0x140629898
0062987E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629882  48 85 C0                        test rax, rax
00629885  74 0E                           je 0x140629895
00629887  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062988B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629890  E8 3B 12 09 00                  call 0x1406baad0
00629895  48 8B 1B                        mov rbx, qword ptr [rbx]
00629898  48 3B DF                        cmp rbx, rdi
0062989B  75 E1                           jne 0x14062987e
0062989D  40 84 ED                        test bpl, bpl
006298A0  74 0C                           je 0x1406298ae
006298A2  48 8D 0D D7 A5 8D 00            lea rcx, [rip + 0x8da5d7]
006298A9  E8 D2 05 D2 FF                  call 0x140349e80
006298AE  49 8B D6                        mov rdx, r14
006298B1  49 8B CF                        mov rcx, r15
006298B4  E8 07 3A 0F 00                  call 0x14071d2c0
006298B9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006298BE  48 85 F6                        test rsi, rsi
006298C1  74 64                           je 0x140629927
006298C3  40 32 FF                        xor dil, dil
006298C6  40 38 3D EB AF 8D 00            cmp byte ptr [rip + 0x8dafeb], dil
006298CD  75 0C                           jne 0x1406298db
006298CF  F7 05 A7 B0 8D 00 00 08 00 00   test dword ptr [rip + 0x8db0a7], 0x800
006298D9  74 13                           je 0x1406298ee
006298DB  48 8D 0D 9E A5 8D 00            lea rcx, [rip + 0x8da59e]
006298E2  E8 39 CD BE FF                  call 0x140216620
006298E7  40 8A F8                        mov dil, al
006298EA  84 C0                           test al, al
006298EC  74 39                           je 0x140629927
006298EE  48 83 C6 30                     add rsi, 0x30
006298F2  48 8B 1E                        mov rbx, qword ptr [rsi]
006298F5  EB 1A                           jmp 0x140629911
006298F7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006298FB  48 85 C0                        test rax, rax
006298FE  74 0E                           je 0x14062990e
00629900  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629904  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629909  E8 C2 11 09 00                  call 0x1406baad0
0062990E  48 8B 1B                        mov rbx, qword ptr [rbx]
00629911  48 3B DE                        cmp rbx, rsi
00629914  75 E1                           jne 0x1406298f7
00629916  40 84 FF                        test dil, dil
00629919  74 0C                           je 0x140629927
0062991B  48 8D 0D 5E A5 8D 00            lea rcx, [rip + 0x8da55e]
00629922  E8 59 05 D2 FF                  call 0x140349e80
00629927  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0062992C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00629931  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00629936  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062993B  48 83 C4 40                     add rsp, 0x40
0062993F  41 5F                           pop r15
00629941  41 5E                           pop r14
00629943  5F                              pop rdi
00629944  C3                              ret
00629945  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoCreateSynchronizationEventWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
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
    result = DifGetAPIThunkContextById(349, a2, a3, a4);
    if (result == 0) goto loc_006298AE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00629832;
    v_stack_m38 = v_stack_p0;
    goto loc_00629840;
loc_00629832:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9285737)) != 0) goto loc_00629862;
    if (((*(unsigned int *)(v_rip + 9285920)) & (0x800ULL)) == 0) goto loc_00629875;
loc_00629862:
    result = ExAcquireRundownProtection(v_rip + 9283095, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006298AE;
loc_00629875:
    goto loc_00629898;
loc_0062987E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629898:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062987E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9283031;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoCreateSynchronizationEvent(a1, a2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00629927;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9285611)) != 0) goto loc_006298DB;
    if (((*(unsigned int *)(v_rip + 9285799)) & (0x800ULL)) == 0) goto loc_006298EE;
loc_006298DB:
    result = ExAcquireRundownProtection(v_rip + 9282974, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00629927;
loc_006298EE:
    v_rsi = (result) + (48);
    goto loc_00629911;
loc_006298F7:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629911:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006298F7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9282910;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoCreateSynchronizationEventWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
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
    result = DifGetAPIThunkContextById(349, Arg2, a3, a4);
    if (result == 0) goto loc_006298AE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00629832;
    v_stack_m38 = v_stack_p0;
    goto loc_00629840;
loc_00629832:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8DB069)) != 0) goto loc_00629862;
    if (((*(uint32_t *)(v_rip + 0x8DB120)) & (0x800ULL)) == 0) goto loc_00629875;
loc_00629862:
    result = ExAcquireRundownProtection(v_rip + 9283095, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006298AE;
loc_00629875:
    goto loc_00629898;
loc_0062987E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00629898:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062987E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9283031;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoCreateSynchronizationEvent(Arg1, Arg2, a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00629927;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DAFEB)) != 0) goto loc_006298DB;
    if (((*(uint32_t *)(v_rip + 0x8DB0A7)) & (0x800ULL)) == 0) goto loc_006298EE;
loc_006298DB:
    result = ExAcquireRundownProtection(v_rip + 9282974, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00629927;
loc_006298EE:
    local_rsi = (result) + (48);
    goto loc_00629911;
loc_006298F7:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00629911:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006298F7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9282910;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006297E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006297E0[BB_006297E0]
  bb_0062981F[BB_0062981F]
  bb_00629826[BB_00629826]
  bb_00629832[BB_00629832]
  bb_00629836[BB_00629836]
  bb_00629840[BB_00629840]
  bb_00629856[BB_00629856]
  bb_00629862[BB_00629862]
  bb_00629875[BB_00629875]
  bb_0062987E[BB_0062987E]
  bb_00629887[BB_00629887]
  bb_00629895[BB_00629895]
  bb_00629898[BB_00629898]
  bb_0062989D[BB_0062989D]
  bb_006298A2[BB_006298A2]
  bb_006298AE[BB_006298AE]
  bb_006298C3[BB_006298C3]
  bb_006298CF[BB_006298CF]
  bb_006298DB[BB_006298DB]
  bb_006298EE[BB_006298EE]
  bb_006298F7[BB_006298F7]
  bb_00629900[BB_00629900]
  bb_0062990E[BB_0062990E]
  bb_00629911[BB_00629911]
  bb_00629916[BB_00629916]
  bb_0062991B[BB_0062991B]
  bb_00629927[BB_00629927]
  bb_00629945[BB_00629945]
  bb_006297E0 -->|branch| bb_006298AE
  bb_006297E0 -->|fallthrough| bb_0062981F
  bb_0062981F -->|branch| bb_00629832
  bb_0062981F -->|fallthrough| bb_00629826
  bb_00629826 -->|branch| bb_00629840
  bb_00629832 -->|branch| bb_00629840
  bb_00629832 -->|fallthrough| bb_00629836
  bb_00629836 -->|flow| bb_00629840
  bb_00629840 -->|branch| bb_00629862
  bb_00629840 -->|fallthrough| bb_00629856
  bb_00629856 -->|branch| bb_00629875
  bb_00629856 -->|fallthrough| bb_00629862
  bb_00629862 -->|branch| bb_006298AE
  bb_00629862 -->|fallthrough| bb_00629875
  bb_00629875 -->|branch| bb_00629898
  bb_0062987E -->|branch| bb_00629895
  bb_0062987E -->|fallthrough| bb_00629887
  bb_00629887 -->|flow| bb_00629895
  bb_00629895 -->|flow| bb_00629898
  bb_00629898 -->|branch| bb_0062987E
  bb_00629898 -->|fallthrough| bb_0062989D
  bb_0062989D -->|branch| bb_006298AE
  bb_0062989D -->|fallthrough| bb_006298A2
  bb_006298A2 -->|flow| bb_006298AE
  bb_006298AE -->|branch| bb_00629927
  bb_006298AE -->|fallthrough| bb_006298C3
  bb_006298C3 -->|branch| bb_006298DB
  bb_006298C3 -->|fallthrough| bb_006298CF
  bb_006298CF -->|branch| bb_006298EE
  bb_006298CF -->|fallthrough| bb_006298DB
  bb_006298DB -->|branch| bb_00629927
  bb_006298DB -->|fallthrough| bb_006298EE
  bb_006298EE -->|branch| bb_00629911
  bb_006298F7 -->|branch| bb_0062990E
  bb_006298F7 -->|fallthrough| bb_00629900
  bb_00629900 -->|flow| bb_0062990E
  bb_0062990E -->|flow| bb_00629911
  bb_00629911 -->|branch| bb_006298F7
  bb_00629911 -->|fallthrough| bb_00629916
  bb_00629916 -->|branch| bb_00629927
  bb_00629916 -->|fallthrough| bb_0062991B
  bb_0062991B -->|flow| bb_00629927
```
