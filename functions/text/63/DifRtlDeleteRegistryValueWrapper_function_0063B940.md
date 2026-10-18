# DifRtlDeleteRegistryValueWrapper

- RVA: `0x0063B940`–`0x0063BABA` (길이 `378` bytes)
- VA: `0x000000014063B940`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `103`개 명령, `378/378` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063B976` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063B99E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063B9D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063B9FD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BA16` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063BA24` → [RtlDeleteRegistryValue](../../page/AD/RtlDeleteRegistryValue_function_00ADA1B0.md) (function, `0x00ADA1B0`)
- `0x0063BA51` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063BA78` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BA91` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063B9B0` → RVA `0x00F048B8` (`.data`; read)
- `0x0063B9C3` → RVA `0x00F04980` (`.data`; read)
- `0x0063B9CF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063BA24` → [RtlDeleteRegistryValue](../../page/AD/RtlDeleteRegistryValue_function_00ADA1B0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063B940  48 8B C4                        mov rax, rsp
0063B943  48 89 58 08                     mov qword ptr [rax + 8], rbx
0063B947  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063B94B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063B94F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063B953  41 54                           push r12
0063B955  41 56                           push r14
0063B957  41 57                           push r15
0063B959  48 83 EC 40                     sub rsp, 0x40
0063B95D  0F 57 C0                        xorps xmm0, xmm0
0063B960  44 8B E1                        mov r12d, ecx
0063B963  B9 A4 00 00 00                  mov ecx, 0xa4
0063B968  4D 8B F0                        mov r14, r8
0063B96B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063B96F  4C 8B FA                        mov r15, rdx
0063B972  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063B976  E8 B9 A0 E5 FF                  call 0x140495a34
0063B97B  48 8B F0                        mov rsi, rax
0063B97E  48 85 C0                        test rax, rax
0063B981  0F 84 94 00 00 00               je 0x14063ba1b
0063B987  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063B98A  A8 18                           test al, 0x18
0063B98C  74 0C                           je 0x14063b99a
0063B98E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063B993  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063B998  EB 0E                           jmp 0x14063b9a8
0063B99A  A8 04                           test al, 4
0063B99C  74 0A                           je 0x14063b9a8
0063B99E  E8 65 82 E9 FF                  call 0x1404d3c08
0063B9A3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063B9A8  40 32 ED                        xor bpl, bpl
0063B9AB  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0063B9B0  40 38 2D 01 8F 8C 00            cmp byte ptr [rip + 0x8c8f01], bpl
0063B9B7  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0063B9BC  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0063B9C1  75 0C                           jne 0x14063b9cf
0063B9C3  F7 05 B3 8F 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8fb3], 0x800
0063B9CD  74 13                           je 0x14063b9e2
0063B9CF  48 8D 0D AA 84 8C 00            lea rcx, [rip + 0x8c84aa]
0063B9D6  E8 45 AC BD FF                  call 0x140216620
0063B9DB  40 8A E8                        mov bpl, al
0063B9DE  84 C0                           test al, al
0063B9E0  74 39                           je 0x14063ba1b
0063B9E2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063B9E6  48 8B 1F                        mov rbx, qword ptr [rdi]
0063B9E9  EB 1A                           jmp 0x14063ba05
0063B9EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063B9EF  48 85 C0                        test rax, rax
0063B9F2  74 0E                           je 0x14063ba02
0063B9F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063B9F8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063B9FD  E8 CE F0 07 00                  call 0x1406baad0
0063BA02  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BA05  48 3B DF                        cmp rbx, rdi
0063BA08  75 E1                           jne 0x14063b9eb
0063BA0A  40 84 ED                        test bpl, bpl
0063BA0D  74 0C                           je 0x14063ba1b
0063BA0F  48 8D 0D 6A 84 8C 00            lea rcx, [rip + 0x8c846a]
0063BA16  E8 65 E4 D0 FF                  call 0x140349e80
0063BA1B  4D 8B C6                        mov r8, r14
0063BA1E  49 8B D7                        mov rdx, r15
0063BA21  41 8B CC                        mov ecx, r12d
0063BA24  E8 87 E7 49 00                  call 0x140ada1b0
0063BA29  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0063BA2D  48 85 F6                        test rsi, rsi
0063BA30  74 64                           je 0x14063ba96
0063BA32  40 32 FF                        xor dil, dil
0063BA35  40 38 3D 7C 8E 8C 00            cmp byte ptr [rip + 0x8c8e7c], dil
0063BA3C  75 0C                           jne 0x14063ba4a
0063BA3E  F7 05 38 8F 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8f38], 0x800
0063BA48  74 13                           je 0x14063ba5d
0063BA4A  48 8D 0D 2F 84 8C 00            lea rcx, [rip + 0x8c842f]
0063BA51  E8 CA AB BD FF                  call 0x140216620
0063BA56  40 8A F8                        mov dil, al
0063BA59  84 C0                           test al, al
0063BA5B  74 39                           je 0x14063ba96
0063BA5D  48 83 C6 30                     add rsi, 0x30
0063BA61  48 8B 1E                        mov rbx, qword ptr [rsi]
0063BA64  EB 1A                           jmp 0x14063ba80
0063BA66  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063BA6A  48 85 C0                        test rax, rax
0063BA6D  74 0E                           je 0x14063ba7d
0063BA6F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063BA73  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063BA78  E8 53 F0 07 00                  call 0x1406baad0
0063BA7D  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BA80  48 3B DE                        cmp rbx, rsi
0063BA83  75 E1                           jne 0x14063ba66
0063BA85  40 84 FF                        test dil, dil
0063BA88  74 0C                           je 0x14063ba96
0063BA8A  48 8D 0D EF 83 8C 00            lea rcx, [rip + 0x8c83ef]
0063BA91  E8 EA E3 D0 FF                  call 0x140349e80
0063BA96  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
0063BA9A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0063BA9F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0063BAA4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063BAA9  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0063BAAE  48 83 C4 40                     add rsp, 0x40
0063BAB2  41 5F                           pop r15
0063BAB4  41 5E                           pop r14
0063BAB6  41 5C                           pop r12
0063BAB8  C3                              ret
0063BAB9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlDeleteRegistryValueWrapper(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
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
    result = DifGetAPIThunkContextById(164, a2, a3, a4);
    if (result == 0) goto loc_0063BA1B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063B99A;
    v_stack_m38 = v_stack_p0;
    goto loc_0063B9A8;
loc_0063B99A:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = (unsigned int)((unsigned int)(a1));
    v_stack_m28 = a2;
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9211649)) != 0) goto loc_0063B9CF;
    if (((*(unsigned int *)(v_rip + 9211827)) & (0x800ULL)) == 0) goto loc_0063B9E2;
