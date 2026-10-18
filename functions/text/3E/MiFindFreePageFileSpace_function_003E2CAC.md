# MiFindFreePageFileSpace

- RVA: `0x003E2CAC`–`0x003E3238` (길이 `1,420` bytes)
- VA: `0x00000001403E2CAC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00094C34`
- 디코드: `378`개 명령, `1,420/1,420` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003E2D29` → [MiPageFileLargestBitmapsRun](../2A/MiPageFileLargestBitmapsRun_function_002AA708.md) (function, `0x002AA708`)
- `0x003E2D81` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x003E2E40` → [RtlLengthCurrentClearRunForward](RtlLengthCurrentClearRunForward_function_003E4B90.md) (function, `0x003E4B90`)
- `0x003E2E57` → [RtlLengthCurrentClearRunForward](RtlLengthCurrentClearRunForward_function_003E4B90.md) (function, `0x003E4B90`)
- `0x003E2F31` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x003E2F7B` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x003E2FA8` → [RtlSetBits](RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x003E2FCA` → [MiSetPageFileAllocationBits](MiSetPageFileAllocationBits_function_003E1D8C.md) (function, `0x003E1D8C`)
- `0x003E2FDF` → [MiInvalidatePageFileBitmapsCache](MiInvalidatePageFileBitmapsCache_function_003E3240.md) (function, `0x003E3240`)
- `0x003E2FFA` → [MiTransferSoftwarePte](../38/MiTransferSoftwarePte_function_003821F0.md) (function, `0x003821F0`)
- `0x003E3043` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x003E3065` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x003E30B0` → [MiPageFileLargestBitmapsRun](../2A/MiPageFileLargestBitmapsRun_function_002AA708.md) (function, `0x002AA708`)
- `0x003E30D9` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x003E30E3` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x003E30F0` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x003E30FA` → [MiRescanPagefileBitmaps](MiRescanPagefileBitmaps_function_003E5178.md) (function, `0x003E5178`)
- `0x003E310A` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003E312E` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003E31BC` → [MiFindFreePageFileSpaceForward](MiFindFreePageFileSpaceForward_function_003E43CC.md) (function, `0x003E43CC`)
- `0x003E321A` → [MiPageFileLargestBitmapsRun](../2A/MiPageFileLargestBitmapsRun_function_002AA708.md) (function, `0x002AA708`)

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x00373185`
- [MiReservePageFileSpace](../38/MiReservePageFileSpace_function_00383ED8.md) at `0x003841CF`
- [MiGetKernelStackSwapSupport](MiGetKernelStackSwapSupport_function_003E2900.md) at `0x003E29E8`
- [MiFindPageFileWriteCluster](MiFindPageFileWriteCluster_function_003E2B00.md) at `0x003E2B82`
- [MiTrimUnusedPageFileRegionsApc](../4D/MiTrimUnusedPageFileRegionsApc_function_004D3700.md) at `0x004D375C`
- [MiTrimUnusedPageFileRegionsApc](../4D/MiTrimUnusedPageFileRegionsApc_function_004D3700.md) at `0x004D37C5`
- [MiReserveWorkingSetSwapSpaceRuns](../../page/A8/MiReserveWorkingSetSwapSpaceRuns_function_00A834A4.md) at `0x00A83522`

### Static image references
- `0x003E2CFC` → RVA `0x00FC6C08` (`ALMOSTRO`; read)
- `0x003E2DA2` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003E3204` → [sub_006EA85E](../6E/Unknown_function_006EA85E.md) (`tail-transfer`)
  - `0x003E320C` → [sub_006EA85E](../6E/Unknown_function_006EA85E.md) (`tail-transfer`)
  - `0x003E322B` → [sub_006EA85E + 0xB](../6E/Unknown_function_006EA85E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E2CAC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003E2CB1  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003E2CB6  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003E2CBB  55                              push rbp
003E2CBC  56                              push rsi
003E2CBD  57                              push rdi
003E2CBE  41 54                           push r12
003E2CC0  41 55                           push r13
003E2CC2  41 56                           push r14
003E2CC4  41 57                           push r15
003E2CC6  48 8B EC                        mov rbp, rsp
003E2CC9  48 83 EC 70                     sub rsp, 0x70
003E2CCD  33 C0                           xor eax, eax
003E2CCF  0F 57 C0                        xorps xmm0, xmm0
003E2CD2  48 89 45 F8                     mov qword ptr [rbp - 8], rax
003E2CD6  45 8B E9                        mov r13d, r9d
003E2CD9  B8 FF FF FF FF                  mov eax, 0xffffffff
003E2CDE  4D 8B F0                        mov r14, r8
003E2CE1  4C 8B FA                        mov r15, rdx
003E2CE4  48 8B F9                        mov rdi, rcx
003E2CE7  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
003E2CEB  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
003E2CEF  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
003E2CF3  4C 3B C0                        cmp r8, rax
003E2CF6  0F 83 5E 02 00 00               jae 0x1403e2f5a
003E2CFC  48 8B 35 05 3F BE 00            mov rsi, qword ptr [rip + 0xbe3f05]
003E2D03  8B D8                           mov ebx, eax
003E2D05  41 F6 C5 10                     test r13b, 0x10
003E2D09  74 73                           je 0x1403e2d7e
003E2D0B  48 8B B7 60 48 00 00            mov rsi, qword ptr [rdi + 0x4860]
003E2D12  44 8B BF 58 48 00 00            mov r15d, dword ptr [rdi + 0x4858]
003E2D19  F6 86 AC 00 00 00 40            test byte ptr [rsi + 0xac], 0x40
003E2D20  0F 85 61 04 00 00               jne 0x1403e3187
003E2D26  48 8B CE                        mov rcx, rsi
003E2D29  E8 DA 79 EC FF                  call 0x1402aa708
003E2D2E  44 8B F0                        mov r14d, eax
003E2D31  41 83 FF 01                     cmp r15d, 1
003E2D35  76 41                           jbe 0x1403e2d78
003E2D37  4C 8D A7 68 48 00 00            lea r12, [rdi + 0x4868]
003E2D3E  41 FF CF                        dec r15d
003E2D41  49 8B 3C 24                     mov rdi, qword ptr [r12]
003E2D45  0F B7 96 AC 00 00 00            movzx edx, word ptr [rsi + 0xac]
003E2D4C  48 8D 8F AC 00 00 00            lea rcx, [rdi + 0xac]
003E2D53  F6 C2 10                        test dl, 0x10
003E2D56  0F 85 9F 04 00 00               jne 0x1403e31fb
003E2D5C  F6 C2 20                        test dl, 0x20
003E2D5F  0F 85 A4 04 00 00               jne 0x1403e3209
003E2D65  F6 01 30                        test byte ptr [rcx], 0x30
003E2D68  0F 84 A9 04 00 00               je 0x1403e3217
003E2D6E  49 83 C4 08                     add r12, 8
003E2D72  49 83 EF 01                     sub r15, 1
003E2D76  75 C9                           jne 0x1403e2d41
003E2D78  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
003E2D7C  EB 4C                           jmp 0x1403e2dca
003E2D7E  49 8B CF                        mov rcx, r15
003E2D81  E8 1A FB E9 FF                  call 0x1402828a0
003E2D86  48 C1 E8 0C                     shr rax, 0xc
003E2D8A  83 E0 0F                        and eax, 0xf
003E2D8D  48 8B B4 C7 60 48 00 00         mov rsi, qword ptr [rdi + rax*8 + 0x4860]
003E2D95  41 8B C5                        mov eax, r13d
003E2D98  24 65                           and al, 0x65
003E2D9A  3C 01                           cmp al, 1
003E2D9C  0F 84 0B 03 00 00               je 0x1403e30ad
003E2DA2  48 8B 05 D7 AE A4 00            mov rax, qword ptr [rip + 0xa4aed7]
003E2DA9  49 8B 1F                        mov rbx, qword ptr [r15]
003E2DAC  48 85 C0                        test rax, rax
003E2DAF  74 0B                           je 0x1403e2dbc
003E2DB1  F6 C3 10                        test bl, 0x10
003E2DB4  75 06                           jne 0x1403e2dbc
003E2DB6  48 F7 D0                        not rax
003E2DB9  48 23 D8                        and rbx, rax
003E2DBC  48 C1 EB 20                     shr rbx, 0x20
003E2DC0  41 F6 C5 10                     test r13b, 0x10
003E2DC4  0F 85 41 FF FF FF               jne 0x1403e2d0b
003E2DCA  33 C0                           xor eax, eax
003E2DCC  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
003E2DD3  41 8B D5                        mov edx, r13d
003E2DD6  83 E2 04                        and edx, 4
003E2DD9  89 55 50                        mov dword ptr [rbp + 0x50], edx
003E2DDC  45 33 FF                        xor r15d, r15d
003E2DDF  44 21 7D C0                     and dword ptr [rbp - 0x40], r15d
003E2DE3  85 D2                           test edx, edx
003E2DE5  0F 84 76 01 00 00               je 0x1403e2f61
003E2DEB  41 B4 11                        mov r12b, 0x11
003E2DEE  F6 86 AF 00 00 00 01            test byte ptr [rsi + 0xaf], 1
003E2DF5  0F 85 55 01 00 00               jne 0x1403e2f50
003E2DFB  41 B9 FF FF FF FF               mov r9d, 0xffffffff
003E2E01  41 3B D9                        cmp ebx, r9d
003E2E04  0F 84 84 00 00 00               je 0x1403e2e8e
003E2E0A  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
003E2E0E  3B 59 18                        cmp ebx, dword ptr [rcx + 0x18]
003E2E11  0F 83 2F 01 00 00               jae 0x1403e2f46
003E2E17  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
003E2E1B  8B D3                           mov edx, ebx
003E2E1D  48 0F A3 10                     bt qword ptr [rax], rdx
003E2E21  0F 92 C0                        setb al
003E2E24  84 C0                           test al, al
003E2E26  75 49                           jne 0x1403e2e71
003E2E28  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
003E2E2C  48 0F A3 10                     bt qword ptr [rax], rdx
003E2E30  0F 92 C0                        setb al
003E2E33  84 C0                           test al, al
003E2E35  75 3A                           jne 0x1403e2e71
003E2E37  45 8B C6                        mov r8d, r14d
003E2E3A  8B D3                           mov edx, ebx
003E2E3C  48 83 C1 18                     add rcx, 0x18
003E2E40  E8 4B 1D 00 00                  call 0x1403e4b90
003E2E45  41 3B C6                        cmp eax, r14d
003E2E48  75 21                           jne 0x1403e2e6b
003E2E4A  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
003E2E4E  44 8B C0                        mov r8d, eax
003E2E51  48 83 C1 08                     add rcx, 8
003E2E55  8B D3                           mov edx, ebx
003E2E57  E8 34 1D 00 00                  call 0x1403e4b90
003E2E5C  8B F8                           mov edi, eax
003E2E5E  41 3B C6                        cmp eax, r14d
003E2E61  74 10                           je 0x1403e2e73
003E2E63  41 F6 C5 40                     test r13b, 0x40
003E2E67  75 0A                           jne 0x1403e2e73
003E2E69  EB 06                           jmp 0x1403e2e71
003E2E6B  41 F6 C5 40                     test r13b, 0x40
003E2E6F  75 D9                           jne 0x1403e2e4a
003E2E71  33 FF                           xor edi, edi
003E2E73  8B C7                           mov eax, edi
003E2E75  49 3B C6                        cmp rax, r14
003E2E78  0F 84 07 01 00 00               je 0x1403e2f85
003E2E7E  41 F6 C5 40                     test r13b, 0x40
003E2E82  0F 85 FD 00 00 00               jne 0x1403e2f85
003E2E88  41 B9 FF FF FF FF               mov r9d, 0xffffffff
003E2E8E  41 F6 C5 08                     test r13b, 8
003E2E92  0F 85 14 03 00 00               jne 0x1403e31ac
003E2E98  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
003E2E9B  83 65 F8 00                     and dword ptr [rbp - 8], 0
003E2E9F  48 8D 4E 70                     lea rcx, [rsi + 0x70]
003E2EA3  F6 41 08 01                     test byte ptr [rcx + 8], 1
003E2EA7  48 8B 01                        mov rax, qword ptr [rcx]
003E2EAA  44 89 75 FC                     mov dword ptr [rbp - 4], r14d
003E2EAE  0F 85 17 03 00 00               jne 0x1403e31cb
003E2EB4  44 0F B6 41 08                  movzx r8d, byte ptr [rcx + 8]
003E2EB9  41 83 E0 01                     and r8d, 1
003E2EBD  45 33 FF                        xor r15d, r15d
003E2EC0  48 85 C0                        test rax, rax
003E2EC3  74 38                           je 0x1403e2efd
003E2EC5  44 3B 70 34                     cmp r14d, dword ptr [rax + 0x34]
003E2EC9  72 23                           jb 0x1403e2eee
003E2ECB  76 17                           jbe 0x1403e2ee4
003E2ECD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
003E2ED1  45 85 C0                        test r8d, r8d
003E2ED4  74 09                           je 0x1403e2edf
003E2ED6  48 85 C9                        test rcx, rcx
003E2ED9  0F 85 FE 02 00 00               jne 0x1403e31dd
003E2EDF  48 8B C1                        mov rax, rcx
003E2EE2  EB DC                           jmp 0x1403e2ec0
003E2EE4  83 78 30 00                     cmp dword ptr [rax + 0x30], 0
003E2EE8  0F 86 4A 02 00 00               jbe 0x1403e3138
003E2EEE  48 8B 08                        mov rcx, qword ptr [rax]
003E2EF1  4C 8B F8                        mov r15, rax
003E2EF4  EB DB                           jmp 0x1403e2ed1
003E2EF6  48 85 D2                        test rdx, rdx
003E2EF9  4C 0F 45 FA                     cmovne r15, rdx
003E2EFD  45 39 4F 34                     cmp dword ptr [r15 + 0x34], r9d
003E2F01  0F 85 19 01 00 00               jne 0x1403e3020
003E2F07  8B 46 6C                        mov eax, dword ptr [rsi + 0x6c]
003E2F0A  49 3B C6                        cmp rax, r14
003E2F0D  0F 82 5C 01 00 00               jb 0x1403e306f
003E2F13  83 F8 20                        cmp eax, 0x20
003E2F16  0F 82 53 01 00 00               jb 0x1403e306f
003E2F1C  85 FF                           test edi, edi
003E2F1E  0F 84 D3 01 00 00               je 0x1403e30f7
003E2F24  48 8D BE C8 00 00 00            lea rdi, [rsi + 0xc8]
003E2F2B  41 8A D4                        mov dl, r12b
003E2F2E  48 8B CF                        mov rcx, rdi
003E2F31  E8 BA 5C F6 FF                  call 0x140348bf0
003E2F36  8B 55 50                        mov edx, dword ptr [rbp + 0x50]
003E2F39  B8 01 00 00 00                  mov eax, 1
003E2F3E  48 8B CF                        mov rcx, rdi
003E2F41  E9 96 FE FF FF                  jmp 0x1403e2ddc
003E2F46  41 F6 C5 48                     test r13b, 0x48
003E2F4A  0F 84 3E FF FF FF               je 0x1403e2e8e
003E2F50  41 F6 C5 04                     test r13b, 4
003E2F54  0F 84 6F 01 00 00               je 0x1403e30c9
003E2F5A  33 C0                           xor eax, eax
003E2F5C  E9 A3 00 00 00                  jmp 0x1403e3004
003E2F61  44 0F 20 C2                     mov rdx, cr8
003E2F65  41 F6 C5 03                     test r13b, 3
003E2F69  0F 84 DB 00 00 00               je 0x1403e304a
003E2F6F  80 FA 02                        cmp dl, 2
003E2F72  0F 85 78 01 00 00               jne 0x1403e30f0
003E2F78  41 B4 11                        mov r12b, 0x11
003E2F7B  E8 00 5F E6 FF                  call 0x140248e80
003E2F80  E9 69 FE FF FF                  jmp 0x1403e2dee
003E2F85  89 5D 50                        mov dword ptr [rbp + 0x50], ebx
003E2F88  85 FF                           test edi, edi
003E2F8A  74 C4                           je 0x1403e2f50
003E2F8C  45 33 F6                        xor r14d, r14d
003E2F8F  41 F6 C5 01                     test r13b, 1
003E2F93  74 23                           je 0x1403e2fb8
003E2F95  48 8B 4E 50                     mov rcx, qword ptr [rsi + 0x50]
003E2F99  44 8B C7                        mov r8d, edi
003E2F9C  48 83 C1 18                     add rcx, 0x18
003E2FA0  8B D3                           mov edx, ebx
003E2FA2  41 BE 02 00 00 00               mov r14d, 2
003E2FA8  E8 63 E6 FF FF                  call 0x1403e1610
003E2FAD  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
003E2FB0  8B 5D 50                        mov ebx, dword ptr [rbp + 0x50]
003E2FB3  2B C7                           sub eax, edi
003E2FB5  89 46 14                        mov dword ptr [rsi + 0x14], eax
003E2FB8  41 F6 C5 02                     test r13b, 2
003E2FBC  74 11                           je 0x1403e2fcf
003E2FBE  41 83 CE 01                     or r14d, 1
003E2FC2  44 8B C7                        mov r8d, edi
003E2FC5  8B D3                           mov edx, ebx
003E2FC7  48 8B CE                        mov rcx, rsi
003E2FCA  E8 BD ED FF FF                  call 0x1403e1d8c
003E2FCF  45 85 F6                        test r14d, r14d
003E2FD2  74 10                           je 0x1403e2fe4
003E2FD4  4D 8B CF                        mov r9, r15
003E2FD7  44 8B C7                        mov r8d, edi
003E2FDA  8B D3                           mov edx, ebx
003E2FDC  48 8B CE                        mov rcx, rsi
003E2FDF  E8 5C 02 00 00                  call 0x1403e3240
003E2FE4  41 F6 C5 04                     test r13b, 4
003E2FE8  74 45                           je 0x1403e302f
003E2FEA  44 8B C3                        mov r8d, ebx
003E2FED  45 8B CE                        mov r9d, r14d
003E2FF0  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
003E2FF4  48 8B D6                        mov rdx, rsi
003E2FF7  48 8B 0B                        mov rcx, qword ptr [rbx]
003E2FFA  E8 F1 F1 F9 FF                  call 0x1403821f0
003E2FFF  48 89 03                        mov qword ptr [rbx], rax
003E3002  8B C7                           mov eax, edi
003E3004  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
003E300C  48 83 C4 70                     add rsp, 0x70
003E3010  41 5F                           pop r15
003E3012  41 5E                           pop r14
003E3014  41 5D                           pop r13
003E3016  41 5C                           pop r12
003E3018  5F                              pop rdi
003E3019  5E                              pop rsi
003E301A  5D                              pop rbp
003E301B  C3                              ret
003E301C  CC                              int3
003E301D  44 8B F1                        mov r14d, ecx
003E3020  41 8B 5F 30                     mov ebx, dword ptr [r15 + 0x30]
003E3024  41 8B FE                        mov edi, r14d
003E3027  89 5D 50                        mov dword ptr [rbp + 0x50], ebx
003E302A  E9 59 FF FF FF                  jmp 0x1403e2f88
003E302F  83 7D C0 00                     cmp dword ptr [rbp - 0x40], 0
003E3033  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
003E303A  41 8A D4                        mov dl, r12b
003E303D  0F 84 EB 00 00 00               je 0x1403e312e
003E3043  E8 A8 5B F6 FF                  call 0x140348bf0
003E3048  EB A0                           jmp 0x1403e2fea
003E304A  85 C0                           test eax, eax
003E304C  0F 85 1D FF FF FF               jne 0x1403e2f6f
003E3052  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
003E3059  80 FA 02                        cmp dl, 2
003E305C  0F 85 81 00 00 00               jne 0x1403e30e3
003E3062  41 B4 11                        mov r12b, 0x11
003E3065  E8 C6 5D E6 FF                  call 0x140248e30
003E306A  E9 7F FD FF FF                  jmp 0x1403e2dee
003E306F  45 84 ED                        test r13b, r13b
003E3072  0F 88 D8 FE FF FF               js 0x1403e2f50
003E3078  49 8B 07                        mov rax, qword ptr [r15]
003E307B  49 8B CF                        mov rcx, r15
003E307E  48 85 C0                        test rax, rax
003E3081  0F 84 15 01 00 00               je 0x1403e319c
003E3087  EB 04                           jmp 0x1403e308d
003E3089  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
003E308D  48 83 78 08 00                  cmp qword ptr [rax + 8], 0
003E3092  4C 8B F8                        mov r15, rax
003E3095  75 F2                           jne 0x1403e3089
003E3097  8B 46 6C                        mov eax, dword ptr [rsi + 0x6c]
003E309A  4D 85 FF                        test r15, r15
003E309D  75 75                           jne 0x1403e3114
003E309F  83 F8 20                        cmp eax, 0x20
003E30A2  0F 83 74 FE FF FF               jae 0x1403e2f1c
003E30A8  E9 A3 FE FF FF                  jmp 0x1403e2f50
003E30AD  48 8B CE                        mov rcx, rsi
003E30B0  E8 53 76 EC FF                  call 0x1402aa708
003E30B5  8B C0                           mov eax, eax
003E30B7  49 3B C6                        cmp rax, r14
003E30BA  0F 83 E2 FC FF FF               jae 0x1403e2da2
003E30C0  41 83 CD 10                     or r13d, 0x10
003E30C4  E9 F7 FC FF FF                  jmp 0x1403e2dc0
003E30C9  83 7D C0 00                     cmp dword ptr [rbp - 0x40], 0
003E30CD  48 8D 8E C8 00 00 00            lea rcx, [rsi + 0xc8]
003E30D4  41 8A D4                        mov dl, r12b
003E30D7  74 31                           je 0x1403e310a
003E30D9  E8 12 5B F6 FF                  call 0x140348bf0
003E30DE  E9 77 FE FF FF                  jmp 0x1403e2f5a
003E30E3  E8 F8 AB E6 FF                  call 0x14024dce0
003E30E8  44 8A E0                        mov r12b, al
003E30EB  E9 FE FC FF FF                  jmp 0x1403e2dee
003E30F0  E8 9B 55 E6 FF                  call 0x140248690
003E30F5  EB F1                           jmp 0x1403e30e8
003E30F7  48 8B CE                        mov rcx, rsi
003E30FA  E8 79 20 00 00                  call 0x1403e5178
003E30FF  41 B9 FF FF FF FF               mov r9d, 0xffffffff
003E3105  E9 91 FD FF FF                  jmp 0x1403e2e9b
003E310A  E8 B1 51 E6 FF                  call 0x1402482c0
003E310F  E9 46 FE FF FF                  jmp 0x1403e2f5a
003E3114  41 8B 4F 34                     mov ecx, dword ptr [r15 + 0x34]
003E3118  83 F8 20                        cmp eax, 0x20
003E311B  0F 82 FC FE FF FF               jb 0x1403e301d
003E3121  3B C1                           cmp eax, ecx
003E3123  0F 87 F3 FD FF FF               ja 0x1403e2f1c
003E3129  E9 EF FE FF FF                  jmp 0x1403e301d
003E312E  E8 8D 51 E6 FF                  call 0x1402482c0
003E3133  E9 B2 FE FF FF                  jmp 0x1403e2fea
003E3138  48 8B 08                        mov rcx, qword ptr [rax]
003E313B  4C 8B F8                        mov r15, rax
003E313E  45 85 C0                        test r8d, r8d
003E3141  74 09                           je 0x1403e314c
003E3143  48 85 C9                        test rcx, rcx
003E3146  0F 85 99 00 00 00               jne 0x1403e31e5
003E314C  33 D2                           xor edx, edx
003E314E  48 85 C9                        test rcx, rcx
003E3151  0F 84 A6 FD FF FF               je 0x1403e2efd
003E3157  44 3B 71 34                     cmp r14d, dword ptr [rcx + 0x34]
003E315B  72 10                           jb 0x1403e316d
003E315D  0F 87 8A 00 00 00               ja 0x1403e31ed
003E3163  83 79 30 00                     cmp dword ptr [rcx + 0x30], 0
003E3167  0F 86 C3 00 00 00               jbe 0x1403e3230
003E316D  48 8B 01                        mov rax, qword ptr [rcx]
003E3170  45 85 C0                        test r8d, r8d
003E3173  74 05                           je 0x1403e317a
003E3175  48 85 C0                        test rax, rax
003E3178  75 7C                           jne 0x1403e31f6
003E317A  48 8B C8                        mov rcx, rax
003E317D  48 85 C9                        test rcx, rcx
003E3180  75 D5                           jne 0x1403e3157
003E3182  E9 6F FD FF FF                  jmp 0x1403e2ef6
003E3187  45 33 F6                        xor r14d, r14d
003E318A  E9 A2 FB FF FF                  jmp 0x1403e2d31
003E318F  49 39 4F 08                     cmp qword ptr [r15 + 8], rcx
003E3193  0F 84 FE FE FF FF               je 0x1403e3097
003E3199  49 8B CF                        mov rcx, r15
003E319C  4D 8B 7F 10                     mov r15, qword ptr [r15 + 0x10]
003E31A0  49 83 E7 FC                     and r15, 0xfffffffffffffffc
003E31A4  0F 84 ED FE FF FF               je 0x1403e3097
003E31AA  EB E3                           jmp 0x1403e318f
003E31AC  45 8B CD                        mov r9d, r13d
003E31AF  89 5D 50                        mov dword ptr [rbp + 0x50], ebx
003E31B2  45 8B C6                        mov r8d, r14d
003E31B5  48 8D 55 50                     lea rdx, [rbp + 0x50]
003E31B9  48 8B CE                        mov rcx, rsi
003E31BC  E8 0B 12 00 00                  call 0x1403e43cc
003E31C1  8B 5D 50                        mov ebx, dword ptr [rbp + 0x50]
003E31C4  8B F8                           mov edi, eax
003E31C6  E9 BD FD FF FF                  jmp 0x1403e2f88
003E31CB  48 85 C0                        test rax, rax
003E31CE  74 08                           je 0x1403e31d8
003E31D0  48 33 C1                        xor rax, rcx
003E31D3  E9 DC FC FF FF                  jmp 0x1403e2eb4
003E31D8  E9 D7 FC FF FF                  jmp 0x1403e2eb4
003E31DD  48 33 C1                        xor rax, rcx
003E31E0  E9 DB FC FF FF                  jmp 0x1403e2ec0
003E31E5  48 33 C8                        xor rcx, rax
003E31E8  E9 5F FF FF FF                  jmp 0x1403e314c
003E31ED  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
003E31F1  E9 7A FF FF FF                  jmp 0x1403e3170
003E31F6  48 33 C8                        xor rcx, rax
003E31F9  EB 82                           jmp 0x1403e317d
003E31FB  F6 01 10                        test byte ptr [rcx], 0x10
003E31FE  0F 85 58 FB FF FF               jne 0x1403e2d5c
003E3204  E9 55 76 30 00                  jmp 0x1406ea85e
003E3209  F6 01 20                        test byte ptr [rcx], 0x20
003E320C  0F 84 4C 76 30 00               je 0x1406ea85e
003E3212  E9 4E FB FF FF                  jmp 0x1403e2d65
003E3217  48 8B CF                        mov rcx, rdi
003E321A  E8 E9 74 EC FF                  call 0x1402aa708
003E321F  41 3B C6                        cmp eax, r14d
003E3222  0F 86 46 FB FF FF               jbe 0x1403e2d6e
003E3228  48 8B F7                        mov rsi, rdi
003E322B  E9 39 76 30 00                  jmp 0x1406ea869
003E3230  48 8B D1                        mov rdx, rcx
003E3233  E9 35 FF FF FF                  jmp 0x1403e316d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindFreePageFileSpace(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m3C;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m40 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (a3 >= ((unsigned int)(0xFFFFFFFFULL))) goto loc_003E2F5A;
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) == 0) goto loc_003E2D7E;
loc_003E2D0B:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 18528) + 172)) & (64)) != 0) goto loc_003E3187;
    result = MiPageFileLargestBitmapsRun(*(unsigned __int64 *)(a1 + 18528), a2, a3, a4);
