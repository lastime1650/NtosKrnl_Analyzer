# KeUpdateTotalCyclesCurrentThread

- RVA: `0x003FA2B0`–`0x003FAAD9` (길이 `2,089` bytes)
- VA: `0x00000001403FA2B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009848C`
- 디코드: `500`개 명령, `2,089/2,089` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x003FA304` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003FA600` → [KiUpdateThreadHgsFeedback](../37/KiUpdateThreadHgsFeedback_function_0037D790.md) (function, `0x0037D790`)
- `0x003FA653` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003FA83D` → [KiEndCounterAccumulation](../37/KiEndCounterAccumulation_function_0037EEAC.md) (function, `0x0037EEAC`)
- `0x003FA97B` → [KiQueryEffectivePriorityThread](../25/KiQueryEffectivePriorityThread_function_00257BA0.md) (function, `0x00257BA0`)
- `0x003FA9B3` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x003FAA16` → [HalRequestSoftwareInterrupt](HalRequestSoftwareInterrupt_function_003FADA0.md) (function, `0x003FADA0`)

### Direct callers
- [PsQueryTotalCycleTimeProcess](../../page/A2/PsQueryTotalCycleTimeProcess_function_00A26840.md) at `0x00A2686B`
- [KeEnableProfiling](../../page/AC/KeEnableProfiling_function_00ACED24.md) at `0x00ACEDA8`

