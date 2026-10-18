# MiMapUserLargePages

- RVA: `0x003D26F4`–`0x003D2DA1` (길이 `1,709` bytes)
- VA: `0x00000001403D26F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00091708`
- 디코드: `410`개 명령, `1,709/1,709` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x003D2737` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003D277A` → [MiComputePreferredNode](MiComputePreferredNode_function_003D3438.md) (function, `0x003D3438`)
- `0x003D2846` → [MiCreateLargePfnList](MiCreateLargePfnList_function_003D2DA8.md) (function, `0x003D2DA8`)
- `0x003D2A01` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x003D2A67` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003D2B51` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x003D2B91` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x003D2BD6` → [MiInsertLargeUserMapping](MiInsertLargeUserMapping_function_003D3154.md) (function, `0x003D3154`)
- `0x003D2C52` → [MiDemotePfnListChain](../69/MiDemotePfnListChain_function_00698B5C.md) (function, `0x00698B5C`)
- `0x003D2C75` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x003D2C8A` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003D2CBF` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x003D2CD8` → [MiLockWorkingSetForLargeMapping](../4E/MiLockWorkingSetForLargeMapping_function_004E3110.md) (function, `0x004E3110`)
- `0x003D2D15` → [MiWorkingSetIsContended](../2A/MiWorkingSetIsContended_function_002AE520.md) (function, `0x002AE520`)
- `0x003D2D4B` → [MiFlushGraphicsPtes](../4E/MiFlushGraphicsPtes_function_004E1374.md) (function, `0x004E1374`)
- `0x003D2D5B` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)
- `0x003D2D76` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x003D2D97` → [MiLogPerfMemoryRangeEvent](../4D/MiLogPerfMemoryRangeEvent_function_004D9D7C.md) (function, `0x004D9D7C`)