loc_003E2D31:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18520)))) <= 1) goto loc_003E2D78;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 18520))) - 1);
loc_003E2D41:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 18528) + 172))) & (16)) != 0) goto loc_003E31FB;
loc_003E2D5C:
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 18528) + 172))) & (32)) != 0) goto loc_003E3209;
loc_003E2D65:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 18536) + 172)) & (48)) == 0) goto loc_003E3217;
loc_003E2D6E:
    v_r12 = (a1 + 18536) + (8);
    v_r15 = (v_r15) - (1);
    if (condition_is_not_equal) goto loc_003E2D41;
loc_003E2D78:
    goto loc_003E2DCA;
loc_003E2D7E:
    result = MI_READ_PTE_LOCK_FREE(v_r15, *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 18528) + 172), a3, a4);
    result = (result) >> (12);
    result = (unsigned int)((result) & (15));
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (101));
    if (((unsigned __int8)(result)) == 1) goto loc_003E30AD;
loc_003E2DA2:
    if (*(unsigned __int64 *)(v_rip + 10792663) == 0) goto loc_003E2DBC;
    result = *(unsigned __int64 *)(v_rip + 10792663);
    v_rbx = *(unsigned __int64 *)(v_r15);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10792663));
        v_rbx = (*(unsigned __int64 *)(v_r15)) & (result);
    }
    v_rbx = (v_rbx) >> (32);
