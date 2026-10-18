# MiAddWorkingSetEntries

- RVA: `0x0027DC00`–`0x0027E4AD` (길이 `2,221` bytes)
- VA: `0x000000014027DC00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006636C`
- 디코드: `503`개 명령, `2,221/2,221` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x0027DCB8` → [ExpAcquireSpinLockSharedAtDpcLevelInstrumented](ExpAcquireSpinLockSharedAtDpcLevelInstrumented_function_0027CD20.md) (function, `0x0027CD20`)
- `0x0027DD83` → [MiWorkingSetVeryLarge](../40/MiWorkingSetVeryLarge_function_0040A210.md) (function, `0x0040A210`)
- `0x0027DF42` → [MiRemoveActivePageTableLinks](../29/MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x0027DFA3` → [MiRemoveActivePageTableLinks](../29/MiRemoveActivePageTableLinks_function_00291FA8.md) (function, `0x00291FA8`)
- `0x0027DFD9` → [MiInsertActivePageTableLinksTail](../29/MiInsertActivePageTableLinksTail_function_00291D98.md) (function, `0x00291D98`)
- `0x0027E042` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0027E157` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x0027E18C` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x0027E1DD` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)
- `0x0027E278` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0027E29B` → [MiIsDriverPage](../2A/MiIsDriverPage_function_002A5514.md) (function, `0x002A5514`)
- `0x0027E32B` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0027E398` → [MiRebuildPageTableAges](../40/MiRebuildPageTableAges_function_0040D4E0.md) (function, `0x0040D4E0`)
- `0x0027E3FB` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x0027E45A` → [ExpReleaseSpinLockSharedFromDpcLevelInstrumented](../2F/ExpReleaseSpinLockSharedFromDpcLevelInstrumented_function_002F0F48.md) (function, `0x002F0F48`)

### Direct callers
- [MiReleaseFaultState](MiReleaseFaultState_function_0027D290.md) at `0x0027D327`
- [sub_0027D88D](Unknown_function_0027D88D.md) at `0x0027D8E9`
- [sub_0027EB06](Unknown_function_0027EB06.md) at `0x0027EB99`
- [MiCompletePrivateZeroFault](../33/MiCompletePrivateZeroFault_function_00330CC0.md) at `0x0033119E`
- [MiAllocateWsle](../33/MiAllocateWsle_function_003332C0.md) at `0x00333687`
- [MiEmptyDeferredWorkingSetEntries](../34/MiEmptyDeferredWorkingSetEntries_function_00347910.md) at `0x00347970`

