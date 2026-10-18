# MiPfnsWorthTrying

- RVA: `0x0031B0C0`–`0x0031BAF5` (길이 `2,613` bytes)
- VA: `0x000000014031B0C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074D64`
- 디코드: `599`개 명령, `2,613/2,613` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x0031B270` → [MiActivePageClaimCandidate](MiActivePageClaimCandidate_function_0031BB00.md) (function, `0x0031BB00`)
- `0x0031B370` → [MiSafeLockPageAtDpc](MiSafeLockPageAtDpc_function_0031C67C.md) (function, `0x0031C67C`)
- `0x0031B38C` → [MiGetBaseResidentPage](MiGetBaseResidentPage_function_0031C750.md) (function, `0x0031C750`)
- `0x0031B3A1` → [MiGetPfnPageSizeIndex](MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0031B3CE` → [MiUnlockPage](MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0031B58B` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0031B5A3` → [MiClusterVadFull](../45/MiClusterVadFull_function_0045AECC.md) (function, `0x0045AECC`)
- `0x0031B5BE` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0031B6DE` → [MiRequestIoPageMdlCacheRelease](../44/MiRequestIoPageMdlCacheRelease_function_00442AD0.md) (function, `0x00442AD0`)
- `0x0031B722` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0031B788` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0031B860` → [MiFindNextLowerLargePageCandidate](../45/MiFindNextLowerLargePageCandidate_function_00454458.md) (function, `0x00454458`)
- `0x0031B98F` → [MiFindNextLowerLargePageCandidate](../45/MiFindNextLowerLargePageCandidate_function_00454458.md) (function, `0x00454458`)
- `0x0031B9CB` → [MiPfnLargeBitSet](../41/MiPfnLargeBitSet_function_00415A20.md) (function, `0x00415A20`)
- `0x0031B9FE` → [MiFindNextLowerLargePageCandidate](../45/MiFindNextLowerLargePageCandidate_function_00454458.md) (function, `0x00454458`)
- `0x0031BAA0` → [MiRequestIoPageMdlCacheRelease](../44/MiRequestIoPageMdlCacheRelease_function_00442AD0.md) (function, `0x00442AD0`)

### Direct callers
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028C1E2`
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028CCAE`
- [MiFindRebuildCandidate](MiFindRebuildCandidate_function_0031AE80.md) at `0x0031AFB0`
- [MiDefragmentSlabWorker](../68/MiDefragmentSlabWorker_function_0068D730.md) at `0x0068D922`
- [MmRelocatePfnList](../../page/90/MmRelocatePfnList_function_00901E70.md) at `0x00901FE3`
- [MiScrubNode](../../page/A4/MiScrubNode_function_00A46098.md) at `0x00A461C1`
- [MmIdentifyPhysicalMemory](../../page/AA/MmIdentifyPhysicalMemory_function_00AAD05C.md) at `0x00AAD1D0`

### Static image references
- `0x0031B0DE` → RVA `0x00EF5124` (`.data`; read)
- `0x0031B143` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0031B2C2` → RVA `0x00E3CBE6` (`.data`; read)
- `0x0031B2CA` → RVA `0x00E3D240` (`.data`; read)
- `0x0031B325` → RVA `0x00EF53AC` (`.data`; read/write)
- `0x0031B486` → RVA `0x00EF53C4` (`.data`; read/write)
- `0x0031B5B0` → RVA `0x00EF5464` (`.data`; read/write)
- `0x0031B689` → RVA `0x00EF5434` (`.data`; read/write)
- `0x0031B6A2` → RVA `0x00EF5420` (`.data`; read/write)
- `0x0031B70F` → RVA `0x00EF53C0` (`.data`; read/write)
- `0x0031B730` → RVA `0x00EF541C` (`.data`; read/write)
- `0x0031B760` → RVA `0x00EF53A8` (`.data`; read/write)
- `0x0031B77B` → RVA `0x00EF5140` (`.data`; read)
- `0x0031B7B1` → RVA `0x00EF53BC` (`.data`; read/write)
- `0x0031B7DA` → RVA `0x00EF5410` (`.data`; read/write)
- `0x0031B7F5` → RVA `0x00EF53B4` (`.data`; read/write)
- `0x0031B829` → RVA `0x00EF5450` (`.data`; read/write)
- `0x0031B86A` → RVA `0x00EF5394` (`.data`; read/write)
- `0x0031B87B` → RVA `0x00EF5398` (`.data`; read/write)
- `0x0031B902` → RVA `0x00EF53A4` (`.data`; read/write)
- `0x0031B947` → RVA `0x00EF5390` (`.data`; read/write)
- `0x0031B973` → RVA `0x00EF542C` (`.data`; read/write)
- `0x0031B99D` → RVA `0x00EF539C` (`.data`; read/write)
- `0x0031B9AB` → RVA `0x00EF53B0` (`.data`; read/write)
- `0x0031B9C4` → RVA `0x00E38D00` (`.data`; read)
- `0x0031BA0C` → RVA `0x00EF53B8` (`.data`; read/write)
- `0x0031BAC9` → RVA `0x00EF53A0` (`.data`; read/write)
- `0x0031BAD4` → RVA `0x00EF5430` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0031B0C0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0031B0C5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0031B0CA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0031B0CF  55                              push rbp
0031B0D0  56                              push rsi
0031B0D1  57                              push rdi
0031B0D2  41 54                           push r12
0031B0D4  41 55                           push r13
0031B0D6  41 56                           push r14
0031B0D8  41 57                           push r15
0031B0DA  48 83 EC 40                     sub rsp, 0x40
0031B0DE  8B 05 40 A0 BD 00               mov eax, dword ptr [rip + 0xbda040]
0031B0E4  45 8B E1                        mov r12d, r9d
0031B0E7  49 8B F8                        mov rdi, r8
0031B0EA  48 8B DA                        mov rbx, rdx
0031B0ED  48 8B E9                        mov rbp, rcx
0031B0F0  A8 02                           test al, 2
0031B0F2  0F 85 81 06 00 00               jne 0x14031b779
0031B0F8  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0031B100  4C 8D 3C 7F                     lea r15, [rdi + rdi*2]
0031B104  44 0F B7 6D 00                  movzx r13d, word ptr [rbp]
0031B109  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0031B110  49 C1 E7 04                     shl r15, 4
0031B114  48 BE 00 00 00 00 00 01 00 00   movabs rsi, 0x10000000000
0031B11E  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0031B123  4C 03 FB                        add r15, rbx
0031B126  41 C7 02 00 00 00 00            mov dword ptr [r10], 0
0031B12D  48 C7 84 24 88 00 00 00 00 00 00 00  mov qword ptr [rsp + 0x88], 0
0031B139  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0031B143  4C 8D 05 B6 4E CE FF            lea r8, [rip - 0x31b14a]
0031B14A  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
0031B154  B9 FF 03 00 00                  mov ecx, 0x3ff
0031B159  49 3B DF                        cmp rbx, r15
0031B15C  0F 83 39 05 00 00               jae 0x14031b69b
0031B162  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B166  48 C1 E8 2B                     shr rax, 0x2b
0031B16A  66 23 C1                        and ax, cx
0031B16D  66 41 3B C5                     cmp ax, r13w
0031B171  0F 85 A4 07 00 00               jne 0x14031b91b
0031B177  8B 7B 20                        mov edi, dword ptr [rbx + 0x20]
0031B17A  41 BE 03 00 00 00               mov r14d, 3
0031B180  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B184  C1 EF 10                        shr edi, 0x10
0031B187  83 E7 07                        and edi, 7
0031B18A  48 85 C6                        test rsi, rax
0031B18D  0F 85 A8 01 00 00               jne 0x14031b33b
0031B193  83 FF 05                        cmp edi, 5
0031B196  0F 84 1F 04 00 00               je 0x14031b5bb
0031B19C  83 FF 01                        cmp edi, 1
0031B19F  0F 86 A6 04 00 00               jbe 0x14031b64b
0031B1A5  33 F6                           xor esi, esi
0031B1A7  33 C9                           xor ecx, ecx
0031B1A9  41 0F BA E4 1C                  bt r12d, 0x1c
0031B1AE  0F 82 A4 07 00 00               jb 0x14031b958
0031B1B4  38 4B 23                        cmp byte ptr [rbx + 0x23], cl
0031B1B7  0F 8C 17 09 00 00               jl 0x14031bad4
0031B1BD  49 8B C1                        mov rax, r9
0031B1C0  4C 8B C3                        mov r8, rbx
0031B1C3  4C 2B C0                        sub r8, rax
0031B1C6  41 8B C4                        mov eax, r12d
0031B1C9  49 C1 F8 04                     sar r8, 4
0031B1CD  25 00 00 41 00                  and eax, 0x410000
0031B1D2  4D 0F AF C3                     imul r8, r11
0031B1D6  83 FF 04                        cmp edi, 4
0031B1D9  0F 86 DC 00 00 00               jbe 0x14031b2bb
0031B1DF  3D 00 00 41 00                  cmp eax, 0x410000
0031B1E4  74 12                           je 0x14031b1f8
0031B1E6  49 8B C0                        mov rax, r8
0031B1E9  48 25 00 FE FF FF               and rax, 0xfffffffffffffe00
0031B1EF  48 3B C2                        cmp rax, rdx
0031B1F2  0F 85 A4 02 00 00               jne 0x14031b49c
0031B1F8  B9 02 00 00 00                  mov ecx, 2
0031B1FD  83 FF 06                        cmp edi, 6
0031B200  0F 85 A5 07 00 00               jne 0x14031b9ab
0031B206  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B20A  48 C1 E8 3C                     shr rax, 0x3c
0031B20E  24 07                           and al, 7
0031B210  3A C1                           cmp al, cl
0031B212  0F 84 23 05 00 00               je 0x14031b73b
0031B218  41 0F BA E4 17                  bt r12d, 0x17
0031B21D  73 38                           jae 0x14031b257
0031B21F  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B223  48 85 C0                        test rax, rax
0031B226  0F 88 1C 02 00 00               js 0x14031b448
0031B22C  41 0F BA E4 1B                  bt r12d, 0x1b
0031B231  0F 82 A5 06 00 00               jb 0x14031b8dc
0031B237  BA 10 00 00 00                  mov edx, 0x10
0031B23C  48 8D 42 FF                     lea rax, [rdx - 1]
0031B240  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0031B248  48 F7 D0                        not rax
0031B24B  49 23 C0                        and rax, r8
0031B24E  4C 3B C0                        cmp r8, rax
0031B251  0F 84 13 03 00 00               je 0x14031b56a
0031B257  44 8B C1                        mov r8d, ecx
0031B25A  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
0031B25F  48 8B CD                        mov rcx, rbp
0031B262  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
0031B26A  45 8B CC                        mov r9d, r12d
0031B26D  48 8B D3                        mov rdx, rbx
0031B270  E8 8B 08 00 00                  call 0x14031bb00
0031B275  4C 8B C0                        mov r8, rax
0031B278  48 85 C0                        test rax, rax
0031B27B  0F 85 83 02 00 00               jne 0x14031b504
0031B281  41 F6 C4 08                     test r12b, 8
0031B285  0F 85 84 04 00 00               jne 0x14031b70f
0031B28B  85 F6                           test esi, esi
0031B28D  0F 85 02 03 00 00               jne 0x14031b595
0031B293  48 BE 00 00 00 00 00 01 00 00   movabs rsi, 0x10000000000
0031B29D  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
0031B2A5  48 83 C3 30                     add rbx, 0x30
0031B2A9  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0031B2AE  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0031B2B6  E9 7E FE FF FF                  jmp 0x14031b139
0031B2BB  3D 00 00 41 00                  cmp eax, 0x410000
0031B2C0  74 27                           je 0x14031b2e9
0031B2C2  38 0D 1E 19 B2 00               cmp byte ptr [rip + 0xb2191e], cl
0031B2C8  74 1F                           je 0x14031b2e9
0031B2CA  48 8B 05 6F 1F B2 00            mov rax, qword ptr [rip + 0xb21f6f]
0031B2D1  49 8B D0                        mov rdx, r8
0031B2D4  48 C1 EA 09                     shr rdx, 9
0031B2D8  0F B6 0C 50                     movzx ecx, byte ptr [rax + rdx*2]
0031B2DC  85 C9                           test ecx, ecx
0031B2DE  74 09                           je 0x14031b2e9
0031B2E0  83 F9 0A                        cmp ecx, 0xa
0031B2E3  0F 85 B9 03 00 00               jne 0x14031b6a2
0031B2E9  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031B2EC  66 85 C0                        test ax, ax
0031B2EF  0F 85 E6 03 00 00               jne 0x14031b6db
0031B2F5  48 BE 00 00 00 00 00 01 00 00   movabs rsi, 0x10000000000
0031B2FF  41 0F BA E4 1A                  bt r12d, 0x1a
0031B304  72 97                           jb 0x14031b29d
0031B306  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B30A  48 85 C6                        test rsi, rax
0031B30D  75 8E                           jne 0x14031b29d
0031B30F  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031B313  48 85 C0                        test rax, rax
0031B316  78 85                           js 0x14031b29d
0031B318  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031B31C  48 85 C0                        test rax, rax
0031B31F  0F 84 78 FF FF FF               je 0x14031b29d
0031B325  FF 05 81 A0 BD 00               inc dword ptr [rip + 0xbda081]
0031B32B  4C 2B FB                        sub r15, rbx
0031B32E  49 C1 FF 04                     sar r15, 4
0031B332  4D 0F AF FB                     imul r15, r11
0031B336  E9 13 02 00 00                  jmp 0x14031b54e
0031B33B  0F B6 7B 22                     movzx edi, byte ptr [rbx + 0x22]
0031B33F  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031B342  83 E7 07                        and edi, 7
0031B345  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B349  48 85 C6                        test rsi, rax
0031B34C  0F 84 B1 00 00 00               je 0x14031b403
0031B352  44 0F 20 C2                     mov rdx, cr8
0031B356  49 8B C1                        mov rax, r9
0031B359  48 8B CB                        mov rcx, rbx
0031B35C  48 2B C8                        sub rcx, rax
0031B35F  48 C1 F9 04                     sar rcx, 4
0031B363  49 0F AF CB                     imul rcx, r11
0031B367  80 FA 02                        cmp dl, 2
0031B36A  0F 82 1B 02 00 00               jb 0x14031b58b
0031B370  E8 07 13 00 00                  call 0x14031c67c
0031B375  0F B6 E8                        movzx ebp, al
0031B378  3C 11                           cmp al, 0x11
0031B37A  0F 84 1D FF FF FF               je 0x14031b29d
0031B380  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B384  48 85 C6                        test rsi, rax
0031B387  74 3E                           je 0x14031b3c7
0031B389  48 8B CB                        mov rcx, rbx
0031B38C  E8 BF 13 00 00                  call 0x14031c750
0031B391  48 8B F0                        mov rsi, rax
0031B394  48 8B CE                        mov rcx, rsi
0031B397  0F B6 78 22                     movzx edi, byte ptr [rax + 0x22]
0031B39B  8B 40 20                        mov eax, dword ptr [rax + 0x20]
0031B39E  83 E7 07                        and edi, 7
0031B3A1  E8 6A 13 00 00                  call 0x14031c710
0031B3A6  44 8B F0                        mov r14d, eax
0031B3A9  48 3B F3                        cmp rsi, rbx
0031B3AC  74 0F                           je 0x14031b3bd
0031B3AE  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0031B3B8  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0031B3BD  48 BE 00 00 00 00 00 01 00 00   movabs rsi, 0x10000000000
0031B3C7  40 0F B6 D5                     movzx edx, bpl
0031B3CB  48 8B CB                        mov rcx, rbx
0031B3CE  E8 0D F0 FF FF                  call 0x14031a3e0
0031B3D3  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0031B3D8  4C 8D 05 21 4C CE FF            lea r8, [rip - 0x31b3df]
0031B3DF  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0031B3E7  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
0031B3F1  48 8B AC 24 80 00 00 00         mov rbp, qword ptr [rsp + 0x80]
0031B3F9  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0031B403  41 83 FE 03                     cmp r14d, 3
0031B407  0F 84 90 FE FF FF               je 0x14031b29d
0031B40D  41 8B C6                        mov eax, r14d
0031B410  4D 8B 84 C0 60 1C 01 00         mov r8, qword ptr [r8 + rax*8 + 0x11c60]
0031B418  49 8B C1                        mov rax, r9
0031B41B  48 8B F3                        mov rsi, rbx
0031B41E  48 2B F0                        sub rsi, rax
0031B421  48 C1 FE 04                     sar rsi, 4
0031B425  49 0F AF F3                     imul rsi, r11
0031B429  83 FF 06                        cmp edi, 6
0031B42C  0F 84 10 04 00 00               je 0x14031b842
0031B432  48 BE 00 00 00 00 00 01 00 00   movabs rsi, 0x10000000000
0031B43C  4C 8D 05 BD 4B CE FF            lea r8, [rip - 0x31b443]
0031B443  E9 4B FD FF FF                  jmp 0x14031b193
0031B448  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031B44C  48 0F BA E0 28                  bt rax, 0x28
0031B451  72 0D                           jb 0x14031b460
0031B453  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031B457  48 85 C0                        test rax, rax
0031B45A  0F 89 67 03 00 00               jns 0x14031b7c7
0031B460  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031B464  48 BA FF FF FF FF FF FF FF 3F   movabs rdx, 0x3fffffffffffffff
0031B46E  48 23 C2                        and rax, rdx
0031B471  48 83 F8 01                     cmp rax, 1
0031B475  0F 86 DC FD FF FF               jbe 0x14031b257
0031B47B  41 0F BA E4 1B                  bt r12d, 0x1b
0031B480  0F 82 D1 FD FF FF               jb 0x14031b257
0031B486  FF 05 38 9F BD 00               inc dword ptr [rip + 0xbd9f38]
0031B48C  4C 2B FB                        sub r15, rbx
0031B48F  49 C1 FF 04                     sar r15, 4
0031B493  4D 0F AF FB                     imul r15, r11
0031B497  E9 B2 00 00 00                  jmp 0x14031b54e
0031B49C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0031B4A1  38 8D E6 3E 00 00               cmp byte ptr [rbp + 0x3ee6], cl
0031B4A7  0F 84 4B FD FF FF               je 0x14031b1f8
0031B4AD  45 33 C9                        xor r9d, r9d
0031B4B0  4C 8D 35 49 4B CE FF            lea r14, [rip - 0x31b4b7]
0031B4B7  41 83 F9 02                     cmp r9d, 2
0031B4BB  73 3A                           jae 0x14031b4f7
0031B4BD  41 8B C1                        mov eax, r9d
0031B4C0  48 03 C0                        add rax, rax
0031B4C3  48 39 B4 C5 C8 3F 00 00         cmp qword ptr [rbp + rax*8 + 0x3fc8], rsi
0031B4CB  74 25                           je 0x14031b4f2
0031B4CD  48 8B 84 C5 D0 3F 00 00         mov rax, qword ptr [rbp + rax*8 + 0x3fd0]
0031B4D5  49 8B D0                        mov rdx, r8
0031B4D8  43 8B 8C 8E E8 35 01 00         mov ecx, dword ptr [r14 + r9*4 + 0x135e8]
0031B4E0  48 D3 EA                        shr rdx, cl
0031B4E3  48 0F A3 10                     bt qword ptr [rax], rdx
0031B4E7  0F 92 C0                        setb al
0031B4EA  84 C0                           test al, al
0031B4EC  0F 85 FB 02 00 00               jne 0x14031b7ed
0031B4F2  41 FF C1                        inc r9d
0031B4F5  EB C0                           jmp 0x14031b4b7
0031B4F7  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0031B4FF  E9 F4 FC FF FF                  jmp 0x14031b1f8
0031B504  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0031B50E  48 8B C2                        mov rax, rdx
0031B511  48 2B D8                        sub rbx, rax
0031B514  48 B9 AB AA AA AA AA AA AA AA   movabs rcx, 0xaaaaaaaaaaaaaaab
0031B51E  48 C1 FB 04                     sar rbx, 4
0031B522  49 8D 40 FF                     lea rax, [r8 - 1]
0031B526  48 0F AF D9                     imul rbx, rcx
0031B52A  48 F7 D0                        not rax
0031B52D  48 23 D8                        and rbx, rax
0031B530  48 8B C2                        mov rax, rdx
0031B533  4C 2B F8                        sub r15, rax
0031B536  49 C1 FF 04                     sar r15, 4
0031B53A  4C 0F AF F9                     imul r15, rcx
0031B53E  49 81 F8 00 02 00 00            cmp r8, 0x200
0031B545  0F 83 3E 04 00 00               jae 0x14031b989
0031B54B  4C 2B FB                        sub r15, rbx
0031B54E  49 8B C7                        mov rax, r15
0031B551  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0031B559  48 83 C4 40                     add rsp, 0x40
0031B55D  41 5F                           pop r15
0031B55F  41 5E                           pop r14
0031B561  41 5D                           pop r13
0031B563  41 5C                           pop r12
0031B565  5F                              pop rdi
0031B566  5E                              pop rsi
0031B567  5D                              pop rbp
0031B568  C3                              ret
0031B569  CC                              int3
0031B56A  49 8B C7                        mov rax, r15
0031B56D  48 2B C3                        sub rax, rbx
0031B570  48 C1 F8 04                     sar rax, 4
0031B574  49 0F AF C3                     imul rax, r11
0031B578  48 3B C2                        cmp rax, rdx
0031B57B  0F 82 D6 FC FF FF               jb 0x14031b257
0031B581  BE 01 00 00 00                  mov esi, 1
0031B586  E9 CC FC FF FF                  jmp 0x14031b257
0031B58B  E8 90 60 00 00                  call 0x140321620
0031B590  E9 E0 FD FF FF                  jmp 0x14031b375
0031B595  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0031B59D  45 33 C0                        xor r8d, r8d
0031B5A0  48 8B CB                        mov rcx, rbx
0031B5A3  E8 24 F9 13 00                  call 0x14045aecc
0031B5A8  85 C0                           test eax, eax
0031B5AA  0F 84 E3 FC FF FF               je 0x14031b293
0031B5B0  FF 05 AE 9E BD 00               inc dword ptr [rip + 0xbd9eae]
0031B5B6  E9 3A 01 00 00                  jmp 0x14031b6f5
0031B5BB  48 8B CB                        mov rcx, rbx
0031B5BE  E8 55 5A F9 FF                  call 0x1402b1018
0031B5C3  85 C0                           test eax, eax
0031B5C5  0F 85 37 03 00 00               jne 0x14031b902
0031B5CB  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031B5CF  48 83 F8 F8                     cmp rax, -8
0031B5D3  0F 84 87 01 00 00               je 0x14031b760
0031B5D9  41 8B C4                        mov eax, r12d
0031B5DC  25 00 00 41 00                  and eax, 0x410000
0031B5E1  3D 00 00 41 00                  cmp eax, 0x410000
0031B5E6  0F 85 33 01 00 00               jne 0x14031b71f
0031B5EC  41 83 FE 03                     cmp r14d, 3
0031B5F0  75 63                           jne 0x14031b655
0031B5F2  48 8B 03                        mov rax, qword ptr [rbx]
0031B5F5  A8 01                           test al, 1
0031B5F7  0F 85 A0 FC FF FF               jne 0x14031b29d
0031B5FD  49 8B C1                        mov rax, r9
0031B600  4C 8B C3                        mov r8, rbx
0031B603  4C 8D 35 F6 49 CE FF            lea r14, [rip - 0x31b60a]
0031B60A  4C 2B C0                        sub r8, rax
0031B60D  49 C1 F8 04                     sar r8, 4
0031B611  4D 0F AF C3                     imul r8, r11
0031B615  45 33 C9                        xor r9d, r9d
0031B618  41 83 F9 02                     cmp r9d, 2
0031B61C  0F 83 7B FC FF FF               jae 0x14031b29d
0031B622  33 D2                           xor edx, edx
0031B624  48 83 FA 03                     cmp rdx, 3
0031B628  0F 8F E9 00 00 00               jg 0x14031b717
0031B62E  41 8B C1                        mov eax, r9d
0031B631  48 6B C8 07                     imul rcx, rax, 7
0031B635  48 03 CA                        add rcx, rdx
0031B638  4D 3B 84 CE 40 74 E3 00         cmp r8, qword ptr [r14 + rcx*8 + 0xe37440]
0031B640  0F 84 E3 01 00 00               je 0x14031b829
0031B646  48 FF C2                        inc rdx
0031B649  EB D9                           jmp 0x14031b624
0031B64B  41 83 FE 03                     cmp r14d, 3
0031B64F  0F 84 48 FC FF FF               je 0x14031b29d
0031B655  49 8B C1                        mov rax, r9
0031B658  48 8B D3                        mov rdx, rbx
0031B65B  48 2B D0                        sub rdx, rax
0031B65E  41 8B C6                        mov eax, r14d
0031B661  48 C1 FA 04                     sar rdx, 4
0031B665  49 0F AF D3                     imul rdx, r11
0031B669  49 8B 8C C0 60 1C 01 00         mov rcx, qword ptr [r8 + rax*8 + 0x11c60]
0031B671  48 81 F9 00 02 00 00            cmp rcx, 0x200
0031B678  0F 83 20 02 00 00               jae 0x14031b89e
0031B67E  41 0F BA E4 18                  bt r12d, 0x18
0031B683  0F 83 20 02 00 00               jae 0x14031b8a9
0031B689  FF 05 A5 9D BD 00               inc dword ptr [rip + 0xbd9da5]
0031B68F  48 F7 D9                        neg rcx
0031B692  48 23 CA                        and rcx, rdx
0031B695  48 8D 04 49                     lea rax, [rcx + rcx*2]
0031B699  EB 26                           jmp 0x14031b6c1
0031B69B  33 C0                           xor eax, eax
0031B69D  E9 AF FE FF FF                  jmp 0x14031b551
0031B6A2  FF 05 78 9D BD 00               inc dword ptr [rip + 0xbd9d78]
0031B6A8  49 8B C1                        mov rax, r9
0031B6AB  48 2B D8                        sub rbx, rax
0031B6AE  48 C1 FB 04                     sar rbx, 4
0031B6B2  49 0F AF DB                     imul rbx, r11
0031B6B6  48 81 E3 00 FE FF FF            and rbx, 0xfffffffffffffe00
0031B6BD  48 8D 04 5B                     lea rax, [rbx + rbx*2]
0031B6C1  48 C1 E0 04                     shl rax, 4
0031B6C5  4C 2B F8                        sub r15, rax
0031B6C8  49 8B C1                        mov rax, r9
0031B6CB  4C 2B F8                        sub r15, rax
0031B6CE  49 C1 FF 04                     sar r15, 4
0031B6D2  4D 0F AF FB                     imul r15, r11
0031B6D6  E9 73 FE FF FF                  jmp 0x14031b54e
0031B6DB  49 8B C8                        mov rcx, r8
0031B6DE  E8 ED 73 12 00                  call 0x140442ad0
0031B6E3  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031B6E6  66 85 C0                        test ax, ax
0031B6E9  0F 84 A0 01 00 00               je 0x14031b88f
0031B6EF  FF 05 B7 9C BD 00               inc dword ptr [rip + 0xbd9cb7]
0031B6F5  4C 2B FB                        sub r15, rbx
0031B6F8  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0031B702  49 C1 FF 04                     sar r15, 4
0031B706  49 0F AF C7                     imul rax, r15
0031B70A  E9 42 FE FF FF                  jmp 0x14031b551
0031B70F  FF 05 AB 9C BD 00               inc dword ptr [rip + 0xbd9cab]
0031B715  EB DE                           jmp 0x14031b6f5
0031B717  41 FF C1                        inc r9d
0031B71A  E9 F9 FE FF FF                  jmp 0x14031b618
0031B71F  48 8B CB                        mov rcx, rbx
0031B722  E8 A9 2B F7 FF                  call 0x14028e2d0
0031B727  83 F8 09                        cmp eax, 9
0031B72A  0F 84 BC FE FF FF               je 0x14031b5ec
0031B730  FF 05 E6 9C BD 00               inc dword ptr [rip + 0xbd9ce6]
0031B736  E9 6D FF FF FF                  jmp 0x14031b6a8
0031B73B  41 F6 C4 08                     test r12b, 8
0031B73F  0F 85 E1 02 00 00               jne 0x14031ba26
0031B745  48 8B 03                        mov rax, qword ptr [rbx]
0031B748  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
0031B752  48 85 C1                        test rcx, rax
0031B755  75 3B                           jne 0x14031b792
0031B757  41 83 0A 01                     or dword ptr [r10], 1
0031B75B  E9 33 FB FF FF                  jmp 0x14031b293
0031B760  FF 05 42 9C BD 00               inc dword ptr [rip + 0xbd9c42]
0031B766  4C 2B FB                        sub r15, rbx
0031B769  49 C1 FF 04                     sar r15, 4
0031B76D  4D 0F AF FB                     imul r15, r11
0031B771  49 8B C7                        mov rax, r15
0031B774  E9 D8 FD FF FF                  jmp 0x14031b551
0031B779  33 D2                           xor edx, edx
0031B77B  48 8D 0D BE 99 BD 00            lea rcx, [rip + 0xbd99be]
0031B782  41 B8 54 03 00 00               mov r8d, 0x354
0031B788  E8 B3 B4 3A 00                  call 0x1406c6c40
0031B78D  E9 66 F9 FF FF                  jmp 0x14031b0f8
0031B792  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0031B796  48 B9 00 00 00 00 00 F0 FF FF   movabs rcx, 0xfffff00000000000
0031B7A0  48 0B C1                        or rax, rcx
0031B7A3  48 C1 E0 03                     shl rax, 3
0031B7A7  48 83 F8 E0                     cmp rax, -0x20
0031B7AB  0F 85 E2 FA FF FF               jne 0x14031b293
0031B7B1  FF 05 05 9C BD 00               inc dword ptr [rip + 0xbd9c05]
0031B7B7  4C 2B FB                        sub r15, rbx
0031B7BA  49 C1 FF 04                     sar r15, 4
0031B7BE  4D 0F AF FB                     imul r15, r11
0031B7C2  E9 87 FD FF FF                  jmp 0x14031b54e
0031B7C7  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031B7CB  48 85 C0                        test rax, rax
0031B7CE  0F 84 8C FC FF FF               je 0x14031b460
0031B7D4  41 09 0A                        or dword ptr [r10], ecx
0031B7D7  4C 2B FB                        sub r15, rbx
0031B7DA  FF 05 30 9C BD 00               inc dword ptr [rip + 0xbd9c30]
0031B7E0  49 C1 FF 04                     sar r15, 4
0031B7E4  4D 0F AF FB                     imul r15, r11
0031B7E8  E9 61 FD FF FF                  jmp 0x14031b54e
0031B7ED  4B 8B 84 CE 60 1C 01 00         mov rax, qword ptr [r14 + r9*8 + 0x11c60]
0031B7F5  FF 05 B9 9B BD 00               inc dword ptr [rip + 0xbd9bb9]
0031B7FB  48 F7 D8                        neg rax
0031B7FE  49 23 C0                        and rax, r8
0031B801  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0031B80B  48 8D 04 40                     lea rax, [rax + rax*2]
0031B80F  48 C1 E0 04                     shl rax, 4
0031B813  4C 2B F8                        sub r15, rax
0031B816  48 8B C2                        mov rax, rdx
0031B819  4C 2B F8                        sub r15, rax
0031B81C  49 C1 FF 04                     sar r15, 4
0031B820  4D 0F AF FB                     imul r15, r11
0031B824  E9 25 FD FF FF                  jmp 0x14031b54e
0031B829  FF 05 21 9C BD 00               inc dword ptr [rip + 0xbd9c21]
0031B82F  4C 2B FB                        sub r15, rbx
0031B832  49 C1 FF 04                     sar r15, 4
0031B836  4D 0F AF FB                     imul r15, r11
0031B83A  49 8B C7                        mov rax, r15
0031B83D  E9 0F FD FF FF                  jmp 0x14031b551
0031B842  49 8D 40 FF                     lea rax, [r8 - 1]
0031B846  48 F7 D0                        not rax
0031B849  48 23 F0                        and rsi, rax
0031B84C  49 8B C1                        mov rax, r9
0031B84F  4C 2B F8                        sub r15, rax
0031B852  48 8B D6                        mov rdx, rsi
0031B855  49 C1 FF 04                     sar r15, 4
0031B859  48 8B CD                        mov rcx, rbp
0031B85C  4D 0F AF FB                     imul r15, r11
0031B860  E8 F3 8B 13 00                  call 0x140454458
0031B865  48 3B C6                        cmp rax, rsi
0031B868  72 11                           jb 0x14031b87b
0031B86A  FF 05 24 9B BD 00               inc dword ptr [rip + 0xbd9b24]
0031B870  4C 2B FE                        sub r15, rsi
0031B873  49 8B C7                        mov rax, r15
0031B876  E9 D6 FC FF FF                  jmp 0x14031b551
0031B87B  FF 05 17 9B BD 00               inc dword ptr [rip + 0xbd9b17]
0031B881  48 8B F0                        mov rsi, rax
0031B884  4C 2B F8                        sub r15, rax
0031B887  49 8B C7                        mov rax, r15
0031B88A  E9 C2 FC FF FF                  jmp 0x14031b551
0031B88F  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
0031B899  E9 57 FA FF FF                  jmp 0x14031b2f5
0031B89E  41 0F BA E4 19                  bt r12d, 0x19
0031B8A3  0F 82 E0 FD FF FF               jb 0x14031b689
0031B8A9  48 8D 41 FF                     lea rax, [rcx - 1]
0031B8AD  48 23 C2                        and rax, rdx
0031B8B0  48 2B C8                        sub rcx, rax
0031B8B3  49 8B C7                        mov rax, r15
0031B8B6  48 2B C3                        sub rax, rbx
0031B8B9  48 C1 F8 04                     sar rax, 4
0031B8BD  49 0F AF C3                     imul rax, r11
0031B8C1  48 3B C8                        cmp rcx, rax
0031B8C4  48 0F 47 C8                     cmova rcx, rax
0031B8C8  48 8D 04 49                     lea rax, [rcx + rcx*2]
0031B8CC  48 C1 E0 04                     shl rax, 4
0031B8D0  48 83 C0 D0                     add rax, -0x30
0031B8D4  48 03 D8                        add rbx, rax
0031B8D7  E9 C1 F9 FF FF                  jmp 0x14031b29d
0031B8DC  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
0031B8E4  48 83 F8 10                     cmp rax, 0x10
0031B8E8  0F 84 49 F9 FF FF               je 0x14031b237
0031B8EE  48 3D 00 02 00 00               cmp rax, 0x200
0031B8F4  0F 85 C2 01 00 00               jne 0x14031babc
0031B8FA  48 8B D0                        mov rdx, rax
0031B8FD  E9 3A F9 FF FF                  jmp 0x14031b23c
0031B902  FF 05 9C 9A BD 00               inc dword ptr [rip + 0xbd9a9c]
0031B908  4C 2B FB                        sub r15, rbx
0031B90B  49 C1 FF 04                     sar r15, 4
0031B90F  4D 0F AF FB                     imul r15, r11
0031B913  49 8B C7                        mov rax, r15
0031B916  E9 36 FC FF FF                  jmp 0x14031b551
0031B91B  49 8B C1                        mov rax, r9
0031B91E  48 2B D8                        sub rbx, rax
0031B921  48 C1 FB 04                     sar rbx, 4
0031B925  49 0F AF DB                     imul rbx, r11
0031B929  49 8B C1                        mov rax, r9
0031B92C  4C 2B F8                        sub r15, rax
0031B92F  41 81 E4 00 00 41 00            and r12d, 0x410000
0031B936  49 C1 FF 04                     sar r15, 4
0031B93A  4D 0F AF FB                     imul r15, r11
0031B93E  41 81 FC 00 00 41 00            cmp r12d, 0x410000
0031B945  75 7A                           jne 0x14031b9c1
0031B947  FF 05 43 9A BD 00               inc dword ptr [rip + 0xbd9a43]
0031B94D  4C 2B FB                        sub r15, rbx
0031B950  49 8B C7                        mov rax, r15
0031B953  E9 F9 FB FF FF                  jmp 0x14031b551
0031B958  83 FF 02                        cmp edi, 2
0031B95B  0F 84 22 01 00 00               je 0x14031ba83
0031B961  83 FF 07                        cmp edi, 7
0031B964  0F 84 19 01 00 00               je 0x14031ba83
0031B96A  83 FF 06                        cmp edi, 6
0031B96D  0F 84 C9 00 00 00               je 0x14031ba3c
0031B973  FF 05 B3 9A BD 00               inc dword ptr [rip + 0xbd9ab3]
0031B979  4C 2B FB                        sub r15, rbx
0031B97C  49 C1 FF 04                     sar r15, 4
0031B980  4D 0F AF FB                     imul r15, r11
0031B984  E9 C5 FB FF FF                  jmp 0x14031b54e
0031B989  48 8B D3                        mov rdx, rbx
0031B98C  48 8B CD                        mov rcx, rbp
0031B98F  E8 C4 8A 13 00                  call 0x140454458
0031B994  48 3B C3                        cmp rax, rbx
0031B997  0F 83 2C 01 00 00               jae 0x14031bac9
0031B99D  FF 05 F9 99 BD 00               inc dword ptr [rip + 0xbd99f9]
0031B9A3  48 8B D8                        mov rbx, rax
0031B9A6  E9 A0 FB FF FF                  jmp 0x14031b54b
0031B9AB  FF 05 FF 99 BD 00               inc dword ptr [rip + 0xbd99ff]
0031B9B1  4C 2B FB                        sub r15, rbx
0031B9B4  49 C1 FF 04                     sar r15, 4
0031B9B8  4D 0F AF FB                     imul r15, r11
0031B9BC  E9 8D FB FF FF                  jmp 0x14031b54e
0031B9C1  48 8B D3                        mov rdx, rbx
0031B9C4  48 8D 0D 35 D3 B1 00            lea rcx, [rip + 0xb1d335]
0031B9CB  E8 50 A0 0F 00                  call 0x140415a20
0031B9D0  83 F8 03                        cmp eax, 3
0031B9D3  0F 84 6E FF FF FF               je 0x14031b947
0031B9D9  8B C0                           mov eax, eax
0031B9DB  4C 8D 35 1E 46 CE FF            lea r14, [rip - 0x31b9e2]
0031B9E2  48 8D 0D 17 D3 B1 00            lea rcx, [rip + 0xb1d317]
0031B9E9  4D 8B 84 C6 60 1C 01 00         mov r8, qword ptr [r14 + rax*8 + 0x11c60]
0031B9F1  49 8D 40 FF                     lea rax, [r8 - 1]
0031B9F5  48 F7 D0                        not rax
0031B9F8  48 23 D8                        and rbx, rax
0031B9FB  48 8B D3                        mov rdx, rbx
0031B9FE  E8 55 8A 13 00                  call 0x140454458
0031BA03  48 3B C3                        cmp rax, rbx
0031BA06  0F 83 DE 00 00 00               jae 0x14031baea
0031BA0C  FF 05 A6 99 BD 00               inc dword ptr [rip + 0xbd99a6]
0031BA12  48 8B D8                        mov rbx, rax
0031BA15  FF 05 75 99 BD 00               inc dword ptr [rip + 0xbd9975]
0031BA1B  4C 2B F8                        sub r15, rax
0031BA1E  49 8B C7                        mov rax, r15
0031BA21  E9 2B FB FF FF                  jmp 0x14031b551
0031BA26  FF 05 94 99 BD 00               inc dword ptr [rip + 0xbd9994]
0031BA2C  4C 2B FB                        sub r15, rbx
0031BA2F  49 C1 FF 04                     sar r15, 4
0031BA33  4D 0F AF FB                     imul r15, r11
0031BA37  E9 12 FB FF FF                  jmp 0x14031b54e
0031BA3C  F6 43 22 10                     test byte ptr [rbx + 0x22], 0x10
0031BA40  0F 85 2D FF FF FF               jne 0x14031b973
0031BA46  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BA49  66 83 F8 01                     cmp ax, 1
0031BA4D  0F 85 20 FF FF FF               jne 0x14031b973
0031BA53  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BA57  48 C1 E8 3C                     shr rax, 0x3c
0031BA5B  24 07                           and al, 7
0031BA5D  3C 02                           cmp al, 2
0031BA5F  0F 84 0E FF FF FF               je 0x14031b973
0031BA65  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BA68  C1 E8 18                        shr eax, 0x18
0031BA6B  A8 08                           test al, 8
0031BA6D  0F 85 00 FF FF FF               jne 0x14031b973
0031BA73  48 8B 03                        mov rax, qword ptr [rbx]
0031BA76  A8 01                           test al, 1
0031BA78  0F 85 D9 F7 FF FF               jne 0x14031b257
0031BA7E  E9 F0 FE FF FF                  jmp 0x14031b973
0031BA83  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BA86  66 85 C0                        test ax, ax
0031BA89  0F 84 04 F8 FF FF               je 0x14031b293
0031BA8F  49 8B C1                        mov rax, r9
0031BA92  48 8B CB                        mov rcx, rbx
0031BA95  48 2B C8                        sub rcx, rax
0031BA98  48 C1 F9 04                     sar rcx, 4
0031BA9C  49 0F AF CB                     imul rcx, r11
0031BAA0  E8 2B 70 12 00                  call 0x140442ad0
0031BAA5  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BAA8  66 85 C0                        test ax, ax
0031BAAB  0F 84 E2 F7 FF FF               je 0x14031b293
0031BAB1  FF 05 75 99 BD 00               inc dword ptr [rip + 0xbd9975]
0031BAB7  E9 39 FC FF FF                  jmp 0x14031b6f5
0031BABC  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
0031BAC4  E9 8E F7 FF FF                  jmp 0x14031b257
0031BAC9  FF 05 D1 98 BD 00               inc dword ptr [rip + 0xbd98d1]
0031BACF  E9 77 FA FF FF                  jmp 0x14031b54b
0031BAD4  FF 05 56 99 BD 00               inc dword ptr [rip + 0xbd9956]
0031BADA  4C 2B FB                        sub r15, rbx
0031BADD  49 C1 FF 04                     sar r15, 4
0031BAE1  4D 0F AF FB                     imul r15, r11
0031BAE5  E9 64 FA FF FF                  jmp 0x14031b54e
0031BAEA  FF 05 C4 98 BD 00               inc dword ptr [rip + 0xbd98c4]
0031BAF0  E9 52 FE FF FF                  jmp 0x14031b947
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfnsWorthTrying(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (64);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12427328)))) & (2)) != 0) goto loc_0031B779;
loc_0031B0F8:
    v_r15 = (a3 + a3 * 2) << (4);
    v_stack_m48 = -1;
    v_r15 = (v_r15) + (a2);
    *(unsigned int *)(a5) = 0;
    v_stack_p10 = 0;