loc_003E2DC0:
    if ((((unsigned __int8)((unsigned int)(a4))) & (16)) != 0) goto loc_003E2D0B;
loc_003E2DCA:
    result = 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (4));
    v_stack_p18 = (unsigned int)(a2);
loc_003E2DDC:
    v_r15 = 0;
    if ((unsigned int)(a2) == 0) goto loc_003E2F61;
loc_003E2DEE:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 175)) & (1)) != 0) goto loc_003E2F50;
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E2E8E;
    if (((unsigned int)(v_rbx)) >= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 80) + 24))) goto loc_003E2F46;
    result = (((unsigned int)(v_rbx)) < (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 80) + 24))) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_003E2E71;
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_003E2E71;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 80)) + (24);
    result = RtlLengthCurrentClearRunForward(a1, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_stack_p18)), (unsigned int)(0xFFFFFFFFULL));
    if (((unsigned int)(result)) != ((unsigned int)(v_stack_p18))) goto loc_003E2E6B;
loc_003E2E4A:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 80)) + (8);
    result = RtlLengthCurrentClearRunForward(a1, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(result)), (unsigned int)(0xFFFFFFFFULL));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_p18))) goto loc_003E2E73;
    if ((((unsigned __int8)((unsigned int)(a4))) & (64)) != 0) goto loc_003E2E73;
    goto loc_003E2E71;
