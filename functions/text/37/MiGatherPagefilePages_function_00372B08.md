# MiGatherPagefilePages

- RVA: `0x00372B08`–`0x003735AB` (길이 `2,723` bytes)
- VA: `0x0000000140372B08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007AA34`
- 디코드: `670`개 명령, `2,723/2,723` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00372C92` → [MiFillNoReservationCluster](../40/MiFillNoReservationCluster_function_00405B40.md) (function, `0x00405B40`)
- `0x00372CC4` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00372D0B` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00372D4E` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00372D60` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x00372D70` → [MiIsPfnOriginalPteLost](MiIsPfnOriginalPteLost_function_00373B5C.md) (function, `0x00373B5C`)
- `0x00372D94` → [MiSetStoreVirtualPagefileValue](MiSetStoreVirtualPagefileValue_function_00373B80.md) (function, `0x00373B80`)
- `0x00372DC7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00372EBA` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x00372EDB` → [MI_PAGEFILE_WRITE](../47/MI_PAGEFILE_WRITE_function_004749F4.md) (function, `0x004749F4`)
- `0x00372F37` → [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) (function, `0x002B46C4`)
- `0x00372F73` → [MiUpdatePfnBackingStore](../44/MiUpdatePfnBackingStore_function_004442B4.md) (function, `0x004442B4`)
- `0x00372FA2` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00372FB9` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00372FF9` → [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) (function, `0x004071A0`)
- `0x00373031` → [MiFindPageFileWriteCluster](../3E/MiFindPageFileWriteCluster_function_003E2B00.md) (function, `0x003E2B00`)
- `0x00373088` → [MiMapPageFileHash](../49/MiMapPageFileHash_function_004921E0.md) (function, `0x004921E0`)
- `0x003730E4` → [IoAsynchronousPageWrite](../29/IoAsynchronousPageWrite_function_00299C08.md) (function, `0x00299C08`)
- `0x00373128` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x0037315C` → [MiMakePageFilePte](../38/MiMakePageFilePte_function_003823C8.md) (function, `0x003823C8`)
- `0x00373185` → [MiFindFreePageFileSpace](../3E/MiFindFreePageFileSpace_function_003E2CAC.md) (function, `0x003E2CAC`)
- `0x003731C2` → [MiUpdatePagefilePeakUsage](../2B/MiUpdatePagefilePeakUsage_function_002B54BC.md) (function, `0x002B54BC`)
- `0x003731D1` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x003731E4` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00373212` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0037323E` → [MiIsStoreVirtualPagefileFull](../4A/MiIsStoreVirtualPagefileFull_function_004ACB9C.md) (function, `0x004ACB9C`)
- `0x0037327B` → [MiPageFileNoFreeSpace](../47/MiPageFileNoFreeSpace_function_0047E45C.md) (function, `0x0047E45C`)
- `0x003732BC` → [MiPageFileLargestBitmapsRun](../2A/MiPageFileLargestBitmapsRun_function_002AA708.md) (function, `0x002AA708`)
- `0x00373301` → [MiMakePagefileWriterEntryAvailable](../47/MiMakePagefileWriterEntryAvailable_function_0047EE78.md) (function, `0x0047EE78`)
- `0x00373326` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0037335C` → [MiWriteComplete](../40/MiWriteComplete_function_004069B0.md) (function, `0x004069B0`)
- `0x00373371` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x003733AD` → [MiSetPageFileAllocationBits](../3E/MiSetPageFileAllocationBits_function_003E1D8C.md) (function, `0x003E1D8C`)
- `0x003733FA` → [MiInvalidatePageFileBitmapsCache](../3E/MiInvalidatePageFileBitmapsCache_function_003E3240.md) (function, `0x003E3240`)
- `0x00373466` → [MiPageFileNoFreeSpace](../47/MiPageFileNoFreeSpace_function_0047E45C.md) (function, `0x0047E45C`)
- `0x00373475` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0037349E` → [RtlFindLongestRunClearCapped](../47/RtlFindLongestRunClearCapped_function_0047BC5C.md) (function, `0x0047BC5C`)
- `0x003734B1` → [MiSetPageFileAllocationBits](../3E/MiSetPageFileAllocationBits_function_003E1D8C.md) (function, `0x003E1D8C`)
- `0x003734E2` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00373561` → [MiTransferMemoryPagefileData](../4D/MiTransferMemoryPagefileData_function_004DB6FC.md) (function, `0x004DB6FC`)
- `0x00373593` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x003735A1` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)

### Direct callers
- [MiModifiedPageWriter](../47/MiModifiedPageWriter_function_0047E5F0.md) at `0x0047E8D2`

### Static image references
- `0x00372C14` → RVA `0x00FC520C` (`ALMOSTRO`; read)
- `0x00372D33` → RVA `0x00E37478` (`.data`; read)
- `0x00372DB8` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x003730D4` → RVA `0x004069B0` (`MiWriteComplete`; read)
- `0x00373195` → RVA `0x00E2DC80` (`.data`; read)
- `0x003734D9` → RVA `0x00011C80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0037350E` → [sub_006E3DF6](../6E/Unknown_function_006E3DF6.md) (`tail-transfer`)
  - `0x00373588` → [sub_006E3DF6 + 0x7A](../6E/Unknown_function_006E3DF6.md) (`tail-transfer`)
  - `0x00373599` → [sub_006E3DF6 + 0x7A](../6E/Unknown_function_006E3DF6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00372B08  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00372B0D  55                              push rbp
00372B0E  53                              push rbx
00372B0F  56                              push rsi
00372B10  57                              push rdi
00372B11  41 54                           push r12
00372B13  41 55                           push r13
00372B15  41 56                           push r14
00372B17  41 57                           push r15
00372B19  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00372B1E  48 81 EC F8 00 00 00            sub rsp, 0xf8
00372B25  4C 8B 79 40                     mov r15, qword ptr [rcx + 0x40]
00372B29  45 33 DB                        xor r11d, r11d
00372B2C  4C 8B E1                        mov r12, rcx
00372B2F  44 89 5D 93                     mov dword ptr [rbp - 0x6d], r11d
00372B33  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00372B3C  41 8B FB                        mov edi, r11d
00372B3F  4C 89 7D AF                     mov qword ptr [rbp - 0x51], r15
00372B43  4D 8B AF D8 00 00 00            mov r13, qword ptr [r15 + 0xd8]
00372B4A  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00372B4E  4C 89 6D BF                     mov qword ptr [rbp - 0x41], r13
00372B52  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00372B56  85 C0                           test eax, eax
00372B58  0F 84 17 07 00 00               je 0x140373275
00372B5E  49 8D 44 24 68                  lea rax, [r12 + 0x68]
00372B63  4C 89 18                        mov qword ptr [rax], r11
00372B66  41 8D 5B 30                     lea ebx, [r11 + 0x30]
00372B6A  C7 40 08 30 00 02 00            mov dword ptr [rax + 8], 0x20030
00372B71  8D 53 D2                        lea edx, [rbx - 0x2e]
00372B74  4C 89 58 20                     mov qword ptr [rax + 0x20], r11
00372B78  4C 89 58 28                     mov qword ptr [rax + 0x28], r11
00372B7C  41 0F B7 8F AC 00 00 00         movzx ecx, word ptr [r15 + 0xac]
00372B84  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
00372B88  48 03 C3                        add rax, rbx
00372B8B  48 89 45 87                     mov qword ptr [rbp - 0x79], rax
00372B8F  8B C1                           mov eax, ecx
00372B91  83 E0 0F                        and eax, 0xf
00372B94  48 03 C3                        add rax, rbx
00372B97  4C 6B D0 58                     imul r10, rax, 0x58
00372B9B  F6 C1 40                        test cl, 0x40
00372B9E  0F 84 28 04 00 00               je 0x140372fcc
00372BA4  4B 8B 34 2A                     mov rsi, qword ptr [r10 + r13]
00372BA8  45 8B D3                        mov r10d, r11d
00372BAB  48 8B C6                        mov rax, rsi
00372BAE  4C 89 5D 77                     mov qword ptr [rbp + 0x77], r11
00372BB2  48 F7 D8                        neg rax
00372BB5  1B FF                           sbb edi, edi
00372BB7  23 FA                           and edi, edx
00372BB9  48 85 F6                        test rsi, rsi
00372BBC  75 29                           jne 0x140372be7
00372BBE  45 39 9D B0 04 00 00            cmp dword ptr [r13 + 0x4b0], r11d
00372BC5  0F 85 CD 03 00 00               jne 0x140372f98
00372BCB  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
00372BD3  0F 84 52 06 00 00               je 0x14037322b
00372BD9  49 8B B5 00 10 00 00            mov rsi, qword ptr [r13 + 0x1000]
00372BE0  48 85 F6                        test rsi, rsi
00372BE3  74 02                           je 0x140372be7
00372BE5  8B FA                           mov edi, edx
00372BE7  4D 85 D2                        test r10, r10
00372BEA  0F 84 91 03 00 00               je 0x140372f81
00372BF0  41 8B 8D B4 04 00 00            mov ecx, dword ptr [r13 + 0x4b4]
00372BF7  8B C7                           mov eax, edi
00372BF9  83 C8 04                        or eax, 4
00372BFC  41 BE 01 00 00 00               mov r14d, 1
00372C02  83 F9 FF                        cmp ecx, -1
00372C05  0F 45 F8                        cmovne edi, eax
00372C08  89 7D 6F                        mov dword ptr [rbp + 0x6f], edi
00372C0B  40 84 FA                        test dl, dil
00372C0E  0F 84 71 06 00 00               je 0x140373285
00372C14  8B 1D F2 25 C5 00               mov ebx, dword ptr [rip + 0xc525f2]
00372C1A  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00372C1D  40 84 FA                        test dl, dil
00372C20  0F 85 B3 03 00 00               jne 0x140372fd9
00372C26  33 C9                           xor ecx, ecx
00372C28  41 38 8D 18 04 00 00            cmp byte ptr [r13 + 0x418], cl
00372C2F  0F 85 A6 05 00 00               jne 0x1403731db
00372C35  41 8B 44 24 28                  mov eax, dword ptr [r12 + 0x28]
00372C3A  24 1C                           and al, 0x1c
00372C3C  3C 08                           cmp al, 8
00372C3E  0F 82 CD 03 00 00               jb 0x140373011
00372C44  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00372C48  83 C8 FF                        or eax, 0xffffffff
00372C4B  41 0B FE                        or edi, r14d
00372C4E  66 01 86 E4 01 00 00            add word ptr [rsi + 0x1e4], ax
00372C55  90                              nop
00372C56  40 84 FA                        test dl, dil
00372C59  0F 84 88 03 00 00               je 0x140372fe7
00372C5F  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
00372C67  89 4D 77                        mov dword ptr [rbp + 0x77], ecx
00372C6A  0F 84 B3 03 00 00               je 0x140373023
00372C70  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00372C74  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
00372C78  41 3B C1                        cmp eax, r9d
00372C7B  44 0F 42 C8                     cmovb r9d, eax
00372C7F  45 85 C9                        test r9d, r9d
00372C82  0F 84 D8 07 00 00               je 0x140373460
00372C88  4C 8B 45 87                     mov r8, qword ptr [rbp - 0x79]
00372C8C  49 8B D7                        mov rdx, r15
00372C8F  49 8B CD                        mov rcx, r13
00372C92  E8 A9 2E 09 00                  call 0x140405b40
00372C97  8B 5D 77                        mov ebx, dword ptr [rbp + 0x77]
00372C9A  8B F0                           mov esi, eax
00372C9C  89 45 A3                        mov dword ptr [rbp - 0x5d], eax
00372C9F  85 F6                           test esi, esi
00372CA1  0F 84 4A 06 00 00               je 0x1403732f1
00372CA7  FF C8                           dec eax
00372CA9  89 75 7F                        mov dword ptr [rbp + 0x7f], esi
00372CAC  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
00372CB4  89 45 8F                        mov dword ptr [rbp - 0x71], eax
00372CB7  89 45 93                        mov dword ptr [rbp - 0x6d], eax
00372CBA  0F 84 61 04 00 00               je 0x140373121
00372CC0  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00372CC4  E8 27 C3 EE FF                  call 0x14025eff0
00372CC9  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00372CCC  83 E7 FE                        and edi, 0xfffffffe
00372CCF  89 7D A7                        mov dword ptr [rbp - 0x59], edi
00372CD2  3B CE                           cmp ecx, esi
00372CD4  0F 85 14 08 00 00               jne 0x1403734ee
00372CDA  8B 75 8F                        mov esi, dword ptr [rbp - 0x71]
00372CDD  89 4D 7F                        mov dword ptr [rbp + 0x7f], ecx
00372CE0  49 8D 44 24 68                  lea rax, [r12 + 0x68]
00372CE5  C1 E1 0C                        shl ecx, 0xc
00372CE8  89 48 28                        mov dword ptr [rax + 0x28], ecx
00372CEB  48 83 C0 30                     add rax, 0x30
00372CEF  41 89 4C 24 2C                  mov dword ptr [r12 + 0x2c], ecx
00372CF4  33 C9                           xor ecx, ecx
00372CF6  41 89 74 24 30                  mov dword ptr [r12 + 0x30], esi
00372CFB  44 8B E1                        mov r12d, ecx
00372CFE  89 4D 6F                        mov dword ptr [rbp + 0x6f], ecx
00372D01  48 8B 08                        mov rcx, qword ptr [rax]
00372D04  89 5D 8F                        mov dword ptr [rbp - 0x71], ebx
00372D07  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
00372D0B  E8 C0 5F FC FF                  call 0x140338cd0
00372D10  48 8B 7D AF                     mov rdi, qword ptr [rbp - 0x51]
00372D14  41 8D 34 06                     lea esi, [r14 + rax]
00372D18  48 8B 17                        mov rdx, qword ptr [rdi]
00372D1B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00372D25  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00372D29  48 C1 E1 04                     shl rcx, 4
00372D2D  48 8B C0                        mov rax, rax
00372D30  48 03 C8                        add rcx, rax
00372D33  48 3B 15 3E 47 AC 00            cmp rdx, qword ptr [rip + 0xac473e]
00372D3A  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
00372D3E  0F 84 93 00 00 00               je 0x140372dd7
00372D44  45 33 E4                        xor r12d, r12d
00372D47  85 F6                           test esi, esi
00372D49  74 15                           je 0x140372d60
00372D4B  48 8B CA                        mov rcx, rdx
00372D4E  E8 7D 5F FC FF                  call 0x140338cd0
00372D53  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
00372D57  41 03 C6                        add eax, r14d
00372D5A  3B F0                           cmp esi, eax
00372D5C  41 0F 45 F4                     cmovne esi, r12d
00372D60  E8 DB 75 FA FF                  call 0x14031a340
00372D65  4C 8B 5D 87                     mov r11, qword ptr [rbp - 0x79]
00372D69  49 8B CB                        mov rcx, r11
00372D6C  44 0F B6 E0                     movzx r12d, al
00372D70  E8 E7 0D 00 00                  call 0x140373b5c
00372D75  33 C9                           xor ecx, ecx
00372D77  85 C0                           test eax, eax
00372D79  75 28                           jne 0x140372da3
00372D7B  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
00372D83  0F 84 E1 01 00 00               je 0x140372f6a
00372D89  49 8B 53 10                     mov rdx, qword ptr [r11 + 0x10]
00372D8D  44 8D 41 04                     lea r8d, [rcx + 4]
00372D91  49 8B CD                        mov rcx, r13
00372D94  E8 E7 0D 00 00                  call 0x140373b80
00372D99  4C 8B 5D 87                     mov r11, qword ptr [rbp - 0x79]
00372D9D  49 89 43 10                     mov qword ptr [r11 + 0x10], rax
00372DA1  33 C9                           xor ecx, ecx
00372DA3  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00372DAD  F0 49 21 43 18                  lock and qword ptr [r11 + 0x18], rax
00372DB2  41 80 FC 02                     cmp r12b, 2
00372DB6  73 18                           jae 0x140372dd0
00372DB8  39 0D 62 3F C5 00               cmp dword ptr [rip + 0xc53f62], ecx
00372DBE  74 0C                           je 0x140372dcc
00372DC0  44 0F 20 C1                     mov rcx, cr8
00372DC4  41 8A D4                        mov dl, r12b
00372DC7  E8 CC 28 18 00                  call 0x1404f5698
00372DCC  45 0F 22 C4                     mov cr8, r12
00372DD0  44 8B 65 6F                     mov r12d, dword ptr [rbp + 0x6f]
00372DD4  8B 5D 77                        mov ebx, dword ptr [rbp + 0x77]
00372DD7  45 03 E6                        add r12d, r14d
00372DDA  41 03 DE                        add ebx, r14d
00372DDD  48 83 C7 08                     add rdi, 8
00372DE1  44 89 65 6F                     mov dword ptr [rbp + 0x6f], r12d
00372DE5  89 5D 77                        mov dword ptr [rbp + 0x77], ebx
00372DE8  44 3B 65 7F                     cmp r12d, dword ptr [rbp + 0x7f]
00372DEC  0F 82 26 FF FF FF               jb 0x140372d18
00372DF2  0F B7 05 13 24 C5 00            movzx eax, word ptr [rip + 0xc52413]
00372DF9  49 B8 B0 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003b0
00372E03  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00372E07  66 83 C0 06                     add ax, 6
00372E0B  8B 7D A7                        mov edi, dword ptr [rbp - 0x59]
00372E0E  49 B9 08 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000008
00372E18  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
00372E1C  66 C1 E0 03                     shl ax, 3
00372E20  66 89 41 08                     mov word ptr [rcx + 8], ax
00372E24  49 8B 10                        mov rdx, qword ptr [r8]
00372E27  49 8B 09                        mov rcx, qword ptr [r9]
00372E2A  49 8B 00                        mov rax, qword ptr [r8]
00372E2D  48 3B D0                        cmp rdx, rax
00372E30  75 F2                           jne 0x140372e24
00372E32  41 8B 5C 24 28                  mov ebx, dword ptr [r12 + 0x28]
00372E37  48 2B CA                        sub rcx, rdx
00372E3A  C1 EB 02                        shr ebx, 2
00372E3D  49 89 4C 24 50                  mov qword ptr [r12 + 0x50], rcx
00372E42  83 E3 07                        and ebx, 7
00372E45  41 8B 8D 8C 03 00 00            mov ecx, dword ptr [r13 + 0x38c]
00372E4C  49 8B 85 00 49 00 00            mov rax, qword ptr [r13 + 0x4900]
00372E53  85 C9                           test ecx, ecx
00372E55  0F 85 B8 06 00 00               jne 0x140373513
00372E5B  48 3D A0 00 00 00               cmp rax, 0xa0
00372E61  0F 82 1B 05 00 00               jb 0x140373382
00372E67  48 3D 20 01 00 00               cmp rax, 0x120
00372E6D  0F 82 C7 06 00 00               jb 0x14037353a
00372E73  41 8B 4C 24 28                  mov ecx, dword ptr [r12 + 0x28]
00372E78  8D 04 9D 00 00 00 00            lea eax, [rbx*4]
00372E7F  83 E1 E3                        and ecx, 0xffffffe3
00372E82  0B C8                           or ecx, eax
00372E84  41 89 4C 24 28                  mov dword ptr [r12 + 0x28], ecx
00372E89  83 FB 02                        cmp ebx, 2
00372E8C  73 31                           jae 0x140372ebf
00372E8E  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00372E92  66 44 29 B1 E6 01 00 00         sub word ptr [rcx + 0x1e6], r14w
00372E9A  90                              nop
00372E9B  45 01 B5 E4 02 00 00            add dword ptr [r13 + 0x2e4], r14d
00372EA2  90                              nop
00372EA3  66 44 01 B1 E6 01 00 00         add word ptr [rcx + 0x1e6], r14w
00372EAB  75 12                           jne 0x140372ebf
00372EAD  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
00372EB4  90                              nop
00372EB5  48 39 00                        cmp qword ptr [rax], rax
00372EB8  74 05                           je 0x140372ebf
00372EBA  E8 C1 FD F6 FF                  call 0x1402e2c80
00372EBF  49 8B 54 24 50                  mov rdx, qword ptr [r12 + 0x50]
00372EC4  44 8B CF                        mov r9d, edi
00372EC7  83 4C 24 20 FF                  or dword ptr [rsp + 0x20], 0xffffffff
00372ECC  44 8B C3                        mov r8d, ebx
00372ECF  41 D1 E9                        shr r9d, 1
00372ED2  49 8B CC                        mov rcx, r12
00372ED5  41 F7 D1                        not r9d
00372ED8  45 23 CE                        and r9d, r14d
00372EDB  E8 14 1B 10 00                  call 0x1404749f4
00372EE0  41 8B 85 80 03 00 00            mov eax, dword ptr [r13 + 0x380]
00372EE7  3D 00 02 00 00                  cmp eax, 0x200
00372EEC  0F 84 12 02 00 00               je 0x140373104
00372EF2  FF C0                           inc eax
00372EF4  41 89 85 80 03 00 00            mov dword ptr [r13 + 0x380], eax
00372EFB  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00372EFE  BA 01 00 00 C0                  mov edx, 0xc0000001
00372F03  49 01 85 78 03 00 00            add qword ptr [r13 + 0x378], rax
00372F0A  4D 8D 6C 24 58                  lea r13, [r12 + 0x58]
00372F0F  44 8B 45 8F                     mov r8d, dword ptr [rbp - 0x71]
00372F13  41 83 64 24 28 BF               and dword ptr [r12 + 0x28], 0xffffffbf
00372F19  41 8B C0                        mov eax, r8d
00372F1C  48 C1 E0 0C                     shl rax, 0xc
00372F20  49 89 45 00                     mov qword ptr [r13], rax
00372F24  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
00372F2C  0F 84 0D 01 00 00               je 0x14037303f
00372F32  8B D6                           mov edx, esi
00372F34  49 8B CC                        mov rcx, r12
00372F37  E8 88 17 F4 FF                  call 0x1402b46c4
00372F3C  8B D0                           mov edx, eax
00372F3E  33 C0                           xor eax, eax
00372F40  85 D2                           test edx, edx
00372F42  0F 88 02 06 00 00               js 0x14037354a
00372F48  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
00372F4C  41 84 FE                        test r14b, dil
00372F4F  0F 85 49 06 00 00               jne 0x14037359e
00372F55  48 81 C4 F8 00 00 00            add rsp, 0xf8
00372F5C  41 5F                           pop r15
00372F5E  41 5E                           pop r14
00372F60  41 5D                           pop r13
00372F62  41 5C                           pop r12
00372F64  5F                              pop rdi
00372F65  5E                              pop rsi
00372F66  5B                              pop rbx
00372F67  5D                              pop rbp
00372F68  C3                              ret
00372F69  CC                              int3
00372F6A  44 8B C3                        mov r8d, ebx
00372F6D  49 8B D7                        mov rdx, r15
00372F70  49 8B CB                        mov rcx, r11
00372F73  E8 3C 13 0D 00                  call 0x1404442b4
00372F78  4C 8B 5D 87                     mov r11, qword ptr [rbp - 0x79]
00372F7C  E9 20 FE FF FF                  jmp 0x140372da1
00372F81  48 85 F6                        test rsi, rsi
00372F84  74 12                           je 0x140372f98
00372F86  41 F6 87 AC 00 00 00 10         test byte ptr [r15 + 0xac], 0x10
00372F8E  4C 89 55 77                     mov qword ptr [rbp + 0x77], r10
00372F92  0F 84 58 FC FF FF               je 0x140372bf0
00372F98  49 8D 9F C8 00 00 00            lea rbx, [r15 + 0xc8]
00372F9F  48 8B CB                        mov rcx, rbx
00372FA2  E8 E9 56 ED FF                  call 0x140248690
00372FA7  41 BE 01 00 00 00               mov r14d, 1
00372FAD  8A D0                           mov dl, al
00372FAF  45 08 B7 AE 00 00 00            or byte ptr [r15 + 0xae], r14b
00372FB6  48 8B CB                        mov rcx, rbx
00372FB9  E8 02 53 ED FF                  call 0x1402482c0
00372FBE  B8 11 77 88 99                  mov eax, 0x99887711
00372FC3  49 89 04 24                     mov qword ptr [r12], rax
00372FC7  E9 7C FF FF FF                  jmp 0x140372f48
00372FCC  4F 8B 14 2A                     mov r10, qword ptr [r10 + r13]
00372FD0  4C 89 55 77                     mov qword ptr [rbp + 0x77], r10
00372FD4  E9 E5 FB FF FF                  jmp 0x140372bbe
00372FD9  48 3B F3                        cmp rsi, rbx
00372FDC  0F 42 DE                        cmovb ebx, esi
00372FDF  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
00372FE2  E9 3F FC FF FF                  jmp 0x140372c26
00372FE7  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
00372FEB  4C 8D 4D 93                     lea r9, [rbp - 0x6d]
00372FEF  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
00372FF3  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
00372FF6  49 8B D7                        mov rdx, r15
00372FF9  E8 A2 41 09 00                  call 0x1404071a0
00372FFE  8B 75 7F                        mov esi, dword ptr [rbp + 0x7f]
00373001  8B D8                           mov ebx, eax
00373003  89 45 77                        mov dword ptr [rbp + 0x77], eax
00373006  8B 45 93                        mov eax, dword ptr [rbp - 0x6d]
00373009  89 75 A3                        mov dword ptr [rbp - 0x5d], esi
0037300C  E9 8E FC FF FF                  jmp 0x140372c9f
00373011  B8 00 01 00 00                  mov eax, 0x100
00373016  3B D8                           cmp ebx, eax
00373018  0F 47 D8                        cmova ebx, eax
0037301B  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
0037301E  E9 21 FC FF FF                  jmp 0x140372c44
00373023  45 33 C9                        xor r9d, r9d
00373026  4C 8D 45 6F                     lea r8, [rbp + 0x6f]
0037302A  48 8D 55 77                     lea rdx, [rbp + 0x77]
0037302E  49 8B CF                        mov rcx, r15
00373031  E8 CA FA 06 00                  call 0x1403e2b00
00373036  44 8B 4D 6F                     mov r9d, dword ptr [rbp + 0x6f]
0037303A  E9 40 FC FF FF                  jmp 0x140372c7f
0037303F  8B C7                           mov eax, edi
00373041  B9 04 00 00 00                  mov ecx, 4
00373046  24 06                           and al, 6
00373048  3A C1                           cmp al, cl
0037304A  0F 84 E2 FE FF FF               je 0x140372f32
00373050  33 C0                           xor eax, eax
00373052  41 F6 87 AC 00 00 00 40         test byte ptr [r15 + 0xac], 0x40
0037305A  0F 85 D0 02 00 00               jne 0x140373330
00373060  65 FF 04 25 AC 2E 00 00         inc dword ptr gs:[0x2eac]
00373068  49 8D 54 24 68                  lea rdx, [r12 + 0x68]
0037306D  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00373070  45 8B C8                        mov r9d, r8d
00373073  65 01 04 25 A8 2E 00 00         add dword ptr gs:[0x2ea8], eax
0037307B  45 33 C0                        xor r8d, r8d
0037307E  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
00373081  49 8B CF                        mov rcx, r15
00373084  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00373088  E8 53 F1 11 00                  call 0x1404921e0
0037308D  66 41 0F BA A7 AC 00 00 00 0B   bt word ptr [r15 + 0xac], 0xb
00373097  49 8D 74 24 18                  lea rsi, [r12 + 0x18]
0037309C  49 8D 54 24 68                  lea rdx, [r12 + 0x68]
003730A1  0F 82 AC 04 00 00               jb 0x140373553
003730A7  45 8B 8F A8 00 00 00            mov r9d, dword ptr [r15 + 0xa8]
003730AE  49 8D 44 24 10                  lea rax, [r12 + 0x10]
003730B3  49 8B 4F 18                     mov rcx, qword ptr [r15 + 0x18]
003730B7  4D 8B C5                        mov r8, r13
003730BA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003730BF  33 C0                           xor eax, eax
003730C1  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
003730C6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
003730CB  88 44 24 38                     mov byte ptr [rsp + 0x38], al
003730CF  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
003730D4  4C 8D 0D D5 38 09 00            lea r9, [rip + 0x938d5]
003730DB  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
003730DF  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
003730E4  E8 1F 6B F2 FF                  call 0x140299c08
003730E9  B9 00 00 00 C0                  mov ecx, 0xc0000000
003730EE  8B D0                           mov edx, eax
003730F0  23 C1                           and eax, ecx
003730F2  3B C1                           cmp eax, ecx
003730F4  0F 85 4E FE FF FF               jne 0x140372f48
003730FA  33 C0                           xor eax, eax
003730FC  44 8B F8                        mov r15d, eax
003730FF  E9 34 02 00 00                  jmp 0x140373338
00373104  49 8B 8D 78 03 00 00            mov rcx, qword ptr [r13 + 0x378]
0037310B  48 8B C1                        mov rax, rcx
0037310E  48 C1 E8 09                     shr rax, 9
00373112  48 2B C8                        sub rcx, rax
00373115  49 89 8D 78 03 00 00            mov qword ptr [r13 + 0x378], rcx
0037311C  E9 DA FD FF FF                  jmp 0x140372efb
00373121  49 8D 8F C8 00 00 00            lea rcx, [r15 + 0xc8]
00373128  E8 63 55 ED FF                  call 0x140248690
0037312D  88 45 6F                        mov byte ptr [rbp + 0x6f], al
00373130  40 F6 C7 02                     test dil, 2
00373134  0F 84 6B 02 00 00               je 0x1403733a5
0037313A  41 0F B7 97 AC 00 00 00         movzx edx, word ptr [r15 + 0xac]
00373142  33 C0                           xor eax, eax
00373144  0F 57 C0                        xorps xmm0, xmm0
00373147  8B CB                           mov ecx, ebx
00373149  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0037314D  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
00373151  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
00373155  89 45 D3                        mov dword ptr [rbp - 0x2d], eax
00373158  48 C1 E2 0C                     shl rdx, 0xc
0037315C  E8 67 F2 00 00                  call 0x1403823c8
00373161  49 8B 8F D8 00 00 00            mov rcx, qword ptr [r15 + 0xd8]
00373168  48 33 C2                        xor rax, rdx
0037316B  48 25 FF 0F FF FF               and rax, 0xffffffffffff0fff
00373171  44 8B C6                        mov r8d, esi
00373174  48 33 C2                        xor rax, rdx
00373177  41 B9 26 00 00 00               mov r9d, 0x26
0037317D  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00373181  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00373185  E8 22 FB 06 00                  call 0x1403e2cac
0037318A  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
0037318D  85 C0                           test eax, eax
0037318F  0F 84 EA 02 00 00               je 0x14037347f
00373195  48 8B 0D E4 AA AB 00            mov rcx, qword ptr [rip + 0xabaae4]
0037319C  48 8B 5D B7                     mov rbx, qword ptr [rbp - 0x49]
003731A0  48 8B C3                        mov rax, rbx
003731A3  48 85 C9                        test rcx, rcx
003731A6  74 0D                           je 0x1403731b5
003731A8  A8 10                           test al, 0x10
003731AA  75 09                           jne 0x1403731b5
003731AC  48 8B D9                        mov rbx, rcx
003731AF  48 F7 D3                        not rbx
003731B2  48 23 D8                        and rbx, rax
003731B5  48 C1 EB 20                     shr rbx, 0x20
003731B9  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
003731BC  89 5D 77                        mov dword ptr [rbp + 0x77], ebx
003731BF  49 8B CF                        mov rcx, r15
003731C2  E8 F5 22 F4 FF                  call 0x1402b54bc
003731C7  8A 55 6F                        mov dl, byte ptr [rbp + 0x6f]
003731CA  49 8D 8F C8 00 00 00            lea rcx, [r15 + 0xc8]
003731D1  E8 EA 50 ED FF                  call 0x1402482c0
003731D6  E9 E5 FA FF FF                  jmp 0x140372cc0
003731DB  8B F1                           mov esi, ecx
003731DD  49 8D 8D 14 04 00 00            lea rcx, [r13 + 0x414]
003731E4  E8 A7 54 ED FF                  call 0x140248690
003731E9  33 C9                           xor ecx, ecx
003731EB  8A D0                           mov dl, al
003731ED  41 38 8D 1A 04 00 00            cmp byte ptr [r13 + 0x41a], cl
003731F4  0F 85 C9 02 00 00               jne 0x1403734c3
003731FA  41 0F B6 85 18 04 00 00         movzx eax, byte ptr [r13 + 0x418]
00373202  84 C0                           test al, al
00373204  74 05                           je 0x14037320b
00373206  8B D8                           mov ebx, eax
00373208  89 45 6F                        mov dword ptr [rbp + 0x6f], eax
0037320B  49 8D 8D 14 04 00 00            lea rcx, [r13 + 0x414]
00373212  E8 A9 50 ED FF                  call 0x1402482c0
00373217  33 C9                           xor ecx, ecx
00373219  85 F6                           test esi, esi
0037321B  0F 85 B8 02 00 00               jne 0x1403734d9
00373221  BA 02 00 00 00                  mov edx, 2
00373226  E9 0A FA FF FF                  jmp 0x140372c35
0037322B  49 8B B5 80 0F 00 00            mov rsi, qword ptr [r13 + 0xf80]
00373232  48 85 F6                        test rsi, rsi
00373235  0F 85 AC F9 FF FF               jne 0x140372be7
0037323B  49 8B CD                        mov rcx, r13
0037323E  E8 59 99 13 00                  call 0x1404acb9c
00373243  8D 56 02                        lea edx, [rsi + 2]
00373246  85 C0                           test eax, eax
00373248  0F 84 99 F9 FF FF               je 0x140372be7
0037324E  41 8B 8D B4 04 00 00            mov ecx, dword ptr [r13 + 0x4b4]
00373255  48 03 CB                        add rcx, rbx
00373258  48 6B C1 58                     imul rax, rcx, 0x58
0037325C  4A 8B 34 28                     mov rsi, qword ptr [rax + r13]
00373260  48 85 F6                        test rsi, rsi
00373263  0F 85 7E F9 FF FF               jne 0x140372be7
00373269  49 8B B5 00 10 00 00            mov rsi, qword ptr [r13 + 0x1000]
00373270  E9 72 F9 FF FF                  jmp 0x140372be7
00373275  49 8B D4                        mov rdx, r12
00373278  49 8B CF                        mov rcx, r15
0037327B  E8 DC B1 10 00                  call 0x14047e45c
00373280  E9 D0 FC FF FF                  jmp 0x140372f55
00373285  48 85 F6                        test rsi, rsi
00373288  0F 84 86 F9 FF FF               je 0x140372c14
0037328E  41 F6 87 AC 00 00 00 10         test byte ptr [r15 + 0xac], 0x10
00373296  0F 85 78 F9 FF FF               jne 0x140372c14
0037329C  4D 85 D2                        test r10, r10
0037329F  0F 84 16 02 00 00               je 0x1403734bb
003732A5  45 84 B7 AF 00 00 00            test byte ptr [r15 + 0xaf], r14b
003732AC  0F 85 09 02 00 00               jne 0x1403734bb
003732B2  41 8B 5F 68                     mov ebx, dword ptr [r15 + 0x68]
003732B6  49 8B CF                        mov rcx, r15
003732B9  8B 7D 6F                        mov edi, dword ptr [rbp + 0x6f]
003732BC  E8 47 74 F3 FF                  call 0x1402aa708
003732C1  C1 EB 02                        shr ebx, 2
003732C4  3B C3                           cmp eax, ebx
003732C6  72 1F                           jb 0x1403732e7
003732C8  8B 05 3E 1F C5 00               mov eax, dword ptr [rip + 0xc51f3e]
003732CE  48 C1 E8 02                     shr rax, 2
003732D2  48 3B F0                        cmp rsi, rax
003732D5  8B C7                           mov eax, edi
003732D7  0F 83 BA 00 00 00               jae 0x140373397
003732DD  48 3B 75 77                     cmp rsi, qword ptr [rbp + 0x77]
003732E1  0F 83 B0 00 00 00               jae 0x140373397
003732E7  BA 02 00 00 00                  mov edx, 2
003732EC  E9 23 F9 FF FF                  jmp 0x140372c14
003732F1  48 8B 75 97                     mov rsi, qword ptr [rbp - 0x69]
003732F5  49 8B CC                        mov rcx, r12
003732F8  66 44 29 B6 E6 01 00 00         sub word ptr [rsi + 0x1e6], r14w
00373300  90                              nop
00373301  E8 72 BB 10 00                  call 0x14047ee78
00373306  90                              nop
00373307  66 44 01 B6 E6 01 00 00         add word ptr [rsi + 0x1e6], r14w
0037330F  0F 85 37 FC FF FF               jne 0x140372f4c
00373315  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
0037331C  90                              nop
0037331D  48 39 00                        cmp qword ptr [rax], rax
00373320  0F 84 26 FC FF FF               je 0x140372f4c
00373326  E8 55 F9 F6 FF                  call 0x1402e2c80
0037332B  E9 1C FC FF FF                  jmp 0x140372f4c
00373330  45 8B FE                        mov r15d, r14d
00373333  49 8D 74 24 18                  lea rsi, [r12 + 0x18]
00373338  89 16                           mov dword ptr [rsi], edx
0037333A  49 89 44 24 20                  mov qword ptr [r12 + 0x20], rax
0037333F  44 0F 20 C3                     mov rbx, cr8
00373343  45 0F 22 C6                     mov cr8, r14
00373347  39 05 D3 39 C5 00               cmp dword ptr [rip + 0xc539d3], eax
0037334D  0F 85 1D 01 00 00               jne 0x140373470
00373353  45 8B C7                        mov r8d, r15d
00373356  48 8B D6                        mov rdx, rsi
00373359  49 8B CC                        mov rcx, r12
0037335C  E8 4F 36 09 00                  call 0x1404069b0
00373361  33 C0                           xor eax, eax
00373363  39 05 B7 39 C5 00               cmp dword ptr [rip + 0xc539b7], eax
00373369  74 0B                           je 0x140373376
0037336B  44 0F 20 C1                     mov rcx, cr8
0037336F  8A D3                           mov dl, bl
00373371  E8 22 23 18 00                  call 0x1404f5698
00373376  0F B6 C3                        movzx eax, bl
00373379  44 0F 22 C0                     mov cr8, rax
0037337D  E9 C6 FB FF FF                  jmp 0x140372f48
00373382  41 C7 85 8C 03 00 00 20 00 00 00  mov dword ptr [r13 + 0x38c], 0x20
0037338D  BB 04 00 00 00                  mov ebx, 4
00373392  E9 DC FA FF FF                  jmp 0x140372e73
00373397  BA 02 00 00 00                  mov edx, 2
0037339C  8B F8                           mov edi, eax
0037339E  0B FA                           or edi, edx
003733A0  E9 6F F8 FF FF                  jmp 0x140372c14
003733A5  44 8B C6                        mov r8d, esi
003733A8  8B D3                           mov edx, ebx
003733AA  49 8B CF                        mov rcx, r15
003733AD  E8 DA E9 06 00                  call 0x1403e1d8c
003733B2  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
003733B6  41 83 C8 FF                     or r8d, 0xffffffff
003733BA  8B C6                           mov eax, esi
003733BC  45 8B D0                        mov r10d, r8d
003733BF  48 8D 04 C1                     lea rax, [rcx + rax*8]
003733C3  49 8D 8C 24 98 00 00 00         lea rcx, [r12 + 0x98]
003733CB  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
003733CF  48 3B C8                        cmp rcx, rax
003733D2  73 51                           jae 0x140373425
003733D4  44 8B E3                        mov r12d, ebx
003733D7  4C 8B E8                        mov r13, rax
003733DA  48 8B 05 97 40 AC 00            mov rax, qword ptr [rip + 0xac4097]
003733E1  48 39 01                        cmp qword ptr [rcx], rax
003733E4  74 56                           je 0x14037343c
003733E6  45 3B D0                        cmp r10d, r8d
003733E9  74 1F                           je 0x14037340a
003733EB  45 8B C4                        mov r8d, r12d
003733EE  45 33 C9                        xor r9d, r9d
003733F1  45 2B C2                        sub r8d, r10d
003733F4  41 8B D2                        mov edx, r10d
003733F7  49 8B CF                        mov rcx, r15
003733FA  E8 41 FE 06 00                  call 0x1403e3240
003733FF  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
00373403  41 83 C8 FF                     or r8d, 0xffffffff
00373407  45 8B D0                        mov r10d, r8d
0037340A  48 83 C1 08                     add rcx, 8
0037340E  45 03 E6                        add r12d, r14d
00373411  48 89 4D 87                     mov qword ptr [rbp - 0x79], rcx
00373415  49 3B CD                        cmp rcx, r13
00373418  72 C0                           jb 0x1403733da
0037341A  4C 8B 6D BF                     mov r13, qword ptr [rbp - 0x41]
0037341E  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
00373422  8B 75 A3                        mov esi, dword ptr [rbp - 0x5d]
00373425  41 8B 4F 68                     mov ecx, dword ptr [r15 + 0x68]
00373429  8B C1                           mov eax, ecx
0037342B  C1 E8 02                        shr eax, 2
0037342E  2B C8                           sub ecx, eax
00373430  03 4D 7F                        add ecx, dword ptr [rbp + 0x7f]
00373433  41 89 4F 68                     mov dword ptr [r15 + 0x68], ecx
00373437  E9 83 FD FF FF                  jmp 0x1403731bf
0037343C  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
00373440  41 8B D4                        mov edx, r12d
00373443  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00373447  48 0F A3 11                     bt qword ptr [rcx], rdx
0037344B  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0037344F  0F 92 C0                        setb al
00373452  84 C0                           test al, al
00373454  75 90                           jne 0x1403733e6
00373456  45 3B D0                        cmp r10d, r8d
00373459  75 AF                           jne 0x14037340a
0037345B  45 8B D4                        mov r10d, r12d
0037345E  EB AA                           jmp 0x14037340a
00373460  49 8B D4                        mov rdx, r12
00373463  49 8B CF                        mov rcx, r15
00373466  E8 F1 AF 10 00                  call 0x14047e45c
0037346B  E9 DC FA FF FF                  jmp 0x140372f4c
00373470  41 8A D6                        mov dl, r14b
00373473  8A CB                           mov cl, bl
00373475  E8 82 22 18 00                  call 0x1404f56fc
0037347A  E9 D4 FE FF FF                  jmp 0x140373353
0037347F  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
00373483  4C 8D 45 9F                     lea r8, [rbp - 0x61]
00373487  41 8B 07                        mov eax, dword ptr [r15]
0037348A  8B D6                           mov edx, esi
0037348C  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0037348F  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
00373492  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00373496  48 8D 4D CF                     lea rcx, [rbp - 0x31]
0037349A  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0037349E  E8 B9 87 10 00                  call 0x14047bc5c
003734A3  8B 5D 9F                        mov ebx, dword ptr [rbp - 0x61]
003734A6  44 8B C0                        mov r8d, eax
003734A9  8B D3                           mov edx, ebx
003734AB  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
003734AE  49 8B CF                        mov rcx, r15
003734B1  E8 D6 E8 06 00                  call 0x1403e1d8c
003734B6  E9 01 FD FF FF                  jmp 0x1403731bc
003734BB  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
003734BE  E9 D9 FE FF FF                  jmp 0x14037339c
003734C3  41 88 8D 1A 04 00 00            mov byte ptr [r13 + 0x41a], cl
003734CA  41 8B F6                        mov esi, r14d
003734CD  41 88 8D 18 04 00 00            mov byte ptr [r13 + 0x418], cl
003734D4  E9 32 FD FF FF                  jmp 0x14037320b
003734D9  4C 8D 05 A0 E7 C9 FF            lea r8, [rip - 0x361860]
003734E0  33 D2                           xor edx, edx
003734E2  E8 69 60 E9 FF                  call 0x140209550
003734E7  33 C9                           xor ecx, ecx
003734E9  E9 33 FD FF FF                  jmp 0x140373221
003734EE  48 8B 55 C7                     mov rdx, qword ptr [rbp - 0x39]
003734F2  4C 8D 61 06                     lea r12, [rcx + 6]
003734F6  8B C6                           mov eax, esi
003734F8  48 83 C0 06                     add rax, 6
003734FC  49 BF 00 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000000
00373506  4E 8D 24 E2                     lea r12, [rdx + r12*8]
0037350A  4C 8D 2C C2                     lea r13, [rdx + rax*8]
0037350E  E9 E3 08 37 00                  jmp 0x1406e3df6
00373513  BA 20 04 00 00                  mov edx, 0x420
00373518  41 B8 04 00 00 00               mov r8d, 4
0037351E  48 3B C2                        cmp rax, rdx
00373521  FF C9                           dec ecx
00373523  41 0F 42 D8                     cmovb ebx, r8d
00373527  48 3B C2                        cmp rax, rdx
0037352A  1B C0                           sbb eax, eax
0037352C  23 C1                           and eax, ecx
0037352E  41 89 85 8C 03 00 00            mov dword ptr [r13 + 0x38c], eax
00373535  E9 39 F9 FF FF                  jmp 0x140372e73
0037353A  41 C7 85 8C 03 00 00 08 00 00 00  mov dword ptr [r13 + 0x38c], 8
00373545  E9 43 FE FF FF                  jmp 0x14037338d
0037354A  44 8B 45 8F                     mov r8d, dword ptr [rbp - 0x71]
0037354E  E9 FF FA FF FF                  jmp 0x140373052
00373553  4D 8B 45 00                     mov r8, qword ptr [r13]
00373557  45 33 C9                        xor r9d, r9d
0037355A  49 C1 E8 0C                     shr r8, 0xc
0037355E  49 8B CF                        mov rcx, r15
00373561  E8 96 81 16 00                  call 0x1404db6fc
00373566  45 33 FF                        xor r15d, r15d
00373569  44 89 3E                        mov dword ptr [rsi], r15d
0037356C  41 8B 84 24 90 00 00 00         mov eax, dword ptr [r12 + 0x90]
00373574  49 89 44 24 20                  mov qword ptr [r12 + 0x20], rax
00373579  44 0F 20 C3                     mov rbx, cr8
0037357D  45 0F 22 C6                     mov cr8, r14
00373581  44 39 3D 98 37 C5 00            cmp dword ptr [rip + 0xc53798], r15d
00373588  0F 84 E2 08 37 00               je 0x1406e3e70
0037358E  41 8A D6                        mov dl, r14b
00373591  8A CB                           mov cl, bl
00373593  E8 64 21 18 00                  call 0x1404f56fc
00373598  90                              nop
00373599  E9 D2 08 37 00                  jmp 0x1406e3e70
0037359E  48 8B CE                        mov rcx, rsi
003735A1  E8 4A BA EE FF                  call 0x14025eff0
003735A6  E9 AA F9 FF FF                  jmp 0x140372f55
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGatherPagefilePages(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (248);
    v_r11 = 0;
    v_stack_mCC = 0;
    v_stack_mB0 = *(unsigned __int64 *)(a1 + 64);
    v_stack_mA0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216);
    v_stack_mC8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 12))) == 0) goto loc_00373275;
    *(unsigned __int64 *)(a1 + 104) = 0;
    *(unsigned int *)(a1 + 104 + 8) = 0x20030ULL;
    *(unsigned __int64 *)(a1 + 104 + 32) = 0;
    *(unsigned __int64 *)(a1 + 104 + 40) = 0;
    v_stack_m98 = a1 + 104;
    result = (a1 + 104) + (v_r11 + 48);
    v_stack_mD8 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 64) + 172)))) & (15));
    result = (result) + (v_r11 + 48);
    v_r10 = (v_r10) * (result);
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 64) + 172))) & (64)) == 0) goto loc_00372FCC;
    v_stack_p18 = 0;
    result = -(*(unsigned __int64 *)(v_r10 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1));
    v_rdi = (unsigned int)((0) & ((unsigned int)(v_r11 + 48 - 46)));
    if (*(unsigned __int64 *)(v_r10 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1) != 0) goto loc_00372BE7;
