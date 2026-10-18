# DifMmAllocateMappingAddressExWrapper

- RVA: `0x00634260`–`0x006343DC` (길이 `380` bytes)
- VA: `0x0000000140634260`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `103`개 명령, `380/380` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00634296` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006342BE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006342F6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063431D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634336` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00634344` → [MmAllocateMappingAddressEx](../../page/A7/MmAllocateMappingAddressEx_function_00A726B0.md) (function, `0x00A726B0`)
- `0x00634372` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634399` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006343B2` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006342D0` → RVA `0x00F048B8` (`.data`; read)
- `0x006342E3` → RVA `0x00F04980` (`.data`; read)
- `0x006342EF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00634344` → [MmAllocateMappingAddressEx](../../page/A7/MmAllocateMappingAddressEx_function_00A726B0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00634260  48 8B C4                        mov rax, rsp
00634263  48 89 58 08                     mov qword ptr [rax + 8], rbx
00634267  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063426B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063426F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00634273  41 54                           push r12
00634275  41 56                           push r14
00634277  41 57                           push r15
00634279  48 83 EC 40                     sub rsp, 0x40
0063427D  0F 57 C0                        xorps xmm0, xmm0
00634280  4C 8B E1                        mov r12, rcx
00634283  B9 D1 01 00 00                  mov ecx, 0x1d1
00634288  45 8B F0                        mov r14d, r8d
0063428B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063428F  44 8B FA                        mov r15d, edx
00634292  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00634296  E8 99 17 E6 FF                  call 0x140495a34
0063429B  48 8B F0                        mov rsi, rax
0063429E  48 85 C0                        test rax, rax
006342A1  0F 84 94 00 00 00               je 0x14063433b
006342A7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006342AA  A8 18                           test al, 0x18
006342AC  74 0C                           je 0x1406342ba
006342AE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006342B3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006342B8  EB 0E                           jmp 0x1406342c8
006342BA  A8 04                           test al, 4
006342BC  74 0A                           je 0x1406342c8
006342BE  E8 45 F9 E9 FF                  call 0x1404d3c08
006342C3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006342C8  40 32 ED                        xor bpl, bpl
006342CB  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
006342D0  40 38 2D E1 05 8D 00            cmp byte ptr [rip + 0x8d05e1], bpl
006342D7  44 89 7C 24 2C                  mov dword ptr [rsp + 0x2c], r15d
006342DC  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
006342E1  75 0C                           jne 0x1406342ef
006342E3  F7 05 93 06 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0693], 0x800
006342ED  74 13                           je 0x140634302
006342EF  48 8D 0D 8A FB 8C 00            lea rcx, [rip + 0x8cfb8a]
006342F6  E8 25 23 BE FF                  call 0x140216620
006342FB  40 8A E8                        mov bpl, al
006342FE  84 C0                           test al, al
00634300  74 39                           je 0x14063433b
00634302  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00634306  48 8B 1F                        mov rbx, qword ptr [rdi]
00634309  EB 1A                           jmp 0x140634325
0063430B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063430F  48 85 C0                        test rax, rax
00634312  74 0E                           je 0x140634322
00634314  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634318  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063431D  E8 AE 67 08 00                  call 0x1406baad0
00634322  48 8B 1B                        mov rbx, qword ptr [rbx]
00634325  48 3B DF                        cmp rbx, rdi
00634328  75 E1                           jne 0x14063430b
0063432A  40 84 ED                        test bpl, bpl
0063432D  74 0C                           je 0x14063433b
0063432F  48 8D 0D 4A FB 8C 00            lea rcx, [rip + 0x8cfb4a]
00634336  E8 45 5B D1 FF                  call 0x140349e80
0063433B  45 8B C6                        mov r8d, r14d
0063433E  41 8B D7                        mov edx, r15d
00634341  49 8B CC                        mov rcx, r12
00634344  E8 67 E3 43 00                  call 0x140a726b0
00634349  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0063434E  48 85 F6                        test rsi, rsi
00634351  74 64                           je 0x1406343b7
00634353  40 32 FF                        xor dil, dil
00634356  40 38 3D 5B 05 8D 00            cmp byte ptr [rip + 0x8d055b], dil
0063435D  75 0C                           jne 0x14063436b
0063435F  F7 05 17 06 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0617], 0x800
00634369  74 13                           je 0x14063437e
0063436B  48 8D 0D 0E FB 8C 00            lea rcx, [rip + 0x8cfb0e]
00634372  E8 A9 22 BE FF                  call 0x140216620
00634377  40 8A F8                        mov dil, al
0063437A  84 C0                           test al, al
0063437C  74 39                           je 0x1406343b7
0063437E  48 83 C6 30                     add rsi, 0x30
00634382  48 8B 1E                        mov rbx, qword ptr [rsi]
00634385  EB 1A                           jmp 0x1406343a1
00634387  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063438B  48 85 C0                        test rax, rax
0063438E  74 0E                           je 0x14063439e
00634390  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634394  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00634399  E8 32 67 08 00                  call 0x1406baad0
0063439E  48 8B 1B                        mov rbx, qword ptr [rbx]
006343A1  48 3B DE                        cmp rbx, rsi
006343A4  75 E1                           jne 0x140634387
006343A6  40 84 FF                        test dil, dil
006343A9  74 0C                           je 0x1406343b7
006343AB  48 8D 0D CE FA 8C 00            lea rcx, [rip + 0x8cface]
006343B2  E8 C9 5A D1 FF                  call 0x140349e80
006343B7  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
006343BC  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006343C1  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006343C6  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006343CB  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
006343D0  48 83 C4 40                     add rsp, 0x40
006343D4  41 5F                           pop r15
006343D6  41 5E                           pop r14
006343D8  41 5C                           pop r12
006343DA  C3                              ret
006343DB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocateMappingAddressExWrapper(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
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
    result = DifGetAPIThunkContextById(465, a2, a3, a4);
    if (result == 0) goto loc_0063433B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006342BA;
    v_stack_m38 = v_stack_p0;
    goto loc_006342C8;
loc_006342BA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m2C = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9242081)) != 0) goto loc_006342EF;
    if (((*(unsigned int *)(v_rip + 9242259)) & (0x800ULL)) == 0) goto loc_00634302;