loc_003E2E6B:
    if ((((unsigned __int8)((unsigned int)(a4))) & (64)) != 0) goto loc_003E2E4A;
loc_003E2E71:
    v_rdi = 0;
loc_003E2E73:
    if (0 == v_stack_p18) goto loc_003E2F85;
    if ((((unsigned __int8)((unsigned int)(a4))) & (64)) != 0) goto loc_003E2F85;
loc_003E2E8E:
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) != 0) goto loc_003E31AC;
loc_003E2E9B:
    v_stack_m3C = (unsigned int)(v_stack_p18);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112 + 8)) & (1)) != 0) goto loc_003E31CB;
loc_003E2EB4:
    a3 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112 + 8)) & (1));
    v_r15 = 0;
loc_003E2EC0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) == 0) goto loc_003E2EFD;
    if (((unsigned int)(v_stack_p18)) < (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) + 52))) goto loc_003E2EEE;
    if (((unsigned int)(v_stack_p18)) <= (*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) + 52))) goto loc_003E2EE4;
loc_003E2ED1:
    if ((unsigned int)(a3) == 0) goto loc_003E2EDF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) + 8) != 0) goto loc_003E31DD;
loc_003E2EDF:
    goto loc_003E2EC0;
loc_003E2EE4:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) + 8) + 48)) <= 0) goto loc_003E3138;
loc_003E2EEE:
    goto loc_003E2ED1;
