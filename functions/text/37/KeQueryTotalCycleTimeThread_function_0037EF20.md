# KeQueryTotalCycleTimeThread

- RVA: `0x0037EF20`–`0x0037FBBC` (길이 `3,228` bytes)
- VA: `0x000000014037EF20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007B7D0`
- 디코드: `763`개 명령, `3,228/3,228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **17**

### Outgoing calls
- `0x0037EF66` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0037EFCC` → [KeQueryPerformanceCounter](KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0037F2C2` → [KiUpdateThreadHgsFeedback](KiUpdateThreadHgsFeedback_function_0037D790.md) (function, `0x0037D790`)
- `0x0037F311` → [KeQueryPerformanceCounter](KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0037F4AF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0037F514` → [KiEndCounterAccumulation](KiEndCounterAccumulation_function_0037EEAC.md) (function, `0x0037EEAC`)
- `0x0037F6F0` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0037F749` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x0037F783` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0037F7EB` → [KeFlushProcessWriteBuffers](../2C/KeFlushProcessWriteBuffers_function_002CE4FC.md) (function, `0x002CE4FC`)
- `0x0037F816` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x0037F833` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0037F854` → [HalRequestSoftwareInterrupt](../3F/HalRequestSoftwareInterrupt_function_003FADA0.md) (function, `0x003FADA0`)
- `0x0037F888` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0037F8EA` → [KiReleaseThreadStateLock](../21/KiReleaseThreadStateLock_function_00217910.md) (function, `0x00217910`)
- `0x0037F907` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0037F98E` → [KiIpiSendRequest](../31/KiIpiSendRequest_function_003113C0.md) (function, `0x003113C0`)
- `0x0037F99C` → [KiIpiStallOnPacketTargetsPrcb](../2C/KiIpiStallOnPacketTargetsPrcb_function_002CE670.md) (function, `0x002CE670`)
- `0x0037FA00` → [KiAcquirePrcbLocksForIsolationUnit](../30/KiAcquirePrcbLocksForIsolationUnit_function_0030ED60.md) (function, `0x0030ED60`)
- `0x0037FA24` → [KiReleasePrcbLocksForIsolationUnit](../39/KiReleasePrcbLocksForIsolationUnit_function_00399C50.md) (function, `0x00399C50`)
- `0x0037FA31` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0037FAB5` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x0037FADF` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0037FAF7` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)

