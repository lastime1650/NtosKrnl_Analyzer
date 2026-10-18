# DifIoReleaseRemoveLockAndWaitExWrapper

- RVA: `0x0062C690`–`0x0062C802` (길이 `370` bytes)
- VA: `0x000000014062C690`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062C6C6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062C6EE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062C726` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C74D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C766` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062C774` → [IoReleaseRemoveLockAndWaitEx](../4B/IoReleaseRemoveLockAndWaitEx_function_004B17B0.md) (function, `0x004B17B0`)
- `0x0062C79D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C7C4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C7DD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062C700` → RVA `0x00F048B8` (`.data`; read)
- `0x0062C713` → RVA `0x00F04980` (`.data`; read)
- `0x0062C71F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062C690  48 8B C4                        mov rax, rsp
0062C693  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062C697  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062C69B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062C69F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062C6A3  41 54                           push r12
0062C6A5  41 56                           push r14
0062C6A7  41 57                           push r15
0062C6A9  48 83 EC 40                     sub rsp, 0x40
0062C6AD  0F 57 C0                        xorps xmm0, xmm0
0062C6B0  4C 8B E1                        mov r12, rcx
0062C6B3  B9 3D 01 00 00                  mov ecx, 0x13d
0062C6B8  45 8B F0                        mov r14d, r8d
0062C6BB  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062C6BF  4C 8B FA                        mov r15, rdx
0062C6C2  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062C6C6  E8 69 93 E6 FF                  call 0x140495a34
0062C6CB  48 8B F0                        mov rsi, rax
0062C6CE  48 85 C0                        test rax, rax
0062C6D1  0F 84 94 00 00 00               je 0x14062c76b
0062C6D7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062C6DA  A8 18                           test al, 0x18
0062C6DC  74 0C                           je 0x14062c6ea
0062C6DE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062C6E3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062C6E8  EB 0E                           jmp 0x14062c6f8
0062C6EA  A8 04                           test al, 4
0062C6EC  74 0A                           je 0x14062c6f8
0062C6EE  E8 15 75 EA FF                  call 0x1404d3c08
0062C6F3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062C6F8  40 32 ED                        xor bpl, bpl
0062C6FB  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0062C700  40 38 2D B1 81 8D 00            cmp byte ptr [rip + 0x8d81b1], bpl
0062C707  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062C70C  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0062C711  75 0C                           jne 0x14062c71f
0062C713  F7 05 63 82 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8263], 0x800
0062C71D  74 13                           je 0x14062c732
0062C71F  48 8D 0D 5A 77 8D 00            lea rcx, [rip + 0x8d775a]
0062C726  E8 F5 9E BE FF                  call 0x140216620
0062C72B  40 8A E8                        mov bpl, al
0062C72E  84 C0                           test al, al
0062C730  74 39                           je 0x14062c76b
0062C732  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062C736  48 8B 1F                        mov rbx, qword ptr [rdi]
0062C739  EB 1A                           jmp 0x14062c755
0062C73B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C73F  48 85 C0                        test rax, rax
0062C742  74 0E                           je 0x14062c752
0062C744  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C748  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C74D  E8 7E E3 08 00                  call 0x1406baad0
0062C752  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C755  48 3B DF                        cmp rbx, rdi
0062C758  75 E1                           jne 0x14062c73b
0062C75A  40 84 ED                        test bpl, bpl
0062C75D  74 0C                           je 0x14062c76b
0062C75F  48 8D 0D 1A 77 8D 00            lea rcx, [rip + 0x8d771a]
0062C766  E8 15 D7 D1 FF                  call 0x140349e80
0062C76B  45 8B C6                        mov r8d, r14d
0062C76E  49 8B D7                        mov rdx, r15
0062C771  49 8B CC                        mov rcx, r12
0062C774  E8 37 50 E8 FF                  call 0x1404b17b0
0062C779  48 85 F6                        test rsi, rsi
0062C77C  74 64                           je 0x14062c7e2
0062C77E  40 32 FF                        xor dil, dil
0062C781  40 38 3D 30 81 8D 00            cmp byte ptr [rip + 0x8d8130], dil
0062C788  75 0C                           jne 0x14062c796
0062C78A  F7 05 EC 81 8D 00 00 08 00 00   test dword ptr [rip + 0x8d81ec], 0x800
0062C794  74 13                           je 0x14062c7a9
0062C796  48 8D 0D E3 76 8D 00            lea rcx, [rip + 0x8d76e3]
0062C79D  E8 7E 9E BE FF                  call 0x140216620
0062C7A2  40 8A F8                        mov dil, al
0062C7A5  84 C0                           test al, al
0062C7A7  74 39                           je 0x14062c7e2
0062C7A9  48 83 C6 30                     add rsi, 0x30
0062C7AD  48 8B 1E                        mov rbx, qword ptr [rsi]
0062C7B0  EB 1A                           jmp 0x14062c7cc
0062C7B2  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C7B6  48 85 C0                        test rax, rax
0062C7B9  74 0E                           je 0x14062c7c9
0062C7BB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C7BF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C7C4  E8 07 E3 08 00                  call 0x1406baad0
0062C7C9  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C7CC  48 3B DE                        cmp rbx, rsi
0062C7CF  75 E1                           jne 0x14062c7b2
0062C7D1  40 84 FF                        test dil, dil
0062C7D4  74 0C                           je 0x14062c7e2
0062C7D6  48 8D 0D A3 76 8D 00            lea rcx, [rip + 0x8d76a3]
0062C7DD  E8 9E D6 D1 FF                  call 0x140349e80
0062C7E2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062C7E7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062C7EC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062C7F1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062C7F6  48 83 C4 40                     add rsp, 0x40
0062C7FA  41 5F                           pop r15
0062C7FC  41 5E                           pop r14
0062C7FE  41 5C                           pop r12
0062C800  C3                              ret
0062C801  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoReleaseRemoveLockAndWaitExWrapper(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(317, a2, a3, a4);
    if (result == 0) goto loc_0062C76B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062C6EA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C6F8;
loc_0062C6EA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9273777)) != 0) goto loc_0062C71F;
    if (((*(unsigned int *)(v_rip + 9273955)) & (0x800ULL)) == 0) goto loc_0062C732;
