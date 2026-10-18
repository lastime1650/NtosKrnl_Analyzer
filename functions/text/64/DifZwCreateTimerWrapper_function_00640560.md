# DifZwCreateTimerWrapper

- RVA: `0x00640560`–`0x006406E5` (길이 `389` bytes)
- VA: `0x0000000140640560`
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
- `0x006405A0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006405C6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00640602` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00640628` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00640641` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00640653` → [ZwCreateTimer](../6A/ZwCreateTimer_function_006AEA30.md) (function, `0x006AEA30`)
- `0x0064067F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006406A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006406BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006405D6` → RVA `0x00F048B8` (`.data`; read)
- `0x006405EF` → RVA `0x00F04980` (`.data`; read)
- `0x006405FB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00640560  48 8B C4                        mov rax, rsp
00640563  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00640567  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064056B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064056F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00640573  55                              push rbp
00640574  41 54                           push r12
00640576  41 55                           push r13
00640578  41 56                           push r14
0064057A  41 57                           push r15
0064057C  48 8B EC                        mov rbp, rsp
0064057F  48 83 EC 50                     sub rsp, 0x50
00640583  0F 57 C0                        xorps xmm0, xmm0
00640586  B9 75 00 00 00                  mov ecx, 0x75
0064058B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064058F  45 8B F9                        mov r15d, r9d
00640592  4D 8B E0                        mov r12, r8
00640595  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00640599  44 8B EA                        mov r13d, edx
0064059C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
006405A0  E8 8F 54 E5 FF                  call 0x140495a34
006405A5  48 8B F0                        mov rsi, rax
006405A8  48 85 C0                        test rax, rax
006405AB  0F 84 95 00 00 00               je 0x140640646
006405B1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006405B4  A8 18                           test al, 0x18
006405B6  74 0A                           je 0x1406405c2
006405B8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006405BC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006405C0  EB 0D                           jmp 0x1406405cf
006405C2  A8 04                           test al, 4
006405C4  74 09                           je 0x1406405cf
006405C6  E8 3D 36 E9 FF                  call 0x1404d3c08
006405CB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006405CF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006405D3  45 32 F6                        xor r14b, r14b
006405D6  44 38 35 DB 42 8C 00            cmp byte ptr [rip + 0x8c42db], r14b
006405DD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006405E1  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
006405E5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
006405E9  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
006405ED  75 0C                           jne 0x1406405fb
006405EF  F7 05 87 43 8C 00 00 08 00 00   test dword ptr [rip + 0x8c4387], 0x800
006405F9  74 13                           je 0x14064060e
006405FB  48 8D 0D 7E 38 8C 00            lea rcx, [rip + 0x8c387e]
00640602  E8 19 60 BD FF                  call 0x140216620
00640607  44 8A F0                        mov r14b, al
0064060A  84 C0                           test al, al
0064060C  74 38                           je 0x140640646
0064060E  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00640612  48 8B 1F                        mov rbx, qword ptr [rdi]
00640615  EB 19                           jmp 0x140640630
00640617  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064061B  48 85 C0                        test rax, rax
0064061E  74 0D                           je 0x14064062d
00640620  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00640624  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00640628  E8 A3 A4 07 00                  call 0x1406baad0
0064062D  48 8B 1B                        mov rbx, qword ptr [rbx]
00640630  48 3B DF                        cmp rbx, rdi
00640633  75 E2                           jne 0x140640617
00640635  45 84 F6                        test r14b, r14b
00640638  74 0C                           je 0x140640646
0064063A  48 8D 0D 3F 38 8C 00            lea rcx, [rip + 0x8c383f]
00640641  E8 3A 98 D0 FF                  call 0x140349e80
00640646  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064064A  45 8B CF                        mov r9d, r15d
0064064D  4D 8B C4                        mov r8, r12
00640650  41 8B D5                        mov edx, r13d
00640653  E8 D8 E3 06 00                  call 0x1406aea30
00640658  89 45 F8                        mov dword ptr [rbp - 8], eax
0064065B  48 85 F6                        test rsi, rsi
0064065E  74 63                           je 0x1406406c3
00640660  40 32 FF                        xor dil, dil
00640663  40 38 3D 4E 42 8C 00            cmp byte ptr [rip + 0x8c424e], dil
0064066A  75 0C                           jne 0x140640678
0064066C  F7 05 0A 43 8C 00 00 08 00 00   test dword ptr [rip + 0x8c430a], 0x800
00640676  74 13                           je 0x14064068b
00640678  48 8D 0D 01 38 8C 00            lea rcx, [rip + 0x8c3801]
0064067F  E8 9C 5F BD FF                  call 0x140216620
00640684  40 8A F8                        mov dil, al
00640687  84 C0                           test al, al
00640689  74 38                           je 0x1406406c3
0064068B  48 83 C6 30                     add rsi, 0x30
0064068F  48 8B 1E                        mov rbx, qword ptr [rsi]
00640692  EB 19                           jmp 0x1406406ad
00640694  48 8D 43 F0                     lea rax, [rbx - 0x10]
00640698  48 85 C0                        test rax, rax
0064069B  74 0D                           je 0x1406406aa
0064069D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006406A1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006406A5  E8 26 A4 07 00                  call 0x1406baad0
006406AA  48 8B 1B                        mov rbx, qword ptr [rbx]
006406AD  48 3B DE                        cmp rbx, rsi
006406B0  75 E2                           jne 0x140640694
006406B2  40 84 FF                        test dil, dil
006406B5  74 0C                           je 0x1406406c3
006406B7  48 8D 0D C2 37 8C 00            lea rcx, [rip + 0x8c37c2]
006406BE  E8 BD 97 D0 FF                  call 0x140349e80
006406C3  8B 45 F8                        mov eax, dword ptr [rbp - 8]
006406C6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006406CB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006406CF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006406D3  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006406D7  49 8B E3                        mov rsp, r11
006406DA  41 5F                           pop r15
006406DC  41 5E                           pop r14
006406DE  41 5D                           pop r13
006406E0  41 5C                           pop r12
006406E2  5D                              pop rbp
006406E3  C3                              ret
006406E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateTimerWrapper(__int64 a1, int a2, __int64 a3, int a4)
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
    unsigned int v_stack_m50;
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
    result = DifGetAPIThunkContextById(117, a2, a3, a4);
    if (result == 0) goto loc_00640646;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006405C2;
    v_stack_m58 = v_stack_p0;
    goto loc_006405CF;