### Direct callers
- [NtQueryInformationThread](../../page/AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE41BF`

### Static image references
- `0x0037EF3F` → RVA `0x00E0A740` (`.data`; read)
- `0x0037F004` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x0037F04E` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x0037F063` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x0037F1F4` → RVA `0x00F10A44` (`.data`; read)
- `0x0037F21C` → RVA `0x00FC6D60` (`ALMOSTRO`; read)
- `0x0037F2AD` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x0037F2C7` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x0037F440` → RVA `0x00E66908` (`.data`; read)
- `0x0037F44A` → RVA `0x00F10E80` (`.data`; read)
- `0x0037F74E` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0037F81F` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0037F90C` → RVA `0x00F231B0` (`.data`; read)
- `0x0037F964` → RVA `0x0049E550` (`EmpCheckErrataList`; read)
- `0x0037F9CA` → RVA `0x00FC6B38` (`ALMOSTRO`; read)
- `0x0037FB40` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x0037FB4D` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0037F9ED` → [sub_006E4548](../6E/Unknown_function_006E4548.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037EF20  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0037EF25  55                              push rbp
0037EF26  56                              push rsi
0037EF27  57                              push rdi
0037EF28  41 54                           push r12
0037EF2A  41 55                           push r13
0037EF2C  41 56                           push r14
0037EF2E  41 57                           push r15
0037EF30  48 8D AC 24 20 FF FF FF         lea rbp, [rsp - 0xe0]
0037EF38  48 81 EC E0 01 00 00            sub rsp, 0x1e0
0037EF3F  48 8B 05 FA B7 A8 00            mov rax, qword ptr [rip + 0xa8b7fa]
0037EF46  48 33 C4                        xor rax, rsp
0037EF49  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
0037EF50  4C 8B EA                        mov r13, rdx
0037EF53  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0037EF57  48 8B F1                        mov rsi, rcx
0037EF5A  33 D2                           xor edx, edx
0037EF5C  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0037EF60  41 B8 08 01 00 00               mov r8d, 0x108
0037EF66  E8 D5 7C 34 00                  call 0x1406c6c40
0037EF6B  33 FF                           xor edi, edi
0037EF6D  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0037EF72  0F 57 C0                        xorps xmm0, xmm0
0037EF75  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0037EF7A  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0037EF7F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0037EF88  48 3B F0                        cmp rsi, rax
0037EF8B  0F 85 B0 07 00 00               jne 0x14037f741
0037EF91  FA                              cli
0037EF92  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
0037EF9B  44 8B DF                        mov r11d, edi
0037EF9E  44 8B E7                        mov r12d, edi
0037EFA1  44 8B FF                        mov r15d, edi
0037EFA4  49 BE 00 03 00 00 80 F7 FF FF   movabs r14, 0xfffff78000000300
0037EFAE  49 BD 60 03 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000360
0037EFB8  C6 43 20 01                     mov byte ptr [rbx + 0x20], 1
0037EFBC  90                              nop
0037EFBD  40 38 BB DC 86 00 00            cmp byte ptr [rbx + 0x86dc], dil
0037EFC4  0F 84 CA 00 00 00               je 0x14037f094
0037EFCA  33 C9                           xor ecx, ecx
0037EFCC  E8 0F F8 FF FF                  call 0x14037e7e0
0037EFD1  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0037EFD8  4C 8B D8                        mov r11, rax
0037EFDB  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0037EFE2  49 8B D3                        mov rdx, r11
0037EFE5  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
0037EFE9  84 C9                           test cl, cl
0037EFEB  74 03                           je 0x14037eff0
0037EFED  48 D3 E2                        shl rdx, cl
0037EFF0  48 F7 E2                        mul rdx
0037EFF3  4C 8B FA                        mov r15, rdx
0037EFF6  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
0037EFFA  4C 2B BB 80 86 00 00            sub r15, qword ptr [rbx + 0x8680]
0037F001  4C 8B E2                        mov r12, rdx
0037F004  40 38 3D 8A 7A C4 00            cmp byte ptr [rip + 0xc47a8a], dil
0037F00B  0F 84 83 00 00 00               je 0x14037f094
0037F011  4C 8B 83 F8 86 00 00            mov r8, qword ptr [rbx + 0x86f8]
0037F018  49 39 3E                        cmp qword ptr [r14], rdi
0037F01B  74 77                           je 0x14037f094
0037F01D  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0037F026  4D 8B 4D 00                     mov r9, qword ptr [r13]
0037F02A  0F B6 C8                        movzx ecx, al
0037F02D  84 C0                           test al, al
0037F02F  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0037F034  49 8B C1                        mov rax, r9
0037F037  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
0037F03C  0F 84 7A 08 00 00               je 0x14037f8bc
0037F042  49 D3 E0                        shl r8, cl
0037F045  49 F7 E0                        mul r8
0037F048  4D 8B C3                        mov r8, r11
0037F04B  49 D3 E0                        shl r8, cl
0037F04E  0F BE 0D 71 7B C4 00            movsx ecx, byte ptr [rip + 0xc47b71]
0037F055  4C 8B D2                        mov r10, rdx
0037F058  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
0037F05D  49 8B C1                        mov rax, r9
0037F060  49 F7 E0                        mul r8
0037F063  48 8B 05 AE 82 C4 00            mov rax, qword ptr [rip + 0xc482ae]
0037F06A  4C 8B CA                        mov r9, rdx
0037F06D  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
0037F072  49 F7 E2                        mul r10
0037F075  48 8B 05 9C 82 C4 00            mov rax, qword ptr [rip + 0xc4829c]
0037F07C  4C 8B D2                        mov r10, rdx
0037F07F  49 F7 E1                        mul r9
0037F082  49 D3 EA                        shr r10, cl
0037F085  4C 8B C2                        mov r8, rdx
0037F088  49 D3 E8                        shr r8, cl
0037F08B  45 2B C2                        sub r8d, r10d
0037F08E  0F 85 7E 05 00 00               jne 0x14037f612
0037F094  4C 89 9B F8 86 00 00            mov qword ptr [rbx + 0x86f8], r11
0037F09B  4C 89 A3 80 86 00 00            mov qword ptr [rbx + 0x8680], r12
0037F0A2  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0037F0A6  49 03 C7                        add rax, r15
0037F0A9  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
0037F0AD  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0037F0B1  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0037F0B5  74 23                           je 0x14037f0da
0037F0B7  8B 83 B8 86 00 00               mov eax, dword ptr [rbx + 0x86b8]
0037F0BD  8B 4E 50                        mov ecx, dword ptr [rsi + 0x50]
0037F0C0  49 0F AF C7                     imul rax, r15
0037F0C4  48 C1 E8 10                     shr rax, 0x10
0037F0C8  48 03 C8                        add rcx, rax
0037F0CB  B8 FF FF FF FF                  mov eax, 0xffffffff
0037F0D0  48 3B C8                        cmp rcx, rax
0037F0D3  48 0F 47 C8                     cmova rcx, rax
0037F0D7  89 4E 50                        mov dword ptr [rsi + 0x50], ecx
0037F0DA  44 0F B6 76 02                  movzx r14d, byte ptr [rsi + 2]
0037F0DF  41 BA 01 00 00 00               mov r10d, 1
0037F0E5  45 8D 6A 63                     lea r13d, [r10 + 0x63]
0037F0E9  41 F6 C6 BE                     test r14b, 0xbe
0037F0ED  0F 84 FB 01 00 00               je 0x14037f2ee
0037F0F3  45 84 F6                        test r14b, r14b
0037F0F6  79 54                           jns 0x14037f14c
0037F0F8  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
0037F0FF  41 8B D2                        mov edx, r10d
0037F102  4C 8B 83 B0 8B 00 00            mov r8, qword ptr [rbx + 0x8bb0]
0037F109  44 8B 88 90 01 00 00            mov r9d, dword ptr [rax + 0x190]
0037F110  41 8B C1                        mov eax, r9d
0037F113  C1 E8 0D                        shr eax, 0xd
0037F116  25 FF FF 03 00                  and eax, 0x3ffff
0037F11B  49 C1 E9 04                     shr r9, 4
0037F11F  0F BD C8                        bsr ecx, eax
0037F122  41 81 E1 FF 01 00 00            and r9d, 0x1ff
0037F129  D3 E2                           shl edx, cl
0037F12B  83 C1 FE                        add ecx, -2
0037F12E  33 D0                           xor edx, eax
0037F130  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0037F134  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0037F138  48 8B 54 D1 08                  mov rdx, qword ptr [rcx + rdx*8 + 8]
0037F13D  4A 8B 04 CA                     mov rax, qword ptr [rdx + r9*8]
0037F141  49 03 C7                        add rax, r15
0037F144  4A 89 04 CA                     mov qword ptr [rdx + r9*8], rax
0037F148  41 80 E6 7F                     and r14b, 0x7f
0037F14C  41 F6 C6 10                     test r14b, 0x10
0037F150  0F 85 81 04 00 00               jne 0x14037f5d7
0037F156  41 F6 C6 20                     test r14b, 0x20
0037F15A  0F 84 43 01 00 00               je 0x14037f2a3
0037F160  4C 8B 8E 88 06 00 00            mov r9, qword ptr [rsi + 0x688]
0037F167  4D 85 C9                        test r9, r9
0037F16A  0F 84 2F 01 00 00               je 0x14037f29f
0037F170  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
0037F177  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
0037F17E  48 85 C9                        test rcx, rcx
0037F181  0F 84 19 0A 00 00               je 0x14037fba0
0037F187  48 85 C0                        test rax, rax
0037F18A  0F 84 10 0A 00 00               je 0x14037fba0
0037F190  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
0037F194  75 11                           jne 0x14037f1a7
0037F196  8B 50 50                        mov edx, dword ptr [rax + 0x50]
0037F199  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
0037F19F  3B D0                           cmp edx, eax
0037F1A1  72 0A                           jb 0x14037f1ad
0037F1A3  8B D0                           mov edx, eax
0037F1A5  EB 06                           jmp 0x14037f1ad
0037F1A7  8B 90 84 00 00 00               mov edx, dword ptr [rax + 0x84]
0037F1AD  44 8B C7                        mov r8d, edi
0037F1B0  48 8D 8B 6A 8A 00 00            lea rcx, [rbx + 0x8a6a]
0037F1B7  0F B7 01                        movzx eax, word ptr [rcx]
0037F1BA  3B D0                           cmp edx, eax
0037F1BC  76 0D                           jbe 0x14037f1cb
0037F1BE  41 FF C0                        inc r8d
0037F1C1  48 83 C1 02                     add rcx, 2
0037F1C5  41 83 F8 03                     cmp r8d, 3
0037F1C9  72 EC                           jb 0x14037f1b7
0037F1CB  44 0F B6 9B 08 8A 00 00         movzx r11d, byte ptr [rbx + 0x8a08]
0037F1D3  41 0F B6 C3                     movzx eax, r11b
0037F1D7  41 8B C8                        mov ecx, r8d
0037F1DA  48 03 C9                        add rcx, rcx
0037F1DD  F6 D8                           neg al
0037F1DF  48 1B D2                        sbb rdx, rdx
0037F1E2  49 8D 04 C9                     lea rax, [r9 + rcx*8]
0037F1E6  83 E2 08                        and edx, 8
0037F1E9  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0037F1ED  49 03 CF                        add rcx, r15
0037F1F0  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0037F1F4  8B 05 4A 18 B9 00               mov eax, dword ptr [rip + 0xb9184a]
0037F1FA  41 8B 89 C0 00 00 00            mov ecx, dword ptr [r9 + 0xc0]
0037F201  3B C1                           cmp eax, ecx
0037F203  0F 87 04 05 00 00               ja 0x14037f70d
0037F209  2B C8                           sub ecx, eax
0037F20B  83 F9 20                        cmp ecx, 0x20
0037F20E  73 0C                           jae 0x14037f21c
0037F210  41 8B C2                        mov eax, r10d
0037F213  D3 E0                           shl eax, cl
0037F215  41 09 81 C4 00 00 00            or dword ptr [r9 + 0xc4], eax
0037F21C  39 3D 3E 7B C4 00               cmp dword ptr [rip + 0xc47b3e], edi
0037F222  75 1E                           jne 0x14037f242
0037F224  0F B6 8E 04 02 00 00            movzx ecx, byte ptr [rsi + 0x204]
0037F22B  8D 41 FE                        lea eax, [rcx - 2]
0037F22E  A9 FB FF FF FF                  test eax, 0xfffffffb
0037F233  0F 84 86 03 00 00               je 0x14037f5bf
0037F239  80 F9 05                        cmp cl, 5
0037F23C  0F 84 7D 03 00 00               je 0x14037f5bf
0037F242  48 39 BE 50 06 00 00            cmp qword ptr [rsi + 0x650], rdi
0037F249  74 54                           je 0x14037f29f
0037F24B  41 8B C8                        mov ecx, r8d
0037F24E  41 0F B6 C3                     movzx eax, r11b
0037F252  48 83 C1 08                     add rcx, 8
0037F256  48 03 C9                        add rcx, rcx
0037F259  F6 D8                           neg al
0037F25B  48 1B D2                        sbb rdx, rdx
0037F25E  83 E2 08                        and edx, 8
0037F261  49 8D 04 C9                     lea rax, [r9 + rcx*8]
0037F265  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
0037F269  49 03 CF                        add rcx, r15
0037F26C  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
0037F270  BA 40 00 00 00                  mov edx, 0x40
0037F275  48 8B 86 50 06 00 00            mov rax, qword ptr [rsi + 0x650]
0037F27C  48 8B 88 88 06 00 00            mov rcx, qword ptr [rax + 0x688]
0037F283  41 8B C0                        mov eax, r8d
0037F286  41 B8 48 00 00 00               mov r8d, 0x48
0037F28C  48 C1 E0 04                     shl rax, 4
0037F290  45 84 DB                        test r11b, r11b
0037F293  41 0F 45 D0                     cmovne edx, r8d
0037F297  48 03 C1                        add rax, rcx
0037F29A  F0 4C 01 3C 02                  lock add qword ptr [rdx + rax], r15
0037F29F  41 80 E6 DF                     and r14b, 0xdf
0037F2A3  41 F6 C6 40                     test r14b, 0x40
0037F2A7  0F 85 4C 03 00 00               jne 0x14037f5f9
0037F2AD  40 38 3D 2A 78 C4 00            cmp byte ptr [rip + 0xc4782a], dil
0037F2B4  74 11                           je 0x14037f2c7
0037F2B6  45 33 C9                        xor r9d, r9d
0037F2B9  4D 8B C7                        mov r8, r15
0037F2BC  48 8B D6                        mov rdx, rsi
0037F2BF  48 8B CB                        mov rcx, rbx
0037F2C2  E8 C9 E4 FF FF                  call 0x14037d790
0037F2C7  4C 8D 0D 32 0C C5 00            lea r9, [rip + 0xc50c32]
0037F2CE  48 39 BB B0 86 00 00            cmp qword ptr [rbx + 0x86b0], rdi
0037F2D5  74 0D                           je 0x14037f2e4
0037F2D7  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
0037F2DE  0F 85 35 08 00 00               jne 0x14037fb19
0037F2E4  41 F6 C6 BE                     test r14b, 0xbe
0037F2E8  0F 85 E2 01 00 00               jne 0x14037f4d0
0037F2EE  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0037F2F2  48 85 C0                        test rax, rax
0037F2F5  74 03                           je 0x14037f2fa
0037F2F7  4C 89 20                        mov qword ptr [rax], r12
0037F2FA  4C 8B F7                        mov r14, rdi
0037F2FD  4C 8B E7                        mov r12, rdi
0037F300  4C 8B FF                        mov r15, rdi
0037F303  4C 8B DF                        mov r11, rdi
0037F306  40 38 BB DC 86 00 00            cmp byte ptr [rbx + 0x86dc], dil
0037F30D  74 54                           je 0x14037f363
0037F30F  33 C9                           xor ecx, ecx
0037F311  E8 CA F4 FF FF                  call 0x14037e7e0
0037F316  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
0037F31D  4C 8B F0                        mov r14, rax
0037F320  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
0037F327  49 8B D6                        mov rdx, r14
0037F32A  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0037F32E  84 C9                           test cl, cl
0037F330  74 03                           je 0x14037f335
0037F332  48 D3 E2                        shl rdx, cl
0037F335  48 F7 E2                        mul rdx
0037F338  4D 8B FE                        mov r15, r14
0037F33B  4C 8B E2                        mov r12, rdx
0037F33E  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
0037F342  48 8B 93 F8 86 00 00            mov rdx, qword ptr [rbx + 0x86f8]
0037F349  4D 8B DC                        mov r11, r12
0037F34C  4C 2B 9B 80 86 00 00            sub r11, qword ptr [rbx + 0x8680]
0037F353  4C 2B FA                        sub r15, rdx
0037F356  40 38 3D 38 77 C4 00            cmp byte ptr [rip + 0xc47738], dil
0037F35D  0F 85 BB 01 00 00               jne 0x14037f51e
0037F363  48 8B 83 00 87 00 00            mov rax, qword ptr [rbx + 0x8700]
0037F36A  49 03 C7                        add rax, r15
0037F36D  48 89 83 00 87 00 00            mov qword ptr [rbx + 0x8700], rax
0037F374  48 8B 83 78 87 00 00            mov rax, qword ptr [rbx + 0x8778]
0037F37B  49 03 C3                        add rax, r11
0037F37E  48 89 83 78 87 00 00            mov qword ptr [rbx + 0x8778], rax
0037F385  F6 46 02 20                     test byte ptr [rsi + 2], 0x20
0037F389  74 7B                           je 0x14037f406
0037F38B  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
0037F392  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
0037F399  48 85 C9                        test rcx, rcx
0037F39C  74 26                           je 0x14037f3c4
0037F39E  48 85 C0                        test rax, rax
0037F3A1  74 21                           je 0x14037f3c4
0037F3A3  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
0037F3A7  75 14                           jne 0x14037f3bd
0037F3A9  44 8B 68 50                     mov r13d, dword ptr [rax + 0x50]
0037F3AD  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
0037F3B3  44 3B E8                        cmp r13d, eax
0037F3B6  72 0C                           jb 0x14037f3c4
0037F3B8  44 8B E8                        mov r13d, eax
0037F3BB  EB 07                           jmp 0x14037f3c4
0037F3BD  44 8B A8 84 00 00 00            mov r13d, dword ptr [rax + 0x84]
0037F3C4  8B CF                           mov ecx, edi
0037F3C6  48 8D 93 6A 8A 00 00            lea rdx, [rbx + 0x8a6a]
0037F3CD  0F B7 02                        movzx eax, word ptr [rdx]
0037F3D0  44 3B E8                        cmp r13d, eax
0037F3D3  76 0B                           jbe 0x14037f3e0
0037F3D5  FF C1                           inc ecx
0037F3D7  48 83 C2 02                     add rdx, 2
0037F3DB  83 F9 03                        cmp ecx, 3
0037F3DE  72 ED                           jb 0x14037f3cd
0037F3E0  40 38 BB 08 8A 00 00            cmp byte ptr [rbx + 0x8a08], dil
0037F3E7  8B C1                           mov eax, ecx
0037F3E9  40 0F 95 C7                     setne dil
0037F3ED  48 81 C7 F0 10 00 00            add rdi, 0x10f0
0037F3F4  48 8D 04 47                     lea rax, [rdi + rax*2]
0037F3F8  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
0037F3FC  48 8D 14 C3                     lea rdx, [rbx + rax*8]
0037F400  49 03 CB                        add rcx, r11
0037F403  48 89 0A                        mov qword ptr [rdx], rcx
0037F406  F6 46 02 40                     test byte ptr [rsi + 2], 0x40
0037F40A  74 10                           je 0x14037f41c
0037F40C  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0037F413  48 85 C0                        test rax, rax
0037F416  74 04                           je 0x14037f41c
0037F418  C6 40 40 01                     mov byte ptr [rax + 0x40], 1
0037F41C  4C 89 B3 F8 86 00 00            mov qword ptr [rbx + 0x86f8], r14
0037F423  4C 89 A3 80 86 00 00            mov qword ptr [rbx + 0x8680], r12
0037F42A  F6 46 02 02                     test byte ptr [rsi + 2], 2
0037F42E  74 48                           je 0x14037f478
0037F430  48 8B 86 68 01 00 00            mov rax, qword ptr [rsi + 0x168]
0037F437  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
0037F43B  4D 85 C0                        test r8, r8
0037F43E  74 38                           je 0x14037f478
0037F440  8B 0D C2 74 AE 00               mov ecx, dword ptr [rip + 0xae74c2]
0037F446  85 C9                           test ecx, ecx
0037F448  74 2E                           je 0x14037f478
0037F44A  4C 8D 0D 2F 1A B9 00            lea r9, [rip + 0xb91a2f]
0037F451  44 8B D9                        mov r11d, ecx
0037F454  4C 8D 50 30                     lea r10, [rax + 0x30]
0037F458  41 BE 01 00 00 00               mov r14d, 1
0037F45E  4D 85 C6                        test r14, r8
0037F461  0F 85 41 07 00 00               jne 0x14037fba8
0037F467  4D 03 F6                        add r14, r14
0037F46A  49 83 C2 18                     add r10, 0x18
0037F46E  49 83 C1 04                     add r9, 4
0037F472  49 83 EB 01                     sub r11, 1
0037F476  75 E6                           jne 0x14037f45e
0037F478  90                              nop
0037F479  80 7B 06 00                     cmp byte ptr [rbx + 6], 0
0037F47D  C6 43 20 00                     mov byte ptr [rbx + 0x20], 0
0037F481  0F 85 C7 03 00 00               jne 0x14037f84e
0037F487  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0037F490  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0037F497  4D 85 C0                        test r8, r8
0037F49A  0F 85 32 02 00 00               jne 0x14037f6d2
0037F4A0  FB                              sti
0037F4A1  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0037F4A5  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
0037F4AC  48 33 CC                        xor rcx, rsp
0037F4AF  E8 8C D1 32 00                  call 0x1406ac640
0037F4B4  48 8B 9C 24 30 02 00 00         mov rbx, qword ptr [rsp + 0x230]
0037F4BC  48 81 C4 E0 01 00 00            add rsp, 0x1e0
0037F4C3  41 5F                           pop r15
0037F4C5  41 5E                           pop r14
0037F4C7  41 5D                           pop r13
0037F4C9  41 5C                           pop r12
0037F4CB  5F                              pop rdi
0037F4CC  5E                              pop rsi
0037F4CD  5D                              pop rbp
0037F4CE  C3                              ret
0037F4CF  CC                              int3
0037F4D0  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
0037F4D4  48 85 C9                        test rcx, rcx
0037F4D7  74 18                           je 0x14037f4f1
0037F4D9  8B 83 D8 00 00 00               mov eax, dword ptr [rbx + 0xd8]
0037F4DF  48 03 C1                        add rax, rcx
0037F4E2  4C 01 38                        add qword ptr [rax], r15
0037F4E5  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
0037F4EC  48 85 C0                        test rax, rax
0037F4EF  75 F1                           jne 0x14037f4e2
0037F4F1  F6 46 02 08                     test byte ptr [rsi + 2], 8
0037F4F5  74 0D                           je 0x14037f504
0037F4F7  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
0037F4FE  0F 85 62 06 00 00               jne 0x14037fb66
0037F504  48 39 BE 68 01 00 00            cmp qword ptr [rsi + 0x168], rdi
0037F50B  0F 84 DD FD FF FF               je 0x14037f2ee
0037F511  48 8B CE                        mov rcx, rsi
0037F514  E8 93 F9 FF FF                  call 0x14037eeac
0037F519  E9 D0 FD FF FF                  jmp 0x14037f2ee
0037F51E  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
0037F528  48 39 38                        cmp qword ptr [rax], rdi
0037F52B  0F 84 32 FE FF FF               je 0x14037f363
0037F531  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
0037F53A  49 B9 60 03 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000360
0037F544  0F B6 C8                        movzx ecx, al
0037F547  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
0037F54C  84 C0                           test al, al
0037F54E  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0037F553  4D 8B C6                        mov r8, r14
0037F556  4D 8B 09                        mov r9, qword ptr [r9]
0037F559  49 8B C1                        mov rax, r9
0037F55C  0F 84 65 03 00 00               je 0x14037f8c7
0037F562  48 D3 E2                        shl rdx, cl
0037F565  48 F7 E2                        mul rdx
0037F568  49 D3 E0                        shl r8, cl
0037F56B  0F BE 0D 54 76 C4 00            movsx ecx, byte ptr [rip + 0xc47654]
0037F572  4C 8B D2                        mov r10, rdx
0037F575  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
0037F57A  49 8B C1                        mov rax, r9
0037F57D  49 F7 E0                        mul r8
0037F580  48 8B 05 91 7D C4 00            mov rax, qword ptr [rip + 0xc47d91]
0037F587  4C 8B CA                        mov r9, rdx
0037F58A  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0037F58F  49 F7 E2                        mul r10
0037F592  48 8B 05 7F 7D C4 00            mov rax, qword ptr [rip + 0xc47d7f]
0037F599  4C 8B D2                        mov r10, rdx
0037F59C  49 F7 E1                        mul r9
0037F59F  49 D3 EA                        shr r10, cl
0037F5A2  48 D3 EA                        shr rdx, cl
0037F5A5  41 2B D2                        sub edx, r10d
0037F5A8  0F 84 B5 FD FF FF               je 0x14037f363
0037F5AE  01 93 44 86 00 00               add dword ptr [rbx + 0x8644], edx
0037F5B4  01 93 50 86 00 00               add dword ptr [rbx + 0x8650], edx
0037F5BA  E9 A4 FD FF FF                  jmp 0x14037f363
0037F5BF  41 8B D0                        mov edx, r8d
0037F5C2  48 03 D2                        add rdx, rdx
0037F5C5  49 8B 4C D1 08                  mov rcx, qword ptr [r9 + rdx*8 + 8]
0037F5CA  49 03 CF                        add rcx, r15
0037F5CD  49 89 4C D1 08                  mov qword ptr [r9 + rdx*8 + 8], rcx
0037F5D2  E9 6B FC FF FF                  jmp 0x14037f242
0037F5D7  0F B6 46 7C                     movzx eax, byte ptr [rsi + 0x7c]
0037F5DB  48 8D 14 C3                     lea rdx, [rbx + rax*8]
0037F5DF  48 8B 8A 88 86 00 00            mov rcx, qword ptr [rdx + 0x8688]
0037F5E6  49 03 CF                        add rcx, r15
0037F5E9  48 89 8A 88 86 00 00            mov qword ptr [rdx + 0x8688], rcx
0037F5F0  41 80 E6 EF                     and r14b, 0xef
0037F5F4  E9 5D FB FF FF                  jmp 0x14037f156
0037F5F9  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
0037F600  48 85 C0                        test rax, rax
0037F603  0F 84 A4 FC FF FF               je 0x14037f2ad
0037F609  40 88 78 40                     mov byte ptr [rax + 0x40], dil
0037F60D  E9 9B FC FF FF                  jmp 0x14037f2ad
0037F612  F7 46 74 00 04 00 00            test dword ptr [rsi + 0x74], 0x400
0037F619  75 1D                           jne 0x14037f638
0037F61B  8B 86 4C 04 00 00               mov eax, dword ptr [rsi + 0x44c]
0037F621  F3 48 0F B8 D0                  popcnt rdx, rax
0037F626  49 8B C3                        mov rax, r11
0037F629  48 C1 E8 04                     shr rax, 4
0037F62D  83 E0 1F                        and eax, 0x1f
0037F630  3B C2                           cmp eax, edx
0037F632  0F 82 C2 00 00 00               jb 0x14037f6fa
0037F638  44 01 83 44 86 00 00            add dword ptr [rbx + 0x8644], r8d
0037F63F  44 01 86 8C 02 00 00            add dword ptr [rsi + 0x28c], r8d
0037F646  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
0037F64A  0F 84 44 FA FF FF               je 0x14037f094
0037F650  80 BE C3 00 00 00 10            cmp byte ptr [rsi + 0xc3], 0x10
0037F657  7D 60                           jge 0x14037f6b9
0037F659  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0037F65D  48 85 C0                        test rax, rax
0037F660  74 57                           je 0x14037f6b9
0037F662  48 8B 46 68                     mov rax, qword ptr [rsi + 0x68]
0037F666  48 85 C0                        test rax, rax
0037F669  74 4E                           je 0x14037f6b9
0037F66B  8B 8B D8 00 00 00               mov ecx, dword ptr [rbx + 0xd8]
0037F671  44 8B CF                        mov r9d, edi
0037F674  48 03 C8                        add rcx, rax
0037F677  80 BE C3 00 00 00 10            cmp byte ptr [rsi + 0xc3], 0x10
0037F67E  0F 8D 10 FA FF FF               jge 0x14037f094
0037F684  F7 46 78 00 02 00 00            test dword ptr [rsi + 0x78], 0x200
0037F68B  75 2C                           jne 0x14037f6b9
0037F68D  48 8B D1                        mov rdx, rcx
0037F690  F6 42 70 02                     test byte ptr [rdx + 0x70], 2
0037F694  75 30                           jne 0x14037f6c6
0037F696  48 8B 92 A0 01 00 00            mov rdx, qword ptr [rdx + 0x1a0]
0037F69D  48 85 D2                        test rdx, rdx
0037F6A0  75 EE                           jne 0x14037f690
0037F6A2  44 03 49 7C                     add r9d, dword ptr [rcx + 0x7c]
0037F6A6  75 0C                           jne 0x14037f6b4
0037F6A8  48 8B 89 A0 01 00 00            mov rcx, qword ptr [rcx + 0x1a0]
0037F6AF  48 85 C9                        test rcx, rcx
0037F6B2  75 EE                           jne 0x14037f6a2
0037F6B4  45 85 C9                        test r9d, r9d
0037F6B7  75 0D                           jne 0x14037f6c6
0037F6B9  80 BE C3 00 00 00 08            cmp byte ptr [rsi + 0xc3], 8
0037F6C0  0F 8D CE F9 FF FF               jge 0x14037f094
0037F6C6  44 01 83 6C 86 00 00            add dword ptr [rbx + 0x866c], r8d
0037F6CD  E9 C2 F9 FF FF                  jmp 0x14037f094
0037F6D2  41 0F 0D 08                     prefetchw byte ptr [r8]
0037F6D6  41 8B 00                        mov eax, dword ptr [r8]
0037F6D9  8B D0                           mov edx, eax
0037F6DB  0F BA F2 15                     btr edx, 0x15
0037F6DF  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
0037F6E4  75 F3                           jne 0x14037f6d9
0037F6E6  0F BA E0 15                     bt eax, 0x15
0037F6EA  0F 83 B0 FD FF FF               jae 0x14037f4a0
0037F6F0  E8 DB 3A EE FF                  call 0x1402631d0
0037F6F5  E9 A6 FD FF FF                  jmp 0x14037f4a0
0037F6FA  44 01 83 48 86 00 00            add dword ptr [rbx + 0x8648], r8d
0037F701  44 01 86 DC 02 00 00            add dword ptr [rsi + 0x2dc], r8d
0037F708  E9 39 FF FF FF                  jmp 0x14037f646
0037F70D  8B D0                           mov edx, eax
0037F70F  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
0037F713  2B D1                           sub edx, ecx
0037F715  83 FA 20                        cmp edx, 0x20
0037F718  0F 83 26 01 00 00               jae 0x14037f844
0037F71E  41 8B 81 C4 00 00 00            mov eax, dword ptr [r9 + 0xc4]
0037F725  8B CA                           mov ecx, edx
0037F727  D3 E0                           shl eax, cl
0037F729  41 0B C2                        or eax, r10d
0037F72C  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
0037F730  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0037F735  49 89 81 C0 00 00 00            mov qword ptr [r9 + 0xc0], rax
0037F73C  E9 DB FA FF FF                  jmp 0x14037f21c
0037F741  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0037F746  48 8B CE                        mov rcx, rsi
0037F749  E8 32 6B 01 00                  call 0x140396280
0037F74E  48 8D 15 EB 94 C4 00            lea rdx, [rip + 0xc494eb]
0037F755  0F B6 9E 84 01 00 00            movzx ebx, byte ptr [rsi + 0x184]
0037F75C  4C 8B F7                        mov r14, rdi
0037F75F  4C 8B FF                        mov r15, rdi
0037F762  8B CB                           mov ecx, ebx
0037F764  83 FB 03                        cmp ebx, 3
0037F767  75 4A                           jne 0x14037f7b3
0037F769  44 8B A6 18 02 00 00            mov r12d, dword ptr [rsi + 0x218]
0037F770  45 85 E4                        test r12d, r12d
0037F773  78 E0                           js 0x14037f755
0037F775  4E 8B 34 E2                     mov r14, qword ptr [rdx + r12*8]
0037F779  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0037F77E  49 8B CE                        mov rcx, r14
0037F781  33 D2                           xor edx, edx
0037F783  E8 D8 F5 F8 FF                  call 0x14030ed60
0037F788  49 3B 76 10                     cmp rsi, qword ptr [r14 + 0x10]
0037F78C  74 4A                           je 0x14037f7d8
0037F78E  0F B6 86 84 01 00 00            movzx eax, byte ptr [rsi + 0x184]
0037F795  3A C3                           cmp al, bl
0037F797  0F 85 82 02 00 00               jne 0x14037fa1f
0037F79D  8B 86 18 02 00 00               mov eax, dword ptr [rsi + 0x218]
0037F7A3  41 3B C4                        cmp eax, r12d
0037F7A6  0F 85 73 02 00 00               jne 0x14037fa1f
0037F7AC  B9 1E 00 00 00                  mov ecx, 0x1e
0037F7B1  CD 29                           int 0x29
0037F7B3  83 E9 01                        sub ecx, 1
0037F7B6  0F 84 FB 01 00 00               je 0x14037f9b7
0037F7BC  83 E9 01                        sub ecx, 1
0037F7BF  0F 84 A5 00 00 00               je 0x14037f86a
0037F7C5  83 F9 03                        cmp ecx, 3
0037F7C8  75 0E                           jne 0x14037f7d8
0037F7CA  0F B6 46 70                     movzx eax, byte ptr [rsi + 0x70]
0037F7CE  24 07                           and al, 7
0037F7D0  3C 01                           cmp al, 1
0037F7D2  0F 85 86 00 00 00               jne 0x14037f85e
0037F7D8  80 FB 02                        cmp bl, 2
0037F7DB  0F 84 EE 00 00 00               je 0x14037f8cf
0037F7E1  0F B6 46 71                     movzx eax, byte ptr [rsi + 0x71]
0037F7E5  84 C0                           test al, al
0037F7E7  74 07                           je 0x14037f7f0
0037F7E9  B1 01                           mov cl, 1
0037F7EB  E8 0C ED F4 FF                  call 0x1402ce4fc
0037F7F0  0F 31                           rdtsc
0037F7F2  48 C1 E2 20                     shl rdx, 0x20
0037F7F6  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0037F7FB  48 0B C2                        or rax, rdx
0037F7FE  4D 8B CF                        mov r9, r15
0037F801  49 89 45 00                     mov qword ptr [r13], rax
0037F805  49 8B D6                        mov rdx, r14
0037F808  4C 8B 66 48                     mov r12, qword ptr [rsi + 0x48]
0037F80C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0037F811  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0037F816  E8 F5 80 E9 FF                  call 0x140217910
0037F81B  48 89 7E 40                     mov qword ptr [rsi + 0x40], rdi
0037F81F  39 3D FB 74 C4 00               cmp dword ptr [rip + 0xc474fb], edi
0037F825  0F B6 5C 24 30                  movzx ebx, byte ptr [rsp + 0x30]
0037F82A  74 0C                           je 0x14037f838
0037F82C  44 0F 20 C1                     mov rcx, cr8
0037F830  0F B6 D3                        movzx edx, bl
0037F833  E8 60 5E 17 00                  call 0x1404f5698
0037F838  44 0F 22 C3                     mov cr8, rbx
0037F83C  49 8B C4                        mov rax, r12
0037F83F  E9 61 FC FF FF                  jmp 0x14037f4a5
0037F844  44 89 54 24 5C                  mov dword ptr [rsp + 0x5c], r10d
0037F849  E9 E2 FE FF FF                  jmp 0x14037f730
0037F84E  B1 02                           mov cl, 2
0037F850  C6 43 06 00                     mov byte ptr [rbx + 6], 0
0037F854  E8 47 B5 07 00                  call 0x1403fada0
0037F859  E9 29 FC FF FF                  jmp 0x14037f487
0037F85E  2C 03                           sub al, 3
0037F860  3C 03                           cmp al, 3
0037F862  0F 86 70 FF FF FF               jbe 0x14037f7d8
0037F868  B3 02                           mov bl, 2
0037F86A  44 8B A6 18 02 00 00            mov r12d, dword ptr [rsi + 0x218]
0037F871  45 85 E4                        test r12d, r12d
0037F874  0F 88 DB FE FF FF               js 0x14037f755
0037F87A  4E 8B 34 E2                     mov r14, qword ptr [rdx + r12*8]
0037F87E  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0037F883  49 8B CE                        mov rcx, r14
0037F886  33 D2                           xor edx, edx
0037F888  E8 D3 F4 F8 FF                  call 0x14030ed60
0037F88D  49 3B 76 08                     cmp rsi, qword ptr [r14 + 8]
0037F891  0F 84 41 FF FF FF               je 0x14037f7d8
0037F897  0F B6 86 84 01 00 00            movzx eax, byte ptr [rsi + 0x184]
0037F89E  3C 02                           cmp al, 2
0037F8A0  0F 85 79 01 00 00               jne 0x14037fa1f
0037F8A6  8B 86 18 02 00 00               mov eax, dword ptr [rsi + 0x218]
0037F8AC  41 3B C4                        cmp eax, r12d
0037F8AF  0F 85 6A 01 00 00               jne 0x14037fa1f
0037F8B5  B9 4A 00 00 00                  mov ecx, 0x4a
0037F8BA  CD 29                           int 0x29
0037F8BC  49 F7 E0                        mul r8
0037F8BF  4D 8B C3                        mov r8, r11
0037F8C2  E9 87 F7 FF FF                  jmp 0x14037f04e
0037F8C7  48 F7 E2                        mul rdx
0037F8CA  E9 9C FC FF FF                  jmp 0x14037f56b
0037F8CF  8B 9E 18 02 00 00               mov ebx, dword ptr [rsi + 0x218]
0037F8D5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0037F8DA  4D 8B CF                        mov r9, r15
0037F8DD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0037F8E2  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0037F8E7  49 8B D6                        mov rdx, r14
0037F8EA  E8 21 80 E9 FF                  call 0x140217910
0037F8EF  33 D2                           xor edx, edx
0037F8F1  48 89 7E 40                     mov qword ptr [rsi + 0x40], rdi
0037F8F5  41 B8 00 01 00 00               mov r8d, 0x100
0037F8FB  48 C7 45 C0 01 00 20 00         mov qword ptr [rbp - 0x40], 0x200001
0037F903  48 8D 4D C8                     lea rcx, [rbp - 0x38]
0037F907  E8 34 73 34 00                  call 0x1406c6c40
0037F90C  48 8B 05 9D 38 BA 00            mov rax, qword ptr [rip + 0xba389d]
0037F913  44 8B 04 98                     mov r8d, dword ptr [rax + rbx*4]
0037F917  41 8B C8                        mov ecx, r8d
0037F91A  0F B7 45 C0                     movzx eax, word ptr [rbp - 0x40]
0037F91E  41 83 E0 3F                     and r8d, 0x3f
0037F922  C1 E9 06                        shr ecx, 6
0037F925  3B C1                           cmp eax, ecx
0037F927  0F 86 D4 01 00 00               jbe 0x14037fb01
0037F92D  48 8D 55 C8                     lea rdx, [rbp - 0x38]
0037F931  41 8B C0                        mov eax, r8d
0037F934  48 8D 14 CA                     lea rdx, [rdx + rcx*8]
0037F938  48 8B 0A                        mov rcx, qword ptr [rdx]
0037F93B  48 0F AB C1                     bts rcx, rax
0037F93F  48 89 0A                        mov qword ptr [rdx], rcx
0037F942  44 0F 20 C1                     mov rcx, cr8
0037F946  B8 0C 00 00 00                  mov eax, 0xc
0037F94B  44 0F 22 C0                     mov cr8, rax
0037F94F  39 3D CB 73 C4 00               cmp dword ptr [rip + 0xc473cb], edi
0037F955  0F 85 D3 00 00 00               jne 0x14037fa2e
0037F95B  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0037F964  48 8D 05 E5 EB 11 00            lea rax, [rip + 0x11ebe5]
0037F96B  0F 57 C0                        xorps xmm0, xmm0
0037F96E  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0037F972  4C 8D 4D A0                     lea r9, [rbp - 0x60]
0037F976  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
0037F97A  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0037F97E  48 C7 44 24 20 05 00 00 00      mov qword ptr [rsp + 0x20], 5
0037F987  33 D2                           xor edx, edx
0037F989  F3 0F 7F 45 A0                  movdqu xmmword ptr [rbp - 0x60], xmm0
0037F98E  E8 2D 1A F9 FF                  call 0x1403113c0
0037F993  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0037F99C  E8 CF EC F4 FF                  call 0x1402ce670
0037F9A1  0F 31                           rdtsc
0037F9A3  48 C1 E2 20                     shl rdx, 0x20
0037F9A7  48 0B C2                        or rax, rdx
0037F9AA  49 89 45 00                     mov qword ptr [r13], rax
0037F9AE  4C 8B 66 48                     mov r12, qword ptr [rsi + 0x48]
0037F9B2  E9 68 FE FF FF                  jmp 0x14037f81f
0037F9B7  44 8B A6 18 02 00 00            mov r12d, dword ptr [rsi + 0x218]
0037F9BE  45 85 E4                        test r12d, r12d
0037F9C1  79 2F                           jns 0x14037f9f2
0037F9C3  41 8B C4                        mov eax, r12d
0037F9C6  0F BA F0 1F                     btr eax, 0x1f
0037F9CA  F7 05 64 71 C4 00 00 00 20 00   test dword ptr [rip + 0xc47164], 0x200000
0037F9D4  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0037F9D8  4C 8B B8 48 8E 00 00            mov r15, qword ptr [rax + 0x8e48]
0037F9DF  75 5A                           jne 0x14037fa3b
0037F9E1  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
0037F9E5  F0 49 0F BA 2F 00               lock bts qword ptr [r15], 0
0037F9EB  73 6A                           jae 0x14037fa57
0037F9ED  E9 56 4B 36 00                  jmp 0x1406e4548
0037F9F2  4E 8B 34 E2                     mov r14, qword ptr [rdx + r12*8]
0037F9F6  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0037F9FB  49 8B CE                        mov rcx, r14
0037F9FE  33 D2                           xor edx, edx
0037FA00  E8 5B F3 F8 FF                  call 0x14030ed60
0037FA05  0F B6 86 84 01 00 00            movzx eax, byte ptr [rsi + 0x184]
0037FA0C  3C 01                           cmp al, 1
0037FA0E  75 0F                           jne 0x14037fa1f
0037FA10  8B 86 18 02 00 00               mov eax, dword ptr [rsi + 0x218]
0037FA16  41 3B C4                        cmp eax, r12d
0037FA19  0F 84 B9 FD FF FF               je 0x14037f7d8
0037FA1F  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0037FA24  E8 27 A2 01 00                  call 0x140399c50
0037FA29  E9 20 FD FF FF                  jmp 0x14037f74e
0037FA2E  0F B6 D0                        movzx edx, al
0037FA31  E8 C6 5C 17 00                  call 0x1404f56fc
0037FA36  E9 20 FF FF FF                  jmp 0x14037f95b
0037FA3B  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0037FA40  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0037FA45  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0037FA4A  90                              nop
0037FA4B  49 87 17                        xchg qword ptr [r15], rdx
0037FA4E  48 85 D2                        test rdx, rdx
0037FA51  0F 85 9B 00 00 00               jne 0x14037faf2
0037FA57  0F B6 86 84 01 00 00            movzx eax, byte ptr [rsi + 0x184]
0037FA5E  3C 01                           cmp al, 1
0037FA60  75 0F                           jne 0x14037fa71
0037FA62  8B 86 18 02 00 00               mov eax, dword ptr [rsi + 0x218]
0037FA68  41 3B C4                        cmp eax, r12d
0037FA6B  0F 84 67 FD FF FF               je 0x14037f7d8
0037FA71  F7 05 BD 70 C4 00 00 00 20 00   test dword ptr [rip + 0xc470bd], 0x200000
0037FA7B  74 6C                           je 0x14037fae9
0037FA7D  0F 0D 4C 24 40                  prefetchw byte ptr [rsp + 0x40]
0037FA82  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0037FA87  48 85 C0                        test rax, rax
0037FA8A  75 2E                           jne 0x14037faba
0037FA8C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0037FA91  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0037FA96  F0 48 0F B1 39                  lock cmpxchg qword ptr [rcx], rdi
0037FA9B  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0037FAA0  48 8D 15 99 91 C4 00            lea rdx, [rip + 0xc49199]
0037FAA7  48 3B C1                        cmp rax, rcx
0037FAAA  0F 84 A5 FC FF FF               je 0x14037f755
0037FAB0  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0037FAB5  E8 E6 7F E9 FF                  call 0x140217aa0
0037FABA  48 8D 48 08                     lea rcx, [rax + 8]
0037FABE  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
0037FAC3  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0037FAC8  48 8B C2                        mov rax, rdx
0037FACB  48 87 01                        xchg qword ptr [rcx], rax
0037FACE  32 C2                           xor al, dl
0037FAD0  48 8D 15 69 91 C4 00            lea rdx, [rip + 0xc49169]
0037FAD7  A8 04                           test al, 4
0037FAD9  0F 84 76 FC FF FF               je 0x14037f755
0037FADF  E8 3C 81 E9 FF                  call 0x140217c20
0037FAE4  E9 65 FC FF FF                  jmp 0x14037f74e
0037FAE9  F0 49 21 3F                     lock and qword ptr [r15], rdi
0037FAED  E9 5C FC FF FF                  jmp 0x14037f74e
0037FAF2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0037FAF7  E8 B4 83 ED FF                  call 0x140257eb0
0037FAFC  E9 56 FF FF FF                  jmp 0x14037fa57
0037FB01  0F B7 45 C2                     movzx eax, word ptr [rbp - 0x3e]
0037FB05  3B C1                           cmp eax, ecx
0037FB07  0F 86 35 FE FF FF               jbe 0x14037f942
0037FB0D  8D 41 01                        lea eax, [rcx + 1]
0037FB10  66 89 45 C0                     mov word ptr [rbp - 0x40], ax
0037FB14  E9 14 FE FF FF                  jmp 0x14037f92d
0037FB19  0F B6 86 04 02 00 00            movzx eax, byte ptr [rsi + 0x204]
0037FB20  44 8B C0                        mov r8d, eax
0037FB23  83 F8 07                        cmp eax, 7
0037FB26  0F 83 B8 F7 FF FF               jae 0x14037f2e4
0037FB2C  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
0037FB2F  8B CF                           mov ecx, edi
0037FB31  8B 56 50                        mov edx, dword ptr [rsi + 0x50]
0037FB34  3B D0                           cmp edx, eax
0037FB36  0F 46 D0                        cmovbe edx, eax
0037FB39  0F B6 86 05 02 00 00            movzx eax, byte ptr [rsi + 0x205]
0037FB40  3B 15 36 58 C4 00               cmp edx, dword ptr [rip + 0xc45836]
0037FB46  0F 93 C1                        setae cl
0037FB49  42 8D 0C 41                     lea ecx, [rcx + r8*2]
0037FB4D  0F AF 0D 8C 58 C4 00            imul ecx, dword ptr [rip + 0xc4588c]
0037FB54  03 C8                           add ecx, eax
0037FB56  48 8B 83 B0 86 00 00            mov rax, qword ptr [rbx + 0x86b0]
0037FB5D  4C 01 3C C8                     add qword ptr [rax + rcx*8], r15
0037FB61  E9 7E F7 FF FF                  jmp 0x14037f2e4
0037FB66  4C 8B 83 C0 00 00 00            mov r8, qword ptr [rbx + 0xc0]
0037FB6D  48 8B 86 40 02 00 00            mov rax, qword ptr [rsi + 0x240]
0037FB74  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
0037FB7C  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
0037FB81  49 8B 80 80 00 00 00            mov rax, qword ptr [r8 + 0x80]
0037FB88  48 23 D0                        and rdx, rax
0037FB8B  48 3B D0                        cmp rdx, rax
0037FB8E  0F 84 70 F9 FF FF               je 0x14037f504
0037FB94  4C 01 BB A8 86 00 00            add qword ptr [rbx + 0x86a8], r15
0037FB9B  E9 64 F9 FF FF                  jmp 0x14037f504
0037FBA0  41 8B D5                        mov edx, r13d
0037FBA3  E9 05 F6 FF FF                  jmp 0x14037f1ad
0037FBA8  41 8B 09                        mov ecx, dword ptr [r9]
0037FBAB  0F 33                           rdpmc
0037FBAD  48 C1 E2 20                     shl rdx, 0x20
0037FBB1  48 0B C2                        or rax, rdx
0037FBB4  49 89 02                        mov qword ptr [r10], rax
0037FBB7  E9 AB F8 FF FF                  jmp 0x14037f467
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeQueryTotalCycleTimeThread(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m150;
    unsigned __int16 v_stack_m156;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 11057146)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m190 = a2;
    a2 = 0;
    result = memset(v_stack_m158, a2, 264, a4);
    v_rdi = 0;
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D8 = v_xmm0;
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_0037F741;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32) = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34524)) == 0) goto loc_0037F094;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, 264, a4);
    v_stack_m198 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)));
    }
    v_stack_m198 = a2;
    v_r15 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432));
    if ((*(unsigned __int8 *)(v_rip + 12876426)) == 0) goto loc_0037F094;
    if ((*(unsigned __int64 *)(v_r14)) == 0) goto loc_0037F094;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176)) == 0) goto loc_0037F8BC;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552)) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176))));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176))));