loc_00372BBE:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1200)) != 0) goto loc_00372F98;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) == 0) goto loc_0037322B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 4096) != 0) {
        v_rdi = (unsigned int)(v_r11 + 48 - 46);
    }
    if (0 == 0) goto loc_00372F81;
loc_00372BF0:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) | (4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1204)))) != -1) { v_rdi = (unsigned int)(result); }
    v_stack_p10 = (unsigned int)(v_rdi);
    if ((((unsigned __int8)(v_r11 + 48 - 46)) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00373285;
loc_00372C14:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12920306)));
    if ((((unsigned __int8)(v_r11 + 48 - 46)) & ((unsigned __int8)(v_rdi))) != 0) goto loc_00372FD9;
loc_00372C26:
    a1 = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 1048)) != 0) goto loc_003731DB;
loc_00372C35:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 40))) & (28));
    if (((unsigned __int8)(result)) < 8) goto loc_00373011;
loc_00372C44:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_rdi = (unsigned int)((v_rdi) | (1));
    if ((((unsigned __int8)(v_r11 + 48 - 46)) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00372FE7;
    v_stack_p18 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) == 0) goto loc_00373023;
    a4 = (unsigned int)(v_stack_p10);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 12)))) < ((unsigned int)((unsigned int)(v_stack_p10)))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 12))); }
