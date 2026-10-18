# KiAbEntryRemoveFromTree

- RVA: `0x00262410`–`0x00262BEB` (길이 `2,011` bytes)
- VA: `0x0000000140262410`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006456C`
- 디코드: `520`개 명령, `2,011/2,011` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **27**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x002624C7` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](../27/ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x002625A2` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00262638` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x00262655` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x0026266E` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x002626AC` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00262749` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00262775` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00262792` → [RtlRbRemoveNode](../2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x002628DE` → [KxWaitForLockChainValid](../21/KxWaitForLockChainValid_function_00217AA0.md) (function, `0x00217AA0`)
- `0x002628FF` → [KeWakeAddressAll](../21/KeWakeAddressAll_function_00217C20.md) (function, `0x00217C20`)
- `0x00262924` → [ExpWaitForSpinLockExclusiveAndAcquire](../32/ExpWaitForSpinLockExclusiveAndAcquire_function_003239A0.md) (function, `0x003239A0`)
- `0x00262987` → [KiReleaseQueuedSpinLockInstrumented](../21/KiReleaseQueuedSpinLockInstrumented_function_002179F0.md) (function, `0x002179F0`)
- `0x00262A06` → [KiAcquireQueuedSpinLockInstrumented](../27/KiAcquireQueuedSpinLockInstrumented_function_00275850.md) (function, `0x00275850`)
- `0x00262A17` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00262A2E` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x00262A4B` → [ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented](../32/ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_00323A70.md) (function, `0x00323A70`)
- `0x00262AA6` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00262AC1` → [KxWaitForLockOwnerShip](../25/KxWaitForLockOwnerShip_function_00257EB0.md) (function, `0x00257EB0`)
- `0x00262B0F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00262B1E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00262B2F` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x00262B38` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x00262B66` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00262B88` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00262BA8` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)
- `0x00262BDF` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [KeAbPreWait](../20/KeAbPreWait_function_0020E560.md) at `0x0020E58F`
- [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) at `0x0020EF97`
- [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) at `0x0020FF3E`
- [ExpAcquireFastResourceSharedSlow](../21/ExpAcquireFastResourceSharedSlow_function_00211260.md) at `0x0021186A`
- [KiAbEntryFreeAndEnableInterrupts](KiAbEntryFreeAndEnableInterrupts_function_002622D0.md) at `0x00262393`
- [ExpAcquireFastResourceExclusiveSlow](../3B/ExpAcquireFastResourceExclusiveSlow_function_003BE2E0.md) at `0x003BE6D3`
- [KiAbCrossThreadRelease](../41/KiAbCrossThreadRelease_function_004167C8.md) at `0x004167E3`

### Static image references
- `0x0026246A` → RVA `0x00E17100` (`.data`; read)
- `0x00262491` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002624AF` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002624B8` → RVA `0x00F0DE58` (`.data`; read)
- `0x0026294E` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00262B01` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00262410  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00262415  55                              push rbp
00262416  56                              push rsi
00262417  57                              push rdi
00262418  41 54                           push r12
0026241A  41 55                           push r13
0026241C  41 56                           push r14
0026241E  41 57                           push r15
00262420  48 8B EC                        mov rbp, rsp
00262423  48 83 EC 50                     sub rsp, 0x50
00262427  48 8B 19                        mov rbx, qword ptr [rcx]
0026242A  33 C0                           xor eax, eax
0026242C  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00262430  4C 8B F1                        mov r14, rcx
00262433  0F B6 49 08                     movzx ecx, byte ptr [rcx + 8]
00262437  0F 57 C0                        xorps xmm0, xmm0
0026243A  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0026243E  0F 57 C9                        xorps xmm1, xmm1
00262441  48 B8 FC FF FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffffffc
0026244B  48 23 D8                        and rbx, rax
0026244E  48 8B C3                        mov rax, rbx
00262451  48 C1 E8 04                     shr rax, 4
00262455  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00262459  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
0026245D  84 C9                           test cl, cl
0026245F  0F 88 6D 02 00 00               js 0x1402626d2
00262465  25 FF 03 00 00                  and eax, 0x3ff
0026246A  48 8D 0D 8F 4C BB 00            lea rcx, [rip + 0xbb4c8f]
00262471  48 C1 E0 06                     shl rax, 6
00262475  48 8D 71 10                     lea rsi, [rcx + 0x10]
00262479  48 03 F0                        add rsi, rax
0026247C  4C 8D 2C 08                     lea r13, [rax + rcx]
00262480  48 89 75 48                     mov qword ptr [rbp + 0x48], rsi
00262484  45 0F 20 C4                     mov r12, cr8
00262488  B8 02 00 00 00                  mov eax, 2
0026248D  44 0F 22 C0                     mov cr8, rax
00262491  83 3D 88 48 D6 00 00            cmp dword ptr [rip + 0xd64888], 0
00262498  0F 85 72 05 00 00               jne 0x140262a10
0026249E  45 0F B6 7E 0B                  movzx r15d, byte ptr [r14 + 0xb]
002624A3  33 C9                           xor ecx, ecx
002624A5  41 83 E7 01                     and r15d, 1
002624A9  0F 85 5A 04 00 00               jne 0x140262909
002624AF  F6 05 50 46 D6 00 21            test byte ptr [rip + 0xd64650], 0x21
002624B6  74 16                           je 0x1402624ce
002624B8  8B 05 9A B9 CA 00               mov eax, dword ptr [rip + 0xcab99a]
002624BE  85 C0                           test eax, eax
002624C0  75 0C                           jne 0x1402624ce
002624C2  B2 FF                           mov dl, 0xff
002624C4  48 8B CE                        mov rcx, rsi
002624C7  E8 54 A8 01 00                  call 0x14027cd20
002624CC  EB 16                           jmp 0x1402624e4
002624CE  0F 0D 0E                        prefetchw byte ptr [rsi]
002624D1  8B 06                           mov eax, dword ptr [rsi]
002624D3  0F BA F0 1F                     btr eax, 0x1f
002624D7  8D 48 01                        lea ecx, [rax + 1]
002624DA  F0 0F B1 0E                     lock cmpxchg dword ptr [rsi], ecx
002624DE  0F 85 3D 05 00 00               jne 0x140262a21
002624E4  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
002624E8  49 8B 7D 00                     mov rdi, qword ptr [r13]
002624EC  F6 C1 01                        test cl, 1
002624EF  0F 85 DF 05 00 00               jne 0x140262ad4
002624F5  83 E1 01                        and ecx, 1
002624F8  48 85 FF                        test rdi, rdi
002624FB  74 3D                           je 0x14026253a
002624FD  48 BA FC FF FF FF FF FF FF 7F   movabs rdx, 0x7ffffffffffffffc
00262507  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00262510  48 8B 47 F0                     mov rax, qword ptr [rdi - 0x10]
00262514  48 23 C2                        and rax, rdx
00262517  48 3B C3                        cmp rax, rbx
0026251A  0F 82 B4 04 00 00               jb 0x1402629d4
00262520  76 18                           jbe 0x14026253a
00262522  48 8B 07                        mov rax, qword ptr [rdi]
00262525  85 C9                           test ecx, ecx
00262527  74 09                           je 0x140262532
00262529  48 85 C0                        test rax, rax
0026252C  0F 85 B7 04 00 00               jne 0x1402629e9
00262532  48 8B F8                        mov rdi, rax
00262535  48 85 FF                        test rdi, rdi
00262538  75 D6                           jne 0x140262510
0026253A  48 8D 77 F0                     lea rsi, [rdi - 0x10]
0026253E  48 C7 45 D0 00 00 00 00         mov qword ptr [rbp - 0x30], 0
00262546  48 8D 4E 48                     lea rcx, [rsi + 0x48]
0026254A  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0026254E  90                              nop
0026254F  F6 05 B0 45 D6 00 21            test byte ptr [rip + 0xd645b0], 0x21
00262556  0F 85 04 02 00 00               jne 0x140262760
0026255C  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00262560  48 87 11                        xchg qword ptr [rcx], rdx
00262563  48 85 D2                        test rdx, rdx
00262566  0F 85 36 05 00 00               jne 0x140262aa2
0026256C  49 3B F6                        cmp rsi, r14
0026256F  0F 85 90 01 00 00               jne 0x140262705
00262575  45 85 FF                        test r15d, r15d
00262578  0F 84 AA 05 00 00               je 0x140262b28
0026257E  48 83 7E 38 00                  cmp qword ptr [rsi + 0x38], 0
00262583  48 8D 4E 38                     lea rcx, [rsi + 0x38]
00262587  0F 85 F2 01 00 00               jne 0x14026277f
0026258D  48 83 7E 28 00                  cmp qword ptr [rsi + 0x28], 0
00262592  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00262596  0F 85 E3 01 00 00               jne 0x14026277f
0026259C  48 8B D7                        mov rdx, rdi
0026259F  49 8B CD                        mov rcx, r13
002625A2  E8 69 26 08 00                  call 0x1402e4c10
002625A7  F6 05 58 45 D6 00 01            test byte ptr [rip + 0xd64558], 1
002625AE  0F 85 DE 05 00 00               jne 0x140262b92
002625B4  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
002625B8  33 DB                           xor ebx, ebx
002625BA  89 18                           mov dword ptr [rax], ebx
002625BC  F6 46 0B 02                     test byte ptr [rsi + 0xb], 2
002625C0  74 0C                           je 0x1402625ce
002625C2  FE 4E 54                        dec byte ptr [rsi + 0x54]
002625C5  0F B6 46 0B                     movzx eax, byte ptr [rsi + 0xb]
002625C9  24 FD                           and al, 0xfd
002625CB  88 46 0B                        mov byte ptr [rsi + 0xb], al
002625CE  F6 46 0B 04                     test byte ptr [rsi + 0xb], 4
002625D2  74 22                           je 0x1402625f6
002625D4  8B 4E 54                        mov ecx, dword ptr [rsi + 0x54]
002625D7  8B C1                           mov eax, ecx
002625D9  C1 E8 08                        shr eax, 8
002625DC  FF C8                           dec eax
002625DE  C1 E0 08                        shl eax, 8
002625E1  33 C1                           xor eax, ecx
002625E3  25 00 7F 00 00                  and eax, 0x7f00
002625E8  33 C1                           xor eax, ecx
002625EA  89 46 54                        mov dword ptr [rsi + 0x54], eax
002625ED  0F B6 46 0B                     movzx eax, byte ptr [rsi + 0xb]
002625F1  24 FB                           and al, 0xfb
002625F3  88 46 0B                        mov byte ptr [rsi + 0xb], al
002625F6  0F B6 46 07                     movzx eax, byte ptr [rsi + 7]
002625FA  24 7F                           and al, 0x7f
002625FC  88 46 07                        mov byte ptr [rsi + 7], al
002625FF  0F B6 46 0B                     movzx eax, byte ptr [rsi + 0xb]
00262603  24 FE                           and al, 0xfe
00262605  88 46 0B                        mov byte ptr [rsi + 0xb], al
00262608  F6 05 F7 44 D6 00 01            test byte ptr [rip + 0xd644f7], 1
0026260F  75 4B                           jne 0x14026265c
00262611  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00262615  48 85 C0                        test rax, rax
00262618  0F 0D 4D D0                     prefetchw byte ptr [rbp - 0x30]
0026261C  75 1F                           jne 0x14026263d
0026261E  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00262622  48 8D 45 D0                     lea rax, [rbp - 0x30]
00262626  F0 48 0F B1 19                  lock cmpxchg qword ptr [rcx], rbx
0026262B  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0026262F  48 3B C1                        cmp rax, rcx
00262632  74 3F                           je 0x140262673
00262634  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00262638  E8 63 54 FB FF                  call 0x140217aa0
0026263D  48 8D 48 08                     lea rcx, [rax + 8]
00262641  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
00262645  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00262649  48 8B C2                        mov rax, rdx
0026264C  48 87 01                        xchg qword ptr [rcx], rax
0026264F  32 C2                           xor al, dl
00262651  A8 04                           test al, 4
00262653  74 1E                           je 0x140262673
00262655  E8 C6 55 FB FF                  call 0x140217c20
0026265A  EB 17                           jmp 0x140262673
0026265C  8B 05 F6 B7 CA 00               mov eax, dword ptr [rip + 0xcab7f6]
00262662  85 C0                           test eax, eax
00262664  75 AB                           jne 0x140262611
00262666  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
0026266A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0026266E  E8 7D 53 FB FF                  call 0x1402179f0
00262673  41 0F B6 46 08                  movzx eax, byte ptr [r14 + 8]
00262678  83 E0 3F                        and eax, 0x3f
0026267B  48 6B C8 58                     imul rcx, rax, 0x58
0026267F  49 8B C6                        mov rax, r14
00262682  48 2B C1                        sub rax, rcx
00262685  48 8B 50 F0                     mov rdx, qword ptr [rax - 0x10]
00262689  41 0F B6 46 09                  movzx eax, byte ptr [r14 + 9]
0026268E  F6 D8                           neg al
00262690  48 1B C9                        sbb rcx, rcx
00262693  F0 FE 8C 11 19 03 00 00         lock dec byte ptr [rcx + rdx + 0x319]
0026269B  83 3D 7E 46 D6 00 00            cmp dword ptr [rip + 0xd6467e], 0
002626A2  74 0D                           je 0x1402626b1
002626A4  44 0F 20 C1                     mov rcx, cr8
002626A8  41 0F B6 D4                     movzx edx, r12b
002626AC  E8 E7 2F 29 00                  call 0x1404f5698
002626B1  41 0F B6 C4                     movzx eax, r12b
002626B5  44 0F 22 C0                     mov cr8, rax
002626B9  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
002626C1  48 83 C4 50                     add rsp, 0x50
002626C5  41 5F                           pop r15
002626C7  41 5E                           pop r14
002626C9  41 5D                           pop r13
002626CB  41 5C                           pop r12
002626CD  5F                              pop rdi
002626CE  5E                              pop rsi
002626CF  5D                              pop rbp
002626D0  C3                              ret
002626D1  CC                              int3
002626D2  83 E1 3F                        and ecx, 0x3f
002626D5  49 8B D6                        mov rdx, r14
002626D8  48 6B C9 58                     imul rcx, rcx, 0x58
002626DC  48 2B D1                        sub rdx, rcx
002626DF  48 8B 4A F0                     mov rcx, qword ptr [rdx - 0x10]
002626E3  33 D2                           xor edx, edx
002626E5  4C 8B 81 20 02 00 00            mov r8, qword ptr [rcx + 0x220]
002626EC  41 F7 70 60                     div dword ptr [r8 + 0x60]
002626F0  49 8B 40 58                     mov rax, qword ptr [r8 + 0x58]
002626F4  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
002626F8  4C 8D 2C C8                     lea r13, [rax + rcx*8]
002626FC  49 8D 75 10                     lea rsi, [r13 + 0x10]
00262700  E9 7B FD FF FF                  jmp 0x140262480
00262705  45 85 FF                        test r15d, r15d
00262708  0F 85 83 02 00 00               jne 0x140262991
0026270E  F6 05 F1 43 D6 00 01            test byte ptr [rip + 0xd643f1], 1
00262715  0F 85 AE 04 00 00               jne 0x140262bc9
0026271B  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0026271F  F0 81 20 FF FF FF BF            lock and dword ptr [rax], 0xbfffffff
00262726  F0 FF 08                        lock dec dword ptr [rax]
00262729  33 DB                           xor ebx, ebx
0026272B  41 0F B6 46 07                  movzx eax, byte ptr [r14 + 7]
00262730  24 7F                           and al, 0x7f
00262732  41 88 46 07                     mov byte ptr [r14 + 7], al
00262736  41 80 7E 09 00                  cmp byte ptr [r14 + 9], 0
0026273B  0F 85 14 03 00 00               jne 0x140262a55
00262741  48 8D 4E 28                     lea rcx, [rsi + 0x28]
00262745  49 8D 56 10                     lea rdx, [r14 + 0x10]
00262749  E8 C2 24 08 00                  call 0x1402e4c10
0026274E  F6 05 B1 43 D6 00 01            test byte ptr [rip + 0xd643b1], 1
00262755  0F 84 B6 FE FF FF               je 0x140262611
0026275B  E9 FC FE FF FF                  jmp 0x14026265c
00262760  8B 05 F2 B6 CA 00               mov eax, dword ptr [rip + 0xcab6f2]
00262766  85 C0                           test eax, eax
00262768  0F 85 EE FD FF FF               jne 0x14026255c
0026276E  48 8B D1                        mov rdx, rcx
00262771  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00262775  E8 D6 30 01 00                  call 0x140275850
0026277A  E9 ED FD FF FF                  jmp 0x14026256c
0026277F  48 85 C9                        test rcx, rcx
00262782  0F 84 14 FE FF FF               je 0x14026259c
00262788  48 8B 19                        mov rbx, qword ptr [rcx]
0026278B  48 8B D3                        mov rdx, rbx
0026278E  48 8D 7B F0                     lea rdi, [rbx - 0x10]
00262792  E8 79 24 08 00                  call 0x1402e4c10
00262797  0F 10 46 10                     movups xmm0, xmmword ptr [rsi + 0x10]
0026279B  48 8D 56 10                     lea rdx, [rsi + 0x10]
0026279F  0F 11 03                        movups xmmword ptr [rbx], xmm0
002627A2  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
002627A7  F2 0F 11 4B 10                  movsd qword ptr [rbx + 0x10], xmm1
002627AC  48 8B 0B                        mov rcx, qword ptr [rbx]
002627AF  48 85 C9                        test rcx, rcx
002627B2  0F 84 F3 01 00 00               je 0x1402629ab
002627B8  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
002627BB  83 E0 03                        and eax, 3
002627BE  48 0B C3                        or rax, rbx
002627C1  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
002627C5  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
002627C9  48 85 C9                        test rcx, rcx
002627CC  74 0D                           je 0x1402627db
002627CE  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
002627D1  83 E0 03                        and eax, 3
002627D4  48 0B C3                        or rax, rbx
002627D7  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
002627DB  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
002627DF  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002627E3  0F 85 C7 02 00 00               jne 0x140262ab0
002627E9  41 F6 45 08 01                  test byte ptr [r13 + 8], 1
002627EE  0F 85 54 03 00 00               jne 0x140262b48
002627F4  49 89 5D 00                     mov qword ptr [r13], rbx
002627F8  33 DB                           xor ebx, ebx
002627FA  48 8D 4F 48                     lea rcx, [rdi + 0x48]
002627FE  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
00262802  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00262806  90                              nop
00262807  F6 05 F8 42 D6 00 21            test byte ptr [rip + 0xd642f8], 0x21
0026280E  0F 85 DD 01 00 00               jne 0x1402629f1
00262814  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00262818  48 87 11                        xchg qword ptr [rcx], rdx
0026281B  48 85 D2                        test rdx, rdx
0026281E  0F 85 99 02 00 00               jne 0x140262abd
00262824  F6 05 DB 42 D6 00 01            test byte ptr [rip + 0xd642db], 1
0026282B  0F 85 41 03 00 00               jne 0x140262b72
00262831  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00262835  89 18                           mov dword ptr [rax], ebx
00262837  0F 10 46 28                     movups xmm0, xmmword ptr [rsi + 0x28]
0026283B  0F 11 47 28                     movups xmmword ptr [rdi + 0x28], xmm0
0026283F  0F 10 46 38                     movups xmm0, xmmword ptr [rsi + 0x38]
00262843  0F 11 47 38                     movups xmmword ptr [rdi + 0x38], xmm0
00262847  0F B6 46 54                     movzx eax, byte ptr [rsi + 0x54]
0026284B  88 47 54                        mov byte ptr [rdi + 0x54], al
0026284E  8B 47 54                        mov eax, dword ptr [rdi + 0x54]
00262851  8B C8                           mov ecx, eax
00262853  33 4E 54                        xor ecx, dword ptr [rsi + 0x54]
00262856  81 E1 00 7F 00 00               and ecx, 0x7f00
0026285C  33 C8                           xor ecx, eax
0026285E  89 4F 54                        mov dword ptr [rdi + 0x54], ecx
00262861  F6 46 0B 02                     test byte ptr [rsi + 0xb], 2
00262865  74 0E                           je 0x140262875
00262867  FE C9                           dec cl
00262869  88 4F 54                        mov byte ptr [rdi + 0x54], cl
0026286C  0F B6 46 0B                     movzx eax, byte ptr [rsi + 0xb]
00262870  24 FD                           and al, 0xfd
00262872  88 46 0B                        mov byte ptr [rsi + 0xb], al
00262875  F6 46 0B 04                     test byte ptr [rsi + 0xb], 4
00262879  74 22                           je 0x14026289d
0026287B  8B 4F 54                        mov ecx, dword ptr [rdi + 0x54]
0026287E  8B C1                           mov eax, ecx
00262880  C1 E8 08                        shr eax, 8
00262883  FF C8                           dec eax
00262885  C1 E0 08                        shl eax, 8
00262888  33 C1                           xor eax, ecx
0026288A  25 00 7F 00 00                  and eax, 0x7f00
0026288F  33 C1                           xor eax, ecx
00262891  89 47 54                        mov dword ptr [rdi + 0x54], eax
00262894  0F B6 46 0B                     movzx eax, byte ptr [rsi + 0xb]
00262898  24 FB                           and al, 0xfb
0026289A  88 46 0B                        mov byte ptr [rsi + 0xb], al
0026289D  0F B6 47 0B                     movzx eax, byte ptr [rdi + 0xb]
002628A1  0C 01                           or al, 1
002628A3  88 47 0B                        mov byte ptr [rdi + 0xb], al
002628A6  F6 05 59 42 D6 00 01            test byte ptr [rip + 0xd64259], 1
002628AD  0F 85 BE 00 00 00               jne 0x140262971
002628B3  0F 0D 4D E8                     prefetchw byte ptr [rbp - 0x18]
002628B7  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
002628BB  48 85 C0                        test rax, rax
002628BE  75 23                           jne 0x1402628e3
002628C0  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
002628C4  48 8D 45 E8                     lea rax, [rbp - 0x18]
002628C8  F0 48 0F B1 19                  lock cmpxchg qword ptr [rcx], rbx
002628CD  48 8D 4D E8                     lea rcx, [rbp - 0x18]
002628D1  48 3B C1                        cmp rax, rcx
002628D4  0F 84 1C FD FF FF               je 0x1402625f6
002628DA  48 8D 4D E8                     lea rcx, [rbp - 0x18]
002628DE  E8 BD 51 FB FF                  call 0x140217aa0
002628E3  48 8D 48 08                     lea rcx, [rax + 8]
002628E7  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
002628EB  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
002628EF  48 8B C2                        mov rax, rdx
002628F2  48 87 01                        xchg qword ptr [rcx], rax
002628F5  32 C2                           xor al, dl
002628F7  A8 04                           test al, 4
002628F9  0F 84 F7 FC FF FF               je 0x1402625f6
002628FF  E8 1C 53 FB FF                  call 0x140217c20
00262904  E9 ED FC FF FF                  jmp 0x1402625f6
00262909  F6 05 F6 41 D6 00 21            test byte ptr [rip + 0xd641f6], 0x21
00262910  0F 85 22 01 00 00               jne 0x140262a38
00262916  F0 0F BA 2E 1F                  lock bts dword ptr [rsi], 0x1f
0026291B  8B F9                           mov edi, ecx
0026291D  73 0C                           jae 0x14026292b
0026291F  B2 FF                           mov dl, 0xff
00262921  48 8B CE                        mov rcx, rsi
00262924  E8 77 10 0C 00                  call 0x1403239a0
00262929  8B F8                           mov edi, eax
0026292B  8B 16                           mov edx, dword ptr [rsi]
0026292D  8B CA                           mov ecx, edx
0026292F  0F BA F1 1E                     btr ecx, 0x1e
00262933  81 F9 00 00 00 80               cmp ecx, 0x80000000
00262939  0F 84 A5 FB FF FF               je 0x1402624e4
0026293F  0F BA E2 1E                     bt edx, 0x1e
00262943  72 07                           jb 0x14026294c
00262945  F0 81 0E 00 00 00 40            lock or dword ptr [rsi], 0x40000000
0026294C  FF C7                           inc edi
0026294E  85 3D 58 29 D6 00               test dword ptr [rip + 0xd62958], edi
00262954  0F 84 A7 01 00 00               je 0x140262b01
0026295A  F3 90                           pause
0026295C  8B 16                           mov edx, dword ptr [rsi]
0026295E  8B C2                           mov eax, edx
00262960  0F BA F0 1E                     btr eax, 0x1e
00262964  3D 00 00 00 80                  cmp eax, 0x80000000
00262969  0F 84 75 FB FF FF               je 0x1402624e4
0026296F  EB CE                           jmp 0x14026293f
00262971  8B 05 E1 B4 CA 00               mov eax, dword ptr [rip + 0xcab4e1]
00262977  85 C0                           test eax, eax
00262979  0F 85 34 FF FF FF               jne 0x1402628b3
0026297F  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00262983  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00262987  E8 64 50 FB FF                  call 0x1402179f0
0026298C  E9 65 FC FF FF                  jmp 0x1402625f6
00262991  F6 05 6E 41 D6 00 01            test byte ptr [rip + 0xd6416e], 1
00262998  0F 85 B2 01 00 00               jne 0x140262b50
0026299E  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
002629A2  33 DB                           xor ebx, ebx
002629A4  89 18                           mov dword ptr [rax], ebx
002629A6  E9 80 FD FF FF                  jmp 0x14026272b
002629AB  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
002629AF  A8 01                           test al, 1
002629B1  0F 85 2E 01 00 00               jne 0x140262ae5
002629B7  48 8B C8                        mov rcx, rax
002629BA  48 3B CA                        cmp rcx, rdx
002629BD  0F 85 02 FE FF FF               jne 0x1402627c5
002629C3  A8 01                           test al, 1
002629C5  0F 85 E9 01 00 00               jne 0x140262bb4
002629CB  49 89 5D 08                     mov qword ptr [r13 + 8], rbx
002629CF  E9 F1 FD FF FF                  jmp 0x1402627c5
002629D4  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
002629D8  85 C9                           test ecx, ecx
002629DA  0F 84 52 FB FF FF               je 0x140262532
002629E0  48 85 C0                        test rax, rax
002629E3  0F 84 49 FB FF FF               je 0x140262532
002629E9  48 33 F8                        xor rdi, rax
002629EC  E9 44 FB FF FF                  jmp 0x140262535
002629F1  8B 05 61 B4 CA 00               mov eax, dword ptr [rip + 0xcab461]
002629F7  85 C0                           test eax, eax
002629F9  0F 85 15 FE FF FF               jne 0x140262814
002629FF  48 8B D1                        mov rdx, rcx
00262A02  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00262A06  E8 45 2E 01 00                  call 0x140275850
00262A0B  E9 14 FE FF FF                  jmp 0x140262824
00262A10  0F B6 D0                        movzx edx, al
00262A13  41 0F B6 CC                     movzx ecx, r12b
00262A17  E8 E0 2C 29 00                  call 0x1404f56fc
00262A1C  E9 7D FA FF FF                  jmp 0x14026249e
00262A21  85 C0                           test eax, eax
00262A23  0F 89 AE FA FF FF               jns 0x1402624d7
00262A29  B2 FF                           mov dl, 0xff
00262A2B  48 8B CE                        mov rcx, rsi
00262A2E  E8 4D F9 0F 00                  call 0x140362380
00262A33  E9 AC FA FF FF                  jmp 0x1402624e4
00262A38  8B 05 1A B4 CA 00               mov eax, dword ptr [rip + 0xcab41a]
00262A3E  85 C0                           test eax, eax
00262A40  0F 85 D0 FE FF FF               jne 0x140262916
00262A46  B2 FF                           mov dl, 0xff
00262A48  48 8B CE                        mov rcx, rsi
00262A4B  E8 20 10 0C 00                  call 0x140323a70
00262A50  E9 8F FA FF FF                  jmp 0x1402624e4
00262A55  41 F6 46 0B 02                  test byte ptr [r14 + 0xb], 2
00262A5A  48 8D 4E 38                     lea rcx, [rsi + 0x38]
00262A5E  74 0E                           je 0x140262a6e
00262A60  FE 4E 54                        dec byte ptr [rsi + 0x54]
00262A63  41 0F B6 46 0B                  movzx eax, byte ptr [r14 + 0xb]
00262A68  24 FD                           and al, 0xfd
00262A6A  41 88 46 0B                     mov byte ptr [r14 + 0xb], al
00262A6E  41 F6 46 0B 04                  test byte ptr [r14 + 0xb], 4
00262A73  0F 84 CC FC FF FF               je 0x140262745
00262A79  8B 56 54                        mov edx, dword ptr [rsi + 0x54]
00262A7C  8B C2                           mov eax, edx
00262A7E  C1 E8 08                        shr eax, 8
00262A81  FF C8                           dec eax
00262A83  C1 E0 08                        shl eax, 8
00262A86  33 C2                           xor eax, edx
00262A88  25 00 7F 00 00                  and eax, 0x7f00
00262A8D  33 C2                           xor eax, edx
00262A8F  89 46 54                        mov dword ptr [rsi + 0x54], eax
00262A92  41 0F B6 46 0B                  movzx eax, byte ptr [r14 + 0xb]
00262A97  24 FB                           and al, 0xfb
00262A99  41 88 46 0B                     mov byte ptr [r14 + 0xb], al
00262A9D  E9 A3 FC FF FF                  jmp 0x140262745
00262AA2  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00262AA6  E8 05 54 FF FF                  call 0x140257eb0
00262AAB  E9 BC FA FF FF                  jmp 0x14026256c
00262AB0  48 39 10                        cmp qword ptr [rax], rdx
00262AB3  75 16                           jne 0x140262acb
00262AB5  48 89 18                        mov qword ptr [rax], rbx
00262AB8  E9 3B FD FF FF                  jmp 0x1402627f8
00262ABD  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00262AC1  E8 EA 53 FF FF                  call 0x140257eb0
00262AC6  E9 59 FD FF FF                  jmp 0x140262824
00262ACB  48 89 58 08                     mov qword ptr [rax + 8], rbx
00262ACF  E9 24 FD FF FF                  jmp 0x1402627f8
00262AD4  48 85 FF                        test rdi, rdi
00262AD7  0F 84 5D FA FF FF               je 0x14026253a
00262ADD  49 33 FD                        xor rdi, r13
00262AE0  E9 10 FA FF FF                  jmp 0x1402624f5
00262AE5  48 83 F8 01                     cmp rax, 1
00262AE9  74 0F                           je 0x140262afa
00262AEB  49 8B CD                        mov rcx, r13
00262AEE  48 83 C9 01                     or rcx, 1
00262AF2  48 33 C8                        xor rcx, rax
00262AF5  E9 C0 FE FF FF                  jmp 0x1402629ba
00262AFA  33 C9                           xor ecx, ecx
00262AFC  E9 B9 FE FF FF                  jmp 0x1402629ba
00262B01  8B 05 B1 3F D6 00               mov eax, dword ptr [rip + 0xd63fb1]
00262B07  A8 40                           test al, 0x40
00262B09  0F 84 4B FE FF FF               je 0x14026295a
00262B0F  E8 7C C9 0A 00                  call 0x14030f490
00262B14  84 C0                           test al, al
00262B16  0F 84 3E FE FF FF               je 0x14026295a
00262B1C  8B CF                           mov ecx, edi
00262B1E  E8 3D C9 0A 00                  call 0x14030f460
00262B23  E9 34 FE FF FF                  jmp 0x14026295c
00262B28  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
00262B2C  48 8B CE                        mov rcx, rsi
00262B2F  E8 5C 7A FE FF                  call 0x14024a590
00262B34  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00262B38  E8 73 46 FB FF                  call 0x1402171b0
00262B3D  33 C9                           xor ecx, ecx
00262B3F  44 8D 79 01                     lea r15d, [rcx + 1]
00262B43  E9 C1 FD FF FF                  jmp 0x140262909
00262B48  49 33 DD                        xor rbx, r13
00262B4B  E9 A4 FC FF FF                  jmp 0x1402627f4
00262B50  8B 05 02 B3 CA 00               mov eax, dword ptr [rip + 0xcab302]
00262B56  85 C0                           test eax, eax
00262B58  0F 85 40 FE FF FF               jne 0x14026299e
00262B5E  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00262B62  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00262B66  E8 D9 E3 05 00                  call 0x1402c0f44
00262B6B  33 DB                           xor ebx, ebx
00262B6D  E9 B9 FB FF FF                  jmp 0x14026272b
00262B72  8B 05 E0 B2 CA 00               mov eax, dword ptr [rip + 0xcab2e0]
00262B78  85 C0                           test eax, eax
00262B7A  0F 85 B1 FC FF FF               jne 0x140262831
00262B80  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00262B84  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00262B88  E8 B7 E3 05 00                  call 0x1402c0f44
00262B8D  E9 A5 FC FF FF                  jmp 0x140262837
00262B92  8B 05 C0 B2 CA 00               mov eax, dword ptr [rip + 0xcab2c0]
00262B98  85 C0                           test eax, eax
00262B9A  0F 85 14 FA FF FF               jne 0x1402625b4
00262BA0  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00262BA4  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00262BA8  E8 97 E3 05 00                  call 0x1402c0f44
00262BAD  33 DB                           xor ebx, ebx
00262BAF  E9 08 FA FF FF                  jmp 0x1402625bc
00262BB4  48 8B C3                        mov rax, rbx
00262BB7  49 33 C5                        xor rax, r13
00262BBA  49 89 45 08                     mov qword ptr [r13 + 8], rax
00262BBE  0C 01                           or al, 1
00262BC0  41 88 45 08                     mov byte ptr [r13 + 8], al
00262BC4  E9 FC FB FF FF                  jmp 0x1402627c5
00262BC9  8B 05 89 B2 CA 00               mov eax, dword ptr [rip + 0xcab289]
00262BCF  85 C0                           test eax, eax
00262BD1  0F 85 44 FB FF FF               jne 0x14026271b
00262BD7  48 8B 55 38                     mov rdx, qword ptr [rbp + 0x38]
00262BDB  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00262BDF  E8 64 E3 08 00                  call 0x1402f0f48
00262BE4  33 DB                           xor ebx, ebx
00262BE6  E9 40 FB FF FF                  jmp 0x14026272b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAbEntryRemoveFromTree(__int64 a1)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m58 = 0;
    v_stack_m40 = 0;
    v_rbx = (*(unsigned __int64 *)(a1)) & (0);
    result = (v_rbx) >> (4);
    v_stack_m68 = v_xmm0;
    v_stack_m50 = v_xmm1;
    if (sign_flag) goto loc_002626D2;
    result = (unsigned int)((result) & (0x3FFULL));
    result = (result) << (6);
    v_rsi = (v_rip + 12274831 + 16) + (result);
loc_00262480:
    v_stack_p10 = v_rsi;
    if ((*(unsigned int *)(v_rip + 14043272)) != 0) goto loc_00262A10;
loc_0026249E:
    a1 = 0;
    v_r15 = (unsigned int)((*(unsigned __int8 *)(a1 + 11)) & (1));
    if (condition_is_not_equal) goto loc_00262909;
    if (((*(unsigned __int8 *)(v_rip + 14042704)) & (33)) == 0) goto loc_002624CE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13285786))) != 0) goto loc_002624CE;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rsi, 255, a3, a4);
    goto loc_002624E4;
loc_002624CE:
loc_002624D7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13285786))) != 0) goto loc_00262A21;
loc_002624E4:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1 + 8))) & (1)) != 0) goto loc_00262AD4;
loc_002624F5:
    a1 = (unsigned int)((*(unsigned __int64 *)(result + v_rip + 12274831 * 1 + 8)) & (1));
    if (*(unsigned __int64 *)(result + v_rip + 12274831 * 1) == 0) goto loc_0026253A;
loc_00262510:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1) - 16)) & (255);
    if (result < v_rbx) goto loc_002629D4;
    if (result <= v_rbx) goto loc_0026253A;
    if ((unsigned int)(a1) == 0) goto loc_00262532;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) != 0) goto loc_002629E9;
loc_00262532:
loc_00262535:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) != 0) goto loc_00262510;
loc_0026253A:
    v_stack_m68 = 0;
    v_stack_m60 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 72;
    if (((*(unsigned __int8 *)(v_rip + 14042544)) & (33)) != 0) goto loc_00262760;
loc_0026255C:
    if (v_stack_m68 != 0) goto loc_00262AA2;
loc_0026256C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16) != a1) goto loc_00262705;
    if ((unsigned int)(v_r15) == 0) goto loc_00262B28;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 56)) != 0) goto loc_0026277F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 40)) != 0) goto loc_0026277F;
loc_0026259C:
    result = RtlRbRemoveNode(result + v_rip + 12274831 * 1, *(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)), a3, a4);
    if (((*(unsigned __int8 *)(v_rip + 14042456)) & (1)) != 0) goto loc_00262B92;
loc_002625B4:
    v_rbx = 0;
    *(unsigned int *)(v_stack_p10) = 0;
loc_002625BC:
    result = v_stack_p10;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11)) & (2)) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11);
        result = (unsigned __int8)((result) & (253));
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11) = (unsigned __int8)(result);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11)) & (4)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 84);
        result = (unsigned int)(a1);
        result = (unsigned int)((result) >> (8));
        result = (unsigned int)((result) - 1);
        result = (unsigned int)((result) << (8));
        result = (unsigned int)((result) ^ ((unsigned int)(a1)));
        result = (unsigned int)((result) & (0x7F00ULL));
        result = (unsigned int)((result) ^ ((unsigned int)(a1)));
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 84) = (unsigned int)(result);
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11);
        result = (unsigned __int8)((result) & (251));
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11) = (unsigned __int8)(result);
    }
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 7)) & (127));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 7) = (unsigned __int8)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11)) & (254));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)) - 16 + 11) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rip + 14042359)) & (1)) != 0) goto loc_0026265C;
loc_00262611:
    if (v_stack_m68 != 0) goto loc_0026263D;
    if (v_stack_m68 == v_stack_m68) goto loc_00262673;
    result = KxWaitForLockChainValid(v_stack_m68, *(unsigned __int64 *)(*(unsigned __int64 *)(result + v_rip + 12274831 * 1)), a3, a4);
loc_0026263D:
    v_stack_m68 = 0;
    result = (unsigned __int8)((v_stack_m60) ^ ((unsigned __int8)(v_stack_m60)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_00262673;
    result = KeWakeAddressAll(result + 8, v_stack_m60, a3, a4);
    goto loc_00262673;
loc_0026265C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13285366))) != 0) goto loc_00262611;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m68, v_stack_p0, a3, a4);
loc_00262673:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 8)) & (63));
    a1 = (v_stack_m68) * (result);
    result = (a1) - (a1);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 9)));
    if ((*(unsigned int *)(v_rip + 14042750)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned __int8)(v_cr8);
loc_002626D2:
    a1 = (unsigned int)((a1) & (63));
    a1 = (a1) * (a1);
    a2 = (a1) - (a1);
    a2 = 0;
    goto loc_00262480;
loc_00262705:
    if ((unsigned int)(v_r15) != 0) goto loc_00262991;
    if (((*(unsigned __int8 *)(v_rip + 14042097)) & (1)) != 0) goto loc_00262BC9;
loc_0026271B:
    v_rbx = 0;
loc_0026272B:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 7)) & (127));
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(a1 + 9)) != 0) goto loc_00262A55;
loc_00262745:
    result = RtlRbRemoveNode(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 40, a1 + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    if (((*(unsigned __int8 *)(v_rip + 14042033)) & (1)) == 0) goto loc_00262611;
    goto loc_0026265C;
loc_00262760:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13285106))) != 0) goto loc_0026255C;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m68, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 40, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_0026256C;
loc_0026277F:
    if (v_stack_m68 == 0) goto loc_0026259C;
    result = RtlRbRemoveNode(v_stack_m68, *(unsigned __int64 *)(v_stack_m68), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) + 16) = v_xmm1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68)) == 0) goto loc_002629AB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68)) + 16))) & (3));
    result = (result) | (*(unsigned __int64 *)(v_stack_m68));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68)) + 16) = result;
loc_002627C5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) + 8) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) + 8) + 16);
        result = (unsigned int)((result) & (3));
        result = (result) | (*(unsigned __int64 *)(v_stack_m68));
        *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) + 8) + 16) = result;
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00262AB0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8)) & (1)) != 0) goto loc_00262B48;
loc_002627F4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8) = *(unsigned __int64 *)(v_stack_m68);
loc_002627F8:
    v_rbx = 0;
    v_stack_m48 = *(unsigned __int64 *)(v_stack_m68) - 16 + 72;
    v_stack_m50 = 0;
    if (((*(unsigned __int8 *)(v_rip + 14041848)) & (33)) != 0) goto loc_002629F1;
loc_00262814:
    if (v_stack_m50 != 0) goto loc_00262ABD;
loc_00262824:
    if (((*(unsigned __int8 *)(v_rip + 14041819)) & (1)) != 0) goto loc_00262B72;
loc_00262831:
    *(unsigned int *)(v_stack_p10) = 0;
loc_00262837:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 40) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 56) = v_xmm0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84))))) ^ (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)));
    a1 = (unsigned int)((a1) & (0x7F00ULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84)))));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84) = (unsigned int)(a1);
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11)) & (2)) != 0) {
        a1 = (unsigned __int8)((a1) - 1);
        *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84) = (unsigned __int8)(a1);
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11);
        result = (unsigned __int8)((result) & (253));
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11) = (unsigned __int8)(result);
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11)) & (4)) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84);
        result = (unsigned int)(a1);
        result = (unsigned int)((result) >> (8));
        result = (unsigned int)((result) - 1);
        result = (unsigned int)((result) << (8));
        result = (unsigned int)((result) ^ ((unsigned int)(a1)));
        result = (unsigned int)((result) & (0x7F00ULL));
        result = (unsigned int)((result) ^ ((unsigned int)(a1)));
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 84) = (unsigned int)(result);
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11);
        result = (unsigned __int8)((result) & (251));
        *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 11) = (unsigned __int8)(result);
    }
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 11)) | (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m68) - 16 + 11) = (unsigned __int8)(result);
    if (((*(unsigned __int8 *)(v_rip + 14041689)) & (1)) != 0) goto loc_00262971;
loc_002628B3:
    if (v_stack_m50 != 0) goto loc_002628E3;
    if (v_stack_m50 == v_stack_m50) goto loc_002625F6;
    result = KxWaitForLockChainValid(v_stack_m50, v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
loc_002628E3:
    v_stack_m50 = 0;
    result = (unsigned __int8)((v_stack_m48) ^ ((unsigned __int8)(v_stack_m48)));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_002625F6;
    result = KeWakeAddressAll(result + 8, v_stack_m48, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_002625F6;
loc_00262909:
    if (((*(unsigned __int8 *)(v_rip + 14041590)) & (33)) != 0) goto loc_00262A38;
loc_00262916:
    v_rdi = (unsigned int)((unsigned int)(result + 8));
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16;
        result = ExpWaitForSpinLockExclusiveAndAcquire(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
        v_rdi = (unsigned int)(result);
    }
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16)))))) == 0x80000000ULL) goto loc_002624E4;
loc_0026293F:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16)))))) >= 0x80000000ULL) {
    }
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 14035288)) & ((unsigned int)(v_rdi))) == 0) goto loc_00262B01;
loc_0026295A:
loc_0026295C:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16)))))) == 0x80000000ULL) goto loc_002624E4;
    goto loc_0026293F;
loc_00262971:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284577))) != 0) goto loc_002628B3;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m50, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_002625F6;
loc_00262991:
    if (((*(unsigned __int8 *)(v_rip + 14041454)) & (1)) != 0) goto loc_00262B50;
loc_0026299E:
    v_rbx = 0;
    *(unsigned int *)(v_stack_p10) = 0;
    goto loc_0026272B;
loc_002629AB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8))) & (1)) != 0) goto loc_00262AE5;
loc_002629BA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8)) != v_stack_p0) goto loc_002627C5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8))) & (1)) != 0) goto loc_00262BB4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8) = 0;
    goto loc_002627C5;
loc_002629D4:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8)) == 0) goto loc_00262532;
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_00262532;
loc_002629E9:
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(v_rdi + 8));
    goto loc_00262535;
loc_002629F1:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284449))) != 0) goto loc_00262814;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m50, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_00262824;
loc_00262A10:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)(result), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_0026249E;
loc_00262A21:
    if (!sign_flag) goto loc_002624D7;
    result = ExpWaitForSpinLockSharedAndAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16, 255, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_002624E4;
loc_00262A38:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284378))) != 0) goto loc_00262916;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16, 255, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_002624E4;
loc_00262A55:
    if (((*(unsigned __int8 *)(a1 + 11)) & (2)) != 0) {
        result = *(unsigned __int8 *)(a1 + 11);
        result = (unsigned __int8)((result) & (253));
        *(unsigned __int8 *)(a1 + 11) = (unsigned __int8)(result);
    }
    if (((*(unsigned __int8 *)(a1 + 11)) & (4)) == 0) goto loc_00262745;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84))))) >> (8));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << (8));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)))));
    result = (unsigned int)((result) & (0x7F00ULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)))));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84) = (unsigned int)(result);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 11)) & (251));
    *(unsigned __int8 *)(a1 + 11) = (unsigned __int8)(result);
    goto loc_00262745;
loc_00262AA2:
    result = KxWaitForLockOwnerShip(v_stack_m68, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_0026256C;
loc_00262AB0:
    if ((*(unsigned __int64 *)(result)) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)))) goto loc_00262ACB;
    *(unsigned __int64 *)(result) = 0;
    goto loc_002627F8;
loc_00262ABD:
    result = KxWaitForLockOwnerShip(v_stack_m50, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_00262824;
loc_00262ACB:
    *(unsigned __int64 *)(result + 8) = 0;
    goto loc_002627F8;
loc_00262AD4:
    if (v_rdi == 0) goto loc_0026253A;
    v_rdi = (v_rdi) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8);
    goto loc_002624F5;
loc_00262AE5:
    if (result == 1) goto loc_00262AFA;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8) | (1);
    a1 = (a1) ^ (result);
    goto loc_002629BA;
loc_00262AFA:
    a1 = 0;
    goto loc_002629BA;
loc_00262B01:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14041009)))) & (64)) == 0) goto loc_0026295A;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0026295A;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_0026295C;
loc_00262B28:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_p10, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m68, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 16 + 84)), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    a1 = 0;
    goto loc_00262909;
loc_00262B48:
    v_rbx = (v_rbx) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8);
    goto loc_002627F4;
loc_00262B50:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284098))) != 0) goto loc_0026299E;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    v_rbx = 0;
    goto loc_0026272B;
loc_00262B72:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284064))) != 0) goto loc_00262831;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    goto loc_00262837;
loc_00262B92:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13284032))) != 0) goto loc_002625B4;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    v_rbx = 0;
    goto loc_002625BC;
loc_00262BB4:
    result = (0) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8) = result;
    result = (unsigned __int8)((result) | (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544) + 88) + a2 + a2 * 2 * 8 + 8) = (unsigned __int8)(result);
    goto loc_002627C5;
loc_00262BC9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13283977))) != 0) goto loc_0026271B;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 - 16) + 544), a4);
    v_rbx = 0;
    goto loc_0026272B;
}
```

## 5. (Beta) C Style

```c
int64_t KiAbEntryRemoveFromTree(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m58 = 0;
    v_stack_m40 = 0;
    local_rbx = (*(uint64_t *)(arg1)) & (0);
    result = (local_rbx) >> (4);
    v_stack_m68 = v_xmm0;
    v_stack_m50 = v_xmm1;
    if (sign_flag) goto loc_002626D2;
    result = (uint32_t)((result) & (0x3FFULL));
    result = (result) << (6);
    local_rsi = (v_rip + 12274831 + 16) + (result);
loc_00262480:
    v_stack_p10 = local_rsi;
    if ((*(uint32_t *)(v_rip + 0xD64888)) != 0) goto loc_00262A10;
loc_0026249E:
    Arg1 = 0;
    local_r15 = (uint32_t)((*(uint8_t *)(arg1 + 0xB)) & (1));
    if (condition_is_not_equal) goto loc_00262909;
    if (((*(uint8_t *)(v_rip + 0xD64650)) & (33)) == 0) goto loc_002624CE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB99A))) != 0) goto loc_002624CE;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(local_rsi, 255, a3, a4);
    goto loc_002624E4;
loc_002624CE:
loc_002624D7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB99A))) != 0) goto loc_00262A21;
loc_002624E4:
    if ((((uint8_t)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1 + 0x8))) & (1)) != 0) goto loc_00262AD4;
loc_002624F5:
    Arg1 = (uint32_t)((*(uint64_t *)(result + v_rip + 0xBB4C8F * 1 + 0x8)) & (1));
    if (*(uint64_t *)(result + v_rip + 0xBB4C8F * 1) == 0) goto loc_0026253A;
loc_00262510:
    result = (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1) - 0x10)) & (255);
    if (result < local_rbx) goto loc_002629D4;
    if (result <= local_rbx) goto loc_0026253A;
    if ((uint32_t)(Arg1) == 0) goto loc_00262532;
    if (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) != 0) goto loc_002629E9;
loc_00262532:
loc_00262535:
    if (*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) != 0) goto loc_00262510;
loc_0026253A:
    v_stack_m68 = 0;
    v_stack_m60 = *(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 16 + 72;
    if (((*(uint8_t *)(v_rip + 0xD645B0)) & (33)) != 0) goto loc_00262760;
loc_0026255C:
    if (v_stack_m68 != 0) goto loc_00262AA2;
loc_0026256C:
    if ((*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 16) != Arg1) goto loc_00262705;
    if ((uint32_t)(local_r15) == 0) goto loc_00262B28;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x38)) != 0) goto loc_0026277F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x28)) != 0) goto loc_0026277F;
loc_0026259C:
    result = RtlRbRemoveNode(result + v_rip + 12274831 * 1, *(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)), a3, a4);
    if (((*(uint8_t *)(v_rip + 0xD64558)) & (1)) != 0) goto loc_00262B92;
loc_002625B4:
    local_rbx = 0;
    *(uint32_t *)(v_stack_p10) = 0;
loc_002625BC:
    result = v_stack_p10;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB)) & (2)) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB);
        result = (uint8_t)((result) & (253));
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB) = (uint8_t)(result);
    }
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB)) & (4)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x54);
        result = (uint32_t)(Arg1);
        result = (uint32_t)((result) >> (8));
        result = (uint32_t)((result) - 1);
        result = (uint32_t)((result) << (8));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
        result = (uint32_t)((result) & (0x7F00ULL));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x54) = (uint32_t)(result);
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB);
        result = (uint8_t)((result) & (251));
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB) = (uint8_t)(result);
    }
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x7)) & (127));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0x7) = (uint8_t)(result);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB)) & (254));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)) - 0x10 + 0xB) = (uint8_t)(result);
    if (((*(uint8_t *)(v_rip + 0xD644F7)) & (1)) != 0) goto loc_0026265C;
loc_00262611:
    if (v_stack_m68 != 0) goto loc_0026263D;
    if (v_stack_m68 == v_stack_m68) goto loc_00262673;
    result = KxWaitForLockChainValid(v_stack_m68, *(uint64_t *)(*(uint64_t *)(result + v_rip + 0xBB4C8F * 1)), a3, a4);
loc_0026263D:
    v_stack_m68 = 0;
    result = (uint8_t)((v_stack_m60) ^ ((uint8_t)(v_stack_m60)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_00262673;
    result = KeWakeAddressAll(result + 8, v_stack_m60, a3, a4);
    goto loc_00262673;
loc_0026265C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB7F6))) != 0) goto loc_00262611;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m68, v_stack_p0, a3, a4);
loc_00262673:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x8)) & (63));
    Arg1 = (v_stack_m68) * (result);
    result = (Arg1) - (Arg1);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x9)));
    if ((*(uint32_t *)(v_rip + 0xD6467E)) != 0) {
        Arg1 = 2;
        a2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (80);
    return (uint8_t)(v_cr8);
loc_002626D2:
    Arg1 = (uint32_t)((Arg1) & (63));
    Arg1 = (Arg1) * (Arg1);
    a2 = (Arg1) - (Arg1);
    a2 = 0;
    goto loc_00262480;
loc_00262705:
    if ((uint32_t)(local_r15) != 0) goto loc_00262991;
    if (((*(uint8_t *)(v_rip + 0xD643F1)) & (1)) != 0) goto loc_00262BC9;
loc_0026271B:
    local_rbx = 0;
loc_0026272B:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x7)) & (127));
    *(uint8_t *)(arg1 + 0x7) = (uint8_t)(result);
    if ((*(uint8_t *)(arg1 + 0x9)) != 0) goto loc_00262A55;
loc_00262745:
    result = RtlRbRemoveNode(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 16 + 40, Arg1 + 16, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    if (((*(uint8_t *)(v_rip + 0xD643B1)) & (1)) == 0) goto loc_00262611;
    goto loc_0026265C;
loc_00262760:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB6F2))) != 0) goto loc_0026255C;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m68, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 16 + 40, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_0026256C;
loc_0026277F:
    if (v_stack_m68 == 0) goto loc_0026259C;
    result = RtlRbRemoveNode(v_stack_m68, *(uint64_t *)(v_stack_m68), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    *(uint64_t *)(*(uint64_t *)(v_stack_m68)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m68) + 0x10) = v_xmm1;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m68)) == 0) goto loc_002629AB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68)) + 0x10))) & (3));
    result = (result) | (*(uint64_t *)(v_stack_m68));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68)) + 0x10) = result;
loc_002627C5:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m68) + 0x8) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68) + 0x8) + 0x10);
        result = (uint32_t)((result) & (3));
        result = (result) | (*(uint64_t *)(v_stack_m68));
        *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m68) + 0x8) + 0x10) = result;
    }
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m68) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00262AB0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8)) & (1)) != 0) goto loc_00262B48;
loc_002627F4:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8) = *(uint64_t *)(v_stack_m68);
loc_002627F8:
    local_rbx = 0;
    v_stack_m48 = *(uint64_t *)(v_stack_m68) - 16 + 72;
    v_stack_m50 = 0;
    if (((*(uint8_t *)(v_rip + 0xD642F8)) & (33)) != 0) goto loc_002629F1;
loc_00262814:
    if (v_stack_m50 != 0) goto loc_00262ABD;
loc_00262824:
    if (((*(uint8_t *)(v_rip + 0xD642DB)) & (1)) != 0) goto loc_00262B72;
loc_00262831:
    *(uint32_t *)(v_stack_p10) = 0;
loc_00262837:
    *(uint64_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x28) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x38) = v_xmm0;
    *(uint8_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54))))) ^ (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)));
    Arg1 = (uint32_t)((Arg1) & (0x7F00ULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54)))));
    *(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54) = (uint32_t)(Arg1);
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB)) & (2)) != 0) {
        Arg1 = (uint8_t)((Arg1) - 1);
        *(uint8_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54) = (uint8_t)(Arg1);
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB);
        result = (uint8_t)((result) & (253));
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB) = (uint8_t)(result);
    }
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB)) & (4)) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54);
        result = (uint32_t)(Arg1);
        result = (uint32_t)((result) >> (8));
        result = (uint32_t)((result) - 1);
        result = (uint32_t)((result) << (8));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
        result = (uint32_t)((result) & (0x7F00ULL));
        result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
        *(uint32_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0x54) = (uint32_t)(result);
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB);
        result = (uint8_t)((result) & (251));
        *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0xB) = (uint8_t)(result);
    }
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0xB)) | (1));
    *(uint8_t *)(*(uint64_t *)(v_stack_m68) - 0x10 + 0xB) = (uint8_t)(result);
    if (((*(uint8_t *)(v_rip + 0xD64259)) & (1)) != 0) goto loc_00262971;
loc_002628B3:
    if (v_stack_m50 != 0) goto loc_002628E3;
    if (v_stack_m50 == v_stack_m50) goto loc_002625F6;
    result = KxWaitForLockChainValid(v_stack_m50, v_stack_m50, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
loc_002628E3:
    v_stack_m50 = 0;
    result = (uint8_t)((v_stack_m48) ^ ((uint8_t)(v_stack_m48)));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_002625F6;
    result = KeWakeAddressAll(result + 8, v_stack_m48, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_002625F6;
loc_00262909:
    if (((*(uint8_t *)(v_rip + 0xD641F6)) & (33)) != 0) goto loc_00262A38;
loc_00262916:
    local_rdi = (uint32_t)((uint32_t)(result + 8));
    if (!(condition_is_above_or_equal)) {
        a2 = 255;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 16;
        result = ExpWaitForSpinLockExclusiveAndAcquire(Arg1, a2, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
        local_rdi = (uint32_t)(result);
    }
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10)))))) == 0x80000000ULL) goto loc_002624E4;
loc_0026293F:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10)))))) >= 0x80000000ULL) {
    }
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD62958)) & ((uint32_t)(local_rdi))) == 0) goto loc_00262B01;
loc_0026295A:
loc_0026295C:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10)))))) == 0x80000000ULL) goto loc_002624E4;
    goto loc_0026293F;
loc_00262971:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB4E1))) != 0) goto loc_002628B3;
    result = KiReleaseQueuedSpinLockInstrumented(v_stack_m50, v_stack_p0, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_002625F6;
loc_00262991:
    if (((*(uint8_t *)(v_rip + 0xD6416E)) & (1)) != 0) goto loc_00262B50;
loc_0026299E:
    local_rbx = 0;
    *(uint32_t *)(v_stack_p10) = 0;
    goto loc_0026272B;
loc_002629AB:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8))) & (1)) != 0) goto loc_00262AE5;
loc_002629BA:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8)) != v_stack_p0) goto loc_002627C5;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8))) & (1)) != 0) goto loc_00262BB4;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8) = 0;
    goto loc_002627C5;
loc_002629D4:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8)) == 0) goto loc_00262532;
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_00262532;
loc_002629E9:
    local_rdi = (local_rdi) ^ (*(uint64_t *)(local_rdi + 0x8));
    goto loc_00262535;
loc_002629F1:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB461))) != 0) goto loc_00262814;
    result = KiAcquireQueuedSpinLockInstrumented(v_stack_m50, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_00262824;
loc_00262A10:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)(result), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_0026249E;
loc_00262A21:
    if (!sign_flag) goto loc_002624D7;
    result = ExpWaitForSpinLockSharedAndAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 16, 255, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_002624E4;
loc_00262A38:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB41A))) != 0) goto loc_00262916;
    result = ExpAcquireSpinLockExclusiveAtDpcLevelInstrumented(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 16, 255, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_002624E4;
loc_00262A55:
    if (((*(uint8_t *)(arg1 + 0xB)) & (2)) != 0) {
        result = *(uint8_t *)(arg1 + 0xB);
        result = (uint8_t)((result) & (253));
        *(uint8_t *)(arg1 + 0xB) = (uint8_t)(result);
    }
    if (((*(uint8_t *)(arg1 + 0xB)) & (4)) == 0) goto loc_00262745;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54))))) >> (8));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << (8));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)))));
    result = (uint32_t)((result) & (0x7F00ULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)))));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54) = (uint32_t)(result);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0xB)) & (251));
    *(uint8_t *)(arg1 + 0xB) = (uint8_t)(result);
    goto loc_00262745;
loc_00262AA2:
    result = KxWaitForLockOwnerShip(v_stack_m68, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_0026256C;
loc_00262AB0:
    if ((*(uint64_t *)(result)) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)))) goto loc_00262ACB;
    *(uint64_t *)(result) = 0;
    goto loc_002627F8;
loc_00262ABD:
    result = KxWaitForLockOwnerShip(v_stack_m50, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_00262824;
loc_00262ACB:
    *(uint64_t *)(result + 0x8) = 0;
    goto loc_002627F8;
loc_00262AD4:
    if (local_rdi == 0) goto loc_0026253A;
    local_rdi = (local_rdi) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8);
    goto loc_002624F5;
loc_00262AE5:
    if (result == 1) goto loc_00262AFA;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8) | (1);
    Arg1 = (Arg1) ^ (result);
    goto loc_002629BA;
loc_00262AFA:
    Arg1 = 0;
    goto loc_002629BA;
loc_00262B01:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD63FB1)))) & (64)) == 0) goto loc_0026295A;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    if ((uint8_t)(result) == 0) goto loc_0026295A;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_0026295C;
loc_00262B28:
    result = ExReleaseSpinLockSharedFromDpcLevel(v_stack_p10, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_m68, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x10 + 0x54)), *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    Arg1 = 0;
    goto loc_00262909;
loc_00262B48:
    local_rbx = (local_rbx) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8);
    goto loc_002627F4;
loc_00262B50:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB302))) != 0) goto loc_0026299E;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    local_rbx = 0;
    goto loc_0026272B;
loc_00262B72:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB2E0))) != 0) goto loc_00262831;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    goto loc_00262837;
loc_00262B92:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB2C0))) != 0) goto loc_002625B4;
    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    local_rbx = 0;
    goto loc_002625BC;
loc_00262BB4:
    result = (0) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8) = result;
    result = (uint8_t)((result) | (1));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220) + 0x58) + a2 + a2 * 2 * 8 + 0x8) = (uint8_t)(result);
    goto loc_002627C5;
loc_00262BC9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAB289))) != 0) goto loc_0026271B;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(v_stack_p10, v_stack_p0, *(uint64_t *)(*(uint64_t *)(a2 - 0x10) + 0x220), a4);
    local_rbx = 0;
    goto loc_0026272B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x10` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x7` | `8` | `R` |
| `Arg1` | `+ 0x7` | `8` | `W` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00262410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
