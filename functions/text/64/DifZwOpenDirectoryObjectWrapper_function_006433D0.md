# DifZwOpenDirectoryObjectWrapper

- RVA: `0x006433D0`–`0x00643545` (길이 `373` bytes)
- VA: `0x00000001406433D0`
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
- `0x0064340C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00643432` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00643466` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064348C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006434A5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006434B3` → [ZwOpenDirectoryObject](../6A/ZwOpenDirectoryObject_function_006ADBD0.md) (function, `0x006ADBD0`)
- `0x006434DF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00643505` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064351E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00643442` → RVA `0x00F048B8` (`.data`; read)
- `0x00643453` → RVA `0x00F04980` (`.data`; read)
- `0x0064345F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006433D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006433D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
006433DA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
006433DF  55                              push rbp
006433E0  41 54                           push r12
006433E2  41 55                           push r13
006433E4  41 56                           push r14
006433E6  41 57                           push r15
006433E8  48 8B EC                        mov rbp, rsp
006433EB  48 83 EC 50                     sub rsp, 0x50
006433EF  33 C0                           xor eax, eax
006433F1  0F 57 C0                        xorps xmm0, xmm0
006433F4  4C 8B E9                        mov r13, rcx
006433F7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006433FB  4D 8B F8                        mov r15, r8
006433FE  44 8B E2                        mov r12d, edx
00643401  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00643405  8D 48 58                        lea ecx, [rax + 0x58]
00643408  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064340C  E8 23 26 E5 FF                  call 0x140495a34
00643411  48 8B F0                        mov rsi, rax
00643414  48 85 C0                        test rax, rax
00643417  0F 84 8D 00 00 00               je 0x1406434aa
0064341D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00643420  A8 18                           test al, 0x18
00643422  74 0A                           je 0x14064342e
00643424  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00643428  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064342C  EB 0D                           jmp 0x14064343b
0064342E  A8 04                           test al, 4
00643430  74 09                           je 0x14064343b
00643432  E8 D1 07 E9 FF                  call 0x1404d3c08
00643437  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064343B  45 32 F6                        xor r14b, r14b
0064343E  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00643442  44 38 35 6F 14 8C 00            cmp byte ptr [rip + 0x8c146f], r14b
00643449  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0064344D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00643451  75 0C                           jne 0x14064345f
00643453  F7 05 23 15 8C 00 00 08 00 00   test dword ptr [rip + 0x8c1523], 0x800
0064345D  74 13                           je 0x140643472
0064345F  48 8D 0D 1A 0A 8C 00            lea rcx, [rip + 0x8c0a1a]
00643466  E8 B5 31 BD FF                  call 0x140216620
0064346B  44 8A F0                        mov r14b, al
0064346E  84 C0                           test al, al
00643470  74 38                           je 0x1406434aa
00643472  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00643476  48 8B 1F                        mov rbx, qword ptr [rdi]
00643479  EB 19                           jmp 0x140643494
0064347B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064347F  48 85 C0                        test rax, rax
00643482  74 0D                           je 0x140643491
00643484  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00643488  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064348C  E8 3F 76 07 00                  call 0x1406baad0
00643491  48 8B 1B                        mov rbx, qword ptr [rbx]
00643494  48 3B DF                        cmp rbx, rdi
00643497  75 E2                           jne 0x14064347b
00643499  45 84 F6                        test r14b, r14b
0064349C  74 0C                           je 0x1406434aa
0064349E  48 8D 0D DB 09 8C 00            lea rcx, [rip + 0x8c09db]
006434A5  E8 D6 69 D0 FF                  call 0x140349e80
006434AA  4D 8B C7                        mov r8, r15
006434AD  41 8B D4                        mov edx, r12d
006434B0  49 8B CD                        mov rcx, r13
006434B3  E8 18 A7 06 00                  call 0x1406adbd0
006434B8  89 45 F0                        mov dword ptr [rbp - 0x10], eax
006434BB  48 85 F6                        test rsi, rsi
006434BE  74 63                           je 0x140643523
006434C0  40 32 FF                        xor dil, dil
006434C3  40 38 3D EE 13 8C 00            cmp byte ptr [rip + 0x8c13ee], dil
006434CA  75 0C                           jne 0x1406434d8
006434CC  F7 05 AA 14 8C 00 00 08 00 00   test dword ptr [rip + 0x8c14aa], 0x800
006434D6  74 13                           je 0x1406434eb
006434D8  48 8D 0D A1 09 8C 00            lea rcx, [rip + 0x8c09a1]
006434DF  E8 3C 31 BD FF                  call 0x140216620
006434E4  40 8A F8                        mov dil, al
006434E7  84 C0                           test al, al
006434E9  74 38                           je 0x140643523
006434EB  48 83 C6 30                     add rsi, 0x30
006434EF  48 8B 1E                        mov rbx, qword ptr [rsi]
006434F2  EB 19                           jmp 0x14064350d
006434F4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006434F8  48 85 C0                        test rax, rax
006434FB  74 0D                           je 0x14064350a
006434FD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00643501  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00643505  E8 C6 75 07 00                  call 0x1406baad0
0064350A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064350D  48 3B DE                        cmp rbx, rsi
00643510  75 E2                           jne 0x1406434f4
00643512  40 84 FF                        test dil, dil
00643515  74 0C                           je 0x140643523
00643517  48 8D 0D 62 09 8C 00            lea rcx, [rip + 0x8c0962]
0064351E  E8 5D 69 D0 FF                  call 0x140349e80
00643523  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00643526  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064352B  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0064352F  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00643533  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00643537  49 8B E3                        mov rsp, r11
0064353A  41 5F                           pop r15
0064353C  41 5E                           pop r14
0064353E  41 5D                           pop r13
00643540  41 5C                           pop r12
00643542  5D                              pop rbp
00643543  C3                              ret
00643544  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenDirectoryObjectWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 88, a2, a3, a4);
    if (result == 0) goto loc_006434AA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064342E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064343B;
