# DifMmAllocateMappingAddressWrapper

- RVA: `0x006343F0`–`0x00634556` (길이 `358` bytes)
- VA: `0x00000001406343F0`
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
- `0x0063441E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00634446` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00634479` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006344A0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006344B9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006344C4` → [MmAllocateMappingAddress](../../page/A7/MmAllocateMappingAddress_function_00A72690.md) (function, `0x00A72690`)
- `0x006344F2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634519` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634532` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00634458` → RVA `0x00F048B8` (`.data`; read)
- `0x00634466` → RVA `0x00F04980` (`.data`; read)
- `0x00634472` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006344C4` → [MmAllocateMappingAddress](../../page/A7/MmAllocateMappingAddress_function_00A72690.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006343F0  48 8B C4                        mov rax, rsp
006343F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006343F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006343FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006343FF  57                              push rdi
00634400  41 56                           push r14
00634402  41 57                           push r15
00634404  48 83 EC 40                     sub rsp, 0x40
00634408  0F 57 C0                        xorps xmm0, xmm0
0063440B  4C 8B F9                        mov r15, rcx
0063440E  B9 E9 00 00 00                  mov ecx, 0xe9
00634413  44 8B F2                        mov r14d, edx
00634416  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0063441A  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0063441E  E8 11 16 E6 FF                  call 0x140495a34
00634423  48 8B F0                        mov rsi, rax
00634426  48 85 C0                        test rax, rax
00634429  0F 84 8F 00 00 00               je 0x1406344be
0063442F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00634432  A8 18                           test al, 0x18
00634434  74 0C                           je 0x140634442
00634436  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063443B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00634440  EB 0E                           jmp 0x140634450
00634442  A8 04                           test al, 4
00634444  74 0A                           je 0x140634450
00634446  E8 BD F7 E9 FF                  call 0x1404d3c08
0063444B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00634450  40 32 ED                        xor bpl, bpl
00634453  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00634458  40 38 2D 59 04 8D 00            cmp byte ptr [rip + 0x8d0459], bpl
0063445F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00634464  75 0C                           jne 0x140634472
00634466  F7 05 10 05 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0510], 0x800
00634470  74 13                           je 0x140634485
00634472  48 8D 0D 07 FA 8C 00            lea rcx, [rip + 0x8cfa07]
00634479  E8 A2 21 BE FF                  call 0x140216620
0063447E  40 8A E8                        mov bpl, al
00634481  84 C0                           test al, al
00634483  74 39                           je 0x1406344be
00634485  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00634489  48 8B 1F                        mov rbx, qword ptr [rdi]
0063448C  EB 1A                           jmp 0x1406344a8
0063448E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00634492  48 85 C0                        test rax, rax
00634495  74 0E                           je 0x1406344a5
00634497  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063449B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006344A0  E8 2B 66 08 00                  call 0x1406baad0
006344A5  48 8B 1B                        mov rbx, qword ptr [rbx]
006344A8  48 3B DF                        cmp rbx, rdi
006344AB  75 E1                           jne 0x14063448e
006344AD  40 84 ED                        test bpl, bpl
006344B0  74 0C                           je 0x1406344be
006344B2  48 8D 0D C7 F9 8C 00            lea rcx, [rip + 0x8cf9c7]
006344B9  E8 C2 59 D1 FF                  call 0x140349e80
006344BE  41 8B D6                        mov edx, r14d
006344C1  49 8B CF                        mov rcx, r15
006344C4  E8 C7 E1 43 00                  call 0x140a72690
006344C9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006344CE  48 85 F6                        test rsi, rsi
006344D1  74 64                           je 0x140634537
006344D3  40 32 FF                        xor dil, dil
006344D6  40 38 3D DB 03 8D 00            cmp byte ptr [rip + 0x8d03db], dil
006344DD  75 0C                           jne 0x1406344eb
006344DF  F7 05 97 04 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0497], 0x800
006344E9  74 13                           je 0x1406344fe
006344EB  48 8D 0D 8E F9 8C 00            lea rcx, [rip + 0x8cf98e]
006344F2  E8 29 21 BE FF                  call 0x140216620
006344F7  40 8A F8                        mov dil, al
006344FA  84 C0                           test al, al
006344FC  74 39                           je 0x140634537
006344FE  48 83 C6 30                     add rsi, 0x30
00634502  48 8B 1E                        mov rbx, qword ptr [rsi]
00634505  EB 1A                           jmp 0x140634521
00634507  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063450B  48 85 C0                        test rax, rax
0063450E  74 0E                           je 0x14063451e
00634510  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634514  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00634519  E8 B2 65 08 00                  call 0x1406baad0
0063451E  48 8B 1B                        mov rbx, qword ptr [rbx]
00634521  48 3B DE                        cmp rbx, rsi
00634524  75 E1                           jne 0x140634507
00634526  40 84 FF                        test dil, dil
00634529  74 0C                           je 0x140634537
0063452B  48 8D 0D 4E F9 8C 00            lea rcx, [rip + 0x8cf94e]
00634532  E8 49 59 D1 FF                  call 0x140349e80
00634537  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0063453C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00634541  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00634546  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063454B  48 83 C4 40                     add rsp, 0x40
0063454F  41 5F                           pop r15
00634551  41 5E                           pop r14
00634553  5F                              pop rdi
00634554  C3                              ret
00634555  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocateMappingAddressWrapper(__int64 a1, int a2)
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
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(233, a2, a3, a4);
    if (result == 0) goto loc_006344BE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00634442;
    v_stack_m38 = v_stack_p0;
    goto loc_00634450;
loc_00634442:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9241689)) != 0) goto loc_00634472;
    if (((*(unsigned int *)(v_rip + 9241872)) & (0x800ULL)) == 0) goto loc_00634485;
loc_00634472:
    result = ExAcquireRundownProtection(v_rip + 9239047, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006344BE;
loc_00634485:
    goto loc_006344A8;
loc_0063448E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006344A8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063448E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9238983;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmAllocateMappingAddress(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00634537;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9241563)) != 0) goto loc_006344EB;
    if (((*(unsigned int *)(v_rip + 9241751)) & (0x800ULL)) == 0) goto loc_006344FE;
loc_006344EB:
    result = ExAcquireRundownProtection(v_rip + 9238926, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00634537;
loc_006344FE:
    v_rsi = (result) + (48);
    goto loc_00634521;
loc_00634507:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00634521:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00634507;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9238862;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocateMappingAddressWrapper(int64_t Arg1, int32_t Arg2)
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
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(233, Arg2, a3, a4);
    if (result == 0) goto loc_006344BE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00634442;
    v_stack_m38 = v_stack_p0;
    goto loc_00634450;
loc_00634442:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8D0459)) != 0) goto loc_00634472;
    if (((*(uint32_t *)(v_rip + 0x8D0510)) & (0x800ULL)) == 0) goto loc_00634485;
loc_00634472:
    result = ExAcquireRundownProtection(v_rip + 9239047, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006344BE;
loc_00634485:
    goto loc_006344A8;
loc_0063448E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006344A8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063448E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9238983;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = MmAllocateMappingAddress(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00634537;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D03DB)) != 0) goto loc_006344EB;
    if (((*(uint32_t *)(v_rip + 0x8D0497)) & (0x800ULL)) == 0) goto loc_006344FE;
loc_006344EB:
    result = ExAcquireRundownProtection(v_rip + 9238926, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00634537;
loc_006344FE:
    local_rsi = (result) + (48);
    goto loc_00634521;
loc_00634507:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_00634521:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00634507;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9238862;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006343F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006343F0[BB_006343F0]
  bb_0063442F[BB_0063442F]
  bb_00634436[BB_00634436]
  bb_00634442[BB_00634442]
  bb_00634446[BB_00634446]
  bb_00634450[BB_00634450]
  bb_00634466[BB_00634466]
  bb_00634472[BB_00634472]
  bb_00634485[BB_00634485]
  bb_0063448E[BB_0063448E]
  bb_00634497[BB_00634497]
  bb_006344A5[BB_006344A5]
  bb_006344A8[BB_006344A8]
  bb_006344AD[BB_006344AD]
  bb_006344B2[BB_006344B2]
  bb_006344BE[BB_006344BE]
  bb_006344D3[BB_006344D3]
  bb_006344DF[BB_006344DF]
  bb_006344EB[BB_006344EB]
  bb_006344FE[BB_006344FE]
  bb_00634507[BB_00634507]
  bb_00634510[BB_00634510]
  bb_0063451E[BB_0063451E]
  bb_00634521[BB_00634521]
  bb_00634526[BB_00634526]
  bb_0063452B[BB_0063452B]
  bb_00634537[BB_00634537]
  bb_00634555[BB_00634555]
  bb_006343F0 -->|branch| bb_006344BE
  bb_006343F0 -->|fallthrough| bb_0063442F
  bb_0063442F -->|branch| bb_00634442
  bb_0063442F -->|fallthrough| bb_00634436
  bb_00634436 -->|branch| bb_00634450
  bb_00634442 -->|branch| bb_00634450
  bb_00634442 -->|fallthrough| bb_00634446
  bb_00634446 -->|flow| bb_00634450
  bb_00634450 -->|branch| bb_00634472
  bb_00634450 -->|fallthrough| bb_00634466
  bb_00634466 -->|branch| bb_00634485
  bb_00634466 -->|fallthrough| bb_00634472
  bb_00634472 -->|branch| bb_006344BE
  bb_00634472 -->|fallthrough| bb_00634485
  bb_00634485 -->|branch| bb_006344A8
  bb_0063448E -->|branch| bb_006344A5
  bb_0063448E -->|fallthrough| bb_00634497
  bb_00634497 -->|flow| bb_006344A5
  bb_006344A5 -->|flow| bb_006344A8
  bb_006344A8 -->|branch| bb_0063448E
  bb_006344A8 -->|fallthrough| bb_006344AD
  bb_006344AD -->|branch| bb_006344BE
  bb_006344AD -->|fallthrough| bb_006344B2
  bb_006344B2 -->|flow| bb_006344BE
  bb_006344BE -->|branch| bb_00634537
  bb_006344BE -->|fallthrough| bb_006344D3
  bb_006344D3 -->|branch| bb_006344EB
  bb_006344D3 -->|fallthrough| bb_006344DF
  bb_006344DF -->|branch| bb_006344FE
  bb_006344DF -->|fallthrough| bb_006344EB
  bb_006344EB -->|branch| bb_00634537
  bb_006344EB -->|fallthrough| bb_006344FE
  bb_006344FE -->|branch| bb_00634521
  bb_00634507 -->|branch| bb_0063451E
  bb_00634507 -->|fallthrough| bb_00634510
  bb_00634510 -->|flow| bb_0063451E
  bb_0063451E -->|flow| bb_00634521
  bb_00634521 -->|branch| bb_00634507
  bb_00634521 -->|fallthrough| bb_00634526
  bb_00634526 -->|branch| bb_00634537
  bb_00634526 -->|fallthrough| bb_0063452B
  bb_0063452B -->|flow| bb_00634537
```
