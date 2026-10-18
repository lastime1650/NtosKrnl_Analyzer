# DifPoFxSetComponentResidencyWrapper

- RVA: `0x00639CE0`–`0x00639E52` (길이 `370` bytes)
- VA: `0x0000000140639CE0`
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
- `0x00639D16` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00639D3E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00639D76` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639D9D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639DB6` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00639DC4` → [PoFxSetComponentResidency](../5D/PoFxSetComponentResidency_function_005D2100.md) (function, `0x005D2100`)
- `0x00639DED` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00639E14` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00639E2D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00639D50` → RVA `0x00F048B8` (`.data`; read)
- `0x00639D63` → RVA `0x00F04980` (`.data`; read)
- `0x00639D6F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00639CE0  48 8B C4                        mov rax, rsp
00639CE3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00639CE7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00639CEB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00639CEF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00639CF3  41 54                           push r12
00639CF5  41 56                           push r14
00639CF7  41 57                           push r15
00639CF9  48 83 EC 40                     sub rsp, 0x40
00639CFD  0F 57 C0                        xorps xmm0, xmm0
00639D00  4C 8B E1                        mov r12, rcx
00639D03  B9 B7 00 00 00                  mov ecx, 0xb7
00639D08  4D 8B F0                        mov r14, r8
00639D0B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00639D0F  44 8B FA                        mov r15d, edx
00639D12  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00639D16  E8 19 BD E5 FF                  call 0x140495a34
00639D1B  48 8B F0                        mov rsi, rax
00639D1E  48 85 C0                        test rax, rax
00639D21  0F 84 94 00 00 00               je 0x140639dbb
00639D27  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00639D2A  A8 18                           test al, 0x18
00639D2C  74 0C                           je 0x140639d3a
00639D2E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00639D33  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00639D38  EB 0E                           jmp 0x140639d48
00639D3A  A8 04                           test al, 4
00639D3C  74 0A                           je 0x140639d48
00639D3E  E8 C5 9E E9 FF                  call 0x1404d3c08
00639D43  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00639D48  40 32 ED                        xor bpl, bpl
00639D4B  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
00639D50  40 38 2D 61 AB 8C 00            cmp byte ptr [rip + 0x8cab61], bpl
00639D57  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
00639D5C  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00639D61  75 0C                           jne 0x140639d6f
00639D63  F7 05 13 AC 8C 00 00 08 00 00   test dword ptr [rip + 0x8cac13], 0x800
00639D6D  74 13                           je 0x140639d82
00639D6F  48 8D 0D 0A A1 8C 00            lea rcx, [rip + 0x8ca10a]
00639D76  E8 A5 C8 BD FF                  call 0x140216620
00639D7B  40 8A E8                        mov bpl, al
00639D7E  84 C0                           test al, al
00639D80  74 39                           je 0x140639dbb
00639D82  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00639D86  48 8B 1F                        mov rbx, qword ptr [rdi]
00639D89  EB 1A                           jmp 0x140639da5
00639D8B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639D8F  48 85 C0                        test rax, rax
00639D92  74 0E                           je 0x140639da2
00639D94  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639D98  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639D9D  E8 2E 0D 08 00                  call 0x1406baad0
00639DA2  48 8B 1B                        mov rbx, qword ptr [rbx]
00639DA5  48 3B DF                        cmp rbx, rdi
00639DA8  75 E1                           jne 0x140639d8b
00639DAA  40 84 ED                        test bpl, bpl
00639DAD  74 0C                           je 0x140639dbb
00639DAF  48 8D 0D CA A0 8C 00            lea rcx, [rip + 0x8ca0ca]
00639DB6  E8 C5 00 D1 FF                  call 0x140349e80
00639DBB  4D 8B C6                        mov r8, r14
00639DBE  41 8B D7                        mov edx, r15d
00639DC1  49 8B CC                        mov rcx, r12
00639DC4  E8 37 83 F9 FF                  call 0x1405d2100
00639DC9  48 85 F6                        test rsi, rsi
00639DCC  74 64                           je 0x140639e32
00639DCE  40 32 FF                        xor dil, dil
00639DD1  40 38 3D E0 AA 8C 00            cmp byte ptr [rip + 0x8caae0], dil
00639DD8  75 0C                           jne 0x140639de6
00639DDA  F7 05 9C AB 8C 00 00 08 00 00   test dword ptr [rip + 0x8cab9c], 0x800
00639DE4  74 13                           je 0x140639df9
00639DE6  48 8D 0D 93 A0 8C 00            lea rcx, [rip + 0x8ca093]
00639DED  E8 2E C8 BD FF                  call 0x140216620
00639DF2  40 8A F8                        mov dil, al
00639DF5  84 C0                           test al, al
00639DF7  74 39                           je 0x140639e32
00639DF9  48 83 C6 30                     add rsi, 0x30
00639DFD  48 8B 1E                        mov rbx, qword ptr [rsi]
00639E00  EB 1A                           jmp 0x140639e1c
00639E02  48 8D 43 F0                     lea rax, [rbx - 0x10]
00639E06  48 85 C0                        test rax, rax
00639E09  74 0E                           je 0x140639e19
00639E0B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00639E0F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00639E14  E8 B7 0C 08 00                  call 0x1406baad0
00639E19  48 8B 1B                        mov rbx, qword ptr [rbx]
00639E1C  48 3B DE                        cmp rbx, rsi
00639E1F  75 E1                           jne 0x140639e02
00639E21  40 84 FF                        test dil, dil
00639E24  74 0C                           je 0x140639e32
00639E26  48 8D 0D 53 A0 8C 00            lea rcx, [rip + 0x8ca053]
00639E2D  E8 4E 00 D1 FF                  call 0x140349e80
00639E32  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00639E37  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00639E3C  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00639E41  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00639E46  48 83 C4 40                     add rsp, 0x40
00639E4A  41 5F                           pop r15
00639E4C  41 5E                           pop r14
00639E4E  41 5C                           pop r12
00639E50  C3                              ret
00639E51  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPoFxSetComponentResidencyWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
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
    result = DifGetAPIThunkContextById(183, a2, a3, a4);
    if (result == 0) goto loc_00639DBB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00639D3A;
    v_stack_m38 = v_stack_p0;
    goto loc_00639D48;
