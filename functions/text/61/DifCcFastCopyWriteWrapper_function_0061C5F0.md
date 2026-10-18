# DifCcFastCopyWriteWrapper

- RVA: `0x0061C5F0`–`0x0061C76B` (길이 `379` bytes)
- VA: `0x000000014061C5F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC264`
- 디코드: `107`개 명령, `379/379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061C628` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061C650` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061C68D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C6B4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C6CD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061C6DE` → [CcFastCopyWrite](../57/CcFastCopyWrite_function_0057CA50.md) (function, `0x0057CA50`)
- `0x0061C707` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C72E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C747` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061C662` → RVA `0x00F048B8` (`.data`; read)
- `0x0061C67A` → RVA `0x00F04980` (`.data`; read)
- `0x0061C686` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061C5F0  48 8B C4                        mov rax, rsp
0061C5F3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0061C5F7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0061C5FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061C5FF  57                              push rdi
0061C600  41 54                           push r12
0061C602  41 55                           push r13
0061C604  41 56                           push r14
0061C606  41 57                           push r15
0061C608  48 83 EC 40                     sub rsp, 0x40
0061C60C  0F 57 C0                        xorps xmm0, xmm0
0061C60F  4C 8B E9                        mov r13, rcx
0061C612  B9 AF 01 00 00                  mov ecx, 0x1af
0061C617  4D 8B F1                        mov r14, r9
0061C61A  0F 11 40 B8                     movups xmmword ptr [rax - 0x48], xmm0
0061C61E  45 8B F8                        mov r15d, r8d
0061C621  44 8B E2                        mov r12d, edx
0061C624  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0061C628  E8 07 94 E7 FF                  call 0x140495a34
0061C62D  48 8B F0                        mov rsi, rax
0061C630  48 85 C0                        test rax, rax
0061C633  0F 84 99 00 00 00               je 0x14061c6d2
0061C639  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061C63C  A8 18                           test al, 0x18
0061C63E  74 0C                           je 0x14061c64c
0061C640  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0061C645  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061C64A  EB 0E                           jmp 0x14061c65a
0061C64C  A8 04                           test al, 4
0061C64E  74 0A                           je 0x14061c65a
0061C650  E8 B3 75 EB FF                  call 0x1404d3c08
0061C655  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061C65A  40 32 ED                        xor bpl, bpl
0061C65D  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0061C662  40 38 2D 4F 82 8E 00            cmp byte ptr [rip + 0x8e824f], bpl
0061C669  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
0061C66E  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
0061C673  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0061C678  75 0C                           jne 0x14061c686
0061C67A  F7 05 FC 82 8E 00 00 08 00 00   test dword ptr [rip + 0x8e82fc], 0x800
0061C684  74 13                           je 0x14061c699
0061C686  48 8D 0D F3 77 8E 00            lea rcx, [rip + 0x8e77f3]
0061C68D  E8 8E 9F BF FF                  call 0x140216620
0061C692  40 8A E8                        mov bpl, al
0061C695  84 C0                           test al, al
0061C697  74 39                           je 0x14061c6d2
0061C699  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061C69D  48 8B 1F                        mov rbx, qword ptr [rdi]
0061C6A0  EB 1A                           jmp 0x14061c6bc
0061C6A2  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C6A6  48 85 C0                        test rax, rax
0061C6A9  74 0E                           je 0x14061c6b9
0061C6AB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C6AF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061C6B4  E8 17 E4 09 00                  call 0x1406baad0
0061C6B9  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C6BC  48 3B DF                        cmp rbx, rdi
0061C6BF  75 E1                           jne 0x14061c6a2
0061C6C1  40 84 ED                        test bpl, bpl
0061C6C4  74 0C                           je 0x14061c6d2
0061C6C6  48 8D 0D B3 77 8E 00            lea rcx, [rip + 0x8e77b3]
0061C6CD  E8 AE D7 D2 FF                  call 0x140349e80
0061C6D2  4D 8B CE                        mov r9, r14
0061C6D5  45 8B C7                        mov r8d, r15d
0061C6D8  41 8B D4                        mov edx, r12d
0061C6DB  49 8B CD                        mov rcx, r13
0061C6DE  E8 6D 03 F6 FF                  call 0x14057ca50
0061C6E3  48 85 F6                        test rsi, rsi
0061C6E6  74 64                           je 0x14061c74c
0061C6E8  40 32 FF                        xor dil, dil
0061C6EB  40 38 3D C6 81 8E 00            cmp byte ptr [rip + 0x8e81c6], dil
0061C6F2  75 0C                           jne 0x14061c700
0061C6F4  F7 05 82 82 8E 00 00 08 00 00   test dword ptr [rip + 0x8e8282], 0x800
0061C6FE  74 13                           je 0x14061c713
0061C700  48 8D 0D 79 77 8E 00            lea rcx, [rip + 0x8e7779]
0061C707  E8 14 9F BF FF                  call 0x140216620
0061C70C  40 8A F8                        mov dil, al
0061C70F  84 C0                           test al, al
0061C711  74 39                           je 0x14061c74c
0061C713  48 83 C6 30                     add rsi, 0x30
0061C717  48 8B 1E                        mov rbx, qword ptr [rsi]
0061C71A  EB 1A                           jmp 0x14061c736
0061C71C  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C720  48 85 C0                        test rax, rax
0061C723  74 0E                           je 0x14061c733
0061C725  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C729  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061C72E  E8 9D E3 09 00                  call 0x1406baad0
0061C733  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C736  48 3B DE                        cmp rbx, rsi
0061C739  75 E1                           jne 0x14061c71c
0061C73B  40 84 FF                        test dil, dil
0061C73E  74 0C                           je 0x14061c74c
0061C740  48 8D 0D 39 77 8E 00            lea rcx, [rip + 0x8e7739]
0061C747  E8 34 D7 D2 FF                  call 0x140349e80
0061C74C  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
0061C751  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0061C755  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0061C759  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0061C75D  49 8B E3                        mov rsp, r11
0061C760  41 5F                           pop r15
0061C762  41 5E                           pop r14
0061C764  41 5D                           pop r13
0061C766  41 5C                           pop r12
0061C768  5F                              pop rdi
0061C769  C3                              ret
0061C76A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCcFastCopyWriteWrapper(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    result = DifGetAPIThunkContextById(431, a2, a3, a4);
    if (result == 0) goto loc_0061C6D2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061C64C;
    v_stack_m48 = v_stack_p0;
    goto loc_0061C65A;
loc_0061C64C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m48 = result;
    }
    v_rbp = 0;
    v_stack_m30 = a1;
    v_stack_m34 = (unsigned int)((unsigned int)(a2));
    v_stack_m38 = (unsigned int)((unsigned int)(a3));
    v_stack_m40 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9339471)) != 0) goto loc_0061C686;
    if (((*(unsigned int *)(v_rip + 9339644)) & (0x800ULL)) == 0) goto loc_0061C699;