loc_00372C7F:
    if ((unsigned int)(a4) == 0) goto loc_00373460;
    result = MiFillNoReservationCluster(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216), *(unsigned __int64 *)(a1 + 64), v_stack_mD8, a4);
    v_stack_mBC = (unsigned int)(result);
loc_00372C9F:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_003732F1;
    result = (unsigned int)((result) - 1);
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_mD0 = (unsigned int)(result);
    v_stack_mCC = (unsigned int)(result);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) == 0) goto loc_00373121;
loc_00372CC0:
    result = KeLeaveCriticalRegionThread(v_stack_mC8, *(unsigned __int64 *)(a1 + 64), v_stack_mD8, a4);
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFEULL));
    v_stack_mB8 = (unsigned int)(v_rdi);
    if (((unsigned int)((unsigned int)(v_stack_p20))) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_003734EE;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p20));
    a1 = (unsigned int)(((unsigned int)(v_stack_p20)) << (12));
    *(unsigned int *)(a1 + 104 + 40) = (unsigned int)(a1);
    result = (a1 + 104) + (48);
    *(unsigned int *)(a1 + 44) = (unsigned int)(a1);
    a1 = 0;
    *(unsigned int *)(a1 + 48) = (unsigned int)((unsigned int)(v_stack_mD0));
    v_stack_p10 = 0;
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_mB0 = result;
    result = MiPageToNode(*(unsigned __int64 *)(result), *(unsigned __int64 *)(a1 + 64), v_stack_mD8, a4);