loc_0062C71F:
    result = ExAcquireRundownProtection(v_rip + 9271130, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C76B;
loc_0062C732:
    goto loc_0062C755;
loc_0062C73B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C755:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062C73B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9271066;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoReleaseRemoveLockAndWaitEx(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_0062C7E2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9273648)) != 0) goto loc_0062C796;
    if (((*(unsigned int *)(v_rip + 9273836)) & (0x800ULL)) == 0) goto loc_0062C7A9;
loc_0062C796:
    result = ExAcquireRundownProtection(v_rip + 9271011, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C7E2;
loc_0062C7A9:
    v_rsi = (result) + (48);
    goto loc_0062C7CC;
loc_0062C7B2:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0062C7CC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062C7B2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9270947;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoReleaseRemoveLockAndWaitExWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(317, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062C76B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062C6EA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C6F8;
loc_0062C6EA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8D81B1)) != 0) goto loc_0062C71F;
    if (((*(uint32_t *)(v_rip + 0x8D8263)) & (0x800ULL)) == 0) goto loc_0062C732;
loc_0062C71F:
    result = ExAcquireRundownProtection(v_rip + 9271130, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062C76B;
loc_0062C732:
    goto loc_0062C755;
loc_0062C73B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062C755:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062C73B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9271066;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoReleaseRemoveLockAndWaitEx(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (result == 0) goto loc_0062C7E2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D8130)) != 0) goto loc_0062C796;
    if (((*(uint32_t *)(v_rip + 0x8D81EC)) & (0x800ULL)) == 0) goto loc_0062C7A9;