loc_003E2EF6:
    v_r15 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 112) + 8);
    if ((unsigned int)((unsigned int)(v_rbx)) != 0) { v_r15 = (unsigned int)((unsigned int)(v_rbx)); }
loc_003E2EFD:
    if ((*(unsigned int *)(v_r15 + 52)) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_003E3020;
    if (((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 108))) < v_stack_p18) goto loc_003E306F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 108)))) < 32) goto loc_003E306F;
loc_003E2F1C:
    if ((unsigned int)((unsigned int)(v_stack_m78)) == 0) goto loc_003E30F7;
    result = MiReleaseSpinLockShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, a3, (unsigned int)(0xFFFFFFFFULL));
    goto loc_003E2DDC;
loc_003E2F46:
    if ((((unsigned __int8)((unsigned int)(a4))) & (72)) == 0) goto loc_003E2E8E;
loc_003E2F50:
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) goto loc_003E30C9;
loc_003E2F5A:
    result = 0;
    goto loc_003E3004;
loc_003E2F61:
    if ((((unsigned __int8)((unsigned int)(a4))) & (3)) == 0) goto loc_003E304A;
loc_003E2F6F:
    if (((unsigned __int8)(v_cr8)) != 2) goto loc_003E30F0;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, v_cr8, a3, (unsigned int)(0xFFFFFFFFULL));
    goto loc_003E2DEE;
