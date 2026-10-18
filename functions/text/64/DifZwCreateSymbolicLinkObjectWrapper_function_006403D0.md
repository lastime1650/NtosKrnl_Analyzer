# DifZwCreateSymbolicLinkObjectWrapper

- RVA: `0x006403D0`–`0x00640555` (길이 `389` bytes)
- VA: `0x00000001406403D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00640410` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00640436` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00640472` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640498` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006404B1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006404C3` → [ZwCreateSymbolicLinkObject](../6A/ZwCreateSymbolicLinkObject_function_006AE9D0.md) (function, `0x006AE9D0`)
- `0x006404EF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640515` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064052E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00640446` → RVA `0x00F048B8` (`.data`; read)
- `0x0064045F` → RVA `0x00F04980` (`.data`; read)
- `0x0064046B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006403D0  48 8B C4                        mov rax, rsp
006403D3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006403D7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006403DB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006403DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
006403E3  55                              push rbp
006403E4  41 54                           push r12
006403E6  41 55                           push r13
006403E8  41 56                           push r14
006403EA  41 57                           push r15
006403EC  48 8B EC                        mov rbp, rsp
006403EF  48 83 EC 50                     sub rsp, 0x50
006403F3  0F 57 C0                        xorps xmm0, xmm0
006403F6  B9 76 00 00 00                  mov ecx, 0x76
006403FB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006403FF  4D 8B F9                        mov r15, r9
00640402  4D 8B E0                        mov r12, r8
00640405  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00640409  44 8B EA                        mov r13d, edx
0064040C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00640410  E8 1F 56 E5 FF                  call 0x140495a34
00640415  48 8B F0                        mov rsi, rax
00640418  48 85 C0                        test rax, rax
0064041B  0F 84 95 00 00 00               je 0x1406404b6
00640421  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00640424  A8 18                           test al, 0x18
00640426  74 0A                           je 0x140640432
00640428  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064042C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00640430  EB 0D                           jmp 0x14064043f
00640432  A8 04                           test al, 4
00640434  74 09                           je 0x14064043f
00640436  E8 CD 37 E9 FF                  call 0x1404d3c08
0064043B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064043F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00640443  45 32 F6                        xor r14b, r14b
00640446  44 38 35 6B 44 8C 00            cmp byte ptr [rip + 0x8c446b], r14b
0064044D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00640451  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00640455  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00640459  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064045D  75 0C                           jne 0x14064046b
0064045F  F7 05 17 45 8C 00 00 08 00 00   test dword ptr [rip + 0x8c4517], 0x800
00640469  74 13                           je 0x14064047e
0064046B  48 8D 0D 0E 3A 8C 00            lea rcx, [rip + 0x8c3a0e]
00640472  E8 A9 61 BD FF                  call 0x140216620
00640477  44 8A F0                        mov r14b, al
0064047A  84 C0                           test al, al
0064047C  74 38                           je 0x1406404b6
0064047E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00640482  48 8B 1F                        mov rbx, qword ptr [rdi]
00640485  EB 19                           jmp 0x1406404a0
00640487  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064048B  48 85 C0                        test rax, rax
0064048E  74 0D                           je 0x14064049d
00640490  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640494  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00640498  E8 33 A6 07 00                  call 0x1406baad0
0064049D  48 8B 1B                        mov rbx, qword ptr [rbx]
006404A0  48 3B DF                        cmp rbx, rdi
006404A3  75 E2                           jne 0x140640487
006404A5  45 84 F6                        test r14b, r14b
006404A8  74 0C                           je 0x1406404b6
006404AA  48 8D 0D CF 39 8C 00            lea rcx, [rip + 0x8c39cf]
006404B1  E8 CA 99 D0 FF                  call 0x140349e80
006404B6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006404BA  4D 8B CF                        mov r9, r15
006404BD  4D 8B C4                        mov r8, r12
006404C0  41 8B D5                        mov edx, r13d
006404C3  E8 08 E5 06 00                  call 0x1406ae9d0
006404C8  89 45 F8                        mov dword ptr [rbp - 8], eax
006404CB  48 85 F6                        test rsi, rsi
006404CE  74 63                           je 0x140640533
006404D0  40 32 FF                        xor dil, dil
006404D3  40 38 3D DE 43 8C 00            cmp byte ptr [rip + 0x8c43de], dil
006404DA  75 0C                           jne 0x1406404e8
006404DC  F7 05 9A 44 8C 00 00 08 00 00   test dword ptr [rip + 0x8c449a], 0x800
006404E6  74 13                           je 0x1406404fb
006404E8  48 8D 0D 91 39 8C 00            lea rcx, [rip + 0x8c3991]
006404EF  E8 2C 61 BD FF                  call 0x140216620
006404F4  40 8A F8                        mov dil, al
006404F7  84 C0                           test al, al
006404F9  74 38                           je 0x140640533
006404FB  48 83 C6 30                     add rsi, 0x30
006404FF  48 8B 1E                        mov rbx, qword ptr [rsi]
00640502  EB 19                           jmp 0x14064051d
00640504  48 8D 43 F0                     lea rax, [rbx - 0x10]
00640508  48 85 C0                        test rax, rax
0064050B  74 0D                           je 0x14064051a
0064050D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640511  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00640515  E8 B6 A5 07 00                  call 0x1406baad0
0064051A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064051D  48 3B DE                        cmp rbx, rsi
00640520  75 E2                           jne 0x140640504
00640522  40 84 FF                        test dil, dil
00640525  74 0C                           je 0x140640533
00640527  48 8D 0D 52 39 8C 00            lea rcx, [rip + 0x8c3952]
0064052E  E8 4D 99 D0 FF                  call 0x140349e80
00640533  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00640536  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064053B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064053F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00640543  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00640547  49 8B E3                        mov rsp, r11
0064054A  41 5F                           pop r15
0064054C  41 5E                           pop r14
0064054E  41 5D                           pop r13
00640550  41 5C                           pop r12
00640552  5D                              pop rbp
00640553  C3                              ret
00640554  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateSymbolicLinkObjectWrapper(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(118, a2, a3, a4);
    if (result == 0) goto loc_006404B6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00640432;
    v_stack_m58 = v_stack_p0;
    goto loc_0064043F;
loc_00640432:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9192555)) != 0) goto loc_0064046B;
    if (((*(unsigned int *)(v_rip + 9192727)) & (0x800ULL)) == 0) goto loc_0064047E;
