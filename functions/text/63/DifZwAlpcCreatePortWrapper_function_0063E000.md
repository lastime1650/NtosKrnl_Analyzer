# DifZwAlpcCreatePortWrapper

- RVA: `0x0063E000`–`0x0063E177` (길이 `375` bytes)
- VA: `0x000000014063E000`
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
- `0x0063E03E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063E064` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063E098` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063E0BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063E0D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063E0E5` → [ZwAlpcCreatePort](../6A/ZwAlpcCreatePort_function_006AE070.md) (function, `0x006AE070`)
- `0x0063E111` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063E137` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063E150` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063E074` → RVA `0x00F048B8` (`.data`; read)
- `0x0063E085` → RVA `0x00F04980` (`.data`; read)
- `0x0063E091` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063E000  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063E005  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063E00A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063E00F  55                              push rbp
0063E010  41 54                           push r12
0063E012  41 55                           push r13
0063E014  41 56                           push r14
0063E016  41 57                           push r15
0063E018  48 8B EC                        mov rbp, rsp
0063E01B  48 83 EC 50                     sub rsp, 0x50
0063E01F  0F 57 C0                        xorps xmm0, xmm0
0063E022  33 C0                           xor eax, eax
0063E024  4C 8B E9                        mov r13, rcx
0063E027  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063E02B  B9 8D 00 00 00                  mov ecx, 0x8d
0063E030  4D 8B F8                        mov r15, r8
0063E033  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063E037  4C 8B E2                        mov r12, rdx
0063E03A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063E03E  E8 F1 79 E5 FF                  call 0x140495a34
0063E043  48 8B F0                        mov rsi, rax
0063E046  48 85 C0                        test rax, rax
0063E049  0F 84 8D 00 00 00               je 0x14063e0dc
0063E04F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063E052  A8 18                           test al, 0x18
0063E054  74 0A                           je 0x14063e060
0063E056  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063E05A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063E05E  EB 0D                           jmp 0x14063e06d
0063E060  A8 04                           test al, 4
0063E062  74 09                           je 0x14063e06d
0063E064  E8 9F 5B E9 FF                  call 0x1404d3c08
0063E069  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063E06D  45 32 F6                        xor r14b, r14b
0063E070  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063E074  44 38 35 3D 68 8C 00            cmp byte ptr [rip + 0x8c683d], r14b
0063E07B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063E07F  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0063E083  75 0C                           jne 0x14063e091
0063E085  F7 05 F1 68 8C 00 00 08 00 00   test dword ptr [rip + 0x8c68f1], 0x800
0063E08F  74 13                           je 0x14063e0a4
0063E091  48 8D 0D E8 5D 8C 00            lea rcx, [rip + 0x8c5de8]
0063E098  E8 83 85 BD FF                  call 0x140216620
0063E09D  44 8A F0                        mov r14b, al
0063E0A0  84 C0                           test al, al
0063E0A2  74 38                           je 0x14063e0dc
0063E0A4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063E0A8  48 8B 1F                        mov rbx, qword ptr [rdi]
0063E0AB  EB 19                           jmp 0x14063e0c6
0063E0AD  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063E0B1  48 85 C0                        test rax, rax
0063E0B4  74 0D                           je 0x14063e0c3
0063E0B6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063E0BA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063E0BE  E8 0D CA 07 00                  call 0x1406baad0
0063E0C3  48 8B 1B                        mov rbx, qword ptr [rbx]
0063E0C6  48 3B DF                        cmp rbx, rdi
0063E0C9  75 E2                           jne 0x14063e0ad
0063E0CB  45 84 F6                        test r14b, r14b
0063E0CE  74 0C                           je 0x14063e0dc
0063E0D0  48 8D 0D A9 5D 8C 00            lea rcx, [rip + 0x8c5da9]
0063E0D7  E8 A4 BD D0 FF                  call 0x140349e80
0063E0DC  4D 8B C7                        mov r8, r15
0063E0DF  49 8B D4                        mov rdx, r12
0063E0E2  49 8B CD                        mov rcx, r13
0063E0E5  E8 86 FF 06 00                  call 0x1406ae070
0063E0EA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063E0ED  48 85 F6                        test rsi, rsi
0063E0F0  74 63                           je 0x14063e155
0063E0F2  40 32 FF                        xor dil, dil
0063E0F5  40 38 3D BC 67 8C 00            cmp byte ptr [rip + 0x8c67bc], dil
0063E0FC  75 0C                           jne 0x14063e10a
0063E0FE  F7 05 78 68 8C 00 00 08 00 00   test dword ptr [rip + 0x8c6878], 0x800
0063E108  74 13                           je 0x14063e11d
0063E10A  48 8D 0D 6F 5D 8C 00            lea rcx, [rip + 0x8c5d6f]
0063E111  E8 0A 85 BD FF                  call 0x140216620
0063E116  40 8A F8                        mov dil, al
0063E119  84 C0                           test al, al
0063E11B  74 38                           je 0x14063e155
0063E11D  48 83 C6 30                     add rsi, 0x30
0063E121  48 8B 1E                        mov rbx, qword ptr [rsi]
0063E124  EB 19                           jmp 0x14063e13f
0063E126  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063E12A  48 85 C0                        test rax, rax
0063E12D  74 0D                           je 0x14063e13c
0063E12F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063E133  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063E137  E8 94 C9 07 00                  call 0x1406baad0
0063E13C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063E13F  48 3B DE                        cmp rbx, rsi
0063E142  75 E2                           jne 0x14063e126
0063E144  40 84 FF                        test dil, dil
0063E147  74 0C                           je 0x14063e155
0063E149  48 8D 0D 30 5D 8C 00            lea rcx, [rip + 0x8c5d30]
0063E150  E8 2B BD D0 FF                  call 0x140349e80
0063E155  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063E158  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063E15D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063E161  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063E165  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063E169  49 8B E3                        mov rsp, r11
0063E16C  41 5F                           pop r15
0063E16E  41 5E                           pop r14
0063E170  41 5D                           pop r13
0063E172  41 5C                           pop r12
0063E174  5D                              pop rbp
0063E175  C3                              ret
0063E176  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwAlpcCreatePortWrapper(__int64 a1, __int64 a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(141, a2, a3, a4);
    if (result == 0) goto loc_0063E0DC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063E060;
    v_stack_m58 = v_stack_p0;
    goto loc_0063E06D;
loc_0063E060:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9201725)) != 0) goto loc_0063E091;
    if (((*(unsigned int *)(v_rip + 9201905)) & (0x800ULL)) == 0) goto loc_0063E0A4;
loc_0063E091:
    result = ExAcquireRundownProtection(v_rip + 9199080, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063E0DC;
loc_0063E0A4:
    goto loc_0063E0C6;
loc_0063E0AD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063E0C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063E0AD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9199017;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwAlpcCreatePort(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063E155;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9201596)) != 0) goto loc_0063E10A;
    if (((*(unsigned int *)(v_rip + 9201784)) & (0x800ULL)) == 0) goto loc_0063E11D;
loc_0063E10A:
    result = ExAcquireRundownProtection(v_rip + 9198959, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063E155;
loc_0063E11D:
    v_rsi = (result) + (48);
    goto loc_0063E13F;
loc_0063E126:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063E13F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063E126;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9198896;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwAlpcCreatePortWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(141, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063E0DC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063E060;
    v_stack_m58 = v_stack_p0;
    goto loc_0063E06D;
loc_0063E060:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C683D)) != 0) goto loc_0063E091;
    if (((*(uint32_t *)(v_rip + 0x8C68F1)) & (0x800ULL)) == 0) goto loc_0063E0A4;
loc_0063E091:
    result = ExAcquireRundownProtection(v_rip + 9199080, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063E0DC;
loc_0063E0A4:
    goto loc_0063E0C6;
loc_0063E0AD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063E0C6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063E0AD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9199017;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwAlpcCreatePort(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063E155;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C67BC)) != 0) goto loc_0063E10A;
    if (((*(uint32_t *)(v_rip + 0x8C6878)) & (0x800ULL)) == 0) goto loc_0063E11D;
loc_0063E10A:
    result = ExAcquireRundownProtection(v_rip + 9198959, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063E155;
loc_0063E11D:
    local_rsi = (result) + (48);
    goto loc_0063E13F;
loc_0063E126:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063E13F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063E126;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9198896;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063E000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063E000[BB_0063E000]
  bb_0063E04F[BB_0063E04F]
  bb_0063E056[BB_0063E056]
  bb_0063E060[BB_0063E060]
  bb_0063E064[BB_0063E064]
  bb_0063E06D[BB_0063E06D]
  bb_0063E085[BB_0063E085]
  bb_0063E091[BB_0063E091]
  bb_0063E0A4[BB_0063E0A4]
  bb_0063E0AD[BB_0063E0AD]
  bb_0063E0B6[BB_0063E0B6]
  bb_0063E0C3[BB_0063E0C3]
  bb_0063E0C6[BB_0063E0C6]
  bb_0063E0CB[BB_0063E0CB]
  bb_0063E0D0[BB_0063E0D0]
  bb_0063E0DC[BB_0063E0DC]
  bb_0063E0F2[BB_0063E0F2]
  bb_0063E0FE[BB_0063E0FE]
  bb_0063E10A[BB_0063E10A]
  bb_0063E11D[BB_0063E11D]
  bb_0063E126[BB_0063E126]
  bb_0063E12F[BB_0063E12F]
  bb_0063E13C[BB_0063E13C]
  bb_0063E13F[BB_0063E13F]
  bb_0063E144[BB_0063E144]
  bb_0063E149[BB_0063E149]
  bb_0063E155[BB_0063E155]
  bb_0063E176[BB_0063E176]
  bb_0063E000 -->|branch| bb_0063E0DC
  bb_0063E000 -->|fallthrough| bb_0063E04F
  bb_0063E04F -->|branch| bb_0063E060
  bb_0063E04F -->|fallthrough| bb_0063E056
  bb_0063E056 -->|branch| bb_0063E06D
  bb_0063E060 -->|branch| bb_0063E06D
  bb_0063E060 -->|fallthrough| bb_0063E064
  bb_0063E064 -->|flow| bb_0063E06D
  bb_0063E06D -->|branch| bb_0063E091
  bb_0063E06D -->|fallthrough| bb_0063E085
  bb_0063E085 -->|branch| bb_0063E0A4
  bb_0063E085 -->|fallthrough| bb_0063E091
  bb_0063E091 -->|branch| bb_0063E0DC
  bb_0063E091 -->|fallthrough| bb_0063E0A4
  bb_0063E0A4 -->|branch| bb_0063E0C6
  bb_0063E0AD -->|branch| bb_0063E0C3
  bb_0063E0AD -->|fallthrough| bb_0063E0B6
  bb_0063E0B6 -->|flow| bb_0063E0C3
  bb_0063E0C3 -->|flow| bb_0063E0C6
  bb_0063E0C6 -->|branch| bb_0063E0AD
  bb_0063E0C6 -->|fallthrough| bb_0063E0CB
  bb_0063E0CB -->|branch| bb_0063E0DC
  bb_0063E0CB -->|fallthrough| bb_0063E0D0
  bb_0063E0D0 -->|flow| bb_0063E0DC
  bb_0063E0DC -->|branch| bb_0063E155
  bb_0063E0DC -->|fallthrough| bb_0063E0F2
  bb_0063E0F2 -->|branch| bb_0063E10A
  bb_0063E0F2 -->|fallthrough| bb_0063E0FE
  bb_0063E0FE -->|branch| bb_0063E11D
  bb_0063E0FE -->|fallthrough| bb_0063E10A
  bb_0063E10A -->|branch| bb_0063E155
  bb_0063E10A -->|fallthrough| bb_0063E11D
  bb_0063E11D -->|branch| bb_0063E13F
  bb_0063E126 -->|branch| bb_0063E13C
  bb_0063E126 -->|fallthrough| bb_0063E12F
  bb_0063E12F -->|flow| bb_0063E13C
  bb_0063E13C -->|flow| bb_0063E13F
  bb_0063E13F -->|branch| bb_0063E126
  bb_0063E13F -->|fallthrough| bb_0063E144
  bb_0063E144 -->|branch| bb_0063E155
  bb_0063E144 -->|fallthrough| bb_0063E149
  bb_0063E149 -->|flow| bb_0063E155
```