loc_0031B139:
    if (a2 >= v_r15) goto loc_0031B69B;
    result = (*(unsigned __int64 *)(a2 + 40)) >> (43);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)(*(unsigned __int16 *)(a1)))) goto loc_0031B91B;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (16));
    v_rdi = (unsigned int)((v_rdi) & (7));
    if (((v_rsi) & (*(unsigned __int64 *)(a2 + 40))) != 0) goto loc_0031B33B;
loc_0031B193:
    if (((unsigned int)(v_rdi)) == 5) goto loc_0031B5BB;
    if (((unsigned int)(v_rdi)) <= 1) goto loc_0031B64B;
    v_rsi = 0;
    a1 = 0;
    if (condition_is_below) goto loc_0031B958;
    if ((*(unsigned __int8 *)(a2 + 35)) < 0) goto loc_0031BAD4;
    a3 = (a2) - (a4);
    a3 = (a3) >> (4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x410000ULL));
    a3 = (a3) * (v_r11);
    if (((unsigned int)(v_rdi)) <= 4) goto loc_0031B2BB;
    if (((unsigned int)(result)) == 0x410000ULL) goto loc_0031B1F8;
    result = (a3) & (-512);
    if (result != -1) goto loc_0031B49C;
loc_0031B1F8:
    if (((unsigned int)(v_rdi)) != 6) goto loc_0031B9AB;
    result = (*(unsigned __int64 *)(a2 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0031B73B;
    if (((unsigned __int8)(result)) >= 2) goto loc_0031B257;
    if (sign_flag) goto loc_0031B448;
    if (condition_is_below) goto loc_0031B8DC;
loc_0031B237:
loc_0031B23C:
    v_stack_p10 = 16;
    result = ~(16 - 1);
    result = (result) & (a3);
    if (a3 == result) goto loc_0031B56A;
loc_0031B257:
    v_stack_m50 = a5;
    v_stack_m58 = 0;
    result = MiActivePageClaimCandidate(0, a2, 2, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (result != 0) goto loc_0031B504;
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) != 0) goto loc_0031B70F;
    if (0 != 0) goto loc_0031B595;
loc_0031B293:
loc_0031B29D:
    v_rbx = (a2) + (48);
    goto loc_0031B139;
loc_0031B2BB:
    if (((unsigned int)(result)) == 0x410000ULL) goto loc_0031B2E9;
    if ((*(unsigned __int8 *)(v_rip + 11671838)) == 0) goto loc_0031B2E9;
    a2 = (result) >> (9);
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11673455) + a2 * 2)) == 0) goto loc_0031B2E9;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11673455) + a2 * 2))) != 10) goto loc_0031B6A2;
loc_0031B2E9:
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbx + 32))) != 0) goto loc_0031B6DB;
loc_0031B2F5:
    if (condition_is_below) goto loc_0031B29D;
    if (((0) & (*(unsigned __int64 *)(v_rbx + 40))) != 0) goto loc_0031B29D;
    if (sign_flag) goto loc_0031B29D;
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_0031B29D;
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B33B:
    v_rdi = (unsigned int)((*(unsigned __int8 *)(v_rbx + 34)) & (7));
    if (((0) & (*(unsigned __int64 *)(v_rbx + 40))) == 0) goto loc_0031B403;
    a1 = (v_rbx) - ((unsigned int)((unsigned int)((unsigned int)(a4))));
    a1 = (a1) >> (4);
    a1 = (a1) * (v_r11);
    if (((unsigned __int8)(v_cr8)) < 2) goto loc_0031B58B;
    result = MiSafeLockPageAtDpc(a1, v_cr8, result, (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_0031B375:
    if (((unsigned __int8)(result)) == 17) goto loc_0031B29D;
    if (((0) & (*(unsigned __int64 *)(v_rbx + 40))) == 0) goto loc_0031B3C7;
    result = MiGetBaseResidentPage(v_rbx, v_cr8, result, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_rdi = (unsigned int)((*(unsigned __int8 *)(result + 34)) & (7));
    result = MiGetPfnPageSizeIndex(result, v_cr8, result, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (result != v_rbx) {
    }
loc_0031B3C7:
    result = MiUnlockPage(v_rbx, (unsigned __int8)((unsigned __int8)(result)), result, (unsigned int)((unsigned int)((unsigned int)(a4))));
loc_0031B403:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 3) goto loc_0031B29D;
    v_rsi = (v_rbx) - ((unsigned int)((unsigned int)((unsigned int)(a4))));
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * (v_r11);
    if (((unsigned int)(v_rdi)) == 6) goto loc_0031B842;
    goto loc_0031B193;
loc_0031B448:
    if (((unsigned int)(v_rdi)) < 6) goto loc_0031B460;
    if (!sign_flag) goto loc_0031B7C7;
loc_0031B460:
    result = (*(unsigned __int64 *)(v_rbx + 24)) & (v_stack_m48);
    if (result <= 1) goto loc_0031B257;
    if (result < 1) goto loc_0031B257;
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B49C:
    v_stack_m48 = result;
    if ((*(unsigned __int8 *)(v_stack_p8 + 16102)) == ((unsigned __int8)(v_rbx))) goto loc_0031B1F8;
    a4 = 0;
loc_0031B4B7:
    if (0 >= 2) goto loc_0031B4F7;
    result = (0) + (0);
    if ((*(unsigned __int64 *)(v_stack_p8 + result * 8 + 16328)) == v_rsi) goto loc_0031B4F2;
    a2 = (v_rip - 3257411) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip - 3257527 + a4 * 4 + 79336))));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_0031B7ED;