loc_0064342E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9180271)) != 0) goto loc_0064345F;
    if (((*(unsigned int *)(v_rip + 9180451)) & (0x800ULL)) == 0) goto loc_00643472;
loc_0064345F:
    result = ExAcquireRundownProtection(v_rip + 9177626, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006434AA;
loc_00643472:
    goto loc_00643494;
loc_0064347B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00643494:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064347B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9177563;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenDirectoryObject(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00643523;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9180142)) != 0) goto loc_006434D8;
    if (((*(unsigned int *)(v_rip + 9180330)) & (0x800ULL)) == 0) goto loc_006434EB;
loc_006434D8:
    result = ExAcquireRundownProtection(v_rip + 9177505, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00643523;
loc_006434EB:
    v_rsi = (result) + (48);
    goto loc_0064350D;
loc_006434F4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064350D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006434F4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9177442;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenDirectoryObjectWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 88, Arg2, Arg3, a4);
    if (result == 0) goto loc_006434AA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064342E;
    v_stack_m58 = v_stack_p0;
    goto loc_0064343B;
loc_0064342E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C146F)) != 0) goto loc_0064345F;
    if (((*(uint32_t *)(v_rip + 0x8C1523)) & (0x800ULL)) == 0) goto loc_00643472;
loc_0064345F:
    result = ExAcquireRundownProtection(v_rip + 9177626, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006434AA;
loc_00643472:
    goto loc_00643494;
loc_0064347B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00643494:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064347B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9177563;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenDirectoryObject(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00643523;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C13EE)) != 0) goto loc_006434D8;
    if (((*(uint32_t *)(v_rip + 0x8C14AA)) & (0x800ULL)) == 0) goto loc_006434EB;
