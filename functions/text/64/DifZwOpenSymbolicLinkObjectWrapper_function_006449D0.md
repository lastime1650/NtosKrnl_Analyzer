# DifZwOpenSymbolicLinkObjectWrapper

- RVA: `0x006449D0`–`0x00644B45` (길이 `373` bytes)
- VA: `0x00000001406449D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00644A0C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00644A32` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00644A66` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644A8C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644AA5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644AB3` → [ZwOpenSymbolicLinkObject](../6A/ZwOpenSymbolicLinkObject_function_006AF7F0.md) (function, `0x006AF7F0`)
- `0x00644ADF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644B05` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644B1E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00644A42` → RVA `0x00F048B8` (`.data`; read)
- `0x00644A53` → RVA `0x00F04980` (`.data`; read)
- `0x00644A5F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006449D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006449D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
006449DA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
006449DF  55                              push rbp
006449E0  41 54                           push r12
006449E2  41 55                           push r13
006449E4  41 56                           push r14
006449E6  41 57                           push r15
006449E8  48 8B EC                        mov rbp, rsp
006449EB  48 83 EC 50                     sub rsp, 0x50
006449EF  33 C0                           xor eax, eax
006449F1  0F 57 C0                        xorps xmm0, xmm0
006449F4  4C 8B E9                        mov r13, rcx
006449F7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006449FB  4D 8B F8                        mov r15, r8
006449FE  44 8B E2                        mov r12d, edx
00644A01  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00644A05  8D 48 4A                        lea ecx, [rax + 0x4a]
00644A08  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00644A0C  E8 23 10 E5 FF                  call 0x140495a34
00644A11  48 8B F0                        mov rsi, rax
00644A14  48 85 C0                        test rax, rax
00644A17  0F 84 8D 00 00 00               je 0x140644aaa
00644A1D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00644A20  A8 18                           test al, 0x18
00644A22  74 0A                           je 0x140644a2e
00644A24  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00644A28  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00644A2C  EB 0D                           jmp 0x140644a3b
00644A2E  A8 04                           test al, 4
00644A30  74 09                           je 0x140644a3b
00644A32  E8 D1 F1 E8 FF                  call 0x1404d3c08
00644A37  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00644A3B  45 32 F6                        xor r14b, r14b
00644A3E  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00644A42  44 38 35 6F FE 8B 00            cmp byte ptr [rip + 0x8bfe6f], r14b
00644A49  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00644A4D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00644A51  75 0C                           jne 0x140644a5f
00644A53  F7 05 23 FF 8B 00 00 08 00 00   test dword ptr [rip + 0x8bff23], 0x800
00644A5D  74 13                           je 0x140644a72
00644A5F  48 8D 0D 1A F4 8B 00            lea rcx, [rip + 0x8bf41a]
00644A66  E8 B5 1B BD FF                  call 0x140216620
00644A6B  44 8A F0                        mov r14b, al
00644A6E  84 C0                           test al, al
00644A70  74 38                           je 0x140644aaa
00644A72  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00644A76  48 8B 1F                        mov rbx, qword ptr [rdi]
00644A79  EB 19                           jmp 0x140644a94
00644A7B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644A7F  48 85 C0                        test rax, rax
00644A82  74 0D                           je 0x140644a91
00644A84  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644A88  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644A8C  E8 3F 60 07 00                  call 0x1406baad0
00644A91  48 8B 1B                        mov rbx, qword ptr [rbx]
00644A94  48 3B DF                        cmp rbx, rdi
00644A97  75 E2                           jne 0x140644a7b
00644A99  45 84 F6                        test r14b, r14b
00644A9C  74 0C                           je 0x140644aaa
00644A9E  48 8D 0D DB F3 8B 00            lea rcx, [rip + 0x8bf3db]
00644AA5  E8 D6 53 D0 FF                  call 0x140349e80
00644AAA  4D 8B C7                        mov r8, r15
00644AAD  41 8B D4                        mov edx, r12d
00644AB0  49 8B CD                        mov rcx, r13
00644AB3  E8 38 AD 06 00                  call 0x1406af7f0
00644AB8  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00644ABB  48 85 F6                        test rsi, rsi
00644ABE  74 63                           je 0x140644b23
00644AC0  40 32 FF                        xor dil, dil
00644AC3  40 38 3D EE FD 8B 00            cmp byte ptr [rip + 0x8bfdee], dil
00644ACA  75 0C                           jne 0x140644ad8
00644ACC  F7 05 AA FE 8B 00 00 08 00 00   test dword ptr [rip + 0x8bfeaa], 0x800
00644AD6  74 13                           je 0x140644aeb
00644AD8  48 8D 0D A1 F3 8B 00            lea rcx, [rip + 0x8bf3a1]
00644ADF  E8 3C 1B BD FF                  call 0x140216620
00644AE4  40 8A F8                        mov dil, al
00644AE7  84 C0                           test al, al
00644AE9  74 38                           je 0x140644b23
00644AEB  48 83 C6 30                     add rsi, 0x30
00644AEF  48 8B 1E                        mov rbx, qword ptr [rsi]
00644AF2  EB 19                           jmp 0x140644b0d
00644AF4  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644AF8  48 85 C0                        test rax, rax
00644AFB  74 0D                           je 0x140644b0a
00644AFD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644B01  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644B05  E8 C6 5F 07 00                  call 0x1406baad0
00644B0A  48 8B 1B                        mov rbx, qword ptr [rbx]
00644B0D  48 3B DE                        cmp rbx, rsi
00644B10  75 E2                           jne 0x140644af4
00644B12  40 84 FF                        test dil, dil
00644B15  74 0C                           je 0x140644b23
00644B17  48 8D 0D 62 F3 8B 00            lea rcx, [rip + 0x8bf362]
00644B1E  E8 5D 53 D0 FF                  call 0x140349e80
00644B23  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00644B26  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00644B2B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00644B2F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00644B33  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00644B37  49 8B E3                        mov rsp, r11
00644B3A  41 5F                           pop r15
00644B3C  41 5E                           pop r14
00644B3E  41 5D                           pop r13
00644B40  41 5C                           pop r12
00644B42  5D                              pop rbp
00644B43  C3                              ret
00644B44  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenSymbolicLinkObjectWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 74, a2, a3, a4);
    if (result == 0) goto loc_00644AAA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00644A2E;
    v_stack_m58 = v_stack_p0;
    goto loc_00644A3B;
