# MiLockStealUserVm

- RVA: `0x002B3EDC`–`0x002B4468` (길이 `1,420` bytes)
- VA: `0x00000001402B3EDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006D7D0`
- 디코드: `305`개 명령, `1,420/1,420` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x002B3F94` → [MiGetTopLevelPfn](MiGetTopLevelPfn_function_002B44E0.md) (function, `0x002B44E0`)
- `0x002B3F9F` → [MiGetPageTablePfnBuddyRaw](MiGetPageTablePfnBuddyRaw_function_002B4470.md) (function, `0x002B4470`)
- `0x002B4002` → [TRY_ACQUIRE_EXLOCK_EXCLUSIVE](TRY_ACQUIRE_EXLOCK_EXCLUSIVE_function_002BD130.md) (function, `0x002BD130`)
- `0x002B4015` → [MiPrepareAttachThread](MiPrepareAttachThread_function_002B4650.md) (function, `0x002B4650`)
- `0x002B4029` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x002B403E` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x002B4074` → [KeForceAttachProcess](../21/KeForceAttachProcess_function_00216650.md) (function, `0x00216650`)
- `0x002B409F` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002B40BD` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x002B40C5` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x002B40EB` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002B40FC` → [MiVadPagesTradable](../40/MiVadPagesTradable_function_00409360.md) (function, `0x00409360`)
- `0x002B413A` → [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x002B41AE` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002B4258` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002B42CB` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x002B42E9` → [ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented](ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented_function_002BE6A0.md) (function, `0x002BE6A0`)
- `0x002B430E` → [MiUnlockStealVm](../28/MiUnlockStealVm_function_0028EF40.md) (function, `0x0028EF40`)
- `0x002B434C` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x002B435C` → [MiSmallVaStillMapsFrame](../47/MiSmallVaStillMapsFrame_function_00471090.md) (function, `0x00471090`)
- `0x002B43E2` → [MiLockLowestValidPageTableEx](../28/MiLockLowestValidPageTableEx_function_00280D10.md) (function, `0x00280D10`)
- `0x002B4415` → [MiRotatedToFrameBuffer](../2C/MiRotatedToFrameBuffer_function_002C5FE4.md) (function, `0x002C5FE4`)
- `0x002B442D` → [MiLockWorkingSetShared](../27/MiLockWorkingSetShared_function_0027CBF0.md) (function, `0x0027CBF0`)
- `0x002B4456` → [MiClusterVadActive](../69/MiClusterVadActive_function_00699724.md) (function, `0x00699724`)

### Direct callers
- [MiStealPage](MiStealPage_function_002B28D0.md) at `0x002B2A44`