### Static image references
- `0x0027DC14` → RVA `0x00E0A740` (`.data`; read)
- `0x0027DC49` → RVA `0x00E388C0` (`.data`; read/write)
- `0x0027DC50` → RVA `0x00E37518` (`.data`; read)
- `0x0027DC8F` → RVA `0x00E38880` (`.data`; read)
- `0x0027DCA3` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x0027DCAC` → RVA `0x00F0DE58` (`.data`; read)
- `0x0027E06B` → RVA `0x00E30088` (`.data`; read)
- `0x0027E0B8` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0027E150` → RVA `0x00E374C0` (`.data`; read)
- `0x0027E253` → RVA `0x00FC6B28` (`ALMOSTRO`; read)
- `0x0027E268` → RVA `0x00FC6B98` (`ALMOSTRO`; read)
- `0x0027E2A9` → RVA `0x00E2D96C` (`.data`; read/write)
- `0x0027E2B5` → RVA `0x00E388C8` (`.data`; read/write)
- `0x0027E2C9` → RVA `0x00E388D0` (`.data`; read/write)
- `0x0027E2D2` → RVA `0x00E388D8` (`.data`; read)
- `0x0027E464` → RVA `0x00FC6CB0` (`ALMOSTRO`; read)
- `0x0027E473` → RVA `0x00FC6D90` (`ALMOSTRO`; read)
- `0x0027E480` → RVA `0x00E2D968` (`.data`; read/write)
- `0x0027E49E` → RVA `0x00E37518` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0027DC00  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0027DC05  55                              push rbp
0027DC06  56                              push rsi
0027DC07  57                              push rdi
0027DC08  41 54                           push r12
0027DC0A  41 55                           push r13
0027DC0C  41 56                           push r14
0027DC0E  41 57                           push r15
0027DC10  48 83 EC 60                     sub rsp, 0x60
0027DC14  48 8B 05 25 CB B8 00            mov rax, qword ptr [rip + 0xb8cb25]
0027DC1B  48 33 C4                        xor rax, rsp
0027DC1E  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0027DC23  41 8B E9                        mov ebp, r9d
0027DC26  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0027DC2B  49 8B D8                        mov rbx, r8
0027DC2E  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0027DC33  4C 8B FA                        mov r15, rdx
0027DC36  48 8B F9                        mov rdi, rcx
0027DC39  F0 01 59 04                     lock add dword ptr [rcx + 4], ebx
0027DC3D  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0027DC43  24 0F                           and al, 0xf
0027DC45  3C 01                           cmp al, 1
0027DC47  75 07                           jne 0x14027dc50
0027DC49  F0 01 1D 70 AC BB 00            lock add dword ptr [rip + 0xbbac70], ebx
0027DC50  8B 05 C2 98 BB 00               mov eax, dword ptr [rip + 0xbb98c2]
0027DC56  85 C0                           test eax, eax
0027DC58  0F 84 2E 08 00 00               je 0x14027e48c
0027DC5E  65 01 1C 25 90 2E 00 00         add dword ptr gs:[0x2e90], ebx
0027DC66  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
0027DC70  49 8B C4                        mov rax, r12
0027DC73  49 B8 FF FF FF FF FF F6 FF FF   movabs r8, 0xfffff6ffffffffff
0027DC7D  4C 3B F8                        cmp r15, rax
0027DC80  0F 83 F6 06 00 00               jae 0x14027e37c
0027DC86  48 8B F3                        mov rsi, rbx
0027DC89  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0027DC8F  4C 8D 35 EA AB BB 00            lea r14, [rip + 0xbbabea]
0027DC96  24 0F                           and al, 0xf
0027DC98  3C 01                           cmp al, 1
0027DC9A  0F 85 89 07 00 00               jne 0x14027e429
0027DCA0  49 8B CE                        mov rcx, r14
0027DCA3  F6 05 5C 8E D4 00 21            test byte ptr [rip + 0xd48e5c], 0x21
0027DCAA  74 1D                           je 0x14027dcc9
0027DCAC  8B 05 A6 01 C9 00               mov eax, dword ptr [rip + 0xc901a6]
0027DCB2  85 C0                           test eax, eax
0027DCB4  75 13                           jne 0x14027dcc9
0027DCB6  B2 FF                           mov dl, 0xff
0027DCB8  E8 63 F0 FF FF                  call 0x14027cd20
0027DCBD  49 B8 FF FF FF FF FF F6 FF FF   movabs r8, 0xfffff6ffffffffff
0027DCC7  EB 16                           jmp 0x14027dcdf
0027DCC9  0F 0D 09                        prefetchw byte ptr [rcx]
0027DCCC  8B 01                           mov eax, dword ptr [rcx]
0027DCCE  0F BA F0 1F                     btr eax, 0x1f
0027DCD2  8D 50 01                        lea edx, [rax + 1]
0027DCD5  F0 0F B1 11                     lock cmpxchg dword ptr [rcx], edx
0027DCD9  0F 85 F4 04 00 00               jne 0x14027e1d3
0027DCDF  F0 48 01 9F 90 00 00 00         lock add qword ptr [rdi + 0x90], rbx
0027DCE7  48 85 F6                        test rsi, rsi
0027DCEA  74 1F                           je 0x14027dd0b
0027DCEC  48 8B CE                        mov rcx, rsi
0027DCEF  F0 48 0F C1 8F 80 00 00 00      lock xadd qword ptr [rdi + 0x80], rcx
0027DCF8  48 8B 87 A0 00 00 00            mov rax, qword ptr [rdi + 0xa0]
0027DCFF  48 03 CE                        add rcx, rsi
0027DD02  48 3B C8                        cmp rcx, rax
0027DD05  0F 87 E5 04 00 00               ja 0x14027e1f0
0027DD0B  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
0027DD11  24 0F                           and al, 0xf
0027DD13  3C 01                           cmp al, 1
0027DD15  0F 84 9A 05 00 00               je 0x14027e2b5
0027DD1B  40 F6 C5 02                     test bpl, 2
0027DD1F  74 1C                           je 0x14027dd3d
0027DD21  F0 48 01 9F 98 00 00 00         lock add qword ptr [rdi + 0x98], rbx
0027DD29  49 8B C4                        mov rax, r12
0027DD2C  4C 3B F8                        cmp r15, rax
0027DD2F  0F 83 C9 05 00 00               jae 0x14027e2fe
0027DD35  F0 48 01 9F 88 00 00 00         lock add qword ptr [rdi + 0x88], rbx
0027DD3D  44 8B 8F B8 00 00 00            mov r9d, dword ptr [rdi + 0xb8]
0027DD44  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
0027DD4E  45 0F B6 C1                     movzx r8d, r9b
0027DD52  41 80 E0 0F                     and r8b, 0xf
0027DD56  41 80 F8 01                     cmp r8b, 1
0027DD5A  0F 83 A9 04 00 00               jae 0x14027e209
0027DD60  40 F6 C5 01                     test bpl, 1
0027DD64  74 38                           je 0x14027dd9e
0027DD66  48 8B B7 80 00 00 00            mov rsi, qword ptr [rdi + 0x80]
0027DD6D  48 3B 77 70                     cmp rsi, qword ptr [rdi + 0x70]
0027DD71  76 2B                           jbe 0x14027dd9e
0027DD73  8B 87 BC 00 00 00               mov eax, dword ptr [rdi + 0xbc]
0027DD79  A8 01                           test al, 1
0027DD7B  75 21                           jne 0x14027dd9e
0027DD7D  48 8B D3                        mov rdx, rbx
0027DD80  48 8B CF                        mov rcx, rdi
0027DD83  E8 88 C4 18 00                  call 0x14040a210
0027DD88  85 C0                           test eax, eax
0027DD8A  0F 85 DF 05 00 00               jne 0x14027e36f
0027DD90  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
0027DD96  A8 40                           test al, 0x40
0027DD98  0F 85 C7 05 00 00               jne 0x14027e365
0027DD9E  40 F6 C5 04                     test bpl, 4
0027DDA2  0F 84 69 02 00 00               je 0x14027e011
0027DDA8  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
0027DDB2  0F 57 C0                        xorps xmm0, xmm0
0027DDB5  49 B9 F8 D7 BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbed7f8
0027DDBF  49 8B F7                        mov rsi, r15
0027DDC2  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
0027DDCC  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0027DDD1  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0027DDD6  48 85 DB                        test rbx, rbx
0027DDD9  74 7E                           je 0x14027de59
0027DDDB  48 BD FF FF FF FF FF F6 FF FF   movabs rbp, 0xfffff6ffffffffff
0027DDE5  49 BE FF FF FF FF FF 00 00 00   movabs r14, 0xffffffffff
0027DDEF  49 8B C4                        mov rax, r12
0027DDF2  48 3B F0                        cmp rsi, rax
0027DDF5  0F 83 14 05 00 00               jae 0x14027e30f
0027DDFB  4C 8B C6                        mov r8, rsi
0027DDFE  49 C1 E8 09                     shr r8, 9
0027DE02  4D 23 C5                        and r8, r13
0027DE05  49 8B C4                        mov rax, r12
0027DE08  4C 03 C0                        add r8, rax
0027DE0B  49 8B 10                        mov rdx, qword ptr [r8]
0027DE0E  49 8B C2                        mov rax, r10
0027DE11  4C 3B C0                        cmp r8, rax
0027DE14  72 21                           jb 0x14027de37
0027DE16  49 8B C1                        mov rax, r9
0027DE19  4C 3B C0                        cmp r8, rax
0027DE1C  77 19                           ja 0x14027de37
0027DE1E  F6 C2 01                        test dl, 1
0027DE21  74 14                           je 0x14027de37
0027DE23  F6 C2 42                        test dl, 0x42
0027DE26  0F 95 C1                        setne cl
0027DE29  F6 C2 20                        test dl, 0x20
0027DE2C  0F 95 C0                        setne al
0027DE2F  84 C8                           test al, cl
0027DE31  0F 84 55 03 00 00               je 0x14027e18c
0027DE37  48 C1 EA 38                     shr rdx, 0x38
0027DE3B  83 E2 0F                        and edx, 0xf
0027DE3E  0F B6 C2                        movzx eax, dl
0027DE41  48 81 C6 00 10 00 00            add rsi, 0x1000
0027DE48  FF 44 84 30                     inc dword ptr [rsp + rax*4 + 0x30]
0027DE4C  48 83 EB 01                     sub rbx, 1
0027DE50  75 9D                           jne 0x14027ddef
0027DE52  4C 8D 35 27 AA BB 00            lea r14, [rip + 0xbbaa27]
0027DE59  40 B6 08                        mov sil, 8
0027DE5C  49 BB FF FF FF FF FF 1F 80 FF   movabs r11, 0xff801fffffffffff
0027DE66  48 BA 00 00 00 40 FB F6 FF FF   movabs rdx, 0xfffff6fb40000000
0027DE70  40 80 C6 FF                     add sil, 0xff
0027DE74  40 0F B6 EE                     movzx ebp, sil
0027DE78  8B 44 AC 30                     mov eax, dword ptr [rsp + rbp*4 + 0x30]
0027DE7C  44 8B E0                        mov r12d, eax
0027DE7F  85 C0                           test eax, eax
0027DE81  0F 84 81 01 00 00               je 0x14027e008
0027DE87  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0027DE8C  44 8B E8                        mov r13d, eax
0027DE8F  4D 8B C1                        mov r8, r9
0027DE92  49 C1 E8 12                     shr r8, 0x12
0027DE96  41 81 E0 F8 FF FF 3F            and r8d, 0x3ffffff8
0027DE9D  48 8B C2                        mov rax, rdx
0027DEA0  4C 03 C0                        add r8, rax
0027DEA3  49 8B 00                        mov rax, qword ptr [r8]
0027DEA6  49 8B CA                        mov rcx, r10
0027DEA9  4C 3B C1                        cmp r8, rcx
0027DEAC  72 28                           jb 0x14027ded6
0027DEAE  48 B9 F8 D7 BE 7D FB F6 FF FF   movabs rcx, 0xfffff6fb7dbed7f8
0027DEB8  48 8B C9                        mov rcx, rcx
0027DEBB  4C 3B C1                        cmp r8, rcx
0027DEBE  77 16                           ja 0x14027ded6
0027DEC0  A8 01                           test al, 1
0027DEC2  74 12                           je 0x14027ded6
0027DEC4  A8 42                           test al, 0x42
0027DEC6  0F 95 C2                        setne dl
0027DEC9  A8 20                           test al, 0x20
0027DECB  0F 95 C1                        setne cl
0027DECE  84 D1                           test cl, dl
0027DED0  0F 84 E2 01 00 00               je 0x14027e0b8
0027DED6  48 C1 E8 0C                     shr rax, 0xc
0027DEDA  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0027DEE4  48 23 C1                        and rax, rcx
0027DEE7  4C 8D 3C 40                     lea r15, [rax + rax*2]
0027DEEB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0027DEF5  49 C1 E7 04                     shl r15, 4
0027DEF9  48 8B C0                        mov rax, rax
0027DEFC  4C 03 F8                        add r15, rax
0027DEFF  49 8B 07                        mov rax, qword ptr [r15]
0027DF02  4D 8B 07                        mov r8, qword ptr [r15]
0027DF05  49 C1 E8 2D                     shr r8, 0x2d
0027DF09  48 C1 E8 37                     shr rax, 0x37
0027DF0D  41 81 E0 FF 03 00 00            and r8d, 0x3ff
0027DF14  24 07                           and al, 7
0027DF16  F6 44 24 20 08                  test byte ptr [rsp + 0x20], 8
0027DF1B  0F 85 D1 00 00 00               jne 0x14027dff2
0027DF21  40 3A F0                        cmp sil, al
0027DF24  74 2A                           je 0x14027df50
0027DF26  0F 86 C6 00 00 00               jbe 0x14027dff2
0027DF2C  49 8B 1F                        mov rbx, qword ptr [r15]
0027DF2F  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
0027DF33  0F BA E0 1A                     bt eax, 0x1a
0027DF37  73 0E                           jae 0x14027df47
0027DF39  45 33 C0                        xor r8d, r8d
0027DF3C  49 8B D7                        mov rdx, r15
0027DF3F  48 8B CF                        mov rcx, rdi
0027DF42  E8 61 40 01 00                  call 0x140291fa8
0027DF47  41 81 E4 FF 03 00 00            and r12d, 0x3ff
0027DF4E  EB 58                           jmp 0x14027dfa8
0027DF50  49 8B 07                        mov rax, qword ptr [r15]
0027DF53  43 8D 0C 04                     lea ecx, [r12 + r8]
0027DF57  8B D1                           mov edx, ecx
0027DF59  44 8B E1                        mov r12d, ecx
0027DF5C  48 C1 E2 2D                     shl rdx, 0x2d
0027DF60  41 81 E4 FF 03 00 00            and r12d, 0x3ff
0027DF67  48 8B CA                        mov rcx, rdx
0027DF6A  48 33 C8                        xor rcx, rax
0027DF6D  4B 8D 04 28                     lea rax, [r8 + r13]
0027DF71  49 23 CB                        and rcx, r11
0027DF74  48 33 CA                        xor rcx, rdx
0027DF77  49 89 0F                        mov qword ptr [r15], rcx
0027DF7A  48 85 C0                        test rax, rax
0027DF7D  0F 84 0C 04 00 00               je 0x14027e38f
0027DF83  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
0027DF87  0F BA E0 1A                     bt eax, 0x1a
0027DF8B  72 65                           jb 0x14027dff2
0027DF8D  49 8B 1F                        mov rbx, qword ptr [r15]
0027DF90  41 8B 47 24                     mov eax, dword ptr [r15 + 0x24]
0027DF94  0F BA E0 1A                     bt eax, 0x1a
0027DF98  73 0E                           jae 0x14027dfa8
0027DF9A  45 33 C0                        xor r8d, r8d
0027DF9D  49 8B D7                        mov rdx, r15
0027DFA0  48 8B CF                        mov rcx, rdi
0027DFA3  E8 00 40 01 00                  call 0x140291fa8
0027DFA8  48 8B C5                        mov rax, rbp
0027DFAB  48 B9 FF FF FF FF FF 1F 00 FC   movabs rcx, 0xfc001fffffffffff
0027DFB5  83 E0 07                        and eax, 7
0027DFB8  48 23 D9                        and rbx, rcx
0027DFBB  48 C1 E0 0A                     shl rax, 0xa
0027DFBF  45 33 C9                        xor r9d, r9d
0027DFC2  49 0B C4                        or rax, r12
0027DFC5  44 0F B6 C6                     movzx r8d, sil
0027DFC9  48 C1 E0 2D                     shl rax, 0x2d
0027DFCD  49 8B D7                        mov rdx, r15
0027DFD0  48 0B C3                        or rax, rbx
0027DFD3  48 8B CF                        mov rcx, rdi
0027DFD6  49 89 07                        mov qword ptr [r15], rax
0027DFD9  E8 BA 3D 01 00                  call 0x140291d98
0027DFDE  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
0027DFE8  49 BB FF FF FF FF FF 1F 80 FF   movabs r11, 0xff801fffffffffff
0027DFF2  F0 4C 01 6C EF 28               lock add qword ptr [rdi + rbp*8 + 0x28], r13
0027DFF8  40 80 FE 07                     cmp sil, 7
0027DFFC  74 62                           je 0x14027e060
0027DFFE  48 BA 00 00 00 40 FB F6 FF FF   movabs rdx, 0xfffff6fb40000000
0027E008  40 84 F6                        test sil, sil
0027E00B  0F 85 5F FE FF FF               jne 0x14027de70
0027E011  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
0027E017  24 0F                           and al, 0xf
0027E019  3C 01                           cmp al, 1
0027E01B  0F 85 14 04 00 00               jne 0x14027e435
0027E021  F6 05 DE 8A D4 00 01            test byte ptr [rip + 0xd48ade], 1
0027E028  0F 85 13 04 00 00               jne 0x14027e441
0027E02E  F0 41 81 26 FF FF FF BF         lock and dword ptr [r14], 0xbfffffff
0027E036  F0 41 FF 0E                     lock dec dword ptr [r14]
0027E03A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0027E03F  48 33 CC                        xor rcx, rsp
0027E042  E8 F9 E5 42 00                  call 0x1406ac640
0027E047  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
0027E04F  48 83 C4 60                     add rsp, 0x60
0027E053  41 5F                           pop r15
0027E055  41 5E                           pop r14
0027E057  41 5D                           pop r13
0027E059  41 5C                           pop r12
0027E05B  5F                              pop rdi
0027E05C  5E                              pop rsi
0027E05D  5D                              pop rbp
0027E05E  C3                              ret
0027E05F  CC                              int3
0027E060  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
0027E064  0F B7 8F AE 00 00 00            movzx ecx, word ptr [rdi + 0xae]
0027E06B  48 8B 05 16 20 BB 00            mov rax, qword ptr [rip + 0xbb2016]
0027E072  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
0027E076  48 8B AB C0 44 00 00            mov rbp, qword ptr [rbx + 0x44c0]
0027E07D  48 3B 55 38                     cmp rdx, qword ptr [rbp + 0x38]
0027E081  48 BA 00 00 00 40 FB F6 FF FF   movabs rdx, 0xfffff6fb40000000
0027E08B  0F 83 90 00 00 00               jae 0x14027e121
0027E091  4D 85 ED                        test r13, r13
0027E094  0F 85 D6 FD FF FF               jne 0x14027de70
0027E09A  4C 39 6F 18                     cmp qword ptr [rdi + 0x18], r13
0027E09E  4C 8D 7F 18                     lea r15, [rdi + 0x18]
0027E0A2  0F 84 C8 FD FF FF               je 0x14027de70
0027E0A8  48 8B 83 D0 44 00 00            mov rax, qword ptr [rbx + 0x44d0]
0027E0AF  45 8D 65 02                     lea r12d, [r13 + 2]
0027E0B3  E9 85 00 00 00                  jmp 0x14027e13d
0027E0B8  48 F7 05 C5 89 D4 00 00 00 60 00  test qword ptr [rip + 0xd489c5], 0x600000
0027E0C3  0F 84 0D FE FF FF               je 0x14027ded6
0027E0C9  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0027E0D2  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0027E0D9  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0027E0E0  0F 84 F0 FD FF FF               je 0x14027ded6
0027E0E6  48 8B 8A 08 05 00 00            mov rcx, qword ptr [rdx + 0x508]
0027E0ED  48 85 C9                        test rcx, rcx
0027E0F0  0F 84 E0 FD FF FF               je 0x14027ded6
0027E0F6  49 C1 E8 03                     shr r8, 3
0027E0FA  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0027E101  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
0027E105  F6 C1 20                        test cl, 0x20
0027E108  74 04                           je 0x14027e10e
0027E10A  48 83 C8 20                     or rax, 0x20
0027E10E  48 8B D0                        mov rdx, rax
0027E111  48 83 C8 42                     or rax, 0x42
0027E115  F6 C1 42                        test cl, 0x42
0027E118  48 0F 44 C2                     cmove rax, rdx
0027E11C  E9 B5 FD FF FF                  jmp 0x14027ded6
0027E121  48 83 7F 18 00                  cmp qword ptr [rdi + 0x18], 0
0027E126  4C 8D 7F 18                     lea r15, [rdi + 0x18]
0027E12A  0F 84 40 FD FF FF               je 0x14027de70
0027E130  48 8B 83 C8 44 00 00            mov rax, qword ptr [rbx + 0x44c8]
0027E137  41 BC 01 00 00 00               mov r12d, 1
0027E13D  48 BA 00 00 00 40 FB F6 FF FF   movabs rdx, 0xfffff6fb40000000
0027E147  49 3B C7                        cmp rax, r15
0027E14A  0F 84 20 FD FF FF               je 0x14027de70
0027E150  48 8D 0D 69 93 BB 00            lea rcx, [rip + 0xbb9369]
0027E157  E8 24 AD FC FF                  call 0x140248e80
0027E15C  80 7D 35 00                     cmp byte ptr [rbp + 0x35], 0
0027E160  0F 85 8A 02 00 00               jne 0x14027e3f0
0027E166  49 8B 07                        mov rax, qword ptr [r15]
0027E169  48 85 C0                        test rax, rax
0027E16C  0F 84 7E 02 00 00               je 0x14027e3f0
0027E172  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0027E176  4C 39 78 08                     cmp qword ptr [rax + 8], r15
0027E17A  75 09                           jne 0x14027e185
0027E17C  4C 39 39                        cmp qword ptr [rcx], r15
0027E17F  0F 84 1D 02 00 00               je 0x14027e3a2
0027E185  B9 03 00 00 00                  mov ecx, 3
0027E18A  CD 29                           int 0x29
0027E18C  E8 07 D8 0A 00                  call 0x14032b998
0027E191  48 85 C0                        test rax, rax
0027E194  0F 84 9D FC FF FF               je 0x14027de37
0027E19A  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
0027E1A1  48 85 C0                        test rax, rax
0027E1A4  0F 84 8D FC FF FF               je 0x14027de37
0027E1AA  49 C1 E8 03                     shr r8, 3
0027E1AE  41 81 E0 FF 01 00 00            and r8d, 0x1ff
0027E1B5  4A 8B 04 C0                     mov rax, qword ptr [rax + r8*8]
0027E1B9  A8 20                           test al, 0x20
0027E1BB  74 04                           je 0x14027e1c1
0027E1BD  48 83 CA 20                     or rdx, 0x20
0027E1C1  48 8B CA                        mov rcx, rdx
0027E1C4  48 83 CA 42                     or rdx, 0x42
0027E1C8  A8 42                           test al, 0x42
0027E1CA  48 0F 44 D1                     cmove rdx, rcx
0027E1CE  E9 64 FC FF FF                  jmp 0x14027de37
0027E1D3  85 C0                           test eax, eax
0027E1D5  0F 89 F7 FA FF FF               jns 0x14027dcd2
0027E1DB  B2 FF                           mov dl, 0xff
0027E1DD  E8 9E 41 0E 00                  call 0x140362380
0027E1E2  E9 D6 FA FF FF                  jmp 0x14027dcbd
0027E1E7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0027E1F0  F0 48 0F B1 8F A0 00 00 00      lock cmpxchg qword ptr [rdi + 0xa0], rcx
0027E1F9  0F 84 0C FB FF FF               je 0x14027dd0b
0027E1FF  48 3B C8                        cmp rcx, rax
0027E202  77 EC                           ja 0x14027e1f0
0027E204  E9 02 FB FF FF                  jmp 0x14027dd0b
0027E209  48 8B 05 78 1E BB 00            mov rax, qword ptr [rip + 0xbb1e78]
0027E210  0F B7 8F AE 00 00 00            movzx ecx, word ptr [rdi + 0xae]
0027E217  48 8B 14 C8                     mov rdx, qword ptr [rax + rcx*8]
0027E21B  41 0F B6 C1                     movzx eax, r9b
0027E21F  83 E0 0F                        and eax, 0xf
0027E222  FF C8                           dec eax
0027E224  48 8B 8A 40 1C 00 00            mov rcx, qword ptr [rdx + 0x1c40]
0027E22B  4C 8B 97 90 00 00 00            mov r10, qword ptr [rdi + 0x90]
0027E232  4C 03 D1                        add r10, rcx
0027E235  48 8D 0C C2                     lea rcx, [rdx + rax*8]
0027E239  48 8B 81 48 1C 00 00            mov rax, qword ptr [rcx + 0x1c48]
0027E240  4C 3B D0                        cmp r10, rax
0027E243  0F 87 C7 01 00 00               ja 0x14027e410
0027E249  41 80 F8 03                     cmp r8b, 3
0027E24D  0F 85 0D FB FF FF               jne 0x14027dd60
0027E253  48 8B 05 CE 88 D4 00            mov rax, qword ptr [rip + 0xd488ce]
0027E25A  48 85 C0                        test rax, rax
0027E25D  74 16                           je 0x14027e275
0027E25F  4C 3B F8                        cmp r15, rax
0027E262  0F 83 FC 01 00 00               jae 0x14027e464
0027E268  4C 3B 3D 29 89 D4 00            cmp r15, qword ptr [rip + 0xd48929]
0027E26F  0F 83 FE 01 00 00               jae 0x14027e473
0027E275  49 8B CF                        mov rcx, r15
0027E278  E8 03 0A 01 00                  call 0x14028ec80
0027E27D  83 F8 0B                        cmp eax, 0xb
0027E280  0F 85 DA FA FF FF               jne 0x14027dd60
0027E286  49 8B CF                        mov rcx, r15
0027E289  48 C1 E9 09                     shr rcx, 9
0027E28D  49 23 CD                        and rcx, r13
0027E290  49 8B C4                        mov rax, r12
0027E293  48 03 C8                        add rcx, rax
0027E296  BA 01 00 00 00                  mov edx, 1
0027E29B  E8 74 72 02 00                  call 0x1402a5514
0027E2A0  48 85 C0                        test rax, rax
0027E2A3  0F 84 B7 FA FF FF               je 0x14027dd60
0027E2A9  F0 01 1D BC F6 BA 00            lock add dword ptr [rip + 0xbaf6bc], ebx
0027E2B0  E9 AB FA FF FF                  jmp 0x14027dd60
0027E2B5  F0 48 01 1D 0B A6 BB 00         lock add qword ptr [rip + 0xbba60b], rbx
0027E2BD  48 85 F6                        test rsi, rsi
0027E2C0  0F 84 55 FA FF FF               je 0x14027dd1b
0027E2C6  48 8B CE                        mov rcx, rsi
0027E2C9  F0 48 0F C1 0D FE A5 BB 00      lock xadd qword ptr [rip + 0xbba5fe], rcx
0027E2D2  48 8B 05 FF A5 BB 00            mov rax, qword ptr [rip + 0xbba5ff]
0027E2D9  48 03 CE                        add rcx, rsi
0027E2DC  48 3B C8                        cmp rcx, rax
0027E2DF  0F 86 36 FA FF FF               jbe 0x14027dd1b
0027E2E5  F0 48 0F B1 0D EA A5 BB 00      lock cmpxchg qword ptr [rip + 0xbba5ea], rcx
0027E2EE  0F 84 27 FA FF FF               je 0x14027dd1b
0027E2F4  48 3B C8                        cmp rcx, rax
0027E2F7  77 EC                           ja 0x14027e2e5
0027E2F9  E9 1D FA FF FF                  jmp 0x14027dd1b
0027E2FE  49 8B C0                        mov rax, r8
0027E301  4C 3B F8                        cmp r15, rax
0027E304  0F 87 2B FA FF FF               ja 0x14027dd35
0027E30A  E9 2E FA FF FF                  jmp 0x14027dd3d
0027E30F  48 8B C5                        mov rax, rbp
0027E312  48 3B F0                        cmp rsi, rax
0027E315  0F 87 E0 FA FF FF               ja 0x14027ddfb
0027E31B  48 8B CE                        mov rcx, rsi
0027E31E  48 C1 E9 09                     shr rcx, 9
0027E322  49 23 CD                        and rcx, r13
0027E325  49 8B C4                        mov rax, r12
0027E328  48 03 C8                        add rcx, rax
0027E32B  E8 70 45 00 00                  call 0x1402828a0
0027E330  48 C1 E8 0C                     shr rax, 0xc
0027E334  49 23 C6                        and rax, r14
0027E337  48 8D 14 40                     lea rdx, [rax + rax*2]
0027E33B  48 03 D2                        add rdx, rdx
0027E33E  49 8B C7                        mov rax, r15
0027E341  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
0027E345  48 C1 EA 2A                     shr rdx, 0x2a
0027E349  83 E2 07                        and edx, 7
0027E34C  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
0027E356  49 B9 F8 D7 BE 7D FB F6 FF FF   movabs r9, 0xfffff6fb7dbed7f8
0027E360  E9 D9 FA FF FF                  jmp 0x14027de3e
0027E365  48 3B 77 78                     cmp rsi, qword ptr [rdi + 0x78]
0027E369  0F 86 2F FA FF FF               jbe 0x14027dd9e
0027E36F  F0 83 8F BC 00 00 00 01         lock or dword ptr [rdi + 0xbc], 1
0027E377  E9 22 FA FF FF                  jmp 0x14027dd9e
0027E37C  49 8B C0                        mov rax, r8
0027E37F  4C 3B F8                        cmp r15, rax
0027E382  0F 87 FE F8 FF FF               ja 0x14027dc86
0027E388  33 F6                           xor esi, esi
0027E38A  E9 FA F8 FF FF                  jmp 0x14027dc89
0027E38F  45 33 C0                        xor r8d, r8d
0027E392  49 8B D1                        mov rdx, r9
0027E395  48 8B CF                        mov rcx, rdi
0027E398  E8 43 F1 18 00                  call 0x14040d4e0
0027E39D  E9 3C FC FF FF                  jmp 0x14027dfde
0027E3A2  48 81 C3 C8 44 00 00            add rbx, 0x44c8
0027E3A9  48 89 01                        mov qword ptr [rcx], rax
0027E3AC  48 89 48 08                     mov qword ptr [rax + 8], rcx
0027E3B0  41 83 FC 01                     cmp r12d, 1
0027E3B4  75 1D                           jne 0x14027e3d3
0027E3B6  48 8B 03                        mov rax, qword ptr [rbx]
0027E3B9  48 39 58 08                     cmp qword ptr [rax + 8], rbx
0027E3BD  0F 85 C2 FD FF FF               jne 0x14027e185
0027E3C3  49 89 07                        mov qword ptr [r15], rax
0027E3C6  49 89 5F 08                     mov qword ptr [r15 + 8], rbx
0027E3CA  4C 89 78 08                     mov qword ptr [rax + 8], r15
0027E3CE  4C 89 3B                        mov qword ptr [rbx], r15
0027E3D1  EB 21                           jmp 0x14027e3f4
0027E3D3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0027E3D7  48 39 18                        cmp qword ptr [rax], rbx
0027E3DA  0F 85 A5 FD FF FF               jne 0x14027e185
0027E3E0  49 89 1F                        mov qword ptr [r15], rbx
0027E3E3  49 89 47 08                     mov qword ptr [r15 + 8], rax
0027E3E7  4C 89 38                        mov qword ptr [rax], r15
0027E3EA  4C 89 7B 08                     mov qword ptr [rbx + 8], r15
0027E3EE  EB 04                           jmp 0x14027e3f4
0027E3F0  C6 45 36 01                     mov byte ptr [rbp + 0x36], 1
0027E3F4  48 8D 0D C5 90 BB 00            lea rcx, [rip + 0xbb90c5]
0027E3FB  E8 E0 B3 FC FF                  call 0x1402497e0
0027E400  49 BA 00 D0 BE 7D FB F6 FF FF   movabs r10, 0xfffff6fb7dbed000
0027E40A  E9 4D FA FF FF                  jmp 0x14027de5c
0027E40F  90                              nop
0027E410  F0 4C 0F B1 91 48 1C 00 00      lock cmpxchg qword ptr [rcx + 0x1c48], r10
0027E419  0F 84 2A FE FF FF               je 0x14027e249
0027E41F  4C 3B D0                        cmp r10, rax
0027E422  77 EC                           ja 0x14027e410
0027E424  E9 20 FE FF FF                  jmp 0x14027e249
0027E429  48 81 C1 00 01 00 00            add rcx, 0x100
0027E430  E9 6E F8 FF FF                  jmp 0x14027dca3
0027E435  4C 8D B7 00 01 00 00            lea r14, [rdi + 0x100]
0027E43C  E9 E0 FB FF FF                  jmp 0x14027e021
0027E441  8B 05 11 FA C8 00               mov eax, dword ptr [rip + 0xc8fa11]
0027E447  85 C0                           test eax, eax
0027E449  0F 85 DF FB FF FF               jne 0x14027e02e
0027E44F  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0027E457  49 8B CE                        mov rcx, r14
0027E45A  E8 E9 2A 07 00                  call 0x1402f0f48
0027E45F  E9 D6 FB FF FF                  jmp 0x14027e03a
0027E464  4C 3B 3D 45 88 D4 00            cmp r15, qword ptr [rip + 0xd48845]
0027E46B  0F 83 F7 FD FF FF               jae 0x14027e268
0027E471  EB 0D                           jmp 0x14027e480
0027E473  4C 3B 3D 16 89 D4 00            cmp r15, qword ptr [rip + 0xd48916]
0027E47A  0F 83 F5 FD FF FF               jae 0x14027e275
0027E480  F0 01 1D E1 F4 BA 00            lock add dword ptr [rip + 0xbaf4e1], ebx
0027E487  E9 D4 F8 FF FF                  jmp 0x14027dd60
0027E48C  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0027E492  24 0F                           and al, 0xf
0027E494  FE C8                           dec al
0027E496  3C 03                           cmp al, 3
0027E498  0F 87 C0 F7 FF FF               ja 0x14027dc5e
0027E49E  C7 05 70 90 BB 00 01 00 00 00   mov dword ptr [rip + 0xbb9070], 1
0027E4A8  E9 B1 F7 FF FF                  jmp 0x14027dc5e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddWorkingSetEntries(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p98;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 12110629)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m78 = a4;
    v_stack_m70 = a2;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) {
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12294338))) == 0) goto loc_0027E48C;
loc_0027DC5E:
    if (a2 >= v_r12) goto loc_0027E37C;