loc_0031B4F2:
    a4 = (unsigned int)((a4) + 1);
    goto loc_0031B4B7;
loc_0031B4F7:
    goto loc_0031B1F8;
loc_0031B504:
    v_rbx = (v_rbx) - (a2);
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * ((unsigned int)(*(unsigned int *)(v_rip - 3257527 + a4 * 4 + 79336)));
    result = ~(v_rip - 3257411 - 1);
    v_rbx = (v_rbx) & (result);
    v_r15 = (v_r15) - (a2);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * ((unsigned int)(*(unsigned int *)(v_rip - 3257527 + a4 * 4 + 79336)));
    if ((v_rip - 3257411) >= 512) goto loc_0031B989;
loc_0031B54B:
    v_r15 = (v_r15) - (v_rbx);
loc_0031B54E:
loc_0031B551:
    v_rsp = (v_rsp) + (64);
    return v_r15;
loc_0031B56A:
    result = (v_r15) - (v_stack_p20);
    result = (result) >> (4);
    result = (result) * (v_r11);
    if (result < a2) goto loc_0031B257;
    goto loc_0031B257;
loc_0031B58B:
    result = MiSafeLockPage((unsigned int)(*(unsigned int *)(v_rip - 3257527 + a4 * 4 + 79336)), a2, v_rip - 3257411, a4);
    goto loc_0031B375;