loc_00639D3A:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9218913)) != 0) goto loc_00639D6F;
    if (((*(unsigned int *)(v_rip + 9219091)) & (0x800ULL)) == 0) goto loc_00639D82;
loc_00639D6F:
    result = ExAcquireRundownProtection(v_rip + 9216266, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639DBB;
loc_00639D82:
    goto loc_00639DA5;
loc_00639D8B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00639DA5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00639D8B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216202;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PoFxSetComponentResidency(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_00639E32;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9218784)) != 0) goto loc_00639DE6;
    if (((*(unsigned int *)(v_rip + 9218972)) & (0x800ULL)) == 0) goto loc_00639DF9;
loc_00639DE6:
    result = ExAcquireRundownProtection(v_rip + 9216147, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00639E32;
loc_00639DF9:
    v_rsi = (result) + (48);
    goto loc_00639E1C;
loc_00639E02:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00639E1C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00639E02;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9216083;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifPoFxSetComponentResidencyWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
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
    result = DifGetAPIThunkContextById(183, Arg2, Arg3, a4);
    if (result == 0) goto loc_00639DBB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00639D3A;
    v_stack_m38 = v_stack_p0;
    goto loc_00639D48;
loc_00639D3A:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8CAB61)) != 0) goto loc_00639D6F;
    if (((*(uint32_t *)(v_rip + 0x8CAC13)) & (0x800ULL)) == 0) goto loc_00639D82;
loc_00639D6F:
    result = ExAcquireRundownProtection(v_rip + 9216266, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639DBB;
loc_00639D82:
    goto loc_00639DA5;
loc_00639D8B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00639DA5:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00639D8B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216202;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = PoFxSetComponentResidency(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if (result == 0) goto loc_00639E32;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CAAE0)) != 0) goto loc_00639DE6;
    if (((*(uint32_t *)(v_rip + 0x8CAB9C)) & (0x800ULL)) == 0) goto loc_00639DF9;