loc_0027DC86:
loc_0027DC89:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0027E429;
loc_0027DCA3:
    if (((*(unsigned __int8 *)(v_rip + 13930076)) & (33)) == 0) goto loc_0027DCC9;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13173158))) != 0) goto loc_0027DCC9;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12299242, 255, a3, a4);
loc_0027DCBD:
    goto loc_0027DCDF;
loc_0027DCC9:
loc_0027DCD2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13173158))) != 0) goto loc_0027E1D3;
loc_0027DCDF:
    if (a3 == 0) goto loc_0027DD0B;
    a1 = (a3) + (a3);
    if (a1 > (*(unsigned __int64 *)(a1 + 160))) goto loc_0027E1F0;
loc_0027DD0B:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_0027E2B5;
loc_0027DD1B:
    if ((((unsigned __int8)((unsigned int)(a4))) & (2)) == 0) goto loc_0027DD3D;
    if (a2 >= v_r12) goto loc_0027E2FE;
loc_0027DD35:
loc_0027DD3D:
    a3 = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15));
    if (((unsigned __int8)(a3)) >= 1) goto loc_0027E209;
loc_0027DD60:
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) == 0) goto loc_0027DD9E;
    if ((*(unsigned __int64 *)(a1 + 128)) <= (*(unsigned __int64 *)(a1 + 112))) goto loc_0027DD9E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 188)))) & (1)) != 0) goto loc_0027DD9E;
    result = MiWorkingSetVeryLarge(a1, a3, a3, (unsigned int)(*(unsigned int *)(a1 + 184)));
    if ((unsigned int)(result) != 0) goto loc_0027E36F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (64)) != 0) goto loc_0027E365;