### Static image references
- `0x003FA33E` → RVA `0x00FC6A95` (`ALMOSTRO`; read)
- `0x003FA389` → RVA `0x00FC6BC6` (`ALMOSTRO`; read)
- `0x003FA39E` → RVA `0x00FC7318` (`ALMOSTRO`; read)
- `0x003FA535` → RVA `0x00F10A44` (`.data`; read)
- `0x003FA55D` → RVA `0x00FC6D60` (`ALMOSTRO`; read)
- `0x003FA5EB` → RVA `0x00FC6ADE` (`ALMOSTRO`; read)
- `0x003FA605` → RVA `0x00FCFF00` (`CACHEALI`; read)
- `0x003FA784` → RVA `0x00E66908` (`.data`; read)
- `0x003FA78E` → RVA `0x00F10E80` (`.data`; read)
- `0x003FAA5A` → RVA `0x00FC537C` (`ALMOSTRO`; read)
- `0x003FAA67` → RVA `0x00FC53E0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FA2B0  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003FA2B5  53                              push rbx
003FA2B6  55                              push rbp
003FA2B7  56                              push rsi
003FA2B8  57                              push rdi
003FA2B9  41 54                           push r12
003FA2BB  41 55                           push r13
003FA2BD  41 56                           push r14
003FA2BF  41 57                           push r15
003FA2C1  48 83 EC 58                     sub rsp, 0x58
003FA2C5  48 8B F1                        mov rsi, rcx
003FA2C8  FA                              cli
003FA2C9  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
003FA2D2  33 FF                           xor edi, edi
003FA2D4  8B EF                           mov ebp, edi
003FA2D6  44 8B FF                        mov r15d, edi
003FA2D9  44 8B F7                        mov r14d, edi
003FA2DC  49 BC 00 03 00 00 80 F7 FF FF   movabs r12, 0xfffff78000000300
003FA2E6  49 BD 60 03 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000360
003FA2F0  C6 43 20 01                     mov byte ptr [rbx + 0x20], 1
003FA2F4  90                              nop
003FA2F5  40 38 BB DC 86 00 00            cmp byte ptr [rbx + 0x86dc], dil
003FA2FC  0F 84 CD 00 00 00               je 0x1403fa3cf
003FA302  33 C9                           xor ecx, ecx
003FA304  E8 D7 44 F8 FF                  call 0x14037e7e0
003FA309  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
003FA310  48 8B E8                        mov rbp, rax
003FA313  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
003FA31A  48 8B D5                        mov rdx, rbp
003FA31D  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003FA322  84 C9                           test cl, cl
003FA324  74 03                           je 0x1403fa329
003FA326  48 D3 E2                        shl rdx, cl
003FA329  48 F7 E2                        mul rdx
003FA32C  4C 8B F2                        mov r14, rdx
003FA32F  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
003FA334  4C 2B B3 80 86 00 00            sub r14, qword ptr [rbx + 0x8680]
003FA33B  4C 8B FA                        mov r15, rdx
003FA33E  40 38 3D 50 C7 BC 00            cmp byte ptr [rip + 0xbcc750], dil
003FA345  0F 84 84 00 00 00               je 0x1403fa3cf
003FA34B  4C 8B 83 F8 86 00 00            mov r8, qword ptr [rbx + 0x86f8]
003FA352  49 39 3C 24                     cmp qword ptr [r12], rdi
003FA356  74 77                           je 0x1403fa3cf
003FA358  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
003FA361  4D 8B 4D 00                     mov r9, qword ptr [r13]
003FA365  0F B6 C8                        movzx ecx, al
003FA368  84 C0                           test al, al
003FA36A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003FA36F  49 8B C1                        mov rax, r9
003FA372  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
003FA377  0F 84 A3 06 00 00               je 0x1403faa20
003FA37D  49 D3 E0                        shl r8, cl
003FA380  49 F7 E0                        mul r8
003FA383  4C 8B C5                        mov r8, rbp
003FA386  49 D3 E0                        shl r8, cl
003FA389  0F BE 0D 36 C8 BC 00            movsx ecx, byte ptr [rip + 0xbcc836]
003FA390  4C 8B D2                        mov r10, rdx
003FA393  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
003FA398  49 8B C1                        mov rax, r9
003FA39B  49 F7 E0                        mul r8
003FA39E  48 8B 05 73 CF BC 00            mov rax, qword ptr [rip + 0xbccf73]
003FA3A5  4C 8B CA                        mov r9, rdx
003FA3A8  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
003FA3AD  49 F7 E2                        mul r10
003FA3B0  48 8B 05 61 CF BC 00            mov rax, qword ptr [rip + 0xbccf61]
003FA3B7  4C 8B D2                        mov r10, rdx
003FA3BA  49 F7 E1                        mul r9
003FA3BD  49 D3 EA                        shr r10, cl
003FA3C0  4C 8B E2                        mov r12, rdx
003FA3C3  49 D3 EC                        shr r12, cl
003FA3C6  45 2B E2                        sub r12d, r10d
003FA3C9  0F 85 6C 05 00 00               jne 0x1403fa93b
003FA3CF  48 89 AB F8 86 00 00            mov qword ptr [rbx + 0x86f8], rbp
003FA3D6  4C 89 BB 80 86 00 00            mov qword ptr [rbx + 0x8680], r15
003FA3DD  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
003FA3E1  49 03 C6                        add rax, r14
003FA3E4  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
003FA3E8  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
003FA3F0  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
003FA3F4  74 23                           je 0x1403fa419
003FA3F6  8B 83 B8 86 00 00               mov eax, dword ptr [rbx + 0x86b8]
003FA3FC  8B 4E 50                        mov ecx, dword ptr [rsi + 0x50]
003FA3FF  49 0F AF C6                     imul rax, r14
003FA403  48 C1 E8 10                     shr rax, 0x10
003FA407  48 03 C8                        add rcx, rax
003FA40A  B8 FF FF FF FF                  mov eax, 0xffffffff
003FA40F  48 3B C8                        cmp rcx, rax
003FA412  48 0F 47 C8                     cmova rcx, rax
003FA416  89 4E 50                        mov dword ptr [rsi + 0x50], ecx
003FA419  0F B6 6E 02                     movzx ebp, byte ptr [rsi + 2]
003FA41D  41 BD 01 00 00 00               mov r13d, 1
003FA423  45 8D 65 63                     lea r12d, [r13 + 0x63]
003FA427  40 F6 C5 BE                     test bpl, 0xbe
003FA42B  0F 84 FB 01 00 00               je 0x1403fa62c
003FA431  40 84 ED                        test bpl, bpl
003FA434  79 57                           jns 0x1403fa48d
003FA436  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
003FA43D  41 8B D5                        mov edx, r13d
003FA440  4C 8B 83 B0 8B 00 00            mov r8, qword ptr [rbx + 0x8bb0]
003FA447  44 8B 88 90 01 00 00            mov r9d, dword ptr [rax + 0x190]
003FA44E  41 8B C1                        mov eax, r9d
003FA451  C1 E8 0D                        shr eax, 0xd
003FA454  25 FF FF 03 00                  and eax, 0x3ffff
003FA459  49 C1 E9 04                     shr r9, 4
003FA45D  0F BD C8                        bsr ecx, eax
003FA460  41 81 E1 FF 01 00 00            and r9d, 0x1ff
003FA467  D3 E2                           shl edx, cl
003FA469  83 C1 FE                        add ecx, -2
003FA46C  33 D0                           xor edx, eax
003FA46E  89 8C 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ecx
003FA475  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
003FA479  48 8B 54 D1 08                  mov rdx, qword ptr [rcx + rdx*8 + 8]
003FA47E  4A 8B 04 CA                     mov rax, qword ptr [rdx + r9*8]
003FA482  49 03 C6                        add rax, r14
003FA485  4A 89 04 CA                     mov qword ptr [rdx + r9*8], rax
003FA489  40 80 E5 7F                     and bpl, 0x7f
003FA48D  40 F6 C5 10                     test bpl, 0x10
003FA491  0F 85 69 04 00 00               jne 0x1403fa900
003FA497  40 F6 C5 20                     test bpl, 0x20
003FA49B  0F 84 40 01 00 00               je 0x1403fa5e1
003FA4A1  4C 8B 8E 88 06 00 00            mov r9, qword ptr [rsi + 0x688]
003FA4A8  4D 85 C9                        test r9, r9
003FA4AB  0F 84 2C 01 00 00               je 0x1403fa5dd
003FA4B1  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
003FA4B8  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
003FA4BF  48 85 C9                        test rcx, rcx
003FA4C2  0F 84 F5 05 00 00               je 0x1403faabd
003FA4C8  48 85 C0                        test rax, rax
003FA4CB  0F 84 EC 05 00 00               je 0x1403faabd
003FA4D1  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
003FA4D5  75 11                           jne 0x1403fa4e8
003FA4D7  8B 50 50                        mov edx, dword ptr [rax + 0x50]
003FA4DA  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
003FA4E0  3B D0                           cmp edx, eax
003FA4E2  72 0A                           jb 0x1403fa4ee
003FA4E4  8B D0                           mov edx, eax
003FA4E6  EB 06                           jmp 0x1403fa4ee
003FA4E8  8B 90 84 00 00 00               mov edx, dword ptr [rax + 0x84]
003FA4EE  44 8B C7                        mov r8d, edi
003FA4F1  48 8D 8B 6A 8A 00 00            lea rcx, [rbx + 0x8a6a]
003FA4F8  0F B7 01                        movzx eax, word ptr [rcx]
003FA4FB  3B D0                           cmp edx, eax
003FA4FD  76 0D                           jbe 0x1403fa50c
003FA4FF  41 FF C0                        inc r8d
003FA502  48 83 C1 02                     add rcx, 2
003FA506  41 83 F8 03                     cmp r8d, 3
003FA50A  72 EC                           jb 0x1403fa4f8
003FA50C  44 0F B6 93 08 8A 00 00         movzx r10d, byte ptr [rbx + 0x8a08]
003FA514  41 0F B6 C2                     movzx eax, r10b
003FA518  41 8B D0                        mov edx, r8d
003FA51B  F6 D8                           neg al
003FA51D  48 1B C9                        sbb rcx, rcx
003FA520  48 03 D2                        add rdx, rdx
003FA523  83 E1 08                        and ecx, 8
003FA526  49 8D 04 09                     lea rax, [r9 + rcx]
003FA52A  48 8B 0C D0                     mov rcx, qword ptr [rax + rdx*8]
003FA52E  49 03 CE                        add rcx, r14
003FA531  48 89 0C D0                     mov qword ptr [rax + rdx*8], rcx
003FA535  8B 05 09 65 B1 00               mov eax, dword ptr [rip + 0xb16509]
003FA53B  41 8B 89 C0 00 00 00            mov ecx, dword ptr [r9 + 0xc0]
003FA542  3B C1                           cmp eax, ecx
003FA544  0F 87 83 04 00 00               ja 0x1403fa9cd
003FA54A  2B C8                           sub ecx, eax
003FA54C  83 F9 20                        cmp ecx, 0x20
003FA54F  73 0C                           jae 0x1403fa55d
003FA551  41 8B C5                        mov eax, r13d
003FA554  D3 E0                           shl eax, cl
003FA556  41 09 81 C4 00 00 00            or dword ptr [r9 + 0xc4], eax
003FA55D  39 3D FD C7 BC 00               cmp dword ptr [rip + 0xbcc7fd], edi
003FA563  75 1E                           jne 0x1403fa583
003FA565  0F B6 8E 04 02 00 00            movzx ecx, byte ptr [rsi + 0x204]
003FA56C  8D 41 FE                        lea eax, [rcx - 2]
003FA56F  A9 FB FF FF FF                  test eax, 0xfffffffb
003FA574  0F 84 6E 03 00 00               je 0x1403fa8e8
003FA57A  80 F9 05                        cmp cl, 5
003FA57D  0F 84 65 03 00 00               je 0x1403fa8e8
003FA583  48 39 BE 50 06 00 00            cmp qword ptr [rsi + 0x650], rdi
003FA58A  74 51                           je 0x1403fa5dd
003FA58C  41 0F B6 C2                     movzx eax, r10b
003FA590  41 8B C8                        mov ecx, r8d
003FA593  48 83 C1 08                     add rcx, 8
003FA597  48 03 C9                        add rcx, rcx
003FA59A  F6 D8                           neg al
003FA59C  48 1B D2                        sbb rdx, rdx
003FA59F  83 E2 08                        and edx, 8
003FA5A2  49 8D 04 C9                     lea rax, [r9 + rcx*8]
003FA5A6  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
003FA5AA  49 03 CE                        add rcx, r14
003FA5AD  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
003FA5B1  45 84 D2                        test r10b, r10b
003FA5B4  48 8B 86 50 06 00 00            mov rax, qword ptr [rsi + 0x650]
003FA5BB  BA 48 00 00 00                  mov edx, 0x48
003FA5C0  48 8B 88 88 06 00 00            mov rcx, qword ptr [rax + 0x688]
003FA5C7  B8 40 00 00 00                  mov eax, 0x40
003FA5CC  0F 45 C2                        cmovne eax, edx
003FA5CF  41 8B D0                        mov edx, r8d
003FA5D2  48 03 D2                        add rdx, rdx
003FA5D5  48 03 C1                        add rax, rcx
003FA5D8  F0 4C 01 34 D0                  lock add qword ptr [rax + rdx*8], r14
003FA5DD  40 80 E5 DF                     and bpl, 0xdf
003FA5E1  40 F6 C5 40                     test bpl, 0x40
003FA5E5  0F 85 37 03 00 00               jne 0x1403fa922
003FA5EB  40 38 3D EC C4 BC 00            cmp byte ptr [rip + 0xbcc4ec], dil
003FA5F2  74 11                           je 0x1403fa605
003FA5F4  45 33 C9                        xor r9d, r9d
003FA5F7  4D 8B C6                        mov r8, r14
003FA5FA  48 8B D6                        mov rdx, rsi
003FA5FD  48 8B CB                        mov rcx, rbx
003FA600  E8 8B 31 F8 FF                  call 0x14037d790
003FA605  4C 8D 0D F4 58 BD 00            lea r9, [rip + 0xbd58f4]
003FA60C  48 39 BB B0 86 00 00            cmp qword ptr [rbx + 0x86b0], rdi
003FA613  74 0D                           je 0x1403fa622
003FA615  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
003FA61C  0F 85 11 04 00 00               jne 0x1403faa33
003FA622  40 F6 C5 BE                     test bpl, 0xbe
003FA626  0F 85 CD 01 00 00               jne 0x1403fa7f9
003FA62C  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
003FA634  48 85 C0                        test rax, rax
003FA637  74 03                           je 0x1403fa63c
003FA639  4C 89 38                        mov qword ptr [rax], r15
003FA63C  48 8B EF                        mov rbp, rdi
003FA63F  4C 8B FF                        mov r15, rdi
003FA642  4C 8B F7                        mov r14, rdi
003FA645  4C 8B DF                        mov r11, rdi
003FA648  40 38 BB DC 86 00 00            cmp byte ptr [rbx + 0x86dc], dil
003FA64F  74 56                           je 0x1403fa6a7
003FA651  33 C9                           xor ecx, ecx
003FA653  E8 88 41 F8 FF                  call 0x14037e7e0
003FA658  0F B6 8B AC 00 00 00            movzx ecx, byte ptr [rbx + 0xac]
003FA65F  48 8B E8                        mov rbp, rax
003FA662  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
003FA669  48 8B D5                        mov rdx, rbp
003FA66C  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003FA671  84 C9                           test cl, cl
003FA673  74 03                           je 0x1403fa678
003FA675  48 D3 E2                        shl rdx, cl
003FA678  48 F7 E2                        mul rdx
003FA67B  4C 8B F5                        mov r14, rbp
003FA67E  4C 8B FA                        mov r15, rdx
003FA681  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
003FA686  48 8B 93 F8 86 00 00            mov rdx, qword ptr [rbx + 0x86f8]
003FA68D  4D 8B DF                        mov r11, r15
003FA690  4C 2B 9B 80 86 00 00            sub r11, qword ptr [rbx + 0x8680]
003FA697  4C 2B F2                        sub r14, rdx
003FA69A  40 38 3D F4 C3 BC 00            cmp byte ptr [rip + 0xbcc3f4], dil
003FA6A1  0F 85 A0 01 00 00               jne 0x1403fa847
003FA6A7  48 8B 83 00 87 00 00            mov rax, qword ptr [rbx + 0x8700]
003FA6AE  49 03 C6                        add rax, r14
003FA6B1  48 89 83 00 87 00 00            mov qword ptr [rbx + 0x8700], rax
003FA6B8  48 8B 83 78 87 00 00            mov rax, qword ptr [rbx + 0x8778]
003FA6BF  49 03 C3                        add rax, r11
003FA6C2  48 89 83 78 87 00 00            mov qword ptr [rbx + 0x8778], rax
003FA6C9  F6 46 02 20                     test byte ptr [rsi + 2], 0x20
003FA6CD  74 7B                           je 0x1403fa74a
003FA6CF  48 8B 8B B0 89 00 00            mov rcx, qword ptr [rbx + 0x89b0]
003FA6D6  48 8B 83 B8 89 00 00            mov rax, qword ptr [rbx + 0x89b8]
003FA6DD  48 85 C9                        test rcx, rcx
003FA6E0  74 26                           je 0x1403fa708
003FA6E2  48 85 C0                        test rax, rax
003FA6E5  74 21                           je 0x1403fa708
003FA6E7  40 38 78 70                     cmp byte ptr [rax + 0x70], dil
003FA6EB  75 14                           jne 0x1403fa701
003FA6ED  44 8B 60 50                     mov r12d, dword ptr [rax + 0x50]
003FA6F1  8B 81 10 02 00 00               mov eax, dword ptr [rcx + 0x210]
003FA6F7  44 3B E0                        cmp r12d, eax
003FA6FA  72 0C                           jb 0x1403fa708
003FA6FC  44 8B E0                        mov r12d, eax
003FA6FF  EB 07                           jmp 0x1403fa708
003FA701  44 8B A0 84 00 00 00            mov r12d, dword ptr [rax + 0x84]
003FA708  8B CF                           mov ecx, edi
003FA70A  48 8D 93 6A 8A 00 00            lea rdx, [rbx + 0x8a6a]
003FA711  0F B7 02                        movzx eax, word ptr [rdx]
003FA714  44 3B E0                        cmp r12d, eax
003FA717  76 0B                           jbe 0x1403fa724
003FA719  FF C1                           inc ecx
003FA71B  48 83 C2 02                     add rdx, 2
003FA71F  83 F9 03                        cmp ecx, 3
003FA722  72 ED                           jb 0x1403fa711
003FA724  40 38 BB 08 8A 00 00            cmp byte ptr [rbx + 0x8a08], dil
003FA72B  8B C1                           mov eax, ecx
003FA72D  40 0F 95 C7                     setne dil
003FA731  48 81 C7 F0 10 00 00            add rdi, 0x10f0
003FA738  48 8D 04 47                     lea rax, [rdi + rax*2]
003FA73C  48 8B 0C C3                     mov rcx, qword ptr [rbx + rax*8]
003FA740  48 8D 14 C3                     lea rdx, [rbx + rax*8]
003FA744  49 03 CB                        add rcx, r11
003FA747  48 89 0A                        mov qword ptr [rdx], rcx
003FA74A  F6 46 02 40                     test byte ptr [rsi + 2], 0x40
003FA74E  74 10                           je 0x1403fa760
003FA750  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
003FA757  48 85 C0                        test rax, rax
003FA75A  74 04                           je 0x1403fa760
003FA75C  44 88 68 40                     mov byte ptr [rax + 0x40], r13b
003FA760  48 89 AB F8 86 00 00            mov qword ptr [rbx + 0x86f8], rbp
003FA767  4C 89 BB 80 86 00 00            mov qword ptr [rbx + 0x8680], r15
003FA76E  F6 46 02 02                     test byte ptr [rsi + 2], 2
003FA772  74 42                           je 0x1403fa7b6
003FA774  48 8B 86 68 01 00 00            mov rax, qword ptr [rsi + 0x168]
003FA77B  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
003FA77F  4D 85 C0                        test r8, r8
003FA782  74 32                           je 0x1403fa7b6
003FA784  8B 0D 7E C1 A6 00               mov ecx, dword ptr [rip + 0xa6c17e]
003FA78A  85 C9                           test ecx, ecx
003FA78C  74 28                           je 0x1403fa7b6
003FA78E  4C 8D 0D EB 66 B1 00            lea r9, [rip + 0xb166eb]
003FA795  44 8B D9                        mov r11d, ecx
003FA798  4C 8D 50 30                     lea r10, [rax + 0x30]
003FA79C  4D 85 C5                        test r13, r8
003FA79F  0F 85 20 03 00 00               jne 0x1403faac5
003FA7A5  4D 03 ED                        add r13, r13
003FA7A8  49 83 C2 18                     add r10, 0x18
003FA7AC  49 83 C1 04                     add r9, 4
003FA7B0  49 83 EB 01                     sub r11, 1
003FA7B4  75 E6                           jne 0x1403fa79c
003FA7B6  90                              nop
003FA7B7  80 7B 06 00                     cmp byte ptr [rbx + 6], 0
003FA7BB  C6 43 20 00                     mov byte ptr [rbx + 0x20], 0
003FA7BF  0F 85 4B 02 00 00               jne 0x1403faa10
003FA7C5  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
003FA7CE  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
003FA7D5  4D 85 C0                        test r8, r8
003FA7D8  0F 85 B7 01 00 00               jne 0x1403fa995
003FA7DE  FB                              sti
003FA7DF  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
003FA7E7  48 83 C4 58                     add rsp, 0x58
003FA7EB  41 5F                           pop r15
003FA7ED  41 5E                           pop r14
003FA7EF  41 5D                           pop r13
003FA7F1  41 5C                           pop r12
003FA7F3  5F                              pop rdi
003FA7F4  5E                              pop rsi
003FA7F5  5D                              pop rbp
003FA7F6  5B                              pop rbx
003FA7F7  C3                              ret
003FA7F8  CC                              int3
003FA7F9  48 8B 4E 68                     mov rcx, qword ptr [rsi + 0x68]
003FA7FD  48 85 C9                        test rcx, rcx
003FA800  74 18                           je 0x1403fa81a
003FA802  8B 83 D8 00 00 00               mov eax, dword ptr [rbx + 0xd8]
003FA808  48 03 C1                        add rax, rcx
003FA80B  4C 01 30                        add qword ptr [rax], r14
003FA80E  48 8B 80 A0 01 00 00            mov rax, qword ptr [rax + 0x1a0]
003FA815  48 85 C0                        test rax, rax
003FA818  75 F1                           jne 0x1403fa80b
003FA81A  F6 46 02 08                     test byte ptr [rsi + 2], 8
003FA81E  74 0D                           je 0x1403fa82d
003FA820  4C 39 8E 20 02 00 00            cmp qword ptr [rsi + 0x220], r9
003FA827  0F 85 53 02 00 00               jne 0x1403faa80
003FA82D  48 39 BE 68 01 00 00            cmp qword ptr [rsi + 0x168], rdi
003FA834  0F 84 F2 FD FF FF               je 0x1403fa62c
003FA83A  48 8B CE                        mov rcx, rsi
003FA83D  E8 6A 46 F8 FF                  call 0x14037eeac
003FA842  E9 E5 FD FF FF                  jmp 0x1403fa62c
003FA847  48 B8 00 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000300
003FA851  48 39 38                        cmp qword ptr [rax], rdi
003FA854  0F 84 4D FE FF FF               je 0x1403fa6a7
003FA85A  A0 69 03 00 00 80 F7 FF FF      movabs al, byte ptr [0xfffff78000000369]
003FA863  49 B9 60 03 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000360
003FA86D  0F B6 C8                        movzx ecx, al
003FA870  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
003FA875  84 C0                           test al, al
003FA877  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
003FA87C  4C 8B C5                        mov r8, rbp
003FA87F  4D 8B 09                        mov r9, qword ptr [r9]
003FA882  49 8B C1                        mov rax, r9
003FA885  0F 84 A0 01 00 00               je 0x1403faa2b
003FA88B  48 D3 E2                        shl rdx, cl
003FA88E  48 F7 E2                        mul rdx
003FA891  49 D3 E0                        shl r8, cl
003FA894  0F BE 0D 2B C3 BC 00            movsx ecx, byte ptr [rip + 0xbcc32b]
003FA89B  4C 8B D2                        mov r10, rdx
003FA89E  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003FA8A3  49 8B C1                        mov rax, r9
003FA8A6  49 F7 E0                        mul r8
003FA8A9  48 8B 05 68 CA BC 00            mov rax, qword ptr [rip + 0xbcca68]
003FA8B0  4C 8B CA                        mov r9, rdx
003FA8B3  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
003FA8B8  49 F7 E2                        mul r10
003FA8BB  48 8B 05 56 CA BC 00            mov rax, qword ptr [rip + 0xbcca56]
003FA8C2  4C 8B D2                        mov r10, rdx
003FA8C5  49 F7 E1                        mul r9
003FA8C8  49 D3 EA                        shr r10, cl
003FA8CB  48 D3 EA                        shr rdx, cl
003FA8CE  41 2B D2                        sub edx, r10d
003FA8D1  0F 84 D0 FD FF FF               je 0x1403fa6a7
003FA8D7  01 93 44 86 00 00               add dword ptr [rbx + 0x8644], edx
003FA8DD  01 93 50 86 00 00               add dword ptr [rbx + 0x8650], edx
003FA8E3  E9 BF FD FF FF                  jmp 0x1403fa6a7
003FA8E8  41 8B D0                        mov edx, r8d
003FA8EB  48 03 D2                        add rdx, rdx
003FA8EE  49 8B 4C D1 08                  mov rcx, qword ptr [r9 + rdx*8 + 8]
003FA8F3  49 03 CE                        add rcx, r14
003FA8F6  49 89 4C D1 08                  mov qword ptr [r9 + rdx*8 + 8], rcx
003FA8FB  E9 83 FC FF FF                  jmp 0x1403fa583
003FA900  0F B6 46 7C                     movzx eax, byte ptr [rsi + 0x7c]
003FA904  48 8D 14 C3                     lea rdx, [rbx + rax*8]
003FA908  48 8B 8A 88 86 00 00            mov rcx, qword ptr [rdx + 0x8688]
003FA90F  49 03 CE                        add rcx, r14
003FA912  48 89 8A 88 86 00 00            mov qword ptr [rdx + 0x8688], rcx
003FA919  40 80 E5 EF                     and bpl, 0xef
003FA91D  E9 75 FB FF FF                  jmp 0x1403fa497
003FA922  48 8B 86 C8 03 00 00            mov rax, qword ptr [rsi + 0x3c8]
003FA929  48 85 C0                        test rax, rax
003FA92C  0F 84 B9 FC FF FF               je 0x1403fa5eb
003FA932  40 88 78 40                     mov byte ptr [rax + 0x40], dil
003FA936  E9 B0 FC FF FF                  jmp 0x1403fa5eb
003FA93B  F7 46 74 00 04 00 00            test dword ptr [rsi + 0x74], 0x400
003FA942  75 19                           jne 0x1403fa95d
003FA944  8B 86 4C 04 00 00               mov eax, dword ptr [rsi + 0x44c]
003FA94A  F3 48 0F B8 D0                  popcnt rdx, rax
003FA94F  48 8B C5                        mov rax, rbp
003FA952  48 C1 E8 04                     shr rax, 4
003FA956  83 E0 1F                        and eax, 0x1f
003FA959  3B C2                           cmp eax, edx
003FA95B  72 60                           jb 0x1403fa9bd
003FA95D  44 01 A3 44 86 00 00            add dword ptr [rbx + 0x8644], r12d
003FA964  44 01 A6 8C 02 00 00            add dword ptr [rsi + 0x28c], r12d
003FA96B  48 3B 73 18                     cmp rsi, qword ptr [rbx + 0x18]
003FA96F  0F 84 5A FA FF FF               je 0x1403fa3cf
003FA975  48 8B D3                        mov rdx, rbx
003FA978  48 8B CE                        mov rcx, rsi
003FA97B  E8 20 D2 E5 FF                  call 0x140257ba0
003FA980  83 F8 08                        cmp eax, 8
003FA983  0F 8D 46 FA FF FF               jge 0x1403fa3cf
003FA989  44 01 A3 6C 86 00 00            add dword ptr [rbx + 0x866c], r12d
003FA990  E9 3A FA FF FF                  jmp 0x1403fa3cf
003FA995  41 0F 0D 08                     prefetchw byte ptr [r8]
003FA999  41 8B 00                        mov eax, dword ptr [r8]
003FA99C  8B D0                           mov edx, eax
003FA99E  0F BA F2 15                     btr edx, 0x15
003FA9A2  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
003FA9A7  75 F3                           jne 0x1403fa99c
003FA9A9  0F BA E0 15                     bt eax, 0x15
003FA9AD  0F 83 2B FE FF FF               jae 0x1403fa7de
003FA9B3  E8 18 88 E6 FF                  call 0x1402631d0
003FA9B8  E9 21 FE FF FF                  jmp 0x1403fa7de
003FA9BD  44 01 A3 48 86 00 00            add dword ptr [rbx + 0x8648], r12d
003FA9C4  44 01 A6 DC 02 00 00            add dword ptr [rsi + 0x2dc], r12d
003FA9CB  EB 9E                           jmp 0x1403fa96b
003FA9CD  8B D0                           mov edx, eax
003FA9CF  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
003FA9D6  2B D1                           sub edx, ecx
003FA9D8  83 FA 20                        cmp edx, 0x20
003FA9DB  73 29                           jae 0x1403faa06
003FA9DD  41 8B 81 C4 00 00 00            mov eax, dword ptr [r9 + 0xc4]
003FA9E4  8B CA                           mov ecx, edx
003FA9E6  D3 E0                           shl eax, cl
003FA9E8  41 0B C5                        or eax, r13d
003FA9EB  89 84 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], eax
003FA9F2  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
003FA9FA  49 89 81 C0 00 00 00            mov qword ptr [r9 + 0xc0], rax
003FAA01  E9 57 FB FF FF                  jmp 0x1403fa55d
003FAA06  44 89 AC 24 B4 00 00 00         mov dword ptr [rsp + 0xb4], r13d
003FAA0E  EB E2                           jmp 0x1403fa9f2
003FAA10  B1 02                           mov cl, 2
003FAA12  C6 43 06 00                     mov byte ptr [rbx + 6], 0
003FAA16  E8 85 03 00 00                  call 0x1403fada0
003FAA1B  E9 A5 FD FF FF                  jmp 0x1403fa7c5
003FAA20  49 F7 E0                        mul r8
003FAA23  4C 8B C5                        mov r8, rbp
003FAA26  E9 5E F9 FF FF                  jmp 0x1403fa389
003FAA2B  48 F7 E2                        mul rdx
003FAA2E  E9 61 FE FF FF                  jmp 0x1403fa894
003FAA33  0F B6 86 04 02 00 00            movzx eax, byte ptr [rsi + 0x204]
003FAA3A  44 8B C0                        mov r8d, eax
003FAA3D  83 F8 07                        cmp eax, 7
003FAA40  0F 83 DC FB FF FF               jae 0x1403fa622
003FAA46  8B 46 54                        mov eax, dword ptr [rsi + 0x54]
003FAA49  8B CF                           mov ecx, edi
003FAA4B  8B 56 50                        mov edx, dword ptr [rsi + 0x50]
003FAA4E  3B D0                           cmp edx, eax
003FAA50  0F 46 D0                        cmovbe edx, eax
003FAA53  0F B6 86 05 02 00 00            movzx eax, byte ptr [rsi + 0x205]
003FAA5A  3B 15 1C A9 BC 00               cmp edx, dword ptr [rip + 0xbca91c]
003FAA60  0F 93 C1                        setae cl
003FAA63  42 8D 0C 41                     lea ecx, [rcx + r8*2]
003FAA67  0F AF 0D 72 A9 BC 00            imul ecx, dword ptr [rip + 0xbca972]
003FAA6E  03 C8                           add ecx, eax
003FAA70  48 8B 83 B0 86 00 00            mov rax, qword ptr [rbx + 0x86b0]
003FAA77  4C 01 34 C8                     add qword ptr [rax + rcx*8], r14
003FAA7B  E9 A2 FB FF FF                  jmp 0x1403fa622
003FAA80  4C 8B 83 C0 00 00 00            mov r8, qword ptr [rbx + 0xc0]
003FAA87  48 8B 86 40 02 00 00            mov rax, qword ptr [rsi + 0x240]
003FAA8E  41 0F B7 88 88 00 00 00         movzx ecx, word ptr [r8 + 0x88]
003FAA96  48 8B 54 C8 08                  mov rdx, qword ptr [rax + rcx*8 + 8]
003FAA9B  49 8B 88 80 00 00 00            mov rcx, qword ptr [r8 + 0x80]
003FAAA2  48 8B C1                        mov rax, rcx
003FAAA5  48 23 C2                        and rax, rdx
003FAAA8  48 3B C1                        cmp rax, rcx
003FAAAB  0F 84 7C FD FF FF               je 0x1403fa82d
003FAAB1  4C 01 B3 A8 86 00 00            add qword ptr [rbx + 0x86a8], r14
003FAAB8  E9 70 FD FF FF                  jmp 0x1403fa82d
003FAABD  41 8B D4                        mov edx, r12d
003FAAC0  E9 29 FA FF FF                  jmp 0x1403fa4ee
003FAAC5  41 8B 09                        mov ecx, dword ptr [r9]
003FAAC8  0F 33                           rdpmc
003FAACA  48 C1 E2 20                     shl rdx, 0x20
003FAACE  48 0B C2                        or rax, rdx
003FAAD1  49 89 02                        mov qword ptr [r10], rax
003FAAD4  E9 CC FC FF FF                  jmp 0x1403fa7a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeUpdateTotalCyclesCurrentThread(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p8;
    unsigned int v_stack_pB0;
    unsigned int v_stack_pB4;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (88);
    v_rdi = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32) = 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34524)) == 0) goto loc_003FA3CF;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    v_stack_m58 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)));
    }
    v_stack_m58 = a2;
    v_r14 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432));
    if ((*(unsigned __int8 *)(v_rip + 12371792)) == 0) goto loc_003FA3CF;
    if ((*(unsigned __int64 *)(v_r12)) == 0) goto loc_003FA3CF;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176)) == 0) goto loc_003FAA20;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552)) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176))));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 176))));
loc_003FA389:
    v_stack_m78 = a2;
    v_stack_m70 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12372022))));
    v_r12 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12372022))));
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(v_r10)));
    if (condition_is_not_equal) goto loc_003FA93B;
loc_003FA3CF:
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432) = a2;
    result = (*(unsigned __int64 *)(a1 + 72)) + (v_r14);
    *(unsigned __int64 *)(a1 + 72) = result;
    v_stack_p20 = result;
    if (0 != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) {
        result = *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34488);
        a1 = *(unsigned int *)(a1 + 80);
        result = (result) * (v_r14);
        result = (result) >> (16);
        a1 = (a1) + (result);
        result = 0xFFFFFFFFULL;
        if (a1 > result) { a1 = result; }
        *(unsigned int *)(a1 + 80) = (unsigned int)(a1);
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 2))) & (190)) == 0) goto loc_003FA62C;
    v_rbp = *(unsigned __int8 *)(a1 + 2);
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
        v_stack_p8 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(a3 + a1 * 8);
        a2 = *(unsigned __int64 *)(a1 + a2 * 8 + 8);
        result = *(unsigned __int64 *)(a2 + a4 * 8);
        result = (result) + (v_r14);
        *(unsigned __int64 *)(a2 + a4 * 8) = result;
        v_rbp = (unsigned __int8)((*(unsigned __int8 *)(a1 + 2)) & (127));
    }
    if ((((unsigned __int8)(v_rbp)) & (16)) != 0) goto loc_003FA900;
loc_003FA497:
    if ((((unsigned __int8)(v_rbp)) & (32)) == 0) goto loc_003FA5E1;
    if (*(unsigned __int64 *)(a1 + 1672) == 0) goto loc_003FA5DD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) == 0) goto loc_003FAABD;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) == 0) goto loc_003FAABD;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 112)) != 0) goto loc_003FA4E8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528))))) goto loc_003FA4EE;
    goto loc_003FA4EE;
loc_003FA4E8:
loc_003FA4EE:
loc_003FA4F8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434)))) goto loc_003FA50C;
    a3 = (unsigned int)((0) + 1);
    a1 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434) + (2);
    if (((unsigned int)(a3)) < 3) goto loc_003FA4F8;
loc_003FA50C:
    result = (unsigned __int8)(-((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336))));
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (unsigned int)((a1) & (8));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1672) + a1 * 1 + a2 * 8)) + (v_r14);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1672) + a1 * 1 + a2 * 8) = a1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11625737)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1672) + 192))))) goto loc_003FA9CD;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 1672) + 192))) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11625737)))));
    result = (unsigned int)(*(unsigned int *)(v_rip + 11625737));
    if (((unsigned int)(a1)) < 32) {
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
    }
    if ((*(unsigned int *)(v_rip + 12371965)) != 0) goto loc_003FA583;
    if ((((unsigned int)(*(unsigned __int8 *)(a1 + 516) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_003FA8E8;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 516))) == 5) goto loc_003FA8E8;
loc_003FA583:
    result = *(unsigned __int8 *)(a1 + 516) - 2;
    if ((*(unsigned __int64 *)(a1 + 1616)) != 0) {
        result = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336));
        a1 = (unsigned int)(a3);
        a1 = (a1) + (8);
        a1 = (a1) + (a1);
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (8));
        result = *(unsigned __int64 *)(a1 + 1672) + a1 * 8;
        a1 = *(unsigned __int64 *)(a2 + result * 1);
        a1 = (a1) + (v_r14);
        *(unsigned __int64 *)(a2 + result * 1) = a1;
        result = *(unsigned __int64 *)(a1 + 1616);
        a2 = 72;
        a1 = *(unsigned __int64 *)(result + 1672);
        result = 64;
        if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336)) != 0) { result = (unsigned int)(a2); }
        a2 = (unsigned int)(a3);
        a2 = (a2) + (a2);
        result = (result) + (a1);
    }
    v_rbp = (unsigned __int8)((v_rbp) & (223));
loc_003FA5E1:
    if ((((unsigned __int8)(v_rbp)) & (64)) != 0) goto loc_003FA922;
loc_003FA5EB:
    if ((*(unsigned __int8 *)(v_rip + 12371180)) != 0) {
        a4 = 0;
        a3 = v_r14;
        a2 = a1;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = KiUpdateThreadHgsFeedback(a1, a2, a3, a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34480)) == 0) goto loc_003FA622;
    if ((*(unsigned __int64 *)(a1 + 544)) != (v_rip + 12409076)) goto loc_003FAA33;
loc_003FA622:
    if ((((unsigned __int8)(v_rbp)) & (190)) != 0) goto loc_003FA7F9;
loc_003FA62C:
    if (v_stack_p10 != 0) {
        *(unsigned __int64 *)(v_stack_p10) = a2;
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34524)) == 0) goto loc_003FA6A7;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, v_rip + 12409076);
    v_stack_m50 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)) != 0) {
        a2 = (result) << ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 172)));
    }
    v_stack_m50 = a2;
    v_r11 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432));
    v_r14 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552));
    if ((*(unsigned __int8 *)(v_rip + 12370932)) != 0) goto loc_003FA847;
loc_003FA6A7:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34560)) + (v_r14);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34560) = result;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34680)) + (v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34680) = result;
    if (((*(unsigned __int8 *)(a1 + 2)) & (32)) == 0) goto loc_003FA74A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) == 0) goto loc_003FA708;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) == 0) goto loc_003FA708;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 112)) != 0) goto loc_003FA701;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35256) + 80)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528))))) goto loc_003FA708;
    goto loc_003FA708;
loc_003FA701:
loc_003FA708:
loc_003FA711:
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132)))) <= ((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434)))) goto loc_003FA724;
    a1 = (unsigned int)((0) + 1);
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + 35434) + (2);
    if (((unsigned int)(a1)) < 3) goto loc_003FA711;
loc_003FA724:
    v_rdi = ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35336)) != 0) ? 1 : 0;
    v_rdi = (v_rdi) + (0x10F0ULL);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8)) + (v_r11);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) = a1;
loc_003FA74A:
    if (((*(unsigned __int8 *)(a1 + 2)) & (64)) == 0) goto loc_003FA760;
    if (*(unsigned __int64 *)(a1 + 968) != 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 968) + 64) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34552) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34432) = a2;
    if (((*(unsigned __int8 *)(a1 + 2)) & (2)) == 0) goto loc_003FA7B6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 360) + 32) == 0) goto loc_003FA7B6;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10928510))) == 0) goto loc_003FA7B6;
loc_003FA79C:
    if (((1) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 360) + 32))) != 0) goto loc_003FAAC5;
loc_003FA7A5:
    v_r13 = (1) + (1);
    v_r10 = (*(unsigned __int64 *)(a1 + 360) + 48) + (24);
    a4 = (v_rip + 11626219) + (4);
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10928510))))) - (1);
    if (condition_is_not_equal) goto loc_003FA79C;
loc_003FA7B6:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 32) = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 6)) != 0) goto loc_003FAA10;
loc_003FA7C5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536) != 0) goto loc_003FA995;
loc_003FA7DE:
    v_rsp = (v_rsp) + (88);
    return v_stack_p20;
loc_003FA7F9:
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_003FA81A;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 216))) + (*(unsigned __int64 *)(a1 + 104));
loc_003FA80B:
    if (*(unsigned __int64 *)(result + 416) != 0) goto loc_003FA80B;
loc_003FA81A:
    if (((*(unsigned __int8 *)(a1 + 2)) & (8)) == 0) goto loc_003FA82D;
    if ((*(unsigned __int64 *)(a1 + 544)) != a4) goto loc_003FAA80;
loc_003FA82D:
    if ((*(unsigned __int64 *)(a1 + 360)) == v_rdi) goto loc_003FA62C;
    result = KiEndCounterAccumulation(a1, *(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536), a4);
    goto loc_003FA62C;
loc_003FA847:
    if ((*(unsigned __int64 *)(result)) == v_rdi) goto loc_003FA6A7;
    v_stack_p30 = v_rdi;
    v_stack_p38 = v_rdi;
    if ((unsigned __int8)(result) == 0) goto loc_003FAA2B;
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32)) + v_rdi + (unsigned int)((unsigned int)(a1)) * 2 * 8) << ((unsigned __int8)((unsigned __int8)(result)));
    a3 = (result) << ((unsigned __int8)((unsigned __int8)(result)));
loc_003FA894:
    v_stack_p30 = a2;
    v_stack_p38 = a2;
    v_r10 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12370731))));
    a2 = (a2) >> ((unsigned __int8)((__int8)(*(unsigned __int8 *)(v_rip + 12370731))));
    a2 = (unsigned int)((a2) - ((unsigned int)(v_r10)));
    if (condition_is_equal) goto loc_003FA6A7;
    goto loc_003FA6A7;
loc_003FA8E8:
    a2 = ((unsigned int)((unsigned int)(a3))) + ((unsigned int)((unsigned int)(a3)));
    a1 = (*(unsigned __int64 *)(a2 + a2 * 8 + 8)) + (v_r14);
    *(unsigned __int64 *)(a2 + a2 * 8 + 8) = a1;
    goto loc_003FA583;
loc_003FA900:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int8 *)(a1 + 124) * 8 + 34440)) + (v_r14);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int8 *)(a1 + 124) * 8 + 34440) = a1;
    v_rbp = (unsigned __int8)((result) & (239));
    goto loc_003FA497;
loc_003FA922:
    if (*(unsigned __int64 *)(a1 + 968) == 0) goto loc_003FA5EB;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 968) + 64) = (unsigned __int8)(v_rdi);
    goto loc_003FA5EB;
loc_003FA93B:
    if (((*(unsigned int *)(a1 + 116)) & (0x400ULL)) != 0) goto loc_003FA95D;
    result = (v_rbp) >> (4);
    result = (unsigned int)((result) & (31));
    if (((unsigned int)(result)) < ((unsigned int)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int8 *)(a1 + 124) * 8))) goto loc_003FA9BD;
loc_003FA95D:
loc_003FA96B:
    if (a1 == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 24))) goto loc_003FA3CF;
    result = KiQueryEffectivePriorityThread(a1, *(unsigned __int64 *)(gs_base + (0 + 32)), a3, a2);
    if (((unsigned int)(result)) >= 8) goto loc_003FA3CF;
    goto loc_003FA3CF;
loc_003FA995:
loc_003FA99C:
    if (((unsigned int)(result)) != 8) goto loc_003FA99C;
    if (((unsigned int)(result)) >= 8) goto loc_003FA7DE;
    result = KiRemoveSystemWorkPriorityKick(a1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), a3, a2);
    goto loc_003FA7DE;
loc_003FA9BD:
    goto loc_003FA96B;
loc_003FA9CD:
    v_stack_pB0 = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(result))) - ((unsigned int)(a1)));
    if (((unsigned int)(a2)) >= 32) goto loc_003FAA06;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 196))) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    result = (unsigned int)((result) | ((unsigned int)(v_r13)));
    v_stack_pB4 = (unsigned int)(result);
loc_003FA9F2:
    *(unsigned __int64 *)(a2 + 192) = v_stack_pB0;
    goto loc_003FA55D;
loc_003FAA06:
    v_stack_pB4 = (unsigned int)(v_r13);
    goto loc_003FA9F2;
loc_003FAA10:
    *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 6) = 0;
    result = HalRequestSoftwareInterrupt(2, a2, a3, a2);
    goto loc_003FA7C5;
loc_003FAA20:
    goto loc_003FA389;
loc_003FAA2B:
    goto loc_003FA894;
loc_003FAA33:
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 516))) >= 7) goto loc_003FA622;
    a2 = (unsigned int)(*(unsigned int *)(a1 + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 84))); }
    a1 = (((unsigned int)(a2)) >= (*(unsigned int *)(v_rip + 12364060))) ? 1 : 0;
    a1 = (unsigned int)((a1 + (unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 516))) * 2) * (*(unsigned int *)(v_rip + 12364146)));
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int8 *)(a1 + 517))));
    goto loc_003FA622;
loc_003FAA80:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 128)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 576) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 136) * 8 + 8));
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 128))) goto loc_003FA82D;
    goto loc_003FA82D;
loc_003FAABD:
    goto loc_003FA4EE;
loc_003FAAC5:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35248) + 528)) + 132))))) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_r10) = result;
    goto loc_003FA7A5;
}
```