### Direct callers
- [MiCopyLargeVad](../../page/81/MiCopyLargeVad_function_008118A4.md) at `0x00811975`
- [MiReserveUserMemory](../../page/88/MiReserveUserMemory_function_00884498.md) at `0x00884DB9`
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F88E`

### Static image references
- `0x003D2710` → RVA `0x00E0A740` (`.data`; read)
- `0x003D2785` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003D2A50` → RVA `0x00FC6B04` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x003D2C25` → [sub_006E9556](../6E/Unknown_function_006E9556.md) (`tail-transfer`)
  - `0x003D2CB9` → [sub_006E9556 + 0x20](../6E/Unknown_function_006E9556.md) (`tail-transfer`)
  - `0x003D2CC5` → [sub_006E9556 + 0x25](../6E/Unknown_function_006E9556.md) (`tail-transfer`)
  - `0x003D2CFE` → [sub_006E9556 + 0x2D](../6E/Unknown_function_006E9556.md) (`tail-transfer`)
  - `0x003D2D06` → [sub_006E9556 + 0x43](../6E/Unknown_function_006E9556.md) (`tail-transfer`)
  - `0x003D2D70` → [sub_006E9556 + 0xCA](../6E/Unknown_function_006E9556.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003D26F4  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
003D26F9  55                              push rbp
003D26FA  56                              push rsi
003D26FB  57                              push rdi
003D26FC  41 54                           push r12
003D26FE  41 55                           push r13
003D2700  41 56                           push r14
003D2702  41 57                           push r15
003D2704  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
003D2709  48 81 EC 70 01 00 00            sub rsp, 0x170
003D2710  48 8B 05 29 80 A3 00            mov rax, qword ptr [rip + 0xa38029]
003D2717  48 33 C4                        xor rax, rsp
003D271A  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
003D271E  8B DA                           mov ebx, edx
003D2720  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
003D2724  33 D2                           xor edx, edx
003D2726  41 8A F0                        mov sil, r8b
003D2729  4C 8B F9                        mov r15, rcx
003D272C  4D 8B F1                        mov r14, r9
003D272F  48 8D 4D 00                     lea rcx, [rbp]
003D2733  44 8D 42 60                     lea r8d, [rdx + 0x60]
003D2737  E8 04 45 2F 00                  call 0x1406c6c40
003D273C  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
003D2740  0F 57 C0                        xorps xmm0, xmm0
003D2743  25 00 00 20 04                  and eax, 0x4200000
003D2748  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
003D274C  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
003D2751  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003D275A  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
003D2761  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
003D2765  4C 8D A8 00 04 00 00            lea r13, [rax + 0x400]
003D276C  85 DB                           test ebx, ebx
003D276E  0F 85 58 02 00 00               jne 0x1403d29cc
003D2774  49 8B D7                        mov rdx, r15
003D2777  49 8B CD                        mov rcx, r13
003D277A  E8 B9 0C 00 00                  call 0x1403d3438
003D277F  8B F8                           mov edi, eax
003D2781  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
003D2785  4C 8D 1D 74 D8 C2 FF            lea r11, [rip - 0x3d278c]
003D278C  41 0F B6 57 20                  movzx edx, byte ptr [r15 + 0x20]
003D2791  41 BA 01 00 00 00               mov r10d, 1
003D2797  45 0F B6 67 21                  movzx r12d, byte ptr [r15 + 0x21]
003D279C  41 8B 4F 30                     mov ecx, dword ptr [r15 + 0x30]
003D27A0  49 C1 E4 20                     shl r12, 0x20
003D27A4  48 C1 E2 20                     shl rdx, 0x20
003D27A8  45 8D 4A 01                     lea r9d, [r10 + 1]
003D27AC  48 0B D0                        or rdx, rax
003D27AF  41 8B 47 1C                     mov eax, dword ptr [r15 + 0x1c]
003D27B3  4C 0B E0                        or r12, rax
003D27B6  48 C1 E2 0C                     shl rdx, 0xc
003D27BA  49 C1 E4 0C                     shl r12, 0xc
003D27BE  8B C1                           mov eax, ecx
003D27C0  49 81 CC FF 0F 00 00            or r12, 0xfff
003D27C7  48 C1 E8 13                     shr rax, 0x13
003D27CB  4D 03 E2                        add r12, r10
003D27CE  48 89 55 B8                     mov qword ptr [rbp - 0x48], rdx
003D27D2  4D 8B C4                        mov r8, r12
003D27D5  83 E0 03                        and eax, 3
003D27D8  4C 2B C2                        sub r8, rdx
003D27DB  49 C1 E8 0C                     shr r8, 0xc
003D27DF  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
003D27E3  41 83 BC C3 78 45 01 00 10      cmp dword ptr [r11 + rax*8 + 0x14578], 0x10
003D27EC  0F 85 27 04 00 00               jne 0x1403d2c19
003D27F2  41 8B C1                        mov eax, r9d
003D27F5  44 89 4D A8                     mov dword ptr [rbp - 0x58], r9d
003D27F9  4D 8B 8C C3 60 1C 01 00         mov r9, qword ptr [r11 + rax*8 + 0x11c60]
003D2801  B9 04 00 00 00                  mov ecx, 4
003D2806  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
003D280A  48 8D 45 00                     lea rax, [rbp]
003D280E  48 83 60 10 00                  and qword ptr [rax + 0x10], 0
003D2813  48 89 40 08                     mov qword ptr [rax + 8], rax
003D2817  48 89 00                        mov qword ptr [rax], rax
003D281A  48 83 C0 18                     add rax, 0x18
003D281E  49 2B CA                        sub rcx, r10
003D2821  75 EB                           jne 0x1403d280e
003D2823  48 8D 45 00                     lea rax, [rbp]
003D2827  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
003D282B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003D2830  21 4C 24 38                     and dword ptr [rsp + 0x38], ecx
003D2834  48 8D 4D E8                     lea rcx, [rbp - 0x18]
003D2838  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
003D283D  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
003D2842  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
003D2846  E8 5D 05 00 00                  call 0x1403d2da8
003D284B  85 C0                           test eax, eax
003D284D  0F 88 0D 02 00 00               js 0x1403d2a60
003D2853  4C 8B 75 B8                     mov r14, qword ptr [rbp - 0x48]
003D2857  48 8D 15 A2 D7 C2 FF            lea rdx, [rip - 0x3d285e]
003D285E  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
003D2862  4D 8B DE                        mov r11, r14
003D2865  83 64 24 74 00                  and dword ptr [rsp + 0x74], 0
003D286A  33 F6                           xor esi, esi
003D286C  83 64 24 58 00                  and dword ptr [rsp + 0x58], 0
003D2871  33 C9                           xor ecx, ecx
003D2873  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003D2878  45 33 C9                        xor r9d, r9d
003D287B  48 C1 E8 07                     shr rax, 7
003D287F  41 B7 11                        mov r15b, 0x11
003D2882  83 E0 1F                        and eax, 0x1f
003D2885  49 C1 EB 09                     shr r11, 9
003D2889  48 89 75 98                     mov qword ptr [rbp - 0x68], rsi
003D288D  33 DB                           xor ebx, ebx
003D288F  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
003D2893  4D 8B D6                        mov r10, r14
003D2896  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
003D289B  8B 84 82 70 10 01 00            mov eax, dword ptr [rdx + rax*4 + 0x11070]
003D28A2  89 45 A0                        mov dword ptr [rbp - 0x60], eax
003D28A5  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003D28AA  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003D28AF  48 8D 44 24 60                  lea rax, [rsp + 0x60]
003D28B4  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003D28B9  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003D28C3  4C 23 D8                        and r11, rax
003D28C6  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
003D28CA  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003D28D4  48 8B C0                        mov rax, rax
003D28D7  4C 03 D8                        add r11, rax
003D28DA  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
003D28DE  4D 3B F4                        cmp r14, r12
003D28E1  0F 83 48 01 00 00               jae 0x1403d2a2f
003D28E7  8B 75 A8                        mov esi, dword ptr [rbp - 0x58]
003D28EA  41 BE 01 00 00 00               mov r14d, 1
003D28F0  44 8B 44 24 5C                  mov r8d, dword ptr [rsp + 0x5c]
003D28F5  41 3B F0                        cmp esi, r8d
003D28F8  77 52                           ja 0x1403d294c
003D28FA  8B C6                           mov eax, esi
003D28FC  48 8B 8C C2 60 1C 01 00         mov rcx, qword ptr [rdx + rax*8 + 0x11c60]
003D2904  33 D2                           xor edx, edx
003D2906  48 C1 E1 0C                     shl rcx, 0xc
003D290A  49 8B C2                        mov rax, r10
003D290D  48 F7 F1                        div rcx
003D2910  48 85 D2                        test rdx, rdx
003D2913  0F 85 A4 00 00 00               jne 0x1403d29bd
003D2919  49 8B C4                        mov rax, r12
003D291C  49 2B C2                        sub rax, r10
003D291F  48 3B C1                        cmp rax, rcx
003D2922  0F 82 95 00 00 00               jb 0x1403d29bd
003D2928  8B D6                           mov edx, esi
003D292A  8B C2                           mov eax, edx
003D292C  48 8D 0C 40                     lea rcx, [rax + rax*2]
003D2930  48 8D 45 00                     lea rax, [rbp]
003D2934  48 8D 04 C8                     lea rax, [rax + rcx*8]
003D2938  48 39 00                        cmp qword ptr [rax], rax
003D293B  0F 84 FA 02 00 00               je 0x1403d2c3b
003D2941  41 3B D0                        cmp edx, r8d
003D2944  0F 87 02 03 00 00               ja 0x1403d2c4c
003D294A  8B F2                           mov esi, edx
003D294C  8B D6                           mov edx, esi
003D294E  4C 8D 55 00                     lea r10, [rbp]
003D2952  4C 8D 04 52                     lea r8, [rdx + rdx*2]
003D2956  4F 8D 14 C2                     lea r10, [r10 + r8*8]
003D295A  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
003D295E  49 8B 0A                        mov rcx, qword ptr [r10]
003D2961  4C 89 55 C0                     mov qword ptr [rbp - 0x40], r10
003D2965  4C 39 51 08                     cmp qword ptr [rcx + 8], r10
003D2969  75 4B                           jne 0x1403d29b6
003D296B  48 8B 01                        mov rax, qword ptr [rcx]
003D296E  48 39 48 08                     cmp qword ptr [rax + 8], rcx
003D2972  75 42                           jne 0x1403d29b6
003D2974  49 89 02                        mov qword ptr [r10], rax
003D2977  4C 89 50 08                     mov qword ptr [rax + 8], r10
003D297B  48 8D 05 7E D6 C2 FF            lea rax, [rip - 0x3d2982]
003D2982  48 8B 84 D0 60 1C 01 00         mov rax, qword ptr [rax + rdx*8 + 0x11c60]
003D298A  BA 10 00 00 00                  mov edx, 0x10
003D298F  4E 29 74 C5 10                  sub qword ptr [rbp + r8*8 + 0x10], r14
003D2994  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
003D2999  83 FE 02                        cmp esi, 2
003D299C  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
003D29A0  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003D29A5  41 0F 45 D6                     cmovne edx, r14d
003D29A9  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
003D29AD  4C 39 00                        cmp qword ptr [rax], r8
003D29B0  0F 84 D2 00 00 00               je 0x1403d2a88
003D29B6  B9 03 00 00 00                  mov ecx, 3
003D29BB  CD 29                           int 0x29
003D29BD  41 03 F6                        add esi, r14d
003D29C0  48 8D 15 39 D6 C2 FF            lea rdx, [rip - 0x3d29c7]
003D29C7  E9 29 FF FF FF                  jmp 0x1403d28f5
003D29CC  8D 7B FF                        lea edi, [rbx - 1]
003D29CF  E9 AD FD FF FF                  jmp 0x1403d2781
003D29D4  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
003D29D8  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
003D29DC  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
003D29E0  48 8B C3                        mov rax, rbx
003D29E3  48 0F AF C2                     imul rax, rdx
003D29E7  48 8D 0C C1                     lea rcx, [rcx + rax*8]
003D29EB  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
003D29EF  03 C3                           add eax, ebx
003D29F1  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
003D29F5  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
003D29F9  A8 0F                           test al, 0xf
003D29FB  0F 84 0A 03 00 00               je 0x1403d2d0b
003D2A01  E8 DA 49 EA FF                  call 0x1402773e0
003D2A06  85 C0                           test eax, eax
003D2A08  0F 85 14 03 00 00               jne 0x1403d2d22
003D2A0E  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
003D2A12  49 8B DE                        mov rbx, r14
003D2A15  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
003D2A1A  4D 3B D4                        cmp r10, r12
003D2A1D  0F 82 0C 03 00 00               jb 0x1403d2d2f
003D2A23  48 8B 75 98                     mov rsi, qword ptr [rbp - 0x68]
003D2A27  4C 8B 75 B8                     mov r14, qword ptr [rbp - 0x48]
003D2A2B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
003D2A2F  81 7C 24 78 00 00 20 04         cmp dword ptr [rsp + 0x78], 0x4200000
003D2A37  0F 84 02 03 00 00               je 0x1403d2d3f
003D2A3D  48 85 F6                        test rsi, rsi
003D2A40  0F 85 0F 03 00 00               jne 0x1403d2d55
003D2A46  41 80 FF 11                     cmp r15b, 0x11
003D2A4A  0F 85 15 03 00 00               jne 0x1403d2d65
003D2A50  8B 05 AE 40 BF 00               mov eax, dword ptr [rip + 0xbf40ae]
003D2A56  A8 01                           test al, 1
003D2A58  0F 85 22 03 00 00               jne 0x1403d2d80
003D2A5E  33 C0                           xor eax, eax
003D2A60  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
003D2A64  48 33 CC                        xor rcx, rsp
003D2A67  E8 D4 9B 2D 00                  call 0x1406ac640
003D2A6C  48 8B 9C 24 C0 01 00 00         mov rbx, qword ptr [rsp + 0x1c0]
003D2A74  48 81 C4 70 01 00 00            add rsp, 0x170
003D2A7B  41 5F                           pop r15
003D2A7D  41 5E                           pop r14
003D2A7F  41 5D                           pop r13
003D2A81  41 5C                           pop r12
003D2A83  5F                              pop rdi
003D2A84  5E                              pop rsi
003D2A85  5D                              pop rbp
003D2A86  C3                              ret
003D2A87  CC                              int3
003D2A88  48 89 41 08                     mov qword ptr [rcx + 8], rax
003D2A8C  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
003D2A91  4C 89 01                        mov qword ptr [rcx], r8
003D2A94  4D 8B F3                        mov r14, r11
003D2A97  48 89 08                        mov qword ptr [rax], rcx
003D2A9A  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
003D2A9F  83 FE 02                        cmp esi, 2
003D2AA2  73 37                           jae 0x1403d2adb
003D2AA4  B9 02 00 00 00                  mov ecx, 2
003D2AA9  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
003D2AB3  2B CE                           sub ecx, esi
003D2AB5  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
003D2ABF  49 C1 EE 09                     shr r14, 9
003D2AC3  4D 23 F2                        and r14, r10
003D2AC6  49 8B C1                        mov rax, r9
003D2AC9  4C 03 F0                        add r14, rax
003D2ACC  48 83 E9 01                     sub rcx, 1
003D2AD0  75 ED                           jne 0x1403d2abf
003D2AD2  4C 8B 55 C0                     mov r10, qword ptr [rbp - 0x40]
003D2AD6  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
003D2ADB  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
003D2AE0  75 10                           jne 0x1403d2af2
003D2AE2  49 33 DE                        xor rbx, r14
003D2AE5  48 F7 C3 00 F0 FF FF            test rbx, -0x1000
003D2AEC  0F 84 B0 00 00 00               je 0x1403d2ba2
003D2AF2  81 7C 24 78 00 00 20 04         cmp dword ptr [rsp + 0x78], 0x4200000
003D2AFA  0F 84 65 01 00 00               je 0x1403d2c65
003D2B00  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
003D2B04  48 85 DB                        test rbx, rbx
003D2B07  0F 85 77 01 00 00               jne 0x1403d2c84
003D2B0D  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
003D2B12  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
003D2B16  0F 85 85 01 00 00               jne 0x1403d2ca1
003D2B1C  83 F9 01                        cmp ecx, 1
003D2B1F  0F 84 74 01 00 00               je 0x1403d2c99
003D2B25  85 F6                           test esi, esi
003D2B27  0F 84 74 01 00 00               je 0x1403d2ca1
003D2B2D  41 80 FF 11                     cmp r15b, 0x11
003D2B31  0F 85 D5 00 00 00               jne 0x1403d2c0c
003D2B37  85 F6                           test esi, esi
003D2B39  0F 84 8B 01 00 00               je 0x1403d2cca
003D2B3F  41 80 FF 11                     cmp r15b, 0x11
003D2B43  0F 85 9C 01 00 00               jne 0x1403d2ce5
003D2B49  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
003D2B4E  49 8B CD                        mov rcx, r13
003D2B51  E8 9A A0 EA FF                  call 0x14027cbf0
003D2B56  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
003D2B5A  44 8A F8                        mov r15b, al
003D2B5D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
003D2B67  49 8B DE                        mov rbx, r14
003D2B6A  48 C1 EB 09                     shr rbx, 9
003D2B6E  48 23 D8                        and rbx, rax
003D2B71  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003D2B7B  48 8B C0                        mov rax, rax
003D2B7E  48 03 D8                        add rbx, rax
003D2B81  48 89 5D 98                     mov qword ptr [rbp - 0x68], rbx
003D2B85  44 8B C9                        mov r9d, ecx
003D2B88  8D 57 01                        lea edx, [rdi + 1]
003D2B8B  49 8B CE                        mov rcx, r14
003D2B8E  45 8A C7                        mov r8b, r15b
003D2B91  E8 DA D3 EA FF                  call 0x14027ff70
003D2B96  4C 8B 55 C0                     mov r10, qword ptr [rbp - 0x40]
003D2B9A  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
003D2B9E  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
003D2BA2  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
003D2BA6  33 DB                           xor ebx, ebx
003D2BA8  4C 8B 45 B0                     mov r8, qword ptr [rbp - 0x50]
003D2BAC  49 C1 E0 0C                     shl r8, 0xc
003D2BB0  49 03 C0                        add rax, r8
003D2BB3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003D2BB7  49 3B C4                        cmp rax, r12
003D2BBA  0F 82 2E 01 00 00               jb 0x1403d2cee
003D2BC0  8B 45 A0                        mov eax, dword ptr [rbp - 0x60]
003D2BC3  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
003D2BC8  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
003D2BCC  44 8B CE                        mov r9d, esi
003D2BCF  49 8B D3                        mov rdx, r11
003D2BD2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003D2BD6  E8 79 05 00 00                  call 0x1403d3154
003D2BDB  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
003D2BDF  48 8B C3                        mov rax, rbx
003D2BE2  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
003D2BE6  48 FF C3                        inc rbx
003D2BE9  48 0F AF C2                     imul rax, rdx
003D2BED  0F AF CB                        imul ecx, ebx
003D2BF0  48 C1 E0 0C                     shl rax, 0xc
003D2BF4  48 01 45 80                     add qword ptr [rbp - 0x80], rax
003D2BF8  48 83 7D 90 00                  cmp qword ptr [rbp - 0x70], 0
003D2BFD  0F 84 D1 FD FF FF               je 0x1403d29d4
003D2C03  01 4C 24 54                     add dword ptr [rsp + 0x54], ecx
003D2C07  E9 D0 FD FF FF                  jmp 0x1403d29dc
003D2C0C  85 C9                           test ecx, ecx
003D2C0E  0F 84 49 FF FF FF               je 0x1403d2b5d
003D2C14  E9 6C FF FF FF                  jmp 0x1403d2b85
003D2C19  41 B9 00 00 A0 00               mov r9d, 0xa00000
003D2C1F  41 23 C9                        and ecx, r9d
003D2C22  41 3B C9                        cmp ecx, r9d
003D2C25  0F 85 2B 69 31 00               jne 0x1406e9556
003D2C2B  41 8B 84 83 10 3F 01 00         mov eax, dword ptr [r11 + rax*4 + 0x13f10]
003D2C33  89 45 A8                        mov dword ptr [rbp - 0x58], eax
003D2C36  E9 BE FB FF FF                  jmp 0x1403d27f9
003D2C3B  41 03 D6                        add edx, r14d
003D2C3E  41 3B D0                        cmp edx, r8d
003D2C41  0F 86 E3 FC FF FF               jbe 0x1403d292a
003D2C47  E9 F5 FC FF FF                  jmp 0x1403d2941
003D2C4C  8B D6                           mov edx, esi
003D2C4E  48 8D 4D 00                     lea rcx, [rbp]
003D2C52  E8 05 5F 2C 00                  call 0x140698b5c
003D2C57  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
003D2C5C  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
003D2C60  E9 E7 FC FF FF                  jmp 0x1403d294c
003D2C65  45 85 C9                        test r9d, r9d
003D2C68  0F 84 92 FE FF FF               je 0x1403d2b00
003D2C6E  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
003D2C72  41 8B D1                        mov edx, r9d
003D2C75  E8 FA E6 10 00                  call 0x1404e1374
003D2C7A  48 83 65 90 00                  and qword ptr [rbp - 0x70], 0
003D2C7F  E9 7C FE FF FF                  jmp 0x1403d2b00
003D2C84  48 8B D3                        mov rdx, rbx
003D2C87  49 8B CD                        mov rcx, r13
003D2C8A  E8 31 42 E4 FF                  call 0x140216ec0
003D2C8F  48 83 65 98 00                  and qword ptr [rbp - 0x68], 0
003D2C94  E9 74 FE FF FF                  jmp 0x1403d2b0d
003D2C99  85 F6                           test esi, esi
003D2C9B  0F 84 8C FE FF FF               je 0x1403d2b2d
003D2CA1  83 64 24 58 00                  and dword ptr [rsp + 0x58], 0
003D2CA6  41 80 FF 11                     cmp r15b, 0x11
003D2CAA  0F 84 87 FE FF FF               je 0x1403d2b37
003D2CB0  83 F9 01                        cmp ecx, 1
003D2CB3  41 8A D7                        mov dl, r15b
003D2CB6  49 8B CD                        mov rcx, r13
003D2CB9  0F 85 B7 68 31 00               jne 0x1406e9576
003D2CBF  E8 AC BF EA FF                  call 0x14027ec70
003D2CC4  90                              nop
003D2CC5  E9 B1 68 31 00                  jmp 0x1406e957b
003D2CCA  44 8B C7                        mov r8d, edi
003D2CCD  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
003D2CD5  49 8B CD                        mov rcx, r13
003D2CD8  E8 33 04 11 00                  call 0x1404e3110
003D2CDD  44 8A F8                        mov r15b, al
003D2CE0  E9 5A FE FF FF                  jmp 0x1403d2b3f
003D2CE5  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
003D2CE9  E9 1E FF FF FF                  jmp 0x1403d2c0c
003D2CEE  4D 8B CC                        mov r9, r12
003D2CF1  4C 2B C8                        sub r9, rax
003D2CF4  49 8D 46 08                     lea rax, [r14 + 8]
003D2CF8  48 A9 FF 0F 00 00               test rax, 0xfff
003D2CFE  0F 85 7F 68 31 00               jne 0x1406e9583
003D2D04  33 C0                           xor eax, eax
003D2D06  E9 8E 68 31 00                  jmp 0x1406e9599
003D2D0B  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
003D2D0F  49 8B CD                        mov rcx, r13
003D2D12  83 E2 01                        and edx, 1
003D2D15  E8 06 B8 ED FF                  call 0x1402ae520
003D2D1A  85 C0                           test eax, eax
003D2D1C  0F 84 DF FC FF FF               je 0x1403d2a01
003D2D22  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
003D2D2A  E9 DF FC FF FF                  jmp 0x1403d2a0e
003D2D2F  4C 8B 5D 88                     mov r11, qword ptr [rbp - 0x78]
003D2D33  48 8D 15 C6 D2 C2 FF            lea rdx, [rip - 0x3d2d3a]
003D2D3A  E9 A8 FB FF FF                  jmp 0x1403d28e7
003D2D3F  45 85 C9                        test r9d, r9d
003D2D42  0F 84 F5 FC FF FF               je 0x1403d2a3d
003D2D48  41 8B D1                        mov edx, r9d
003D2D4B  E8 24 E6 10 00                  call 0x1404e1374
003D2D50  E9 E8 FC FF FF                  jmp 0x1403d2a3d
003D2D55  48 8B D6                        mov rdx, rsi
003D2D58  49 8B CD                        mov rcx, r13
003D2D5B  E8 60 41 E4 FF                  call 0x140216ec0
003D2D60  E9 E1 FC FF FF                  jmp 0x1403d2a46
003D2D65  83 7C 24 50 01                  cmp dword ptr [rsp + 0x50], 1
003D2D6A  41 8A D7                        mov dl, r15b
003D2D6D  49 8B CD                        mov rcx, r13
003D2D70  0F 85 AA 68 31 00               jne 0x1406e9620
003D2D76  E8 F5 BE EA FF                  call 0x14027ec70
003D2D7B  E9 D0 FC FF FF                  jmp 0x1403d2a50
003D2D80  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
003D2D84  41 B8 1B 00 00 00               mov r8d, 0x1b
003D2D8A  4C 8B 4D E0                     mov r9, qword ptr [rbp - 0x20]
003D2D8E  49 8B CE                        mov rcx, r14
003D2D91  8B 90 D0 01 00 00               mov edx, dword ptr [rax + 0x1d0]
003D2D97  E8 E0 6F 10 00                  call 0x1404d9d7c
003D2D9C  E9 BD FC FF FF                  jmp 0x1403d2a5e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMapUserLargePages(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 10715177)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mD8 = a1;
    a2 = 0;
    result = memset(v_stack_mA8, a2, a2 + 96, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (0x4200000ULL));
    v_stack_m130 = (unsigned int)(result);
    v_stack_mB8 = v_xmm0;
    v_stack_mD0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_003D29CC;
    result = MiComputePreferredNode(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a1, a2 + 96, a4);
loc_003D2781:
    v_r12 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    a2 = (*(unsigned __int8 *)(a1 + 32)) << (32);
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_r12 = (v_r12) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    a2 = (a2) << (12);
    v_r12 = (v_r12) << (12);
    v_r12 = (v_r12) | (0xFFFULL);
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 48))))) >> (19);
    v_r12 = (v_r12) + (1);
    v_stack_mF0 = a2;
    result = (unsigned int)((result) & (3));
    a3 = (v_r12) - (a2);
    a3 = (a3) >> (12);
    v_stack_mC8 = a3;
    if ((*(unsigned int *)(v_rip - 4007820 + result * 8 + 83320)) != 16) goto loc_003D2C19;
    v_stack_m100 = (unsigned int)(1 + 1);
loc_003D27F9:
    v_stack_m14C = (unsigned int)((unsigned int)((unsigned int)(1 + 1)));
loc_003D280E:
    *(unsigned __int64 *)(v_stack_mA8 + 8) = v_stack_mA8;
    *(unsigned __int64 *)(v_stack_mA8) = v_stack_mA8;
    result = (v_stack_mA8) + (24);
    a1 = (4) - (1);
    if (condition_is_not_equal) goto loc_003D280E;
    v_stack_mC0 = a1;
    v_stack_m168 = v_stack_mA8;
    v_stack_m178 = a4;
    v_stack_m180 = a3;
    v_stack_m188 = (unsigned int)((unsigned int)(a2));
    result = MiCreateLargePfnList(v_stack_mC0, a2, a3, *(unsigned __int64 *)(v_rip - 4007820 + (unsigned int)((unsigned int)(1 + 1)) * 8 + 72800));
    if (sign_flag) goto loc_003D2A60;
    v_rsi = 0;
    a1 = 0;
    a4 = 0;
    result = ((unsigned int)(*(unsigned int *)(a1 + 48))) >> (7);
    result = (unsigned int)((result) & (31));
    v_r11 = (v_stack_mF0) >> (9);
    v_stack_m110 = 0;
    v_rbx = 0;
    v_stack_m118 = 0;
    v_stack_m154 = 0;
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4008030 + result * 4 + 69744)));
    v_stack_m140 = v_stack_m148;
    v_stack_m148 = v_stack_m148;
    v_r11 = (v_r11) & (v_stack_m148);
    v_stack_m128 = v_stack_mF0;
    v_r11 = (v_r11) + (v_stack_m148);
    v_stack_m120 = v_r11;
    if (v_stack_mF0 >= v_r12) goto loc_003D2A2F;
loc_003D28E7:
loc_003D28F5:
    if (((unsigned int)((unsigned int)(v_stack_m100))) > ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_003D294C;
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_rip - 4008030 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m100))) * 8 + 72800)) << (12);
    if (0 != 0) goto loc_003D29BD;
    result = (v_r12) - (v_stack_mF0);
    if (result < a1) goto loc_003D29BD;
loc_003D292A:
    if ((*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))) * 2 * 8)) == (v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))) * 2 * 8)) goto loc_003D2C3B;
loc_003D2941:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))) > ((unsigned int)((unsigned int)(v_stack_m14C)))) goto loc_003D2C4C;
loc_003D294C:
    v_stack_mE0 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2;
    v_stack_mE8 = v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8) + 8)) != (v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8)) goto loc_003D29B6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8)) + 8)) != (*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8))) goto loc_003D29B6;
    *(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8)) + 8) = v_stack_mA8 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 2 * 8;
    v_stack_mF8 = *(unsigned __int64 *)(v_rip - 4008322 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) * 8 + 72800);
    a2 = 16;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))))))) != 2) { a2 = 1; }
    v_stack_m138 = a2;
    if ((*(unsigned __int64 *)(v_stack_m140)) == v_stack_m148) goto loc_003D2A88;
loc_003D29B6:
loc_003D29BD:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m100)))))) + (1));
    goto loc_003D28F5;
loc_003D29CC:
    goto loc_003D2781;
loc_003D29D4:
    v_stack_m118 = 1;
    v_stack_m154 = 3;
loc_003D29DC:
    result = (0) * (v_rip - 4008391);
    result = (unsigned int)(((unsigned int)(v_stack_m134)) + (0));
    v_stack_m120 = v_stack_m120 + result * 8;
    v_stack_m134 = (unsigned int)(result);
    if ((((unsigned __int8)(result)) & (15)) == 0) goto loc_003D2D0B;
loc_003D2A01:
    result = KeShouldYieldProcessor(v_stack_m120 + result * 8, v_rip - 4008391, v_stack_m148, a4);
    if ((unsigned int)(result) != 0) goto loc_003D2D22;
loc_003D2A0E:
    if (v_stack_m128 < v_r12) goto loc_003D2D2F;
loc_003D2A2F:
    if (v_stack_m130 == 0x4200000ULL) goto loc_003D2D3F;
loc_003D2A3D:
    if (v_stack_m110 != 0) goto loc_003D2D55;
loc_003D2A46:
    if (17 != 17) goto loc_003D2D65;
loc_003D2A50:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12533934)))) & (1)) != 0) goto loc_003D2D80;
loc_003D2A5E:
    result = 0;
loc_003D2A60:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4008391, v_stack_m148, (unsigned int)(v_stack_m154));
    v_rsp = (v_rsp) + (368);
    return result;
loc_003D2A88:
    *(unsigned __int64 *)(a1 + 8) = result;
    *(unsigned __int64 *)(a1) = v_stack_p60;
    *(unsigned __int64 *)(result) = a1;
    v_stack_p68 = a1;
    if (((unsigned int)(v_stack_m110)) >= 2) goto loc_003D2ADB;
    a1 = (unsigned int)((2) - ((unsigned int)(v_stack_m110)));
loc_003D2ABF:
    v_r14 = (v_r11) >> (9);
    v_r14 = (v_r14) & (v_stack_m128);
    v_r14 = (v_r14) + ((unsigned int)(v_stack_m154));
    a1 = (a1) - (1);
    if (condition_is_not_equal) goto loc_003D2ABF;
loc_003D2ADB:
    if (v_stack_p58 != 0) goto loc_003D2AF2;
    v_rbx = (v_stack_p18) ^ (v_r14);
    if (((v_rbx) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_003D2BA2;
loc_003D2AF2:
    if (v_stack_p78 == 0x4200000ULL) goto loc_003D2C65;
loc_003D2B00:
    if (v_stack_m110 != 0) goto loc_003D2C84;
loc_003D2B0D:
    if (v_stack_p58 != 0) goto loc_003D2CA1;
    if (((unsigned int)((unsigned int)(v_stack_p50))) == 1) goto loc_003D2C99;
    if ((unsigned int)(v_stack_m110) == 0) goto loc_003D2CA1;
loc_003D2B2D:
    if (17 != 17) goto loc_003D2C0C;
loc_003D2B37:
    if ((unsigned int)(v_stack_m110) == 0) goto loc_003D2CCA;
loc_003D2B3F:
    if (17 != 17) goto loc_003D2CE5;
    result = MiLockWorkingSetShared(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_rip - 4008391, v_stack_p60, (unsigned int)(v_stack_p54));
loc_003D2B5D:
    v_rbx = (v_r14) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + (result);
    v_stack_m110 = v_rbx;
loc_003D2B85:
    result = MiMakeSystemAddressValid(v_r14, v_rbx - 1 + 1, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p50))));
loc_003D2BA2:
    v_rbx = 0;
    a3 = (v_stack_mF8) << (12);
    result = (v_stack_m128) + (a3);
    v_stack_m128 = result;
    if (result < v_r12) goto loc_003D2CEE;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_m108));
    result = MiInsertLargeUserMapping(v_stack_mD8, v_stack_m120, v_stack_p60, (unsigned int)((unsigned int)(v_stack_m110)));
    v_rbx = (v_rbx) + 1;
    result = (0) * (v_stack_mF8);
    a1 = (unsigned int)(((unsigned int)(v_stack_p70)) * ((unsigned int)(v_rbx)));
    result = (result) << (12);
    if (v_stack_m118 == 0) goto loc_003D29D4;
    goto loc_003D29DC;
loc_003D2C0C:
    if ((unsigned int)(a1) == 0) goto loc_003D2B5D;
    goto loc_003D2B85;
loc_003D2C19:
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xA00000ULL))));
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m120 + result * 4 + 81680)));
    goto loc_003D27F9;
loc_003D2C3B:
    a2 = (unsigned int)((v_stack_mF8) + ((unsigned int)(v_r14)));
    if (a2 <= ((unsigned int)(v_stack_p60))) goto loc_003D292A;
    goto loc_003D2941;
loc_003D2C4C:
    result = MiDemotePfnListChain(v_stack_mA8, (unsigned int)((unsigned int)(v_stack_m110)), v_stack_p60, (unsigned int)(0xA00000ULL));
    goto loc_003D294C;
loc_003D2C65:
    if ((unsigned int)((unsigned int)(v_stack_p54)) == 0) goto loc_003D2B00;
    result = MiFlushGraphicsPtes(v_stack_m118, (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))), v_stack_p60, (unsigned int)(v_stack_p54));
    goto loc_003D2B00;
loc_003D2C84:
    result = MiUnlockPageTable(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_rbx, v_stack_p60, (unsigned int)(v_stack_p54));
    goto loc_003D2B0D;
loc_003D2C99:
    if ((unsigned int)(v_stack_m110) == 0) goto loc_003D2B2D;
loc_003D2CA1:
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_003D2B37;
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned __int8)((unsigned __int8)(result)), v_stack_p60, (unsigned int)(v_stack_p54));
loc_003D2CCA:
    v_stack_p50 = 1;
    result = MiLockWorkingSetForLargeMapping(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)(v_rbx - 1)), (unsigned int)(v_stack_p54));
    goto loc_003D2B3F;
loc_003D2CE5:
    goto loc_003D2C0C;
loc_003D2CEE:
    a4 = (v_r12) - (result);
    result = 0;
loc_003D2D0B:
    a2 = (unsigned int)(((unsigned int)(v_stack_p50)) & (1));
    result = MiWorkingSetIsContended(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, a2, (unsigned int)((unsigned int)(v_rbx - 1)), a4);
    if ((unsigned int)(result) == 0) goto loc_003D2A01;
loc_003D2D22:
    v_stack_p58 = 1;
    goto loc_003D2A0E;
loc_003D2D2F:
    goto loc_003D28E7;
loc_003D2D3F:
    if ((unsigned int)(a4) == 0) goto loc_003D2A3D;
    result = MiFlushGraphicsPtes(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned int)((unsigned int)(a4)), (unsigned int)((unsigned int)(v_rbx - 1)), a4);
    goto loc_003D2A3D;
loc_003D2D55:
    result = MiUnlockPageTable(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, v_stack_m110, (unsigned int)((unsigned int)(v_rbx - 1)), a4);
    goto loc_003D2A46;
loc_003D2D65:
    result = MiUnlockWorkingSetExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)(v_rbx - 1)), a4);
    goto loc_003D2A50;
loc_003D2D80:
    result = MiLogPerfMemoryRangeEvent(v_r14, (unsigned int)(*(unsigned int *)(v_stack_mD0 + 464)), 27, v_stack_mC8);
    goto loc_003D2A5E;
}
```

