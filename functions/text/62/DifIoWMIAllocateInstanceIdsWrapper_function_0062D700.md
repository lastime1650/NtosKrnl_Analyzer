# DifIoWMIAllocateInstanceIdsWrapper

- RVA: `0x0062D700`–`0x0062D877` (길이 `375` bytes)
- VA: `0x000000014062D700`
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
- `0x0062D73E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062D764` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062D798` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D7BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D7D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062D7E5` → [IoWMIAllocateInstanceIds](../../page/7B/IoWMIAllocateInstanceIds_function_007B1F70.md) (function, `0x007B1F70`)
- `0x0062D811` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D837` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D850` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062D774` → RVA `0x00F048B8` (`.data`; read)
- `0x0062D785` → RVA `0x00F04980` (`.data`; read)
- `0x0062D791` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062D7E5` → [IoWMIAllocateInstanceIds](../../page/7B/IoWMIAllocateInstanceIds_function_007B1F70.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062D700  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0062D705  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0062D70A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0062D70F  55                              push rbp
0062D710  41 54                           push r12
0062D712  41 55                           push r13
0062D714  41 56                           push r14
0062D716  41 57                           push r15
0062D718  48 8B EC                        mov rbp, rsp
0062D71B  48 83 EC 50                     sub rsp, 0x50
0062D71F  0F 57 C0                        xorps xmm0, xmm0
0062D722  33 C0                           xor eax, eax
0062D724  4C 8B E9                        mov r13, rcx
0062D727  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0062D72B  B9 32 01 00 00                  mov ecx, 0x132
0062D730  4D 8B F8                        mov r15, r8
0062D733  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062D737  44 8B E2                        mov r12d, edx
0062D73A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062D73E  E8 F1 82 E6 FF                  call 0x140495a34
0062D743  48 8B F0                        mov rsi, rax
0062D746  48 85 C0                        test rax, rax
0062D749  0F 84 8D 00 00 00               je 0x14062d7dc
0062D74F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062D752  A8 18                           test al, 0x18
0062D754  74 0A                           je 0x14062d760
0062D756  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062D75A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0062D75E  EB 0D                           jmp 0x14062d76d
0062D760  A8 04                           test al, 4
0062D762  74 09                           je 0x14062d76d
0062D764  E8 9F 64 EA FF                  call 0x1404d3c08
0062D769  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062D76D  45 32 F6                        xor r14b, r14b
0062D770  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0062D774  44 38 35 3D 71 8D 00            cmp byte ptr [rip + 0x8d713d], r14b
0062D77B  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0062D77F  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0062D783  75 0C                           jne 0x14062d791
0062D785  F7 05 F1 71 8D 00 00 08 00 00   test dword ptr [rip + 0x8d71f1], 0x800
0062D78F  74 13                           je 0x14062d7a4
0062D791  48 8D 0D E8 66 8D 00            lea rcx, [rip + 0x8d66e8]
0062D798  E8 83 8E BE FF                  call 0x140216620
0062D79D  44 8A F0                        mov r14b, al
0062D7A0  84 C0                           test al, al
0062D7A2  74 38                           je 0x14062d7dc
0062D7A4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062D7A8  48 8B 1F                        mov rbx, qword ptr [rdi]
0062D7AB  EB 19                           jmp 0x14062d7c6
0062D7AD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D7B1  48 85 C0                        test rax, rax
0062D7B4  74 0D                           je 0x14062d7c3
0062D7B6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D7BA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062D7BE  E8 0D D3 08 00                  call 0x1406baad0
0062D7C3  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D7C6  48 3B DF                        cmp rbx, rdi
0062D7C9  75 E2                           jne 0x14062d7ad
0062D7CB  45 84 F6                        test r14b, r14b
0062D7CE  74 0C                           je 0x14062d7dc
0062D7D0  48 8D 0D A9 66 8D 00            lea rcx, [rip + 0x8d66a9]
0062D7D7  E8 A4 C6 D1 FF                  call 0x140349e80
0062D7DC  4D 8B C7                        mov r8, r15
0062D7DF  41 8B D4                        mov edx, r12d
0062D7E2  49 8B CD                        mov rcx, r13
0062D7E5  E8 86 47 18 00                  call 0x1407b1f70
0062D7EA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0062D7ED  48 85 F6                        test rsi, rsi
0062D7F0  74 63                           je 0x14062d855
0062D7F2  40 32 FF                        xor dil, dil
0062D7F5  40 38 3D BC 70 8D 00            cmp byte ptr [rip + 0x8d70bc], dil
0062D7FC  75 0C                           jne 0x14062d80a
0062D7FE  F7 05 78 71 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7178], 0x800
0062D808  74 13                           je 0x14062d81d
0062D80A  48 8D 0D 6F 66 8D 00            lea rcx, [rip + 0x8d666f]
0062D811  E8 0A 8E BE FF                  call 0x140216620
0062D816  40 8A F8                        mov dil, al
0062D819  84 C0                           test al, al
0062D81B  74 38                           je 0x14062d855
0062D81D  48 83 C6 30                     add rsi, 0x30
0062D821  48 8B 1E                        mov rbx, qword ptr [rsi]
0062D824  EB 19                           jmp 0x14062d83f
0062D826  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D82A  48 85 C0                        test rax, rax
0062D82D  74 0D                           je 0x14062d83c
0062D82F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D833  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062D837  E8 94 D2 08 00                  call 0x1406baad0
0062D83C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D83F  48 3B DE                        cmp rbx, rsi
0062D842  75 E2                           jne 0x14062d826
0062D844  40 84 FF                        test dil, dil
0062D847  74 0C                           je 0x14062d855
0062D849  48 8D 0D 30 66 8D 00            lea rcx, [rip + 0x8d6630]
0062D850  E8 2B C6 D1 FF                  call 0x140349e80
0062D855  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0062D858  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0062D85D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0062D861  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0062D865  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0062D869  49 8B E3                        mov rsp, r11
0062D86C  41 5F                           pop r15
0062D86E  41 5E                           pop r14
0062D870  41 5D                           pop r13
0062D872  41 5C                           pop r12
0062D874  5D                              pop rbp
0062D875  C3                              ret
0062D876  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoWMIAllocateInstanceIdsWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(306, a2, a3, a4);
    if (result == 0) goto loc_0062D7DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062D760;
    v_stack_m58 = v_stack_p0;
    goto loc_0062D76D;