loc_0027DD9E:
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) goto loc_0027E011;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (a3 == 0) goto loc_0027DE59;
loc_0027DDEF:
    if (a2 >= v_r12) goto loc_0027E30F;
loc_0027DDFB:
    a3 = (a2) >> (9);
    a3 = (a3) & (v_r13);
    a3 = (a3) + (v_r12);
    if (a3 < v_r10) goto loc_0027DE37;
    if (a3 > ((unsigned int)(*(unsigned int *)(a1 + 184)))) goto loc_0027DE37;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_0027DE37;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0027E18C;
loc_0027DE37:
    a2 = (*(unsigned __int64 *)(a3)) >> (56);
    a2 = (unsigned int)((a2) & (15));
loc_0027DE3E:
    v_rsi = (a2) + (0x1000ULL);
    v_rbx = (a3) - (1);
    if (condition_is_not_equal) goto loc_0027DDEF;
loc_0027DE59:
loc_0027DE5C:
loc_0027DE70:
    v_rsi = (unsigned __int8)((8) + (255));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48))) == 0) goto loc_0027E008;
    a3 = (v_stack_m70) >> (18);
    a3 = (unsigned int)((a3) & (0x3FFFFFF8ULL));
    a3 = (a3) + (a2);
    if (a3 < v_r10) goto loc_0027DED6;
    if (a3 > v_r10) goto loc_0027DED6;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (1)) == 0) goto loc_0027DED6;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(a3))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_0027E0B8;