loc_00372D18:
    a1 = (*(unsigned __int64 *)(v_stack_mB0) + *(unsigned __int64 *)(v_stack_mB0) * 2) << (4);
    a1 = (a1) + (result);
    v_stack_mD8 = a1;
    if ((*(unsigned __int64 *)(v_stack_mB0)) == (*(unsigned __int64 *)(v_rip + 11290430))) goto loc_00372DD7;
    v_r12 = 0;
    v_rsi = 1 + result * 1;
    if ((unsigned int)(1 + result * 1) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_mB0);
        result = MiPageToNode(a1, *(unsigned __int64 *)(v_stack_mB0), v_stack_mD8, a4);
        a1 = v_stack_mD8;
        result = (unsigned int)((result) + (1));
        v_rsi = 1 + result * 1;
        if (((unsigned int)(1 + result * 1)) != ((unsigned int)(result))) { v_rsi = 0; }
    }
    result = MiLockPageInline(a1, *(unsigned __int64 *)(v_stack_mB0), v_stack_mD8, a4);
    result = MiIsPfnOriginalPteLost(v_stack_mD8, *(unsigned __int64 *)(v_stack_mB0), v_stack_mD8, a4);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_00372DA3;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) == 0) goto loc_00372F6A;
    result = MiSetStoreVirtualPagefileValue(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216), *(unsigned __int64 *)(v_stack_mD8 + 16), a1 + 4, a4);
    *(unsigned __int64 *)(v_stack_mD8 + 16) = result;
