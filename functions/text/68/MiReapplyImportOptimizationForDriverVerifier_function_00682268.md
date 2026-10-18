# MiReapplyImportOptimizationForDriverVerifier

- RVA: `0x00682268`–`0x00682710` (길이 `1,192` bytes)
- VA: `0x0000000140682268`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D8380`
- 디코드: `313`개 명령, `1,192/1,192` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0068229C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006822B0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006822CC` → [MiInitializeDriverPatchState](../../page/AB/MiInitializeDriverPatchState_function_00AB07A4.md) (function, `0x00AB07A4`)
- `0x006822D9` → [MmHasImageBeenImportOptimized](../../page/70/MmHasImageBeenImportOptimized_function_00704CD8.md) (function, `0x00704CD8`)
- `0x00682318` → [MiEnumerateBasePatches](../../pagelk/B7/MiEnumerateBasePatches_function_00B74B38.md) (function, `0x00B74B38`)
- `0x00682338` → [RtlImageDirectoryEntryToData](../43/RtlImageDirectoryEntryToData_function_004328D0.md) (function, `0x004328D0`)
- `0x0068234D` → [MiSectionControlArea](../29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x0068238D` → [MiLockAndMapEntireDriver](../../page/80/MiLockAndMapEntireDriver_function_008015C8.md) (function, `0x008015C8`)
- `0x006823C6` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x006823E9` → [MiCheckVerifierFunctionsCfgState](../../page/80/MiCheckVerifierFunctionsCfgState_function_0080C918.md) (function, `0x0080C918`)
- `0x00682401` → [VslReapplyImportOptimizationForDriverVerifier](../../page/71/VslReapplyImportOptimizationForDriverVerifier_function_00719BD4.md) (function, `0x00719BD4`)
- `0x006824A9` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x0068253A` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00682651` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0068265B` → [KeQueryActiveProcessorCountEx](../24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00682674` → [KeIpiGenericCall](../47/KeIpiGenericCall_function_00471720.md) (function, `0x00471720`)
- `0x0068268C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x006826A2` → [MiUnlockEntireDriver](../../page/80/MiUnlockEntireDriver_function_00801780.md) (function, `0x00801780`)
- `0x006826D3` → [MiUnlockAndFreeDvPatchImage](MiUnlockAndFreeDvPatchImage_function_00682A78.md) (function, `0x00682A78`)
- `0x006826ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MmApplyVerifierToRunningImage](../../pagevrfy/BB/MmApplyVerifierToRunningImage_function_00BB4780.md) at `0x00BB47BC`

### Static image references
- `0x00682311` → RVA `0x00682050` (`MiLockPatchIatForDV`; read)
- `0x006823D6` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00682587` → RVA `0x00FC6B48` (`ALMOSTRO`; read)
- `0x0068259A` → RVA `0x004CDA40` (`MiIsTargetFullyRetpolined`; read)
- `0x00682615` → RVA `0x00E2D860` (`.data`; read)
- `0x00682645` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00682669` → RVA `0x00682720` (`MiReapplyImportOptimizationWorker`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x006822CC` → [MiInitializeDriverPatchState](../../page/AB/MiInitializeDriverPatchState_function_00AB07A4.md) (`.text` → `PAGE`)
  - `0x006822D9` → [MmHasImageBeenImportOptimized](../../page/70/MmHasImageBeenImportOptimized_function_00704CD8.md) (`.text` → `PAGE`)
  - `0x00682318` → [MiEnumerateBasePatches](../../pagelk/B7/MiEnumerateBasePatches_function_00B74B38.md) (`.text` → `PAGELK`)
  - `0x0068238D` → [MiLockAndMapEntireDriver](../../page/80/MiLockAndMapEntireDriver_function_008015C8.md) (`.text` → `PAGE`)
  - `0x006823E9` → [MiCheckVerifierFunctionsCfgState](../../page/80/MiCheckVerifierFunctionsCfgState_function_0080C918.md) (`.text` → `PAGE`)
  - `0x00682401` → [VslReapplyImportOptimizationForDriverVerifier](../../page/71/VslReapplyImportOptimizationForDriverVerifier_function_00719BD4.md) (`.text` → `PAGE`)
  - `0x006826A2` → [MiUnlockEntireDriver](../../page/80/MiUnlockEntireDriver_function_00801780.md) (`.text` → `PAGE`)
  - `0x006826ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00682268  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0068226D  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00682272  55                              push rbp
00682273  56                              push rsi
00682274  57                              push rdi
00682275  41 54                           push r12
00682277  41 55                           push r13
00682279  41 56                           push r14
0068227B  41 57                           push r15
0068227D  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00682282  48 81 EC 00 01 00 00            sub rsp, 0x100
00682289  48 8B F2                        mov rsi, rdx
0068228C  45 8B F8                        mov r15d, r8d
0068228F  33 D2                           xor edx, edx
00682291  48 8B F9                        mov rdi, rcx
00682294  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00682298  44 8D 42 68                     lea r8d, [rdx + 0x68]
0068229C  E8 9F 49 04 00                  call 0x1406c6c40
006822A1  83 65 67 00                     and dword ptr [rbp + 0x67], 0
006822A5  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
006822AA  33 D2                           xor edx, edx
006822AC  44 8D 42 50                     lea r8d, [rdx + 0x50]
006822B0  E8 8B 49 04 00                  call 0x1406c6c40
006822B5  48 8D 45 8F                     lea rax, [rbp - 0x71]
006822B9  48 8B CF                        mov rcx, rdi
006822BC  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
006822C0  48 8D 55 B7                     lea rdx, [rbp - 0x49]
006822C4  48 8D 45 8F                     lea rax, [rbp - 0x71]
006822C8  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
006822CC  E8 D3 E4 42 00                  call 0x140ab07a4
006822D1  48 8B CF                        mov rcx, rdi
006822D4  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
006822D9  E8 FA 29 08 00                  call 0x140704cd8
006822DE  85 C0                           test eax, eax
006822E0  75 0A                           jne 0x1406822ec
006822E2  BB 84 01 00 C0                  mov ebx, 0xc0000184
006822E7  E9 AD 03 00 00                  jmp 0x140682699
006822EC  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
006822F2  84 C0                           test al, al
006822F4  79 0A                           jns 0x140682300
006822F6  BB BB 00 00 C0                  mov ebx, 0xc00000bb
006822FB  E9 99 03 00 00                  jmp 0x140682699
00682300  48 8D 87 00 01 00 00            lea rax, [rdi + 0x100]
00682307  48 39 00                        cmp qword ptr [rax], rax
0068230A  74 1C                           je 0x140682328
0068230C  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00682311  48 8D 15 38 FD FF FF            lea rdx, [rip - 0x2c8]
00682318  E8 1B 28 4F 00                  call 0x140b74b38
0068231D  8B 5D 9F                        mov ebx, dword ptr [rbp - 0x61]
00682320  85 DB                           test ebx, ebx
00682322  0F 88 71 03 00 00               js 0x140682699
00682328  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0068232C  4C 8D 4D 7F                     lea r9, [rbp + 0x7f]
00682330  41 B8 0C 00 00 00               mov r8d, 0xc
00682336  B2 01                           mov dl, 1
00682338  E8 93 05 DB FF                  call 0x1404328d0
0068233D  48 8B 4F 70                     mov rcx, qword ptr [rdi + 0x70]
00682341  45 33 ED                        xor r13d, r13d
00682344  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00682348  48 85 C9                        test rcx, rcx
0068234B  74 1C                           je 0x140682369
0068234D  E8 5E 29 C1 FF                  call 0x140294cb0
00682352  48 8B 48 60                     mov rcx, qword ptr [rax + 0x60]
00682356  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
0068235A  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
0068235E  48 85 D2                        test rdx, rdx
00682361  74 0D                           je 0x140682370
00682363  4C 8B 6A 58                     mov r13, qword ptr [rdx + 0x58]
00682367  EB 07                           jmp 0x140682370
00682369  4C 8B AF 18 01 00 00            mov r13, qword ptr [rdi + 0x118]
00682370  44 8B 77 40                     mov r14d, dword ptr [rdi + 0x40]
00682374  41 C1 EE 0C                     shr r14d, 0xc
00682378  4D 85 ED                        test r13, r13
0068237B  0F 84 75 FF FF FF               je 0x1406822f6
00682381  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00682386  48 8B CF                        mov rcx, rdi
00682389  48 8D 55 B7                     lea rdx, [rbp - 0x49]
0068238D  E8 36 F2 17 00                  call 0x1408015c8
00682392  8B D8                           mov ebx, eax
00682394  85 C0                           test eax, eax
00682396  0F 88 FD 02 00 00               js 0x140682699
0068239C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006823A1  F6 41 0A 05                     test byte ptr [rcx + 0xa], 5
006823A5  74 06                           je 0x1406823ad
006823A7  4C 8B 61 18                     mov r12, qword ptr [rcx + 0x18]
006823AB  EB 21                           jmp 0x1406823ce
006823AD  45 33 C9                        xor r9d, r9d
006823B0  C7 44 24 28 20 00 00 00         mov dword ptr [rsp + 0x28], 0x20
006823B8  33 D2                           xor edx, edx
006823BA  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
006823C2  45 8D 41 01                     lea r8d, [r9 + 1]
006823C6  E8 35 64 C9 FF                  call 0x140318800
006823CB  4C 8B E0                        mov r12, rax
006823CE  4C 2B 67 30                     sub r12, qword ptr [rdi + 0x30]
006823D2  4C 03 65 A7                     add r12, qword ptr [rbp - 0x59]
006823D6  48 F7 05 A7 46 94 00 00 80 00 00  test qword ptr [rip + 0x9446a7], 0x8000
006823E1  74 53                           je 0x140682436
006823E3  41 8B D7                        mov edx, r15d
006823E6  48 8B CE                        mov rcx, rsi
006823E9  E8 2A A5 18 00                  call 0x14080c918
006823EE  8B D8                           mov ebx, eax
006823F0  85 C0                           test eax, eax
006823F2  0F 88 A1 02 00 00               js 0x140682699
006823F8  45 8B C7                        mov r8d, r15d
006823FB  48 8B D6                        mov rdx, rsi
006823FE  48 8B CF                        mov rcx, rdi
00682401  E8 CE 77 09 00                  call 0x140719bd4
00682406  8B D8                           mov ebx, eax
00682408  85 C0                           test eax, eax
0068240A  0F 88 89 02 00 00               js 0x140682699
00682410  45 85 FF                        test r15d, r15d
00682413  0F 84 80 02 00 00               je 0x140682699
00682419  49 8B D7                        mov rdx, r15
0068241C  48 63 0E                        movsxd rcx, dword ptr [rsi]
0068241F  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00682423  48 8D 76 18                     lea rsi, [rsi + 0x18]
00682427  49 89 04 CC                     mov qword ptr [r12 + rcx*8], rax
0068242B  48 83 EA 01                     sub rdx, 1
0068242F  75 EB                           jne 0x14068241c
00682431  E9 63 02 00 00                  jmp 0x140682699
00682436  46 8D 14 F5 40 00 00 00         lea r10d, [r14*8 + 0x40]
0068243E  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
00682443  45 85 F6                        test r14d, r14d
00682446  74 42                           je 0x14068248a
00682448  44 8B 7D 67                     mov r15d, dword ptr [rbp + 0x67]
0068244C  49 8D 55 40                     lea rdx, [r13 + 0x40]
00682450  45 8B CE                        mov r9d, r14d
00682453  4C 8B 02                        mov r8, qword ptr [rdx]
00682456  4D 85 C0                        test r8, r8
00682459  74 1D                           je 0x140682478
0068245B  41 0F B7 48 04                  movzx ecx, word ptr [r8 + 4]
00682460  41 0F B7 40 02                  movzx eax, word ptr [r8 + 2]
00682465  D1 E8                           shr eax, 1
00682467  D1 E9                           shr ecx, 1
00682469  03 C8                           add ecx, eax
0068246B  41 0F B7 00                     movzx eax, word ptr [r8]
0068246F  C1 E8 02                        shr eax, 2
00682472  44 03 F8                        add r15d, eax
00682475  44 03 F9                        add r15d, ecx
00682478  48 83 C2 08                     add rdx, 8
0068247C  49 83 E9 01                     sub r9, 1
00682480  75 D1                           jne 0x140682453
00682482  44 89 7D 67                     mov dword ptr [rbp + 0x67], r15d
00682486  44 8B 7D 77                     mov r15d, dword ptr [rbp + 0x77]
0068248A  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
0068248D  BB 40 00 00 00                  mov ebx, 0x40
00682492  41 B8 4D 6D 76 66               mov r8d, 0x66766d4d
00682498  48 89 5D 7F                     mov qword ptr [rbp + 0x7f], rbx
0068249C  42 8D 0C 70                     lea ecx, [rax + r14*2]
006824A0  41 03 CE                        add ecx, r14d
006824A3  41 8D 14 8A                     lea edx, [r10 + rcx*4]
006824A7  8B CB                           mov ecx, ebx
006824A9  E8 92 90 CD FF                  call 0x14035b540
006824AE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
006824B3  48 85 C0                        test rax, rax
006824B6  75 0A                           jne 0x1406824c2
006824B8  BB 9A 00 00 C0                  mov ebx, 0xc000009a
006824BD  E9 D7 01 00 00                  jmp 0x140682699
006824C2  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
006824C7  83 65 67 00                     and dword ptr [rbp + 0x67], 0
006824CB  42 8D 0C F5 40 00 00 00         lea ecx, [r14*8 + 0x40]
006824D3  0F 11 00                        movups xmmword ptr [rax], xmm0
006824D6  41 0F 10 4D 10                  movups xmm1, xmmword ptr [r13 + 0x10]
006824DB  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
006824DF  41 0F 10 45 20                  movups xmm0, xmmword ptr [r13 + 0x20]
006824E4  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
006824E8  F2 41 0F 10 4D 30               movsd xmm1, qword ptr [r13 + 0x30]
006824EE  F2 0F 11 48 30                  movsd qword ptr [rax + 0x30], xmm1
006824F3  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
006824F8  48 03 C8                        add rcx, rax
006824FB  48 89 48 38                     mov qword ptr [rax + 0x38], rcx
006824FF  45 85 F6                        test r14d, r14d
00682502  74 54                           je 0x140682558
00682504  44 8B 7D 67                     mov r15d, dword ptr [rbp + 0x67]
00682508  4A 8B 14 2B                     mov rdx, qword ptr [rbx + r13]
0068250C  48 85 D2                        test rdx, rdx
0068250F  74 35                           je 0x140682546
00682511  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
00682515  0F B7 4A 04                     movzx ecx, word ptr [rdx + 4]
00682519  83 C0 0C                        add eax, 0xc
0068251C  0F B7 1A                        movzx ebx, word ptr [rdx]
0068251F  03 C8                           add ecx, eax
00682521  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00682526  03 D9                           add ebx, ecx
00682528  4C 8B 45 7F                     mov r8, qword ptr [rbp + 0x7f]
0068252C  41 8B CF                        mov ecx, r15d
0068252F  48 03 48 38                     add rcx, qword ptr [rax + 0x38]
00682533  49 89 0C 00                     mov qword ptr [r8 + rax], rcx
00682537  44 8B C3                        mov r8d, ebx
0068253A  E8 01 43 04 00                  call 0x1406c6840
0068253F  44 03 FB                        add r15d, ebx
00682542  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
00682546  48 83 C3 08                     add rbx, 8
0068254A  48 89 5D 7F                     mov qword ptr [rbp + 0x7f], rbx
0068254E  49 83 EE 01                     sub r14, 1
00682552  75 B4                           jne 0x140682508
00682554  44 8B 7D 77                     mov r15d, dword ptr [rbp + 0x77]
00682558  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0068255D  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00682561  2B 4F 30                        sub ecx, dword ptr [rdi + 0x30]
00682564  89 48 04                        mov dword ptr [rax + 4], ecx
00682567  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0068256C  4C 89 60 18                     mov qword ptr [rax + 0x18], r12
00682570  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00682575  48 83 60 10 00                  and qword ptr [rax + 0x10], 0
0068257A  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0068257F  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00682583  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
00682587  48 8B 05 BA 45 94 00            mov rax, qword ptr [rip + 0x9445ba]
0068258E  48 0F BA E0 29                  bt rax, 0x29
00682593  73 10                           jae 0x1406825a5
00682595  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0068259A  48 8D 0D 9F B4 E4 FF            lea rcx, [rip - 0x1b4b61]
006825A1  48 89 48 28                     mov qword ptr [rax + 0x28], rcx
006825A5  43 8D 04 7F                     lea eax, [r15 + r15*2]
006825A9  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
006825AE  C1 E0 03                        shl eax, 3
006825B1  89 45 87                        mov dword ptr [rbp - 0x79], eax
006825B4  4D 8B 45 10                     mov r8, qword ptr [r13 + 0x10]
006825B8  45 85 FF                        test r15d, r15d
006825BB  74 7B                           je 0x140682638
006825BD  45 8B CF                        mov r9d, r15d
006825C0  4D 85 C0                        test r8, r8
006825C3  74 69                           je 0x14068262e
006825C5  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
006825C9  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
006825CD  48 3B D1                        cmp rdx, rcx
006825D0  76 05                           jbe 0x1406825d7
006825D2  48 2B D1                        sub rdx, rcx
006825D5  EB 0A                           jmp 0x1406825e1
006825D7  8B 47 40                        mov eax, dword ptr [rdi + 0x40]
006825DA  48 2B C2                        sub rax, rdx
006825DD  48 8D 14 01                     lea rdx, [rcx + rax]
006825E1  48 63 0E                        movsxd rcx, dword ptr [rsi]
006825E4  33 C0                           xor eax, eax
006825E6  41 BA 00 00 00 80               mov r10d, 0x80000000
006825EC  49 3B D2                        cmp rdx, r10
006825EF  0F 46 C2                        cmovbe eax, edx
006825F2  41 89 04 88                     mov dword ptr [r8 + rcx*4], eax
006825F6  48 8B 05 4B 45 94 00            mov rax, qword ptr [rip + 0x94454b]
006825FD  48 0F BA E0 29                  bt rax, 0x29
00682602  73 2A                           jae 0x14068262e
00682604  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
00682608  48 B8 00 00 00 00 00 80 00 00   movabs rax, 0x800000000000
00682612  48 03 C8                        add rcx, rax
00682615  48 8B 05 44 B2 7A 00            mov rax, qword ptr [rip + 0x7ab244]
0068261C  48 C1 E9 10                     shr rcx, 0x10
00682620  48 0F A3 08                     bt qword ptr [rax], rcx
00682624  72 08                           jb 0x14068262e
00682626  48 63 06                        movsxd rax, dword ptr [rsi]
00682629  41 83 24 80 00                  and dword ptr [r8 + rax*4], 0
0068262E  48 83 C6 18                     add rsi, 0x18
00682632  49 83 E9 01                     sub r9, 1
00682636  75 88                           jne 0x1406825c0
00682638  44 0F 20 C7                     mov rdi, cr8
0068263C  BA 0C 00 00 00                  mov edx, 0xc
00682641  44 0F 22 C2                     mov cr8, rdx
00682645  83 3D D4 46 94 00 00            cmp dword ptr [rip + 0x9446d4], 0
0068264C  74 08                           je 0x140682656
0068264E  40 8A CF                        mov cl, dil
00682651  E8 A6 30 E7 FF                  call 0x1404f56fc
00682656  B9 FF FF 00 00                  mov ecx, 0xffff
0068265B  E8 90 78 BC FF                  call 0x140249ef0
00682660  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00682665  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00682669  48 8D 0D B0 00 00 00            lea rcx, [rip + 0xb0]
00682670  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00682674  E8 A7 F0 DE FF                  call 0x140471720
00682679  83 3D A0 46 94 00 00            cmp dword ptr [rip + 0x9446a0], 0
00682680  48 8B D8                        mov rbx, rax
00682683  74 0C                           je 0x140682691
00682685  44 0F 20 C1                     mov rcx, cr8
00682689  40 8A D7                        mov dl, dil
0068268C  E8 07 30 E7 FF                  call 0x1404f5698
00682691  40 0F B6 CF                     movzx ecx, dil
00682695  44 0F 22 C1                     mov cr8, rcx
00682699  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0068269E  48 8D 4D B7                     lea rcx, [rbp - 0x49]
006826A2  E8 D9 F0 17 00                  call 0x140801780
006826A7  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
006826AB  48 8D 45 8F                     lea rax, [rbp - 0x71]
006826AF  48 3B C8                        cmp rcx, rax
006826B2  74 2D                           je 0x1406826e1
006826B4  48 8D 45 8F                     lea rax, [rbp - 0x71]
006826B8  48 39 41 08                     cmp qword ptr [rcx + 8], rax
006826BC  75 1C                           jne 0x1406826da
006826BE  48 8B 01                        mov rax, qword ptr [rcx]
006826C1  48 39 48 08                     cmp qword ptr [rax + 8], rcx
006826C5  75 13                           jne 0x1406826da
006826C7  48 8D 55 8F                     lea rdx, [rbp - 0x71]
006826CB  48 89 45 8F                     mov qword ptr [rbp - 0x71], rax
006826CF  48 89 50 08                     mov qword ptr [rax + 8], rdx
006826D3  E8 A0 03 00 00                  call 0x140682a78
006826D8  EB CD                           jmp 0x1406826a7
006826DA  B9 03 00 00 00                  mov ecx, 3
006826DF  CD 29                           int 0x29
006826E1  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
006826E6  48 85 C9                        test rcx, rcx
006826E9  74 07                           je 0x1406826f2
006826EB  33 D2                           xor edx, edx
006826ED  E8 7E 01 50 00                  call 0x140b82870
006826F2  8B C3                           mov eax, ebx
006826F4  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
006826FC  48 81 C4 00 01 00 00            add rsp, 0x100
00682703  41 5F                           pop r15
00682705  41 5E                           pop r14
00682707  41 5D                           pop r13
00682709  41 5C                           pop r12
0068270B  5F                              pop rdi
0068270C  5E                              pop rsi
0068270D  5D                              pop rbp
0068270E  C3                              ret
0068270F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReapplyImportOptimizationForDriverVerifier(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m104;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (256);
    a2 = 0;
    result = memset(v_stack_mA8, a2, a2 + 104, a4);
    a2 = 0;
    result = memset(v_stack_m108, a2, a2 + 80, a4);
    v_stack_mC8 = v_stack_mD0;
    v_stack_mD0 = v_stack_mD0;
    result = MiInitializeDriverPatchState(a1, v_stack_mA8, a2 + 80, a4);
    v_stack_mF8 = a1;
    result = MmHasImageBeenImportOptimized(a1, v_stack_mA8, a2 + 80, a4);
    if ((unsigned int)(result) != 0) goto loc_006822EC;
    goto loc_00682699;
loc_006822EC:
    if (!sign_flag) goto loc_00682300;
loc_006822F6:
    goto loc_00682699;
loc_00682300:
    if ((*(unsigned __int64 *)(a1 + 256)) == (a1 + 256)) goto loc_00682328;
    result = MiEnumerateBasePatches(a1, v_rip - 712, v_stack_m108, a4);
    if (sign_flag) goto loc_00682699;
loc_00682328:
    result = RtlImageDirectoryEntryToData(*(unsigned __int64 *)(a1 + 48), 1, 12, v_stack_p20);
    v_r13 = 0;
    v_stack_mB8 = result;
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00682369;
    result = MiSectionControlArea(*(unsigned __int64 *)(a1 + 112), 1, 12, v_stack_p20);
    a1 = (*(unsigned __int64 *)(result + 96)) & (-8);
    if (*(unsigned __int64 *)(a1 + 32) == 0) goto loc_00682370;
    goto loc_00682370;
loc_00682369:
loc_00682370:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) >> (12));
    if (*(unsigned __int64 *)(a1 + 280) == 0) goto loc_006822F6;
    result = MiLockAndMapEntireDriver(a1, v_stack_mA8, v_stack_mF0, v_stack_p20);
    if (sign_flag) goto loc_00682699;
    if (((*(unsigned __int8 *)(v_stack_mF0 + 10)) & (5)) == 0) goto loc_006823AD;
    goto loc_006823CE;
loc_006823AD:
    a4 = 0;
    v_stack_m110 = 32;
    a2 = 0;
    v_stack_m118 = 1;
    result = MmMapLockedPagesSpecifyCache(v_stack_mF0, a2, a4 + 1, a4);
loc_006823CE:
    v_r12 = (result) - (*(unsigned __int64 *)(a1 + 48));
    v_r12 = (v_r12) + (v_stack_mB8);
    if (((*(unsigned __int64 *)(v_rip + 9717415)) & (0x8000ULL)) == 0) goto loc_00682436;
    result = MiCheckVerifierFunctionsCfgState(0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4 + 1, a4);
    if (sign_flag) goto loc_00682699;
    result = VslReapplyImportOptimizationForDriverVerifier(a1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if (sign_flag) goto loc_00682699;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00682699;
loc_0068241C:
    *(unsigned __int64 *)(v_r12 + (int)(*(unsigned int *)(a2)) * 8) = *(unsigned __int64 *)(a2 + 8);
    a2 = ((unsigned int)(a3)) - (1);
    if (condition_is_not_equal) goto loc_0068241C;
    goto loc_00682699;
loc_00682436:
    v_stack_mFC = (unsigned int)(v_r14 * 8 + 64);
    if ((unsigned int)(v_r14) == 0) goto loc_0068248A;
loc_00682453:
    result = *(unsigned __int64 *)(a2 + 8);
    v_r15 = (unsigned int)(v_stack_p8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 64) != 0) {
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 64) + 4);
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 64) + 2);
        result = (unsigned int)((result) >> (1));
        a1 = (unsigned int)((a1) >> (1));
        a1 = (unsigned int)((a1) + ((unsigned int)(result)));
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 64));
        result = (unsigned int)((result) >> (2));
        v_r15 = (unsigned int)(((unsigned int)(v_stack_p8)) + ((unsigned int)(result)));
        v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a1)));
    }
    a2 = (*(unsigned __int64 *)(a1 + 280) + 64) + (8);
    a4 = ((unsigned int)((unsigned int)(v_r14))) - (1);
    if (condition_is_not_equal) goto loc_00682453;
    v_stack_p8 = (unsigned int)(v_r15);
loc_0068248A:
    v_stack_p20 = 64;
    a1 = (unsigned int)(((unsigned int)(v_stack_p8) + v_r14 * 2) + ((unsigned int)(v_r14)));
    result = MiAllocatePool(64, v_r14 * 8 + 64 + a1 * 4, (unsigned int)(0x66766D4DULL), a4);
    v_stack_mE8 = result;
    if (result != 0) goto loc_006824C2;
    goto loc_00682699;
loc_006824C2:
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm1;
    *(unsigned __int64 *)(result + 32) = v_xmm0;
    *(unsigned __int64 *)(result + 48) = v_xmm1;
    a1 = (v_r14 * 8 + 64) + (v_stack_mE8);
    *(unsigned __int64 *)(v_stack_mE8 + 56) = a1;
    if ((unsigned int)(v_r14) == 0) goto loc_00682558;
loc_00682508:
    result = v_stack_mE8;
    v_rbx = (unsigned int)(0xC000009AULL);
    v_r15 = (unsigned int)(v_stack_p8);
    if (*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + *(unsigned __int64 *)(a1 + 280) * 1) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + *(unsigned __int64 *)(a1 + 280) * 1) + 2);
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + *(unsigned __int64 *)(a1 + 280) * 1) + 4);
        result = (unsigned int)((result) + (12));
        v_rbx = *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + *(unsigned __int64 *)(a1 + 280) * 1));
        a1 = (unsigned int)((a1) + ((unsigned int)(result)));
        result = v_stack_mE8;
        v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(a1)));
        a3 = v_stack_p20;
        a1 = (unsigned int)((unsigned int)(v_stack_p8));
        a1 = (a1) + (*(unsigned __int64 *)(result + 56));
        *(unsigned __int64 *)(a3 + result * 1) = a1;
        a3 = (unsigned int)(v_rbx);
        result = memcpy(a1, *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + *(unsigned __int64 *)(a1 + 280) * 1), a3, a4);
        v_r15 = (unsigned int)(((unsigned int)(v_stack_p8)) + ((unsigned int)(v_rbx)));
        v_rbx = v_stack_p20;
    }
    v_rbx = (v_rbx) + (8);
    v_stack_p20 = v_rbx;
    v_r14 = (v_r14) - (1);
    if (condition_is_not_equal) goto loc_00682508;
loc_00682558:
    a1 = (unsigned int)((v_stack_mB8) - (*(unsigned int *)(a1 + 48)));
    *(unsigned int *)(v_stack_mE8 + 4) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_stack_mE8 + 24) = v_r12;
    *(unsigned __int64 *)(v_stack_mE8 + 32) = *(unsigned __int64 *)(a1 + 48);
    result = *(unsigned __int64 *)(v_rip + 9717178);
    if (!(condition_is_above_or_equal)) {
        result = v_stack_mE8;
        a1 = v_rip - 1788769;
        *(unsigned __int64 *)(result + 40) = a1;
    }
    v_stack_mE0 = a2 + 24;
    result = (unsigned int)(((unsigned int)(v_stack_p18) + (unsigned int)(v_stack_p18) * 2) << (3));
    v_stack_mD8 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_00682638;
loc_006825C0:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16) == 0) goto loc_0068262E;
    if ((*(unsigned __int64 *)(a2 + 24 + 8)) <= (*(unsigned __int64 *)(a1 + 48))) goto loc_006825D7;
    a2 = (*(unsigned __int64 *)(a2 + 24 + 8)) - (*(unsigned __int64 *)(a1 + 48));
    goto loc_006825E1;
loc_006825D7:
    result = ((unsigned int)(*(unsigned int *)(a1 + 64))) - (a2);
loc_006825E1:
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 48) + result * 1) <= ((unsigned int)(0x80000000ULL))) { result = (unsigned int)(*(unsigned __int64 *)(a1 + 48) + result * 1); }
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16) + (int)(*(unsigned int *)(a2 + 24)) * 4) = (unsigned int)(result);
    if ((*(unsigned __int64 *)(a1 + 48) + result * 1) >= ((unsigned int)(0x80000000ULL))) goto loc_0068262E;
    a1 = (*(unsigned __int64 *)(a2 + 24 + 8)) + (*(unsigned __int64 *)(v_rip + 9717067));
    a1 = (a1) >> (16);
    result = *(unsigned __int64 *)(v_rip + 8041028);
    if (!(condition_is_below)) {
        result = (int)(*(unsigned int *)(a2 + 24));
    }
    v_rsi = (a2 + 24) + (24);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_006825C0;
loc_00682638:
    if ((*(unsigned int *)(v_rip + 9717460)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 12, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    }
    result = KeQueryActiveProcessorCountEx((unsigned int)(0xFFFFULL), 12, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    v_stack_m104 = (unsigned int)(result);
    v_stack_m108 = (unsigned int)(result);
    result = KeIpiGenericCall(v_rip + 176, v_stack_m108, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    if ((*(unsigned int *)(v_rip + 9717408)) != 0) {
        a1 = 12;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    }
loc_00682699:
    result = MiUnlockEntireDriver(v_stack_mA8, v_stack_mF0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
loc_006826A7:
    if (v_stack_mD0 == v_stack_mD0) goto loc_006826E1;
    if ((*(unsigned __int64 *)(v_stack_mD0 + 8)) != v_stack_mD0) goto loc_006826DA;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0) + 8)) != v_stack_mD0) goto loc_006826DA;
    v_stack_mD0 = *(unsigned __int64 *)(v_stack_mD0);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mD0) + 8) = v_stack_mD0;
    result = MiUnlockAndFreeDvPatchImage(v_stack_mD0, v_stack_mD0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    goto loc_006826A7;
loc_006826DA:
loc_006826E1:
    if (v_stack_mE8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_mE8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 280) + 16), a4);
    }
    v_rsp = (v_rsp) + (256);
    return (unsigned int)((unsigned int)(result));
}
```

## 5. (Beta) C Style

```c
int64_t MiReapplyImportOptimizationForDriverVerifier(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m104;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m5F;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (256);
    Arg2 = 0;
    result = memset(v_stack_mA8, Arg2, Arg2 + 104, a4);
    Arg2 = 0;
    result = memset(v_stack_m108, Arg2, Arg2 + 80, a4);
    v_stack_mC8 = v_stack_mD0;
    v_stack_mD0 = v_stack_mD0;
    result = MiInitializeDriverPatchState(Arg1, v_stack_mA8, Arg2 + 80, a4);
    v_stack_mF8 = Arg1;
    result = MmHasImageBeenImportOptimized(Arg1, v_stack_mA8, Arg2 + 80, a4);
    if ((uint32_t)(result) != 0) goto loc_006822EC;
    goto loc_00682699;
loc_006822EC:
    if (!sign_flag) goto loc_00682300;
loc_006822F6:
    goto loc_00682699;
loc_00682300:
    if ((*(uint64_t *)(arg1 + 0x100)) == (Arg1 + 256)) goto loc_00682328;
    result = MiEnumerateBasePatches(Arg1, v_rip - 712, v_stack_m108, a4);
    if (sign_flag) goto loc_00682699;
loc_00682328:
    result = RtlImageDirectoryEntryToData(*(uint64_t *)(arg1 + 0x30), 1, 12, v_stack_p20);
    local_r13 = 0;
    v_stack_mB8 = result;
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00682369;
    result = MiSectionControlArea(*(uint64_t *)(arg1 + 0x70), 1, 12, v_stack_p20);
    Arg1 = (*(uint64_t *)(result + 0x60)) & (-8);
    if (*(uint64_t *)(arg1 + 0x20) == 0) goto loc_00682370;
    goto loc_00682370;
loc_00682369:
loc_00682370:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (12));
    if (*(uint64_t *)(arg1 + 0x118) == 0) goto loc_006822F6;
    result = MiLockAndMapEntireDriver(Arg1, v_stack_mA8, v_stack_mF0, v_stack_p20);
    if (sign_flag) goto loc_00682699;
    if (((*(uint8_t *)(v_stack_mF0 + 0xA)) & (5)) == 0) goto loc_006823AD;
    goto loc_006823CE;
loc_006823AD:
    a4 = 0;
    v_stack_m110 = 32;
    Arg2 = 0;
    v_stack_m118 = 1;
    result = MmMapLockedPagesSpecifyCache(v_stack_mF0, Arg2, a4 + 1, a4);
loc_006823CE:
    local_r12 = (result) - (*(uint64_t *)(arg1 + 0x30));
    local_r12 = (local_r12) + (v_stack_mB8);
    if (((*(uint64_t *)(v_rip + 0x9446A7)) & (0x8000ULL)) == 0) goto loc_00682436;
    result = MiCheckVerifierFunctionsCfgState(0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4 + 1, a4);
    if (sign_flag) goto loc_00682699;
    result = VslReapplyImportOptimizationForDriverVerifier(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if (sign_flag) goto loc_00682699;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00682699;
loc_0068241C:
    *(uint64_t *)(local_r12 + (int32_t)(*(uint32_t *)(arg2)) * 8) = *(uint64_t *)(arg2 + 0x8);
    Arg2 = ((uint32_t)(Arg3)) - (1);
    if (condition_is_not_equal) goto loc_0068241C;
    goto loc_00682699;
loc_00682436:
    v_stack_mFC = (uint32_t)(local_r14 * 8 + 64);
    if ((uint32_t)(local_r14) == 0) goto loc_0068248A;
loc_00682453:
    result = *(uint64_t *)(arg2 + 0x8);
    local_r15 = (uint32_t)(v_stack_p8);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x40) != 0) {
        Arg1 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x40) + 0x4);
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x40) + 0x2);
        result = (uint32_t)((result) >> (1));
        Arg1 = (uint32_t)((Arg1) >> (1));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x40));
        result = (uint32_t)((result) >> (2));
        local_r15 = (uint32_t)(((uint32_t)(v_stack_p8)) + ((uint32_t)(result)));
        local_r15 = (uint32_t)((local_r15) + ((uint32_t)(Arg1)));
    }
    Arg2 = (*(uint64_t *)(arg1 + 0x118) + 64) + (8);
    a4 = ((uint32_t)((uint32_t)(local_r14))) - (1);
    if (condition_is_not_equal) goto loc_00682453;
    v_stack_p8 = (uint32_t)(local_r15);
loc_0068248A:
    v_stack_p20 = 64;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p8) + local_r14 * 2) + ((uint32_t)(local_r14)));
    result = MiAllocatePool(64, local_r14 * 8 + 64 + Arg1 * 4, (uint32_t)(0x66766D4DULL), a4);
    v_stack_mE8 = result;
    if (result != 0) goto loc_006824C2;
    goto loc_00682699;
loc_006824C2:
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm1;
    *(uint64_t *)(result + 0x20) = v_xmm0;
    *(uint64_t *)(result + 0x30) = v_xmm1;
    Arg1 = (local_r14 * 8 + 64) + (v_stack_mE8);
    *(void **)(v_stack_mE8 + 0x38) = Arg1;
    if ((uint32_t)(local_r14) == 0) goto loc_00682558;
loc_00682508:
    result = v_stack_mE8;
    local_rbx = (uint32_t)(0xC000009AULL);
    local_r15 = (uint32_t)(v_stack_p8);
    if (*(uint64_t *)((uint32_t)(0xC000009AULL) + *(uint64_t *)(arg1 + 0x118) * 1) != 0) {
        result = *(uint16_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + *(uint64_t *)(arg1 + 0x118) * 1) + 0x2);
        Arg1 = *(uint16_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + *(uint64_t *)(arg1 + 0x118) * 1) + 0x4);
        result = (uint32_t)((result) + (12));
        local_rbx = *(uint16_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + *(uint64_t *)(arg1 + 0x118) * 1));
        Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
        result = v_stack_mE8;
        local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(Arg1)));
        Arg3 = v_stack_p20;
        Arg1 = (uint32_t)((uint32_t)(v_stack_p8));
        Arg1 = (Arg1) + (*(uint64_t *)(result + 0x38));
        *(void **)(Arg3 + result * 1) = Arg1;
        Arg3 = (uint32_t)(local_rbx);
        result = memcpy(Arg1, *(uint64_t *)((uint32_t)(0xC000009AULL) + *(uint64_t *)(arg1 + 0x118) * 1), Arg3, a4);
        local_r15 = (uint32_t)(((uint32_t)(v_stack_p8)) + ((uint32_t)(local_rbx)));
        local_rbx = v_stack_p20;
    }
    local_rbx = (local_rbx) + (8);
    v_stack_p20 = local_rbx;
    local_r14 = (local_r14) - (1);
    if (condition_is_not_equal) goto loc_00682508;
loc_00682558:
    Arg1 = (uint32_t)((v_stack_mB8) - (*(uint32_t *)(arg1 + 0x30)));
    *(uint32_t *)(v_stack_mE8 + 0x4) = (uint32_t)(Arg1);
    *(uint64_t *)(v_stack_mE8 + 0x18) = local_r12;
    *(uint64_t *)(v_stack_mE8 + 0x20) = *(uint64_t *)(arg1 + 0x30);
    result = *(uint64_t *)(v_rip + 0x9445BA);
    if (!(condition_is_above_or_equal)) {
        result = v_stack_mE8;
        Arg1 = v_rip - 1788769;
        *(void **)(result + 0x28) = Arg1;
    }
    v_stack_mE0 = Arg2 + 24;
    result = (uint32_t)(((uint32_t)(v_stack_p18) + (uint32_t)(v_stack_p18) * 2) << (3));
    v_stack_mD8 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_00682638;
loc_006825C0:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10) == 0) goto loc_0068262E;
    if ((*(uint64_t *)(arg2 + 0x18 + 0x8)) <= (*(uint64_t *)(arg1 + 0x30))) goto loc_006825D7;
    Arg2 = (*(uint64_t *)(arg2 + 0x18 + 0x8)) - (*(uint64_t *)(arg1 + 0x30));
    goto loc_006825E1;
loc_006825D7:
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x40))) - (Arg2);
loc_006825E1:
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x30) + result * 1) <= ((uint32_t)(0x80000000ULL))) { result = (uint32_t)(*(uint64_t *)(arg1 + 0x30) + result * 1); }
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10) + (int32_t)(*(uint32_t *)(arg2 + 0x18)) * 4) = (uint32_t)(result);
    if ((*(uint64_t *)(arg1 + 0x30) + result * 1) >= ((uint32_t)(0x80000000ULL))) goto loc_0068262E;
    Arg1 = (*(uint64_t *)(arg2 + 0x18 + 0x8)) + (*(uint64_t *)(v_rip + 0x94454B));
    Arg1 = (Arg1) >> (16);
    result = *(uint64_t *)(v_rip + 0x7AB244);
    if (!(condition_is_below)) {
        result = (int32_t)(*(uint32_t *)(arg2 + 0x18));
    }
    local_rsi = (Arg2 + 24) + (24);
    a4 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) - (1);
    if (condition_is_not_equal) goto loc_006825C0;
loc_00682638:
    if ((*(uint32_t *)(v_rip + 0x9446D4)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 12, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    }
    result = KeQueryActiveProcessorCountEx((uint32_t)(0xFFFFULL), 12, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    v_stack_m104 = (uint32_t)(result);
    v_stack_m108 = (uint32_t)(result);
    result = KeIpiGenericCall(v_rip + 176, v_stack_m108, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    if ((*(uint32_t *)(v_rip + 0x9446A0)) != 0) {
        Arg1 = 12;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    }
loc_00682699:
    result = MiUnlockEntireDriver(v_stack_mA8, v_stack_mF0, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
loc_006826A7:
    if (v_stack_mD0 == v_stack_mD0) goto loc_006826E1;
    if ((*(uint64_t *)(v_stack_mD0 + 0x8)) != v_stack_mD0) goto loc_006826DA;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mD0) + 0x8)) != v_stack_mD0) goto loc_006826DA;
    v_stack_mD0 = *(uint64_t *)(v_stack_mD0);
    *(uint64_t *)(*(uint64_t *)(v_stack_mD0) + 0x8) = v_stack_mD0;
    result = MiUnlockAndFreeDvPatchImage(v_stack_mD0, v_stack_mD0, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    goto loc_006826A7;
loc_006826DA:
loc_006826E1:
    if (v_stack_mE8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_mE8, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x118) + 0x10), a4);
    }
    local_rsp = (local_rsp) + (256);
    return (uint32_t)((uint32_t)(result));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x118` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00682268&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