loc_0031B595:
    a3 = 0;
    result = MiClusterVadFull(v_stack_p20, v_stack_p88, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0031B293;
    goto loc_0031B6F5;
loc_0031B5BB:
    result = MiIsPageOnBadList(v_stack_p20, v_stack_p88, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0031B902;
    if ((*(unsigned __int64 *)(v_stack_p20 + 8)) == -8) goto loc_0031B760;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0x410000ULL));
    if (((unsigned int)(result)) != 0x410000ULL) goto loc_0031B71F;
loc_0031B5EC:
    if (((unsigned int)(v_rip - 3257527)) != 3) goto loc_0031B655;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p20))) & (1)) != 0) goto loc_0031B29D;
    a3 = (v_stack_p20) - (a4);
    a3 = (a3) >> (4);
    a3 = (a3) * (v_r11);
    a4 = 0;
loc_0031B618:
    if (0 >= 2) goto loc_0031B29D;
    a2 = 0;
loc_0031B624:
    if (0 > 3) goto loc_0031B717;
    a1 = (v_stack_p20) * (0);
    a1 = (a1) + (0);
    if (a3 == (*(unsigned __int64 *)(v_rip - 3257866 + a1 * 8 + 14906432))) goto loc_0031B829;
    a2 = (a2) + 1;
    goto loc_0031B624;