loc_0064046B:
    result = ExAcquireRundownProtection(v_rip + 9189902, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006404B6;
loc_0064047E:
    goto loc_006404A0;
loc_00640487:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006404A0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00640487;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9189839;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCreateSymbolicLinkObject(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00640533;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9192414)) != 0) goto loc_006404E8;
    if (((*(unsigned int *)(v_rip + 9192602)) & (0x800ULL)) == 0) goto loc_006404FB;
loc_006404E8:
    result = ExAcquireRundownProtection(v_rip + 9189777, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00640533;
loc_006404FB:
    v_rsi = (result) + (48);
    goto loc_0064051D;
loc_00640504:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064051D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00640504;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9189714;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateSymbolicLinkObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(118, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006404B6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00640432;
    v_stack_m58 = v_stack_p0;
    goto loc_0064043F;
loc_00640432:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C446B)) != 0) goto loc_0064046B;
    if (((*(uint32_t *)(v_rip + 0x8C4517)) & (0x800ULL)) == 0) goto loc_0064047E;
loc_0064046B:
    result = ExAcquireRundownProtection(v_rip + 9189902, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006404B6;
loc_0064047E:
    goto loc_006404A0;
loc_00640487:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006404A0:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00640487;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9189839;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwCreateSymbolicLinkObject(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00640533;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C43DE)) != 0) goto loc_006404E8;
    if (((*(uint32_t *)(v_rip + 0x8C449A)) & (0x800ULL)) == 0) goto loc_006404FB;