loc_00372DA1:
    a1 = 0;
loc_00372DA3:
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_00372DD0;
    if ((*(unsigned int *)(v_rip + 12926818)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a1 + 4, a4);
    }
loc_00372DD0:
loc_00372DD7:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_p10)) + (1));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p18)) + (1));
    v_rdi = (v_stack_mB0) + (8);
    v_stack_p10 = (unsigned int)(v_r12);
    v_stack_p18 = (unsigned int)(v_rbx);
    if (((unsigned int)(v_r12)) < v_stack_p20) goto loc_00372D18;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rip + 12919827)) + (6));
    result = (unsigned __int16)((result) << (3));
    *(unsigned __int16 *)(v_stack_m98 + 8) = (unsigned __int16)(result);
loc_00372E24:
    if ((*(unsigned __int64 *)(a1 + 4)) != (*(unsigned __int64 *)(a1 + 4))) goto loc_00372E24;
    a1 = (*(unsigned __int64 *)(a4)) - (*(unsigned __int64 *)(a1 + 4));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 40))) >> (2));
    *(unsigned __int64 *)(v_stack_p8 + 80) = a1;
    v_rbx = (unsigned int)((v_rbx) & (7));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 908))) != 0) goto loc_00373513;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 18688)) < 160) goto loc_00373382;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 18688)) < 288) goto loc_0037353A;
loc_00372E73:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 40))) & (0xFFFFFFE3ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(v_rbx * 4)));
    *(unsigned int *)(v_stack_p8 + 40) = (unsigned int)(a1);
    if (((unsigned int)(v_rbx)) >= 2) goto loc_00372EBF;
    if (((unsigned int)(v_rbx)) != 2) goto loc_00372EBF;
    result = v_stack_mC8 + 152;
    if ((*(unsigned __int64 *)(v_stack_mC8 + 152)) != (v_stack_mC8 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mC8, *(unsigned __int64 *)(a1 + 4), a1 + 4, a4);
    }
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mB8)))) >> (1));
    a4 = (unsigned int)(~(a4));
    a4 = (unsigned int)((a4) & (1));
    result = MI_PAGEFILE_WRITE(v_stack_p8, *(unsigned __int64 *)(v_stack_p8 + 80), (unsigned int)((unsigned int)(v_rbx)), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 896)))) == 512) goto loc_00373104;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 896))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 896) = (unsigned int)(result);
loc_00372EFB:
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0)))) << (12);
    *(unsigned __int64 *)(v_stack_p8 + 88) = result;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) == 0) goto loc_0037303F;
loc_00372F32:
    result = MiStoreWriteModifiedPages(v_stack_p8, (unsigned int)((unsigned int)(v_rsi)), (unsigned int)(v_stack_mD0), a4);
    result = 0;
    if (sign_flag) goto loc_0037354A;
loc_00372F48:
loc_00372F4C:
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_mB8)))) != 0) goto loc_0037359E;
loc_00372F55:
    v_rsp = (v_rsp) + (248);
    return result;
loc_00372F6A:
    result = MiUpdatePfnBackingStore(v_stack_mD8, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(v_rbx)), a4);
    goto loc_00372DA1;
loc_00372F81:
    if (v_stack_mC8 == 0) goto loc_00372F98;
    v_stack_p18 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (16)) == 0) goto loc_00372BF0;
loc_00372F98:
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1 + 64) + 200, *(unsigned __int64 *)(a1 + 64), (unsigned int)((unsigned int)(v_rbx)), a4);
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a1 + 64) + 200, (unsigned __int8)(result), (unsigned int)((unsigned int)(v_rbx)), a4);
    *(unsigned __int64 *)(v_stack_p8) = (unsigned int)(0x99887711ULL);
    goto loc_00372F48;
loc_00372FCC:
    v_stack_p18 = *(unsigned __int64 *)(0 + v_stack_p8 + 88 * 1);
    goto loc_00372BBE;
loc_00372FD9:
    v_rbx = *(unsigned __int64 *)(a1 + 64) + 200;
    if (v_stack_mC8 < (*(unsigned __int64 *)(a1 + 64) + 200)) { v_rbx = (unsigned int)(v_stack_mC8); }
    v_stack_p10 = (unsigned int)(v_rbx);
    goto loc_00372C26;
loc_00372FE7:
    v_stack_p20 = (unsigned int)(v_rbx);
    result = MiBuildReservationCluster(v_stack_mD8, *(unsigned __int64 *)(a1 + 64), v_stack_p20, v_stack_mCC);
    v_stack_p18 = (unsigned int)(result);
    v_stack_mBC = (unsigned int)((unsigned int)(v_stack_p20));
    goto loc_00372C9F;