loc_006405C2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9192155)) != 0) goto loc_006405FB;
    if (((*(unsigned int *)(v_rip + 9192327)) & (0x800ULL)) == 0) goto loc_0064060E;
loc_006405FB:
    result = ExAcquireRundownProtection(v_rip + 9189502, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00640646;
loc_0064060E:
    goto loc_00640630;
loc_00640617:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00640630:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00640617;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9189439;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCreateTimer(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_006406C3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9192014)) != 0) goto loc_00640678;
    if (((*(unsigned int *)(v_rip + 9192202)) & (0x800ULL)) == 0) goto loc_0064068B;
loc_00640678:
    result = ExAcquireRundownProtection(v_rip + 9189377, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_006406C3;
loc_0064068B:
    v_rsi = (result) + (48);
    goto loc_006406AD;
loc_00640694:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_006406AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00640694;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9189314;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateTimerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
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
    uint32_t v_stack_m50;
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
    result = DifGetAPIThunkContextById(117, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00640646;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006405C2;
    v_stack_m58 = v_stack_p0;
    goto loc_006405CF;
loc_006405C2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8C42DB)) != 0) goto loc_006405FB;
    if (((*(uint32_t *)(v_rip + 0x8C4387)) & (0x800ULL)) == 0) goto loc_0064060E;
loc_006405FB:
    result = ExAcquireRundownProtection(v_rip + 9189502, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00640646;
loc_0064060E:
    goto loc_00640630;
loc_00640617:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00640630:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00640617;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9189439;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwCreateTimer(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_006406C3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C424E)) != 0) goto loc_00640678;
    if (((*(uint32_t *)(v_rip + 0x8C430A)) & (0x800ULL)) == 0) goto loc_0064068B;