loc_0037F04E:
    v_stack_m1B8 = a2;
    v_stack_m1B0 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12876657))));
    a3 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12876657))));
    a3 = (unsigned int)((a3) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_0037F612;
loc_0037F094:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432) = a2;
    result = (*(unsigned __int64 *)(a1 + 72)) + (v_r15);
    *(unsigned __int64 *)(a1 + 72) = result;
    v_stack_m180 = result;
    if (0 != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34488);
        a1 = *(unsigned int *)(a1 + 80);
        result = (result) * (v_r15);
        result = (result) >> (16);
        a1 = (a1) + (result);
        result = 0xFFFFFFFFULL;
        if (a1 > result) { a1 = result; }
        *(unsigned int *)(a1 + 80) = (unsigned int)(a1);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 2))) & (190)) == 0) goto loc_0037F2EE;
    v_r14 = *(unsigned __int8 *)(a1 + 2);
    if (sign_flag) {
        result = *(unsigned __int64 *)(a1 + 544);
        a2 = 1;
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35760);
        a4 = *(unsigned int *)(result + 400);
        result = (unsigned int)(a4);
        result = (unsigned int)((result) >> (13));
        result = (unsigned int)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (unsigned int)((a4) & (511));
        a2 = (unsigned int)((a2) << ((unsigned __int8)(a1)));
        a1 = (unsigned int)((a1) + (-2));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        v_stack_m1C8 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(a3 + a1 * 8);
        a2 = *(unsigned __int64 *)(a1 + a2 * 8 + 8);
        result = *(unsigned __int64 *)(a2 + a4 * 8);
        result = (result) + (v_r15);
        *(unsigned __int64 *)(a2 + a4 * 8) = result;
        v_r14 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 2)) & (127));
    }
    if ((((unsigned __int8)(v_r14)) & (16)) != 0) goto loc_0037F5D7;