loc_0027DED6:
    result = (*(unsigned __int64 *)(a3)) >> (12);
    result = (result) & (a1);
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + (result);
    a3 = (*(unsigned __int64 *)(v_r15)) >> (45);
    result = (*(unsigned __int64 *)(v_r15)) >> (55);
    a3 = (unsigned int)((a3) & (0x3FFULL));
    result = (unsigned __int8)((result) & (7));
    if (((v_stack_m78) & (8)) != 0) goto loc_0027DFF2;
    if (((unsigned __int8)(v_rsi)) == ((unsigned __int8)(result))) goto loc_0027DF50;
    if (((unsigned __int8)(v_rsi)) <= ((unsigned __int8)(result))) goto loc_0027DFF2;
    result = (unsigned int)(*(unsigned int *)(v_r15 + 36));
    if (((unsigned __int8)(v_rsi)) < ((unsigned __int8)(result))) {
        a3 = 0;
        a2 = v_r15;
        a1 = a1;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, v_stack_m70);
    }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48))))) & (0x3FFULL));
    goto loc_0027DFA8;
loc_0027DF50:
    a2 = ((unsigned int)((unsigned int)(v_r12 + a3 * 1))) << (45);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_r12 + a3 * 1))) & (0x3FFULL));
    a1 = (a2) ^ (*(unsigned __int64 *)(v_r15));
    a1 = (a1) & (v_r11);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(v_r15) = a1;
    if (a3 + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48)))) * 1 == 0) goto loc_0027E38F;
    if (condition_is_below) goto loc_0027DFF2;
    result = (unsigned int)(*(unsigned int *)(v_r15 + 36));
    if (!(condition_is_above_or_equal)) {
        a3 = 0;
        a2 = v_r15;
        a1 = a1;
        result = MiRemoveActivePageTableLinks(a1, a2, a3, v_stack_m70);
    }
    result = (unsigned int)(((unsigned __int8)(v_rsi)) & (7));
    v_rbx = (*(unsigned __int64 *)(v_r15)) & (a1);
    result = (result) << (10);
    a4 = 0;
    result = (result) | (v_r12);
    result = (result) << (45);
    result = (result) | (v_rbx);
    *(unsigned __int64 *)(v_r15) = result;
    result = MiInsertActivePageTableLinksTail(a1, v_r15, (unsigned __int8)(v_rsi), a4);