loc_0031B64B:
    if (((unsigned int)(v_rip - 3257866)) == 3) goto loc_0031B29D;
loc_0031B655:
    a2 = (v_stack_p20) - (0);
    a2 = (a2) >> (4);
    a2 = (a2) * (v_r11);
    if ((*(unsigned __int64 *)(a3 + (unsigned int)((unsigned int)(v_rip - 3257866)) * 8 + 72800)) >= 512) goto loc_0031B89E;
    if ((*(unsigned __int64 *)(a3 + (unsigned int)((unsigned int)(v_rip - 3257866)) * 8 + 72800)) >= 512) goto loc_0031B8A9;
loc_0031B689:
    a1 = -(*(unsigned __int64 *)(a3 + (unsigned int)((unsigned int)(v_rip - 3257866)) * 8 + 72800));
    a1 = (a1) & (a2);
    goto loc_0031B6C1;
loc_0031B69B:
    result = 0;
    goto loc_0031B551;
loc_0031B6A2:
loc_0031B6A8:
    v_rbx = (v_stack_p20) - (0);
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * (v_r11);
    v_rbx = (v_rbx) & (-512);
loc_0031B6C1:
    result = (v_rbx + v_rbx * 2) << (4);
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) - (0);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B6DB:
    result = MiRequestIoPageMdlCacheRelease(a3, a2, a3, a4);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbx + 32))) == 0) goto loc_0031B88F;
