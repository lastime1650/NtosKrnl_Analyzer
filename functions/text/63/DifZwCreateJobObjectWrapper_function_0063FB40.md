# DifZwCreateJobObjectWrapper

- RVA: `0x0063FB40`–`0x0063FCB5` (길이 `373` bytes)
- VA: `0x000000014063FB40`
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
- `0x0063FB7C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063FBA2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063FBD6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063FBFC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063FC15` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063FC23` → [ZwCreateJobObject](../6A/ZwCreateJobObject_function_006AE750.md) (function, `0x006AE750`)
- `0x0063FC4F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063FC75` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063FC8E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063FBB2` → RVA `0x00F048B8` (`.data`; read)
- `0x0063FBC3` → RVA `0x00F04980` (`.data`; read)
- `0x0063FBCF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063FB40  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063FB45  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063FB4A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063FB4F  55                              push rbp
0063FB50  41 54                           push r12
0063FB52  41 55                           push r13
0063FB54  41 56                           push r14
0063FB56  41 57                           push r15
0063FB58  48 8B EC                        mov rbp, rsp
0063FB5B  48 83 EC 50                     sub rsp, 0x50
0063FB5F  33 C0                           xor eax, eax
0063FB61  0F 57 C0                        xorps xmm0, xmm0
0063FB64  4C 8B E9                        mov r13, rcx
0063FB67  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063FB6B  4D 8B F8                        mov r15, r8
0063FB6E  44 8B E2                        mov r12d, edx
0063FB71  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063FB75  8D 48 7B                        lea ecx, [rax + 0x7b]
0063FB78  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063FB7C  E8 B3 5E E5 FF                  call 0x140495a34
0063FB81  48 8B F0                        mov rsi, rax
0063FB84  48 85 C0                        test rax, rax
0063FB87  0F 84 8D 00 00 00               je 0x14063fc1a
0063FB8D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063FB90  A8 18                           test al, 0x18
0063FB92  74 0A                           je 0x14063fb9e
0063FB94  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063FB98  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063FB9C  EB 0D                           jmp 0x14063fbab
0063FB9E  A8 04                           test al, 4
0063FBA0  74 09                           je 0x14063fbab
0063FBA2  E8 61 40 E9 FF                  call 0x1404d3c08
0063FBA7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063FBAB  45 32 F6                        xor r14b, r14b
0063FBAE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063FBB2  44 38 35 FF 4C 8C 00            cmp byte ptr [rip + 0x8c4cff], r14b
0063FBB9  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0063FBBD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0063FBC1  75 0C                           jne 0x14063fbcf
0063FBC3  F7 05 B3 4D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c4db3], 0x800
0063FBCD  74 13                           je 0x14063fbe2
0063FBCF  48 8D 0D AA 42 8C 00            lea rcx, [rip + 0x8c42aa]
0063FBD6  E8 45 6A BD FF                  call 0x140216620
0063FBDB  44 8A F0                        mov r14b, al
0063FBDE  84 C0                           test al, al
0063FBE0  74 38                           je 0x14063fc1a
0063FBE2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063FBE6  48 8B 1F                        mov rbx, qword ptr [rdi]
0063FBE9  EB 19                           jmp 0x14063fc04
0063FBEB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063FBEF  48 85 C0                        test rax, rax
0063FBF2  74 0D                           je 0x14063fc01
0063FBF4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063FBF8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063FBFC  E8 CF AE 07 00                  call 0x1406baad0
0063FC01  48 8B 1B                        mov rbx, qword ptr [rbx]
0063FC04  48 3B DF                        cmp rbx, rdi
0063FC07  75 E2                           jne 0x14063fbeb
0063FC09  45 84 F6                        test r14b, r14b
0063FC0C  74 0C                           je 0x14063fc1a
0063FC0E  48 8D 0D 6B 42 8C 00            lea rcx, [rip + 0x8c426b]
0063FC15  E8 66 A2 D0 FF                  call 0x140349e80
0063FC1A  4D 8B C7                        mov r8, r15
0063FC1D  41 8B D4                        mov edx, r12d
0063FC20  49 8B CD                        mov rcx, r13
0063FC23  E8 28 EB 06 00                  call 0x1406ae750
0063FC28  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063FC2B  48 85 F6                        test rsi, rsi
0063FC2E  74 63                           je 0x14063fc93
0063FC30  40 32 FF                        xor dil, dil
0063FC33  40 38 3D 7E 4C 8C 00            cmp byte ptr [rip + 0x8c4c7e], dil
0063FC3A  75 0C                           jne 0x14063fc48
0063FC3C  F7 05 3A 4D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c4d3a], 0x800
0063FC46  74 13                           je 0x14063fc5b
0063FC48  48 8D 0D 31 42 8C 00            lea rcx, [rip + 0x8c4231]
0063FC4F  E8 CC 69 BD FF                  call 0x140216620
0063FC54  40 8A F8                        mov dil, al
0063FC57  84 C0                           test al, al
0063FC59  74 38                           je 0x14063fc93
0063FC5B  48 83 C6 30                     add rsi, 0x30
0063FC5F  48 8B 1E                        mov rbx, qword ptr [rsi]
0063FC62  EB 19                           jmp 0x14063fc7d
0063FC64  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063FC68  48 85 C0                        test rax, rax
0063FC6B  74 0D                           je 0x14063fc7a
0063FC6D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063FC71  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063FC75  E8 56 AE 07 00                  call 0x1406baad0
0063FC7A  48 8B 1B                        mov rbx, qword ptr [rbx]
0063FC7D  48 3B DE                        cmp rbx, rsi
0063FC80  75 E2                           jne 0x14063fc64
0063FC82  40 84 FF                        test dil, dil
0063FC85  74 0C                           je 0x14063fc93
0063FC87  48 8D 0D F2 41 8C 00            lea rcx, [rip + 0x8c41f2]
0063FC8E  E8 ED A1 D0 FF                  call 0x140349e80
0063FC93  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063FC96  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063FC9B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063FC9F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063FCA3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063FCA7  49 8B E3                        mov rsp, r11
0063FCAA  41 5F                           pop r15
0063FCAC  41 5E                           pop r14
0063FCAE  41 5D                           pop r13
0063FCB0  41 5C                           pop r12
0063FCB2  5D                              pop rbp
0063FCB3  C3                              ret
0063FCB4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateJobObjectWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 123, a2, a3, a4);
    if (result == 0) goto loc_0063FC1A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063FB9E;
    v_stack_m58 = v_stack_p0;
    goto loc_0063FBAB;
loc_0063FB9E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9194751)) != 0) goto loc_0063FBCF;
    if (((*(unsigned int *)(v_rip + 9194931)) & (0x800ULL)) == 0) goto loc_0063FBE2;
loc_0063FBCF:
    result = ExAcquireRundownProtection(v_rip + 9192106, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063FC1A;
loc_0063FBE2:
    goto loc_0063FC04;
loc_0063FBEB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063FC04:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063FBEB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9192043;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwCreateJobObject(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063FC93;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9194622)) != 0) goto loc_0063FC48;
    if (((*(unsigned int *)(v_rip + 9194810)) & (0x800ULL)) == 0) goto loc_0063FC5B;
loc_0063FC48:
    result = ExAcquireRundownProtection(v_rip + 9191985, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063FC93;
loc_0063FC5B:
    v_rsi = (result) + (48);
    goto loc_0063FC7D;
loc_0063FC64:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0063FC7D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063FC64;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9191922;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateJobObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 123, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063FC1A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063FB9E;
    v_stack_m58 = v_stack_p0;
    goto loc_0063FBAB;
loc_0063FB9E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C4CFF)) != 0) goto loc_0063FBCF;
    if (((*(uint32_t *)(v_rip + 0x8C4DB3)) & (0x800ULL)) == 0) goto loc_0063FBE2;
loc_0063FBCF:
    result = ExAcquireRundownProtection(v_rip + 9192106, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063FC1A;
loc_0063FBE2:
    goto loc_0063FC04;
loc_0063FBEB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063FC04:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063FBEB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9192043;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwCreateJobObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063FC93;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C4C7E)) != 0) goto loc_0063FC48;
    if (((*(uint32_t *)(v_rip + 0x8C4D3A)) & (0x800ULL)) == 0) goto loc_0063FC5B;
loc_0063FC48:
    result = ExAcquireRundownProtection(v_rip + 9191985, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063FC93;
loc_0063FC5B:
    local_rsi = (result) + (48);
    goto loc_0063FC7D;
loc_0063FC64:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0063FC7D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063FC64;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9191922;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063FB40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063FB40[BB_0063FB40]
  bb_0063FB8D[BB_0063FB8D]
  bb_0063FB94[BB_0063FB94]
  bb_0063FB9E[BB_0063FB9E]
  bb_0063FBA2[BB_0063FBA2]
  bb_0063FBAB[BB_0063FBAB]
  bb_0063FBC3[BB_0063FBC3]
  bb_0063FBCF[BB_0063FBCF]
  bb_0063FBE2[BB_0063FBE2]
  bb_0063FBEB[BB_0063FBEB]
  bb_0063FBF4[BB_0063FBF4]
  bb_0063FC01[BB_0063FC01]
  bb_0063FC04[BB_0063FC04]
  bb_0063FC09[BB_0063FC09]
  bb_0063FC0E[BB_0063FC0E]
  bb_0063FC1A[BB_0063FC1A]
  bb_0063FC30[BB_0063FC30]
  bb_0063FC3C[BB_0063FC3C]
  bb_0063FC48[BB_0063FC48]
  bb_0063FC5B[BB_0063FC5B]
  bb_0063FC64[BB_0063FC64]
  bb_0063FC6D[BB_0063FC6D]
  bb_0063FC7A[BB_0063FC7A]
  bb_0063FC7D[BB_0063FC7D]
  bb_0063FC82[BB_0063FC82]
  bb_0063FC87[BB_0063FC87]
  bb_0063FC93[BB_0063FC93]
  bb_0063FCB4[BB_0063FCB4]
  bb_0063FB40 -->|branch| bb_0063FC1A
  bb_0063FB40 -->|fallthrough| bb_0063FB8D
  bb_0063FB8D -->|branch| bb_0063FB9E
  bb_0063FB8D -->|fallthrough| bb_0063FB94
  bb_0063FB94 -->|branch| bb_0063FBAB
  bb_0063FB9E -->|branch| bb_0063FBAB
  bb_0063FB9E -->|fallthrough| bb_0063FBA2
  bb_0063FBA2 -->|flow| bb_0063FBAB
  bb_0063FBAB -->|branch| bb_0063FBCF
  bb_0063FBAB -->|fallthrough| bb_0063FBC3
  bb_0063FBC3 -->|branch| bb_0063FBE2
  bb_0063FBC3 -->|fallthrough| bb_0063FBCF
  bb_0063FBCF -->|branch| bb_0063FC1A
  bb_0063FBCF -->|fallthrough| bb_0063FBE2
  bb_0063FBE2 -->|branch| bb_0063FC04
  bb_0063FBEB -->|branch| bb_0063FC01
  bb_0063FBEB -->|fallthrough| bb_0063FBF4
  bb_0063FBF4 -->|flow| bb_0063FC01
  bb_0063FC01 -->|flow| bb_0063FC04
  bb_0063FC04 -->|branch| bb_0063FBEB
  bb_0063FC04 -->|fallthrough| bb_0063FC09
  bb_0063FC09 -->|branch| bb_0063FC1A
  bb_0063FC09 -->|fallthrough| bb_0063FC0E
  bb_0063FC0E -->|flow| bb_0063FC1A
  bb_0063FC1A -->|branch| bb_0063FC93
  bb_0063FC1A -->|fallthrough| bb_0063FC30
  bb_0063FC30 -->|branch| bb_0063FC48
  bb_0063FC30 -->|fallthrough| bb_0063FC3C
  bb_0063FC3C -->|branch| bb_0063FC5B
  bb_0063FC3C -->|fallthrough| bb_0063FC48
  bb_0063FC48 -->|branch| bb_0063FC93
  bb_0063FC48 -->|fallthrough| bb_0063FC5B
  bb_0063FC5B -->|branch| bb_0063FC7D
  bb_0063FC64 -->|branch| bb_0063FC7A
  bb_0063FC64 -->|fallthrough| bb_0063FC6D
  bb_0063FC6D -->|flow| bb_0063FC7A
  bb_0063FC7A -->|flow| bb_0063FC7D
  bb_0063FC7D -->|branch| bb_0063FC64
  bb_0063FC7D -->|fallthrough| bb_0063FC82
  bb_0063FC82 -->|branch| bb_0063FC93
  bb_0063FC82 -->|fallthrough| bb_0063FC87
  bb_0063FC87 -->|flow| bb_0063FC93
```