loc_0037F156:
    if ((((unsigned __int8)(v_r14)) & (32)) == 0) goto loc_0037F2A3;
    if (*(unsigned __int64 *)(a1 + 1672) == 0) goto loc_0037F29F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) == 0) goto loc_0037FBA0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) == 0) goto loc_0037FBA0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 112)) != 0) goto loc_0037F1A7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528))))) goto loc_0037F1AD;
    goto loc_0037F1AD;
loc_0037F1A7:
loc_0037F1AD:
loc_0037F1B7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434)))) goto loc_0037F1CB;
    a3 = (unsigned int)((0) + 1);
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434) + (2);
    if (((unsigned int)(a3)) < 3) goto loc_0037F1B7;
loc_0037F1CB:
    a1 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132))) & (8));
    a1 = (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(a1 + 1672) + a1 * 8 * 1)) + (v_r15);
    *(unsigned __int64 *)(a2 + *(unsigned __int64 *)(a1 + 1672) + a1 * 8 * 1) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12130378)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1672) + 192))))) goto loc_0037F70D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1672) + 192))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12130378)))));
    result = (unsigned int)(*(unsigned int *)(v_rip + 12130378));
    if (((unsigned int)(a1)) < 32) {
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    }
    if ((*(unsigned int *)(v_rip + 12876606)) != 0) goto loc_0037F242;
    if ((((unsigned int)(*(unsigned __int8 *)(a1 + 516) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037F5BF;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 516))) == 5) goto loc_0037F5BF;