loc_00373011:
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) > 256) { v_rbx = 256; }
    v_stack_p10 = (unsigned int)(v_rbx);
    goto loc_00372C44;
loc_00373023:
    a4 = 0;
    result = MiFindPageFileWriteCluster(*(unsigned __int64 *)(a1 + 64), v_stack_p18, v_stack_p10, a4);
    goto loc_00372C7F;
loc_0037303F:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mB8)))) & (6));
    if (((unsigned __int8)(result)) == 4) goto loc_00372F32;
    result = 0;
loc_00373052:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (64)) != 0) goto loc_00373330;
    a3 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_p20));
    result = MiMapPageFileHash(*(unsigned __int64 *)(a1 + 64), v_stack_p8 + 104, a3, (unsigned int)((unsigned int)(v_stack_p10)));
    if (condition_is_below) goto loc_00373553;
    v_stack_p50 = v_stack_p8 + 16;
    result = 0;
    v_stack_p48 = v_stack_p8 + 24;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 168)));
    v_stack_p28 = (unsigned int)(v_rbx);
    v_stack_p20 = v_stack_p8;
    result = IoAsynchronousPageWrite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 24), v_stack_p8 + 104, v_stack_p8 + 88, v_rip + 604373);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_00372F48;
    result = 0;
    goto loc_00373338;
loc_00373104:
    result = (*(unsigned __int64 *)(v_stack_p8 + 88 + 888)) >> (9);
    a1 = (*(unsigned __int64 *)(v_stack_p8 + 88 + 888)) - (result);
    *(unsigned __int64 *)(v_stack_p8 + 88 + 888) = a1;
    goto loc_00372EFB;
loc_00373121:
    result = ExAcquireSpinLockExclusive(0 + 200, (unsigned int)((unsigned int)(result)), v_stack_p8 + 88, v_rip + 604373);
    v_stack_p10 = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(v_stack_mB8))) & (2)) == 0) goto loc_003733A5;
    result = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m8C = 0;
    a2 = (*(unsigned __int16 *)(0 + 172)) << (12);
    result = MiMakePageFilePte((unsigned int)((unsigned int)(v_rbx)), a2, v_stack_p8 + 88, v_rip + 604373);
    result = (result) ^ (a2);
    result = (result) & (0xFFFFFFFFFFFF0FFFULL);
    result = (result) ^ (a2);
    v_stack_mA8 = result;
    result = MiFindFreePageFileSpace(*(unsigned __int64 *)(0 + 216), v_stack_mA8, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    v_stack_p20 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_0037347F;
    if (*(unsigned __int64 *)(v_rip + 11250404) == 0) goto loc_003731B5;
    v_rbx = v_stack_mA8;
    if ((((unsigned __int8)(v_stack_mA8)) & (16)) == 0) {
        v_rbx = *(unsigned __int64 *)(v_rip + 11250404);
        v_rbx = ~(v_rbx);
        v_rbx = (v_rbx) & (v_stack_mA8);
    }
    v_rbx = (v_rbx) >> (32);
    v_stack_mC0 = (unsigned int)(v_rbx);
loc_003731BC:
    v_stack_p18 = (unsigned int)(v_rbx);
loc_003731BF:
    result = MiUpdatePagefilePeakUsage(0, v_stack_mA8, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    result = MiReleaseSpinLockExclusive(0 + 200, v_stack_p10, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    goto loc_00372CC0;
loc_003731DB:
    result = ExAcquireSpinLockExclusive(v_stack_p8 + 88 + 1044, v_stack_p10, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    a1 = 0;
    if ((*(unsigned __int8 *)(v_stack_p8 + 88 + 1050)) != 0) goto loc_003734C3;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 88 + 1048)) != 0) {
        v_rbx = (unsigned int)(*(unsigned __int8 *)(v_stack_p8 + 88 + 1048));
        v_stack_p10 = (unsigned int)(*(unsigned __int8 *)(v_stack_p8 + 88 + 1048));
    }
    result = MiReleaseSpinLockExclusive(v_stack_p8 + 88 + 1044, (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    a1 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(0 + 200))) != 0) goto loc_003734D9;
loc_00373221:
    goto loc_00372C35;
loc_0037322B:
    if (*(unsigned __int64 *)(v_stack_p8 + 88 + 3968) != 0) goto loc_00372BE7;
    result = MiIsStoreVirtualPagefileFull(v_stack_p8 + 88, 2, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    if ((unsigned int)(result) == 0) goto loc_00372BE7;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_p8 + 88 + 1204))) + (v_rbx);
    result = (result) * (a1);
    if (*(unsigned __int64 *)(result + v_stack_p8 + 88 * 1) != 0) goto loc_00372BE7;
    goto loc_00372BE7;
loc_00373275:
    result = MiPageFileNoFreeSpace(0, v_stack_p8, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    goto loc_00372F55;
loc_00373285:
    if (*(unsigned __int64 *)(v_stack_p8 + 88 + 4096) == 0) goto loc_00372C14;
    if (((*(unsigned __int8 *)(0 + 172)) & (16)) != 0) goto loc_00372C14;
    if (*(unsigned __int64 *)(0 + v_stack_p8 + 88 * 1) == 0) goto loc_003734BB;
    if (((*(unsigned __int8 *)(0 + 175)) & (1)) != 0) goto loc_003734BB;
    result = MiPageFileLargestBitmapsRun(0, v_stack_p8, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 104))) >> (2));
    if (((unsigned int)(result)) < ((unsigned int)(v_rbx))) goto loc_003732E7;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 12918590))) >> (2);
    if ((*(unsigned __int64 *)(v_stack_p8 + 88 + 4096)) >= result) goto loc_00373397;
    if ((*(unsigned __int64 *)(v_stack_p8 + 88 + 4096)) >= v_stack_p18) goto loc_00373397;
loc_003732E7:
    goto loc_00372C14;
loc_003732F1:
    result = MiMakePagefileWriterEntryAvailable(v_stack_p8, 2, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    if ((*(unsigned __int64 *)(v_stack_p8 + 88 + 4096)) != v_stack_p18) goto loc_00372F4C;
    if ((*(unsigned __int64 *)(v_stack_mC8 + 152)) == (v_stack_mC8 + 152)) goto loc_00372F4C;
    result = KiCheckForKernelApcDelivery(v_stack_p8, 2, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    goto loc_00372F4C;
loc_00373330:
loc_00373338:
    *(unsigned int *)(v_stack_p8 + 24) = 2;
    *(unsigned __int64 *)(v_stack_p8 + 32) = result;
    if ((*(unsigned int *)(v_rip + 12925395)) != ((unsigned int)(result))) goto loc_00373470;
loc_00373353:
    result = MiWriteComplete(v_stack_p8, v_stack_p8 + 24, 1, 38);
    result = 0;
    if ((*(unsigned int *)(v_rip + 12925367)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, 38);
    }
    goto loc_00372F48;
loc_00373382:
    *(unsigned int *)(v_stack_p8 + 88 + 908) = 32;
loc_0037338D:
    goto loc_00372E73;
loc_00373397:
loc_0037339C:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)((unsigned __int8)(result))))) | (2));
    goto loc_00372C14;
loc_003733A5:
    result = MiSetPageFileAllocationBits(1, 4, (unsigned int)((unsigned int)(v_stack_p8 + 24)), 38);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8 + 24))) | (0xFFFFFFFFULL));
    v_stack_mD8 = v_stack_p8 + 152;
    if ((v_stack_p8 + 152) >= (v_stack_mD8 + (unsigned int)((unsigned int)(v_stack_p8 + 24)) * 8)) goto loc_00373425;
loc_003733DA:
    if ((*(unsigned __int64 *)(v_stack_p8 + 152)) == (*(unsigned __int64 *)(v_rip + 11288727))) goto loc_0037343C;
loc_003733E6:
    result = *(unsigned __int64 *)(v_rip + 11288727);
    v_r10 = (unsigned int)((unsigned int)(a3));
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) != ((unsigned int)(a3))) {
        a3 = 4;
        a4 = 0;
        a3 = (unsigned int)((a3) - ((unsigned int)((unsigned int)((unsigned int)(a3)))));
        a2 = (unsigned int)((unsigned int)((unsigned int)(a3)));
        a1 = 1;
        result = MiInvalidatePageFileBitmapsCache(a1, a2, a3, a4);
        a1 = v_stack_mD8;
        a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
        v_r10 = (unsigned int)(a3);
    }
    a1 = (a1) + (8);
    v_r12 = (unsigned int)((4) + (1));
    v_stack_mD8 = a1;
    if (a1 < (v_stack_mD8 + (unsigned int)((unsigned int)(v_stack_p8 + 24)) * 8)) goto loc_003733DA;
loc_00373425:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(1 + 104))))) >> (2));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 104))) - ((unsigned int)(result)));
    a1 = (unsigned int)((a1) + (v_stack_p20));
    *(unsigned int *)(1 + 104) = (unsigned int)(a1);
    goto loc_003731BF;
loc_0037343C:
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_003733E6;
    if (((unsigned int)(v_r10)) != ((unsigned int)(a3))) goto loc_0037340A;
    goto loc_0037340A;
loc_00373460:
    result = MiPageFileNoFreeSpace(1, v_stack_p8, a3, a4);
    goto loc_00372F4C;
loc_00373470:
    result = KiRaiseIrqlProcessIrqlFlags(4, 1, a3, a4);
    goto loc_00373353;
loc_0037347F:
    v_stack_m90 = (unsigned int)((unsigned int)(*(unsigned int *)(1)));
    v_stack_mC0 = 4;
    v_stack_m88 = *(unsigned __int64 *)(*(unsigned __int64 *)(1 + 80) + 16);
    result = RtlFindLongestRunClearCapped(v_stack_m90, (unsigned int)((unsigned int)((unsigned int)(v_stack_mBC))), v_stack_mC0, a4);
    v_stack_p20 = (unsigned int)(result);
    result = MiSetPageFileAllocationBits(1, (unsigned int)((unsigned int)((unsigned int)(v_stack_mC0))), (unsigned int)((unsigned int)(result)), a4);
    goto loc_003731BC;
loc_003734BB:
    goto loc_0037339C;
loc_003734C3:
    *(unsigned __int8 *)(v_stack_mA0 + 1050) = 1;
    *(unsigned __int8 *)(v_stack_mA0 + 1048) = 1;
    goto loc_0037320B;
loc_003734D9:
    a2 = 0;
    result = KeDelayExecutionThread(1, a2, v_rip - 3545184, a4);
    a1 = 0;
    goto loc_00373221;
loc_003734EE:
    result = (1) + (6);
loc_00373513:
    a1 = (unsigned int)((a1) - 1);
    v_rbx = (unsigned int)(v_stack_mC0);
    if (result < ((unsigned int)(0x420ULL))) { v_rbx = 4; }
    result = (unsigned int)((result) & ((unsigned int)(a1)));
    *(unsigned int *)(v_stack_m98 + result * 8 + 908) = (unsigned int)(result);
    goto loc_00372E73;
loc_0037353A:
    *(unsigned int *)(v_stack_m98 + result * 8 + 908) = 8;
    goto loc_0037338D;
loc_0037354A:
    goto loc_00373052;