loc_0062D760:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9269565)) != 0) goto loc_0062D791;
    if (((*(unsigned int *)(v_rip + 9269745)) & (0x800ULL)) == 0) goto loc_0062D7A4;
loc_0062D791:
    result = ExAcquireRundownProtection(v_rip + 9266920, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D7DC;
loc_0062D7A4:
    goto loc_0062D7C6;
loc_0062D7AD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062D7C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062D7AD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9266857;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoWMIAllocateInstanceIds(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0062D855;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9269436)) != 0) goto loc_0062D80A;
    if (((*(unsigned int *)(v_rip + 9269624)) & (0x800ULL)) == 0) goto loc_0062D81D;
loc_0062D80A:
    result = ExAcquireRundownProtection(v_rip + 9266799, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D855;
loc_0062D81D:
    v_rsi = (result) + (48);
    goto loc_0062D83F;
loc_0062D826:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062D83F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062D826;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9266736;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoWMIAllocateInstanceIdsWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(306, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062D7DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062D760;
    v_stack_m58 = v_stack_p0;
    goto loc_0062D76D;
loc_0062D760:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D713D)) != 0) goto loc_0062D791;
    if (((*(uint32_t *)(v_rip + 0x8D71F1)) & (0x800ULL)) == 0) goto loc_0062D7A4;
loc_0062D791:
    result = ExAcquireRundownProtection(v_rip + 9266920, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062D7DC;
loc_0062D7A4:
    goto loc_0062D7C6;
loc_0062D7AD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062D7C6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062D7AD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9266857;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoWMIAllocateInstanceIds(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0062D855;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D70BC)) != 0) goto loc_0062D80A;
    if (((*(uint32_t *)(v_rip + 0x8D7178)) & (0x800ULL)) == 0) goto loc_0062D81D;