loc_0037F242:
    result = *(unsigned __int8 *)(a1 + 516) - 2;
    if ((*(unsigned __int64 *)(a1 + 1616)) != 0) {
        a1 = (unsigned int)(a3);
        result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336));
        a1 = (a1) + (8);
        a1 = (a1) + (a1);
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (8));
        result = *(unsigned __int64 *)(a1 + 1672) + a1 * 8;
        a1 = *(unsigned __int64 *)(a2 + result * 1);
        a1 = (a1) + (v_r15);
        *(unsigned __int64 *)(a2 + result * 1) = a1;
        a2 = 64;
        result = *(unsigned __int64 *)(a1 + 1616);
        a1 = *(unsigned __int64 *)(result + 1672);
        result = (unsigned int)(a3);
        a3 = 72;
        result = (result) << (4);
        if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336)) != 0) { a2 = (unsigned int)(a3); }
        result = (result) + (a1);
    }
    v_r14 = (unsigned __int8)((v_r14) & (223));
loc_0037F2A3:
    if ((((unsigned __int8)(v_r14)) & (64)) != 0) goto loc_0037F5F9;
loc_0037F2AD:
    if ((*(unsigned __int8 *)(v_rip + 12875818)) != 0) {
        a4 = 0;
        a3 = v_r15;
        a2 = a1;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiUpdateThreadHgsFeedback(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34480)) == 0) goto loc_0037F2E4;
    if ((*(unsigned __int64 *)(a1 + 544)) != (v_rip + 12913714)) goto loc_0037FB19;
loc_0037F2E4:
    if ((((unsigned __int8)(v_r14)) & (190)) != 0) goto loc_0037F4D0;
loc_0037F2EE:
    if (v_stack_m190 != 0) {
        *(unsigned __int64 *)(v_stack_m190) = a2;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34524)) == 0) goto loc_0037F363;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, v_rip + 12913714);
    v_stack_m188 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)));
    }
    v_stack_m188 = a2;
    v_r11 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432));
    v_r15 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552));
    if ((*(unsigned __int8 *)(v_rip + 12875576)) != 0) goto loc_0037F51E;
loc_0037F363:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34560)) + (v_r15);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34560) = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34680)) + (v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34680) = result;
    if (((*(unsigned __int8 *)(a1 + 2)) & (32)) == 0) goto loc_0037F406;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) == 0) goto loc_0037F3C4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) == 0) goto loc_0037F3C4;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 112)) != 0) goto loc_0037F3BD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528))))) goto loc_0037F3C4;
    goto loc_0037F3C4;
loc_0037F3BD:
loc_0037F3C4:
loc_0037F3CD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434)))) goto loc_0037F3E0;
    a1 = (unsigned int)((0) + 1);
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434) + (2);
    if (((unsigned int)(a1)) < 3) goto loc_0037F3CD;
loc_0037F3E0:
    v_rdi = ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336)) != 0) ? 1 : 0;
    v_rdi = (v_rdi) + (0x10F0ULL);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8)) + (v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) = a1;