loc_0063B9CF:
    result = ExAcquireRundownProtection(v_rip + 9209002, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BA1B;
loc_0063B9E2:
    goto loc_0063BA05;
loc_0063B9EB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BA05:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063B9EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9208938;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlDeleteRegistryValue((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    v_stack_m1C = (unsigned int)(result);
    if (result == 0) goto loc_0063BA96;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9211516)) != 0) goto loc_0063BA4A;
    if (((*(unsigned int *)(v_rip + 9211704)) & (0x800ULL)) == 0) goto loc_0063BA5D;
loc_0063BA4A:
    result = ExAcquireRundownProtection(v_rip + 9208879, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BA96;
loc_0063BA5D:
    v_rsi = (result) + (48);
    goto loc_0063BA80;
loc_0063BA66:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BA80:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063BA66;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9208815;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m1C);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlDeleteRegistryValueWrapper(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(164, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063BA1B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063B99A;
    v_stack_m38 = v_stack_p0;
    goto loc_0063B9A8;
loc_0063B99A:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m28 = Arg2;
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C8F01)) != 0) goto loc_0063B9CF;
    if (((*(uint32_t *)(v_rip + 0x8C8FB3)) & (0x800ULL)) == 0) goto loc_0063B9E2;
loc_0063B9CF:
    result = ExAcquireRundownProtection(v_rip + 9209002, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BA1B;
loc_0063B9E2:
    goto loc_0063BA05;
loc_0063B9EB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BA05:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063B9EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9208938;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlDeleteRegistryValue((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, a4);
    v_stack_m1C = (uint32_t)(result);
    if (result == 0) goto loc_0063BA96;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C8E7C)) != 0) goto loc_0063BA4A;
    if (((*(uint32_t *)(v_rip + 0x8C8F38)) & (0x800ULL)) == 0) goto loc_0063BA5D;