loc_00644A2E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9174639)) != 0) goto loc_00644A5F;
    if (((*(unsigned int *)(v_rip + 9174819)) & (0x800ULL)) == 0) goto loc_00644A72;
loc_00644A5F:
    result = ExAcquireRundownProtection(v_rip + 9171994, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644AAA;
loc_00644A72:
    goto loc_00644A94;
loc_00644A7B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00644A94:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00644A7B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9171931;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenSymbolicLinkObject(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00644B23;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9174510)) != 0) goto loc_00644AD8;
    if (((*(unsigned int *)(v_rip + 9174698)) & (0x800ULL)) == 0) goto loc_00644AEB;
loc_00644AD8:
    result = ExAcquireRundownProtection(v_rip + 9171873, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00644B23;
loc_00644AEB:
    v_rsi = (result) + (48);
    goto loc_00644B0D;
loc_00644AF4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00644B0D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00644AF4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9171810;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenSymbolicLinkObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 74, Arg2, Arg3, a4);
    if (result == 0) goto loc_00644AAA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00644A2E;
    v_stack_m58 = v_stack_p0;
    goto loc_00644A3B;
loc_00644A2E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8BFE6F)) != 0) goto loc_00644A5F;
    if (((*(uint32_t *)(v_rip + 0x8BFF23)) & (0x800ULL)) == 0) goto loc_00644A72;
loc_00644A5F:
    result = ExAcquireRundownProtection(v_rip + 9171994, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00644AAA;
loc_00644A72:
    goto loc_00644A94;
loc_00644A7B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00644A94:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00644A7B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9171931;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenSymbolicLinkObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00644B23;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BFDEE)) != 0) goto loc_00644AD8;
    if (((*(uint32_t *)(v_rip + 0x8BFEAA)) & (0x800ULL)) == 0) goto loc_00644AEB;
