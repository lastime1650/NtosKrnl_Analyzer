# MiSystemFault

- RVA: `0x0034AA64`–`0x0034B2BB` (길이 `2,135` bytes)
- VA: `0x000000014034AA64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00078528`
- 디코드: `510`개 명령, `2,135/2,135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x0034AAB3` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x0034AB5F` → [KeInvalidAccessAllowed](KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x0034AB7B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0034AB8D` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0034ABBC` → [MiSystemVaTypeHasWsles](MiSystemVaTypeHasWsles_function_0034B2C4.md) (function, `0x0034B2C4`)
- `0x0034ABC9` → [MiSystemVaTypeToVm](../28/MiSystemVaTypeToVm_function_0028EB50.md) (function, `0x0028EB50`)
- `0x0034ABEF` → [MiSynchronizeSystemVa](../28/MiSynchronizeSystemVa_function_0028ECB8.md) (function, `0x0028ECB8`)
- `0x0034ABFF` → [MiCheckSystemPageTables](MiCheckSystemPageTables_function_0034B2F0.md) (function, `0x0034B2F0`)
- `0x0034AC8E` → [MiUnlockSystemVa](MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x0034AD16` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0034AD3D` → [MiHyperSpaceSize](../2C/MiHyperSpaceSize_function_002C2DFC.md) (function, `0x002C2DFC`)
- `0x0034ADA2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034ADF2` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x0034AE26` → [MiReleaseSpinLockShared](MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x0034AE3D` → [MiUnlockSystemVa](MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x0034AEBB` → [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) (function, `0x00362A0C`)
- `0x0034AEC6` → [MiUnlockSystemVa](MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x0034AEDB` → [MiCopyOnWriteCheckConditions](../2A/MiCopyOnWriteCheckConditions_function_002A750C.md) (function, `0x002A750C`)
- `0x0034AEF1` → [MiCheckSystemNxFault](../4A/MiCheckSystemNxFault_function_004A44C0.md) (function, `0x004A44C0`)
- `0x0034AF10` → [MiNoFaultFound](../41/MiNoFaultFound_function_0041BB20.md) (function, `0x0041BB20`)
- `0x0034AF4D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034AF6B` → [MiResolveDemandZeroFault](../2B/MiResolveDemandZeroFault_function_002B5A40.md) (function, `0x002B5A40`)
- `0x0034B06E` → [MiUnlockSystemVa](MiUnlockSystemVa_function_0034B800.md) (function, `0x0034B800`)
- `0x0034B093` → [MiUpdatePfnForPrefetchByPte](../32/MiUpdatePfnForPrefetchByPte_function_00321210.md) (function, `0x00321210`)
- `0x0034B0A0` → [MiGenerateAccessViolation](MiGenerateAccessViolation_function_0034B50C.md) (function, `0x0034B50C`)
- `0x0034B0C0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034B10E` → [KeInvalidAccessAllowed](KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x0034B11E` → [MiGenerateAccessViolation](MiGenerateAccessViolation_function_0034B50C.md) (function, `0x0034B50C`)
- `0x0034B13E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034B152` → [MiGenerateAccessViolation](MiGenerateAccessViolation_function_0034B50C.md) (function, `0x0034B50C`)
- `0x0034B177` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034B1E2` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0034B1EE` → [MiTransientPageListWriter](../4D/MiTransientPageListWriter_function_004DB35C.md) (function, `0x004DB35C`)
- `0x0034B268` → [KeInvalidAccessAllowed](KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)

### Direct callers
- [sub_0027F36E](../27/Unknown_function_0027F36E.md) at `0x0027F4C1`

### Static image references
- `0x0034AA87` → RVA `0x00E0A740` (`.data`; read)
- `0x0034AB01` → RVA `0x00E2F388` (`.data`; read)
- `0x0034AB34` → RVA `0x00E2FF04` (`.data`; read)
- `0x0034ACA9` → RVA `0x00E2F380` (`.data`; read)
- `0x0034ACBF` → RVA `0x00E2F390` (`.data`; read)
- `0x0034ADEB` → RVA `0x00E2FF00` (`.data`; read)
- `0x0034ADF7` → RVA `0x00E2FF08` (`.data`; read)
- `0x0034AE52` → RVA `0x00E2DC80` (`.data`; read)
- `0x0034AFAF` → RVA `0x00E38340` (`.data`; read)
- `0x0034B187` → RVA `0x00E38200` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0034B261` → [sub_006E218A](../6E/Unknown_function_006E218A.md) (`tail-transfer`)
  - `0x0034B275` → [sub_006E218A](../6E/Unknown_function_006E218A.md) (`tail-transfer`)
  - `0x0034B293` → [sub_006E218A + 0x2D](../6E/Unknown_function_006E218A.md) (`tail-transfer`)
  - `0x0034B2B6` → [sub_006E218A + 0x3C](../6E/Unknown_function_006E218A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0034AA64  48 8B C4                        mov rax, rsp
0034AA67  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0034AA6B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0034AA6F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0034AA73  55                              push rbp
0034AA74  41 54                           push r12
0034AA76  41 55                           push r13
0034AA78  41 56                           push r14
0034AA7A  41 57                           push r15
0034AA7C  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0034AA80  48 81 EC C0 00 00 00            sub rsp, 0xc0
0034AA87  48 8B 05 B2 FC AB 00            mov rax, qword ptr [rip + 0xabfcb2]
0034AA8E  48 33 C4                        xor rax, rsp
0034AA91  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0034AA95  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0034AA98  48 8B F9                        mov rdi, rcx
0034AA9B  0F BA E0 08                     bt eax, 8
0034AA9F  0F 82 9B 05 00 00               jb 0x14034b040
0034AAA5  84 C0                           test al, al
0034AAA7  0F 88 87 04 00 00               js 0x14034af34
0034AAAD  4C 8B 09                        mov r9, qword ptr [rcx]
0034AAB0  49 8B C9                        mov rcx, r9
0034AAB3  E8 E8 15 F3 FF                  call 0x14027c0a0
0034AAB8  48 8B D8                        mov rbx, rax
0034AABB  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
0034AAC5  49 8B CD                        mov rcx, r13
0034AAC8  48 BA FF FF FF FF FF F6 FF FF   movabs rdx, 0xfffff6ffffffffff
0034AAD2  4C 3B C9                        cmp r9, rcx
0034AAD5  0F 83 CB 01 00 00               jae 0x14034aca6
0034AADB  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034AADF  48 8B C8                        mov rcx, rax
0034AAE2  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0034AAE6  A8 01                           test al, 1
0034AAE8  0F 85 BA 02 00 00               jne 0x14034ada8
0034AAEE  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0034AAF8  48 3B D8                        cmp rbx, rax
0034AAFB  0F 82 E0 02 00 00               jb 0x14034ade1
0034AB01  48 3B 1D 80 48 AE 00            cmp rbx, qword ptr [rip + 0xae4880]
0034AB08  0F 83 2F 02 00 00               jae 0x14034ad3d
0034AB0E  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0034AB17  41 8B 87 A4 05 00 00            mov eax, dword ptr [r15 + 0x5a4]
0034AB1E  0F BA E0 0A                     bt eax, 0xa
0034AB22  0F 82 18 05 00 00               jb 0x14034b040
0034AB28  33 F6                           xor esi, esi
0034AB2A  0F BA E0 08                     bt eax, 8
0034AB2E  0F 82 B4 06 00 00               jb 0x14034b1e8
0034AB34  39 35 CA 53 AE 00               cmp dword ptr [rip + 0xae53ca], esi
0034AB3A  4C 8B 27                        mov r12, qword ptr [rdi]
0034AB3D  0F 85 A8 02 00 00               jne 0x14034adeb
0034AB43  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0034AB47  41 BF 03 00 00 00               mov r15d, 3
0034AB4D  48 8B C1                        mov rax, rcx
0034AB50  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034AB54  F6 C1 01                        test cl, 1
0034AB57  0F 85 C6 03 00 00               jne 0x14034af23
0034AB5D  33 D2                           xor edx, edx
0034AB5F  E8 8C 08 00 00                  call 0x14034b3f0
0034AB64  84 C0                           test al, al
0034AB66  0F 85 C0 03 00 00               jne 0x14034af2c
0034AB6C  44 8A EE                        mov r13b, sil
0034AB6F  33 D2                           xor edx, edx
0034AB71  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0034AB75  41 B8 80 00 00 00               mov r8d, 0x80
0034AB7B  E8 C0 C0 37 00                  call 0x1406c6c40
0034AB80  41 BE 01 00 00 00               mov r14d, 1
0034AB86  48 8B CB                        mov rcx, rbx
0034AB89  44 89 75 AB                     mov dword ptr [rbp - 0x55], r14d
0034AB8D  E8 EE 40 F4 FF                  call 0x14028ec80
0034AB92  8B 4F 50                        mov ecx, dword ptr [rdi + 0x50]
0034AB95  44 8B D0                        mov r10d, eax
0034AB98  F6 C1 40                        test cl, 0x40
0034AB9B  0F 85 F6 00 00 00               jne 0x14034ac97
0034ABA1  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034ABA5  41 84 C6                        test r14b, al
0034ABA8  0F 85 7A 04 00 00               jne 0x14034b028
0034ABAE  45 84 ED                        test r13b, r13b
0034ABB1  45 0F 44 F7                     cmove r14d, r15d
0034ABB5  44 89 75 AB                     mov dword ptr [rbp - 0x55], r14d
0034ABB9  41 8B CA                        mov ecx, r10d
0034ABBC  E8 03 07 00 00                  call 0x14034b2c4
0034ABC1  85 C0                           test eax, eax
0034ABC3  0F 84 C0 03 00 00               je 0x14034af89
0034ABC9  E8 82 3F F4 FF                  call 0x14028eb50
0034ABCE  4C 8B E0                        mov r12, rax
0034ABD1  48 85 C0                        test rax, rax
0034ABD4  0F 84 60 04 00 00               je 0x14034b03a
0034ABDA  48 8B 17                        mov rdx, qword ptr [rdi]
0034ABDD  48 8D 45 A7                     lea rax, [rbp - 0x59]
0034ABE1  45 33 C9                        xor r9d, r9d
0034ABE4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0034ABE9  45 8B C2                        mov r8d, r10d
0034ABEC  49 8B CC                        mov rcx, r12
0034ABEF  E8 C4 40 F4 FF                  call 0x14028ecb8
0034ABF4  85 C0                           test eax, eax
0034ABF6  0F 84 77 04 00 00               je 0x14034b073
0034ABFC  48 8B CF                        mov rcx, rdi
0034ABFF  E8 EC 06 00 00                  call 0x14034b2f0
0034AC04  83 F8 02                        cmp eax, 2
0034AC07  0F 84 5D 04 00 00               je 0x14034b06a
0034AC0D  83 F8 01                        cmp eax, 1
0034AC10  0F 84 23 02 00 00               je 0x14034ae39
0034AC16  0F 10 45 BF                     movups xmm0, xmmword ptr [rbp - 0x41]
0034AC1A  F2 0F 10 4D CF                  movsd xmm1, qword ptr [rbp - 0x31]
0034AC1F  0F 11 47 38                     movups xmmword ptr [rdi + 0x38], xmm0
0034AC23  F2 0F 11 4F 48                  movsd qword ptr [rdi + 0x48], xmm1
0034AC28  4C 8B 7F 18                     mov r15, qword ptr [rdi + 0x18]
0034AC2C  49 8B 1F                        mov rbx, qword ptr [r15]
0034AC2F  F6 C3 01                        test bl, 1
0034AC32  0F 85 44 02 00 00               jne 0x14034ae7c
0034AC38  48 8B 17                        mov rdx, qword ptr [rdi]
0034AC3B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0034AC45  48 8B C0                        mov rax, rax
0034AC48  48 3B D0                        cmp rdx, rax
0034AC4B  0F 83 06 01 00 00               jae 0x14034ad57
0034AC51  4C 8B F6                        mov r14, rsi
0034AC54  48 0F BA E3 0A                  bt rbx, 0xa
0034AC59  0F 82 EA 01 00 00               jb 0x14034ae49
0034AC5F  48 8B D3                        mov rdx, rbx
0034AC62  41 BF E0 03 00 00               mov r15d, 0x3e0
0034AC68  49 23 D7                        and rdx, r15
0034AC6B  0F 94 C1                        sete cl
0034AC6E  48 0F BA E3 0B                  bt rbx, 0xb
0034AC73  0F 93 C0                        setae al
0034AC76  84 C8                           test al, cl
0034AC78  74 5C                           je 0x14034acd6
0034AC7A  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0034AC7D  A8 40                           test al, 0x40
0034AC7F  0F 84 73 04 00 00               je 0x14034b0f8
0034AC85  BE 05 00 00 C0                  mov esi, 0xc0000005
0034AC8A  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0034AC8E  E8 6D 0B 00 00                  call 0x14034b800
0034AC93  8B C6                           mov eax, esi
0034AC95  EB 78                           jmp 0x14034ad0f
0034AC97  41 83 FA 05                     cmp r10d, 5
0034AC9B  0F 84 18 FF FF FF               je 0x14034abb9
0034ACA1  E9 9A 03 00 00                  jmp 0x14034b040
0034ACA6  48 8B CA                        mov rcx, rdx
0034ACA9  48 3B 1D D0 46 AE 00            cmp rbx, qword ptr [rip + 0xae46d0]
0034ACB0  0F 82 25 FE FF FF               jb 0x14034aadb
0034ACB6  4C 3B C9                        cmp r9, rcx
0034ACB9  0F 87 1C FE FF FF               ja 0x14034aadb
0034ACBF  48 3B 1D CA 46 AE 00            cmp rbx, qword ptr [rip + 0xae46ca]
0034ACC6  0F 87 0F FE FF FF               ja 0x14034aadb
0034ACCC  48 83 4F 08 02                  or qword ptr [rdi + 8], 2
0034ACD1  E9 05 FE FF FF                  jmp 0x14034aadb
0034ACD6  41 BC 00 03 00 00               mov r12d, 0x300
0034ACDC  49 3B D4                        cmp rdx, r12
0034ACDF  0F 84 EB 02 00 00               je 0x14034afd0
0034ACE5  49 3B D7                        cmp rdx, r15
0034ACE8  0F 84 CD 02 00 00               je 0x14034afbb
0034ACEE  F6 47 08 02                     test byte ptr [rdi + 8], 2
0034ACF2  74 12                           je 0x14034ad06
0034ACF4  4D 85 F6                        test r14, r14
0034ACF7  75 0D                           jne 0x14034ad06
0034ACF9  8A C3                           mov al, bl
0034ACFB  C0 E8 05                        shr al, 5
0034ACFE  A8 04                           test al, 4
0034AD00  0F 84 74 05 00 00               je 0x14034b27a
0034AD06  4C 89 77 68                     mov qword ptr [rdi + 0x68], r14
0034AD0A  B8 16 00 00 C0                  mov eax, 0xc0000016
0034AD0F  48 8B 4D 27                     mov rcx, qword ptr [rbp + 0x27]
0034AD13  48 33 CC                        xor rcx, rsp
0034AD16  E8 25 19 36 00                  call 0x1406ac640
0034AD1B  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
0034AD23  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0034AD27  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0034AD2B  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0034AD2F  49 8B E3                        mov rsp, r11
0034AD32  41 5F                           pop r15
0034AD34  41 5E                           pop r14
0034AD36  41 5D                           pop r13
0034AD38  41 5C                           pop r12
0034AD3A  5D                              pop rbp
0034AD3B  C3                              ret
0034AD3C  CC                              int3
0034AD3D  E8 BA 80 F7 FF                  call 0x1402c2dfc
0034AD42  48 03 05 3F 46 AE 00            add rax, qword ptr [rip + 0xae463f]
0034AD49  48 3B D8                        cmp rbx, rax
0034AD4C  0F 83 BC FD FF FF               jae 0x14034ab0e
0034AD52  E9 8A 00 00 00                  jmp 0x14034ade1
0034AD57  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0034AD61  48 8B C0                        mov rax, rax
0034AD64  48 3B D0                        cmp rdx, rax
0034AD67  0F 87 E4 FE FF FF               ja 0x14034ac51
0034AD6D  45 84 ED                        test r13b, r13b
0034AD70  0F 85 0F FF FF FF               jne 0x14034ac85
0034AD76  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034AD7A  41 F6 C1 01                     test r9b, 1
0034AD7E  74 10                           je 0x14034ad90
0034AD80  49 8B C1                        mov rax, r9
0034AD83  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034AD87  80 38 01                        cmp byte ptr [rax], 1
0034AD8A  0F 84 FA FE FF FF               je 0x14034ac8a
0034AD90  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0034AD94  B9 50 00 00 00                  mov ecx, 0x50
0034AD99  48 C7 44 24 20 09 00 00 00      mov qword ptr [rsp + 0x20], 9
0034ADA2  E8 B9 28 1B 00                  call 0x1404fd660
0034ADA7  CC                              int3
0034ADA8  80 39 07                        cmp byte ptr [rcx], 7
0034ADAB  74 09                           je 0x14034adb6
0034ADAD  80 39 08                        cmp byte ptr [rcx], 8
0034ADB0  0F 85 38 FD FF FF               jne 0x14034aaee
0034ADB6  49 8B C5                        mov rax, r13
0034ADB9  4C 3B C8                        cmp r9, rax
0034ADBC  0F 82 9E 02 00 00               jb 0x14034b060
0034ADC2  48 8B C2                        mov rax, rdx
0034ADC5  4C 3B C8                        cmp r9, rax
0034ADC8  0F 87 92 02 00 00               ja 0x14034b060
0034ADCE  48 B8 FF FF FE FF FF 7F 00 00   movabs rax, 0x7ffffffeffff
0034ADD8  48 3B D8                        cmp rbx, rax
0034ADDB  0F 87 69 02 00 00               ja 0x14034b04a
0034ADE1  B8 C0 00 00 00                  mov eax, 0xc0
0034ADE6  E9 24 FF FF FF                  jmp 0x14034ad0f
0034ADEB  48 8D 0D 0E 51 AE 00            lea rcx, [rip + 0xae510e]
0034ADF2  E8 E9 2E F0 FF                  call 0x14024dce0
0034ADF7  4C 8B 35 0A 51 AE 00            mov r14, qword ptr [rip + 0xae510a]
0034ADFE  8A D0                           mov dl, al
0034AE00  EB 0F                           jmp 0x14034ae11
0034AE02  4D 3B 7E 18                     cmp r15, qword ptr [r14 + 0x18]
0034AE06  0F 87 21 04 00 00               ja 0x14034b22d
0034AE0C  73 08                           jae 0x14034ae16
0034AE0E  4D 8B 36                        mov r14, qword ptr [r14]
0034AE11  4D 85 F6                        test r14, r14
0034AE14  75 EC                           jne 0x14034ae02
0034AE16  4D 85 F6                        test r14, r14
0034AE19  0F 85 B5 02 00 00               jne 0x14034b0d4
0034AE1F  48 8D 0D DA 50 AE 00            lea rcx, [rip + 0xae50da]
0034AE26  E8 C5 DD FF FF                  call 0x140348bf0
0034AE2B  4D 85 F6                        test r14, r14
0034AE2E  0F 84 0F FD FF FF               je 0x14034ab43
0034AE34  E9 07 02 00 00                  jmp 0x14034b040
0034AE39  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0034AE3D  E8 BE 09 00 00                  call 0x14034b800
0034AE42  33 C0                           xor eax, eax
0034AE44  E9 C6 FE FF FF                  jmp 0x14034ad0f
0034AE49  F6 C3 02                        test bl, 2
0034AE4C  0F 85 01 01 00 00               jne 0x14034af53
0034AE52  48 8B 05 27 2E AE 00            mov rax, qword ptr [rip + 0xae2e27]
0034AE59  4C 8B F3                        mov r14, rbx
0034AE5C  48 85 C0                        test rax, rax
0034AE5F  74 12                           je 0x14034ae73
0034AE61  F6 C3 10                        test bl, 0x10
0034AE64  0F 85 B0 00 00 00               jne 0x14034af1a
0034AE6A  4C 8B F0                        mov r14, rax
0034AE6D  49 F7 D6                        not r14
0034AE70  4C 23 F3                        and r14, rbx
0034AE73  49 C1 FE 10                     sar r14, 0x10
0034AE77  E9 72 FE FF FF                  jmp 0x14034acee
0034AE7C  84 DB                           test bl, bl
0034AE7E  0F 88 0F 03 00 00               js 0x14034b193
0034AE84  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0034AE88  F6 C2 01                        test dl, 1
0034AE8B  0F 85 E8 01 00 00               jne 0x14034b079
0034AE91  F6 47 08 02                     test byte ptr [rdi + 8], 2
0034AE95  74 4E                           je 0x14034aee5
0034AE97  48 0F BA E3 0B                  bt rbx, 0xb
0034AE9C  72 58                           jb 0x14034aef6
0034AE9E  48 0F BA E3 09                  bt rbx, 9
0034AEA3  0F 83 9B 02 00 00               jae 0x14034b144
0034AEA9  48 8B 0F                        mov rcx, qword ptr [rdi]
0034AEAC  45 33 C9                        xor r9d, r9d
0034AEAF  49 83 C8 FF                     or r8, 0xffffffffffffffff
0034AEB3  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0034AEB8  49 8B D7                        mov rdx, r15
0034AEBB  E8 4C 7B 01 00                  call 0x140362a0c
0034AEC0  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0034AEC4  8B D8                           mov ebx, eax
0034AEC6  E8 35 09 00 00                  call 0x14034b800
0034AECB  85 DB                           test ebx, ebx
0034AECD  0F 89 6F FF FF FF               jns 0x14034ae42
0034AED3  45 33 C0                        xor r8d, r8d
0034AED6  8B D3                           mov edx, ebx
0034AED8  49 8B CC                        mov rcx, r12
0034AEDB  E8 2C C6 F5 FF                  call 0x1402a750c
0034AEE0  E9 5D FF FF FF                  jmp 0x14034ae42
0034AEE5  41 B8 02 00 00 00               mov r8d, 2
0034AEEB  48 8B D3                        mov rdx, rbx
0034AEEE  48 8B CF                        mov rcx, rdi
0034AEF1  E8 CA 95 15 00                  call 0x1404a44c0
0034AEF6  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034AEFA  49 8B D7                        mov rdx, r15
0034AEFD  4C 8B 07                        mov r8, qword ptr [rdi]
0034AF00  48 8B CF                        mov rcx, rdi
0034AF03  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0034AF08  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0034AF10  E8 0B 0C 0D 00                  call 0x14041bb20
0034AF15  E9 70 FD FF FF                  jmp 0x14034ac8a
0034AF1A  49 83 E6 EF                     and r14, 0xffffffffffffffef
0034AF1E  E9 50 FF FF FF                  jmp 0x14034ae73
0034AF23  80 38 01                        cmp byte ptr [rax], 1
0034AF26  0F 85 F4 02 00 00               jne 0x14034b220
0034AF2C  41 B5 01                        mov r13b, 1
0034AF2F  E9 3B FC FF FF                  jmp 0x14034ab6f
0034AF34  4C 8B 49 10                     mov r9, qword ptr [rcx + 0x10]
0034AF38  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0034AF3C  48 8B 11                        mov rdx, qword ptr [rcx]
0034AF3F  B9 50 00 00 00                  mov ecx, 0x50
0034AF44  48 C7 44 24 20 0E 00 00 00      mov qword ptr [rsp + 0x20], 0xe
0034AF4D  E8 0E 27 1B 00                  call 0x1404fd660
0034AF52  CC                              int3
0034AF53  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034AF57  A8 01                           test al, 1
0034AF59  0F 85 A1 02 00 00               jne 0x14034b200
0034AF5F  45 33 C9                        xor r9d, r9d
0034AF62  45 33 C0                        xor r8d, r8d
0034AF65  49 8B D7                        mov rdx, r15
0034AF68  48 8B CF                        mov rcx, rdi
0034AF6B  E8 D0 AA F6 FF                  call 0x1402b5a40
0034AF70  0F 10 47 38                     movups xmm0, xmmword ptr [rdi + 0x38]
0034AF74  8B F0                           mov esi, eax
0034AF76  F2 0F 10 4F 48                  movsd xmm1, qword ptr [rdi + 0x48]
0034AF7B  0F 11 45 BF                     movups xmmword ptr [rbp - 0x41], xmm0
0034AF7F  F2 0F 11 4D CF                  movsd qword ptr [rbp - 0x31], xmm1
0034AF84  E9 01 FD FF FF                  jmp 0x14034ac8a
0034AF89  41 83 FA 0D                     cmp r10d, 0xd
0034AF8D  0F 85 EA 01 00 00               jne 0x14034b17d
0034AF93  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034AF97  48 8B C8                        mov rcx, rax
0034AF9A  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
0034AF9E  A8 01                           test al, 1
0034AFA0  0F 84 94 00 00 00               je 0x14034b03a
0034AFA6  80 39 04                        cmp byte ptr [rcx], 4
0034AFA9  0F 85 17 01 00 00               jne 0x14034b0c6
0034AFAF  4C 8D 25 8A D3 AE 00            lea r12, [rip + 0xaed38a]
0034AFB6  E9 1F FC FF FF                  jmp 0x14034abda
0034AFBB  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034AFBF  A8 01                           test al, 1
0034AFC1  74 0D                           je 0x14034afd0
0034AFC3  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034AFC7  80 38 04                        cmp byte ptr [rax], 4
0034AFCA  0F 84 1E FD FF FF               je 0x14034acee
0034AFD0  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0034AFD3  A8 40                           test al, 0x40
0034AFD5  75 24                           jne 0x14034affb
0034AFD7  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0034AFDB  48 8B C1                        mov rax, rcx
0034AFDE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034AFE2  F6 C1 01                        test cl, 1
0034AFE5  0F 84 7B 02 00 00               je 0x14034b266
0034AFEB  80 38 01                        cmp byte ptr [rax], 1
0034AFEE  74 0B                           je 0x14034affb
0034AFF0  8A 08                           mov cl, byte ptr [rax]
0034AFF2  80 F9 06                        cmp cl, 6
0034AFF5  0F 85 5D 02 00 00               jne 0x14034b258
0034AFFB  48 8B C3                        mov rax, rbx
0034AFFE  49 23 C7                        and rax, r15
0034B001  49 3B C4                        cmp rax, r12
0034B004  0F 84 7B FC FF FF               je 0x14034ac85
0034B00A  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0034B00E  A8 01                           test al, 1
0034B010  0F 84 6F FC FF FF               je 0x14034ac85
0034B016  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034B01A  80 38 01                        cmp byte ptr [rax], 1
0034B01D  0F 84 CB FC FF FF               je 0x14034acee
0034B023  E9 5D FC FF FF                  jmp 0x14034ac85
0034B028  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034B02C  44 38 30                        cmp byte ptr [rax], r14b
0034B02F  0F 85 79 FB FF FF               jne 0x14034abae
0034B035  E9 7F FB FF FF                  jmp 0x14034abb9
0034B03A  41 F6 C6 02                     test r14b, 2
0034B03E  75 5D                           jne 0x14034b09d
0034B040  B8 05 00 00 C0                  mov eax, 0xc0000005
0034B045  E9 C5 FC FF FF                  jmp 0x14034ad0f
0034B04A  48 3B 1D 2F 43 AE 00            cmp rbx, qword ptr [rip + 0xae432f]
0034B051  72 0D                           jb 0x14034b060
0034B053  48 3B 1D 36 43 AE 00            cmp rbx, qword ptr [rip + 0xae4336]
0034B05A  0F 86 81 FD FF FF               jbe 0x14034ade1
0034B060  B8 06 00 00 D0                  mov eax, 0xd0000006
0034B065  E9 A5 FC FF FF                  jmp 0x14034ad0f
0034B06A  48 8D 4D A7                     lea rcx, [rbp - 0x59]
0034B06E  E8 8D 07 00 00                  call 0x14034b800
0034B073  44 8B 75 AB                     mov r14d, dword ptr [rbp - 0x55]
0034B077  EB C1                           jmp 0x14034b03a
0034B079  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
0034B07D  80 3A 01                        cmp byte ptr [rdx], 1
0034B080  0F 85 0B FE FF FF               jne 0x14034ae91
0034B086  8B 52 50                        mov edx, dword ptr [rdx + 0x50]
0034B089  45 33 C0                        xor r8d, r8d
0034B08C  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0034B090  83 E2 07                        and edx, 7
0034B093  E8 78 61 FD FF                  call 0x140321210
0034B098  E9 ED FB FF FF                  jmp 0x14034ac8a
0034B09D  48 8B CF                        mov rcx, rdi
0034B0A0  E8 67 04 00 00                  call 0x14034b50c
0034B0A5  85 C0                           test eax, eax
0034B0A7  75 97                           jne 0x14034b040
0034B0A9  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034B0AD  8D 48 50                        lea ecx, [rax + 0x50]
0034B0B0  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0034B0B4  48 8B 17                        mov rdx, qword ptr [rdi]
0034B0B7  48 C7 44 24 20 02 00 00 00      mov qword ptr [rsp + 0x20], 2
0034B0C0  E8 9B 25 1B 00                  call 0x1404fd660
0034B0C5  CC                              int3
0034B0C6  80 39 01                        cmp byte ptr [rcx], 1
0034B0C9  0F 84 E0 FE FF FF               je 0x14034afaf
0034B0CF  E9 66 FF FF FF                  jmp 0x14034b03a
0034B0D4  49 C1 EC 09                     shr r12, 9
0034B0D8  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0034B0E2  4C 23 E0                        and r12, rax
0034B0E5  49 8B C5                        mov rax, r13
0034B0E8  4C 03 E0                        add r12, rax
0034B0EB  4D 39 66 28                     cmp qword ptr [r14 + 0x28], r12
0034B0EF  4C 0F 45 F6                     cmovne r14, rsi
0034B0F3  E9 27 FD FF FF                  jmp 0x14034ae1f
0034B0F8  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0034B0FC  48 8B C1                        mov rax, rcx
0034B0FF  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034B103  F6 C1 01                        test cl, 1
0034B106  0F 85 2A 01 00 00               jne 0x14034b236
0034B10C  33 D2                           xor edx, edx
0034B10E  E8 DD 02 00 00                  call 0x14034b3f0
0034B113  84 C0                           test al, al
0034B115  0F 85 6A FB FF FF               jne 0x14034ac85
0034B11B  48 8B CF                        mov rcx, rdi
0034B11E  E8 E9 03 00 00                  call 0x14034b50c
0034B123  85 C0                           test eax, eax
0034B125  0F 85 5A FB FF FF               jne 0x14034ac85
0034B12B  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034B12F  8D 48 50                        lea ecx, [rax + 0x50]
0034B132  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0034B136  48 8B 17                        mov rdx, qword ptr [rdi]
0034B139  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0034B13E  E8 1D 25 1B 00                  call 0x1404fd660
0034B143  CC                              int3
0034B144  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0034B147  A8 40                           test al, 0x40
0034B149  0F 85 5A FD FF FF               jne 0x14034aea9
0034B14F  48 8B CF                        mov rcx, rdi
0034B152  E8 B5 03 00 00                  call 0x14034b50c
0034B157  85 C0                           test eax, eax
0034B159  0F 85 26 FB FF FF               jne 0x14034ac85
0034B15F  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034B163  4C 8B C3                        mov r8, rbx
0034B166  48 8B 17                        mov rdx, qword ptr [rdi]
0034B169  B9 BE 00 00 00                  mov ecx, 0xbe
0034B16E  48 C7 44 24 20 0B 00 00 00      mov qword ptr [rsp + 0x20], 0xb
0034B177  E8 E4 24 1B 00                  call 0x1404fd660
0034B17C  CC                              int3
0034B17D  41 83 FA 08                     cmp r10d, 8
0034B181  0F 85 B3 FE FF FF               jne 0x14034b03a
0034B187  4C 8D 25 72 D0 AE 00            lea r12, [rip + 0xaed072]
0034B18E  E9 47 FA FF FF                  jmp 0x14034abda
0034B193  48 8B 17                        mov rdx, qword ptr [rdi]
0034B196  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0034B1A0  48 8B C0                        mov rax, rax
0034B1A3  48 3B D0                        cmp rdx, rax
0034B1A6  0F 82 D8 FC FF FF               jb 0x14034ae84
0034B1AC  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0034B1B6  48 8B C0                        mov rax, rax
0034B1B9  48 3B D0                        cmp rdx, rax
0034B1BC  0F 87 C2 FC FF FF               ja 0x14034ae84
0034B1C2  F6 45 AB 02                     test byte ptr [rbp - 0x55], 2
0034B1C6  0F 84 B9 FA FF FF               je 0x14034ac85
0034B1CC  4C 8B 4F 10                     mov r9, qword ptr [rdi + 0x10]
0034B1D0  B9 50 00 00 00                  mov ecx, 0x50
0034B1D5  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
0034B1D9  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
0034B1E2  E8 79 24 1B 00                  call 0x1404fd660
0034B1E7  CC                              int3
0034B1E8  48 8B 17                        mov rdx, qword ptr [rdi]
0034B1EB  49 8B CF                        mov rcx, r15
0034B1EE  E8 69 01 19 00                  call 0x1404db35c
0034B1F3  85 C0                           test eax, eax
0034B1F5  0F 84 39 F9 FF FF               je 0x14034ab34
0034B1FB  E9 40 FE FF FF                  jmp 0x14034b040
0034B200  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034B204  80 38 01                        cmp byte ptr [rax], 1
0034B207  0F 84 7D FA FF FF               je 0x14034ac8a
0034B20D  E9 4D FD FF FF                  jmp 0x14034af5f
0034B212  80 F9 06                        cmp cl, 6
0034B215  0F 85 51 F9 FF FF               jne 0x14034ab6c
0034B21B  E9 0C FD FF FF                  jmp 0x14034af2c
0034B220  8A 08                           mov cl, byte ptr [rax]
0034B222  41 3A CF                        cmp cl, r15b
0034B225  0F 84 01 FD FF FF               je 0x14034af2c
0034B22B  EB E5                           jmp 0x14034b212
0034B22D  4D 8B 76 08                     mov r14, qword ptr [r14 + 8]
0034B231  E9 DB FB FF FF                  jmp 0x14034ae11
0034B236  80 38 01                        cmp byte ptr [rax], 1
0034B239  0F 84 46 FA FF FF               je 0x14034ac85
0034B23F  8A 08                           mov cl, byte ptr [rax]
0034B241  80 F9 03                        cmp cl, 3
0034B244  0F 84 3B FA FF FF               je 0x14034ac85
0034B24A  80 F9 06                        cmp cl, 6
0034B24D  0F 84 32 FA FF FF               je 0x14034ac85
0034B253  E9 C3 FE FF FF                  jmp 0x14034b11b
0034B258  80 F9 03                        cmp cl, 3
0034B25B  0F 84 9A FD FF FF               je 0x14034affb
0034B261  E9 24 6F 39 00                  jmp 0x1406e218a
0034B266  33 D2                           xor edx, edx
0034B268  E8 83 01 00 00                  call 0x14034b3f0
0034B26D  84 C0                           test al, al
0034B26F  0F 85 86 FD FF FF               jne 0x14034affb
0034B275  E9 10 6F 39 00                  jmp 0x1406e218a
0034B27A  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
0034B27D  A8 40                           test al, 0x40
0034B27F  0F 85 00 FA FF FF               jne 0x14034ac85
0034B285  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0034B289  48 8B C1                        mov rax, rcx
0034B28C  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0034B290  F6 C1 01                        test cl, 1
0034B293  0F 84 1E 6F 39 00               je 0x1406e21b7
0034B299  80 38 01                        cmp byte ptr [rax], 1
0034B29C  0F 84 E3 F9 FF FF               je 0x14034ac85
0034B2A2  8A 08                           mov cl, byte ptr [rax]
0034B2A4  80 F9 03                        cmp cl, 3
0034B2A7  0F 84 D8 F9 FF FF               je 0x14034ac85
0034B2AD  80 F9 06                        cmp cl, 6
0034B2B0  0F 84 CF F9 FF FF               je 0x14034ac85
0034B2B6  E9 0B 6F 39 00                  jmp 0x1406e21c6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSystemFault(__int64 a1)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mC8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 11271346)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
    if (condition_is_below) goto loc_0034B040;
    if (sign_flag) goto loc_0034AF34;
    result = MiGetLeafVa(*(unsigned __int64 *)(a1), a2, a3, *(unsigned __int64 *)(a1));
    if ((*(unsigned __int64 *)(a1)) >= v_r13) goto loc_0034ACA6;
loc_0034AADB:
    a1 = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_0034ADA8;
loc_0034AAEE:
    if (result < (*(unsigned __int64 *)(a1 + 16))) goto loc_0034ADE1;
    if (result >= (*(unsigned __int64 *)(v_rip + 11421824))) goto loc_0034AD3D;
loc_0034AB0E:
    if (result < (*(unsigned __int64 *)(v_rip + 11421824))) goto loc_0034B040;
    v_rsi = 0;
    if (condition_is_below) goto loc_0034B1E8;
loc_0034AB34:
    if ((*(unsigned int *)(v_rip + 11424714)) != 0) goto loc_0034ADEB;
loc_0034AB43:
    result = (*(unsigned __int64 *)(a1 + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 16))) & (1)) != 0) goto loc_0034AF23;
    a2 = 0;
    result = KeInvalidAccessAllowed(*(unsigned __int64 *)(a1 + 16), a2, a3, *(unsigned __int64 *)(a1));
    if ((unsigned __int8)(result) != 0) goto loc_0034AF2C;
loc_0034AB6C:
loc_0034AB6F:
    a2 = 0;
    result = memset(v_rsp - 95 - 89, a2, 128, *(unsigned __int64 *)(a1));
    *(unsigned int *)(v_rsp - 95 - 85) = 1;
    result = MiGetSystemRegionType(result, a2, 128, *(unsigned __int64 *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (64)) != 0) goto loc_0034AC97;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a1 + 16)))) != 0) goto loc_0034B028;
loc_0034ABAE:
    v_r14 = 1;
    if (0 == 0) { v_r14 = 3; }
    *(unsigned int *)(v_rsp - 95 - 85) = (unsigned int)(v_r14);
loc_0034ABB9:
    result = MiSystemVaTypeHasWsles((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, 128, *(unsigned __int64 *)(a1));
    if ((unsigned int)(result) == 0) goto loc_0034AF89;
    result = MiSystemVaTypeToVm((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, 128, *(unsigned __int64 *)(a1));
    if (result == 0) goto loc_0034B03A;
loc_0034ABDA:
    a4 = 0;
    v_stack_mC8 = v_rsp - 95 - 89;
    result = MiSynchronizeSystemVa(result, *(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if ((unsigned int)(result) == 0) goto loc_0034B073;
    result = MiCheckSystemPageTables(a1, *(unsigned __int64 *)(a1), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if (((unsigned int)(result)) == 2) goto loc_0034B06A;
    if (((unsigned int)(result)) == 1) goto loc_0034AE39;
    *(unsigned __int64 *)(a1 + 56) = v_xmm0;
    *(unsigned __int64 *)(a1 + 72) = v_xmm1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) & (1)) != 0) goto loc_0034AE7C;
    if ((*(unsigned __int64 *)(a1)) >= result) goto loc_0034AD57;
loc_0034AC51:
    if ((*(unsigned __int64 *)(a1)) < result) goto loc_0034AE49;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))) & (992);
    a1 = (condition_is_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0034ACD6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (64)) == 0) goto loc_0034B0F8;
loc_0034AC85:
loc_0034AC8A:
    result = MiUnlockSystemVa(v_rsp - 95 - 89, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    goto loc_0034AD0F;
loc_0034AC97:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 5) goto loc_0034ABB9;
    goto loc_0034B040;
loc_0034ACA6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))) < (*(unsigned __int64 *)(v_rip + 11421392))) goto loc_0034AADB;
    if (0 > a2) goto loc_0034AADB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24))) > (*(unsigned __int64 *)(v_rip + 11421386))) goto loc_0034AADB;
    goto loc_0034AADB;
loc_0034ACD6:
    if (a2 == 768) goto loc_0034AFD0;
    if (a2 == 992) goto loc_0034AFBB;
loc_0034ACEE:
    if (((*(unsigned __int8 *)(a1 + 8)) & (2)) == 0) goto loc_0034AD06;
    if (0 != 0) goto loc_0034AD06;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)))) >> (5));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_0034B27A;
loc_0034AD06:
    *(unsigned __int64 *)(a1 + 104) = 0;
loc_0034AD0F:
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 39)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    return result;
loc_0034AD3D:
    result = MiHyperSpaceSize(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11421247));
    if ((*(unsigned __int64 *)(v_stack_m28 + 56)) >= result) goto loc_0034AB0E;
    goto loc_0034ADE1;
loc_0034AD57:
    if (a2 > result) goto loc_0034AC51;
    if (0 != 0) goto loc_0034AC85;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) == 0) goto loc_0034AD90;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034AC8A;
loc_0034AD90:
    v_stack_mA0 = 9;
    result = KeBugCheckEx(80, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034ADA8:
    if ((*(unsigned __int8 *)(80)) == 7) goto loc_0034ADB6;
    if ((*(unsigned __int8 *)(80)) != 8) goto loc_0034AAEE;
loc_0034ADB6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) < 0) goto loc_0034B060;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) > a2) goto loc_0034B060;
    if ((*(unsigned __int64 *)(v_stack_m28 + 56)) > a2) goto loc_0034B04A;
loc_0034ADE1:
    goto loc_0034AD0F;
loc_0034ADEB:
    result = ExAcquireSpinLockShared(v_rip + 11424014, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    goto loc_0034AE11;
loc_0034AE02:
    if (992 > (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11424010) + 24))) goto loc_0034B22D;
    if (992 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11424010) + 24))) goto loc_0034AE16;
loc_0034AE11:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11424010)) != 0) goto loc_0034AE02;
loc_0034AE16:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11424010)) != 0) goto loc_0034B0D4;
loc_0034AE1F:
    result = MiReleaseSpinLockShared(v_rip + 11423962, (unsigned __int8)(result), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11424010)) == 0) goto loc_0034AB43;
    goto loc_0034B040;
loc_0034AE39:
    result = MiUnlockSystemVa(v_rsp - 95 - 89, (unsigned __int8)(result), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034AE42:
    result = 0;
    goto loc_0034AD0F;
loc_0034AE49:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (2)) != 0) goto loc_0034AF53;
    if (*(unsigned __int64 *)(v_rip + 11415079) == 0) goto loc_0034AE73;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (16)) != 0) goto loc_0034AF1A;
    v_r14 = ~(*(unsigned __int64 *)(v_rip + 11415079));
    v_r14 = (v_r14) & (*(unsigned __int64 *)(v_stack_m28 + 56));
loc_0034AE73:
    v_r14 = (v_r14) >> (16);
    goto loc_0034ACEE;
loc_0034AE7C:
    if (sign_flag) goto loc_0034B193;
loc_0034AE84:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) != 0) goto loc_0034B079;
loc_0034AE91:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)) & (2)) == 0) goto loc_0034AEE5;
    if (condition_is_below) goto loc_0034AEF6;
    if (condition_is_above_or_equal) goto loc_0034B144;
loc_0034AEA9:
    a4 = 0;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)) | (-1);
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = MiCopyOnWrite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), 992, a3, a4);
    result = MiUnlockSystemVa(v_rsp - 95 - 89, 992, a3, a4);
    if (!sign_flag) goto loc_0034AE42;
    a3 = 0;
    result = MiCopyOnWriteCheckConditions(768, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a3, a4);
    goto loc_0034AE42;
loc_0034AEE5:
    result = MiCheckSystemNxFault(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(result)), 2, a4);
loc_0034AEF6:
    v_stack_m98 = (unsigned int)((unsigned int)(result));
    v_stack_mA0 = 1;
    result = MiNoFaultFound(*(unsigned __int64 *)(v_stack_m28 + 72), 992, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    goto loc_0034AC8A;
loc_0034AF1A:
    v_r14 = (v_r14) & (-17);
    goto loc_0034AE73;
loc_0034AF23:
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_0034B220;
loc_0034AF2C:
    goto loc_0034AB6F;
loc_0034AF34:
    v_stack_mA0 = 14;
    result = KeBugCheckEx(80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034AF53:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) != 0) goto loc_0034B200;
loc_0034AF5F:
    a4 = 0;
    a3 = 0;
    result = MiResolveDemandZeroFault(*(unsigned __int64 *)(v_stack_m28 + 72), 992, a3, a4);
    *(unsigned __int64 *)(v_rsp - 95 - 65) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 95 - 49) = v_xmm1;
    goto loc_0034AC8A;
loc_0034AF89:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 13) goto loc_0034B17D;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) == 0) goto loc_0034B03A;
    if ((*(unsigned __int8 *)(a1)) != 4) goto loc_0034B0C6;
loc_0034AFAF:
    goto loc_0034ABDA;
loc_0034AFBB:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) == 0) goto loc_0034AFD0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 4) goto loc_0034ACEE;
loc_0034AFD0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80)))) & (64)) != 0) goto loc_0034AFFB;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) == 0) goto loc_0034B266;
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034AFFB;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) != 6) goto loc_0034B258;
loc_0034AFFB:
    result = ((unsigned int)((unsigned int)(result))) & (992);
    if (result == (v_rip + 11457418)) goto loc_0034AC85;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) == 0) goto loc_0034AC85;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034ACEE;
    goto loc_0034AC85;
loc_0034B028:
    result = (result) & (-2);
    if ((*(unsigned __int8 *)(result)) != ((unsigned __int8)(v_r14))) goto loc_0034ABAE;
    goto loc_0034ABB9;
loc_0034B03A:
    if ((((unsigned __int8)(v_r14)) & (2)) != 0) goto loc_0034B09D;
loc_0034B040:
    goto loc_0034AD0F;
loc_0034B04A:
    if (((unsigned int)((unsigned int)(result))) < (*(unsigned __int64 *)(v_rip + 11420463))) goto loc_0034B060;
    if (((unsigned int)((unsigned int)(result))) <= (*(unsigned __int64 *)(v_rip + 11420470))) goto loc_0034ADE1;
loc_0034B060:
    goto loc_0034AD0F;
loc_0034B06A:
    result = MiUnlockSystemVa(v_rsp - 95 - 89, 992, a3, a4);
loc_0034B073:
    goto loc_0034B03A;
loc_0034B079:
    a2 = (992) & (-2);
    if ((*(unsigned __int8 *)(a2)) != 1) goto loc_0034AE91;
    a3 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 80))) & (7));
    result = MiUpdatePfnForPrefetchByPte(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24), a2, a3, a4);
    goto loc_0034AC8A;
loc_0034B09D:
    result = MiGenerateAccessViolation(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0034B040;
    v_stack_mA0 = 2;
    result = KeBugCheckEx(result + 80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034B0C6:
    if ((*(unsigned __int8 *)(result + 80)) == 1) goto loc_0034AFAF;
    goto loc_0034B03A;
loc_0034B0D4:
    v_r12 = (v_rip + 11457418) >> (9);
    v_r12 = (v_r12) & (result);
    v_r12 = (v_r12) + (1);
    v_r14 = (unsigned int)(*(unsigned int *)(v_rsp - 95 - 85));
    if ((*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(v_rsp - 95 - 85)) + 40)) != v_r12) { v_r14 = (unsigned int)((unsigned int)(result)); }
    goto loc_0034AE1F;
loc_0034B0F8:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16))) & (1)) != 0) goto loc_0034B236;
    a2 = 0;
    result = KeInvalidAccessAllowed(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if ((unsigned __int8)(result) != 0) goto loc_0034AC85;
loc_0034B11B:
    result = MiGenerateAccessViolation(*(unsigned __int64 *)(v_stack_m28 + 72), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if ((unsigned int)(result) != 0) goto loc_0034AC85;
    v_stack_mA0 = (unsigned int)((unsigned int)(result));
    result = KeBugCheckEx(result + 80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034B144:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80)))) & (64)) != 0) goto loc_0034AEA9;
    result = MiGenerateAccessViolation(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if ((unsigned int)(result) != 0) goto loc_0034AC85;
    v_stack_mA0 = 11;
    result = KeBugCheckEx(190, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034B17D:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 8) goto loc_0034B03A;
    goto loc_0034ABDA;
loc_0034B193:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72))) < result) goto loc_0034AE84;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72))) > result) goto loc_0034AE84;
    if (((*(unsigned __int8 *)(v_rsp - 95 - 85)) & (2)) == 0) goto loc_0034AC85;
    v_stack_mA0 = 8;
    result = KeBugCheckEx(80, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
loc_0034B1E8:
    result = MiTransientPageListWriter(992, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if ((unsigned int)(result) == 0) goto loc_0034AB34;
    goto loc_0034B040;
loc_0034B200:
    result = (result) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034AC8A;
    goto loc_0034AF5F;
loc_0034B212:
    if (992 != 6) goto loc_0034AB6C;
    goto loc_0034AF2C;
loc_0034B220:
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 992) goto loc_0034AF2C;
    goto loc_0034B212;
loc_0034B22D:
    goto loc_0034AE11;
loc_0034B236:
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034AC85;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 3) goto loc_0034AC85;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 6) goto loc_0034AC85;
    goto loc_0034B11B;
loc_0034B258:
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 3) goto loc_0034AFFB;
loc_0034B266:
    a2 = 0;
    result = KeInvalidAccessAllowed(*(unsigned __int8 *)(result), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16));
    if ((unsigned __int8)(result) != 0) goto loc_0034AFFB;
loc_0034B27A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 80)))) & (64)) != 0) goto loc_0034AC85;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16)) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_0034AC85;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 3) goto loc_0034AC85;
    if (((unsigned __int8)(*(unsigned __int8 *)(result))) == 6) goto loc_0034AC85;
}
```

## 5. (Beta) C Style

```c
int64_t MiSystemFault(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mC8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0xABFCB2)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
    if (condition_is_below) goto loc_0034B040;
    if (sign_flag) goto loc_0034AF34;
    result = MiGetLeafVa(*(uint64_t *)(arg1), a2, a3, *(uint64_t *)(arg1));
    if ((*(uint64_t *)(arg1)) >= local_r13) goto loc_0034ACA6;
loc_0034AADB:
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_0034ADA8;
loc_0034AAEE:
    if (result < (*(uint64_t *)(arg1 + 0x10))) goto loc_0034ADE1;
    if (result >= (*(uint64_t *)(v_rip + 0xAE4880))) goto loc_0034AD3D;
loc_0034AB0E:
    if (result < (*(uint64_t *)(v_rip + 0xAE4880))) goto loc_0034B040;
    local_rsi = 0;
    if (condition_is_below) goto loc_0034B1E8;
loc_0034AB34:
    if ((*(uint32_t *)(v_rip + 0xAE53CA)) != 0) goto loc_0034ADEB;
loc_0034AB43:
    result = (*(uint64_t *)(arg1 + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x10))) & (1)) != 0) goto loc_0034AF23;
    a2 = 0;
    result = KeInvalidAccessAllowed(*(uint64_t *)(arg1 + 0x10), a2, a3, *(uint64_t *)(arg1));
    if ((uint8_t)(result) != 0) goto loc_0034AF2C;
loc_0034AB6C:
loc_0034AB6F:
    a2 = 0;
    result = memset(local_rsp - 95 - 89, a2, 128, *(uint64_t *)(arg1));
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = 1;
    result = MiGetSystemRegionType(result, a2, 128, *(uint64_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (64)) != 0) goto loc_0034AC97;
    if (((1) & ((uint8_t)(*(uint64_t *)(arg1 + 0x10)))) != 0) goto loc_0034B028;
loc_0034ABAE:
    local_r14 = 1;
    if (0 == 0) { local_r14 = 3; }
    *(uint32_t *)(local_rsp - 0x5F - 0x55) = (uint32_t)(local_r14);
loc_0034ABB9:
    result = MiSystemVaTypeHasWsles((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a2, 128, *(uint64_t *)(arg1));
    if ((uint32_t)(result) == 0) goto loc_0034AF89;
    result = MiSystemVaTypeToVm((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a2, 128, *(uint64_t *)(arg1));
    if (result == 0) goto loc_0034B03A;
loc_0034ABDA:
    a4 = 0;
    v_stack_mC8 = local_rsp - 95 - 89;
    result = MiSynchronizeSystemVa(result, *(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    if ((uint32_t)(result) == 0) goto loc_0034B073;
    result = MiCheckSystemPageTables(Arg1, *(uint64_t *)(arg1), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    if (((uint32_t)(result)) == 2) goto loc_0034B06A;
    if (((uint32_t)(result)) == 1) goto loc_0034AE39;
    *(uint64_t *)(arg1 + 0x38) = v_xmm0;
    *(uint64_t *)(arg1 + 0x48) = v_xmm1;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) & (1)) != 0) goto loc_0034AE7C;
    if ((*(uint64_t *)(arg1)) >= result) goto loc_0034AD57;
loc_0034AC51:
    if ((*(uint64_t *)(arg1)) < result) goto loc_0034AE49;
    a2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))) & (992);
    Arg1 = (condition_is_equal) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0034ACD6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (64)) == 0) goto loc_0034B0F8;
loc_0034AC85:
loc_0034AC8A:
    result = MiUnlockSystemVa(local_rsp - 95 - 89, a2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    goto loc_0034AD0F;
loc_0034AC97:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 5) goto loc_0034ABB9;
    goto loc_0034B040;
loc_0034ACA6:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))) < (*(uint64_t *)(v_rip + 0xAE46D0))) goto loc_0034AADB;
    if (0 > a2) goto loc_0034AADB;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18))) > (*(uint64_t *)(v_rip + 0xAE46CA))) goto loc_0034AADB;
    goto loc_0034AADB;
loc_0034ACD6:
    if (a2 == 768) goto loc_0034AFD0;
    if (a2 == 992) goto loc_0034AFBB;
loc_0034ACEE:
    if (((*(uint8_t *)(arg1 + 0x8)) & (2)) == 0) goto loc_0034AD06;
    if (0 != 0) goto loc_0034AD06;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)))) >> (5));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_0034B27A;
loc_0034AD06:
    *(uint64_t *)(arg1 + 0x68) = 0;
loc_0034AD0F:
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x27)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    return result;
loc_0034AD3D:
    result = MiHyperSpaceSize(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAE463F));
    if ((*(uint64_t *)(v_stack_m28 + 0x38)) >= result) goto loc_0034AB0E;
    goto loc_0034ADE1;
loc_0034AD57:
    if (a2 > result) goto loc_0034AC51;
    if (0 != 0) goto loc_0034AC85;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) == 0) goto loc_0034AD90;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_0034AC8A;
loc_0034AD90:
    v_stack_mA0 = 9;
    result = KeBugCheckEx(80, a2, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034ADA8:
    if ((*(uint8_t *)(80)) == 7) goto loc_0034ADB6;
    if ((*(uint8_t *)(80)) != 8) goto loc_0034AAEE;
loc_0034ADB6:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) < 0) goto loc_0034B060;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) > a2) goto loc_0034B060;
    if ((*(uint64_t *)(v_stack_m28 + 0x38)) > a2) goto loc_0034B04A;
loc_0034ADE1:
    goto loc_0034AD0F;
loc_0034ADEB:
    result = ExAcquireSpinLockShared(v_rip + 11424014, a2, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    goto loc_0034AE11;
loc_0034AE02:
    if (992 > (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE510A) + 0x18))) goto loc_0034B22D;
    if (992 >= (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE510A) + 0x18))) goto loc_0034AE16;
loc_0034AE11:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE510A)) != 0) goto loc_0034AE02;
loc_0034AE16:
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE510A)) != 0) goto loc_0034B0D4;
loc_0034AE1F:
    result = MiReleaseSpinLockShared(v_rip + 11423962, (uint8_t)(result), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAE510A)) == 0) goto loc_0034AB43;
    goto loc_0034B040;
loc_0034AE39:
    result = MiUnlockSystemVa(local_rsp - 95 - 89, (uint8_t)(result), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034AE42:
    result = 0;
    goto loc_0034AD0F;
loc_0034AE49:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38))) & (2)) != 0) goto loc_0034AF53;
    if (*(uint64_t *)(v_rip + 0xAE2E27) == 0) goto loc_0034AE73;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38))) & (16)) != 0) goto loc_0034AF1A;
    local_r14 = ~(*(uint64_t *)(v_rip + 0xAE2E27));
    local_r14 = (local_r14) & (*(uint64_t *)(v_stack_m28 + 0x38));
loc_0034AE73:
    local_r14 = (local_r14) >> (16);
    goto loc_0034ACEE;
loc_0034AE7C:
    if (sign_flag) goto loc_0034B193;
loc_0034AE84:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) != 0) goto loc_0034B079;
loc_0034AE91:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)) & (2)) == 0) goto loc_0034AEE5;
    if (condition_is_below) goto loc_0034AEF6;
    if (condition_is_above_or_equal) goto loc_0034B144;
loc_0034AEA9:
    a4 = 0;
    a3 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)) | (-1);
    v_stack_mA0 = *(uint64_t *)(v_stack_m28 + 0x40);
    result = MiCopyOnWrite(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), 992, a3, a4);
    result = MiUnlockSystemVa(local_rsp - 95 - 89, 992, a3, a4);
    if (!sign_flag) goto loc_0034AE42;
    a3 = 0;
    result = MiCopyOnWriteCheckConditions(768, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a3, a4);
    goto loc_0034AE42;
loc_0034AEE5:
    result = MiCheckSystemNxFault(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(result)), 2, a4);
loc_0034AEF6:
    v_stack_m98 = (uint32_t)((uint32_t)(result));
    v_stack_mA0 = 1;
    result = MiNoFaultFound(*(uint64_t *)(v_stack_m28 + 0x48), 992, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    goto loc_0034AC8A;
loc_0034AF1A:
    local_r14 = (local_r14) & (-17);
    goto loc_0034AE73;
loc_0034AF23:
    if ((*(uint8_t *)(result)) != 1) goto loc_0034B220;
loc_0034AF2C:
    goto loc_0034AB6F;
loc_0034AF34:
    v_stack_mA0 = 14;
    result = KeBugCheckEx(80, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034AF53:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) != 0) goto loc_0034B200;
loc_0034AF5F:
    a4 = 0;
    a3 = 0;
    result = MiResolveDemandZeroFault(*(uint64_t *)(v_stack_m28 + 0x48), 992, a3, a4);
    *(uint64_t *)(local_rsp - 0x5F - 0x41) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F - 0x31) = v_xmm1;
    goto loc_0034AC8A;
loc_0034AF89:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 13) goto loc_0034B17D;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) == 0) goto loc_0034B03A;
    if ((*(uint8_t *)(arg1)) != 4) goto loc_0034B0C6;
loc_0034AFAF:
    goto loc_0034ABDA;
loc_0034AFBB:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) == 0) goto loc_0034AFD0;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 4) goto loc_0034ACEE;
loc_0034AFD0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50)))) & (64)) != 0) goto loc_0034AFFB;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) == 0) goto loc_0034B266;
    if ((*(uint8_t *)(result)) == 1) goto loc_0034AFFB;
    if (((uint8_t)(*(uint8_t *)(result))) != 6) goto loc_0034B258;
loc_0034AFFB:
    result = ((uint32_t)((uint32_t)(result))) & (992);
    if (result == (v_rip + 11457418)) goto loc_0034AC85;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) == 0) goto loc_0034AC85;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_0034ACEE;
    goto loc_0034AC85;
loc_0034B028:
    result = (result) & (-2);
    if ((*(uint8_t *)(result)) != ((uint8_t)(local_r14))) goto loc_0034ABAE;
    goto loc_0034ABB9;
loc_0034B03A:
    if ((((uint8_t)(local_r14)) & (2)) != 0) goto loc_0034B09D;
loc_0034B040:
    goto loc_0034AD0F;
loc_0034B04A:
    if (((uint32_t)((uint32_t)(result))) < (*(uint64_t *)(v_rip + 0xAE432F))) goto loc_0034B060;
    if (((uint32_t)((uint32_t)(result))) <= (*(uint64_t *)(v_rip + 0xAE4336))) goto loc_0034ADE1;
loc_0034B060:
    goto loc_0034AD0F;
loc_0034B06A:
    result = MiUnlockSystemVa(local_rsp - 95 - 89, 992, a3, a4);
loc_0034B073:
    goto loc_0034B03A;
loc_0034B079:
    a2 = (992) & (-2);
    if ((*(uint8_t *)(a2)) != 1) goto loc_0034AE91;
    a3 = 0;
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(a2 + 0x50))) & (7));
    result = MiUpdatePfnForPrefetchByPte(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18), a2, a3, a4);
    goto loc_0034AC8A;
loc_0034B09D:
    result = MiGenerateAccessViolation(*(uint64_t *)(v_stack_m28 + 0x48), a2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0034B040;
    v_stack_mA0 = 2;
    result = KeBugCheckEx(result + 80, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034B0C6:
    if ((*(uint8_t *)(result + 0x50)) == 1) goto loc_0034AFAF;
    goto loc_0034B03A;
loc_0034B0D4:
    local_r12 = (v_rip + 11457418) >> (9);
    local_r12 = (local_r12) & (result);
    local_r12 = (local_r12) + (1);
    local_r14 = (uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55));
    if ((*(uint64_t *)((uint32_t)(*(uint32_t *)(local_rsp - 0x5F - 0x55)) + 0x28)) != local_r12) { local_r14 = (uint32_t)((uint32_t)(result)); }
    goto loc_0034AE1F;
loc_0034B0F8:
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10))) & (1)) != 0) goto loc_0034B236;
    a2 = 0;
    result = KeInvalidAccessAllowed(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10), a2, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if ((uint8_t)(result) != 0) goto loc_0034AC85;
loc_0034B11B:
    result = MiGenerateAccessViolation(*(uint64_t *)(v_stack_m28 + 0x48), a2, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if ((uint32_t)(result) != 0) goto loc_0034AC85;
    v_stack_mA0 = (uint32_t)((uint32_t)(result));
    result = KeBugCheckEx(result + 80, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034B144:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50)))) & (64)) != 0) goto loc_0034AEA9;
    result = MiGenerateAccessViolation(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if ((uint32_t)(result) != 0) goto loc_0034AC85;
    v_stack_mA0 = 11;
    result = KeBugCheckEx(190, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), (uint32_t)((uint32_t)(result)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034B17D:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 8) goto loc_0034B03A;
    goto loc_0034ABDA;
loc_0034B193:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) < result) goto loc_0034AE84;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) > result) goto loc_0034AE84;
    if (((*(uint8_t *)(local_rsp - 0x5F - 0x55)) & (2)) == 0) goto loc_0034AC85;
    v_stack_mA0 = 8;
    result = KeBugCheckEx(80, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
loc_0034B1E8:
    result = MiTransientPageListWriter(992, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if ((uint32_t)(result) == 0) goto loc_0034AB34;
    goto loc_0034B040;
loc_0034B200:
    result = (result) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_0034AC8A;
    goto loc_0034AF5F;
loc_0034B212:
    if (992 != 6) goto loc_0034AB6C;
    goto loc_0034AF2C;
loc_0034B220:
    if (((uint8_t)(*(uint8_t *)(result))) == 992) goto loc_0034AF2C;
    goto loc_0034B212;
loc_0034B22D:
    goto loc_0034AE11;
loc_0034B236:
    if ((*(uint8_t *)(result)) == 1) goto loc_0034AC85;
    if (((uint8_t)(*(uint8_t *)(result))) == 3) goto loc_0034AC85;
    if (((uint8_t)(*(uint8_t *)(result))) == 6) goto loc_0034AC85;
    goto loc_0034B11B;
loc_0034B258:
    if (((uint8_t)(*(uint8_t *)(result))) == 3) goto loc_0034AFFB;
loc_0034B266:
    a2 = 0;
    result = KeInvalidAccessAllowed(*(uint8_t *)(result), a2, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10));
    if ((uint8_t)(result) != 0) goto loc_0034AFFB;
loc_0034B27A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x50)))) & (64)) != 0) goto loc_0034AC85;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10)) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_0034AC85;
    if (((uint8_t)(*(uint8_t *)(result))) == 3) goto loc_0034AC85;
    if (((uint8_t)(*(uint8_t *)(result))) == 6) goto loc_0034AC85;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x38` | `128` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `W` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034AA64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