loc_006342EF:
    result = ExAcquireRundownProtection(v_rip + 9239434, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063433B;
loc_00634302:
    goto loc_00634325;
loc_0063430B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00634325:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063430B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9239370;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmAllocateMappingAddressEx(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_006343B7;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9241947)) != 0) goto loc_0063436B;
    if (((*(unsigned int *)(v_rip + 9242135)) & (0x800ULL)) == 0) goto loc_0063437E;
loc_0063436B:
    result = ExAcquireRundownProtection(v_rip + 9239310, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_006343B7;
loc_0063437E:
    v_rsi = (result) + (48);
    goto loc_006343A1;
loc_00634387:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_006343A1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00634387;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9239246;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocateMappingAddressExWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
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
    result = DifGetAPIThunkContextById(465, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063433B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006342BA;
    v_stack_m38 = v_stack_p0;
    goto loc_006342C8;
loc_006342BA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8D05E1)) != 0) goto loc_006342EF;
    if (((*(uint32_t *)(v_rip + 0x8D0693)) & (0x800ULL)) == 0) goto loc_00634302;
loc_006342EF:
    result = ExAcquireRundownProtection(v_rip + 9239434, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063433B;
loc_00634302:
    goto loc_00634325;
loc_0063430B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00634325:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063430B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9239370;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = MmAllocateMappingAddressEx(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_006343B7;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D055B)) != 0) goto loc_0063436B;
    if (((*(uint32_t *)(v_rip + 0x8D0617)) & (0x800ULL)) == 0) goto loc_0063437E;