loc_0037F406:
    if (((*(unsigned __int8 *)(a1 + 2)) & (64)) == 0) goto loc_0037F41C;
    if (*(unsigned __int64 *)(a1 + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 968) + 64) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432) = a2;
    if (((*(unsigned __int8 *)(a1 + 2)) & (2)) == 0) goto loc_0037F478;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 360) + 32) == 0) goto loc_0037F478;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11433154))) == 0) goto loc_0037F478;
loc_0037F45E:
    if (((1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 360) + 32))) != 0) goto loc_0037FBA8;
loc_0037F467:
    v_r14 = (1) + (1);
    v_r10 = (*(unsigned __int64 *)(a1 + 360) + 48) + (24);
    a4 = (v_rip + 12130863) + (4);
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11433154))))) - (1);
    if (condition_is_not_equal) goto loc_0037F45E;
loc_0037F478:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32) = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 6)) != 0) goto loc_0037F84E;
loc_0037F487:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_0037F6D2;
loc_0037F4A0:
loc_0037F4A5:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    v_rsp = (v_rsp) + (480);
    return result;
loc_0037F4D0:
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_0037F4F1;
    result = ((unsigned int)(*(unsigned int *)(v_stack_p18 + 216))) + (*(unsigned __int64 *)(a1 + 104));
loc_0037F4E2:
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_0037F4E2;
loc_0037F4F1:
    if (((*(unsigned __int8 *)(a1 + 2)) & (8)) == 0) goto loc_0037F504;
    if ((*(unsigned __int64 *)(a1 + 544)) != a4) goto loc_0037FB66;
loc_0037F504:
    if ((*(unsigned __int64 *)(a1 + 360)) == v_rdi) goto loc_0037F2EE;
    result = KiEndCounterAccumulation(a1, *(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_0037F2EE;
loc_0037F51E:
    if ((*(unsigned __int64 *)(result)) == v_rdi) goto loc_0037F363;
    v_stack_p70 = v_rdi;
    v_stack_p78 = v_rdi;
    if ((unsigned __int8)(result) == 0) goto loc_0037F8C7;
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) << ((unsigned __int8)((unsigned __int8)(result)));
    a3 = (v_r14) << ((unsigned __int8)((unsigned __int8)(result)));
loc_0037F56B:
    v_stack_p70 = a2;
    v_stack_p78 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12875348))));
    a2 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12875348))));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r10)));
    if (condition_is_equal) goto loc_0037F363;
    goto loc_0037F363;
loc_0037F5BF:
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (*(unsigned __int64 *)(a2 + a2 * 8 + 8)) + (v_r15);
    *(unsigned __int64 *)(a2 + a2 * 8 + 8) = a1;
    goto loc_0037F242;
loc_0037F5D7:
    a1 = (*(unsigned __int64 *)(v_stack_p18 + *(unsigned __int8 *)(a1 + 124) * 8 + 34440)) + (v_r15);
    *(unsigned __int64 *)(v_stack_p18 + *(unsigned __int8 *)(a1 + 124) * 8 + 34440) = a1;
    v_r14 = (unsigned __int8)((v_r14) & (239));
    goto loc_0037F156;
loc_0037F5F9:
    if (*(unsigned __int64 *)(a1 + 968) == 0) goto loc_0037F2AD;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 968) + 64) = (unsigned __int8)(v_rdi);
    goto loc_0037F2AD;
loc_0037F612:
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_0037F638;
    result = (v_r11) >> (4);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) < ((unsigned int)(v_stack_p18 + *(unsigned __int8 *)(a1 + 124) * 8))) goto loc_0037F6FA;
loc_0037F638:
loc_0037F646:
    if (a1 == (*(unsigned __int64 *)(v_stack_p18 + 24))) goto loc_0037F094;
    if ((*(unsigned __int8 *)(a1 + 195)) >= 16) goto loc_0037F6B9;
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_0037F6B9;
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_0037F6B9;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p18 + 216))) + (*(unsigned __int64 *)(a1 + 104));
    if ((*(unsigned __int8 *)(a1 + 195)) >= 16) goto loc_0037F094;
    if (((*(unsigned int *)(a1 + 120)) & (512)) != 0) goto loc_0037F6B9;
loc_0037F690:
    if (((*(unsigned __int8 *)(a1 + 112)) & (2)) != 0) goto loc_0037F6C6;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037F690;
loc_0037F6A2:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + (*(unsigned int *)(a1 + 124)));
    if (condition_is_not_equal) goto loc_0037F6B4;
    if (*(unsigned __int64 *)(a1 + 416) != 0) goto loc_0037F6A2;
loc_0037F6B4:
    if ((unsigned int)(a4) != 0) goto loc_0037F6C6;
loc_0037F6B9:
    if ((*(unsigned __int8 *)(a1 + 195)) >= 8) goto loc_0037F094;
loc_0037F6C6:
    goto loc_0037F094;
loc_0037F6D2:
loc_0037F6D9:
    if ((*(unsigned __int8 *)(a1 + 195)) != 8) goto loc_0037F6D9;
    if ((*(unsigned __int8 *)(a1 + 195)) >= 8) goto loc_0037F4A0;
    result = KiRemoveSystemWorkPriorityKick(*(unsigned __int64 *)(a1 + 416), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a4);
    goto loc_0037F4A0;
loc_0037F6FA:
    goto loc_0037F646;
loc_0037F70D:
    v_stack_p58 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(*(unsigned __int64 *)(a1 + 416))));
    if (((unsigned int)(a2)) >= 32) goto loc_0037F844;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 196))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) | ((unsigned int)(v_r10)));
    v_stack_p5C = (unsigned int)(result);
loc_0037F730:
    *(unsigned __int64 *)(a4 + 192) = v_stack_p58;
    goto loc_0037F21C;
loc_0037F741:
    result = KiAcquireThreadLockRaiseToDpc(a1, v_stack_p30, a3, a4);
loc_0037F74E:
loc_0037F755:
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 388))) != 3) goto loc_0037F7B3;
    if (sign_flag) goto loc_0037F755;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(v_rip + 12883179 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_p38, a4);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12883179 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 16))) goto loc_0037F7D8;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 388)))) goto loc_0037FA1F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0037FA1F;
loc_0037F7B3:
    a1 = (unsigned int)((30) - (1));
    if (condition_is_equal) goto loc_0037F9B7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0037F86A;
    if (((unsigned int)(a1)) != 3) goto loc_0037F7D8;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 112)) & (7));
    if (((unsigned __int8)(result)) != 1) goto loc_0037F85E;
loc_0037F7D8:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) == 2) goto loc_0037F8CF;
    result = *(unsigned __int8 *)(a1 + 113);
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 113)) != 0) {
        a1 = 1;
        result = KeFlushProcessWriteBuffers(a1, a2, v_stack_p38, a4);
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132))) = result;
    v_stack_p20 = v_stack_p40;
    result = KiReleaseThreadStateLock(a1, *(unsigned __int64 *)(v_rip + 12883179 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), v_stack_p38, v_rdi);
    *(unsigned __int64 *)(a1 + 64) = v_rdi;
loc_0037F81F:
    if ((*(unsigned int *)(v_rip + 12875003)) != ((unsigned int)(v_rdi))) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_stack_p30);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_p38, v_rdi);
    }
    goto loc_0037F4A5;
loc_0037F844:
    v_stack_p5C = (unsigned int)(v_r10);
    goto loc_0037F730;
loc_0037F84E:
    *(unsigned __int8 *)(v_stack_p30 + 6) = 0;
    result = HalRequestSoftwareInterrupt(2, a2, v_stack_p38, v_rdi);
    goto loc_0037F487;
loc_0037F85E:
    result = (unsigned __int8)((result) - (3));
    if (((unsigned __int8)(result)) <= 3) goto loc_0037F7D8;
loc_0037F86A:
    if (sign_flag) goto loc_0037F755;
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_p38, v_rdi);
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8) + 8))) goto loc_0037F7D8;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 2) goto loc_0037FA1F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0037FA1F;
loc_0037F8BC:
    goto loc_0037F04E;
loc_0037F8C7:
    goto loc_0037F56B;
loc_0037F8CF:
    v_stack_p20 = v_stack_p40;
    result = KiReleaseThreadStateLock(74, *(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), v_stack_p38, v_rdi);
    a2 = 0;
    *(unsigned __int64 *)(a1 + 64) = v_rdi;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, a2, 256, v_rdi);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12204189) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 4))) & (63));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12204189) + (unsigned int)(*(unsigned int *)(a1 + 536)) * 4))))) >> (6));
    if (((unsigned int)(v_stack_m158)) <= ((unsigned int)(a1))) goto loc_0037FB01;
loc_0037F92D:
    *(unsigned __int64 *)(v_stack_m150 + a1 * 8) = *(unsigned __int64 *)(v_stack_m150 + a1 * 8);
loc_0037F942:
    if ((*(unsigned int *)(v_rip + 12874699)) != ((unsigned int)(v_rdi))) goto loc_0037FA2E;
loc_0037F95B:
    v_stack_m160 = v_rip + 1174501;
    v_stack_m168 = v_rdi;
    v_stack_p20 = 5;
    a2 = 0;
    v_stack_m178 = v_xmm0;
    result = KiIpiSendRequest(*(unsigned __int64 *)(gs_base + (0 + 32)), a2, v_stack_m158, v_stack_m178);
    result = KiIpiStallOnPacketTargetsPrcb(*(unsigned __int64 *)(gs_base + (0 + 32)), *(unsigned __int64 *)(gs_base + (0 + 32)), v_stack_m158, v_stack_m178);
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32))) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132))) = result;
    goto loc_0037F81F;
loc_0037F9B7:
    if (!sign_flag) goto loc_0037F9F2;
    if (((*(unsigned int *)(v_rip + 12874084)) & (0x200000ULL)) != 0) goto loc_0037FA3B;
    v_stack_p54 = (unsigned int)(v_rdi);
    if (condition_is_above_or_equal) goto loc_0037FA57;
loc_0037F9F2:
    a2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(unsigned __int64 *)(a2 + (unsigned int)(*(unsigned int *)(a1 + 536)) * 8), a2, v_stack_p38, v_stack_m178);
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_0037FA1F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0037F7D8;
loc_0037FA1F:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p38, a2, v_stack_p38, v_stack_m178);
    goto loc_0037F74E;
loc_0037FA2E:
    result = KiRaiseIrqlProcessIrqlFlags(v_stack_p38, (unsigned __int8)(result), v_stack_p38, v_stack_m178);
    goto loc_0037F95B;
loc_0037FA3B:
    v_stack_p48 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) * 8) + 36424);
    v_stack_p40 = v_rdi;
    if (v_stack_p40 != 0) goto loc_0037FAF2;
loc_0037FA57:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 388))) != 1) goto loc_0037FA71;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 536))))) goto loc_0037F7D8;
loc_0037FA71:
    if (((*(unsigned int *)(v_rip + 12873917)) & (0x200000ULL)) == 0) goto loc_0037FAE9;
    if (v_stack_p40 != 0) goto loc_0037FABA;
    if (v_stack_p40 == v_stack_p40) goto loc_0037F755;
    result = KxWaitForLockChainValid(v_stack_p40, v_rip + 12882329, v_stack_p38, v_stack_m178);