loc_006434D8:
    result = ExAcquireRundownProtection(v_rip + 9177505, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00643523;
loc_006434EB:
    local_rsi = (result) + (48);
    goto loc_0064350D;
loc_006434F4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0064350D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006434F4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9177442;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006433D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006433D0[BB_006433D0]
  bb_0064341D[BB_0064341D]
  bb_00643424[BB_00643424]
  bb_0064342E[BB_0064342E]
  bb_00643432[BB_00643432]
  bb_0064343B[BB_0064343B]
  bb_00643453[BB_00643453]
  bb_0064345F[BB_0064345F]
  bb_00643472[BB_00643472]
  bb_0064347B[BB_0064347B]
  bb_00643484[BB_00643484]
  bb_00643491[BB_00643491]
  bb_00643494[BB_00643494]
  bb_00643499[BB_00643499]
  bb_0064349E[BB_0064349E]
  bb_006434AA[BB_006434AA]
  bb_006434C0[BB_006434C0]
  bb_006434CC[BB_006434CC]
  bb_006434D8[BB_006434D8]
  bb_006434EB[BB_006434EB]
  bb_006434F4[BB_006434F4]
  bb_006434FD[BB_006434FD]
  bb_0064350A[BB_0064350A]
  bb_0064350D[BB_0064350D]
  bb_00643512[BB_00643512]
  bb_00643517[BB_00643517]
  bb_00643523[BB_00643523]
  bb_00643544[BB_00643544]
  bb_006433D0 -->|branch| bb_006434AA
  bb_006433D0 -->|fallthrough| bb_0064341D
  bb_0064341D -->|branch| bb_0064342E
  bb_0064341D -->|fallthrough| bb_00643424
  bb_00643424 -->|branch| bb_0064343B
  bb_0064342E -->|branch| bb_0064343B
  bb_0064342E -->|fallthrough| bb_00643432
  bb_00643432 -->|flow| bb_0064343B
  bb_0064343B -->|branch| bb_0064345F
  bb_0064343B -->|fallthrough| bb_00643453
  bb_00643453 -->|branch| bb_00643472
  bb_00643453 -->|fallthrough| bb_0064345F
  bb_0064345F -->|branch| bb_006434AA
  bb_0064345F -->|fallthrough| bb_00643472
  bb_00643472 -->|branch| bb_00643494
  bb_0064347B -->|branch| bb_00643491
  bb_0064347B -->|fallthrough| bb_00643484
  bb_00643484 -->|flow| bb_00643491
  bb_00643491 -->|flow| bb_00643494
  bb_00643494 -->|branch| bb_0064347B
  bb_00643494 -->|fallthrough| bb_00643499
  bb_00643499 -->|branch| bb_006434AA
  bb_00643499 -->|fallthrough| bb_0064349E
  bb_0064349E -->|flow| bb_006434AA
  bb_006434AA -->|branch| bb_00643523
  bb_006434AA -->|fallthrough| bb_006434C0
  bb_006434C0 -->|branch| bb_006434D8
  bb_006434C0 -->|fallthrough| bb_006434CC
  bb_006434CC -->|branch| bb_006434EB
  bb_006434CC -->|fallthrough| bb_006434D8
  bb_006434D8 -->|branch| bb_00643523
  bb_006434D8 -->|fallthrough| bb_006434EB
  bb_006434EB -->|branch| bb_0064350D
  bb_006434F4 -->|branch| bb_0064350A
  bb_006434F4 -->|fallthrough| bb_006434FD
  bb_006434FD -->|flow| bb_0064350A
  bb_0064350A -->|flow| bb_0064350D
  bb_0064350D -->|branch| bb_006434F4
  bb_0064350D -->|fallthrough| bb_00643512
  bb_00643512 -->|branch| bb_00643523
  bb_00643512 -->|fallthrough| bb_00643517
  bb_00643517 -->|flow| bb_00643523
```