loc_0062C796:
    result = ExAcquireRundownProtection(v_rip + 9271011, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_0062C7E2;
loc_0062C7A9:
    local_rsi = (result) + (48);
    goto loc_0062C7CC;
loc_0062C7B2:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0062C7CC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062C7B2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9270947;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062C690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062C690[BB_0062C690]
  bb_0062C6D7[BB_0062C6D7]
  bb_0062C6DE[BB_0062C6DE]
  bb_0062C6EA[BB_0062C6EA]
  bb_0062C6EE[BB_0062C6EE]
  bb_0062C6F8[BB_0062C6F8]
  bb_0062C713[BB_0062C713]
  bb_0062C71F[BB_0062C71F]
  bb_0062C732[BB_0062C732]
  bb_0062C73B[BB_0062C73B]
  bb_0062C744[BB_0062C744]
  bb_0062C752[BB_0062C752]
  bb_0062C755[BB_0062C755]
  bb_0062C75A[BB_0062C75A]
  bb_0062C75F[BB_0062C75F]
  bb_0062C76B[BB_0062C76B]
  bb_0062C77E[BB_0062C77E]
  bb_0062C78A[BB_0062C78A]
  bb_0062C796[BB_0062C796]
  bb_0062C7A9[BB_0062C7A9]
  bb_0062C7B2[BB_0062C7B2]
  bb_0062C7BB[BB_0062C7BB]
  bb_0062C7C9[BB_0062C7C9]
  bb_0062C7CC[BB_0062C7CC]
  bb_0062C7D1[BB_0062C7D1]
  bb_0062C7D6[BB_0062C7D6]
  bb_0062C7E2[BB_0062C7E2]
  bb_0062C801[BB_0062C801]
  bb_0062C690 -->|branch| bb_0062C76B
  bb_0062C690 -->|fallthrough| bb_0062C6D7
  bb_0062C6D7 -->|branch| bb_0062C6EA
  bb_0062C6D7 -->|fallthrough| bb_0062C6DE
  bb_0062C6DE -->|branch| bb_0062C6F8
  bb_0062C6EA -->|branch| bb_0062C6F8
  bb_0062C6EA -->|fallthrough| bb_0062C6EE
  bb_0062C6EE -->|flow| bb_0062C6F8
  bb_0062C6F8 -->|branch| bb_0062C71F
  bb_0062C6F8 -->|fallthrough| bb_0062C713
  bb_0062C713 -->|branch| bb_0062C732
  bb_0062C713 -->|fallthrough| bb_0062C71F
  bb_0062C71F -->|branch| bb_0062C76B
  bb_0062C71F -->|fallthrough| bb_0062C732
  bb_0062C732 -->|branch| bb_0062C755
  bb_0062C73B -->|branch| bb_0062C752
  bb_0062C73B -->|fallthrough| bb_0062C744
  bb_0062C744 -->|flow| bb_0062C752
  bb_0062C752 -->|flow| bb_0062C755
  bb_0062C755 -->|branch| bb_0062C73B
  bb_0062C755 -->|fallthrough| bb_0062C75A
  bb_0062C75A -->|branch| bb_0062C76B
  bb_0062C75A -->|fallthrough| bb_0062C75F
  bb_0062C75F -->|flow| bb_0062C76B
  bb_0062C76B -->|branch| bb_0062C7E2
  bb_0062C76B -->|fallthrough| bb_0062C77E
  bb_0062C77E -->|branch| bb_0062C796
  bb_0062C77E -->|fallthrough| bb_0062C78A
  bb_0062C78A -->|branch| bb_0062C7A9
  bb_0062C78A -->|fallthrough| bb_0062C796
  bb_0062C796 -->|branch| bb_0062C7E2
  bb_0062C796 -->|fallthrough| bb_0062C7A9
  bb_0062C7A9 -->|branch| bb_0062C7CC
  bb_0062C7B2 -->|branch| bb_0062C7C9
  bb_0062C7B2 -->|fallthrough| bb_0062C7BB
  bb_0062C7BB -->|flow| bb_0062C7C9
  bb_0062C7C9 -->|flow| bb_0062C7CC
  bb_0062C7CC -->|branch| bb_0062C7B2
  bb_0062C7CC -->|fallthrough| bb_0062C7D1
  bb_0062C7D1 -->|branch| bb_0062C7E2
  bb_0062C7D1 -->|fallthrough| bb_0062C7D6
  bb_0062C7D6 -->|flow| bb_0062C7E2
```