## 5. (Beta) C Style

```c
int64_t KeUpdateTotalCyclesCurrentThread(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p8;
    uint32_t v_stack_pB0;
    uint32_t v_stack_pB4;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (88);
    local_rdi = 0;
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20) = 1;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86DC)) == 0) goto loc_003FA3CF;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, a4);
    v_stack_m58 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)));
    }
    v_stack_m58 = Arg2;
    local_r14 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680));
    if ((*(uint8_t *)(v_rip + 0xBCC750)) == 0) goto loc_003FA3CF;
    if ((*(uint64_t *)(local_r12)) == 0) goto loc_003FA3CF;
    v_stack_m78 = 0;
    v_stack_m70 = 0;
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0)) == 0) goto loc_003FAA20;
    a3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8)) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0))));
    a3 = (result) << ((uint8_t)((uint8_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xB0))));
loc_003FA389:
    v_stack_m78 = Arg2;
    v_stack_m70 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xBCC836))));
    local_r12 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xBCC836))));
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(local_r10)));
    if (condition_is_not_equal) goto loc_003FA93B;
loc_003FA3CF:
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8) = result;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680) = Arg2;
    result = (*(uint64_t *)(arg1 + 0x48)) + (local_r14);
    *(uint64_t *)(arg1 + 0x48) = result;
    v_stack_p20 = result;
    if (0 != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) {
        result = *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86B8);
        Arg1 = *(uint32_t *)(arg1 + 0x50);
        result = (result) * (local_r14);
        result = (result) >> (16);
        Arg1 = (Arg1) + (result);
        result = 0xFFFFFFFFULL;
        if (Arg1 > result) { Arg1 = result; }
        *(uint32_t *)(arg1 + 0x50) = (uint32_t)(Arg1);
    }
    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x2))) & (190)) == 0) goto loc_003FA62C;
    local_rbp = *(uint8_t *)(arg1 + 0x2);
    if (sign_flag) {
        result = *(uint64_t *)(arg1 + 0x220);
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
        v_stack_p8 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(a3 + arg1 * 8);
        Arg2 = *(uint64_t *)(arg1 + Arg2 * 8 + 0x8);
        result = *(uint64_t *)(Arg2 + a4 * 8);
        result = (result) + (local_r14);
        *(uint64_t *)(Arg2 + a4 * 8) = result;
        local_rbp = (uint8_t)((*(uint8_t *)(arg1 + 0x2)) & (127));
    }
    if ((((uint8_t)(local_rbp)) & (16)) != 0) goto loc_003FA900;
loc_003FA497:
    if ((((uint8_t)(local_rbp)) & (32)) == 0) goto loc_003FA5E1;
    if (*(uint64_t *)(arg1 + 0x688) == 0) goto loc_003FA5DD;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) == 0) goto loc_003FAABD;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) == 0) goto loc_003FAABD;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x70)) != 0) goto loc_003FA4E8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210))))) goto loc_003FA4EE;
    goto loc_003FA4EE;
loc_003FA4E8:
loc_003FA4EE:
loc_003FA4F8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A6A)))) goto loc_003FA50C;
    a3 = (uint32_t)((0) + 1);
    Arg1 = (*(uint64_t *)(gs_base + (0 + 0x20)) + 35434) + (2);
    if (((uint32_t)(a3)) < 3) goto loc_003FA4F8;
loc_003FA50C:
    result = (uint8_t)(-((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08))));
    Arg2 = ((uint32_t)((uint32_t)(a3))) + ((uint32_t)((uint32_t)(a3)));
    Arg1 = (uint32_t)((Arg1) & (8));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x688) + arg1 * 1 + Arg2 * 8)) + (local_r14);
    *(void **)(*(uint64_t *)(arg1 + 0x688) + arg1 * 1 + Arg2 * 8) = Arg1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB16509)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x688) + 0xC0))))) goto loc_003FA9CD;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x688) + 0xC0))) - ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB16509)))));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xB16509));
    if (((uint32_t)(Arg1)) < 32) {
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
    }
    if ((*(uint32_t *)(v_rip + 0xBCC7FD)) != 0) goto loc_003FA583;
    if ((((uint32_t)(*(uint8_t *)(arg1 + 0x204) - 2)) & (0xFFFFFFFBULL)) == 0) goto loc_003FA8E8;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x204))) == 5) goto loc_003FA8E8;
loc_003FA583:
    result = *(uint8_t *)(arg1 + 0x204) - 2;
    if ((*(uint64_t *)(arg1 + 0x650)) != 0) {
        result = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08));
        Arg1 = (uint32_t)(a3);
        Arg1 = (Arg1) + (8);
        Arg1 = (Arg1) + (Arg1);
        result = (uint8_t)(-(result));
        Arg2 = (uint32_t)((Arg2) & (8));
        result = *(uint64_t *)(arg1 + 0x688) + Arg1 * 8;
        Arg1 = *(uint64_t *)(Arg2 + result * 1);
        Arg1 = (Arg1) + (local_r14);
        *(void **)(Arg2 + result * 1) = Arg1;
        result = *(uint64_t *)(arg1 + 0x650);
        Arg2 = 72;
        Arg1 = *(uint64_t *)(result + 0x688);
        result = 64;
        if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08)) != 0) { result = (uint32_t)(Arg2); }
        Arg2 = (uint32_t)(a3);
        Arg2 = (Arg2) + (Arg2);
        result = (result) + (Arg1);
    }
    local_rbp = (uint8_t)((local_rbp) & (223));
loc_003FA5E1:
    if ((((uint8_t)(local_rbp)) & (64)) != 0) goto loc_003FA922;
loc_003FA5EB:
    if ((*(uint8_t *)(v_rip + 0xBCC4EC)) != 0) {
        a4 = 0;
        a3 = local_r14;
        Arg2 = Arg1;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = KiUpdateThreadHgsFeedback(Arg1, Arg2, a3, a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86B0)) == 0) goto loc_003FA622;
    if ((*(uint64_t *)(arg1 + 0x220)) != (v_rip + 12409076)) goto loc_003FAA33;
loc_003FA622:
    if ((((uint8_t)(local_rbp)) & (190)) != 0) goto loc_003FA7F9;
loc_003FA62C:
    if (v_stack_p10 != 0) {
        *(uint64_t *)(v_stack_p10) = Arg2;
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86DC)) == 0) goto loc_003FA6A7;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, v_rip + 12409076);
    v_stack_m50 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)) != 0) {
        Arg2 = (result) << ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xAC)));
    }
    v_stack_m50 = Arg2;
    local_r11 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680));
    local_r14 = (result) - (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8));
    if ((*(uint8_t *)(v_rip + 0xBCC3F4)) != 0) goto loc_003FA847;
loc_003FA6A7:
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8700)) + (local_r14);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8700) = result;
    result = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8778)) + (local_r11);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8778) = result;
    if (((*(uint8_t *)(arg1 + 0x2)) & (32)) == 0) goto loc_003FA74A;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) == 0) goto loc_003FA708;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) == 0) goto loc_003FA708;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x70)) != 0) goto loc_003FA701;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B8) + 0x50)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210))))) goto loc_003FA708;
    goto loc_003FA708;
loc_003FA701:
loc_003FA708:
loc_003FA711:
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84)))) <= ((uint32_t)(*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A6A)))) goto loc_003FA724;
    Arg1 = (uint32_t)((0) + 1);
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20)) + 35434) + (2);
    if (((uint32_t)(Arg1)) < 3) goto loc_003FA711;
loc_003FA724:
    local_rdi = ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8A08)) != 0) ? 1 : 0;
    local_rdi = (local_rdi) + (0x10F0ULL);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(arg1)) * 2 * 8)) + (local_r11);
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(arg1)) * 2 * 8) = Arg1;
loc_003FA74A:
    if (((*(uint8_t *)(arg1 + 0x2)) & (64)) == 0) goto loc_003FA760;
    if (*(uint64_t *)(arg1 + 0x3C8) != 0) {
        *(uint8_t *)(*(uint64_t *)(arg1 + 0x3C8) + 0x40) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x86F8) = result;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8680) = Arg2;
    if (((*(uint8_t *)(arg1 + 0x2)) & (2)) == 0) goto loc_003FA7B6;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x168) + 0x20) == 0) goto loc_003FA7B6;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA6C17E))) == 0) goto loc_003FA7B6;
loc_003FA79C:
    if (((1) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x168) + 0x20))) != 0) goto loc_003FAAC5;
loc_003FA7A5:
    local_r13 = (1) + (1);
    local_r10 = (*(uint64_t *)(arg1 + 0x168) + 48) + (24);
    a4 = (v_rip + 11626219) + (4);
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA6C17E))))) - (1);
    if (condition_is_not_equal) goto loc_003FA79C;
loc_003FA7B6:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x20) = 0;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6)) != 0) goto loc_003FAA10;
loc_003FA7C5:
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8) != 0) goto loc_003FA995;
loc_003FA7DE:
    local_rsp = (local_rsp) + (88);
    return v_stack_p20;
loc_003FA7F9:
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_003FA81A;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xD8))) + (*(uint64_t *)(arg1 + 0x68));
loc_003FA80B:
    if (*(uint64_t *)(result + 0x1A0) != 0) goto loc_003FA80B;
loc_003FA81A:
    if (((*(uint8_t *)(arg1 + 0x2)) & (8)) == 0) goto loc_003FA82D;
    if ((*(uint64_t *)(arg1 + 0x220)) != a4) goto loc_003FAA80;
loc_003FA82D:
    if ((*(uint64_t *)(arg1 + 0x168)) == local_rdi) goto loc_003FA62C;
    result = KiEndCounterAccumulation(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8), a4);
    goto loc_003FA62C;
loc_003FA847:
    if ((*(uint64_t *)(result)) == local_rdi) goto loc_003FA6A7;
    v_stack_p30 = local_rdi;
    v_stack_p38 = local_rdi;
    if ((uint8_t)(result) == 0) goto loc_003FAA2B;
    Arg2 = (*(uint64_t *)(gs_base + (0 + 0x20)) + local_rdi + (uint32_t)((uint32_t)(Arg1)) * 2 * 8) << ((uint8_t)((uint8_t)(result)));
    a3 = (result) << ((uint8_t)((uint8_t)(result)));
loc_003FA894:
    v_stack_p30 = Arg2;
    v_stack_p38 = Arg2;
    local_r10 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xBCC32B))));
    Arg2 = (Arg2) >> ((uint8_t)((int8_t)(*(uint8_t *)(v_rip + 0xBCC32B))));
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_r10)));
    if (condition_is_equal) goto loc_003FA6A7;
    goto loc_003FA6A7;
loc_003FA8E8:
    Arg2 = ((uint32_t)((uint32_t)(a3))) + ((uint32_t)((uint32_t)(a3)));
    Arg1 = (*(uint64_t *)(Arg2 + Arg2 * 8 + 0x8)) + (local_r14);
    *(void **)(Arg2 + Arg2 * 8 + 0x8) = Arg1;
    goto loc_003FA583;
loc_003FA900:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint8_t *)(arg1 + 0x7C) * 8 + 0x8688)) + (local_r14);
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint8_t *)(arg1 + 0x7C) * 8 + 0x8688) = Arg1;
    local_rbp = (uint8_t)((result) & (239));
    goto loc_003FA497;
loc_003FA922:
    if (*(uint64_t *)(arg1 + 0x3C8) == 0) goto loc_003FA5EB;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x3C8) + 0x40) = (uint8_t)(local_rdi);
    goto loc_003FA5EB;
loc_003FA93B:
    if (((*(uint32_t *)(arg1 + 0x74)) & (0x400ULL)) != 0) goto loc_003FA95D;
    result = (local_rbp) >> (4);
    result = (uint32_t)((result) & (31));
    if (((uint32_t)(result)) < ((uint32_t)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint8_t *)(arg1 + 0x7C) * 8))) goto loc_003FA9BD;
loc_003FA95D:
loc_003FA96B:
    if (Arg1 == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x18))) goto loc_003FA3CF;
    result = KiQueryEffectivePriorityThread(Arg1, *(uint64_t *)(gs_base + (0 + 0x20)), a3, Arg2);
    if (((uint32_t)(result)) >= 8) goto loc_003FA3CF;
    goto loc_003FA3CF;
loc_003FA995:
loc_003FA99C:
    if (((uint32_t)(result)) != 8) goto loc_003FA99C;
    if (((uint32_t)(result)) >= 8) goto loc_003FA7DE;
    result = KiRemoveSystemWorkPriorityKick(Arg1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(a3)))), a3, Arg2);
    goto loc_003FA7DE;
loc_003FA9BD:
    goto loc_003FA96B;
loc_003FA9CD:
    v_stack_pB0 = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(result))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(Arg2)) >= 32) goto loc_003FAA06;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0xC4))) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    result = (uint32_t)((result) | ((uint32_t)(local_r13)));
    v_stack_pB4 = (uint32_t)(result);
loc_003FA9F2:
    *(uint64_t *)(Arg2 + 0xC0) = v_stack_pB0;
    goto loc_003FA55D;
loc_003FAA06:
    v_stack_pB4 = (uint32_t)(local_r13);
    goto loc_003FA9F2;
loc_003FAA10:
    *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x6) = 0;
    result = HalRequestSoftwareInterrupt(2, Arg2, a3, Arg2);
    goto loc_003FA7C5;
loc_003FAA20:
    goto loc_003FA389;
loc_003FAA2B:
    goto loc_003FA894;
loc_003FAA33:
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x204))) >= 7) goto loc_003FA622;
    Arg2 = (uint32_t)(*(uint32_t *)(arg1 + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x54))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x54))); }
    Arg1 = (((uint32_t)(Arg2)) >= (*(uint32_t *)(v_rip + 0xBCA91C))) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1 + (uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x204))) * 2) * (*(uint32_t *)(v_rip + 0xBCA972)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint8_t *)(arg1 + 0x205))));
    goto loc_003FA622;
loc_003FAA80:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x80)) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x240) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x88) * 8 + 0x8));
    if (result == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x80))) goto loc_003FA82D;
    goto loc_003FA82D;
loc_003FAABD:
    goto loc_003FA4EE;
loc_003FAAC5:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x89B0) + 0x210)) + 0x84))))) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_r10) = result;
    goto loc_003FA7A5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x74` | `32` | `R` |
| `Arg1` | `+ 0x28C` | `32` | `R/W` |
| `Arg1` | `+ 0x2DC` | `32` | `R/W` |
| `Arg1` | `+ 0x44C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FA2B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