loc_0031B6F5:
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    result = ((unsigned int)(*(unsigned int *)(v_rbx + 32))) * (v_r15);
    goto loc_0031B551;
loc_0031B70F:
    goto loc_0031B6F5;
loc_0031B717:
    a4 = (unsigned int)((a4) + 1);
    goto loc_0031B618;
loc_0031B71F:
    result = MiGetPfnSlabType(v_rbx, a2, a3, a4);
    if (((unsigned int)(result)) == 9) goto loc_0031B5EC;
    goto loc_0031B6A8;
loc_0031B73B:
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) != 0) goto loc_0031BA26;
    if (((v_rbx) & (*(unsigned __int64 *)(v_rbx))) != 0) goto loc_0031B792;
    goto loc_0031B293;
loc_0031B760:
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B551;
loc_0031B779:
    a2 = 0;
    result = memset(v_rip + 12425662, a2, 852, a4);
    goto loc_0031B0F8;
loc_0031B792:
    result = (result) & (-2);
    result = (result) | (v_rip + 12425662);
    result = (result) << (3);
    if (result != -32) goto loc_0031B293;
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B7C7:
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_0031B460;
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B7ED:
    result = -(*(unsigned __int64 *)(v_rip - 3257866 + a4 * 8 + 72800));
    result = (result) & (852);
    result = (result + result * 2) << (4);
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) - (0);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B829:
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B551;
loc_0031B842:
    result = ~(852 - 1);
    v_rsi = (1) & (result);
    v_r15 = (v_r15) - (a4);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, v_rsi, 852, a4);
    if (result < v_rsi) goto loc_0031B87B;
    v_r15 = (v_r15) - (v_rsi);
    goto loc_0031B551;
loc_0031B87B:
    v_r15 = (v_r15) - (v_r15);
    goto loc_0031B551;
loc_0031B88F:
    goto loc_0031B2F5;
loc_0031B89E:
    if (condition_is_below) goto loc_0031B689;
loc_0031B8A9:
    result = (v_stack_p8 - 1) & (v_rsi);
    a1 = (v_stack_p8) - (result);
    result = (v_r15) - (v_rbx);
    result = (result) >> (4);
    result = (result) * (v_r11);
    if (a1 > result) { a1 = result; }
    result = (a1 + a1 * 2) << (4);
    result = (result) + (-48);
    v_rbx = (v_rbx) + (result);
    goto loc_0031B29D;