loc_006404E8:
    result = ExAcquireRundownProtection(v_rip + 9189777, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00640533;
loc_006404FB:
    local_rsi = (result) + (48);
    goto loc_0064051D;
loc_00640504:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0064051D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00640504;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9189714;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006403D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006403D0[BB_006403D0]
  bb_00640421[BB_00640421]
  bb_00640428[BB_00640428]
  bb_00640432[BB_00640432]
  bb_00640436[BB_00640436]
  bb_0064043F[BB_0064043F]
  bb_0064045F[BB_0064045F]
  bb_0064046B[BB_0064046B]
  bb_0064047E[BB_0064047E]
  bb_00640487[BB_00640487]
  bb_00640490[BB_00640490]
  bb_0064049D[BB_0064049D]
  bb_006404A0[BB_006404A0]
  bb_006404A5[BB_006404A5]
  bb_006404AA[BB_006404AA]
  bb_006404B6[BB_006404B6]
  bb_006404D0[BB_006404D0]
  bb_006404DC[BB_006404DC]
  bb_006404E8[BB_006404E8]
  bb_006404FB[BB_006404FB]
  bb_00640504[BB_00640504]
  bb_0064050D[BB_0064050D]
  bb_0064051A[BB_0064051A]
  bb_0064051D[BB_0064051D]
  bb_00640522[BB_00640522]
  bb_00640527[BB_00640527]
  bb_00640533[BB_00640533]
  bb_00640554[BB_00640554]
  bb_006403D0 -->|branch| bb_006404B6
  bb_006403D0 -->|fallthrough| bb_00640421
  bb_00640421 -->|branch| bb_00640432
  bb_00640421 -->|fallthrough| bb_00640428
  bb_00640428 -->|branch| bb_0064043F
  bb_00640432 -->|branch| bb_0064043F
  bb_00640432 -->|fallthrough| bb_00640436
  bb_00640436 -->|flow| bb_0064043F
  bb_0064043F -->|branch| bb_0064046B
  bb_0064043F -->|fallthrough| bb_0064045F
  bb_0064045F -->|branch| bb_0064047E
  bb_0064045F -->|fallthrough| bb_0064046B
  bb_0064046B -->|branch| bb_006404B6
  bb_0064046B -->|fallthrough| bb_0064047E
  bb_0064047E -->|branch| bb_006404A0
  bb_00640487 -->|branch| bb_0064049D
  bb_00640487 -->|fallthrough| bb_00640490
  bb_00640490 -->|flow| bb_0064049D
  bb_0064049D -->|flow| bb_006404A0
  bb_006404A0 -->|branch| bb_00640487
  bb_006404A0 -->|fallthrough| bb_006404A5
  bb_006404A5 -->|branch| bb_006404B6
  bb_006404A5 -->|fallthrough| bb_006404AA
  bb_006404AA -->|flow| bb_006404B6
  bb_006404B6 -->|branch| bb_00640533
  bb_006404B6 -->|fallthrough| bb_006404D0
  bb_006404D0 -->|branch| bb_006404E8
  bb_006404D0 -->|fallthrough| bb_006404DC
  bb_006404DC -->|branch| bb_006404FB
  bb_006404DC -->|fallthrough| bb_006404E8
  bb_006404E8 -->|branch| bb_00640533
  bb_006404E8 -->|fallthrough| bb_006404FB
  bb_006404FB -->|branch| bb_0064051D
  bb_00640504 -->|branch| bb_0064051A
  bb_00640504 -->|fallthrough| bb_0064050D
  bb_0064050D -->|flow| bb_0064051A
  bb_0064051A -->|flow| bb_0064051D
  bb_0064051D -->|branch| bb_00640504
  bb_0064051D -->|fallthrough| bb_00640522
  bb_00640522 -->|branch| bb_00640533
  bb_00640522 -->|fallthrough| bb_00640527
  bb_00640527 -->|flow| bb_00640533
```