loc_003E2F85:
    v_stack_p18 = (unsigned int)(v_rbx);
loc_003E2F88:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200) == 0) goto loc_003E2F50;
    v_r14 = 0;
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 80);
        a3 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200);
        a1 = (a1) + (24);
        a2 = (unsigned int)(v_rbx);
        v_r14 = 2;
        result = RtlSetBits(a1, a2, a3, (unsigned int)(0xFFFFFFFFULL));
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 20);
        v_rbx = v_stack_p18;
        result = (unsigned int)((result) - ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200)));
        *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 20) = (unsigned int)(result);
    }
    if ((((unsigned __int8)((unsigned int)(a4))) & (2)) != 0) {
        v_r14 = (unsigned int)((v_r14) | (1));
        a3 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200);
        a2 = (unsigned int)(v_rbx);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528);
        result = MiSetPageFileAllocationBits(a1, a2, a3, (unsigned int)(0xFFFFFFFFULL));
    }
    if ((unsigned int)(v_r14) != 0) {
        a4 = v_r15;
        a3 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200);
        a2 = (unsigned int)(v_rbx);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528);
        result = MiInvalidatePageFileBitmapsCache(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) goto loc_003E302F;
loc_003E2FEA:
    result = MiTransferSoftwarePte(*(unsigned __int64 *)(v_stack_p10), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    *(unsigned __int64 *)(v_stack_p10) = result;
loc_003E3004:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200));
loc_003E301D:
loc_003E3020:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 48)));
    goto loc_003E2F88;
loc_003E302F:
    if (v_stack_m78 == 0) goto loc_003E312E;
    result = MiReleaseSpinLockShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_003E2FEA;
loc_003E304A:
    if ((unsigned int)(result) != 0) goto loc_003E2F6F;
    v_stack_m78 = 1;
    if (17 != 2) goto loc_003E30E3;
    result = ExAcquireSpinLockSharedAtDpcLevel(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_003E2DEE;
loc_003E306F:
    if (sign_flag) goto loc_003E2F50;
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_003E319C;
    goto loc_003E308D;
loc_003E3089:
loc_003E308D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8)) != 0) goto loc_003E3089;
loc_003E3097:
    if (*(unsigned __int64 *)(v_r15 + 8) != 0) goto loc_003E3114;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 108)))) >= 32) goto loc_003E2F1C;
    goto loc_003E2F50;
loc_003E30AD:
    result = MiPageFileLargestBitmapsRun(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528), 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    if (((unsigned int)((unsigned int)(result))) >= ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p10))))) goto loc_003E2DA2;
    v_r13 = (unsigned int)(((unsigned int)(a4)) | (16));
    goto loc_003E2DC0;
loc_003E30C9:
    if (v_stack_m78 == 0) goto loc_003E310A;
    result = MiReleaseSpinLockShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_003E2F5A;
loc_003E30E3:
    result = ExAcquireSpinLockShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
loc_003E30E8:
    goto loc_003E2DEE;
loc_003E30F0:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528) + 200, 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_003E30E8;
loc_003E30F7:
    result = MiRescanPagefileBitmaps(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528), 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_r14)));
    goto loc_003E2E9B;
loc_003E310A:
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528), 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xFFFFFFFFULL));
    goto loc_003E2F5A;
loc_003E3114:
    if (((unsigned int)(result)) < 32) goto loc_003E301D;
    if (((unsigned int)(result)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 52))))) goto loc_003E2F1C;
    goto loc_003E301D;
loc_003E312E:
    result = MiReleaseSpinLockExclusive((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 52)), 17, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xFFFFFFFFULL));
    goto loc_003E2FEA;
loc_003E3138:
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) == 0) goto loc_003E314C;
    if (*(unsigned __int64 *)(result) != 0) goto loc_003E31E5;
loc_003E314C:
    a2 = 0;
    if (*(unsigned __int64 *)(result) == 0) goto loc_003E2EFD;
loc_003E3157:
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p10))))) < (*(unsigned int *)(*(unsigned __int64 *)(result) + 52))) goto loc_003E316D;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p10))))) > (*(unsigned int *)(*(unsigned __int64 *)(result) + 52))) goto loc_003E31ED;
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + 48)) <= 0) goto loc_003E3230;
loc_003E316D:
loc_003E3170:
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) == 0) goto loc_003E317A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result)) != 0) goto loc_003E31F6;
loc_003E317A:
loc_003E317D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result)) != 0) goto loc_003E3157;
    goto loc_003E2EF6;
loc_003E3187:
    v_r14 = 0;
    goto loc_003E2D31;
loc_003E318F:
    if ((*(unsigned __int64 *)(result + 8)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(result)))) goto loc_003E3097;
loc_003E319C:
    v_r15 = (*(unsigned __int64 *)(result + 16)) & (-4);
    if (condition_is_equal) goto loc_003E3097;
    goto loc_003E318F;
loc_003E31AC:
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 48)));
    result = MiFindFreePageFileSpaceForward(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528), v_stack_p18, 0, (unsigned int)((unsigned int)(v_r13)));
    goto loc_003E2F88;
loc_003E31CB:
    if (result == 0) goto loc_003E31D8;
    result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528));
    goto loc_003E2EB4;
loc_003E31D8:
    goto loc_003E2EB4;
loc_003E31DD:
    result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528));
    goto loc_003E2EC0;
loc_003E31E5:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 18536) + result * 8 + 18528)) ^ (result);
    goto loc_003E314C;
loc_003E31ED:
    goto loc_003E3170;