loc_0062D80A:
    result = ExAcquireRundownProtection(v_rip + 9266799, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062D855;
loc_0062D81D:
    local_rsi = (result) + (48);
    goto loc_0062D83F;
loc_0062D826:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0062D83F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062D826;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9266736;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062D700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062D700[BB_0062D700]
  bb_0062D74F[BB_0062D74F]
  bb_0062D756[BB_0062D756]
  bb_0062D760[BB_0062D760]
  bb_0062D764[BB_0062D764]
  bb_0062D76D[BB_0062D76D]
  bb_0062D785[BB_0062D785]
  bb_0062D791[BB_0062D791]
  bb_0062D7A4[BB_0062D7A4]
  bb_0062D7AD[BB_0062D7AD]
  bb_0062D7B6[BB_0062D7B6]
  bb_0062D7C3[BB_0062D7C3]
  bb_0062D7C6[BB_0062D7C6]
  bb_0062D7CB[BB_0062D7CB]
  bb_0062D7D0[BB_0062D7D0]
  bb_0062D7DC[BB_0062D7DC]
  bb_0062D7F2[BB_0062D7F2]
  bb_0062D7FE[BB_0062D7FE]
  bb_0062D80A[BB_0062D80A]
  bb_0062D81D[BB_0062D81D]
  bb_0062D826[BB_0062D826]
  bb_0062D82F[BB_0062D82F]
  bb_0062D83C[BB_0062D83C]
  bb_0062D83F[BB_0062D83F]
  bb_0062D844[BB_0062D844]
  bb_0062D849[BB_0062D849]
  bb_0062D855[BB_0062D855]
  bb_0062D876[BB_0062D876]
  bb_0062D700 -->|branch| bb_0062D7DC
  bb_0062D700 -->|fallthrough| bb_0062D74F
  bb_0062D74F -->|branch| bb_0062D760
  bb_0062D74F -->|fallthrough| bb_0062D756
  bb_0062D756 -->|branch| bb_0062D76D
  bb_0062D760 -->|branch| bb_0062D76D
  bb_0062D760 -->|fallthrough| bb_0062D764
  bb_0062D764 -->|flow| bb_0062D76D
  bb_0062D76D -->|branch| bb_0062D791
  bb_0062D76D -->|fallthrough| bb_0062D785
  bb_0062D785 -->|branch| bb_0062D7A4
  bb_0062D785 -->|fallthrough| bb_0062D791
  bb_0062D791 -->|branch| bb_0062D7DC
  bb_0062D791 -->|fallthrough| bb_0062D7A4
  bb_0062D7A4 -->|branch| bb_0062D7C6
  bb_0062D7AD -->|branch| bb_0062D7C3
  bb_0062D7AD -->|fallthrough| bb_0062D7B6
  bb_0062D7B6 -->|flow| bb_0062D7C3
  bb_0062D7C3 -->|flow| bb_0062D7C6
  bb_0062D7C6 -->|branch| bb_0062D7AD
  bb_0062D7C6 -->|fallthrough| bb_0062D7CB
  bb_0062D7CB -->|branch| bb_0062D7DC
  bb_0062D7CB -->|fallthrough| bb_0062D7D0
  bb_0062D7D0 -->|flow| bb_0062D7DC
  bb_0062D7DC -->|branch| bb_0062D855
  bb_0062D7DC -->|fallthrough| bb_0062D7F2
  bb_0062D7F2 -->|branch| bb_0062D80A
  bb_0062D7F2 -->|fallthrough| bb_0062D7FE
  bb_0062D7FE -->|branch| bb_0062D81D
  bb_0062D7FE -->|fallthrough| bb_0062D80A
  bb_0062D80A -->|branch| bb_0062D855
  bb_0062D80A -->|fallthrough| bb_0062D81D
  bb_0062D81D -->|branch| bb_0062D83F
  bb_0062D826 -->|branch| bb_0062D83C
  bb_0062D826 -->|fallthrough| bb_0062D82F
  bb_0062D82F -->|flow| bb_0062D83C
  bb_0062D83C -->|flow| bb_0062D83F
  bb_0062D83F -->|branch| bb_0062D826
  bb_0062D83F -->|fallthrough| bb_0062D844
  bb_0062D844 -->|branch| bb_0062D855
  bb_0062D844 -->|fallthrough| bb_0062D849
  bb_0062D849 -->|flow| bb_0062D855
```