loc_0031B8DC:
    if (v_stack_p90 == 16) goto loc_0031B237;
    if (v_stack_p90 != 512) goto loc_0031BABC;
    goto loc_0031B23C;
loc_0031B902:
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B551;
loc_0031B91B:
    v_rbx = (v_rbx) - (a4);
    v_rbx = (v_rbx) >> (4);
    v_rbx = (v_rbx) * (v_r11);
    v_r15 = (v_r15) - (a4);
    v_r12 = (unsigned int)(((unsigned int)(a4)) & (0x410000ULL));
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    if (((unsigned int)(v_r12)) != 0x410000ULL) goto loc_0031B9C1;
loc_0031B947:
    v_r15 = (v_r15) - (v_rbx);
    goto loc_0031B551;
loc_0031B958:
    if (((unsigned int)(v_rdi)) == 2) goto loc_0031BA83;
    if (((unsigned int)(v_rdi)) == 7) goto loc_0031BA83;
    if (((unsigned int)(v_rdi)) == 6) goto loc_0031BA3C;
loc_0031B973:
    v_r15 = (v_r15) - (v_rbx);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B989:
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, v_rbx, 852, a4);
    if (result >= v_rbx) goto loc_0031BAC9;
    goto loc_0031B54B;
loc_0031B9AB:
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031B9C1:
    result = MiPfnLargeBitSet(v_rip + 11653941, result, 852, a4);
    if (((unsigned int)(result)) == 3) goto loc_0031B947;
    result = ~(*(unsigned __int64 *)(v_rip - 3258850 + (unsigned int)((unsigned int)(result)) * 8 + 72800) - 1);
    v_rbx = (result) & (result);
    result = MiFindNextLowerLargePageCandidate(v_rip + 11653911, v_rbx, *(unsigned __int64 *)(v_rip - 3258850 + (unsigned int)((unsigned int)(result)) * 8 + 72800), a4);
    if (result >= v_rbx) goto loc_0031BAEA;
    v_r15 = (v_r15) - (result);
    goto loc_0031B551;
loc_0031BA26:
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031BA3C:
    if (((*(unsigned __int8 *)(result + 34)) & (16)) != 0) goto loc_0031B973;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32)))) != 1) goto loc_0031B973;
    result = (*(unsigned __int64 *)(result + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0031B973;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0031B973;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) != 0) goto loc_0031B257;
    goto loc_0031B973;
loc_0031BA83:
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_0031B293;
    a1 = (result) - (a4);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_r11);
    result = MiRequestIoPageMdlCacheRelease(a1, v_rbx, *(unsigned __int64 *)(v_rip - 3258850 + (unsigned int)((unsigned int)(result)) * 8 + 72800), a4);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32))) == 0) goto loc_0031B293;
    goto loc_0031B6F5;
loc_0031BABC:
    v_stack_p88 = v_r15;
    goto loc_0031B257;
loc_0031BAC9:
    goto loc_0031B54B;
loc_0031BAD4:
    v_r15 = (v_r15) - (result);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * (v_r11);
    goto loc_0031B54E;
loc_0031BAEA:
    goto loc_0031B947;
}
```

## 5. (Beta) C Style

```c
int64_t MiPfnsWorthTrying(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (64);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBDA040)))) & (2)) != 0) goto loc_0031B779;
loc_0031B0F8:
    local_r15 = (Arg3 + Arg3 * 2) << (4);
    v_stack_m48 = -1;
    local_r15 = (local_r15) + (Arg2);
    *(uint32_t *)(arg5) = 0;
    v_stack_p10 = 0;
loc_0031B139:
    if (Arg2 >= local_r15) goto loc_0031B69B;
    result = (*(uint64_t *)(Arg2 + 0x28)) >> (43);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0x3FFULL))));
    if (((uint16_t)(result)) != ((uint16_t)(*(uint16_t *)(arg1)))) goto loc_0031B91B;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x20))) >> (16));
    local_rdi = (uint32_t)((local_rdi) & (7));
    if (((local_rsi) & (*(uint64_t *)(Arg2 + 0x28))) != 0) goto loc_0031B33B;
loc_0031B193:
    if (((uint32_t)(local_rdi)) == 5) goto loc_0031B5BB;
    if (((uint32_t)(local_rdi)) <= 1) goto loc_0031B64B;
    local_rsi = 0;
    Arg1 = 0;
    if (condition_is_below) goto loc_0031B958;
    if ((*(uint8_t *)(Arg2 + 0x23)) < 0) goto loc_0031BAD4;
    Arg3 = (Arg2) - (Arg4);
    Arg3 = (Arg3) >> (4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x410000ULL));
    Arg3 = (Arg3) * (local_r11);
    if (((uint32_t)(local_rdi)) <= 4) goto loc_0031B2BB;
    if (((uint32_t)(result)) == 0x410000ULL) goto loc_0031B1F8;
    result = (Arg3) & (-512);
    if (result != -1) goto loc_0031B49C;
loc_0031B1F8:
    if (((uint32_t)(local_rdi)) != 6) goto loc_0031B9AB;
    result = (*(uint64_t *)(Arg2 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0031B73B;
    if (((uint8_t)(result)) >= 2) goto loc_0031B257;
    if (sign_flag) goto loc_0031B448;
    if (condition_is_below) goto loc_0031B8DC;
loc_0031B237:
loc_0031B23C:
    v_stack_p10 = 16;
    result = ~(16 - 1);
    result = (result) & (Arg3);
    if (Arg3 == result) goto loc_0031B56A;
loc_0031B257:
    v_stack_m50 = Arg5;
    v_stack_m58 = 0;
    result = MiActivePageClaimCandidate(0, Arg2, 2, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (result != 0) goto loc_0031B504;
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) != 0) goto loc_0031B70F;
    if (0 != 0) goto loc_0031B595;
loc_0031B293:
loc_0031B29D:
    local_rbx = (Arg2) + (48);
    goto loc_0031B139;
loc_0031B2BB:
    if (((uint32_t)(result)) == 0x410000ULL) goto loc_0031B2E9;
    if ((*(uint8_t *)(v_rip + 0xB2191E)) == 0) goto loc_0031B2E9;
    Arg2 = (result) >> (9);
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB21F6F) + Arg2 * 2)) == 0) goto loc_0031B2E9;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB21F6F) + Arg2 * 2))) != 10) goto loc_0031B6A2;
loc_0031B2E9:
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) != 0) goto loc_0031B6DB;
loc_0031B2F5:
    if (condition_is_below) goto loc_0031B29D;
    if (((0) & (*(uint64_t *)(local_rbx + 0x28))) != 0) goto loc_0031B29D;
    if (sign_flag) goto loc_0031B29D;
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_0031B29D;
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B33B:
    local_rdi = (uint32_t)((*(uint8_t *)(local_rbx + 0x22)) & (7));
    if (((0) & (*(uint64_t *)(local_rbx + 0x28))) == 0) goto loc_0031B403;
    Arg1 = (local_rbx) - ((uint32_t)((uint32_t)((uint32_t)(Arg4))));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_r11);
    if (((uint8_t)(v_cr8)) < 2) goto loc_0031B58B;
    result = MiSafeLockPageAtDpc(Arg1, v_cr8, result, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_0031B375:
    if (((uint8_t)(result)) == 17) goto loc_0031B29D;
    if (((0) & (*(uint64_t *)(local_rbx + 0x28))) == 0) goto loc_0031B3C7;
    result = MiGetBaseResidentPage(local_rbx, v_cr8, result, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    local_rdi = (uint32_t)((*(uint8_t *)(result + 0x22)) & (7));
    result = MiGetPfnPageSizeIndex(result, v_cr8, result, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (result != local_rbx) {
    }
loc_0031B3C7:
    result = MiUnlockPage(local_rbx, (uint8_t)((uint8_t)(result)), result, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
loc_0031B403:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 3) goto loc_0031B29D;
    local_rsi = (local_rbx) - ((uint32_t)((uint32_t)((uint32_t)(Arg4))));
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * (local_r11);
    if (((uint32_t)(local_rdi)) == 6) goto loc_0031B842;
    goto loc_0031B193;
loc_0031B448:
    if (((uint32_t)(local_rdi)) < 6) goto loc_0031B460;
    if (!sign_flag) goto loc_0031B7C7;
loc_0031B460:
    result = (*(uint64_t *)(local_rbx + 0x18)) & (v_stack_m48);
    if (result <= 1) goto loc_0031B257;
    if (result < 1) goto loc_0031B257;
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B49C:
    v_stack_m48 = result;
    if ((*(uint8_t *)(v_stack_p8 + 0x3EE6)) == ((uint8_t)(local_rbx))) goto loc_0031B1F8;
    Arg4 = 0;
loc_0031B4B7:
    if (0 >= 2) goto loc_0031B4F7;
    result = (0) + (0);
    if ((*(uint64_t *)(v_stack_p8 + result * 8 + 0x3FC8)) == local_rsi) goto loc_0031B4F2;
    Arg2 = (v_rip - 3257411) >> ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip - 0x31B4B7 + Arg4 * 4 + 0x135E8))));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_0031B7ED;
loc_0031B4F2:
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_0031B4B7;
loc_0031B4F7:
    goto loc_0031B1F8;