loc_0027DFDE:
loc_0027DFF2:
    if (((unsigned __int8)(v_rsi)) == 7) goto loc_0027E060;
loc_0027E008:
    if ((unsigned __int8)(v_rsi) != 0) goto loc_0027DE70;
loc_0027E011:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 184))) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0027E435;
loc_0027E021:
    if (((*(unsigned __int8 *)(v_rip + 13929182)) & (1)) != 0) goto loc_0027E441;
loc_0027E02E:
loc_0027E03A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_r15, (unsigned __int8)(v_rsi), a4);
    v_rsp = (v_rsp) + (96);
    return result;
loc_0027E060:
    if ((*(unsigned __int64 *)(a1 + 96)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17600) + 56))) goto loc_0027E121;
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48)))) != 0) goto loc_0027DE70;
    if ((*(unsigned __int64 *)(a1 + 24)) == ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48)))))) goto loc_0027DE70;
    goto loc_0027E13D;
loc_0027E0B8:
    if (((*(unsigned __int64 *)(v_rip + 13928901)) & (0x600000ULL)) == 0) goto loc_0027DED6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_0027DED6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_0027DED6;
    a3 = ((unsigned __int8)(v_rsi)) >> (3);
    a3 = (unsigned int)((a3) & (511));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17616);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (32)) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17616)) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a3 * 8))) & (66)) == 0) { result = result; }
    goto loc_0027DED6;
loc_0027E121:
    if ((*(unsigned __int64 *)(a1 + 24)) == 0) goto loc_0027DE70;
loc_0027E13D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17608)) == (a1 + 24)) goto loc_0027DE70;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12292969, result, a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17600) + 53)) != 0) goto loc_0027E3F0;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_0027E3F0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8)) != (a1 + 24)) goto loc_0027E185;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24 + 8))) == (a1 + 24)) goto loc_0027E3A2;
loc_0027E185:
loc_0027E18C:
    result = MiPteHasShadow(3, result, a3, a4);
    if (result == 0) goto loc_0027DE37;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0027DE37;
    a3 = (a3) >> (3);
    a3 = (unsigned int)((a3) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (32)) != 0) {
        a2 = (result) | (32);
    }
    a2 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8))) & (66)) == 0) { a2 = a2; }
    goto loc_0027DE37;
loc_0027E1D3:
    if (!sign_flag) goto loc_0027DCD2;
    result = ExpWaitForSpinLockSharedAndAcquire(a2, 255, a3, a4);
    goto loc_0027DCBD;
loc_0027E1F0:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + a3 * 8)) == 0) goto loc_0027DD0B;
    if (a2 > result) goto loc_0027E1F0;
    goto loc_0027DD0B;
loc_0027E209:
    result = (unsigned int)((0) & (15));
    result = (unsigned int)((result) - 1);
    v_r10 = (*(unsigned __int64 *)(a1 + 144)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263032) + *(unsigned __int16 *)(a1 + 174) * 8) + 7232));
    if (v_r10 > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263032) + *(unsigned __int16 *)(a1 + 174) * 8) + result * 8 + 7240))) goto loc_0027E410;
loc_0027E249:
    if (((unsigned __int8)(a3)) != 3) goto loc_0027DD60;
    if (*(unsigned __int64 *)(v_rip + 13928654) == 0) goto loc_0027E275;
    if ((a1 + 24) >= (*(unsigned __int64 *)(v_rip + 13928654))) goto loc_0027E464;
loc_0027E268:
    if ((a1 + 24) >= (*(unsigned __int64 *)(v_rip + 13928745))) goto loc_0027E473;
loc_0027E275:
    result = MiGetSystemRegionType(a1 + 24, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263032) + *(unsigned __int16 *)(a1 + 174) * 8), a3, a4);
    if (((unsigned int)(result)) != 11) goto loc_0027DD60;
    a1 = (a1 + 24) >> (9);
    a1 = (a1) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48)))));
    a1 = (a1) + (1);
    result = MiIsDriverPage(a1, 1, a3, a4);
    if (result == 0) goto loc_0027DD60;
    goto loc_0027DD60;
loc_0027E2B5:
    if (v_rsi == 0) goto loc_0027DD1B;
    a1 = (v_rsi) + (v_rsi);
    if (a1 <= (*(unsigned __int64 *)(v_rip + 12297727))) goto loc_0027DD1B;
loc_0027E2E5:
    if (a1 == (*(unsigned __int64 *)(v_rip + 12297727))) goto loc_0027DD1B;
    if (a1 > (*(unsigned __int64 *)(v_rip + 12297727))) goto loc_0027E2E5;
    goto loc_0027DD1B;
loc_0027E2FE:
    if ((a1 + 24) > a3) goto loc_0027DD35;
    goto loc_0027DD3D;
loc_0027E30F:
    if (v_rsi > (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17600))) goto loc_0027DDFB;
    a1 = (v_rsi) >> (9);
    a1 = (a1) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + (unsigned __int8)(v_rsi) * 4 + 48)))));
    a1 = (a1) + (1);
    result = MI_READ_PTE_LOCK_FREE(a1, 1, a3, a4);
    result = (result) >> (12);
    result = (result) & (v_rip + 12298791);
    a2 = (result + result * 2) + (result + result * 2);
    a2 = (*(unsigned __int64 *)(a1 + 24 + a2 * 8)) >> (42);
    a2 = (unsigned int)((a2) & (7));
    goto loc_0027DE3E;
loc_0027E365:
    if (v_rsi <= (*(unsigned __int64 *)(a1 + 120))) goto loc_0027DD9E;
loc_0027E36F:
    goto loc_0027DD9E;
loc_0027E37C:
    if ((a1 + 24) > a3) goto loc_0027DC86;
    v_rsi = 0;
    goto loc_0027DC89;
loc_0027E38F:
    a3 = 0;
    result = MiRebuildPageTableAges(a1, 0, a3, a4);
    goto loc_0027DFDE;
loc_0027E3A2:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8)) + (0x44C8ULL);
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(result + 8) = a1;
    if (1 != 1) goto loc_0027E3D3;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8)) != v_rbx) goto loc_0027E185;
    *(unsigned __int64 *)(a1 + 24) = *(unsigned __int64 *)(v_rbx);
    *(unsigned __int64 *)(a1 + 24 + 8) = v_rbx;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx) + 8) = a1 + 24;
    *(unsigned __int64 *)(v_rbx) = a1 + 24;
    goto loc_0027E3F4;