loc_003E31F6:
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 8));
    goto loc_003E317D;
loc_003E31FB:
    if (((*(unsigned __int8 *)(a1)) & (16)) != 0) goto loc_003E2D5C;
loc_003E3209:
    goto loc_003E2D65;
loc_003E3217:
    result = MiPageFileLargestBitmapsRun((unsigned int)((unsigned int)(result)), v_stack_p18, 0, (unsigned int)((unsigned int)(v_r13)));
    if (((unsigned int)(result)) <= 0) goto loc_003E2D6E;
loc_003E3230:
    goto loc_003E316D;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindFreePageFileSpace(void *Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m3C;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m40 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    if (Arg3 >= ((uint32_t)(0xFFFFFFFFULL))) goto loc_003E2F5A;
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) == 0) goto loc_003E2D7E;
loc_003E2D0B:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x4860) + 0xAC)) & (64)) != 0) goto loc_003E3187;
    result = MiPageFileLargestBitmapsRun(*(uint64_t *)(arg1 + 0x4860), Arg2, Arg3, Arg4);
loc_003E2D31:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4858)))) <= 1) goto loc_003E2D78;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4858))) - 1);
loc_003E2D41:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x4860) + 0xAC))) & (16)) != 0) goto loc_003E31FB;
loc_003E2D5C:
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x4860) + 0xAC))) & (32)) != 0) goto loc_003E3209;
loc_003E2D65:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x4868) + 0xAC)) & (48)) == 0) goto loc_003E3217;
loc_003E2D6E:
    local_r12 = (Arg1 + 18536) + (8);
    local_r15 = (local_r15) - (1);
    if (condition_is_not_equal) goto loc_003E2D41;
loc_003E2D78:
    goto loc_003E2DCA;
loc_003E2D7E:
    result = MI_READ_PTE_LOCK_FREE(local_r15, *(uint16_t *)(*(uint64_t *)(arg1 + 0x4860) + 0xAC), Arg3, Arg4);
    result = (result) >> (12);
    result = (uint32_t)((result) & (15));
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (101));
    if (((uint8_t)(result)) == 1) goto loc_003E30AD;
loc_003E2DA2:
    if (*(uint64_t *)(v_rip + 0xA4AED7) == 0) goto loc_003E2DBC;
    result = *(uint64_t *)(v_rip + 0xA4AED7);
    local_rbx = *(uint64_t *)(local_r15);
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA4AED7));
        local_rbx = (*(uint64_t *)(local_r15)) & (result);
    }
    local_rbx = (local_rbx) >> (32);
loc_003E2DC0:
    if ((((uint8_t)((uint32_t)(Arg4))) & (16)) != 0) goto loc_003E2D0B;
loc_003E2DCA:
    result = 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (4));
    v_stack_p18 = (uint32_t)(Arg2);
loc_003E2DDC:
    local_r15 = 0;
    if ((uint32_t)(Arg2) == 0) goto loc_003E2F61;
loc_003E2DEE:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0xAF)) & (1)) != 0) goto loc_003E2F50;
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E2E8E;
    if (((uint32_t)(local_rbx)) >= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x50) + 0x18))) goto loc_003E2F46;
    result = (((uint32_t)(local_rbx)) < (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x50) + 0x18))) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_003E2E71;
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_003E2E71;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x50)) + (24);
    result = RtlLengthCurrentClearRunForward(Arg1, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(v_stack_p18)), (uint32_t)(0xFFFFFFFFULL));
    if (((uint32_t)(result)) != ((uint32_t)(v_stack_p18))) goto loc_003E2E6B;
loc_003E2E4A:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x50)) + (8);
    result = RtlLengthCurrentClearRunForward(Arg1, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(result)), (uint32_t)(0xFFFFFFFFULL));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_p18))) goto loc_003E2E73;
    if ((((uint8_t)((uint32_t)(Arg4))) & (64)) != 0) goto loc_003E2E73;
    goto loc_003E2E71;
loc_003E2E6B:
    if ((((uint8_t)((uint32_t)(Arg4))) & (64)) != 0) goto loc_003E2E4A;
loc_003E2E71:
    local_rdi = 0;
loc_003E2E73:
    if (0 == v_stack_p18) goto loc_003E2F85;
    if ((((uint8_t)((uint32_t)(Arg4))) & (64)) != 0) goto loc_003E2F85;
loc_003E2E8E:
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) != 0) goto loc_003E31AC;
loc_003E2E9B:
    v_stack_m3C = (uint32_t)(v_stack_p18);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70 + 0x8)) & (1)) != 0) goto loc_003E31CB;
loc_003E2EB4:
    Arg3 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70 + 0x8)) & (1));
    local_r15 = 0;
loc_003E2EC0:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) == 0) goto loc_003E2EFD;
    if (((uint32_t)(v_stack_p18)) < (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) + 0x34))) goto loc_003E2EEE;
    if (((uint32_t)(v_stack_p18)) <= (*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) + 0x34))) goto loc_003E2EE4;
loc_003E2ED1:
    if ((uint32_t)(Arg3) == 0) goto loc_003E2EDF;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) + 0x8) != 0) goto loc_003E31DD;
loc_003E2EDF:
    goto loc_003E2EC0;
loc_003E2EE4:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) + 0x8) + 0x30)) <= 0) goto loc_003E3138;
loc_003E2EEE:
    goto loc_003E2ED1;
loc_003E2EF6:
    local_r15 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x70) + 0x8);
    if ((uint32_t)((uint32_t)(local_rbx)) != 0) { local_r15 = (uint32_t)((uint32_t)(local_rbx)); }
loc_003E2EFD:
    if ((*(uint32_t *)(local_r15 + 0x34)) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_003E3020;
    if (((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x6C))) < v_stack_p18) goto loc_003E306F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x6C)))) < 32) goto loc_003E306F;
loc_003E2F1C:
    if ((uint32_t)((uint32_t)(v_stack_m78)) == 0) goto loc_003E30F7;
    result = MiReleaseSpinLockShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, Arg3, (uint32_t)(0xFFFFFFFFULL));
    goto loc_003E2DDC;
loc_003E2F46:
    if ((((uint8_t)((uint32_t)(Arg4))) & (72)) == 0) goto loc_003E2E8E;
loc_003E2F50:
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) goto loc_003E30C9;
loc_003E2F5A:
    result = 0;
    goto loc_003E3004;
loc_003E2F61:
    if ((((uint8_t)((uint32_t)(Arg4))) & (3)) == 0) goto loc_003E304A;
loc_003E2F6F:
    if (((uint8_t)(v_cr8)) != 2) goto loc_003E30F0;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, v_cr8, Arg3, (uint32_t)(0xFFFFFFFFULL));
    goto loc_003E2DEE;