loc_0031B504:
    local_rbx = (local_rbx) - (Arg2);
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * ((uint32_t)(*(uint32_t *)(v_rip - 0x31B4B7 + Arg4 * 4 + 0x135E8)));
    result = ~(v_rip - 3257411 - 1);
    local_rbx = (local_rbx) & (result);
    local_r15 = (local_r15) - (Arg2);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * ((uint32_t)(*(uint32_t *)(v_rip - 0x31B4B7 + Arg4 * 4 + 0x135E8)));
    if ((v_rip - 3257411) >= 512) goto loc_0031B989;
loc_0031B54B:
    local_r15 = (local_r15) - (local_rbx);
loc_0031B54E:
loc_0031B551:
    local_rsp = (local_rsp) + (64);
    return local_r15;
loc_0031B56A:
    result = (local_r15) - (v_stack_p20);
    result = (result) >> (4);
    result = (result) * (local_r11);
    if (result < Arg2) goto loc_0031B257;
    goto loc_0031B257;
loc_0031B58B:
    result = MiSafeLockPage((uint32_t)(*(uint32_t *)(v_rip - 0x31B4B7 + Arg4 * 4 + 0x135E8)), Arg2, v_rip - 3257411, Arg4);
    goto loc_0031B375;
loc_0031B595:
    Arg3 = 0;
    result = MiClusterVadFull(v_stack_p20, v_stack_p88, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0031B293;
    goto loc_0031B6F5;
loc_0031B5BB:
    result = MiIsPageOnBadList(v_stack_p20, v_stack_p88, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0031B902;
    if ((*(uint64_t *)(v_stack_p20 + 0x8)) == -8) goto loc_0031B760;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0x410000ULL));
    if (((uint32_t)(result)) != 0x410000ULL) goto loc_0031B71F;
loc_0031B5EC:
    if (((uint32_t)(v_rip - 3257527)) != 3) goto loc_0031B655;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p20))) & (1)) != 0) goto loc_0031B29D;
    Arg3 = (v_stack_p20) - (Arg4);
    Arg3 = (Arg3) >> (4);
    Arg3 = (Arg3) * (local_r11);
    Arg4 = 0;
loc_0031B618:
    if (0 >= 2) goto loc_0031B29D;
    Arg2 = 0;
loc_0031B624:
    if (0 > 3) goto loc_0031B717;
    Arg1 = (v_stack_p20) * (0);
    Arg1 = (Arg1) + (0);
    if (Arg3 == (*(uint64_t *)(v_rip - 0x31B60A + arg1 * 8 + 0xE37440))) goto loc_0031B829;
    Arg2 = (Arg2) + 1;
    goto loc_0031B624;
loc_0031B64B:
    if (((uint32_t)(v_rip - 3257866)) == 3) goto loc_0031B29D;
loc_0031B655:
    Arg2 = (v_stack_p20) - (0);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (local_r11);
    if ((*(uint64_t *)(arg3 + (uint32_t)((uint32_t)(v_rip - 0x31B60A)) * 8 + 0x11C60)) >= 512) goto loc_0031B89E;
    if ((*(uint64_t *)(arg3 + (uint32_t)((uint32_t)(v_rip - 0x31B60A)) * 8 + 0x11C60)) >= 512) goto loc_0031B8A9;
loc_0031B689:
    Arg1 = -(*(uint64_t *)(arg3 + (uint32_t)((uint32_t)(v_rip - 0x31B60A)) * 8 + 0x11C60));
    Arg1 = (Arg1) & (Arg2);
    goto loc_0031B6C1;
loc_0031B69B:
    result = 0;
    goto loc_0031B551;
loc_0031B6A2:
loc_0031B6A8:
    local_rbx = (v_stack_p20) - (0);
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * (local_r11);
    local_rbx = (local_rbx) & (-512);
loc_0031B6C1:
    result = (local_rbx + local_rbx * 2) << (4);
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) - (0);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B6DB:
    result = MiRequestIoPageMdlCacheRelease(Arg3, Arg2, Arg3, Arg4);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) == 0) goto loc_0031B88F;
loc_0031B6F5:
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    result = ((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) * (local_r15);
    goto loc_0031B551;
loc_0031B70F:
    goto loc_0031B6F5;
loc_0031B717:
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_0031B618;
loc_0031B71F:
    result = MiGetPfnSlabType(local_rbx, Arg2, Arg3, Arg4);
    if (((uint32_t)(result)) == 9) goto loc_0031B5EC;
    goto loc_0031B6A8;
loc_0031B73B:
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) != 0) goto loc_0031BA26;
    if (((local_rbx) & (*(uint64_t *)(local_rbx))) != 0) goto loc_0031B792;
    goto loc_0031B293;
loc_0031B760:
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B551;
loc_0031B779:
    Arg2 = 0;
    result = memset(v_rip + 12425662, Arg2, 852, Arg4);
    goto loc_0031B0F8;
loc_0031B792:
    result = (result) & (-2);
    result = (result) | (v_rip + 12425662);
    result = (result) << (3);
    if (result != -32) goto loc_0031B293;
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B7C7:
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_0031B460;
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B7ED:
    result = -(*(uint64_t *)(v_rip - 0x31B60A + Arg4 * 8 + 0x11C60));
    result = (result) & (852);
    result = (result + result * 2) << (4);
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) - (0);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B829:
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B551;
loc_0031B842:
    result = ~(852 - 1);
    local_rsi = (1) & (result);
    local_r15 = (local_r15) - (Arg4);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, local_rsi, 852, Arg4);
    if (result < local_rsi) goto loc_0031B87B;
    local_r15 = (local_r15) - (local_rsi);
    goto loc_0031B551;
loc_0031B87B:
    local_r15 = (local_r15) - (local_r15);
    goto loc_0031B551;
loc_0031B88F:
    goto loc_0031B2F5;
loc_0031B89E:
    if (condition_is_below) goto loc_0031B689;
loc_0031B8A9:
    result = (v_stack_p8 - 1) & (local_rsi);
    Arg1 = (v_stack_p8) - (result);
    result = (local_r15) - (local_rbx);
    result = (result) >> (4);
    result = (result) * (local_r11);
    if (Arg1 > result) { Arg1 = result; }
    result = (Arg1 + Arg1 * 2) << (4);
    result = (result) + (-48);
    local_rbx = (local_rbx) + (result);
    goto loc_0031B29D;
loc_0031B8DC:
    if (v_stack_p90 == 16) goto loc_0031B237;
    if (v_stack_p90 != 512) goto loc_0031BABC;
    goto loc_0031B23C;
loc_0031B902:
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B551;
loc_0031B91B:
    local_rbx = (local_rbx) - (Arg4);
    local_rbx = (local_rbx) >> (4);
    local_rbx = (local_rbx) * (local_r11);
    local_r15 = (local_r15) - (Arg4);
    local_r12 = (uint32_t)(((uint32_t)(Arg4)) & (0x410000ULL));
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    if (((uint32_t)(local_r12)) != 0x410000ULL) goto loc_0031B9C1;
loc_0031B947:
    local_r15 = (local_r15) - (local_rbx);
    goto loc_0031B551;
loc_0031B958:
    if (((uint32_t)(local_rdi)) == 2) goto loc_0031BA83;
    if (((uint32_t)(local_rdi)) == 7) goto loc_0031BA83;
    if (((uint32_t)(local_rdi)) == 6) goto loc_0031BA3C;
loc_0031B973:
    local_r15 = (local_r15) - (local_rbx);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B989:
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, local_rbx, 852, Arg4);
    if (result >= local_rbx) goto loc_0031BAC9;
    goto loc_0031B54B;
loc_0031B9AB:
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031B9C1:
    result = MiPfnLargeBitSet(v_rip + 11653941, result, 852, Arg4);
    if (((uint32_t)(result)) == 3) goto loc_0031B947;
    result = ~(*(uint64_t *)(v_rip - 0x31B9E2 + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60) - 1);
    local_rbx = (result) & (result);
    result = MiFindNextLowerLargePageCandidate(v_rip + 11653911, local_rbx, *(uint64_t *)(v_rip - 0x31B9E2 + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60), Arg4);
    if (result >= local_rbx) goto loc_0031BAEA;
    local_r15 = (local_r15) - (result);
    goto loc_0031B551;
loc_0031BA26:
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031BA3C:
    if (((*(uint8_t *)(result + 0x22)) & (16)) != 0) goto loc_0031B973;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) != 1) goto loc_0031B973;
    result = (*(uint64_t *)(result + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0031B973;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0031B973;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) != 0) goto loc_0031B257;
    goto loc_0031B973;
loc_0031BA83:
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_0031B293;
    Arg1 = (result) - (Arg4);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_r11);
    result = MiRequestIoPageMdlCacheRelease(Arg1, local_rbx, *(uint64_t *)(v_rip - 0x31B9E2 + (uint32_t)((uint32_t)(result)) * 8 + 0x11C60), Arg4);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20))) == 0) goto loc_0031B293;
    goto loc_0031B6F5;
loc_0031BABC:
    v_stack_p88 = local_r15;
    goto loc_0031B257;
loc_0031BAC9:
    goto loc_0031B54B;
loc_0031BAD4:
    local_r15 = (local_r15) - (result);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * (local_r11);
    goto loc_0031B54E;
loc_0031BAEA:
    goto loc_0031B947;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x0 + rdi*2` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R/W` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031B0C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