loc_0063436B:
    result = ExAcquireRundownProtection(v_rip + 9239310, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_006343B7;
loc_0063437E:
    local_rsi = (result) + (48);
    goto loc_006343A1;
loc_00634387:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_006343A1:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00634387;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9239246;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00634260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00634260[BB_00634260]
  bb_006342A7[BB_006342A7]
  bb_006342AE[BB_006342AE]
  bb_006342BA[BB_006342BA]
  bb_006342BE[BB_006342BE]
  bb_006342C8[BB_006342C8]
  bb_006342E3[BB_006342E3]
  bb_006342EF[BB_006342EF]
  bb_00634302[BB_00634302]
  bb_0063430B[BB_0063430B]
  bb_00634314[BB_00634314]
  bb_00634322[BB_00634322]
  bb_00634325[BB_00634325]
  bb_0063432A[BB_0063432A]
  bb_0063432F[BB_0063432F]
  bb_0063433B[BB_0063433B]
  bb_00634353[BB_00634353]
  bb_0063435F[BB_0063435F]
  bb_0063436B[BB_0063436B]
  bb_0063437E[BB_0063437E]
  bb_00634387[BB_00634387]
  bb_00634390[BB_00634390]
  bb_0063439E[BB_0063439E]
  bb_006343A1[BB_006343A1]
  bb_006343A6[BB_006343A6]
  bb_006343AB[BB_006343AB]
  bb_006343B7[BB_006343B7]
  bb_006343DB[BB_006343DB]
  bb_00634260 -->|branch| bb_0063433B
  bb_00634260 -->|fallthrough| bb_006342A7
  bb_006342A7 -->|branch| bb_006342BA
  bb_006342A7 -->|fallthrough| bb_006342AE
  bb_006342AE -->|branch| bb_006342C8
  bb_006342BA -->|branch| bb_006342C8
  bb_006342BA -->|fallthrough| bb_006342BE
  bb_006342BE -->|flow| bb_006342C8
  bb_006342C8 -->|branch| bb_006342EF
  bb_006342C8 -->|fallthrough| bb_006342E3
  bb_006342E3 -->|branch| bb_00634302
  bb_006342E3 -->|fallthrough| bb_006342EF
  bb_006342EF -->|branch| bb_0063433B
  bb_006342EF -->|fallthrough| bb_00634302
  bb_00634302 -->|branch| bb_00634325
  bb_0063430B -->|branch| bb_00634322
  bb_0063430B -->|fallthrough| bb_00634314
  bb_00634314 -->|flow| bb_00634322
  bb_00634322 -->|flow| bb_00634325
  bb_00634325 -->|branch| bb_0063430B
  bb_00634325 -->|fallthrough| bb_0063432A
  bb_0063432A -->|branch| bb_0063433B
  bb_0063432A -->|fallthrough| bb_0063432F
  bb_0063432F -->|flow| bb_0063433B
  bb_0063433B -->|branch| bb_006343B7
  bb_0063433B -->|fallthrough| bb_00634353
  bb_00634353 -->|branch| bb_0063436B
  bb_00634353 -->|fallthrough| bb_0063435F
  bb_0063435F -->|branch| bb_0063437E
  bb_0063435F -->|fallthrough| bb_0063436B
  bb_0063436B -->|branch| bb_006343B7
  bb_0063436B -->|fallthrough| bb_0063437E
  bb_0063437E -->|branch| bb_006343A1
  bb_00634387 -->|branch| bb_0063439E
  bb_00634387 -->|fallthrough| bb_00634390
  bb_00634390 -->|flow| bb_0063439E
  bb_0063439E -->|flow| bb_006343A1
  bb_006343A1 -->|branch| bb_00634387
  bb_006343A1 -->|fallthrough| bb_006343A6
  bb_006343A6 -->|branch| bb_006343B7
  bb_006343A6 -->|fallthrough| bb_006343AB
  bb_006343AB -->|flow| bb_006343B7
```