loc_00644AD8:
    result = ExAcquireRundownProtection(v_rip + 9171873, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00644B23;
loc_00644AEB:
    local_rsi = (result) + (48);
    goto loc_00644B0D;
loc_00644AF4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_00644B0D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00644AF4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9171810;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006449D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006449D0[BB_006449D0]
  bb_00644A1D[BB_00644A1D]
  bb_00644A24[BB_00644A24]
  bb_00644A2E[BB_00644A2E]
  bb_00644A32[BB_00644A32]
  bb_00644A3B[BB_00644A3B]
  bb_00644A53[BB_00644A53]
  bb_00644A5F[BB_00644A5F]
  bb_00644A72[BB_00644A72]
  bb_00644A7B[BB_00644A7B]
  bb_00644A84[BB_00644A84]
  bb_00644A91[BB_00644A91]
  bb_00644A94[BB_00644A94]
  bb_00644A99[BB_00644A99]
  bb_00644A9E[BB_00644A9E]
  bb_00644AAA[BB_00644AAA]
  bb_00644AC0[BB_00644AC0]
  bb_00644ACC[BB_00644ACC]
  bb_00644AD8[BB_00644AD8]
  bb_00644AEB[BB_00644AEB]
  bb_00644AF4[BB_00644AF4]
  bb_00644AFD[BB_00644AFD]
  bb_00644B0A[BB_00644B0A]
  bb_00644B0D[BB_00644B0D]
  bb_00644B12[BB_00644B12]
  bb_00644B17[BB_00644B17]
  bb_00644B23[BB_00644B23]
  bb_00644B44[BB_00644B44]
  bb_006449D0 -->|branch| bb_00644AAA
  bb_006449D0 -->|fallthrough| bb_00644A1D
  bb_00644A1D -->|branch| bb_00644A2E
  bb_00644A1D -->|fallthrough| bb_00644A24
  bb_00644A24 -->|branch| bb_00644A3B
  bb_00644A2E -->|branch| bb_00644A3B
  bb_00644A2E -->|fallthrough| bb_00644A32
  bb_00644A32 -->|flow| bb_00644A3B
  bb_00644A3B -->|branch| bb_00644A5F
  bb_00644A3B -->|fallthrough| bb_00644A53
  bb_00644A53 -->|branch| bb_00644A72
  bb_00644A53 -->|fallthrough| bb_00644A5F
  bb_00644A5F -->|branch| bb_00644AAA
  bb_00644A5F -->|fallthrough| bb_00644A72
  bb_00644A72 -->|branch| bb_00644A94
  bb_00644A7B -->|branch| bb_00644A91
  bb_00644A7B -->|fallthrough| bb_00644A84
  bb_00644A84 -->|flow| bb_00644A91
  bb_00644A91 -->|flow| bb_00644A94
  bb_00644A94 -->|branch| bb_00644A7B
  bb_00644A94 -->|fallthrough| bb_00644A99
  bb_00644A99 -->|branch| bb_00644AAA
  bb_00644A99 -->|fallthrough| bb_00644A9E
  bb_00644A9E -->|flow| bb_00644AAA
  bb_00644AAA -->|branch| bb_00644B23
  bb_00644AAA -->|fallthrough| bb_00644AC0
  bb_00644AC0 -->|branch| bb_00644AD8
  bb_00644AC0 -->|fallthrough| bb_00644ACC
  bb_00644ACC -->|branch| bb_00644AEB
  bb_00644ACC -->|fallthrough| bb_00644AD8
  bb_00644AD8 -->|branch| bb_00644B23
  bb_00644AD8 -->|fallthrough| bb_00644AEB
  bb_00644AEB -->|branch| bb_00644B0D
  bb_00644AF4 -->|branch| bb_00644B0A
  bb_00644AF4 -->|fallthrough| bb_00644AFD
  bb_00644AFD -->|flow| bb_00644B0A
  bb_00644B0A -->|flow| bb_00644B0D
  bb_00644B0D -->|branch| bb_00644AF4
  bb_00644B0D -->|fallthrough| bb_00644B12
  bb_00644B12 -->|branch| bb_00644B23
  bb_00644B12 -->|fallthrough| bb_00644B17
  bb_00644B17 -->|flow| bb_00644B23
```