loc_00373553:
    a4 = 0;
    a3 = (*(unsigned __int64 *)(v_stack_m98 + result * 8)) >> (12);
    result = MiTransferMemoryPagefileData(1, (unsigned int)(0x420ULL), a3, a4);
    v_r15 = 0;
    *(unsigned int *)(1) = 0;
    *(unsigned __int64 *)(v_stack_m98 + a1 + 6 * 8 + 32) = (unsigned int)(*(unsigned int *)(v_stack_m98 + a1 + 6 * 8 + 144));
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned __int8)((unsigned __int8)(result))), 1, a3, a4);
loc_0037359E:
    result = KeLeaveCriticalRegionThread(1, 1, a3, a4);
    goto loc_00372F55;
}
```

## 5. (Beta) C Style

```c
int64_t MiGatherPagefilePages(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m118;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (248);
    local_r11 = 0;
    v_stack_mCC = 0;
    v_stack_mB0 = *(uint64_t *)(arg1 + 0x40);
    v_stack_mA0 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8);
    v_stack_mC8 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xC))) == 0) goto loc_00373275;
    *(uint64_t *)(arg1 + 0x68) = 0;
    *(uint32_t *)(arg1 + 0x68 + 0x8) = 0x20030ULL;
    *(uint64_t *)(arg1 + 0x68 + 0x20) = 0;
    *(uint64_t *)(arg1 + 0x68 + 0x28) = 0;
    v_stack_m98 = Arg1 + 104;
    result = (Arg1 + 104) + (local_r11 + 48);
    v_stack_mD8 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)))) & (15));
    result = (result) + (local_r11 + 48);
    local_r10 = (local_r10) * (result);
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC))) & (64)) == 0) goto loc_00372FCC;
    v_stack_p18 = 0;
    result = -(*(uint64_t *)(local_r10 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1));
    local_rdi = (uint32_t)((0) & ((uint32_t)(local_r11 + 48 - 46)));
    if (*(uint64_t *)(local_r10 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1) != 0) goto loc_00372BE7;
loc_00372BBE:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B0)) != 0) goto loc_00372F98;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) == 0) goto loc_0037322B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x1000) != 0) {
        local_rdi = (uint32_t)(local_r11 + 48 - 46);
    }
    if (0 == 0) goto loc_00372F81;
loc_00372BF0:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) | (4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4B4)))) != -1) { local_rdi = (uint32_t)(result); }
    v_stack_p10 = (uint32_t)(local_rdi);
    if ((((uint8_t)(local_r11 + 48 - 46)) & ((uint8_t)(local_rdi))) == 0) goto loc_00373285;
loc_00372C14:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC525F2)));
    if ((((uint8_t)(local_r11 + 48 - 46)) & ((uint8_t)(local_rdi))) != 0) goto loc_00372FD9;
loc_00372C26:
    Arg1 = 0;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x418)) != 0) goto loc_003731DB;
loc_00372C35:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) & (28));
    if (((uint8_t)(result)) < 8) goto loc_00373011;
loc_00372C44:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    local_rdi = (uint32_t)((local_rdi) | (1));
    if ((((uint8_t)(local_r11 + 48 - 46)) & ((uint8_t)(local_rdi))) == 0) goto loc_00372FE7;
    v_stack_p18 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) == 0) goto loc_00373023;
    a4 = (uint32_t)(v_stack_p10);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xC)))) < ((uint32_t)((uint32_t)(v_stack_p10)))) { a4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xC))); }
loc_00372C7F:
    if ((uint32_t)(a4) == 0) goto loc_00373460;
    result = MiFillNoReservationCluster(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8), *(uint64_t *)(arg1 + 0x40), v_stack_mD8, a4);
    v_stack_mBC = (uint32_t)(result);
loc_00372C9F:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_003732F1;
    result = (uint32_t)((result) - 1);
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_mD0 = (uint32_t)(result);
    v_stack_mCC = (uint32_t)(result);
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) == 0) goto loc_00373121;
loc_00372CC0:
    result = KeLeaveCriticalRegionThread(v_stack_mC8, *(uint64_t *)(arg1 + 0x40), v_stack_mD8, a4);
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFEULL));
    v_stack_mB8 = (uint32_t)(local_rdi);
    if (((uint32_t)((uint32_t)(v_stack_p20))) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_003734EE;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p20));
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p20)) << (12));
    *(uint32_t *)(arg1 + 0x68 + 0x28) = (uint32_t)(Arg1);
    result = (Arg1 + 104) + (48);
    *(uint32_t *)(arg1 + 0x2C) = (uint32_t)(Arg1);
    Arg1 = 0;
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)((uint32_t)(v_stack_mD0));
    v_stack_p10 = 0;
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_mB0 = result;
    result = MiPageToNode(*(uint64_t *)(result), *(uint64_t *)(arg1 + 0x40), v_stack_mD8, a4);
loc_00372D18:
    Arg1 = (*(uint64_t *)(v_stack_mB0) + *(uint64_t *)(v_stack_mB0) * 2) << (4);
    Arg1 = (Arg1) + (result);
    v_stack_mD8 = Arg1;
    if ((*(uint64_t *)(v_stack_mB0)) == (*(uint64_t *)(v_rip + 0xAC473E))) goto loc_00372DD7;
    local_r12 = 0;
    local_rsi = 1 + result * 1;
    if ((uint32_t)(1 + result * 1) != 0) {
        Arg1 = *(uint64_t *)(v_stack_mB0);
        result = MiPageToNode(Arg1, *(uint64_t *)(v_stack_mB0), v_stack_mD8, a4);
        Arg1 = v_stack_mD8;
        result = (uint32_t)((result) + (1));
        local_rsi = 1 + result * 1;
        if (((uint32_t)(1 + result * 1)) != ((uint32_t)(result))) { local_rsi = 0; }
    }
    result = MiLockPageInline(Arg1, *(uint64_t *)(v_stack_mB0), v_stack_mD8, a4);
    result = MiIsPfnOriginalPteLost(v_stack_mD8, *(uint64_t *)(v_stack_mB0), v_stack_mD8, a4);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_00372DA3;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) == 0) goto loc_00372F6A;
    result = MiSetStoreVirtualPagefileValue(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8), *(uint64_t *)(v_stack_mD8 + 0x10), Arg1 + 4, a4);
    *(uint64_t *)(v_stack_mD8 + 0x10) = result;
loc_00372DA1:
    Arg1 = 0;
loc_00372DA3:
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_00372DD0;
    if ((*(uint32_t *)(v_rip + 0xC53F62)) != 0) {
        Arg1 = v_cr8;
        a2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, Arg1 + 4, a4);
    }
loc_00372DD0:
loc_00372DD7:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_p10)) + (1));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p18)) + (1));
    local_rdi = (v_stack_mB0) + (8);
    v_stack_p10 = (uint32_t)(local_r12);
    v_stack_p18 = (uint32_t)(local_rbx);
    if (((uint32_t)(local_r12)) < v_stack_p20) goto loc_00372D18;
    result = (uint16_t)((*(uint16_t *)(v_rip + 0xC52413)) + (6));
    result = (uint16_t)((result) << (3));
    *(uint16_t *)(v_stack_m98 + 0x8) = (uint16_t)(result);
loc_00372E24:
    if ((*(uint64_t *)(arg1 + 0x4)) != (*(uint64_t *)(arg1 + 0x4))) goto loc_00372E24;
    Arg1 = (*(uint64_t *)(a4)) - (*(uint64_t *)(arg1 + 0x4));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28))) >> (2));
    *(void **)(v_stack_p8 + 0x50) = Arg1;
    local_rbx = (uint32_t)((local_rbx) & (7));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x38C))) != 0) goto loc_00373513;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4900)) < 160) goto loc_00373382;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4900)) < 288) goto loc_0037353A;
loc_00372E73:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x28))) & (0xFFFFFFE3ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_rbx * 4)));
    *(uint32_t *)(v_stack_p8 + 0x28) = (uint32_t)(Arg1);
    if (((uint32_t)(local_rbx)) >= 2) goto loc_00372EBF;
    if (((uint32_t)(local_rbx)) != 2) goto loc_00372EBF;
    result = v_stack_mC8 + 152;
    if ((*(uint64_t *)(v_stack_mC8 + 0x98)) != (v_stack_mC8 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mC8, *(uint64_t *)(arg1 + 0x4), Arg1 + 4, a4);
    }
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mB8)))) >> (1));
    a4 = (uint32_t)(~(a4));
    a4 = (uint32_t)((a4) & (1));
    result = MI_PAGEFILE_WRITE(v_stack_p8, *(uint64_t *)(v_stack_p8 + 0x50), (uint32_t)((uint32_t)(local_rbx)), a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x380)))) == 512) goto loc_00373104;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x380))) + 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x380) = (uint32_t)(result);
loc_00372EFB:
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0)))) << (12);
    *(uint64_t *)(v_stack_p8 + 0x58) = result;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) == 0) goto loc_0037303F;
loc_00372F32:
    result = MiStoreWriteModifiedPages(v_stack_p8, (uint32_t)((uint32_t)(local_rsi)), (uint32_t)(v_stack_mD0), a4);
    result = 0;
    if (sign_flag) goto loc_0037354A;
loc_00372F48:
loc_00372F4C:
    if (((1) & ((uint8_t)((uint32_t)(v_stack_mB8)))) != 0) goto loc_0037359E;
loc_00372F55:
    local_rsp = (local_rsp) + (248);
    return result;
loc_00372F6A:
    result = MiUpdatePfnBackingStore(v_stack_mD8, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(local_rbx)), a4);
    goto loc_00372DA1;
loc_00372F81:
    if (v_stack_mC8 == 0) goto loc_00372F98;
    v_stack_p18 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (16)) == 0) goto loc_00372BF0;
loc_00372F98:
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1 + 0x40) + 200, *(uint64_t *)(arg1 + 0x40), (uint32_t)((uint32_t)(local_rbx)), a4);
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg1 + 0x40) + 200, (uint8_t)(result), (uint32_t)((uint32_t)(local_rbx)), a4);
    *(uint64_t *)(v_stack_p8) = (uint32_t)(0x99887711ULL);
    goto loc_00372F48;
loc_00372FCC:
    v_stack_p18 = *(uint64_t *)(0 + v_stack_p8 + 0x58 * 1);
    goto loc_00372BBE;
loc_00372FD9:
    local_rbx = *(uint64_t *)(arg1 + 0x40) + 200;
    if (v_stack_mC8 < (*(uint64_t *)(arg1 + 0x40) + 200)) { local_rbx = (uint32_t)(v_stack_mC8); }
    v_stack_p10 = (uint32_t)(local_rbx);
    goto loc_00372C26;
loc_00372FE7:
    v_stack_p20 = (uint32_t)(local_rbx);
    result = MiBuildReservationCluster(v_stack_mD8, *(uint64_t *)(arg1 + 0x40), v_stack_p20, v_stack_mCC);
    v_stack_p18 = (uint32_t)(result);
    v_stack_mBC = (uint32_t)((uint32_t)(v_stack_p20));
    goto loc_00372C9F;
loc_00373011:
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) > 256) { local_rbx = 256; }
    v_stack_p10 = (uint32_t)(local_rbx);
    goto loc_00372C44;
loc_00373023:
    a4 = 0;
    result = MiFindPageFileWriteCluster(*(uint64_t *)(arg1 + 0x40), v_stack_p18, v_stack_p10, a4);
    goto loc_00372C7F;
loc_0037303F:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mB8)))) & (6));
    if (((uint8_t)(result)) == 4) goto loc_00372F32;
    result = 0;