loc_0061C686:
    result = ExAcquireRundownProtection(v_rip + 9336819, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C6D2;
loc_0061C699:
    goto loc_0061C6BC;
loc_0061C6A2:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061C6BC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061C6A2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9336755;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = CcFastCopyWrite(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (result == 0) goto loc_0061C74C;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9339334)) != 0) goto loc_0061C700;
    if (((*(unsigned int *)(v_rip + 9339522)) & (0x800ULL)) == 0) goto loc_0061C713;
loc_0061C700:
    result = ExAcquireRundownProtection(v_rip + 9336697, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C74C;
loc_0061C713:
    v_rsi = (result) + (48);
    goto loc_0061C736;
loc_0061C71C:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0061C736:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061C71C;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9336633;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifCcFastCopyWriteWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    result = DifGetAPIThunkContextById(431, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0061C6D2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061C64C;
    v_stack_m48 = v_stack_p0;
    goto loc_0061C65A;
loc_0061C64C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m48 = result;
    }
    local_rbp = 0;
    v_stack_m30 = Arg1;
    v_stack_m34 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m38 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m40 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8E824F)) != 0) goto loc_0061C686;
    if (((*(uint32_t *)(v_rip + 0x8E82FC)) & (0x800ULL)) == 0) goto loc_0061C699;
loc_0061C686:
    result = ExAcquireRundownProtection(v_rip + 9336819, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C6D2;
loc_0061C699:
    goto loc_0061C6BC;
loc_0061C6A2:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0061C6BC:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061C6A2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9336755;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = CcFastCopyWrite(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if (result == 0) goto loc_0061C74C;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E81C6)) != 0) goto loc_0061C700;
    if (((*(uint32_t *)(v_rip + 0x8E8282)) & (0x800ULL)) == 0) goto loc_0061C713;
