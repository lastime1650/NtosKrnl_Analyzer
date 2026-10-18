# DifKeReleaseInStackQueuedSpinLockForDpcWrapper

- RVA: `0x006313B0`–`0x00631500` (길이 `336` bytes)
- VA: `0x00000001406313B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006313D8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00631400` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063142E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00631455` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063146E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00631476` → [KeReleaseInStackQueuedSpinLockForDpc](../46/KeReleaseInStackQueuedSpinLockForDpc_function_0046A3E0.md) (function, `0x0046A3E0`)
- `0x0063149F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006314C6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006314DF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00631412` → RVA `0x00F048B8` (`.data`; read)
- `0x0063141B` → RVA `0x00F04980` (`.data`; read)
- `0x00631427` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006313B0  48 8B C4                        mov rax, rsp
006313B3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006313B7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006313BB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006313BF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006313C3  41 56                           push r14
006313C5  48 83 EC 30                     sub rsp, 0x30
006313C9  48 8B E9                        mov rbp, rcx
006313CC  0F 57 C0                        xorps xmm0, xmm0
006313CF  B9 07 01 00 00                  mov ecx, 0x107
006313D4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
006313D8  E8 57 46 E6 FF                  call 0x140495a34
006313DD  48 8B F8                        mov rdi, rax
006313E0  48 85 C0                        test rax, rax
006313E3  0F 84 8A 00 00 00               je 0x140631473
006313E9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006313EC  A8 18                           test al, 0x18
006313EE  74 0C                           je 0x1406313fc
006313F0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
006313F5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006313FA  EB 0E                           jmp 0x14063140a
006313FC  A8 04                           test al, 4
006313FE  74 0A                           je 0x14063140a
00631400  E8 03 28 EA FF                  call 0x1404d3c08
00631405  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063140A  40 32 F6                        xor sil, sil
0063140D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00631412  40 38 35 9F 34 8D 00            cmp byte ptr [rip + 0x8d349f], sil
00631419  75 0C                           jne 0x140631427
0063141B  F7 05 5B 35 8D 00 00 08 00 00   test dword ptr [rip + 0x8d355b], 0x800
00631425  74 13                           je 0x14063143a
00631427  48 8D 0D 52 2A 8D 00            lea rcx, [rip + 0x8d2a52]
0063142E  E8 ED 51 BE FF                  call 0x140216620
00631433  40 8A F0                        mov sil, al
00631436  84 C0                           test al, al
00631438  74 39                           je 0x140631473
0063143A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0063143E  49 8B 1E                        mov rbx, qword ptr [r14]
00631441  EB 1A                           jmp 0x14063145d
00631443  48 8D 43 F0                     lea rax, [rbx - 0x10]
00631447  48 85 C0                        test rax, rax
0063144A  74 0E                           je 0x14063145a
0063144C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00631450  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00631455  E8 76 96 08 00                  call 0x1406baad0
0063145A  48 8B 1B                        mov rbx, qword ptr [rbx]
0063145D  49 3B DE                        cmp rbx, r14
00631460  75 E1                           jne 0x140631443
00631462  40 84 F6                        test sil, sil
00631465  74 0C                           je 0x140631473
00631467  48 8D 0D 12 2A 8D 00            lea rcx, [rip + 0x8d2a12]
0063146E  E8 0D 8A D1 FF                  call 0x140349e80
00631473  48 8B CD                        mov rcx, rbp
00631476  E8 65 8F E3 FF                  call 0x14046a3e0
0063147B  48 85 FF                        test rdi, rdi
0063147E  74 64                           je 0x1406314e4
00631480  40 32 F6                        xor sil, sil
00631483  40 38 35 2E 34 8D 00            cmp byte ptr [rip + 0x8d342e], sil
0063148A  75 0C                           jne 0x140631498
0063148C  F7 05 EA 34 8D 00 00 08 00 00   test dword ptr [rip + 0x8d34ea], 0x800
00631496  74 13                           je 0x1406314ab
00631498  48 8D 0D E1 29 8D 00            lea rcx, [rip + 0x8d29e1]
0063149F  E8 7C 51 BE FF                  call 0x140216620
006314A4  40 8A F0                        mov sil, al
006314A7  84 C0                           test al, al
006314A9  74 39                           je 0x1406314e4
006314AB  48 83 C7 30                     add rdi, 0x30
006314AF  48 8B 1F                        mov rbx, qword ptr [rdi]
006314B2  EB 1A                           jmp 0x1406314ce
006314B4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006314B8  48 85 C0                        test rax, rax
006314BB  74 0E                           je 0x1406314cb
006314BD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006314C1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006314C6  E8 05 96 08 00                  call 0x1406baad0
006314CB  48 8B 1B                        mov rbx, qword ptr [rbx]
006314CE  48 3B DF                        cmp rbx, rdi
006314D1  75 E1                           jne 0x1406314b4
006314D3  40 84 F6                        test sil, sil
006314D6  74 0C                           je 0x1406314e4
006314D8  48 8D 0D A1 29 8D 00            lea rcx, [rip + 0x8d29a1]
006314DF  E8 9C 89 D1 FF                  call 0x140349e80
006314E4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006314E9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006314EE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006314F3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
006314F8  48 83 C4 30                     add rsp, 0x30
006314FC  41 5E                           pop r14
006314FE  C3                              ret
006314FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeReleaseInStackQueuedSpinLockForDpcWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(263, a2, a3, a4);
    if (result == 0) goto loc_00631473;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006313FC;
    v_stack_m18 = v_stack_p0;
    goto loc_0063140A;
loc_006313FC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9254047)) != 0) goto loc_00631427;
    if (((*(unsigned int *)(v_rip + 9254235)) & (0x800ULL)) == 0) goto loc_0063143A;