loc_0027E3D3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) != v_rbx) goto loc_0027E185;
    *(unsigned __int64 *)(a1 + 24) = v_rbx;
    *(unsigned __int64 *)(a1 + 24 + 8) = *(unsigned __int64 *)(v_rbx + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = a1 + 24;
    *(unsigned __int64 *)(v_rbx + 8) = a1 + 24;
    goto loc_0027E3F4;
loc_0027E3F0:
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12263446) + *(unsigned __int16 *)(a1 + 174) * 8) + 17600) + 54) = 1;
loc_0027E3F4:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12292293, 0, a3, a4);
    goto loc_0027DE5C;
loc_0027E410:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8))) == v_rbx) goto loc_0027E249;
    if (v_r10 > result) goto loc_0027E410;
    goto loc_0027E249;
loc_0027E429:
    a1 = (v_rip + 12292293) + (256);
    goto loc_0027DCA3;
loc_0027E435:
    goto loc_0027E021;
loc_0027E441:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13171217))) != 0) goto loc_0027E02E;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(a1 + 256, v_stack_p98, a3, a4);
    goto loc_0027E03A;
loc_0027E464:
    if ((a1 + 24) >= (*(unsigned __int64 *)(v_rip + 13928517))) goto loc_0027E268;
    goto loc_0027E480;
loc_0027E473:
    if ((a1 + 24) >= (*(unsigned __int64 *)(v_rip + 13928726))) goto loc_0027E275;
loc_0027E480:
    goto loc_0027DD60;
loc_0027E48C:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 256 + 184))) & (15));
    result = (unsigned __int8)((result) - 1);
    if (((unsigned __int8)(result)) > 3) goto loc_0027DC5E;
    *(unsigned int *)(v_rip + 12292208) = 1;
    goto loc_0027DC5E;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddWorkingSetEntries(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p20;
    uint64_t v_stack_p98;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0xB8CB25)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m78 = Arg4;
    v_stack_m70 = Arg2;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) {
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB98C2))) == 0) goto loc_0027E48C;
loc_0027DC5E:
    if (Arg2 >= local_r12) goto loc_0027E37C;
loc_0027DC86:
loc_0027DC89:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0027E429;
loc_0027DCA3:
    if (((*(uint8_t *)(v_rip + 0xD48E5C)) & (33)) == 0) goto loc_0027DCC9;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC901A6))) != 0) goto loc_0027DCC9;
    result = ExpAcquireSpinLockSharedAtDpcLevelInstrumented(v_rip + 12299242, 255, Arg3, Arg4);
loc_0027DCBD:
    goto loc_0027DCDF;
loc_0027DCC9:
loc_0027DCD2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC901A6))) != 0) goto loc_0027E1D3;
loc_0027DCDF:
    if (Arg3 == 0) goto loc_0027DD0B;
    Arg1 = (Arg3) + (Arg3);
    if (Arg1 > (*(uint64_t *)(arg1 + 0xA0))) goto loc_0027E1F0;
loc_0027DD0B:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_0027E2B5;
loc_0027DD1B:
    if ((((uint8_t)((uint32_t)(Arg4))) & (2)) == 0) goto loc_0027DD3D;
    if (Arg2 >= local_r12) goto loc_0027E2FE;
loc_0027DD35:
loc_0027DD3D:
    Arg3 = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15));
    if (((uint8_t)(Arg3)) >= 1) goto loc_0027E209;
loc_0027DD60:
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) == 0) goto loc_0027DD9E;
    if ((*(uint64_t *)(arg1 + 0x80)) <= (*(uint64_t *)(arg1 + 0x70))) goto loc_0027DD9E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xBC)))) & (1)) != 0) goto loc_0027DD9E;
    result = MiWorkingSetVeryLarge(Arg1, Arg3, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if ((uint32_t)(result) != 0) goto loc_0027E36F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (64)) != 0) goto loc_0027E365;
loc_0027DD9E:
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) goto loc_0027E011;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (Arg3 == 0) goto loc_0027DE59;
loc_0027DDEF:
    if (Arg2 >= local_r12) goto loc_0027E30F;
loc_0027DDFB:
    Arg3 = (Arg2) >> (9);
    Arg3 = (Arg3) & (local_r13);
    Arg3 = (Arg3) + (local_r12);
    if (Arg3 < local_r10) goto loc_0027DE37;
    if (Arg3 > ((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) goto loc_0027DE37;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_0027DE37;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0027E18C;
loc_0027DE37:
    Arg2 = (*(uint64_t *)(Arg3)) >> (56);
    Arg2 = (uint32_t)((Arg2) & (15));
loc_0027DE3E:
    local_rsi = (Arg2) + (0x1000ULL);
    local_rbx = (Arg3) - (1);
    if (condition_is_not_equal) goto loc_0027DDEF;
loc_0027DE59:
loc_0027DE5C:
loc_0027DE70:
    local_rsi = (uint8_t)((8) + (255));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30))) == 0) goto loc_0027E008;
    Arg3 = (v_stack_m70) >> (18);
    Arg3 = (uint32_t)((Arg3) & (0x3FFFFFF8ULL));
    Arg3 = (Arg3) + (Arg2);
    if (Arg3 < local_r10) goto loc_0027DED6;
    if (Arg3 > local_r10) goto loc_0027DED6;
    if ((((uint8_t)(*(uint64_t *)(Arg3))) & (1)) == 0) goto loc_0027DED6;
    Arg2 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(Arg3))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_0027E0B8;
loc_0027DED6:
    result = (*(uint64_t *)(Arg3)) >> (12);
    result = (result) & (Arg1);
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + (result);
    Arg3 = (*(uint64_t *)(local_r15)) >> (45);
    result = (*(uint64_t *)(local_r15)) >> (55);
    Arg3 = (uint32_t)((Arg3) & (0x3FFULL));
    result = (uint8_t)((result) & (7));
    if (((v_stack_m78) & (8)) != 0) goto loc_0027DFF2;
    if (((uint8_t)(local_rsi)) == ((uint8_t)(result))) goto loc_0027DF50;
    if (((uint8_t)(local_rsi)) <= ((uint8_t)(result))) goto loc_0027DFF2;
    result = (uint32_t)(*(uint32_t *)(local_r15 + 0x24));
    if (((uint8_t)(local_rsi)) < ((uint8_t)(result))) {
        Arg3 = 0;
        Arg2 = local_r15;
        Arg1 = Arg1;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, v_stack_m70);
    }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30))))) & (0x3FFULL));
    goto loc_0027DFA8;
loc_0027DF50:
    Arg2 = ((uint32_t)((uint32_t)(local_r12 + Arg3 * 1))) << (45);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_r12 + Arg3 * 1))) & (0x3FFULL));
    Arg1 = (Arg2) ^ (*(uint64_t *)(local_r15));
    Arg1 = (Arg1) & (local_r11);
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(local_r15) = Arg1;
    if (Arg3 + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30)))) * 1 == 0) goto loc_0027E38F;
    if (condition_is_below) goto loc_0027DFF2;
    result = (uint32_t)(*(uint32_t *)(local_r15 + 0x24));
    if (!(condition_is_above_or_equal)) {
        Arg3 = 0;
        Arg2 = local_r15;
        Arg1 = Arg1;
        result = MiRemoveActivePageTableLinks(Arg1, Arg2, Arg3, v_stack_m70);
    }
    result = (uint32_t)(((uint8_t)(local_rsi)) & (7));
    local_rbx = (*(uint64_t *)(local_r15)) & (Arg1);
    result = (result) << (10);
    Arg4 = 0;
    result = (result) | (local_r12);
    result = (result) << (45);
    result = (result) | (local_rbx);
    *(uint64_t *)(local_r15) = result;
    result = MiInsertActivePageTableLinksTail(Arg1, local_r15, (uint8_t)(local_rsi), Arg4);
loc_0027DFDE:
loc_0027DFF2:
    if (((uint8_t)(local_rsi)) == 7) goto loc_0027E060;
loc_0027E008:
    if ((uint8_t)(local_rsi) != 0) goto loc_0027DE70;
loc_0027E011:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0027E435;
loc_0027E021:
    if (((*(uint8_t *)(v_rip + 0xD48ADE)) & (1)) != 0) goto loc_0027E441;
loc_0027E02E:
loc_0027E03A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_r15, (uint8_t)(local_rsi), Arg4);
    local_rsp = (local_rsp) + (96);
    return result;