loc_00640678:
    result = ExAcquireRundownProtection(v_rip + 9189377, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_006406C3;
loc_0064068B:
    local_rsi = (result) + (48);
    goto loc_006406AD;
loc_00640694:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_006406AD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00640694;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9189314;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00640560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00640560[BB_00640560]
  bb_006405B1[BB_006405B1]
  bb_006405B8[BB_006405B8]
  bb_006405C2[BB_006405C2]
  bb_006405C6[BB_006405C6]
  bb_006405CF[BB_006405CF]
  bb_006405EF[BB_006405EF]
  bb_006405FB[BB_006405FB]
  bb_0064060E[BB_0064060E]
  bb_00640617[BB_00640617]
  bb_00640620[BB_00640620]
  bb_0064062D[BB_0064062D]
  bb_00640630[BB_00640630]
  bb_00640635[BB_00640635]
  bb_0064063A[BB_0064063A]
  bb_00640646[BB_00640646]
  bb_00640660[BB_00640660]
  bb_0064066C[BB_0064066C]
  bb_00640678[BB_00640678]
  bb_0064068B[BB_0064068B]
  bb_00640694[BB_00640694]
  bb_0064069D[BB_0064069D]
  bb_006406AA[BB_006406AA]
  bb_006406AD[BB_006406AD]
  bb_006406B2[BB_006406B2]
  bb_006406B7[BB_006406B7]
  bb_006406C3[BB_006406C3]
  bb_006406E4[BB_006406E4]
  bb_00640560 -->|branch| bb_00640646
  bb_00640560 -->|fallthrough| bb_006405B1
  bb_006405B1 -->|branch| bb_006405C2
  bb_006405B1 -->|fallthrough| bb_006405B8
  bb_006405B8 -->|branch| bb_006405CF
  bb_006405C2 -->|branch| bb_006405CF
  bb_006405C2 -->|fallthrough| bb_006405C6
  bb_006405C6 -->|flow| bb_006405CF
  bb_006405CF -->|branch| bb_006405FB
  bb_006405CF -->|fallthrough| bb_006405EF
  bb_006405EF -->|branch| bb_0064060E
  bb_006405EF -->|fallthrough| bb_006405FB
  bb_006405FB -->|branch| bb_00640646
  bb_006405FB -->|fallthrough| bb_0064060E
  bb_0064060E -->|branch| bb_00640630
  bb_00640617 -->|branch| bb_0064062D
  bb_00640617 -->|fallthrough| bb_00640620
  bb_00640620 -->|flow| bb_0064062D
  bb_0064062D -->|flow| bb_00640630
  bb_00640630 -->|branch| bb_00640617
  bb_00640630 -->|fallthrough| bb_00640635
  bb_00640635 -->|branch| bb_00640646
  bb_00640635 -->|fallthrough| bb_0064063A
  bb_0064063A -->|flow| bb_00640646
  bb_00640646 -->|branch| bb_006406C3
  bb_00640646 -->|fallthrough| bb_00640660
  bb_00640660 -->|branch| bb_00640678
  bb_00640660 -->|fallthrough| bb_0064066C
  bb_0064066C -->|branch| bb_0064068B
  bb_0064066C -->|fallthrough| bb_00640678
  bb_00640678 -->|branch| bb_006406C3
  bb_00640678 -->|fallthrough| bb_0064068B
  bb_0064068B -->|branch| bb_006406AD
  bb_00640694 -->|branch| bb_006406AA
  bb_00640694 -->|fallthrough| bb_0064069D
  bb_0064069D -->|flow| bb_006406AA
  bb_006406AA -->|flow| bb_006406AD
  bb_006406AD -->|branch| bb_00640694
  bb_006406AD -->|fallthrough| bb_006406B2
  bb_006406B2 -->|branch| bb_006406C3
  bb_006406B2 -->|fallthrough| bb_006406B7
  bb_006406B7 -->|flow| bb_006406C3
```