### Static image references
- `0x002B3FC2` → RVA `0x00FC6B70` (`ALMOSTRO`; read)
- `0x002B3FEE` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x002B3FFB` → RVA `0x00E374C0` (`.data`; read)
- `0x002B402E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x002B41D5` → RVA `0x00E2DCE0` (`.data`; read)
- `0x002B4209` → RVA `0x00E30088` (`.data`; read)
- `0x002B4275` → RVA `0x00014578` (`.rdata`; read)
- `0x002B42BF` → RVA `0x00EF51B4` (`.data`; read/write)
- `0x002B42D4` → RVA `0x00F0DE58` (`.data`; read)
- `0x002B42FD` → RVA `0x00EF51C0` (`.data`; read/write)
- `0x002B4305` → RVA `0x00EF51C4` (`.data`; read/write)
- `0x002B4313` → RVA `0x00EF517C` (`.data`; read/write)
- `0x002B4325` → RVA `0x00EF5164` (`.data`; read/write)
- `0x002B43A8` → RVA `0x00EF51BC` (`.data`; read/write)
- `0x002B4407` → RVA `0x00EF51B0` (`.data`; read/write)
- `0x002B4437` → RVA `0x00EF51D0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002B4428` → [sub_006DB988 + 0x6](../6D/Unknown_function_006DB988.md) (`tail-transfer`)
  - `0x002B4463` → [sub_006DB988](../6D/Unknown_function_006DB988.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B3EDC  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002B3EE1  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
002B3EE6  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
002B3EEB  55                              push rbp
002B3EEC  56                              push rsi
002B3EED  57                              push rdi
002B3EEE  41 54                           push r12
002B3EF0  41 55                           push r13
002B3EF2  41 56                           push r14
002B3EF4  41 57                           push r15
002B3EF6  48 83 EC 40                     sub rsp, 0x40
002B3EFA  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
002B3F02  49 8B D9                        mov rbx, r9
002B3F05  48 C1 E3 19                     shl rbx, 0x19
002B3F09  48 8B F2                        mov rsi, rdx
002B3F0C  41 0F B6 E8                     movzx ebp, r8b
002B3F10  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
002B3F1A  48 8B C1                        mov rax, rcx
002B3F1D  48 C1 E0 19                     shl rax, 0x19
002B3F21  48 2B D8                        sub rbx, rax
002B3F24  48 C1 FB 10                     sar rbx, 0x10
002B3F28  48 8B C1                        mov rax, rcx
002B3F2B  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
002B3F35  48 3B D8                        cmp rbx, rax
002B3F38  0F 83 38 04 00 00               jae 0x1402b4376
002B3F3E  83 A4 24 88 00 00 00 00         and dword ptr [rsp + 0x88], 0
002B3F46  C6 47 40 00                     mov byte ptr [rdi + 0x40], 0
002B3F4A  C7 84 24 A0 00 00 00 02 00 00 00  mov dword ptr [rsp + 0xa0], 2
002B3F55  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B3F5F  4C 8B 62 28                     mov r12, qword ptr [rdx + 0x28]
002B3F63  4C 8B FE                        mov r15, rsi
002B3F66  4C 2B F8                        sub r15, rax
002B3F69  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B3F73  49 C1 FF 04                     sar r15, 4
002B3F77  4C 0F AF F8                     imul r15, rax
002B3F7B  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002B3F85  4C 23 E0                        and r12, rax
002B3F88  4D 3B E7                        cmp r12, r15
002B3F8B  0F 84 94 03 00 00               je 0x1402b4325
002B3F91  48 8B CE                        mov rcx, rsi
002B3F94  E8 47 05 00 00                  call 0x1402b44e0
002B3F99  48 8B C8                        mov rcx, rax
002B3F9C  4C 8B C0                        mov r8, rax
002B3F9F  E8 CC 04 00 00                  call 0x1402b4470
002B3FA4  4C 8B F0                        mov r14, rax
002B3FA7  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
002B3FB1  4C 8D A8 00 04 00 00            lea r13, [rax + 0x400]
002B3FB8  4C 3B C6                        cmp r8, rsi
002B3FBB  74 05                           je 0x1402b3fc2
002B3FBD  F0 4D 21 48 18                  lock and qword ptr [r8 + 0x18], r9
002B3FC2  4C 3B 35 A7 2B D1 00            cmp r14, qword ptr [rip + 0xd12ba7]
002B3FC9  0F 84 F0 02 00 00               je 0x1402b42bf
002B3FCF  4D 3B E7                        cmp r12, r15
002B3FD2  0F 84 1F 04 00 00               je 0x1402b43f7
002B3FD8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B3FE1  4C 3B B0 B8 00 00 00            cmp r14, qword ptr [rax + 0xb8]
002B3FE8  0F 84 42 03 00 00               je 0x1402b4330
002B3FEE  F6 05 11 2B D1 00 21            test byte ptr [rip + 0xd12b11], 0x21
002B3FF5  0F 85 D9 02 00 00               jne 0x1402b42d4
002B3FFB  48 8D 0D BE 34 B8 00            lea rcx, [rip + 0xb834be]
002B4002  E8 29 91 00 00                  call 0x1402bd130
002B4007  85 C0                           test eax, eax
002B4009  0F 84 99 03 00 00               je 0x1402b43a8
002B400F  49 8B D5                        mov rdx, r13
002B4012  49 8B CE                        mov rcx, r14
002B4015  E8 36 06 00 00                  call 0x1402b4650
002B401A  44 8B E0                        mov r12d, eax
002B401D  F0 4C 21 4E 18                  lock and qword ptr [rsi + 0x18], r9
002B4022  48 8D 0D 97 34 B8 00            lea rcx, [rip + 0xb83497]
002B4029  E8 B2 57 F9 FF                  call 0x1402497e0
002B402E  83 3D EB 2C D1 00 00            cmp dword ptr [rip + 0xd12ceb], 0
002B4035  74 0C                           je 0x1402b4043
002B4037  44 0F 20 C1                     mov rcx, cr8
002B403B  40 8A D5                        mov dl, bpl
002B403E  E8 55 16 24 00                  call 0x1404f5698
002B4043  44 0F 22 C5                     mov cr8, rbp
002B4047  45 85 E4                        test r12d, r12d
002B404A  0F 84 AD 02 00 00               je 0x1402b42fd
002B4050  4C 89 6F 38                     mov qword ptr [rdi + 0x38], r13
002B4054  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B405D  4C 3B B0 B8 00 00 00            cmp r14, qword ptr [rax + 0xb8]
002B4064  74 13                           je 0x1402b4079
002B4066  48 8D 57 48                     lea rdx, [rdi + 0x48]
002B406A  C6 47 40 01                     mov byte ptr [rdi + 0x40], 1
002B406E  45 33 C0                        xor r8d, r8d
002B4071  49 8B CE                        mov rcx, r14
002B4074  E8 D7 25 F6 FF                  call 0x140216650
002B4079  48 83 67 20 00                  and qword ptr [rdi + 0x20], 0
002B407E  49 8B CD                        mov rcx, r13
002B4081  48 83 67 28 00                  and qword ptr [rdi + 0x28], 0
002B4086  44 8B A4 24 88 00 00 00         mov r12d, dword ptr [rsp + 0x88]
002B408E  4C 89 6F 18                     mov qword ptr [rdi + 0x18], r13
002B4092  45 85 E4                        test r12d, r12d
002B4095  0F 84 92 03 00 00               je 0x1402b442d
002B409B  80 4F 25 01                     or byte ptr [rdi + 0x25], 1
002B409F  E8 FC F7 06 00                  call 0x1403238a0
002B40A4  88 47 24                        mov byte ptr [rdi + 0x24], al
002B40A7  41 BE 00 04 00 00               mov r14d, 0x400
002B40AD  8B 47 08                        mov eax, dword ptr [rdi + 8]
002B40B0  A8 08                           test al, 8
002B40B2  0F 85 00 02 00 00               jne 0x1402b42b8
002B40B8  B9 01 00 00 00                  mov ecx, 1
002B40BD  E8 2E 80 FC FF                  call 0x14027c0f0
002B40C2  48 8B CB                        mov rcx, rbx
002B40C5  E8 06 28 06 00                  call 0x1403168d0
002B40CA  48 8B E8                        mov rbp, rax
002B40CD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B40D6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002B40DD  48 8B 89 10 04 00 00            mov rcx, qword ptr [rcx + 0x410]
002B40E4  48 81 C1 EC 03 00 00            add rcx, 0x3ec
002B40EB  E8 A0 64 F9 FF                  call 0x14024a590
002B40F0  48 85 ED                        test rbp, rbp
002B40F3  0F 84 0C 02 00 00               je 0x1402b4305
002B40F9  48 8B CD                        mov rcx, rbp
002B40FC  E8 5F 52 15 00                  call 0x140409360
002B4101  85 C0                           test eax, eax
002B4103  0F 84 89 02 00 00               je 0x1402b4392
002B4109  45 85 E4                        test r12d, r12d
002B410C  0F 85 44 02 00 00               jne 0x1402b4356
002B4112  48 83 A4 24 88 00 00 00 00      and qword ptr [rsp + 0x88], 0
002B411B  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
002B4125  49 8B C4                        mov rax, r12
002B4128  48 3B D8                        cmp rbx, rax
002B412B  0F 83 82 02 00 00               jae 0x1402b43b3
002B4131  45 33 C0                        xor r8d, r8d
002B4134  48 8B D3                        mov rdx, rbx
002B4137  49 8B CD                        mov rcx, r13
002B413A  E8 01 22 FC FF                  call 0x140276340
002B413F  4C 63 C0                        movsxd r8, eax
002B4142  85 C0                           test eax, eax
002B4144  0F 84 7F 02 00 00               je 0x1402b43c9
002B414A  0F 57 C0                        xorps xmm0, xmm0
002B414D  33 D2                           xor edx, edx
002B414F  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
002B4154  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
002B4159  48 C1 EB 09                     shr rbx, 9
002B415D  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002B4167  48 23 D8                        and rbx, rax
002B416A  49 8B C4                        mov rax, r12
002B416D  48 03 D8                        add rbx, rax
002B4170  48 89 5C D4 20                  mov qword ptr [rsp + rdx*8 + 0x20], rbx
002B4175  48 FF C2                        inc rdx
002B4178  48 83 FA 04                     cmp rdx, 4
002B417C  7C DB                           jl 0x1402b4159
002B417E  4A 8B 54 C4 20                  mov rdx, qword ptr [rsp + r8*8 + 0x20]
002B4183  4A 8B 4C C4 18                  mov rcx, qword ptr [rsp + r8*8 + 0x18]
002B4188  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
002B4190  48 85 D2                        test rdx, rdx
002B4193  0F 84 30 02 00 00               je 0x1402b43c9
002B4199  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002B41A1  48 89 57 28                     mov qword ptr [rdi + 0x28], rdx
002B41A5  48 3B CB                        cmp rcx, rbx
002B41A8  0F 85 5D 01 00 00               jne 0x1402b430b
002B41AE  E8 ED E6 FC FF                  call 0x1402828a0
002B41B3  A8 01                           test al, 1
002B41B5  0F 84 50 01 00 00               je 0x1402b430b
002B41BB  48 C1 E8 0C                     shr rax, 0xc
002B41BF  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002B41C9  48 23 C1                        and rax, rcx
002B41CC  49 3B C7                        cmp rax, r15
002B41CF  0F 85 36 01 00 00               jne 0x1402b430b
002B41D5  4C 3B 3D 04 9B B7 00            cmp r15, qword ptr [rip + 0xb79b04]
002B41DC  0F 87 29 01 00 00               ja 0x1402b430b
002B41E2  4B 8D 04 7F                     lea rax, [r15 + r15*2]
002B41E6  48 03 C0                        add rax, rax
002B41E9  48 B9 28 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000028
002B41F3  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
002B41F7  48 C1 E8 36                     shr rax, 0x36
002B41FB  0F BA E0 00                     bt eax, 0
002B41FF  0F 83 06 01 00 00               jae 0x1402b430b
002B4205  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B4209  48 8B 0D 78 BE B7 00            mov rcx, qword ptr [rip + 0xb7be78]
002B4210  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
002B4218  48 C1 E8 2B                     shr rax, 0x2b
002B421C  25 FF 03 00 00                  and eax, 0x3ff
002B4221  48 39 14 C1                     cmp qword ptr [rcx + rax*8], rdx
002B4225  0F 85 E0 00 00 00               jne 0x1402b430b
002B422B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B422F  48 85 C0                        test rax, rax
002B4232  0F 88 D3 00 00 00               js 0x1402b430b
002B4238  48 0F BA 66 28 35               bt qword ptr [rsi + 0x28], 0x35
002B423E  0F 82 C7 00 00 00               jb 0x1402b430b
002B4244  44 8B 07                        mov r8d, dword ptr [rdi]
002B4247  B9 00 00 41 00                  mov ecx, 0x410000
002B424C  41 8B C0                        mov eax, r8d
002B424F  23 C1                           and eax, ecx
002B4251  3B C1                           cmp eax, ecx
002B4253  74 11                           je 0x1402b4266
002B4255  48 8B CE                        mov rcx, rsi
002B4258  E8 73 A0 FD FF                  call 0x14028e2d0
002B425D  83 F8 09                        cmp eax, 9
002B4260  0F 85 A5 00 00 00               jne 0x1402b430b
002B4266  41 0F BA E0 17                  bt r8d, 0x17
002B426B  73 23                           jae 0x1402b4290
002B426D  48 85 ED                        test rbp, rbp
002B4270  74 1E                           je 0x1402b4290
002B4272  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
002B4275  48 8D 15 FC 02 D6 FF            lea rdx, [rip - 0x29fd04]
002B427C  8B C1                           mov eax, ecx
002B427E  48 C1 E8 13                     shr rax, 0x13
002B4282  83 E0 03                        and eax, 3
002B4285  48 83 3C C2 10                  cmp qword ptr [rdx + rax*8], 0x10
002B428A  0F 84 B2 01 00 00               je 0x1402b4442
002B4290  44 85 77 08                     test dword ptr [rdi + 8], r14d
002B4294  0F 85 78 01 00 00               jne 0x1402b4412
002B429A  B8 01 00 00 00                  mov eax, 1
002B429F  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
002B42A7  48 83 C4 40                     add rsp, 0x40
002B42AB  41 5F                           pop r15
002B42AD  41 5E                           pop r14
002B42AF  41 5D                           pop r13
002B42B1  41 5C                           pop r12
002B42B3  5F                              pop rdi
002B42B4  5E                              pop rsi
002B42B5  5D                              pop rbp
002B42B6  C3                              ret
002B42B7  CC                              int3
002B42B8  33 ED                           xor ebp, ebp
002B42BA  E9 4A FE FF FF                  jmp 0x1402b4109
002B42BF  FF 05 EF 0E C4 00               inc dword ptr [rip + 0xc40eef]
002B42C5  40 8A D5                        mov dl, bpl
002B42C8  48 8B CE                        mov rcx, rsi
002B42CB  E8 10 61 06 00                  call 0x14031a3e0
002B42D0  33 C0                           xor eax, eax
002B42D2  EB CB                           jmp 0x1402b429f
002B42D4  8B 05 7E 9B C5 00               mov eax, dword ptr [rip + 0xc59b7e]
002B42DA  85 C0                           test eax, eax
002B42DC  0F 85 19 FD FF FF               jne 0x1402b3ffb
002B42E2  48 8D 0D D7 31 B8 00            lea rcx, [rip + 0xb831d7]
002B42E9  E8 B2 A3 00 00                  call 0x1402be6a0
002B42EE  49 B9 FF FF FF FF FF FF FF 7F   movabs r9, 0x7fffffffffffffff
002B42F8  E9 0A FD FF FF                  jmp 0x1402b4007
002B42FD  FF 05 BD 0E C4 00               inc dword ptr [rip + 0xc40ebd]
002B4303  EB CB                           jmp 0x1402b42d0
002B4305  FF 05 B9 0E C4 00               inc dword ptr [rip + 0xc40eb9]
002B430B  48 8B CF                        mov rcx, rdi
002B430E  E8 2D AC FD FF                  call 0x14028ef40
002B4313  FF 05 63 0E C4 00               inc dword ptr [rip + 0xc40e63]
002B4319  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
002B4320  E9 7A FF FF FF                  jmp 0x1402b429f
002B4325  FF 05 39 0E C4 00               inc dword ptr [rip + 0xc40e39]
002B432B  E9 61 FC FF FF                  jmp 0x1402b3f91
002B4330  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B4339  80 B8 4A 02 00 00 01            cmp byte ptr [rax + 0x24a], 1
002B4340  0F 84 A8 FC FF FF               je 0x1402b3fee
002B4346  40 8A D5                        mov dl, bpl
002B4349  48 8B CE                        mov rcx, rsi
002B434C  E8 8F 60 06 00                  call 0x14031a3e0
002B4351  E9 23 FD FF FF                  jmp 0x1402b4079
002B4356  49 8B D7                        mov rdx, r15
002B4359  48 8B CB                        mov rcx, rbx
002B435C  E8 2F CD 1B 00                  call 0x140471090
002B4361  85 C0                           test eax, eax
002B4363  0F 84 CE 00 00 00               je 0x1402b4437
002B4369  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002B4371  E9 5F FE FF FF                  jmp 0x1402b41d5
002B4376  48 8B C1                        mov rax, rcx
002B4379  48 3B D8                        cmp rbx, rax
002B437C  0F 87 BC FB FF FF               ja 0x1402b3f3e
002B4382  C7 84 24 88 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x88], 1
002B438D  E9 B4 FB FF FF                  jmp 0x1402b3f46
002B4392  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
002B4395  24 70                           and al, 0x70
002B4397  3C 40                           cmp al, 0x40
002B4399  0F 85 83 00 00 00               jne 0x1402b4422
002B439F  44 09 77 08                     or dword ptr [rdi + 8], r14d
002B43A3  E9 61 FD FF FF                  jmp 0x1402b4109
002B43A8  FF 05 0E 0E C4 00               inc dword ptr [rip + 0xc40e0e]
002B43AE  E9 12 FF FF FF                  jmp 0x1402b42c5
002B43B3  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002B43BD  48 8B C0                        mov rax, rax
002B43C0  48 3B D8                        cmp rbx, rax
002B43C3  0F 87 68 FD FF FF               ja 0x1402b4131
002B43C9  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
002B43D1  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
002B43D9  48 8B D3                        mov rdx, rbx
002B43DC  45 33 C9                        xor r9d, r9d
002B43DF  49 8B CD                        mov rcx, r13
002B43E2  E8 29 C9 FC FF                  call 0x140280d10
002B43E7  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
002B43EF  48 8B D0                        mov rdx, rax
002B43F2  E9 AA FD FF FF                  jmp 0x1402b41a1
002B43F7  F7 80 FC 05 00 00 00 10 00 00   test dword ptr [rax + 0x5fc], 0x1000
002B4401  0F 84 D1 FB FF FF               je 0x1402b3fd8
002B4407  FF 05 A3 0D C4 00               inc dword ptr [rip + 0xc40da3]
002B440D  E9 B3 FE FF FF                  jmp 0x1402b42c5
002B4412  48 8B CB                        mov rcx, rbx
002B4415  E8 CA 1B 01 00                  call 0x1402c5fe4
002B441A  85 C0                           test eax, eax
002B441C  0F 84 78 FE FF FF               je 0x1402b429a
002B4422  FF 05 9C 0D C4 00               inc dword ptr [rip + 0xc40d9c]
002B4428  E9 61 75 42 00                  jmp 0x1406db98e
002B442D  E8 BE 87 FC FF                  call 0x14027cbf0
002B4432  E9 6D FC FF FF                  jmp 0x1402b40a4
002B4437  FF 05 93 0D C4 00               inc dword ptr [rip + 0xc40d93]
002B443D  E9 C9 FE FF FF                  jmp 0x1402b430b
002B4442  0F BA E1 15                     bt ecx, 0x15
002B4446  0F 83 44 FE FF FF               jae 0x1402b4290
002B444C  4C 8D 47 78                     lea r8, [rdi + 0x78]
002B4450  48 8B D6                        mov rdx, rsi
002B4453  48 8B CD                        mov rcx, rbp
002B4456  E8 C9 52 3E 00                  call 0x140699724
002B445B  85 C0                           test eax, eax
002B445D  0F 84 2D FE FF FF               je 0x1402b4290
002B4463  E9 20 75 42 00                  jmp 0x1406db988
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockStealUserVm(__int64 a1, __int64 a2, unsigned __int8 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p98;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    v_rbx = (a4) << (25);
    result = (a1) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if (v_rbx >= a1) goto loc_002B4376;
loc_002B3F3E:
loc_002B3F46:
    *(unsigned __int8 *)(a5 + 64) = 0;
    v_stack_p28 = 2;
    v_r15 = (a2) - (a1);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (a1);
    v_r12 = (*(unsigned __int64 *)(a2 + 40)) & (a1);
    if (v_r12 == v_r15) goto loc_002B4325;
loc_002B3F91:
    result = MiGetTopLevelPfn(a2, a2, a3, a4);
    result = MiGetPageTablePfnBuddyRaw(result, a2, result, a4);
    if (result != a2) {
    }
    if (result == (*(unsigned __int64 *)(v_rip + 13708199))) goto loc_002B42BF;
    if (v_r12 == v_r15) goto loc_002B43F7;
loc_002B3FD8:
    if (result == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_002B4330;
loc_002B3FEE:
    if (((*(unsigned __int8 *)(v_rip + 13708049)) & (33)) != 0) goto loc_002B42D4;
loc_002B3FFB:
    result = TRY_ACQUIRE_EXLOCK_EXCLUSIVE(v_rip + 12072126, a2, result, a4);
loc_002B4007:
    if ((unsigned int)(result) == 0) goto loc_002B43A8;
    result = MiPrepareAttachThread(result, result + 1024, result, a4);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12072087, result + 1024, result, a4);
    if ((*(unsigned int *)(v_rip + 13708523)) != 0) {
        a1 = v_cr8;
        a2 = a3;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, result, a4);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_002B42FD;
    *(unsigned __int64 *)(a5 + 56) = result + 1024;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (result != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) {
        a2 = a5 + 72;
        *(unsigned __int8 *)(a5 + 64) = 1;
        a3 = 0;
        a1 = result;
        result = KeForceAttachProcess(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a5 + 24) = result + 1024;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_002B442D;
    result = MiLockWorkingSetExclusive(result + 1024, a2, a3, a4);
loc_002B40A4:
    *(unsigned __int8 *)(a5 + 36) = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 8)))) & (8)) != 0) goto loc_002B42B8;
    result = MiLockVadTree(1, a2, a3, a4);
    result = MiLocateAddress(v_rbx, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, a2, a3, a4);
    if (result == 0) goto loc_002B4305;
    result = MiVadPagesTradable(result, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002B4392;
loc_002B4109:
    if ((unsigned int)((unsigned int)(v_stack_p10)) != 0) goto loc_002B4356;
    if (v_rbx >= ((unsigned int)(v_stack_p10))) goto loc_002B43B3;
loc_002B4131:
    a3 = 0;
    result = MiFastLockLeafPageTable(result + 1024, v_rbx, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002B43C9;
    a2 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
loc_002B4159:
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & (result);
    v_rbx = (v_rbx) + ((unsigned int)(v_stack_p10));
    *(unsigned __int64 *)(v_rsp + a2 * 8 + 32) = v_rbx;
    a2 = (a2) + 1;
    if (a2 < 4) goto loc_002B4159;
    v_stack_p10 = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 24);
    if (*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 32) == 0) goto loc_002B43C9;
loc_002B41A1:
    *(unsigned __int64 *)(a5 + 40) = *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 32);
    if ((*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 24)) != v_stack_p20) goto loc_002B430B;
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 24), *(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 32), (int)((unsigned int)(result)), a4);
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_002B430B;
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 24));
    if (result != v_r15) goto loc_002B430B;
loc_002B41D5:
    if (v_r15 > (*(unsigned __int64 *)(v_rip + 12032772))) goto loc_002B430B;
    result = (v_r15 + v_r15 * 2) + (v_r15 + v_r15 * 2);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + (int)((unsigned int)(result)) * 8 + 24) + result * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002B430B;
    result = (*(unsigned __int64 *)(a2 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12041848) + result * 8)) != v_stack_p8) goto loc_002B430B;
    if (sign_flag) goto loc_002B430B;
    if (condition_is_below) goto loc_002B430B;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5))))) & ((unsigned int)((unsigned int)(0x410000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x410000ULL)))) goto loc_002B4266;
    result = MiGetPfnSlabType(a2, v_stack_p8, (unsigned int)(*(unsigned int *)(a5)), a4);
    if (((unsigned int)(result)) != 9) goto loc_002B430B;
loc_002B4266:
    if (((unsigned int)(result)) >= 9) goto loc_002B4290;
    if (result == 0) goto loc_002B4290;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) >> (19);
    result = (unsigned int)((result) & (3));
    if ((*(unsigned __int64 *)(v_rip - 2751748 + result * 8)) == 16) goto loc_002B4442;
loc_002B4290:
    if (((*(unsigned int *)(a5 + 8)) & ((unsigned int)((unsigned int)(0x400ULL)))) != 0) goto loc_002B4412;
loc_002B429A:
loc_002B429F:
    v_rsp = (v_rsp) + (64);
    return 1;
loc_002B42B8:
    v_rbp = 0;
    goto loc_002B4109;
loc_002B42BF:
loc_002B42C5:
    result = MiUnlockPage(a2, 0, (unsigned int)(*(unsigned int *)(a5)), a4);
loc_002B42D0:
    result = 0;
    goto loc_002B429F;
loc_002B42D4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12950398))) != 0) goto loc_002B3FFB;
    result = ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 12071383, 0, (unsigned int)(*(unsigned int *)(a5)), a4);
    goto loc_002B4007;
loc_002B42FD:
    goto loc_002B42D0;
loc_002B4305:
loc_002B430B:
    result = MiUnlockStealVm(a5, 0, (unsigned int)(*(unsigned int *)(a5)), a4);
    goto loc_002B429F;
loc_002B4325:
    goto loc_002B3F91;
loc_002B4330:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_002B3FEE;
    result = MiUnlockPage(a2, 0, (unsigned int)(*(unsigned int *)(a5)), a4);
    goto loc_002B4079;
loc_002B4356:
    result = MiSmallVaStillMapsFrame(v_stack_p18, v_r15, (unsigned int)(*(unsigned int *)(a5)), a4);
    if ((unsigned int)(result) == 0) goto loc_002B4437;
    goto loc_002B41D5;
loc_002B4376:
    if (v_stack_p98 > v_stack_p18) goto loc_002B3F3E;
    v_stack_p88 = 1;
    goto loc_002B3F46;
loc_002B4392:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rbp + 48))) & (112));
    if (((unsigned __int8)(result)) != 64) goto loc_002B4422;
    goto loc_002B4109;
loc_002B43A8:
    goto loc_002B42C5;
loc_002B43B3:
    if (v_stack_p98 > result) goto loc_002B4131;
loc_002B43C9:
    a4 = 0;
    result = MiLockLowestValidPageTableEx(result + 1024, v_stack_p98, v_stack_p88, a4);
    goto loc_002B41A1;
loc_002B43F7:
    if (((*(unsigned int *)(result + 1532)) & (0x1000ULL)) == 0) goto loc_002B3FD8;
    goto loc_002B42C5;
loc_002B4412:
    result = MiRotatedToFrameBuffer(v_stack_p98, result, v_stack_p88, a4);
    if ((unsigned int)(result) == 0) goto loc_002B429A;
loc_002B4422:
loc_002B442D:
    result = MiLockWorkingSetShared(v_stack_p98, result, v_stack_p88, a4);
    goto loc_002B40A4;
loc_002B4437:
    goto loc_002B430B;
loc_002B4442:
    if (condition_is_above_or_equal) goto loc_002B4290;
    result = MiClusterVadActive(0, a2, a5 + 120, a4);
    if ((unsigned int)(result) == 0) goto loc_002B4290;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockStealUserVm(int64_t Arg1, void *Arg2, uint8_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;
    uint32_t v_stack_p88;
    uint64_t v_stack_p98;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    local_rbx = (Arg4) << (25);
    result = (Arg1) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if (local_rbx >= Arg1) goto loc_002B4376;
loc_002B3F3E:
loc_002B3F46:
    *(uint8_t *)(arg5 + 0x40) = 0;
    v_stack_p28 = 2;
    local_r15 = (Arg2) - (Arg1);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (Arg1);
    local_r12 = (*(uint64_t *)(arg2 + 0x28)) & (Arg1);
    if (local_r12 == local_r15) goto loc_002B4325;
loc_002B3F91:
    result = MiGetTopLevelPfn(Arg2, Arg2, Arg3, Arg4);
    result = MiGetPageTablePfnBuddyRaw(result, Arg2, result, Arg4);
    if (result != Arg2) {
    }
    if (result == (*(uint64_t *)(v_rip + 0xD12BA7))) goto loc_002B42BF;
    if (local_r12 == local_r15) goto loc_002B43F7;
loc_002B3FD8:
    if (result == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_002B4330;
loc_002B3FEE:
    if (((*(uint8_t *)(v_rip + 0xD12B11)) & (33)) != 0) goto loc_002B42D4;
loc_002B3FFB:
    result = TRY_ACQUIRE_EXLOCK_EXCLUSIVE(v_rip + 12072126, Arg2, result, Arg4);
loc_002B4007:
    if ((uint32_t)(result) == 0) goto loc_002B43A8;
    result = MiPrepareAttachThread(result, result + 1024, result, Arg4);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12072087, result + 1024, result, Arg4);
    if ((*(uint32_t *)(v_rip + 0xD12CEB)) != 0) {
        Arg1 = v_cr8;
        Arg2 = Arg3;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, result, Arg4);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_002B42FD;
    *(uint64_t *)(arg5 + 0x38) = result + 1024;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (result != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) {
        Arg2 = Arg5 + 72;
        *(uint8_t *)(arg5 + 0x40) = 1;
        Arg3 = 0;
        Arg1 = result;
        result = KeForceAttachProcess(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(arg5 + 0x18) = result + 1024;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_002B442D;
    result = MiLockWorkingSetExclusive(result + 1024, Arg2, Arg3, Arg4);
loc_002B40A4:
    *(uint8_t *)(arg5 + 0x24) = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x8)))) & (8)) != 0) goto loc_002B42B8;
    result = MiLockVadTree(1, Arg2, Arg3, Arg4);
    result = MiLocateAddress(local_rbx, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (0x3ECULL);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_002B4305;
    result = MiVadPagesTradable(result, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B4392;
loc_002B4109:
    if ((uint32_t)((uint32_t)(v_stack_p10)) != 0) goto loc_002B4356;
    if (local_rbx >= ((uint32_t)(v_stack_p10))) goto loc_002B43B3;
loc_002B4131:
    Arg3 = 0;
    result = MiFastLockLeafPageTable(result + 1024, local_rbx, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B43C9;
    Arg2 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
loc_002B4159:
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & (result);
    local_rbx = (local_rbx) + ((uint32_t)(v_stack_p10));
    *(uint64_t *)(local_rsp + arg2 * 8 + 0x20) = local_rbx;
    Arg2 = (Arg2) + 1;
    if (Arg2 < 4) goto loc_002B4159;
    v_stack_p10 = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x18);
    if (*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x20) == 0) goto loc_002B43C9;
loc_002B41A1:
    *(uint64_t *)(arg5 + 0x28) = *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x20);
    if ((*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x18)) != v_stack_p20) goto loc_002B430B;
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x18), *(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x20), (int32_t)((uint32_t)(result)), Arg4);
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_002B430B;
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x18));
    if (result != local_r15) goto loc_002B430B;
loc_002B41D5:
    if (local_r15 > (*(uint64_t *)(v_rip + 0xB79B04))) goto loc_002B430B;
    result = (local_r15 + local_r15 * 2) + (local_r15 + local_r15 * 2);
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp + (int32_t)((uint32_t)(result)) * 8 + 0x18) + result * 8)) >> (54);
    if (condition_is_above_or_equal) goto loc_002B430B;
    result = (*(uint64_t *)(arg2 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7BE78) + result * 8)) != v_stack_p8) goto loc_002B430B;
    if (sign_flag) goto loc_002B430B;
    if (condition_is_below) goto loc_002B430B;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5))))) & ((uint32_t)((uint32_t)(0x410000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x410000ULL)))) goto loc_002B4266;
    result = MiGetPfnSlabType(Arg2, v_stack_p8, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
    if (((uint32_t)(result)) != 9) goto loc_002B430B;
loc_002B4266:
    if (((uint32_t)(result)) >= 9) goto loc_002B4290;
    if (result == 0) goto loc_002B4290;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) >> (19);
    result = (uint32_t)((result) & (3));
    if ((*(uint64_t *)(v_rip - 0x29FD04 + result * 8)) == 16) goto loc_002B4442;
loc_002B4290:
    if (((*(uint32_t *)(arg5 + 0x8)) & ((uint32_t)((uint32_t)(0x400ULL)))) != 0) goto loc_002B4412;
loc_002B429A:
loc_002B429F:
    local_rsp = (local_rsp) + (64);
    return 1;
loc_002B42B8:
    local_rbp = 0;
    goto loc_002B4109;
loc_002B42BF:
loc_002B42C5:
    result = MiUnlockPage(Arg2, 0, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
loc_002B42D0:
    result = 0;
    goto loc_002B429F;
loc_002B42D4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC59B7E))) != 0) goto loc_002B3FFB;
    result = ExpTryAcquireSpinLockExclusiveAtDpcLevelInstrumented(v_rip + 12071383, 0, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
    goto loc_002B4007;
loc_002B42FD:
    goto loc_002B42D0;
loc_002B4305:
loc_002B430B:
    result = MiUnlockStealVm(Arg5, 0, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
    goto loc_002B429F;
loc_002B4325:
    goto loc_002B3F91;
loc_002B4330:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_002B3FEE;
    result = MiUnlockPage(Arg2, 0, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
    goto loc_002B4079;
loc_002B4356:
    result = MiSmallVaStillMapsFrame(v_stack_p18, local_r15, (uint32_t)(*(uint32_t *)(arg5)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B4437;
    goto loc_002B41D5;
loc_002B4376:
    if (v_stack_p98 > v_stack_p18) goto loc_002B3F3E;
    v_stack_p88 = 1;
    goto loc_002B3F46;
loc_002B4392:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x30))) & (112));
    if (((uint8_t)(result)) != 64) goto loc_002B4422;
    goto loc_002B4109;
loc_002B43A8:
    goto loc_002B42C5;
loc_002B43B3:
    if (v_stack_p98 > result) goto loc_002B4131;
loc_002B43C9:
    Arg4 = 0;
    result = MiLockLowestValidPageTableEx(result + 1024, v_stack_p98, v_stack_p88, Arg4);
    goto loc_002B41A1;
loc_002B43F7:
    if (((*(uint32_t *)(result + 0x5FC)) & (0x1000ULL)) == 0) goto loc_002B3FD8;
    goto loc_002B42C5;
loc_002B4412:
    result = MiRotatedToFrameBuffer(v_stack_p98, result, v_stack_p88, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B429A;
loc_002B4422:
loc_002B442D:
    result = MiLockWorkingSetShared(v_stack_p98, result, v_stack_p88, Arg4);
    goto loc_002B40A4;
loc_002B4437:
    goto loc_002B430B;
loc_002B4442:
    if (condition_is_above_or_equal) goto loc_002B4290;
    result = MiClusterVadActive(0, Arg2, Arg5 + 120, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B4290;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x8` | `32` | `R` |
| `Arg5` | `+ 0x8` | `32` | `R/W` |
| `Arg5` | `+ 0x18` | `64` | `W` |
| `Arg5` | `+ 0x20` | `64` | `R/W` |
| `Arg5` | `+ 0x24` | `8` | `W` |
| `Arg5` | `+ 0x25` | `8` | `R/W` |
| `Arg5` | `+ 0x28` | `64` | `R/W` |
| `Arg5` | `+ 0x28` | `64` | `W` |
| `Arg5` | `+ 0x38` | `64` | `W` |
| `Arg5` | `+ 0x40` | `8` | `W` |
| `Arg5` | `+ 0x48` | `64` | `R` |
| `Arg5` | `+ 0x78` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B3EDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