loc_0027E060:
    if ((*(uint64_t *)(arg1 + 0x60)) >= (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44C0) + 0x38))) goto loc_0027E121;
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30)))) != 0) goto loc_0027DE70;
    if ((*(uint64_t *)(arg1 + 0x18)) == ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30)))))) goto loc_0027DE70;
    goto loc_0027E13D;
loc_0027E0B8:
    if (((*(uint64_t *)(v_rip + 0xD489C5)) & (0x600000ULL)) == 0) goto loc_0027DED6;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_0027DED6;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_0027DED6;
    Arg3 = ((uint8_t)(local_rsi)) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44D0);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (32)) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44D0)) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg3 * 8))) & (66)) == 0) { result = result; }
    goto loc_0027DED6;
loc_0027E121:
    if ((*(uint64_t *)(arg1 + 0x18)) == 0) goto loc_0027DE70;
loc_0027E13D:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44C8)) == (Arg1 + 24)) goto loc_0027DE70;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 12292969, result, Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44C0) + 0x35)) != 0) goto loc_0027E3F0;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_0027E3F0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)) != (Arg1 + 24)) goto loc_0027E185;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18 + 0x8))) == (Arg1 + 24)) goto loc_0027E3A2;
loc_0027E185:
loc_0027E18C:
    result = MiPteHasShadow(3, result, Arg3, Arg4);
    if (result == 0) goto loc_0027DE37;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0027DE37;
    Arg3 = (Arg3) >> (3);
    Arg3 = (uint32_t)((Arg3) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (32)) != 0) {
        Arg2 = (result) | (32);
    }
    Arg2 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8))) & (66)) == 0) { Arg2 = Arg2; }
    goto loc_0027DE37;
loc_0027E1D3:
    if (!sign_flag) goto loc_0027DCD2;
    result = ExpWaitForSpinLockSharedAndAcquire(Arg2, 255, Arg3, Arg4);
    goto loc_0027DCBD;
loc_0027E1F0:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + Arg3 * 8)) == 0) goto loc_0027DD0B;
    if (Arg2 > result) goto loc_0027E1F0;
    goto loc_0027DD0B;
loc_0027E209:
    result = (uint32_t)((0) & (15));
    result = (uint32_t)((result) - 1);
    local_r10 = (*(uint64_t *)(arg1 + 0x90)) + (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB1E78) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x1C40));
    if (local_r10 > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB1E78) + *(uint16_t *)(arg1 + 0xAE) * 8) + result * 8 + 0x1C48))) goto loc_0027E410;
loc_0027E249:
    if (((uint8_t)(Arg3)) != 3) goto loc_0027DD60;
    if (*(uint64_t *)(v_rip + 0xD488CE) == 0) goto loc_0027E275;
    if ((Arg1 + 24) >= (*(uint64_t *)(v_rip + 0xD488CE))) goto loc_0027E464;
loc_0027E268:
    if ((Arg1 + 24) >= (*(uint64_t *)(v_rip + 0xD48929))) goto loc_0027E473;
loc_0027E275:
    result = MiGetSystemRegionType(Arg1 + 24, *(uint64_t *)(*(uint64_t *)(v_rip + 0xBB1E78) + *(uint16_t *)(arg1 + 0xAE) * 8), Arg3, Arg4);
    if (((uint32_t)(result)) != 11) goto loc_0027DD60;
    Arg1 = (Arg1 + 24) >> (9);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30)))));
    Arg1 = (Arg1) + (1);
    result = MiIsDriverPage(Arg1, 1, Arg3, Arg4);
    if (result == 0) goto loc_0027DD60;
    goto loc_0027DD60;
loc_0027E2B5:
    if (local_rsi == 0) goto loc_0027DD1B;
    Arg1 = (local_rsi) + (local_rsi);
    if (Arg1 <= (*(uint64_t *)(v_rip + 0xBBA5FF))) goto loc_0027DD1B;
loc_0027E2E5:
    if (Arg1 == (*(uint64_t *)(v_rip + 0xBBA5FF))) goto loc_0027DD1B;
    if (Arg1 > (*(uint64_t *)(v_rip + 0xBBA5FF))) goto loc_0027E2E5;
    goto loc_0027DD1B;
loc_0027E2FE:
    if ((Arg1 + 24) > Arg3) goto loc_0027DD35;
    goto loc_0027DD3D;
loc_0027E30F:
    if (local_rsi > (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44C0))) goto loc_0027DDFB;
    Arg1 = (local_rsi) >> (9);
    Arg1 = (Arg1) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + (uint8_t)(local_rsi) * 4 + 0x30)))));
    Arg1 = (Arg1) + (1);
    result = MI_READ_PTE_LOCK_FREE(Arg1, 1, Arg3, Arg4);
    result = (result) >> (12);
    result = (result) & (v_rip + 12298791);
    Arg2 = (result + result * 2) + (result + result * 2);
    Arg2 = (*(uint64_t *)(arg1 + 0x18 + Arg2 * 8)) >> (42);
    Arg2 = (uint32_t)((Arg2) & (7));
    goto loc_0027DE3E;
loc_0027E365:
    if (local_rsi <= (*(uint64_t *)(arg1 + 0x78))) goto loc_0027DD9E;
loc_0027E36F:
    goto loc_0027DD9E;
loc_0027E37C:
    if ((Arg1 + 24) > Arg3) goto loc_0027DC86;
    local_rsi = 0;
    goto loc_0027DC89;
loc_0027E38F:
    Arg3 = 0;
    result = MiRebuildPageTableAges(Arg1, 0, Arg3, Arg4);
    goto loc_0027DFDE;
loc_0027E3A2:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8)) + (0x44C8ULL);
    *(uint64_t *)(arg1) = result;
    *(void **)(result + 0x8) = Arg1;
    if (1 != 1) goto loc_0027E3D3;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx) + 0x8)) != local_rbx) goto loc_0027E185;
    *(uint64_t *)(arg1 + 0x18) = *(uint64_t *)(local_rbx);
    *(uint64_t *)(arg1 + 0x18 + 0x8) = local_rbx;
    *(void **)(*(uint64_t *)(local_rbx) + 0x8) = Arg1 + 24;
    *(void **)(local_rbx) = Arg1 + 24;
    goto loc_0027E3F4;
loc_0027E3D3:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) != local_rbx) goto loc_0027E185;
    *(uint64_t *)(arg1 + 0x18) = local_rbx;
    *(uint64_t *)(arg1 + 0x18 + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    *(void **)(*(uint64_t *)(local_rbx + 0x8)) = Arg1 + 24;
    *(void **)(local_rbx + 0x8) = Arg1 + 24;
    goto loc_0027E3F4;
loc_0027E3F0:
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB2016) + *(uint16_t *)(arg1 + 0xAE) * 8) + 0x44C0) + 0x36) = 1;
loc_0027E3F4:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12292293, 0, Arg3, Arg4);
    goto loc_0027DE5C;
loc_0027E410:
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8))) == local_rbx) goto loc_0027E249;
    if (local_r10 > result) goto loc_0027E410;
    goto loc_0027E249;
loc_0027E429:
    Arg1 = (v_rip + 12292293) + (256);
    goto loc_0027DCA3;
loc_0027E435:
    goto loc_0027E021;
loc_0027E441:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8FA11))) != 0) goto loc_0027E02E;
    result = ExpReleaseSpinLockSharedFromDpcLevelInstrumented(Arg1 + 256, v_stack_p98, Arg3, Arg4);
    goto loc_0027E03A;
loc_0027E464:
    if ((Arg1 + 24) >= (*(uint64_t *)(v_rip + 0xD48845))) goto loc_0027E268;
    goto loc_0027E480;
loc_0027E473:
    if ((Arg1 + 24) >= (*(uint64_t *)(v_rip + 0xD48916))) goto loc_0027E275;
loc_0027E480:
    goto loc_0027DD60;
loc_0027E48C:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x100 + 0xB8))) & (15));
    result = (uint8_t)((result) - 1);
    if (((uint8_t)(result)) > 3) goto loc_0027DC5E;
    *(uint32_t *)(v_rip + 0xBB9070) = 1;
    goto loc_0027DC5E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28 + rbp*8` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R/W` |
| `Arg1` | `+ 0x88` | `64` | `R/W` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R/W` |
| `Arg1` | `+ 0x98` | `64` | `R/W` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xAE` | `16` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R` |
| `Arg1` | `+ 0xBC` | `32` | `R/W` |
| `Arg1` | `+ 0x100` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027DC00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