loc_0037FABA:
    v_stack_p40 = v_rdi;
    result = (unsigned __int8)((v_stack_p48) ^ ((unsigned __int8)(v_stack_p48)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0037F755;
    result = KeWakeAddressAll(result + 8, v_rip + 12882281, v_stack_p38, v_stack_m178);
    goto loc_0037F74E;
loc_0037FAE9:
    goto loc_0037F74E;
loc_0037FAF2:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_rip + 12882281, v_stack_p38, v_stack_m178);
    goto loc_0037FA57;
loc_0037FB01:
    if (((unsigned int)(v_stack_m156)) <= ((unsigned int)(v_stack_p40))) goto loc_0037F942;
    v_stack_m158 = (unsigned __int16)(v_stack_p40 + 1);
    goto loc_0037F92D;
loc_0037FB19:
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 516))) >= 7) goto loc_0037F2E4;
    a2 = (unsigned int)(*(unsigned int *)(a1 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84))); }
    a1 = (((unsigned int)(a2)) >= (*(unsigned int *)(v_rip + 12867638))) ? 1 : 0;
    a1 = (unsigned int)((a1 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 516))) * 2) * (*(unsigned int *)(v_rip + 12867724)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(a1 + 517))));
    goto loc_0037F2E4;
loc_0037FB66:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 192) + 136) * 8 + 8)) & (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 192) + 128));
    if (a2 == (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 192) + 128))) goto loc_0037F504;
    goto loc_0037F504;
loc_0037FBA0:
    goto loc_0037F1AD;
loc_0037FBA8:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132))))) << (32);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a1 + 536)) + 192) + 128)) | (a2);
    *(unsigned __int64 *)(v_r10) = result;
    goto loc_0037F467;
}
```

## 5. (Beta) C Style

```c
int64_t KeQueryTotalCycleTimeThread(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m150;
    uint16_t v_stack_m156;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0xA8B7FA)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m190 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m158, Arg2, 264, a4);
    local_rdi = 0;
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D8 = v_xmm0;
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_0037F741;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20) = 1;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86DC)) == 0) goto loc_0037F094;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, 264, a4);
    v_stack_m198 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)));
    }
    v_stack_m198 = Arg2;
    local_r15 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680));
    if ((*(uint8_t *)(v_rip + 0xC47A8A)) == 0) goto loc_0037F094;
    if ((*(uint64_t *)(local_r14)) == 0) goto loc_0037F094;
    v_stack_m1B8 = 0;
    v_stack_m1B0 = 0;
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0)) == 0) goto loc_0037F8BC;
    a3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8)) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0))));
    a3 = (result) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0))));
loc_0037F04E:
    v_stack_m1B8 = Arg2;
    v_stack_m1B0 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC47B71))));
    a3 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC47B71))));
    a3 = (uint32_t)((a3) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_0037F612;
loc_0037F094:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8) = result;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680) = Arg2;
    result = (*(uint64_t *)(Arg1 + 0x48)) + (local_r15);
    *(uint64_t *)(Arg1 + 0x48) = result;
    v_stack_m180 = result;
    if (0 != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86B8);
        Arg1 = *(uint32_t *)(Arg1 + 0x50);
        result = (result) * (local_r15);
        result = (result) >> (16);
        Arg1 = (Arg1) + (result);
        result = 0xFFFFFFFFULL;
        if (Arg1 > result) { Arg1 = result; }
        *(uint32_t *)(Arg1 + 0x50) = (uint32_t)(Arg1);
    }
    if ((((uint8_t)(*(uint8_t *)(Arg1 + 0x2))) & (190)) == 0) goto loc_0037F2EE;
    local_r14 = *(uint8_t *)(Arg1 + 0x2);
    if (sign_flag) {
        result = *(uint64_t *)(Arg1 + 0x220);
        Arg2 = 1;
        a3 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8BB0);
        a4 = *(uint32_t *)(result + 0x190);
        result = (uint32_t)(a4);
        result = (uint32_t)((result) >> (13));
        result = (uint32_t)((result) & (0x3FFFFULL));
        a4 = (a4) >> (4);
        a4 = (uint32_t)((a4) & (511));
        Arg2 = (uint32_t)((Arg2) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)((Arg1) + (-2));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        v_stack_m1C8 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(a3 + Arg1 * 8);
        Arg2 = *(uint64_t *)(Arg1 + arg2 * 8 + 0x8);
        result = *(uint64_t *)(arg2 + a4 * 8);
        result = (result) + (local_r15);
        *(uint64_t *)(arg2 + a4 * 8) = result;
        local_r14 = (uint8_t)((*(uint8_t *)(Arg1 + 0x2)) & (127));
    }
    if ((((uint8_t)(local_r14)) & (16)) != 0) goto loc_0037F5D7;
loc_0037F156:
    if ((((uint8_t)(local_r14)) & (32)) == 0) goto loc_0037F2A3;
    if (*(uint64_t *)(Arg1 + 0x688) == 0) goto loc_0037F29F;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) == 0) goto loc_0037FBA0;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) == 0) goto loc_0037FBA0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x70)) != 0) goto loc_0037F1A7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210))))) goto loc_0037F1AD;
    goto loc_0037F1AD;
loc_0037F1A7:
loc_0037F1AD:
loc_0037F1B7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A6A)))) goto loc_0037F1CB;
    a3 = (uint32_t)((0) + 1);
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x20)) + 35434) + (2);
    if (((uint32_t)(a3)) < 3) goto loc_0037F1B7;
loc_0037F1CB:
    Arg1 = ((uint32_t)((uint32_t)(a3))) + ((uint32_t)((uint32_t)(a3)));
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84))) & (8));
    Arg1 = (*(uint64_t *)(arg2 + *(uint64_t *)(Arg1 + 0x688) + Arg1 * 8 * 1)) + (local_r15);
    *(uint64_t *)(arg2 + *(uint64_t *)(Arg1 + 0x688) + Arg1 * 8 * 1) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9184A)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x688) + 0xC0))))) goto loc_0037F70D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x688) + 0xC0))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB9184A)))));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xB9184A));
    if (((uint32_t)(Arg1)) < 32) {
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    }
    if ((*(uint32_t *)(v_rip + 0xC47B3E)) != 0) goto loc_0037F242;
    if ((((uint32_t)(*(uint8_t *)(Arg1 + 0x204) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_0037F5BF;
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x204))) == 5) goto loc_0037F5BF;
loc_0037F242:
    result = *(uint8_t *)(Arg1 + 0x204) - 2;
    if ((*(uint64_t *)(Arg1 + 0x650)) != 0) {
        Arg1 = (uint32_t)(a3);
        result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08));
        Arg1 = (Arg1) + (8);
        Arg1 = (Arg1) + (Arg1);
        result = (uint8_t)(-(result));
        Arg2 = (uint32_t)((Arg2) & (8));
        result = *(uint64_t *)(Arg1 + 0x688) + Arg1 * 8;
        Arg1 = *(uint64_t *)(arg2 + result * 1);
        Arg1 = (Arg1) + (local_r15);
        *(uint64_t *)(arg2 + result * 1) = Arg1;
        Arg2 = 64;
        result = *(uint64_t *)(Arg1 + 0x650);
        Arg1 = *(uint64_t *)(result + 0x688);
        result = (uint32_t)(a3);
        a3 = 72;
        result = (result) << (4);
        if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08)) != 0) { Arg2 = (uint32_t)(a3); }
        result = (result) + (Arg1);
    }
    local_r14 = (uint8_t)((local_r14) & (223));
loc_0037F2A3:
    if ((((uint8_t)(local_r14)) & (64)) != 0) goto loc_0037F5F9;
loc_0037F2AD:
    if ((*(uint8_t *)(v_rip + 0xC4782A)) != 0) {
        a4 = 0;
        a3 = local_r15;
        Arg2 = Arg1;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiUpdateThreadHgsFeedback(Arg1, Arg2, a3, a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86B0)) == 0) goto loc_0037F2E4;
    if ((*(uint64_t *)(Arg1 + 0x220)) != (v_rip + 12913714)) goto loc_0037FB19;
loc_0037F2E4:
    if ((((uint8_t)(local_r14)) & (190)) != 0) goto loc_0037F4D0;
loc_0037F2EE:
    if (v_stack_m190 != 0) {
        *(void **)(v_stack_m190) = Arg2;
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86DC)) == 0) goto loc_0037F363;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, v_rip + 12913714);
    v_stack_m188 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)));
    }
    v_stack_m188 = Arg2;
    local_r11 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680));
    local_r15 = (result) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8));
    if ((*(uint8_t *)(v_rip + 0xC47738)) != 0) goto loc_0037F51E;
loc_0037F363:
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8700)) + (local_r15);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8700) = result;
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8778)) + (local_r11);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8778) = result;
    if (((*(uint8_t *)(Arg1 + 0x2)) & (32)) == 0) goto loc_0037F406;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) == 0) goto loc_0037F3C4;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) == 0) goto loc_0037F3C4;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x70)) != 0) goto loc_0037F3BD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210))))) goto loc_0037F3C4;
    goto loc_0037F3C4;
loc_0037F3BD:
loc_0037F3C4:
loc_0037F3CD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A6A)))) goto loc_0037F3E0;
    Arg1 = (uint32_t)((0) + 1);
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20)) + 35434) + (2);
    if (((uint32_t)(Arg1)) < 3) goto loc_0037F3CD;
loc_0037F3E0:
    local_rdi = ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08)) != 0) ? 1 : 0;
    local_rdi = (local_rdi) + (0x10F0ULL);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8)) + (local_r11);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8) = Arg1;
loc_0037F406:
    if (((*(uint8_t *)(Arg1 + 0x2)) & (64)) == 0) goto loc_0037F41C;
    if (*(uint64_t *)(Arg1 + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(Arg1 + 0x3C8) + 0x40) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8) = result;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680) = Arg2;
    if (((*(uint8_t *)(Arg1 + 0x2)) & (2)) == 0) goto loc_0037F478;
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x168) + 0x20) == 0) goto loc_0037F478;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE74C2))) == 0) goto loc_0037F478;
loc_0037F45E:
    if (((1) & (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x168) + 0x20))) != 0) goto loc_0037FBA8;
loc_0037F467:
    local_r14 = (1) + (1);
    local_r10 = (*(uint64_t *)(Arg1 + 0x168) + 48) + (24);
    a4 = (v_rip + 12130863) + (4);
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAE74C2))))) - (1);
    if (condition_is_not_equal) goto loc_0037F45E;
loc_0037F478:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20) = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6)) != 0) goto loc_0037F84E;
loc_0037F487:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_0037F6D2;
loc_0037F4A0:
loc_0037F4A5:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    local_rsp = (local_rsp) + (480);
    return result;
loc_0037F4D0:
    if (*(uint64_t *)(Arg1 + 0x68) == 0) goto loc_0037F4F1;
    result = ((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xD8))) + (*(uint64_t *)(Arg1 + 0x68));
loc_0037F4E2:
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_0037F4E2;
loc_0037F4F1:
    if (((*(uint8_t *)(Arg1 + 0x2)) & (8)) == 0) goto loc_0037F504;
    if ((*(uint64_t *)(Arg1 + 0x220)) != a4) goto loc_0037FB66;
loc_0037F504:
    if ((*(uint64_t *)(Arg1 + 0x168)) == local_rdi) goto loc_0037F2EE;
    result = KiEndCounterAccumulation(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    goto loc_0037F2EE;
loc_0037F51E:
    if ((*(uint64_t *)(result)) == local_rdi) goto loc_0037F363;
    v_stack_p70 = local_rdi;
    v_stack_p78 = local_rdi;
    if ((uint8_t)(result) == 0) goto loc_0037F8C7;
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8) << ((uint8_t)((uint8_t)(result)));
    a3 = (local_r14) << ((uint8_t)((uint8_t)(result)));
loc_0037F56B:
    v_stack_p70 = Arg2;
    v_stack_p78 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC47654))));
    Arg2 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xC47654))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_r10)));
    if (condition_is_equal) goto loc_0037F363;
    goto loc_0037F363;
loc_0037F5BF:
    Arg2 = ((uint32_t)((uint32_t)(a3))) + ((uint32_t)((uint32_t)(a3)));
    Arg1 = (*(uint64_t *)(arg2 + arg2 * 8 + 0x8)) + (local_r15);
    *(uint64_t *)(arg2 + arg2 * 8 + 0x8) = Arg1;
    goto loc_0037F242;