## 5. (Beta) C Style

```c
int64_t MiMapUserLargePages(void *Arg1, int32_t Arg2, uint8_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint8_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m48;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0xA38029)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mD8 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, Arg2 + 96, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (0x4200000ULL));
    v_stack_m130 = (uint32_t)(result);
    v_stack_mB8 = v_xmm0;
    v_stack_mD0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_003D29CC;
    result = MiComputePreferredNode(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg1, Arg2 + 96, Arg4);
loc_003D2781:
    local_r12 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    Arg2 = (*(uint8_t *)(arg1 + 0x20)) << (32);
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    local_r12 = (local_r12) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    Arg2 = (Arg2) << (12);
    local_r12 = (local_r12) << (12);
    local_r12 = (local_r12) | (0xFFFULL);
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x30))))) >> (19);
    local_r12 = (local_r12) + (1);
    v_stack_mF0 = Arg2;
    result = (uint32_t)((result) & (3));
    Arg3 = (local_r12) - (Arg2);
    Arg3 = (Arg3) >> (12);
    v_stack_mC8 = Arg3;
    if ((*(uint32_t *)(v_rip - 0x3D278C + result * 8 + 0x14578)) != 16) goto loc_003D2C19;
    v_stack_m100 = (uint32_t)(1 + 1);
loc_003D27F9:
    v_stack_m14C = (uint32_t)((uint32_t)((uint32_t)(1 + 1)));
loc_003D280E:
    *(uint64_t *)(v_stack_mA8 + 0x8) = v_stack_mA8;
    *(uint64_t *)(v_stack_mA8) = v_stack_mA8;
    result = (v_stack_mA8) + (24);
    Arg1 = (4) - (1);
    if (condition_is_not_equal) goto loc_003D280E;
    v_stack_mC0 = Arg1;
    v_stack_m168 = v_stack_mA8;
    v_stack_m178 = Arg4;
    v_stack_m180 = Arg3;
    v_stack_m188 = (uint32_t)((uint32_t)(Arg2));
    result = MiCreateLargePfnList(v_stack_mC0, Arg2, Arg3, *(uint64_t *)(v_rip - 0x3D278C + (uint32_t)((uint32_t)(1 + 0x1)) * 8 + 0x11C60));
    if (sign_flag) goto loc_003D2A60;
    local_rsi = 0;
    Arg1 = 0;
    Arg4 = 0;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x30))) >> (7);
    result = (uint32_t)((result) & (31));
    local_r11 = (v_stack_mF0) >> (9);
    v_stack_m110 = 0;
    local_rbx = 0;
    v_stack_m118 = 0;
    v_stack_m154 = 0;
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3D285E + result * 4 + 0x11070)));
    v_stack_m140 = v_stack_m148;
    v_stack_m148 = v_stack_m148;
    local_r11 = (local_r11) & (v_stack_m148);
    v_stack_m128 = v_stack_mF0;
    local_r11 = (local_r11) + (v_stack_m148);
    v_stack_m120 = local_r11;
    if (v_stack_mF0 >= local_r12) goto loc_003D2A2F;
loc_003D28E7:
loc_003D28F5:
    if (((uint32_t)((uint32_t)(v_stack_m100))) > ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_003D294C;
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(v_rip - 0x3D285E + (uint32_t)((uint32_t)((uint32_t)(v_stack_m100))) * 8 + 0x11C60)) << (12);
    if (0 != 0) goto loc_003D29BD;
    result = (local_r12) - (v_stack_mF0);
    if (result < Arg1) goto loc_003D29BD;
loc_003D292A:
    if ((*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))) * 2 * 8)) == (v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))) * 2 * 8)) goto loc_003D2C3B;
loc_003D2941:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))) > ((uint32_t)((uint32_t)(v_stack_m14C)))) goto loc_003D2C4C;
loc_003D294C:
    v_stack_mE0 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2;
    v_stack_mE8 = v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8) + 0x8)) != (v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8)) goto loc_003D29B6;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8)) + 0x8)) != (*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8))) goto loc_003D29B6;
    *(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8) = *(uint64_t *)(*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8)) + 0x8) = v_stack_mA8 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 2 * 8;
    v_stack_mF8 = *(uint64_t *)(v_rip - 0x3D2982 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) * 8 + 0x11C60);
    Arg2 = 16;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))))))) != 2) { Arg2 = 1; }
    v_stack_m138 = Arg2;
    if ((*(uint64_t *)(v_stack_m140)) == v_stack_m148) goto loc_003D2A88;
loc_003D29B6:
loc_003D29BD:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m100)))))) + (1));
    goto loc_003D28F5;
loc_003D29CC:
    goto loc_003D2781;
loc_003D29D4:
    v_stack_m118 = 1;
    v_stack_m154 = 3;
loc_003D29DC:
    result = (0) * (v_rip - 4008391);
    result = (uint32_t)(((uint32_t)(v_stack_m134)) + (0));
    v_stack_m120 = v_stack_m120 + result * 8;
    v_stack_m134 = (uint32_t)(result);
    if ((((uint8_t)(result)) & (15)) == 0) goto loc_003D2D0B;
loc_003D2A01:
    result = KeShouldYieldProcessor(v_stack_m120 + result * 8, v_rip - 4008391, v_stack_m148, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003D2D22;
loc_003D2A0E:
    if (v_stack_m128 < local_r12) goto loc_003D2D2F;
loc_003D2A2F:
    if (v_stack_m130 == 0x4200000ULL) goto loc_003D2D3F;
loc_003D2A3D:
    if (v_stack_m110 != 0) goto loc_003D2D55;
loc_003D2A46:
    if (17 != 17) goto loc_003D2D65;
loc_003D2A50:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF40AE)))) & (1)) != 0) goto loc_003D2D80;
loc_003D2A5E:
    result = 0;
loc_003D2A60:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4008391, v_stack_m148, (uint32_t)(v_stack_m154));
    local_rsp = (local_rsp) + (368);
    return result;
loc_003D2A88:
    *(uint64_t *)(arg1 + 0x8) = result;
    *(uint64_t *)(arg1) = v_stack_p60;
    *(void **)(result) = Arg1;
    v_stack_p68 = Arg1;
    if (((uint32_t)(v_stack_m110)) >= 2) goto loc_003D2ADB;
    Arg1 = (uint32_t)((2) - ((uint32_t)(v_stack_m110)));
loc_003D2ABF:
    local_r14 = (local_r11) >> (9);
    local_r14 = (local_r14) & (v_stack_m128);
    local_r14 = (local_r14) + ((uint32_t)(v_stack_m154));
    Arg1 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_003D2ABF;
loc_003D2ADB:
    if (v_stack_p58 != 0) goto loc_003D2AF2;
    local_rbx = (v_stack_p18) ^ (local_r14);
    if (((local_rbx) & (0xFFFFFFFFFFFFF000ULL)) == 0) goto loc_003D2BA2;
loc_003D2AF2:
    if (v_stack_p78 == 0x4200000ULL) goto loc_003D2C65;
loc_003D2B00:
    if (v_stack_m110 != 0) goto loc_003D2C84;
loc_003D2B0D:
    if (v_stack_p58 != 0) goto loc_003D2CA1;
    if (((uint32_t)((uint32_t)(v_stack_p50))) == 1) goto loc_003D2C99;
    if ((uint32_t)(v_stack_m110) == 0) goto loc_003D2CA1;
loc_003D2B2D:
    if (17 != 17) goto loc_003D2C0C;
loc_003D2B37:
    if ((uint32_t)(v_stack_m110) == 0) goto loc_003D2CCA;
loc_003D2B3F:
    if (17 != 17) goto loc_003D2CE5;
    result = MiLockWorkingSetShared(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_rip - 4008391, v_stack_p60, (uint32_t)(v_stack_p54));
loc_003D2B5D:
    local_rbx = (local_r14) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + (result);
    v_stack_m110 = local_rbx;
loc_003D2B85:
    result = MiMakeSystemAddressValid(local_r14, local_rbx - 1 + 1, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p50))));
loc_003D2BA2:
    local_rbx = 0;
    Arg3 = (v_stack_mF8) << (12);
    result = (v_stack_m128) + (Arg3);
    v_stack_m128 = result;
    if (result < local_r12) goto loc_003D2CEE;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_m108));
    result = MiInsertLargeUserMapping(v_stack_mD8, v_stack_m120, v_stack_p60, (uint32_t)((uint32_t)(v_stack_m110)));
    local_rbx = (local_rbx) + 1;
    result = (0) * (v_stack_mF8);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p70)) * ((uint32_t)(local_rbx)));
    result = (result) << (12);
    if (v_stack_m118 == 0) goto loc_003D29D4;
    goto loc_003D29DC;
loc_003D2C0C:
    if ((uint32_t)(Arg1) == 0) goto loc_003D2B5D;
    goto loc_003D2B85;
loc_003D2C19:
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xA00000ULL))));
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m120 + result * 4 + 0x13F10)));
    goto loc_003D27F9;
loc_003D2C3B:
    Arg2 = (uint32_t)((v_stack_mF8) + ((uint32_t)(local_r14)));
    if (Arg2 <= ((uint32_t)(v_stack_p60))) goto loc_003D292A;
    goto loc_003D2941;
loc_003D2C4C:
    result = MiDemotePfnListChain(v_stack_mA8, (uint32_t)((uint32_t)(v_stack_m110)), v_stack_p60, (uint32_t)(0xA00000ULL));
    goto loc_003D294C;
loc_003D2C65:
    if ((uint32_t)((uint32_t)(v_stack_p54)) == 0) goto loc_003D2B00;
    result = MiFlushGraphicsPtes(v_stack_m118, (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))), v_stack_p60, (uint32_t)(v_stack_p54));
    goto loc_003D2B00;
loc_003D2C84:
    result = MiUnlockPageTable(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, local_rbx, v_stack_p60, (uint32_t)(v_stack_p54));
    goto loc_003D2B0D;
loc_003D2C99:
    if ((uint32_t)(v_stack_m110) == 0) goto loc_003D2B2D;
loc_003D2CA1:
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_003D2B37;
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint8_t)((uint8_t)(result)), v_stack_p60, (uint32_t)(v_stack_p54));
loc_003D2CCA:
    v_stack_p50 = 1;
    result = MiLockWorkingSetForLargeMapping(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)(local_rbx - 1)), (uint32_t)(v_stack_p54));
    goto loc_003D2B3F;
loc_003D2CE5:
    goto loc_003D2C0C;
loc_003D2CEE:
    Arg4 = (local_r12) - (result);
    result = 0;
loc_003D2D0B:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p50)) & (1));
    result = MiWorkingSetIsContended(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, Arg2, (uint32_t)((uint32_t)(local_rbx - 1)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_003D2A01;
loc_003D2D22:
    v_stack_p58 = 1;
    goto loc_003D2A0E;
loc_003D2D2F:
    goto loc_003D28E7;
loc_003D2D3F:
    if ((uint32_t)(Arg4) == 0) goto loc_003D2A3D;
    result = MiFlushGraphicsPtes(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint32_t)((uint32_t)(Arg4)), (uint32_t)((uint32_t)(local_rbx - 1)), Arg4);
    goto loc_003D2A3D;
loc_003D2D55:
    result = MiUnlockPageTable(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, v_stack_m110, (uint32_t)((uint32_t)(local_rbx - 1)), Arg4);
    goto loc_003D2A46;
loc_003D2D65:
    result = MiUnlockWorkingSetExclusive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)(local_rbx - 1)), Arg4);
    goto loc_003D2A50;
loc_003D2D80:
    result = MiLogPerfMemoryRangeEvent(local_r14, (uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x1D0)), 27, v_stack_mC8);
    goto loc_003D2A5E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D26F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