loc_0063BA4A:
    result = ExAcquireRundownProtection(v_rip + 9208879, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BA96;
loc_0063BA5D:
    local_rsi = (result) + (48);
    goto loc_0063BA80;
loc_0063BA66:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BA80:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063BA66;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9208815;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m1C);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063B940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063B940[BB_0063B940]
  bb_0063B987[BB_0063B987]
  bb_0063B98E[BB_0063B98E]
  bb_0063B99A[BB_0063B99A]
  bb_0063B99E[BB_0063B99E]
  bb_0063B9A8[BB_0063B9A8]
  bb_0063B9C3[BB_0063B9C3]
  bb_0063B9CF[BB_0063B9CF]
  bb_0063B9E2[BB_0063B9E2]
  bb_0063B9EB[BB_0063B9EB]
  bb_0063B9F4[BB_0063B9F4]
  bb_0063BA02[BB_0063BA02]
  bb_0063BA05[BB_0063BA05]
  bb_0063BA0A[BB_0063BA0A]
  bb_0063BA0F[BB_0063BA0F]
  bb_0063BA1B[BB_0063BA1B]
  bb_0063BA32[BB_0063BA32]
  bb_0063BA3E[BB_0063BA3E]
  bb_0063BA4A[BB_0063BA4A]
  bb_0063BA5D[BB_0063BA5D]
  bb_0063BA66[BB_0063BA66]
  bb_0063BA6F[BB_0063BA6F]
  bb_0063BA7D[BB_0063BA7D]
  bb_0063BA80[BB_0063BA80]
  bb_0063BA85[BB_0063BA85]
  bb_0063BA8A[BB_0063BA8A]
  bb_0063BA96[BB_0063BA96]
  bb_0063BAB9[BB_0063BAB9]
  bb_0063B940 -->|branch| bb_0063BA1B
  bb_0063B940 -->|fallthrough| bb_0063B987
  bb_0063B987 -->|branch| bb_0063B99A
  bb_0063B987 -->|fallthrough| bb_0063B98E
  bb_0063B98E -->|branch| bb_0063B9A8
  bb_0063B99A -->|branch| bb_0063B9A8
  bb_0063B99A -->|fallthrough| bb_0063B99E
  bb_0063B99E -->|flow| bb_0063B9A8
  bb_0063B9A8 -->|branch| bb_0063B9CF
  bb_0063B9A8 -->|fallthrough| bb_0063B9C3
  bb_0063B9C3 -->|branch| bb_0063B9E2
  bb_0063B9C3 -->|fallthrough| bb_0063B9CF
  bb_0063B9CF -->|branch| bb_0063BA1B
  bb_0063B9CF -->|fallthrough| bb_0063B9E2
  bb_0063B9E2 -->|branch| bb_0063BA05
  bb_0063B9EB -->|branch| bb_0063BA02
  bb_0063B9EB -->|fallthrough| bb_0063B9F4
  bb_0063B9F4 -->|flow| bb_0063BA02
  bb_0063BA02 -->|flow| bb_0063BA05
  bb_0063BA05 -->|branch| bb_0063B9EB
  bb_0063BA05 -->|fallthrough| bb_0063BA0A
  bb_0063BA0A -->|branch| bb_0063BA1B
  bb_0063BA0A -->|fallthrough| bb_0063BA0F
  bb_0063BA0F -->|flow| bb_0063BA1B
  bb_0063BA1B -->|branch| bb_0063BA96
  bb_0063BA1B -->|fallthrough| bb_0063BA32
  bb_0063BA32 -->|branch| bb_0063BA4A
  bb_0063BA32 -->|fallthrough| bb_0063BA3E
  bb_0063BA3E -->|branch| bb_0063BA5D
  bb_0063BA3E -->|fallthrough| bb_0063BA4A
  bb_0063BA4A -->|branch| bb_0063BA96
  bb_0063BA4A -->|fallthrough| bb_0063BA5D
  bb_0063BA5D -->|branch| bb_0063BA80
  bb_0063BA66 -->|branch| bb_0063BA7D
  bb_0063BA66 -->|fallthrough| bb_0063BA6F
  bb_0063BA6F -->|flow| bb_0063BA7D
  bb_0063BA7D -->|flow| bb_0063BA80
  bb_0063BA80 -->|branch| bb_0063BA66
  bb_0063BA80 -->|fallthrough| bb_0063BA85
  bb_0063BA85 -->|branch| bb_0063BA96
  bb_0063BA85 -->|fallthrough| bb_0063BA8A
  bb_0063BA8A -->|flow| bb_0063BA96
```