loc_003E2F85:
    v_stack_p18 = (uint32_t)(local_rbx);
loc_003E2F88:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200) == 0) goto loc_003E2F50;
    local_r14 = 0;
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x50);
        Arg3 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200);
        Arg1 = (Arg1) + (24);
        Arg2 = (uint32_t)(local_rbx);
        local_r14 = 2;
        result = RtlSetBits(Arg1, Arg2, Arg3, (uint32_t)(0xFFFFFFFFULL));
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x14);
        local_rbx = v_stack_p18;
        result = (uint32_t)((result) - ((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200)));
        *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x14) = (uint32_t)(result);
    }
    if ((((uint8_t)((uint32_t)(Arg4))) & (2)) != 0) {
        local_r14 = (uint32_t)((local_r14) | (1));
        Arg3 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860);
        result = MiSetPageFileAllocationBits(Arg1, Arg2, Arg3, (uint32_t)(0xFFFFFFFFULL));
    }
    if ((uint32_t)(local_r14) != 0) {
        Arg4 = local_r15;
        Arg3 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860);
        result = MiInvalidatePageFileBitmapsCache(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) goto loc_003E302F;
loc_003E2FEA:
    result = MiTransferSoftwarePte(*(uint64_t *)(v_stack_p10), *(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    *(uint64_t *)(v_stack_p10) = result;
loc_003E3004:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200));
loc_003E301D:
loc_003E3020:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x30)));
    goto loc_003E2F88;
loc_003E302F:
    if (v_stack_m78 == 0) goto loc_003E312E;
    result = MiReleaseSpinLockShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_003E2FEA;
loc_003E304A:
    if ((uint32_t)(result) != 0) goto loc_003E2F6F;
    v_stack_m78 = 1;
    if (17 != 2) goto loc_003E30E3;
    result = ExAcquireSpinLockSharedAtDpcLevel(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_003E2DEE;
loc_003E306F:
    if (sign_flag) goto loc_003E2F50;
    if (*(uint64_t *)(local_r15) == 0) goto loc_003E319C;
    goto loc_003E308D;
loc_003E3089:
loc_003E308D:
    if ((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8)) != 0) goto loc_003E3089;
loc_003E3097:
    if (*(uint64_t *)(local_r15 + 0x8) != 0) goto loc_003E3114;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 0x6C)))) >= 32) goto loc_003E2F1C;
    goto loc_003E2F50;
loc_003E30AD:
    result = MiPageFileLargestBitmapsRun(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860), 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    if (((uint32_t)((uint32_t)(result))) >= ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p10))))) goto loc_003E2DA2;
    local_r13 = (uint32_t)(((uint32_t)(Arg4)) | (16));
    goto loc_003E2DC0;
loc_003E30C9:
    if (v_stack_m78 == 0) goto loc_003E310A;
    result = MiReleaseSpinLockShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_003E2F5A;
loc_003E30E3:
    result = ExAcquireSpinLockShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
loc_003E30E8:
    goto loc_003E2DEE;
loc_003E30F0:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860) + 200, 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_003E30E8;
loc_003E30F7:
    result = MiRescanPagefileBitmaps(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860), 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_r14)));
    goto loc_003E2E9B;
loc_003E310A:
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860), 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xFFFFFFFFULL));
    goto loc_003E2F5A;
loc_003E3114:
    if (((uint32_t)(result)) < 32) goto loc_003E301D;
    if (((uint32_t)(result)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x34))))) goto loc_003E2F1C;
    goto loc_003E301D;
loc_003E312E:
    result = MiReleaseSpinLockExclusive((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x34)), 17, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xFFFFFFFFULL));
    goto loc_003E2FEA;
loc_003E3138:
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) == 0) goto loc_003E314C;
    if (*(uint64_t *)(result) != 0) goto loc_003E31E5;
loc_003E314C:
    Arg2 = 0;
    if (*(uint64_t *)(result) == 0) goto loc_003E2EFD;
loc_003E3157:
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p10))))) < (*(uint32_t *)(*(uint64_t *)(result) + 0x34))) goto loc_003E316D;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p10))))) > (*(uint32_t *)(*(uint64_t *)(result) + 0x34))) goto loc_003E31ED;
    if ((*(uint32_t *)(*(uint64_t *)(result) + 0x30)) <= 0) goto loc_003E3230;
loc_003E316D:
loc_003E3170:
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) == 0) goto loc_003E317A;
    if (*(uint64_t *)(*(uint64_t *)(result)) != 0) goto loc_003E31F6;
loc_003E317A:
loc_003E317D:
    if (*(uint64_t *)(*(uint64_t *)(result)) != 0) goto loc_003E3157;
    goto loc_003E2EF6;
loc_003E3187:
    local_r14 = 0;
    goto loc_003E2D31;
loc_003E318F:
    if ((*(uint64_t *)(result + 0x8)) == (*(uint64_t *)(*(uint64_t *)(result)))) goto loc_003E3097;
loc_003E319C:
    local_r15 = (*(uint64_t *)(result + 0x10)) & (-4);
    if (condition_is_equal) goto loc_003E3097;
    goto loc_003E318F;
loc_003E31AC:
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x30)));
    result = MiFindFreePageFileSpaceForward(*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860), v_stack_p18, 0, (uint32_t)((uint32_t)(local_r13)));
    goto loc_003E2F88;
loc_003E31CB:
    if (result == 0) goto loc_003E31D8;
    result = (result) ^ (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860));
    goto loc_003E2EB4;
loc_003E31D8:
    goto loc_003E2EB4;
loc_003E31DD:
    result = (result) ^ (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860));
    goto loc_003E2EC0;
loc_003E31E5:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x4868) + result * 8 + 0x4860)) ^ (result);
    goto loc_003E314C;
loc_003E31ED:
    goto loc_003E3170;
loc_003E31F6:
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x8));
    goto loc_003E317D;
loc_003E31FB:
    if (((*(uint8_t *)(arg1)) & (16)) != 0) goto loc_003E2D5C;
loc_003E3209:
    goto loc_003E2D65;
loc_003E3217:
    result = MiPageFileLargestBitmapsRun((uint32_t)((uint32_t)(result)), v_stack_p18, 0, (uint32_t)((uint32_t)(local_r13)));
    if (((uint32_t)(result)) <= 0) goto loc_003E2D6E;
loc_003E3230:
    goto loc_003E316D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4858` | `32` | `R` |
| `Arg1` | `+ 0x4860` | `64` | `R` |
| `Arg1` | `+ 0x4860 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x4868` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E2CAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
