# MiGatherMappedPages

- RVA: `0x00404E80`–`0x0040546D` (길이 `1,517` bytes)
- VA: `0x0000000140404E80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009A7D4`
- 디코드: `368`개 명령, `1,517/1,517` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **32**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00404EEC` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00404F21` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x00404F79` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00404FB3` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00404FC0` → [MiReferencePageForModifiedWrite](MiReferencePageForModifiedWrite_function_00405DAC.md) (function, `0x00405DAC`)
- `0x00404FCB` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00404FDB` → [MiReferenceControlAreaFileWithTag](../34/MiReferenceControlAreaFileWithTag_function_00348390.md) (function, `0x00348390`)
- `0x00405004` → [CcNotifyOfMappedWrite](CcNotifyOfMappedWrite_function_0040338C.md) (function, `0x0040338C`)
- `0x00405013` → [MiBuildMappedCluster](MiBuildMappedCluster_function_00405F1C.md) (function, `0x00405F1C`)
- `0x00405055` → [MiStartingOffset](../34/MiStartingOffset_function_003482E0.md) (function, `0x003482E0`)
- `0x004050D4` → [FsRtlAcquireFileForModWriteEx](../29/FsRtlAcquireFileForModWriteEx_function_00299E5C.md) (function, `0x00299E5C`)
- `0x004050F2` → [CcNotifyOfMappedWrite](CcNotifyOfMappedWrite_function_0040338C.md) (function, `0x0040338C`)
- `0x00405105` → [FsRtlReleaseFileForModWrite](../29/FsRtlReleaseFileForModWrite_function_00299100.md) (function, `0x00299100`)
- `0x00405117` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x00405140` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x00405179` → [MiWriteComplete](MiWriteComplete_function_004069B0.md) (function, `0x004069B0`)
- `0x0040518D` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x004051FB` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00405208` → [IoDiskIoAttributionDereference](../34/IoDiskIoAttributionDereference_function_00349978.md) (function, `0x00349978`)
- `0x00405221` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)
- `0x004052AE` → [MiFlushFileOnlyMdl](MiFlushFileOnlyMdl_function_00403208.md) (function, `0x00403208`)
- `0x004052D6` → [MiWriteComplete](MiWriteComplete_function_004069B0.md) (function, `0x004069B0`)
- `0x004052EA` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00405300` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x0040530D` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)
- `0x00405318` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00405332` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00405376` → [IoAsynchronousPageWrite](../29/IoAsynchronousPageWrite_function_00299C08.md) (function, `0x00299C08`)
- `0x00405398` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x004053C5` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004053F0` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00405407` → [ObFastDereferenceObjectDeferDelete](../23/ObFastDereferenceObjectDeferDelete_function_002378C0.md) (function, `0x002378C0`)

### Direct callers
- [MiMappedPageWriter](MiMappedPageWriter_function_00404AC0.md) at `0x00404CC0`

### Static image references
- `0x00404EE1` → RVA `0x000134D0` (`.rdata`; read)
- `0x00404F3B` → RVA `0x00E2DC80` (`.data`; read)
- `0x00405162` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00405348` → RVA `0x004069B0` (`MiWriteComplete`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00404F64` → [sub_006EC390 + 0x19](../6E/Unknown_function_006EC390.md) (`tail-transfer`)
  - `0x004053D1` → [sub_006EC390](../6E/Unknown_function_006EC390.md) (`tail-transfer`)
  - `0x004053E8` → [sub_006EC390](../6E/Unknown_function_006EC390.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00404E80  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00404E85  55                              push rbp
00404E86  56                              push rsi
00404E87  57                              push rdi
00404E88  41 54                           push r12
00404E8A  41 55                           push r13
00404E8C  41 56                           push r14
00404E8E  41 57                           push r15
00404E90  48 81 EC 90 00 00 00            sub rsp, 0x90
00404E97  45 33 FF                        xor r15d, r15d
00404E9A  4D 8B F0                        mov r14, r8
00404E9D  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00404EA2  8B DA                           mov ebx, edx
00404EA4  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00404EA9  48 8B E9                        mov rbp, rcx
00404EAC  48 BE FF FF FF FF 3F 00 00 00   movabs rsi, 0x3fffffffff
00404EB6  45 8D 67 01                     lea r12d, [r15 + 1]
00404EBA  83 FA 10                        cmp edx, 0x10
00404EBD  0F 83 FE 02 00 00               jae 0x1404051c1
00404EC3  41 8B FF                        mov edi, r15d
00404EC6  44 38 BD 1B 04 00 00            cmp byte ptr [rbp + 0x41b], r15b
00404ECD  0F 85 E8 04 00 00               jne 0x1404053bb
00404ED3  8A 85 38 04 00 00               mov al, byte ptr [rbp + 0x438]
00404ED9  84 C0                           test al, al
00404EDB  0F 84 CD 04 00 00               je 0x1404053ae
00404EE1  4C 8D 05 E8 E5 C0 FF            lea r8, [rip - 0x3f1a18]
00404EE8  33 D2                           xor edx, edx
00404EEA  33 C9                           xor ecx, ecx
00404EEC  E8 5F 46 E0 FF                  call 0x140209550
00404EF1  8B C3                           mov eax, ebx
00404EF3  48 83 C0 40                     add rax, 0x40
00404EF7  4C 6B E0 58                     imul r12, rax, 0x58
00404EFB  49 8B 5C 2C 10                  mov rbx, qword ptr [r12 + rbp + 0x10]
00404F00  48 3B DE                        cmp rbx, rsi
00404F03  0F 84 E5 02 00 00               je 0x1404051ee
00404F09  48 8D 3C 5B                     lea rdi, [rbx + rbx*2]
00404F0D  48 C1 E7 04                     shl rdi, 4
00404F11  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00404F1B  48 8B CB                        mov rcx, rbx
00404F1E  48 03 F8                        add rdi, rax
00404F21  E8 FA C6 F1 FF                  call 0x140321620
00404F26  44 8A F8                        mov r15b, al
00404F29  3C 11                           cmp al, 0x11
00404F2B  74 CE                           je 0x140404efb
00404F2D  49 8B 54 2C 10                  mov rdx, qword ptr [r12 + rbp + 0x10]
00404F32  48 3B DA                        cmp rbx, rdx
00404F35  0F 85 F1 03 00 00               jne 0x14040532c
00404F3B  48 8B 05 3E 8D A2 00            mov rax, qword ptr [rip + 0xa28d3e]
00404F42  4C 8B 6F 10                     mov r13, qword ptr [rdi + 0x10]
00404F46  48 85 C0                        test rax, rax
00404F49  74 0C                           je 0x140404f57
00404F4B  41 F6 C5 10                     test r13b, 0x10
00404F4F  75 06                           jne 0x140404f57
00404F51  48 F7 D0                        not rax
00404F54  4C 23 E8                        and r13, rax
00404F57  49 C1 FD 10                     sar r13, 0x10
00404F5B  49 8B 75 00                     mov rsi, qword ptr [r13]
00404F5F  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00404F62  A8 20                           test al, 0x20
00404F64  0F 85 3F 74 2E 00               jne 0x1406ec3a9
00404F6A  A8 08                           test al, 8
00404F6C  0F 85 89 03 00 00               jne 0x1404052fb
00404F72  48 8D 5E 48                     lea rbx, [rsi + 0x48]
00404F76  48 8B CB                        mov rcx, rbx
00404F79  E8 02 3F E4 FF                  call 0x140248e80
00404F7E  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
00404F81  A8 08                           test al, 8
00404F83  0F 85 64 04 00 00               jne 0x1404053ed
00404F89  4C 8B 66 78                     mov r12, qword ptr [rsi + 0x78]
00404F8D  B9 01 00 00 00                  mov ecx, 1
00404F92  01 4E 4C                        add dword ptr [rsi + 0x4c], ecx
00404F95  49 83 E4 F8                     and r12, 0xfffffffffffffff8
00404F99  74 15                           je 0x140404fb0
00404F9B  8B C1                           mov eax, ecx
00404F9D  F0 49 0F C1 44 24 20            lock xadd qword ptr [r12 + 0x20], rax
00404FA4  48 03 C1                        add rax, rcx
00404FA7  48 3B C1                        cmp rax, rcx
00404FAA  0F 8E F2 03 00 00               jle 0x1404053a2
00404FB0  48 8B CB                        mov rcx, rbx
00404FB3  E8 28 48 E4 FF                  call 0x1402497e0
00404FB8  BA 01 00 00 00                  mov edx, 1
00404FBD  48 8B CF                        mov rcx, rdi
00404FC0  E8 E7 0D 00 00                  call 0x140405dac
00404FC5  41 8A D7                        mov dl, r15b
00404FC8  48 8B CF                        mov rcx, rdi
00404FCB  E8 10 54 F1 FF                  call 0x14031a3e0
00404FD0  45 33 C0                        xor r8d, r8d
00404FD3  BA 4D 6D 53 63                  mov edx, 0x63536d4d
00404FD8  48 8B CE                        mov rcx, rsi
00404FDB  E8 B0 33 F4 FF                  call 0x140348390
00404FE0  80 BD 1B 04 00 00 00            cmp byte ptr [rbp + 0x41b], 0
00404FE7  4C 8B F8                        mov r15, rax
00404FEA  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00404FEE  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00404FF3  0F 85 F9 01 00 00               jne 0x1404051f2
00404FF9  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00404FFE  45 33 C0                        xor r8d, r8d
00405001  48 8B C8                        mov rcx, rax
00405004  E8 83 E3 FF FF                  call 0x14040338c
00405009  44 8B C0                        mov r8d, eax
0040500C  49 8D 56 68                     lea rdx, [r14 + 0x68]
00405010  48 8B CF                        mov rcx, rdi
00405013  E8 04 0F 00 00                  call 0x140405f1c
00405018  49 89 46 60                     mov qword ptr [r14 + 0x60], rax
0040501C  48 8B F8                        mov rdi, rax
0040501F  49 89 76 48                     mov qword ptr [r14 + 0x48], rsi
00405023  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00405028  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
0040502C  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00405030  48 03 D2                        add rdx, rdx
00405033  48 B8 08 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000008
0040503D  48 8B 14 D0                     mov rdx, qword ptr [rax + rdx*8]
00405041  41 83 C8 FF                     or r8d, 0xffffffff
00405045  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0040504F  49 8B CD                        mov rcx, r13
00405052  48 0B D0                        or rdx, rax
00405055  E8 86 32 F4 FF                  call 0x1403482e0
0040505A  41 8B 56 28                     mov edx, dword ptr [r14 + 0x28]
0040505E  48 8B D8                        mov rbx, rax
00405061  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00405066  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00405069  41 89 46 2C                     mov dword ptr [r14 + 0x2c], eax
0040506D  C1 E8 0C                        shr eax, 0xc
00405070  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00405077  FF C8                           dec eax
00405079  41 89 46 30                     mov dword ptr [r14 + 0x30], eax
0040507D  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00405080  49 8D 7E 50                     lea rdi, [r14 + 0x50]
00405084  48 83 27 00                     and qword ptr [rdi], 0
00405088  48 03 C3                        add rax, rbx
0040508B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00405090  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00405094  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
00405097  8B C2                           mov eax, edx
00405099  83 E0 FD                        and eax, 0xfffffffd
0040509C  83 CA 02                        or edx, 2
0040509F  F6 C1 10                        test cl, 0x10
004050A2  B9 04 00 00 00                  mov ecx, 4
004050A7  0F 44 D0                        cmove edx, eax
004050AA  83 A4 24 D8 00 00 00 00         and dword ptr [rsp + 0xd8], 0
004050B2  41 89 56 28                     mov dword ptr [r14 + 0x28], edx
004050B6  8B 46 38                        mov eax, dword ptr [rsi + 0x38]
004050B9  84 C1                           test cl, al
004050BB  75 76                           jne 0x140405133
004050BD  A8 10                           test al, 0x10
004050BF  0F 85 35 03 00 00               jne 0x1404053fa
004050C5  4C 8B C7                        mov r8, rdi
004050C8  4D 89 7E 40                     mov qword ptr [r14 + 0x40], r15
004050CC  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
004050D1  49 8B CF                        mov rcx, r15
004050D4  E8 83 4D E9 FF                  call 0x140299e5c
004050D9  85 C0                           test eax, eax
004050DB  0F 88 2E 01 00 00               js 0x14040520f
004050E1  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
004050E6  48 8B D3                        mov rdx, rbx
004050E9  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
004050EE  45 8B 40 28                     mov r8d, dword ptr [r8 + 0x28]
004050F2  E8 95 E2 FF FF                  call 0x14040338c
004050F7  85 C0                           test eax, eax
004050F9  0F 85 41 01 00 00               jne 0x140405240
004050FF  48 8B 17                        mov rdx, qword ptr [rdi]
00405102  49 8B CF                        mov rcx, r15
00405105  E8 F6 3F E9 FF                  call 0x140299100
0040510A  48 8D 4E 40                     lea rcx, [rsi + 0x40]
0040510E  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
00405114  49 8B D7                        mov rdx, r15
00405117  E8 A4 27 E3 FF                  call 0x1402378c0
0040511C  49 83 66 40 00                  and qword ptr [r14 + 0x40], 0
00405121  BA 01 00 00 00                  mov edx, 1
00405126  48 83 27 00                     and qword ptr [rdi], 0
0040512A  BB 54 00 00 C0                  mov ebx, 0xc0000054
0040512F  8B FA                           mov edi, edx
00405131  EB 1E                           jmp 0x140405151
00405133  48 8D 4E 40                     lea rcx, [rsi + 0x40]
00405137  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
0040513D  49 8B D7                        mov rdx, r15
00405140  E8 7B 27 E3 FF                  call 0x1402378c0
00405145  BA 01 00 00 00                  mov edx, 1
0040514A  BB 54 00 00 C0                  mov ebx, 0xc0000054
0040514F  8B FA                           mov edi, edx
00405151  49 83 66 20 00                  and qword ptr [r14 + 0x20], 0
00405156  41 89 5E 18                     mov dword ptr [r14 + 0x18], ebx
0040515A  44 0F 20 C3                     mov rbx, cr8
0040515E  44 0F 22 C2                     mov cr8, rdx
00405162  83 3D B7 1B BC 00 00            cmp dword ptr [rip + 0xbc1bb7], 0
00405169  0F 85 8A 00 00 00               jne 0x1404051f9
0040516F  44 8B C7                        mov r8d, edi
00405172  49 8D 56 18                     lea rdx, [r14 + 0x18]
00405176  49 8B CE                        mov rcx, r14
00405179  E8 32 18 00 00                  call 0x1404069b0
0040517E  83 3D 9B 1B BC 00 00            cmp dword ptr [rip + 0xbc1b9b], 0
00405185  74 0B                           je 0x140405192
00405187  44 0F 20 C1                     mov rcx, cr8
0040518B  8A D3                           mov dl, bl
0040518D  E8 06 05 0F 00                  call 0x1404f5698
00405192  0F B6 D3                        movzx edx, bl
00405195  44 0F 22 C2                     mov cr8, rdx
00405199  BE 01 00 00 00                  mov esi, 1
0040519E  4D 85 E4                        test r12, r12
004051A1  75 62                           jne 0x140405205
004051A3  8B C6                           mov eax, esi
004051A5  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
004051AD  48 81 C4 90 00 00 00            add rsp, 0x90
004051B4  41 5F                           pop r15
004051B6  41 5E                           pop r14
004051B8  41 5D                           pop r13
004051BA  41 5C                           pop r12
004051BC  5F                              pop rdi
004051BD  5E                              pop rsi
004051BE  5D                              pop rbp
004051BF  C3                              ret
004051C0  CC                              int3
004051C1  41 8B DF                        mov ebx, r15d
004051C4  48 81 C1 10 16 00 00            add rcx, 0x1610
004051CB  48 8B 01                        mov rax, qword ptr [rcx]
004051CE  48 3B C6                        cmp rax, rsi
004051D1  0F 85 EC FC FF FF               jne 0x140404ec3
004051D7  41 03 DC                        add ebx, r12d
004051DA  48 83 C1 58                     add rcx, 0x58
004051DE  8B C3                           mov eax, ebx
004051E0  83 FB 10                        cmp ebx, 0x10
004051E3  72 E6                           jb 0x1404051cb
004051E5  83 F8 10                        cmp eax, 0x10
004051E8  0F 85 D5 FC FF FF               jne 0x140404ec3
004051EE  33 C0                           xor eax, eax
004051F0  EB B3                           jmp 0x1404051a5
004051F2  33 C0                           xor eax, eax
004051F4  E9 10 FE FF FF                  jmp 0x140405009
004051F9  8A CB                           mov cl, bl
004051FB  E8 FC 04 0F 00                  call 0x1404f56fc
00405200  E9 6A FF FF FF                  jmp 0x14040516f
00405205  49 8B CC                        mov rcx, r12
00405208  E8 6B 47 F4 FF                  call 0x140349978
0040520D  EB 94                           jmp 0x1404051a3
0040520F  48 8D 4E 40                     lea rcx, [rsi + 0x40]
00405213  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
00405219  49 8B D7                        mov rdx, r15
0040521C  BB 54 00 00 C0                  mov ebx, 0xc0000054
00405221  E8 9A 26 E3 FF                  call 0x1402378c0
00405226  49 83 66 40 00                  and qword ptr [r14 + 0x40], 0
0040522B  48 83 27 00                     and qword ptr [rdi], 0
0040522F  8B BC 24 D8 00 00 00            mov edi, dword ptr [rsp + 0xd8]
00405236  BA 01 00 00 00                  mov edx, 1
0040523B  E9 11 FF FF FF                  jmp 0x140405151
00405240  B9 01 00 00 00                  mov ecx, 1
00405245  3B C1                           cmp eax, ecx
00405247  0F 84 D0 01 00 00               je 0x14040541d
0040524D  49 89 5E 58                     mov qword ptr [r14 + 0x58], rbx
00405251  8B 8D E0 02 00 00               mov ecx, dword ptr [rbp + 0x2e0]
00405257  48 8B 85 00 49 00 00            mov rax, qword ptr [rbp + 0x4900]
0040525E  85 C9                           test ecx, ecx
00405260  0F 85 BF 01 00 00               jne 0x140405425
00405266  48 3D 20 01 00 00               cmp rax, 0x120
0040526C  0F 82 DD 01 00 00               jb 0x14040544f
00405272  8D 51 02                        lea edx, [rcx + 2]
00405275  65 FF 04 25 B4 2E 00 00         inc dword ptr gs:[0x2eb4]
0040527D  49 8D 7E 18                     lea rdi, [r14 + 0x18]
00405281  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00405288  65 01 04 25 B0 2E 00 00         add dword ptr gs:[0x2eb0], eax
00405290  F6 46 3E 0C                     test byte ptr [rsi + 0x3e], 0xc
00405294  0F 84 A2 00 00 00               je 0x14040533c
0040529A  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0040529F  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
004052A4  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
004052A9  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
004052AE  E8 55 DF FF FF                  call 0x140403208
004052B3  44 0F 20 C3                     mov rbx, cr8
004052B7  BE 01 00 00 00                  mov esi, 1
004052BC  44 0F 22 C6                     mov cr8, rsi
004052C0  83 3D 59 1A BC 00 00            cmp dword ptr [rip + 0xbc1a59], 0
004052C7  0F 85 C6 00 00 00               jne 0x140405393
004052CD  45 33 C0                        xor r8d, r8d
004052D0  48 8B D7                        mov rdx, rdi
004052D3  49 8B CE                        mov rcx, r14
004052D6  E8 D5 16 00 00                  call 0x1404069b0
004052DB  83 3D 3E 1A BC 00 00            cmp dword ptr [rip + 0xbc1a3e], 0
004052E2  74 0B                           je 0x1404052ef
004052E4  44 0F 20 C1                     mov rcx, cr8
004052E8  8A D3                           mov dl, bl
004052EA  E8 A9 03 0F 00                  call 0x1404f5698
004052EF  0F B6 C3                        movzx eax, bl
004052F2  44 0F 22 C0                     mov cr8, rax
004052F6  E9 A3 FE FF FF                  jmp 0x14040519e
004052FB  33 D2                           xor edx, edx
004052FD  48 8B CF                        mov rcx, rdi
00405300  E8 8B 22 E8 FF                  call 0x140287590
00405305  BA 10 00 00 00                  mov edx, 0x10
0040530A  48 8B CF                        mov rcx, rdi
0040530D  E8 EE 4C EB FF                  call 0x1402ba000
00405312  41 8A D7                        mov dl, r15b
00405315  48 8B CF                        mov rcx, rdi
00405318  E8 C3 50 F1 FF                  call 0x14031a3e0
0040531D  48 BE FF FF FF FF 3F 00 00 00   movabs rsi, 0x3fffffffff
00405327  E9 CF FB FF FF                  jmp 0x140404efb
0040532C  41 8A D7                        mov dl, r15b
0040532F  48 8B CF                        mov rcx, rdi
00405332  E8 A9 50 F1 FF                  call 0x14031a3e0
00405337  E9 BF FB FF FF                  jmp 0x140404efb
0040533C  49 8D 46 10                     lea rax, [r14 + 0x10]
00405340  49 8B CF                        mov rcx, r15
00405343  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00405348  4C 8D 0D 61 16 00 00            lea r9, [rip + 0x1661]
0040534F  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00405354  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00405359  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0040535E  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
00405363  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00405368  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
0040536C  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00405371  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00405376  E8 8D 48 E9 FF                  call 0x140299c08
0040537B  8B C8                           mov ecx, eax
0040537D  8B D8                           mov ebx, eax
0040537F  B8 00 00 00 C0                  mov eax, 0xc0000000
00405384  23 C8                           and ecx, eax
00405386  3B C8                           cmp ecx, eax
00405388  0F 85 0B FE FF FF               jne 0x140405199
0040538E  E9 9C FE FF FF                  jmp 0x14040522f
00405393  40 8A D6                        mov dl, sil
00405396  8A CB                           mov cl, bl
00405398  E8 5F 03 0F 00                  call 0x1404f56fc
0040539D  E9 2B FF FF FF                  jmp 0x1404052cd
004053A2  B9 0E 00 00 00                  mov ecx, 0xe
004053A7  CD 29                           int 0x29
004053A9  E9 02 FC FF FF                  jmp 0x140404fb0
004053AE  85 FF                           test edi, edi
004053B0  0F 85 2B FB FF FF               jne 0x140404ee1
004053B6  E9 36 FB FF FF                  jmp 0x140404ef1
004053BB  48 8D B5 14 04 00 00            lea rsi, [rbp + 0x414]
004053C2  48 8B CE                        mov rcx, rsi
004053C5  E8 C6 32 E4 FF                  call 0x140248690
004053CA  44 38 BD 1D 04 00 00            cmp byte ptr [rbp + 0x41d], r15b
004053D1  0F 84 B9 6F 2E 00               je 0x1406ec390
004053D7  44 88 BD 1D 04 00 00            mov byte ptr [rbp + 0x41d], r15b
004053DE  41 8B FC                        mov edi, r12d
004053E1  44 88 BD 1B 04 00 00            mov byte ptr [rbp + 0x41b], r15b
004053E8  E9 A3 6F 2E 00                  jmp 0x1406ec390
004053ED  48 8B CB                        mov rcx, rbx
004053F0  E8 EB 43 E4 FF                  call 0x1402497e0
004053F5  E9 01 FF FF FF                  jmp 0x1404052fb
004053FA  48 8D 4E 40                     lea rcx, [rsi + 0x40]
004053FE  41 B8 4D 6D 53 63               mov r8d, 0x63536d4d
00405404  49 8B D7                        mov rdx, r15
00405407  E8 B4 24 E3 FF                  call 0x1402378c0
0040540C  BA 01 00 00 00                  mov edx, 1
00405411  BB 98 00 00 C0                  mov ebx, 0xc0000098
00405416  8B FA                           mov edi, edx
00405418  E9 34 FD FF FF                  jmp 0x140405151
0040541D  48 09 0F                        or qword ptr [rdi], rcx
00405420  E9 28 FE FF FF                  jmp 0x14040524d
00405425  BA 02 00 00 00                  mov edx, 2
0040542A  41 B8 20 04 00 00               mov r8d, 0x420
00405430  49 3B C0                        cmp rax, r8
00405433  FF C9                           dec ecx
00405435  44 8D 4A 02                     lea r9d, [rdx + 2]
00405439  41 0F 42 D1                     cmovb edx, r9d
0040543D  49 3B C0                        cmp rax, r8
00405440  1B C0                           sbb eax, eax
00405442  23 C1                           and eax, ecx
00405444  89 85 E0 02 00 00               mov dword ptr [rbp + 0x2e0], eax
0040544A  E9 26 FE FF FF                  jmp 0x140405275
0040544F  48 3D A0 00 00 00               cmp rax, 0xa0
00405455  BA 04 00 00 00                  mov edx, 4
0040545A  1B C0                           sbb eax, eax
0040545C  83 E0 18                        and eax, 0x18
0040545F  83 C0 08                        add eax, 8
00405462  89 85 E0 02 00 00               mov dword ptr [rbp + 0x2e0], eax
00405468  E9 08 FE FF FF                  jmp 0x140405275
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGatherMappedPages(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pD8;
    unsigned int v_stack_pE8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    v_r15 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if (a2 >= 16) goto loc_004051C1;
loc_00404EC3:
    if ((*(unsigned __int8 *)(a1 + 1051)) != 0) goto loc_004053BB;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 1080)) == 0) goto loc_004053AE;
loc_00404EE1:
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip - 4135448, a4);
loc_00404EF1:
    result = ((unsigned int)((unsigned int)((unsigned int)(a2)))) + (64);
    v_r12 = (v_r15 + 1) * (result);
loc_00404EFB:
    if ((*(unsigned __int64 *)(v_r12 + a1 * 1 + 16)) == v_rsi) goto loc_004051EE;
    v_rdi = (*(unsigned __int64 *)(v_r12 + a1 * 1 + 16) + *(unsigned __int64 *)(v_r12 + a1 * 1 + 16) * 2) << (4);
    v_rdi = (v_rdi) + (result);
    result = MiSafeLockPage(*(unsigned __int64 *)(v_r12 + a1 * 1 + 16), a2, v_rip - 4135448, a4);
    if (((unsigned __int8)(result)) == 17) goto loc_00404EFB;
    if ((*(unsigned __int64 *)(v_r12 + a1 * 1 + 16)) != (*(unsigned __int64 *)(v_r12 + a1 * 1 + 16))) goto loc_0040532C;
    if (*(unsigned __int64 *)(v_rip + 10652990) == 0) goto loc_00404F57;
    result = *(unsigned __int64 *)(v_rip + 10652990);
    v_r13 = *(unsigned __int64 *)(v_rdi + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 10652990));
        v_r13 = (*(unsigned __int64 *)(v_rdi + 16)) & (result);
    }
    v_r13 = (v_r13) >> (16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13) + 56)))) & (8)) != 0) goto loc_004052FB;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(unsigned __int64 *)(v_r13) + 72, *(unsigned __int64 *)(v_r12 + a1 * 1 + 16), v_rip - 4135448, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13) + 56)))) & (8)) != 0) goto loc_004053ED;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r13) + 120)) & (-8);
    if (condition_is_equal) goto loc_00404FB0;
    result = (1) + (1);
    if (result <= 1) goto loc_004053A2;
loc_00404FB0:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(unsigned __int64 *)(v_r13) + 72, *(unsigned __int64 *)(v_r12 + a1 * 1 + 16), v_rip - 4135448, a4);
    result = MiReferencePageForModifiedWrite(v_rdi, 1, v_rip - 4135448, a4);
    result = MiUnlockPage(v_rdi, (unsigned __int8)((unsigned __int8)(result)), v_rip - 4135448, a4);
    a3 = 0;
    result = MiReferenceControlAreaFileWithTag(*(unsigned __int64 *)(v_r13), (unsigned int)(0x63536D4DULL), a3, a4);
    v_stack_m50 = *(unsigned __int64 *)(result + 40);
    if ((*(unsigned __int8 *)(a1 + 1051)) != 0) goto loc_004051F2;
    a3 = 0;
    result = CcNotifyOfMappedWrite(*(unsigned __int64 *)(result + 40), v_stack_m68, a3, a4);
loc_00405009:
    result = MiBuildMappedCluster(v_rdi, a3 + 104, (unsigned int)((unsigned int)(result)), a4);
    *(unsigned __int64 *)(a3 + 96) = result;
    *(unsigned __int64 *)(a3 + 72) = *(unsigned __int64 *)(v_r13);
    v_stack_m60 = result;
    a2 = (*(unsigned __int64 *)(result + 48) + *(unsigned __int64 *)(result + 48) * 2) + (*(unsigned __int64 *)(result + 48) + *(unsigned __int64 *)(result + 48) * 2);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (0xFFFFFFFFULL));
    a2 = (*(unsigned __int64 *)(result + a2 * 8)) | (result);
    result = MiStartingOffset(v_r13, a2, a3, a4);
    v_stack_m68 = result;
    *(unsigned int *)(a3 + 44) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 40)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) >> (12));
    v_stack_p20 = (unsigned int)(result);
    result = (unsigned int)((result) - 1);
    *(unsigned int *)(a3 + 48) = (unsigned int)(result);
    result = ((unsigned int)(*(unsigned int *)(result + 40))) + (result);
    v_stack_m58 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 40))))) & (0xFFFFFFFDULL));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 40))) | (2));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 8) + 52)))) & (16)) == 0) { a2 = (unsigned int)(result); }
    *(unsigned int *)(a3 + 40) = a2;
    if (((4) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13) + 56))))) != 0) goto loc_00405133;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r13) + 56)))) & (16)) != 0) goto loc_004053FA;
    *(unsigned __int64 *)(a3 + 64) = result;
    result = FsRtlAcquireFileForModWriteEx(result, v_stack_m58, a3 + 80, a4);
    if (sign_flag) goto loc_0040520F;
    result = CcNotifyOfMappedWrite(v_stack_m50, result, (unsigned int)(*(unsigned int *)(v_stack_m60 + 40)), a4);
    if ((unsigned int)(result) != 0) goto loc_00405240;
    result = FsRtlReleaseFileForModWrite(result, *(unsigned __int64 *)(a3 + 80), (unsigned int)(*(unsigned int *)(v_stack_m60 + 40)), a4);
    result = ObFastDereferenceObjectDeferDelete(*(unsigned __int64 *)(v_r13) + 64, result, (unsigned int)(0x63536D4DULL), a4);
    goto loc_00405151;
loc_00405133:
    result = ObFastDereferenceObjectDeferDelete(*(unsigned __int64 *)(v_r13) + 64, result, (unsigned int)(0x63536D4DULL), a4);
loc_00405151:
    *(unsigned int *)(a3 + 24) = (unsigned int)((unsigned int)(0xC0000054ULL));
    if ((*(unsigned int *)(v_rip + 12327863)) != 0) goto loc_004051F9;
loc_0040516F:
    result = MiWriteComplete(a3, a3 + 24, 1, a4);
    if ((*(unsigned int *)(v_rip + 12327835)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 1, a4);
    }
loc_00405199:
loc_0040519E:
    if (v_r12 != 0) goto loc_00405205;
loc_004051A3:
loc_004051A5:
    v_rsp = (v_rsp) + (144);
    return 1;
loc_004051C1:
    a1 = (a1) + (0x1610ULL);
loc_004051CB:
    if ((*(unsigned __int64 *)(a1)) != 1) goto loc_00404EC3;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)(v_r12)));
    a1 = (a1) + (88);
    if (((unsigned int)(v_rbx)) < 16) goto loc_004051CB;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != 16) goto loc_00404EC3;
loc_004051EE:
    result = 0;
    goto loc_004051A5;
loc_004051F2:
    result = 0;
    goto loc_00405009;
loc_004051F9:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rbx), (unsigned __int8)(v_cr8), 1, a4);
    goto loc_0040516F;
loc_00405205:
    result = IoDiskIoAttributionDereference(v_r12, (unsigned __int8)(v_cr8), 1, a4);
    goto loc_004051A3;
loc_0040520F:
    result = ObFastDereferenceObjectDeferDelete(1 + 64, result, (unsigned int)(0x63536D4DULL), a4);
loc_0040522F:
    goto loc_00405151;
loc_00405240:
    if (((unsigned int)(result)) == 1) goto loc_0040541D;
loc_0040524D:
    *(unsigned __int64 *)(a3 + 88) = (unsigned int)(0xC0000054ULL);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 736))) != 0) goto loc_00405425;
    if ((*(unsigned __int64 *)(a1 + 18688)) < 288) goto loc_0040544F;
loc_00405275:
    if (((*(unsigned __int8 *)(1 + 62)) & (12)) == 0) goto loc_0040533C;
    v_stack_p28 = a3 + 24;
    v_stack_p20 = v_r13;
    result = MiFlushFileOnlyMdl((unsigned int)(*(unsigned int *)(a1 + 736)), v_stack_p68, v_stack_p60, a4);
    if ((*(unsigned int *)(v_rip + 12327513)) != 0) goto loc_00405393;
loc_004052CD:
    a3 = 0;
    result = MiWriteComplete(0, a3 + 24, a3, a4);
    if ((*(unsigned int *)(v_rip + 12327486)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    goto loc_0040519E;
loc_004052FB:
    a2 = 0;
    result = MiUnlinkPageFromListEx(a3 + 24, a2, a3, a4);
    result = MiInsertPageInList(a3 + 24, 16, a3, a4);
    result = MiUnlockPage(a3 + 24, (unsigned __int8)(result), a3, a4);
    goto loc_00404EFB;
loc_0040532C:
    result = MiUnlockPage(a3 + 24, (unsigned __int8)(result), a3, a4);
    goto loc_00404EFB;
loc_0040533C:
    v_stack_p50 = a3 + 16;
    v_stack_p48 = a3 + 24;
    v_stack_p40 = v_r12;
    v_stack_p38 = 0;
    v_stack_p28 = (unsigned int)((unsigned __int8)(result));
    v_stack_p20 = 0;
    result = IoAsynchronousPageWrite(result, v_stack_p68, v_stack_p60, v_rip + 5729);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000000ULL))));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(0xC0000000ULL)))) goto loc_00405199;
    goto loc_0040522F;
loc_00405393:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)((unsigned int)((unsigned int)(result))), 1, v_stack_p60, v_rip + 5729);
    goto loc_004052CD;
loc_004053A2:
    goto loc_00404FB0;
loc_004053AE:
    if ((unsigned int)(a3 + 24) != 0) goto loc_00404EE1;
    goto loc_00404EF1;
loc_004053BB:
    result = ExAcquireSpinLockExclusive(a1 + 1044, 1, v_stack_p60, v_rip + 5729);
    *(unsigned __int8 *)(a1 + 1053) = (unsigned __int8)(result);
    *(unsigned __int8 *)(a1 + 1051) = (unsigned __int8)(result);
loc_004053ED:
    result = ExReleaseSpinLockExclusiveFromDpcLevel((unsigned int)((unsigned int)(result)), 1, v_stack_p60, v_rip + 5729);
    goto loc_004052FB;
loc_004053FA:
    result = ObFastDereferenceObjectDeferDelete(a1 + 1044 + 64, result, (unsigned int)(0x63536D4DULL), v_rip + 5729);
    goto loc_00405151;
loc_0040541D:
    goto loc_0040524D;
loc_00405425:
    a1 = (unsigned int)((a1 + 1044 + 64) - 1);
    a2 = 2;
    if (result < ((unsigned int)(0x420ULL))) { a2 = (unsigned int)(2 + 2); }
    result = (unsigned int)((result) & ((unsigned int)(a1)));
    *(unsigned int *)(a1 + 736) = (unsigned int)(result);
    goto loc_00405275;
loc_0040544F:
    result = (unsigned int)((result) & (24));
    result = (unsigned int)((result) + (8));
    *(unsigned int *)(a1 + 736) = (unsigned int)(result);
    goto loc_00405275;
}
```

## 5. (Beta) C Style

```c
int64_t MiGatherMappedPages(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint8_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint32_t v_stack_pD8;
    uint32_t v_stack_pE8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    local_r15 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if (Arg2 >= 16) goto loc_004051C1;
loc_00404EC3:
    if ((*(uint8_t *)(arg1 + 0x41B)) != 0) goto loc_004053BB;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x438)) == 0) goto loc_004053AE;
loc_00404EE1:
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip - 4135448, a4);
loc_00404EF1:
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg2)))) + (64);
    local_r12 = (local_r15 + 1) * (result);
loc_00404EFB:
    if ((*(uint64_t *)(local_r12 + arg1 * 1 + 0x10)) == local_rsi) goto loc_004051EE;
    local_rdi = (*(uint64_t *)(local_r12 + arg1 * 1 + 0x10) + *(uint64_t *)(local_r12 + arg1 * 1 + 0x10) * 2) << (4);
    local_rdi = (local_rdi) + (result);
    result = MiSafeLockPage(*(uint64_t *)(local_r12 + arg1 * 1 + 0x10), Arg2, v_rip - 4135448, a4);
    if (((uint8_t)(result)) == 17) goto loc_00404EFB;
    if ((*(uint64_t *)(local_r12 + arg1 * 1 + 0x10)) != (*(uint64_t *)(local_r12 + arg1 * 1 + 0x10))) goto loc_0040532C;
    if (*(uint64_t *)(v_rip + 0xA28D3E) == 0) goto loc_00404F57;
    result = *(uint64_t *)(v_rip + 0xA28D3E);
    local_r13 = *(uint64_t *)(local_rdi + 0x10);
    if ((((uint8_t)(*(uint64_t *)(local_rdi + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xA28D3E));
        local_r13 = (*(uint64_t *)(local_rdi + 0x10)) & (result);
    }
    local_r13 = (local_r13) >> (16);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13) + 0x38)))) & (8)) != 0) goto loc_004052FB;
    result = ExAcquireSpinLockExclusiveAtDpcLevel(*(uint64_t *)(local_r13) + 72, *(uint64_t *)(local_r12 + arg1 * 1 + 0x10), v_rip - 4135448, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13) + 0x38)))) & (8)) != 0) goto loc_004053ED;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(local_r13) + 0x78)) & (-8);
    if (condition_is_equal) goto loc_00404FB0;
    result = (1) + (1);
    if (result <= 1) goto loc_004053A2;
loc_00404FB0:
    result = ExReleaseSpinLockExclusiveFromDpcLevel(*(uint64_t *)(local_r13) + 72, *(uint64_t *)(local_r12 + arg1 * 1 + 0x10), v_rip - 4135448, a4);
    result = MiReferencePageForModifiedWrite(local_rdi, 1, v_rip - 4135448, a4);
    result = MiUnlockPage(local_rdi, (uint8_t)((uint8_t)(result)), v_rip - 4135448, a4);
    Arg3 = 0;
    result = MiReferenceControlAreaFileWithTag(*(uint64_t *)(local_r13), (uint32_t)(0x63536D4DULL), Arg3, a4);
    v_stack_m50 = *(uint64_t *)(result + 0x28);
    if ((*(uint8_t *)(arg1 + 0x41B)) != 0) goto loc_004051F2;
    Arg3 = 0;
    result = CcNotifyOfMappedWrite(*(uint64_t *)(result + 0x28), v_stack_m68, Arg3, a4);
loc_00405009:
    result = MiBuildMappedCluster(local_rdi, Arg3 + 104, (uint32_t)((uint32_t)(result)), a4);
    *(uint64_t *)(arg3 + 0x60) = result;
    *(uint64_t *)(arg3 + 0x48) = *(uint64_t *)(local_r13);
    v_stack_m60 = result;
    Arg2 = (*(uint64_t *)(result + 0x30) + *(uint64_t *)(result + 0x30) * 2) + (*(uint64_t *)(result + 0x30) + *(uint64_t *)(result + 0x30) * 2);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (0xFFFFFFFFULL));
    Arg2 = (*(uint64_t *)(result + Arg2 * 8)) | (result);
    result = MiStartingOffset(local_r13, Arg2, Arg3, a4);
    v_stack_m68 = result;
    *(uint32_t *)(arg3 + 0x2C) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x28)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) >> (12));
    v_stack_p20 = (uint32_t)(result);
    result = (uint32_t)((result) - 1);
    *(uint32_t *)(arg3 + 0x30) = (uint32_t)(result);
    result = ((uint32_t)(*(uint32_t *)(result + 0x28))) + (result);
    v_stack_m58 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x28))))) & (0xFFFFFFFDULL));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3 + 0x28))) | (2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x8) + 0x34)))) & (16)) == 0) { Arg2 = (uint32_t)(result); }
    *(uint32_t *)(arg3 + 0x28) = Arg2;
    if (((4) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13) + 0x38))))) != 0) goto loc_00405133;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r13) + 0x38)))) & (16)) != 0) goto loc_004053FA;
    *(uint64_t *)(arg3 + 0x40) = result;
    result = FsRtlAcquireFileForModWriteEx(result, v_stack_m58, Arg3 + 80, a4);
    if (sign_flag) goto loc_0040520F;
    result = CcNotifyOfMappedWrite(v_stack_m50, result, (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x28)), a4);
    if ((uint32_t)(result) != 0) goto loc_00405240;
    result = FsRtlReleaseFileForModWrite(result, *(uint64_t *)(arg3 + 0x50), (uint32_t)(*(uint32_t *)(v_stack_m60 + 0x28)), a4);
    result = ObFastDereferenceObjectDeferDelete(*(uint64_t *)(local_r13) + 64, result, (uint32_t)(0x63536D4DULL), a4);
    goto loc_00405151;
loc_00405133:
    result = ObFastDereferenceObjectDeferDelete(*(uint64_t *)(local_r13) + 64, result, (uint32_t)(0x63536D4DULL), a4);
loc_00405151:
    *(uint32_t *)(arg3 + 0x18) = (uint32_t)((uint32_t)(0xC0000054ULL));
    if ((*(uint32_t *)(v_rip + 0xBC1BB7)) != 0) goto loc_004051F9;
loc_0040516F:
    result = MiWriteComplete(Arg3, Arg3 + 24, 1, a4);
    if ((*(uint32_t *)(v_rip + 0xBC1B9B)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 1, a4);
    }
loc_00405199:
loc_0040519E:
    if (local_r12 != 0) goto loc_00405205;
loc_004051A3:
loc_004051A5:
    local_rsp = (local_rsp) + (144);
    return 1;
loc_004051C1:
    Arg1 = (Arg1) + (0x1610ULL);
loc_004051CB:
    if ((*(uint64_t *)(arg1)) != 1) goto loc_00404EC3;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)(local_r12)));
    Arg1 = (Arg1) + (88);
    if (((uint32_t)(local_rbx)) < 16) goto loc_004051CB;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != 16) goto loc_00404EC3;
loc_004051EE:
    result = 0;
    goto loc_004051A5;
loc_004051F2:
    result = 0;
    goto loc_00405009;
loc_004051F9:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rbx), (uint8_t)(v_cr8), 1, a4);
    goto loc_0040516F;
loc_00405205:
    result = IoDiskIoAttributionDereference(local_r12, (uint8_t)(v_cr8), 1, a4);
    goto loc_004051A3;
loc_0040520F:
    result = ObFastDereferenceObjectDeferDelete(1 + 64, result, (uint32_t)(0x63536D4DULL), a4);
loc_0040522F:
    goto loc_00405151;
loc_00405240:
    if (((uint32_t)(result)) == 1) goto loc_0040541D;
loc_0040524D:
    *(uint64_t *)(arg3 + 0x58) = (uint32_t)(0xC0000054ULL);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2E0))) != 0) goto loc_00405425;
    if ((*(uint64_t *)(arg1 + 0x4900)) < 288) goto loc_0040544F;
loc_00405275:
    if (((*(uint8_t *)(1 + 0x3E)) & (12)) == 0) goto loc_0040533C;
    v_stack_p28 = Arg3 + 24;
    v_stack_p20 = local_r13;
    result = MiFlushFileOnlyMdl((uint32_t)(*(uint32_t *)(arg1 + 0x2E0)), v_stack_p68, v_stack_p60, a4);
    if ((*(uint32_t *)(v_rip + 0xBC1A59)) != 0) goto loc_00405393;
loc_004052CD:
    Arg3 = 0;
    result = MiWriteComplete(0, Arg3 + 24, Arg3, a4);
    if ((*(uint32_t *)(v_rip + 0xBC1A3E)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, a4);
    }
    goto loc_0040519E;
loc_004052FB:
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(Arg3 + 24, Arg2, Arg3, a4);
    result = MiInsertPageInList(Arg3 + 24, 16, Arg3, a4);
    result = MiUnlockPage(Arg3 + 24, (uint8_t)(result), Arg3, a4);
    goto loc_00404EFB;
loc_0040532C:
    result = MiUnlockPage(Arg3 + 24, (uint8_t)(result), Arg3, a4);
    goto loc_00404EFB;
loc_0040533C:
    v_stack_p50 = Arg3 + 16;
    v_stack_p48 = Arg3 + 24;
    v_stack_p40 = local_r12;
    v_stack_p38 = 0;
    v_stack_p28 = (uint32_t)((uint8_t)(result));
    v_stack_p20 = 0;
    result = IoAsynchronousPageWrite(result, v_stack_p68, v_stack_p60, v_rip + 5729);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000000ULL))));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(0xC0000000ULL)))) goto loc_00405199;
    goto loc_0040522F;
loc_00405393:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)((uint32_t)((uint32_t)(result))), 1, v_stack_p60, v_rip + 5729);
    goto loc_004052CD;
loc_004053A2:
    goto loc_00404FB0;
loc_004053AE:
    if ((uint32_t)(Arg3 + 24) != 0) goto loc_00404EE1;
    goto loc_00404EF1;
loc_004053BB:
    result = ExAcquireSpinLockExclusive(Arg1 + 1044, 1, v_stack_p60, v_rip + 5729);
    *(uint8_t *)(arg1 + 0x41D) = (uint8_t)(result);
    *(uint8_t *)(arg1 + 0x41B) = (uint8_t)(result);
loc_004053ED:
    result = ExReleaseSpinLockExclusiveFromDpcLevel((uint32_t)((uint32_t)(result)), 1, v_stack_p60, v_rip + 5729);
    goto loc_004052FB;
loc_004053FA:
    result = ObFastDereferenceObjectDeferDelete(Arg1 + 1044 + 64, result, (uint32_t)(0x63536D4DULL), v_rip + 5729);
    goto loc_00405151;
loc_0040541D:
    goto loc_0040524D;
loc_00405425:
    Arg1 = (uint32_t)((Arg1 + 1044 + 64) - 1);
    Arg2 = 2;
    if (result < ((uint32_t)(0x420ULL))) { Arg2 = (uint32_t)(2 + 2); }
    result = (uint32_t)((result) & ((uint32_t)(Arg1)));
    *(uint32_t *)(arg1 + 0x2E0) = (uint32_t)(result);
    goto loc_00405275;
loc_0040544F:
    result = (uint32_t)((result) & (24));
    result = (uint32_t)((result) + (8));
    *(uint32_t *)(arg1 + 0x2E0) = (uint32_t)(result);
    goto loc_00405275;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x2E0` | `32` | `R` |
| `Arg1` | `+ 0x2E0` | `32` | `W` |
| `Arg1` | `+ 0x414` | `64` | `R` |
| `Arg1` | `+ 0x41B` | `8` | `R` |
| `Arg1` | `+ 0x41B` | `8` | `W` |
| `Arg1` | `+ 0x41D` | `8` | `R` |
| `Arg1` | `+ 0x41D` | `8` | `W` |
| `Arg1` | `+ 0x438` | `8` | `R` |
| `Arg1` | `+ 0x4900` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R/W` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `32` | `W` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x20` | `64` | `R/W` |
| `Arg3` | `+ 0x28` | `32` | `R` |
| `Arg3` | `+ 0x28` | `32` | `W` |
| `Arg3` | `+ 0x2C` | `32` | `W` |
| `Arg3` | `+ 0x30` | `32` | `W` |
| `Arg3` | `+ 0x40` | `64` | `R/W` |
| `Arg3` | `+ 0x40` | `64` | `W` |
| `Arg3` | `+ 0x48` | `64` | `W` |
| `Arg3` | `+ 0x50` | `64` | `R` |
| `Arg3` | `+ 0x58` | `64` | `W` |
| `Arg3` | `+ 0x60` | `64` | `W` |
| `Arg3` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00404E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
