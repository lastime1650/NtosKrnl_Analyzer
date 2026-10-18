# DifIoAcquireRemoveLockExWrapper

- RVA: `0x00627200`–`0x00627392` (길이 `402` bytes)
- VA: `0x0000000140627200`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00627240` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00627266` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006272A8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006272CE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006272E7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00627300` → [IoAcquireRemoveLockEx](../43/IoAcquireRemoveLockEx_function_00433420.md) (function, `0x00433420`)
- `0x0062732C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00627352` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062736B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00627276` → RVA `0x00F048B8` (`.data`; read)
- `0x00627295` → RVA `0x00F04980` (`.data`; read)
- `0x006272A1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00627200  48 8B C4                        mov rax, rsp
00627203  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00627207  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062720B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062720F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00627213  55                              push rbp
00627214  41 54                           push r12
00627216  41 55                           push r13
00627218  41 56                           push r14
0062721A  41 57                           push r15
0062721C  48 8B EC                        mov rbp, rsp
0062721F  48 83 EC 60                     sub rsp, 0x60
00627223  0F 57 C0                        xorps xmm0, xmm0
00627226  B9 73 01 00 00                  mov ecx, 0x173
0062722B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0062722F  45 8B F9                        mov r15d, r9d
00627232  4D 8B E0                        mov r12, r8
00627235  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00627239  4C 8B EA                        mov r13, rdx
0062723C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00627240  E8 EF E7 E6 FF                  call 0x140495a34
00627245  48 8B F0                        mov rsi, rax
00627248  48 85 C0                        test rax, rax
0062724B  0F 84 9B 00 00 00               je 0x1406272ec
00627251  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00627254  A8 18                           test al, 0x18
00627256  74 0A                           je 0x140627262
00627258  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062725C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00627260  EB 0D                           jmp 0x14062726f
00627262  A8 04                           test al, 4
00627264  74 09                           je 0x14062726f
00627266  E8 9D C9 EA FF                  call 0x1404d3c08
0062726B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0062726F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00627273  45 32 F6                        xor r14b, r14b
00627276  44 38 35 3B D6 8D 00            cmp byte ptr [rip + 0x8dd63b], r14b
0062727D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00627281  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00627284  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00627287  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0062728B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0062728F  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
00627293  75 0C                           jne 0x1406272a1
00627295  F7 05 E1 D6 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd6e1], 0x800
0062729F  74 13                           je 0x1406272b4
006272A1  48 8D 0D D8 CB 8D 00            lea rcx, [rip + 0x8dcbd8]
006272A8  E8 73 F3 BE FF                  call 0x140216620
006272AD  44 8A F0                        mov r14b, al
006272B0  84 C0                           test al, al
006272B2  74 38                           je 0x1406272ec
006272B4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006272B8  48 8B 1F                        mov rbx, qword ptr [rdi]
006272BB  EB 19                           jmp 0x1406272d6
006272BD  48 8D 43 F0                     lea rax, [rbx - 0x10]
006272C1  48 85 C0                        test rax, rax
006272C4  74 0D                           je 0x1406272d3
006272C6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006272CA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006272CE  E8 FD 37 09 00                  call 0x1406baad0
006272D3  48 8B 1B                        mov rbx, qword ptr [rbx]
006272D6  48 3B DF                        cmp rbx, rdi
006272D9  75 E2                           jne 0x1406272bd
006272DB  45 84 F6                        test r14b, r14b
006272DE  74 0C                           je 0x1406272ec
006272E0  48 8D 0D 99 CB 8D 00            lea rcx, [rip + 0x8dcb99]
006272E7  E8 94 2B D2 FF                  call 0x140349e80
006272EC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006272EF  45 8B CF                        mov r9d, r15d
006272F2  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
006272F6  4D 8B C4                        mov r8, r12
006272F9  49 8B D5                        mov rdx, r13
006272FC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00627300  E8 1B C1 E0 FF                  call 0x140433420
00627305  89 45 F8                        mov dword ptr [rbp - 8], eax
00627308  48 85 F6                        test rsi, rsi
0062730B  74 63                           je 0x140627370
0062730D  40 32 FF                        xor dil, dil
00627310  40 38 3D A1 D5 8D 00            cmp byte ptr [rip + 0x8dd5a1], dil
00627317  75 0C                           jne 0x140627325
00627319  F7 05 5D D6 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd65d], 0x800
00627323  74 13                           je 0x140627338
00627325  48 8D 0D 54 CB 8D 00            lea rcx, [rip + 0x8dcb54]
0062732C  E8 EF F2 BE FF                  call 0x140216620
00627331  40 8A F8                        mov dil, al
00627334  84 C0                           test al, al
00627336  74 38                           je 0x140627370
00627338  48 83 C6 30                     add rsi, 0x30
0062733C  48 8B 1E                        mov rbx, qword ptr [rsi]
0062733F  EB 19                           jmp 0x14062735a
00627341  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627345  48 85 C0                        test rax, rax
00627348  74 0D                           je 0x140627357
0062734A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062734E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00627352  E8 79 37 09 00                  call 0x1406baad0
00627357  48 8B 1B                        mov rbx, qword ptr [rbx]
0062735A  48 3B DE                        cmp rbx, rsi
0062735D  75 E2                           jne 0x140627341
0062735F  40 84 FF                        test dil, dil
00627362  74 0C                           je 0x140627370
00627364  48 8D 0D 15 CB 8D 00            lea rcx, [rip + 0x8dcb15]
0062736B  E8 10 2B D2 FF                  call 0x140349e80
00627370  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00627373  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00627378  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0062737C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00627380  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00627384  49 8B E3                        mov rsp, r11
00627387  41 5F                           pop r15
00627389  41 5E                           pop r14
0062738B  41 5D                           pop r13
0062738D  41 5C                           pop r12
0062738F  5D                              pop rbp
00627390  C3                              ret
00627391  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoAcquireRemoveLockExWrapper(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(371, a2, a3, a4);
    if (result == 0) goto loc_006272EC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00627262;
    v_stack_m58 = v_stack_p0;
    goto loc_0062726F;
loc_00627262:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m4C = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9295419)) != 0) goto loc_006272A1;
    if (((*(unsigned int *)(v_rip + 9295585)) & (0x800ULL)) == 0) goto loc_006272B4;
loc_006272A1:
    result = ExAcquireRundownProtection(v_rip + 9292760, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006272EC;
loc_006272B4:
    goto loc_006272D6;
loc_006272BD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006272D6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006272BD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9292697;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = IoAcquireRemoveLockEx(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00627370;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9295265)) != 0) goto loc_00627325;
    if (((*(unsigned int *)(v_rip + 9295453)) & (0x800ULL)) == 0) goto loc_00627338;
loc_00627325:
    result = ExAcquireRundownProtection(v_rip + 9292628, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00627370;
loc_00627338:
    v_rsi = (result) + (48);
    goto loc_0062735A;
loc_00627341:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0062735A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00627341;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9292565;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoAcquireRemoveLockExWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(371, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_006272EC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00627262;
    v_stack_m58 = v_stack_p0;
    goto loc_0062726F;
loc_00627262:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8DD63B)) != 0) goto loc_006272A1;
    if (((*(uint32_t *)(v_rip + 0x8DD6E1)) & (0x800ULL)) == 0) goto loc_006272B4;
loc_006272A1:
    result = ExAcquireRundownProtection(v_rip + 9292760, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006272EC;
loc_006272B4:
    goto loc_006272D6;
loc_006272BD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_006272D6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006272BD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9292697;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = IoAcquireRemoveLockEx(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00627370;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DD5A1)) != 0) goto loc_00627325;
    if (((*(uint32_t *)(v_rip + 0x8DD65D)) & (0x800ULL)) == 0) goto loc_00627338;
loc_00627325:
    result = ExAcquireRundownProtection(v_rip + 9292628, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00627370;
loc_00627338:
    local_rsi = (result) + (48);
    goto loc_0062735A;
loc_00627341:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0062735A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00627341;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9292565;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00627200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00627200[BB_00627200]
  bb_00627251[BB_00627251]
  bb_00627258[BB_00627258]
  bb_00627262[BB_00627262]
  bb_00627266[BB_00627266]
  bb_0062726F[BB_0062726F]
  bb_00627295[BB_00627295]
  bb_006272A1[BB_006272A1]
  bb_006272B4[BB_006272B4]
  bb_006272BD[BB_006272BD]
  bb_006272C6[BB_006272C6]
  bb_006272D3[BB_006272D3]
  bb_006272D6[BB_006272D6]
  bb_006272DB[BB_006272DB]
  bb_006272E0[BB_006272E0]
  bb_006272EC[BB_006272EC]
  bb_0062730D[BB_0062730D]
  bb_00627319[BB_00627319]
  bb_00627325[BB_00627325]
  bb_00627338[BB_00627338]
  bb_00627341[BB_00627341]
  bb_0062734A[BB_0062734A]
  bb_00627357[BB_00627357]
  bb_0062735A[BB_0062735A]
  bb_0062735F[BB_0062735F]
  bb_00627364[BB_00627364]
  bb_00627370[BB_00627370]
  bb_00627391[BB_00627391]
  bb_00627200 -->|branch| bb_006272EC
  bb_00627200 -->|fallthrough| bb_00627251
  bb_00627251 -->|branch| bb_00627262
  bb_00627251 -->|fallthrough| bb_00627258
  bb_00627258 -->|branch| bb_0062726F
  bb_00627262 -->|branch| bb_0062726F
  bb_00627262 -->|fallthrough| bb_00627266
  bb_00627266 -->|flow| bb_0062726F
  bb_0062726F -->|branch| bb_006272A1
  bb_0062726F -->|fallthrough| bb_00627295
  bb_00627295 -->|branch| bb_006272B4
  bb_00627295 -->|fallthrough| bb_006272A1
  bb_006272A1 -->|branch| bb_006272EC
  bb_006272A1 -->|fallthrough| bb_006272B4
  bb_006272B4 -->|branch| bb_006272D6
  bb_006272BD -->|branch| bb_006272D3
  bb_006272BD -->|fallthrough| bb_006272C6
  bb_006272C6 -->|flow| bb_006272D3
  bb_006272D3 -->|flow| bb_006272D6
  bb_006272D6 -->|branch| bb_006272BD
  bb_006272D6 -->|fallthrough| bb_006272DB
  bb_006272DB -->|branch| bb_006272EC
  bb_006272DB -->|fallthrough| bb_006272E0
  bb_006272E0 -->|flow| bb_006272EC
  bb_006272EC -->|branch| bb_00627370
  bb_006272EC -->|fallthrough| bb_0062730D
  bb_0062730D -->|branch| bb_00627325
  bb_0062730D -->|fallthrough| bb_00627319
  bb_00627319 -->|branch| bb_00627338
  bb_00627319 -->|fallthrough| bb_00627325
  bb_00627325 -->|branch| bb_00627370
  bb_00627325 -->|fallthrough| bb_00627338
  bb_00627338 -->|branch| bb_0062735A
  bb_00627341 -->|branch| bb_00627357
  bb_00627341 -->|fallthrough| bb_0062734A
  bb_0062734A -->|flow| bb_00627357
  bb_00627357 -->|flow| bb_0062735A
  bb_0062735A -->|branch| bb_00627341
  bb_0062735A -->|fallthrough| bb_0062735F
  bb_0062735F -->|branch| bb_00627370
  bb_0062735F -->|fallthrough| bb_00627364
  bb_00627364 -->|flow| bb_00627370
```