loc_00631427:
    result = ExAcquireRundownProtection(v_rip + 9251410, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00631473;
loc_0063143A:
    goto loc_0063145D;
loc_00631443:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063145D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00631443;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9251346;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeReleaseInStackQueuedSpinLockForDpc(a1, a2, a3, a4);
    if (result == 0) goto loc_006314E4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9253934)) != 0) goto loc_00631498;
    if (((*(unsigned int *)(v_rip + 9254122)) & (0x800ULL)) == 0) goto loc_006314AB;
loc_00631498:
    result = ExAcquireRundownProtection(v_rip + 9251297, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006314E4;
loc_006314AB:
    v_rdi = (result) + (48);
    goto loc_006314CE;
loc_006314B4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006314CE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_006314B4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9251233;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeReleaseInStackQueuedSpinLockForDpcWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(263, a2, a3, a4);
    if (result == 0) goto loc_00631473;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006313FC;
    v_stack_m18 = v_stack_p0;
    goto loc_0063140A;
loc_006313FC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D349F)) != 0) goto loc_00631427;
    if (((*(uint32_t *)(v_rip + 0x8D355B)) & (0x800ULL)) == 0) goto loc_0063143A;
loc_00631427:
    result = ExAcquireRundownProtection(v_rip + 9251410, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00631473;
loc_0063143A:
    goto loc_0063145D;
loc_00631443:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063145D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00631443;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9251346;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeReleaseInStackQueuedSpinLockForDpc(Arg1, a2, a3, a4);
    if (result == 0) goto loc_006314E4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D342E)) != 0) goto loc_00631498;
    if (((*(uint32_t *)(v_rip + 0x8D34EA)) & (0x800ULL)) == 0) goto loc_006314AB;
loc_00631498:
    result = ExAcquireRundownProtection(v_rip + 9251297, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006314E4;
loc_006314AB:
    local_rdi = (result) + (48);
    goto loc_006314CE;
loc_006314B4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006314CE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_006314B4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9251233;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006313B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006313B0[BB_006313B0]
  bb_006313E9[BB_006313E9]
  bb_006313F0[BB_006313F0]
  bb_006313FC[BB_006313FC]
  bb_00631400[BB_00631400]
  bb_0063140A[BB_0063140A]
  bb_0063141B[BB_0063141B]
  bb_00631427[BB_00631427]
  bb_0063143A[BB_0063143A]
  bb_00631443[BB_00631443]
  bb_0063144C[BB_0063144C]
  bb_0063145A[BB_0063145A]
  bb_0063145D[BB_0063145D]
  bb_00631462[BB_00631462]
  bb_00631467[BB_00631467]
  bb_00631473[BB_00631473]
  bb_00631480[BB_00631480]
  bb_0063148C[BB_0063148C]
  bb_00631498[BB_00631498]
  bb_006314AB[BB_006314AB]
  bb_006314B4[BB_006314B4]
  bb_006314BD[BB_006314BD]
  bb_006314CB[BB_006314CB]
  bb_006314CE[BB_006314CE]
  bb_006314D3[BB_006314D3]
  bb_006314D8[BB_006314D8]
  bb_006314E4[BB_006314E4]
  bb_006314FF[BB_006314FF]
  bb_006313B0 -->|branch| bb_00631473
  bb_006313B0 -->|fallthrough| bb_006313E9
  bb_006313E9 -->|branch| bb_006313FC
  bb_006313E9 -->|fallthrough| bb_006313F0
  bb_006313F0 -->|branch| bb_0063140A
  bb_006313FC -->|branch| bb_0063140A
  bb_006313FC -->|fallthrough| bb_00631400
  bb_00631400 -->|flow| bb_0063140A
  bb_0063140A -->|branch| bb_00631427
  bb_0063140A -->|fallthrough| bb_0063141B
  bb_0063141B -->|branch| bb_0063143A
  bb_0063141B -->|fallthrough| bb_00631427
  bb_00631427 -->|branch| bb_00631473
  bb_00631427 -->|fallthrough| bb_0063143A
  bb_0063143A -->|branch| bb_0063145D
  bb_00631443 -->|branch| bb_0063145A
  bb_00631443 -->|fallthrough| bb_0063144C
  bb_0063144C -->|flow| bb_0063145A
  bb_0063145A -->|flow| bb_0063145D
  bb_0063145D -->|branch| bb_00631443
  bb_0063145D -->|fallthrough| bb_00631462
  bb_00631462 -->|branch| bb_00631473
  bb_00631462 -->|fallthrough| bb_00631467
  bb_00631467 -->|flow| bb_00631473
  bb_00631473 -->|branch| bb_006314E4
  bb_00631473 -->|fallthrough| bb_00631480
  bb_00631480 -->|branch| bb_00631498
  bb_00631480 -->|fallthrough| bb_0063148C
  bb_0063148C -->|branch| bb_006314AB
  bb_0063148C -->|fallthrough| bb_00631498
  bb_00631498 -->|branch| bb_006314E4
  bb_00631498 -->|fallthrough| bb_006314AB
  bb_006314AB -->|branch| bb_006314CE
  bb_006314B4 -->|branch| bb_006314CB
  bb_006314B4 -->|fallthrough| bb_006314BD
  bb_006314BD -->|flow| bb_006314CB
  bb_006314CB -->|flow| bb_006314CE
  bb_006314CE -->|branch| bb_006314B4
  bb_006314CE -->|fallthrough| bb_006314D3
  bb_006314D3 -->|branch| bb_006314E4
  bb_006314D3 -->|fallthrough| bb_006314D8
  bb_006314D8 -->|flow| bb_006314E4
```