loc_00639DE6:
    result = ExAcquireRundownProtection(v_rip + 9216147, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00639E32;
loc_00639DF9:
    local_rsi = (result) + (48);
    goto loc_00639E1C;
loc_00639E02:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_00639E1C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00639E02;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9216083;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00639CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00639CE0[BB_00639CE0]
  bb_00639D27[BB_00639D27]
  bb_00639D2E[BB_00639D2E]
  bb_00639D3A[BB_00639D3A]
  bb_00639D3E[BB_00639D3E]
  bb_00639D48[BB_00639D48]
  bb_00639D63[BB_00639D63]
  bb_00639D6F[BB_00639D6F]
  bb_00639D82[BB_00639D82]
  bb_00639D8B[BB_00639D8B]
  bb_00639D94[BB_00639D94]
  bb_00639DA2[BB_00639DA2]
  bb_00639DA5[BB_00639DA5]
  bb_00639DAA[BB_00639DAA]
  bb_00639DAF[BB_00639DAF]
  bb_00639DBB[BB_00639DBB]
  bb_00639DCE[BB_00639DCE]
  bb_00639DDA[BB_00639DDA]
  bb_00639DE6[BB_00639DE6]
  bb_00639DF9[BB_00639DF9]
  bb_00639E02[BB_00639E02]
  bb_00639E0B[BB_00639E0B]
  bb_00639E19[BB_00639E19]
  bb_00639E1C[BB_00639E1C]
  bb_00639E21[BB_00639E21]
  bb_00639E26[BB_00639E26]
  bb_00639E32[BB_00639E32]
  bb_00639E51[BB_00639E51]
  bb_00639CE0 -->|branch| bb_00639DBB
  bb_00639CE0 -->|fallthrough| bb_00639D27
  bb_00639D27 -->|branch| bb_00639D3A
  bb_00639D27 -->|fallthrough| bb_00639D2E
  bb_00639D2E -->|branch| bb_00639D48
  bb_00639D3A -->|branch| bb_00639D48
  bb_00639D3A -->|fallthrough| bb_00639D3E
  bb_00639D3E -->|flow| bb_00639D48
  bb_00639D48 -->|branch| bb_00639D6F
  bb_00639D48 -->|fallthrough| bb_00639D63
  bb_00639D63 -->|branch| bb_00639D82
  bb_00639D63 -->|fallthrough| bb_00639D6F
  bb_00639D6F -->|branch| bb_00639DBB
  bb_00639D6F -->|fallthrough| bb_00639D82
  bb_00639D82 -->|branch| bb_00639DA5
  bb_00639D8B -->|branch| bb_00639DA2
  bb_00639D8B -->|fallthrough| bb_00639D94
  bb_00639D94 -->|flow| bb_00639DA2
  bb_00639DA2 -->|flow| bb_00639DA5
  bb_00639DA5 -->|branch| bb_00639D8B
  bb_00639DA5 -->|fallthrough| bb_00639DAA
  bb_00639DAA -->|branch| bb_00639DBB
  bb_00639DAA -->|fallthrough| bb_00639DAF
  bb_00639DAF -->|flow| bb_00639DBB
  bb_00639DBB -->|branch| bb_00639E32
  bb_00639DBB -->|fallthrough| bb_00639DCE
  bb_00639DCE -->|branch| bb_00639DE6
  bb_00639DCE -->|fallthrough| bb_00639DDA
  bb_00639DDA -->|branch| bb_00639DF9
  bb_00639DDA -->|fallthrough| bb_00639DE6
  bb_00639DE6 -->|branch| bb_00639E32
  bb_00639DE6 -->|fallthrough| bb_00639DF9
  bb_00639DF9 -->|branch| bb_00639E1C
  bb_00639E02 -->|branch| bb_00639E19
  bb_00639E02 -->|fallthrough| bb_00639E0B
  bb_00639E0B -->|flow| bb_00639E19
  bb_00639E19 -->|flow| bb_00639E1C
  bb_00639E1C -->|branch| bb_00639E02
  bb_00639E1C -->|fallthrough| bb_00639E21
  bb_00639E21 -->|branch| bb_00639E32
  bb_00639E21 -->|fallthrough| bb_00639E26
  bb_00639E26 -->|flow| bb_00639E32
```