loc_0037F5D7:
    Arg1 = (*(uint64_t *)(v_stack_p18 + *(uint8_t *)(Arg1 + 0x7C) * 8 + 0x8688)) + (local_r15);
    *(uint64_t *)(v_stack_p18 + *(uint8_t *)(Arg1 + 0x7C) * 8 + 0x8688) = Arg1;
    local_r14 = (uint8_t)((local_r14) & (239));
    goto loc_0037F156;
loc_0037F5F9:
    if (*(uint64_t *)(Arg1 + 0x3C8) == 0) goto loc_0037F2AD;
    *(uint8_t *)(*(uint64_t *)(Arg1 + 0x3C8) + 0x40) = (uint8_t)(local_rdi);
    goto loc_0037F2AD;
loc_0037F612:
    if (((*(uint32_t *)(Arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_0037F638;
    result = (local_r11) >> (4);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) < ((uint32_t)(v_stack_p18 + *(uint8_t *)(Arg1 + 0x7C) * 8))) goto loc_0037F6FA;
loc_0037F638:
loc_0037F646:
    if (Arg1 == (*(uint64_t *)(v_stack_p18 + 0x18))) goto loc_0037F094;
    if ((*(uint8_t *)(Arg1 + 0xC3)) >= 16) goto loc_0037F6B9;
    if (*(uint64_t *)(Arg1 + 0x68) == 0) goto loc_0037F6B9;
    if (*(uint64_t *)(Arg1 + 0x68) == 0) goto loc_0037F6B9;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xD8))) + (*(uint64_t *)(Arg1 + 0x68));
    if ((*(uint8_t *)(Arg1 + 0xC3)) >= 16) goto loc_0037F094;
    if (((*(uint32_t *)(Arg1 + 0x78)) & (512)) != 0) goto loc_0037F6B9;
loc_0037F690:
    if (((*(uint8_t *)(Arg1 + 0x70)) & (2)) != 0) goto loc_0037F6C6;
    if (*(uint64_t *)(Arg1 + 0x1A0) != 0) goto loc_0037F690;
loc_0037F6A2:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + (*(uint32_t *)(Arg1 + 0x7C)));
    if (condition_is_not_equal) goto loc_0037F6B4;
    if (*(uint64_t *)(Arg1 + 0x1A0) != 0) goto loc_0037F6A2;
loc_0037F6B4:
    if ((uint32_t)(a4) != 0) goto loc_0037F6C6;
loc_0037F6B9:
    if ((*(uint8_t *)(Arg1 + 0xC3)) >= 8) goto loc_0037F094;
loc_0037F6C6:
    goto loc_0037F094;
loc_0037F6D2:
loc_0037F6D9:
    if ((*(uint8_t *)(Arg1 + 0xC3)) != 8) goto loc_0037F6D9;
    if ((*(uint8_t *)(Arg1 + 0xC3)) >= 8) goto loc_0037F4A0;
    result = KiRemoveSystemWorkPriorityKick(*(uint64_t *)(Arg1 + 0x1A0), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, a4);
    goto loc_0037F4A0;
loc_0037F6FA:
    goto loc_0037F646;
loc_0037F70D:
    v_stack_p58 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(*(uint64_t *)(Arg1 + 0x1A0))));
    if (((uint32_t)(Arg2)) >= 32) goto loc_0037F844;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(a4 + 0xC4))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) | ((uint32_t)(local_r10)));
    v_stack_p5C = (uint32_t)(result);
loc_0037F730:
    *(uint64_t *)(a4 + 0xC0) = v_stack_p58;
    goto loc_0037F21C;
loc_0037F741:
    result = KiAcquireThreadLockRaiseToDpc(Arg1, v_stack_p30, a3, a4);
loc_0037F74E:
loc_0037F755:
    if (((uint32_t)(*(uint8_t *)(Arg1 + 0x184))) != 3) goto loc_0037F7B3;
    if (sign_flag) goto loc_0037F755;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(v_rip + 0xC494EB + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), Arg2, v_stack_p38, a4);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC494EB + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x10))) goto loc_0037F7D8;
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != ((uint8_t)(*(uint8_t *)(Arg1 + 0x184)))) goto loc_0037FA1F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0037FA1F;
loc_0037F7B3:
    Arg1 = (uint32_t)((30) - (1));
    if (condition_is_equal) goto loc_0037F9B7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0037F86A;
    if (((uint32_t)(Arg1)) != 3) goto loc_0037F7D8;
    result = (uint8_t)((*(uint8_t *)(Arg1 + 0x70)) & (7));
    if (((uint8_t)(result)) != 1) goto loc_0037F85E;
loc_0037F7D8:
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) == 2) goto loc_0037F8CF;
    result = *(uint8_t *)(Arg1 + 0x71);
    if ((uint8_t)(*(uint8_t *)(Arg1 + 0x71)) != 0) {
        Arg1 = 1;
        result = KeFlushProcessWriteBuffers(Arg1, Arg2, v_stack_p38, a4);
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84))) = result;
    v_stack_p20 = v_stack_p40;
    result = KiReleaseThreadStateLock(Arg1, *(uint64_t *)(v_rip + 0xC494EB + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), v_stack_p38, local_rdi);
    *(uint64_t *)(Arg1 + 0x40) = local_rdi;
loc_0037F81F:
    if ((*(uint32_t *)(v_rip + 0xC474FB)) != ((uint32_t)(local_rdi))) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(v_stack_p30);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_p38, local_rdi);
    }
    goto loc_0037F4A5;
loc_0037F844:
    v_stack_p5C = (uint32_t)(local_r10);
    goto loc_0037F730;
loc_0037F84E:
    *(uint8_t *)(v_stack_p30 + 0x6) = 0;
    result = HalRequestSoftwareInterrupt(2, Arg2, v_stack_p38, local_rdi);
    goto loc_0037F487;
loc_0037F85E:
    result = (uint8_t)((result) - (3));
    if (((uint8_t)(result)) <= 3) goto loc_0037F7D8;
loc_0037F86A:
    if (sign_flag) goto loc_0037F755;
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(arg2 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), Arg2, v_stack_p38, local_rdi);
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(arg2 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8) + 0x8))) goto loc_0037F7D8;
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 2) goto loc_0037FA1F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0037FA1F;
loc_0037F8BC:
    goto loc_0037F04E;
loc_0037F8C7:
    goto loc_0037F56B;
loc_0037F8CF:
    v_stack_p20 = v_stack_p40;
    result = KiReleaseThreadStateLock(74, *(uint64_t *)(arg2 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), v_stack_p38, local_rdi);
    Arg2 = 0;
    *(uint64_t *)(Arg1 + 0x40) = local_rdi;
    v_stack_m158 = 0x200001ULL;
    result = memset(v_stack_m150, Arg2, 256, local_rdi);
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA389D) + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 4))) & (63));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBA389D) + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 4))))) >> (6));
    if (((uint32_t)(v_stack_m158)) <= ((uint32_t)(Arg1))) goto loc_0037FB01;
loc_0037F92D:
    *(uint64_t *)(v_stack_m150 + Arg1 * 8) = *(uint64_t *)(v_stack_m150 + Arg1 * 8);
loc_0037F942:
    if ((*(uint32_t *)(v_rip + 0xC473CB)) != ((uint32_t)(local_rdi))) goto loc_0037FA2E;
loc_0037F95B:
    v_stack_m160 = v_rip + 1174501;
    v_stack_m168 = local_rdi;
    v_stack_p20 = 5;
    Arg2 = 0;
    v_stack_m178 = v_xmm0;
    result = KiIpiSendRequest(*(uint64_t *)(gs_base + (0 + 0x20)), Arg2, v_stack_m158, v_stack_m178);
    result = KiIpiStallOnPacketTargetsPrcb(*(uint64_t *)(gs_base + (0 + 0x20)), *(uint64_t *)(gs_base + (0 + 0x20)), v_stack_m158, v_stack_m178);
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20))) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84))) = result;
    goto loc_0037F81F;
loc_0037F9B7:
    if (!sign_flag) goto loc_0037F9F2;
    if (((*(uint32_t *)(v_rip + 0xC47164)) & (0x200000ULL)) != 0) goto loc_0037FA3B;
    v_stack_p54 = (uint32_t)(local_rdi);
    if (condition_is_above_or_equal) goto loc_0037FA57;
loc_0037F9F2:
    Arg2 = 0;
    result = KiAcquirePrcbLocksForIsolationUnit(*(uint64_t *)(arg2 + (uint32_t)(*(uint32_t *)(Arg1 + 0x218)) * 8), Arg2, v_stack_p38, v_stack_m178);
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 1) goto loc_0037FA1F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0037F7D8;
loc_0037FA1F:
    result = KiReleasePrcbLocksForIsolationUnit(v_stack_p38, Arg2, v_stack_p38, v_stack_m178);
    goto loc_0037F74E;
loc_0037FA2E:
    result = KiRaiseIrqlProcessIrqlFlags(v_stack_p38, (uint8_t)(result), v_stack_p38, v_stack_m178);
    goto loc_0037F95B;
loc_0037FA3B:
    v_stack_p48 = *(uint64_t *)(*(uint64_t *)(arg2 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) * 8) + 0x8E48);
    v_stack_p40 = local_rdi;
    if (v_stack_p40 != 0) goto loc_0037FAF2;
loc_0037FA57:
    if (((uint8_t)(*(uint8_t *)(Arg1 + 0x184))) != 1) goto loc_0037FA71;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x218))))) goto loc_0037F7D8;
loc_0037FA71:
    if (((*(uint32_t *)(v_rip + 0xC470BD)) & (0x200000ULL)) == 0) goto loc_0037FAE9;
    if (v_stack_p40 != 0) goto loc_0037FABA;
    if (v_stack_p40 == v_stack_p40) goto loc_0037F755;
    result = KxWaitForLockChainValid(v_stack_p40, v_rip + 12882329, v_stack_p38, v_stack_m178);
loc_0037FABA:
    v_stack_p40 = local_rdi;
    result = (uint8_t)((v_stack_p48) ^ ((uint8_t)(v_stack_p48)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0037F755;
    result = KeWakeAddressAll(result + 8, v_rip + 12882281, v_stack_p38, v_stack_m178);
    goto loc_0037F74E;
loc_0037FAE9:
    goto loc_0037F74E;
loc_0037FAF2:
    result = KxWaitForLockOwnerShip(v_stack_p40, v_rip + 12882281, v_stack_p38, v_stack_m178);
    goto loc_0037FA57;
loc_0037FB01:
    if (((uint32_t)(v_stack_m156)) <= ((uint32_t)(v_stack_p40))) goto loc_0037F942;
    v_stack_m158 = (uint16_t)(v_stack_p40 + 1);
    goto loc_0037F92D;
loc_0037FB19:
    if (((uint32_t)(*(uint8_t *)(Arg1 + 0x204))) >= 7) goto loc_0037F2E4;
    Arg2 = (uint32_t)(*(uint32_t *)(Arg1 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x54))); }
    Arg1 = (((uint32_t)(Arg2)) >= (*(uint32_t *)(v_rip + 0xC45836))) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1 + (uint32_t)((uint32_t)(*(uint8_t *)(Arg1 + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xC4588C)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint8_t *)(Arg1 + 0x205))));
    goto loc_0037F2E4;
loc_0037FB66:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x240) + *(uint16_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)) + 0xC0) + 0x88) * 8 + 0x8)) & (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)) + 0xC0) + 0x80));
    if (Arg2 == (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)) + 0xC0) + 0x80))) goto loc_0037F504;
    goto loc_0037F504;
loc_0037FBA0:
    goto loc_0037F1AD;
loc_0037FBA8:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84))))) << (32);
    result = (*(uint64_t *)(*(uint64_t *)((uint32_t)(*(uint32_t *)(Arg1 + 0x218)) + 0xC0) + 0x80)) | (Arg2);
    *(uint64_t *)(local_r10) = result;
    goto loc_0037F467;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037EF20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