loc_00373052:
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (64)) != 0) goto loc_00373330;
    a3 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_p20));
    result = MiMapPageFileHash(*(uint64_t *)(arg1 + 0x40), v_stack_p8 + 104, a3, (uint32_t)((uint32_t)(v_stack_p10)));
    if (condition_is_below) goto loc_00373553;
    v_stack_p50 = v_stack_p8 + 16;
    result = 0;
    v_stack_p48 = v_stack_p8 + 24;
    v_stack_p40 = 0;
    v_stack_p38 = 0;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0xA8)));
    v_stack_p28 = (uint32_t)(local_rbx);
    v_stack_p20 = v_stack_p8;
    result = IoAsynchronousPageWrite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0x18), v_stack_p8 + 104, v_stack_p8 + 88, v_rip + 604373);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_00372F48;
    result = 0;
    goto loc_00373338;
loc_00373104:
    result = (*(uint64_t *)(v_stack_p8 + 0x58 + 0x378)) >> (9);
    Arg1 = (*(uint64_t *)(v_stack_p8 + 0x58 + 0x378)) - (result);
    *(void **)(v_stack_p8 + 0x58 + 0x378) = Arg1;
    goto loc_00372EFB;
loc_00373121:
    result = ExAcquireSpinLockExclusive(0 + 200, (uint32_t)((uint32_t)(result)), v_stack_p8 + 88, v_rip + 604373);
    v_stack_p10 = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(v_stack_mB8))) & (2)) == 0) goto loc_003733A5;
    result = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m50 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m8C = 0;
    a2 = (*(uint16_t *)(0 + 0xAC)) << (12);
    result = MiMakePageFilePte((uint32_t)((uint32_t)(local_rbx)), a2, v_stack_p8 + 88, v_rip + 604373);
    result = (result) ^ (a2);
    result = (result) & (0xFFFFFFFFFFFF0FFFULL);
    result = (result) ^ (a2);
    v_stack_mA8 = result;
    result = MiFindFreePageFileSpace(*(uint64_t *)(0 + 0xD8), v_stack_mA8, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    v_stack_p20 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_0037347F;
    if (*(uint64_t *)(v_rip + 0xABAAE4) == 0) goto loc_003731B5;
    local_rbx = v_stack_mA8;
    if ((((uint8_t)(v_stack_mA8)) & (16)) == 0) {
        local_rbx = *(uint64_t *)(v_rip + 0xABAAE4);
        local_rbx = ~(local_rbx);
        local_rbx = (local_rbx) & (v_stack_mA8);
    }
    local_rbx = (local_rbx) >> (32);
    v_stack_mC0 = (uint32_t)(local_rbx);
loc_003731BC:
    v_stack_p18 = (uint32_t)(local_rbx);
loc_003731BF:
    result = MiUpdatePagefilePeakUsage(0, v_stack_mA8, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    result = MiReleaseSpinLockExclusive(0 + 200, v_stack_p10, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    goto loc_00372CC0;
loc_003731DB:
    result = ExAcquireSpinLockExclusive(v_stack_p8 + 88 + 1044, v_stack_p10, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    Arg1 = 0;
    if ((*(uint8_t *)(v_stack_p8 + 0x58 + 0x41A)) != 0) goto loc_003734C3;
    if ((uint8_t)(*(uint8_t *)(v_stack_p8 + 0x58 + 0x418)) != 0) {
        local_rbx = (uint32_t)(*(uint8_t *)(v_stack_p8 + 0x58 + 0x418));
        v_stack_p10 = (uint32_t)(*(uint8_t *)(v_stack_p8 + 0x58 + 0x418));
    }
    result = MiReleaseSpinLockExclusive(v_stack_p8 + 88 + 1044, (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    Arg1 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(0 + 200))) != 0) goto loc_003734D9;
loc_00373221:
    goto loc_00372C35;
loc_0037322B:
    if (*(uint64_t *)(v_stack_p8 + 0x58 + 0xF80) != 0) goto loc_00372BE7;
    result = MiIsStoreVirtualPagefileFull(v_stack_p8 + 88, 2, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    if ((uint32_t)(result) == 0) goto loc_00372BE7;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x58 + 0x4B4))) + (local_rbx);
    result = (result) * (Arg1);
    if (*(uint64_t *)(result + v_stack_p8 + 0x58 * 1) != 0) goto loc_00372BE7;
    goto loc_00372BE7;
loc_00373275:
    result = MiPageFileNoFreeSpace(0, v_stack_p8, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    goto loc_00372F55;
loc_00373285:
    if (*(uint64_t *)(v_stack_p8 + 0x58 + 0x1000) == 0) goto loc_00372C14;
    if (((*(uint8_t *)(0 + 0xAC)) & (16)) != 0) goto loc_00372C14;
    if (*(uint64_t *)(0 + v_stack_p8 + 0x58 * 1) == 0) goto loc_003734BB;
    if (((*(uint8_t *)(0 + 0xAF)) & (1)) != 0) goto loc_003734BB;
    result = MiPageFileLargestBitmapsRun(0, v_stack_p8, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x68))) >> (2));
    if (((uint32_t)(result)) < ((uint32_t)(local_rbx))) goto loc_003732E7;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0xC51F3E))) >> (2);
    if ((*(uint64_t *)(v_stack_p8 + 0x58 + 0x1000)) >= result) goto loc_00373397;
    if ((*(uint64_t *)(v_stack_p8 + 0x58 + 0x1000)) >= v_stack_p18) goto loc_00373397;
loc_003732E7:
    goto loc_00372C14;
loc_003732F1:
    result = MiMakePagefileWriterEntryAvailable(v_stack_p8, 2, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    if ((*(uint64_t *)(v_stack_p8 + 0x58 + 0x1000)) != v_stack_p18) goto loc_00372F4C;
    if ((*(uint64_t *)(v_stack_mC8 + 0x98)) == (v_stack_mC8 + 152)) goto loc_00372F4C;
    result = KiCheckForKernelApcDelivery(v_stack_p8, 2, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    goto loc_00372F4C;
loc_00373330:
loc_00373338:
    *(uint32_t *)(v_stack_p8 + 0x18) = 2;
    *(uint64_t *)(v_stack_p8 + 0x20) = result;
    if ((*(uint32_t *)(v_rip + 0xC539D3)) != ((uint32_t)(result))) goto loc_00373470;
loc_00373353:
    result = MiWriteComplete(v_stack_p8, v_stack_p8 + 24, 1, 38);
    result = 0;
    if ((*(uint32_t *)(v_rip + 0xC539B7)) != 0) {
        Arg1 = 1;
        a2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, 1, 38);
    }
    goto loc_00372F48;
loc_00373382:
    *(uint32_t *)(v_stack_p8 + 0x58 + 0x38C) = 32;
loc_0037338D:
    goto loc_00372E73;
loc_00373397:
loc_0037339C:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)((uint8_t)(result))))) | (2));
    goto loc_00372C14;
loc_003733A5:
    result = MiSetPageFileAllocationBits(1, 4, (uint32_t)((uint32_t)(v_stack_p8 + 24)), 38);
    a3 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8 + 24))) | (0xFFFFFFFFULL));
    v_stack_mD8 = v_stack_p8 + 152;
    if ((v_stack_p8 + 152) >= (v_stack_mD8 + (uint32_t)((uint32_t)(v_stack_p8 + 24)) * 8)) goto loc_00373425;
loc_003733DA:
    if ((*(uint64_t *)(v_stack_p8 + 0x98)) == (*(uint64_t *)(v_rip + 0xAC4097))) goto loc_0037343C;
loc_003733E6:
    result = *(uint64_t *)(v_rip + 0xAC4097);
    local_r10 = (uint32_t)((uint32_t)(a3));
    if (((uint32_t)((uint32_t)((uint32_t)(a3)))) != ((uint32_t)(a3))) {
        a3 = 4;
        a4 = 0;
        a3 = (uint32_t)((a3) - ((uint32_t)((uint32_t)((uint32_t)(a3)))));
        a2 = (uint32_t)((uint32_t)((uint32_t)(a3)));
        Arg1 = 1;
        result = MiInvalidatePageFileBitmapsCache(Arg1, a2, a3, a4);
        Arg1 = v_stack_mD8;
        a3 = (uint32_t)((a3) | (0xFFFFFFFFULL));
        local_r10 = (uint32_t)(a3);
    }
    Arg1 = (Arg1) + (8);
    local_r12 = (uint32_t)((4) + (1));
    v_stack_mD8 = Arg1;
    if (Arg1 < (v_stack_mD8 + (uint32_t)((uint32_t)(v_stack_p8 + 24)) * 8)) goto loc_003733DA;
loc_00373425:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x68))))) >> (2));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x68))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) + (v_stack_p20));
    *(uint32_t *)(1 + 0x68) = (uint32_t)(Arg1);
    goto loc_003731BF;
loc_0037343C:
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_003733E6;
    if (((uint32_t)(local_r10)) != ((uint32_t)(a3))) goto loc_0037340A;
    goto loc_0037340A;
loc_00373460:
    result = MiPageFileNoFreeSpace(1, v_stack_p8, a3, a4);
    goto loc_00372F4C;
loc_00373470:
    result = KiRaiseIrqlProcessIrqlFlags(4, 1, a3, a4);
    goto loc_00373353;
loc_0037347F:
    v_stack_m90 = (uint32_t)((uint32_t)(*(uint32_t *)(1)));
    v_stack_mC0 = 4;
    v_stack_m88 = *(uint64_t *)(*(uint64_t *)(1 + 0x50) + 0x10);
    result = RtlFindLongestRunClearCapped(v_stack_m90, (uint32_t)((uint32_t)((uint32_t)(v_stack_mBC))), v_stack_mC0, a4);
    v_stack_p20 = (uint32_t)(result);
    result = MiSetPageFileAllocationBits(1, (uint32_t)((uint32_t)((uint32_t)(v_stack_mC0))), (uint32_t)((uint32_t)(result)), a4);
    goto loc_003731BC;
loc_003734BB:
    goto loc_0037339C;
loc_003734C3:
    *(uint8_t *)(v_stack_mA0 + 0x41A) = 1;
    *(uint8_t *)(v_stack_mA0 + 0x418) = 1;
    goto loc_0037320B;
loc_003734D9:
    a2 = 0;
    result = KeDelayExecutionThread(1, a2, v_rip - 3545184, a4);
    Arg1 = 0;
    goto loc_00373221;
loc_003734EE:
    result = (1) + (6);
loc_00373513:
    Arg1 = (uint32_t)((Arg1) - 1);
    local_rbx = (uint32_t)(v_stack_mC0);
    if (result < ((uint32_t)(0x420ULL))) { local_rbx = 4; }
    result = (uint32_t)((result) & ((uint32_t)(Arg1)));
    *(uint32_t *)(v_stack_m98 + result * 8 + 0x38C) = (uint32_t)(result);
    goto loc_00372E73;
loc_0037353A:
    *(uint32_t *)(v_stack_m98 + result * 8 + 0x38C) = 8;
    goto loc_0037338D;
loc_0037354A:
    goto loc_00373052;
loc_00373553:
    a4 = 0;
    a3 = (*(uint64_t *)(v_stack_m98 + result * 8)) >> (12);
    result = MiTransferMemoryPagefileData(1, (uint32_t)(0x420ULL), a3, a4);
    local_r15 = 0;
    *(uint32_t *)(1) = 0;
    *(uint64_t *)(v_stack_m98 + arg1 + 0x6 * 8 + 0x20) = (uint32_t)(*(uint32_t *)(v_stack_m98 + arg1 + 0x6 * 8 + 0x90));
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint8_t)((uint8_t)(result))), 1, a3, a4);
loc_0037359E:
    result = KeLeaveCriticalRegionThread(1, 1, a3, a4);
    goto loc_00372F55;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00372B08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