loc_0061C700:
    result = ExAcquireRundownProtection(v_rip + 9336697, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C74C;
loc_0061C713:
    local_rsi = (result) + (48);
    goto loc_0061C736;
loc_0061C71C:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0061C736:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061C71C;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9336633;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061C5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061C5F0[BB_0061C5F0]
  bb_0061C639[BB_0061C639]
  bb_0061C640[BB_0061C640]
  bb_0061C64C[BB_0061C64C]
  bb_0061C650[BB_0061C650]
  bb_0061C65A[BB_0061C65A]
  bb_0061C67A[BB_0061C67A]
  bb_0061C686[BB_0061C686]
  bb_0061C699[BB_0061C699]
  bb_0061C6A2[BB_0061C6A2]
  bb_0061C6AB[BB_0061C6AB]
  bb_0061C6B9[BB_0061C6B9]
  bb_0061C6BC[BB_0061C6BC]
  bb_0061C6C1[BB_0061C6C1]
  bb_0061C6C6[BB_0061C6C6]
  bb_0061C6D2[BB_0061C6D2]
  bb_0061C6E8[BB_0061C6E8]
  bb_0061C6F4[BB_0061C6F4]
  bb_0061C700[BB_0061C700]
  bb_0061C713[BB_0061C713]
  bb_0061C71C[BB_0061C71C]
  bb_0061C725[BB_0061C725]
  bb_0061C733[BB_0061C733]
  bb_0061C736[BB_0061C736]
  bb_0061C73B[BB_0061C73B]
  bb_0061C740[BB_0061C740]
  bb_0061C74C[BB_0061C74C]
  bb_0061C76A[BB_0061C76A]
  bb_0061C5F0 -->|branch| bb_0061C6D2
  bb_0061C5F0 -->|fallthrough| bb_0061C639
  bb_0061C639 -->|branch| bb_0061C64C
  bb_0061C639 -->|fallthrough| bb_0061C640
  bb_0061C640 -->|branch| bb_0061C65A
  bb_0061C64C -->|branch| bb_0061C65A
  bb_0061C64C -->|fallthrough| bb_0061C650
  bb_0061C650 -->|flow| bb_0061C65A
  bb_0061C65A -->|branch| bb_0061C686
  bb_0061C65A -->|fallthrough| bb_0061C67A
  bb_0061C67A -->|branch| bb_0061C699
  bb_0061C67A -->|fallthrough| bb_0061C686
  bb_0061C686 -->|branch| bb_0061C6D2
  bb_0061C686 -->|fallthrough| bb_0061C699
  bb_0061C699 -->|branch| bb_0061C6BC
  bb_0061C6A2 -->|branch| bb_0061C6B9
  bb_0061C6A2 -->|fallthrough| bb_0061C6AB
  bb_0061C6AB -->|flow| bb_0061C6B9
  bb_0061C6B9 -->|flow| bb_0061C6BC
  bb_0061C6BC -->|branch| bb_0061C6A2
  bb_0061C6BC -->|fallthrough| bb_0061C6C1
  bb_0061C6C1 -->|branch| bb_0061C6D2
  bb_0061C6C1 -->|fallthrough| bb_0061C6C6
  bb_0061C6C6 -->|flow| bb_0061C6D2
  bb_0061C6D2 -->|branch| bb_0061C74C
  bb_0061C6D2 -->|fallthrough| bb_0061C6E8
  bb_0061C6E8 -->|branch| bb_0061C700
  bb_0061C6E8 -->|fallthrough| bb_0061C6F4
  bb_0061C6F4 -->|branch| bb_0061C713
  bb_0061C6F4 -->|fallthrough| bb_0061C700
  bb_0061C700 -->|branch| bb_0061C74C
  bb_0061C700 -->|fallthrough| bb_0061C713
  bb_0061C713 -->|branch| bb_0061C736
  bb_0061C71C -->|branch| bb_0061C733
  bb_0061C71C -->|fallthrough| bb_0061C725
  bb_0061C725 -->|flow| bb_0061C733
  bb_0061C733 -->|flow| bb_0061C736
  bb_0061C736 -->|branch| bb_0061C71C
  bb_0061C736 -->|fallthrough| bb_0061C73B
  bb_0061C73B -->|branch| bb_0061C74C
  bb_0061C73B -->|fallthrough| bb_0061C740
  bb_0061C740 -->|flow| bb_0061C74C
```
