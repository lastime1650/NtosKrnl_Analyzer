# MiCreateNewSection

- RVA: `0x00985DB0`–`0x009864AC` (길이 `1,788` bytes)
- VA: `0x0000000140985DB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097C74`
- 디코드: `418`개 명령, `1,788/1,788` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00985DF8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00985E53` → [MiAllocateMappedWriterMdls](../../text/40/MiAllocateMappedWriterMdls_function_00403058.md) (function, `0x00403058`)
- `0x00985E65` → [MiMakePartitionActive](../../text/49/MiMakePartitionActive_function_004959B8.md) (function, `0x004959B8`)
- `0x00985EB5` → [MiCreateDataFileMap](MiCreateDataFileMap_function_00983494.md) (function, `0x00983494`)
- `0x00985F12` → [MiSectionCreated](../../text/2A/MiSectionCreated_function_002ABA18.md) (function, `0x002ABA18`)
- `0x00985F31` → [MiReleaseControlAreaWaiters](../../text/28/MiReleaseControlAreaWaiters_function_002865F0.md) (function, `0x002865F0`)
- `0x00985F3F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00985F77` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x00985F7F` → [FsRtlReleaseFile](FsRtlReleaseFile_function_00985B70.md) (function, `0x00985B70`)
- `0x00985FC0` → [MiCreateImageFileMap](MiCreateImageFileMap_function_00986830.md) (function, `0x00986830`)
- `0x00986017` → [MiParseComAndCetHeaders](../94/MiParseComAndCetHeaders_function_00941974.md) (function, `0x00941974`)
- `0x0098609E` → [SeGetImageRequiredSigningLevel](../A1/SeGetImageRequiredSigningLevel_function_00A135BC.md) (function, `0x00A135BC`)
- `0x009860E8` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (function, `0x004F4150`)
- `0x00986185` → [MiRelocateImage](MiRelocateImage_function_00988E14.md) (function, `0x00988E14`)
- `0x009861FD` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x00986205` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x00986218` → [MiReleaseImageSection](../../text/49/MiReleaseImageSection_function_00493044.md) (function, `0x00493044`)
- `0x00986258` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x00986260` → [FsRtlReleaseFile](FsRtlReleaseFile_function_00985B70.md) (function, `0x00985B70`)
- `0x00986273` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0098629D` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x009862A5` → [FsRtlReleaseFile](FsRtlReleaseFile_function_00985B70.md) (function, `0x00985B70`)
- `0x009862C3` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (function, `0x0042A7D0`)
- `0x009862CB` → [FsRtlReleaseFile](FsRtlReleaseFile_function_00985B70.md) (function, `0x00985B70`)
- `0x009863ED` → [FsRtlGetDirectImageOriginalBase](../AC/FsRtlGetDirectImageOriginalBase_function_00AC9C70.md) (function, `0x00AC9C70`)
- `0x00986445` → [MiRelocateImage](MiRelocateImage_function_00988E14.md) (function, `0x00988E14`)
- `0x00986466` → [MiMakeImageReadOnly](../../text/49/MiMakeImageReadOnly_function_0049CB74.md) (function, `0x0049CB74`)
- `0x00986492` → [MiFinalizeImageHeaderPage](../../text/4A/MiFinalizeImageHeaderPage_function_004A89A8.md) (function, `0x004A89A8`)

### Direct callers
- [sub_00984B34](Unknown_function_00984B34.md) at `0x00984C00`

### Static image references
- `0x00985DCC` → RVA `0x00E0A740` (`.data`; read)
- `0x00985E3E` → RVA `0x00E38D00` (`.data`; read)
- `0x009860F5` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0098631A` → RVA `0x00E2D7F8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x00985DF8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00985E53` → [MiAllocateMappedWriterMdls](../../text/40/MiAllocateMappedWriterMdls_function_00403058.md) (`PAGE` → `.text`)
  - `0x00985E65` → [MiMakePartitionActive](../../text/49/MiMakePartitionActive_function_004959B8.md) (`PAGE` → `.text`)
  - `0x00985F12` → [MiSectionCreated](../../text/2A/MiSectionCreated_function_002ABA18.md) (`PAGE` → `.text`)
  - `0x00985F31` → [MiReleaseControlAreaWaiters](../../text/28/MiReleaseControlAreaWaiters_function_002865F0.md) (`PAGE` → `.text`)
  - `0x00985F3F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00985F77` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x009860E8` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (`PAGE` → `.text`)
  - `0x009861FD` → [MmUnmapLockedPages](../../text/24/MmUnmapLockedPages_function_00246E60.md) (`PAGE` → `.text`)
  - `0x00986205` → [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) (`PAGE` → `.text`)
  - `0x00986218` → [MiReleaseImageSection](../../text/49/MiReleaseImageSection_function_00493044.md) (`PAGE` → `.text`)
  - `0x00986258` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x00986273` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0098629D` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x009862C3` → [IoSetTopLevelIrp](../../text/42/IoSetTopLevelIrp_function_0042A7D0.md) (`PAGE` → `.text`)
  - `0x00986466` → [MiMakeImageReadOnly](../../text/49/MiMakeImageReadOnly_function_0049CB74.md) (`PAGE` → `.text`)
  - `0x00986492` → [MiFinalizeImageHeaderPage](../../text/4A/MiFinalizeImageHeaderPage_function_004A89A8.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **18**
  - `0x00985F6A` → [sub_00B2AF8E + 0x113](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00985F87` → [sub_00B2AF8E + 0x113](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986290` → [sub_00B2AF8E](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x009862AD` → [sub_00B2AF8E](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986314` → [sub_00B2AF8E + 0xA](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986329` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098633B` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098636E` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986378` → [sub_00B2AF8E + 0x41](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098638C` → [sub_00B2AF8E + 0x41](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x009863F6` → [sub_00B2AF8E + 0x6B](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098641C` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986425` → [sub_00B2AF8E + 0x8C](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098644E` → [sub_00B2AF8E + 0x75](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x0098645E` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986477` → [sub_00B2AF8E + 0x101](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x00986498` → [sub_00B2AF8E + 0x101](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)
  - `0x009864A7` → [sub_00B2AF8E + 0x2D](../B2/Unknown_function_00B2AF8E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00985DB0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00985DB5  55                              push rbp
00985DB6  56                              push rsi
00985DB7  57                              push rdi
00985DB8  41 54                           push r12
00985DBA  41 55                           push r13
00985DBC  41 56                           push r14
00985DBE  41 57                           push r15
00985DC0  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
00985DC5  48 81 EC 10 01 00 00            sub rsp, 0x110
00985DCC  48 8B 05 6D 49 48 00            mov rax, qword ptr [rip + 0x48496d]
00985DD3  48 33 C4                        xor rax, rsp
00985DD6  48 89 45 00                     mov qword ptr [rbp], rax
00985DDA  33 F6                           xor esi, esi
00985DDC  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00985DE1  48 8B D9                        mov rbx, rcx
00985DE4  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00985DE9  33 D2                           xor edx, edx
00985DEB  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00985DF0  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00985DF4  44 8D 46 70                     lea r8d, [rsi + 0x70]
00985DF8  E8 43 0E D4 FF                  call 0x1406c6c40
00985DFD  48 8B BB B0 00 00 00            mov rdi, qword ptr [rbx + 0xb0]
00985E04  44 8B EE                        mov r13d, esi
00985E07  8A 43 18                        mov al, byte ptr [rbx + 0x18]
00985E0A  4C 8B 7B 38                     mov r15, qword ptr [rbx + 0x38]
00985E0E  44 8B 63 10                     mov r12d, dword ptr [rbx + 0x10]
00985E12  4C 8B B3 98 00 00 00            mov r14, qword ptr [rbx + 0x98]
00985E19  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00985E1D  40 88 74 24 52                  mov byte ptr [rsp + 0x52], sil
00985E22  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00985E27  40 88 74 24 51                  mov byte ptr [rsp + 0x51], sil
00985E2C  40 88 74 24 54                  mov byte ptr [rsp + 0x54], sil
00985E31  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00985E35  48 85 FF                        test rdi, rdi
00985E38  0F 85 46 04 00 00               jne 0x140986284
00985E3E  48 8D 3D BB 2E 4B 00            lea rdi, [rip + 0x4b2ebb]
00985E45  8B 47 04                        mov eax, dword ptr [rdi + 4]
00985E48  84 C0                           test al, al
00985E4A  0F 88 3C 04 00 00               js 0x14098628c
00985E50  48 8B CF                        mov rcx, rdi
00985E53  E8 00 D2 A7 FF                  call 0x140403058
00985E58  8B F0                           mov esi, eax
00985E5A  85 C0                           test eax, eax
00985E5C  0F 88 03 01 00 00               js 0x140985f65
00985E62  48 8B CF                        mov rcx, rdi
00985E65  E8 4E FB B0 FF                  call 0x1404959b8
00985E6A  85 C0                           test eax, eax
00985E6C  0F 84 EE 00 00 00               je 0x140985f60
00985E72  4C 21 6D 80                     and qword ptr [rbp - 0x80], r13
00985E76  45 8B FC                        mov r15d, r12d
00985E79  8B 83 AC 00 00 00               mov eax, dword ptr [rbx + 0xac]
00985E7F  48 8B D7                        mov rdx, rdi
00985E82  41 81 E7 00 00 00 01            and r15d, 0x1000000
00985E89  0F 85 FD 00 00 00               jne 0x140985f8c
00985E8F  8B 0B                           mov ecx, dword ptr [rbx]
00985E91  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00985E96  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00985E9A  4D 8B CE                        mov r9, r14
00985E9D  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00985EA1  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00985EA4  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00985EA9  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00985EAE  49 8B CC                        mov rcx, r12
00985EB1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00985EB5  E8 DA D5 FF FF                  call 0x140983494
00985EBA  8B F8                           mov edi, eax
00985EBC  85 C0                           test eax, eax
00985EBE  0F 88 EE 03 00 00               js 0x1409862b2
00985EC4  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00985EC9  48 83 CA FF                     or rdx, 0xffffffffffffffff
00985ECD  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00985ED2  48 89 08                        mov qword ptr [rax], rcx
00985ED5  4D 85 F6                        test r14, r14
00985ED8  0F 84 EC 00 00 00               je 0x140985fca
00985EDE  4C 89 B3 80 00 00 00            mov qword ptr [rbx + 0x80], r14
00985EE5  F7 03 00 00 40 00               test dword ptr [rbx], 0x400000
00985EEB  4C 8B 31                        mov r14, qword ptr [rcx]
00985EEE  B9 01 00 00 00                  mov ecx, 1
00985EF3  0F 85 DF 03 00 00               jne 0x1409862d8
00985EF9  F7 03 00 10 00 00               test dword ptr [rbx], 0x1000
00985EFF  0F 85 DC 03 00 00               jne 0x1409862e1
00985F05  4C 8B 4D 80                     mov r9, qword ptr [rbp - 0x80]
00985F09  4D 8B C6                        mov r8, r14
00985F0C  49 8B D4                        mov rdx, r12
00985F0F  48 8B CB                        mov rcx, rbx
00985F12  E8 01 5B 92 FF                  call 0x1402aba18
00985F17  8B 0B                           mov ecx, dword ptr [rbx]
00985F19  48 8B F0                        mov rsi, rax
00985F1C  F6 C1 02                        test cl, 2
00985F1F  0F 85 2C 03 00 00               jne 0x140986251
00985F25  45 85 FF                        test r15d, r15d
00985F28  0F 85 B6 00 00 00               jne 0x140985fe4
00985F2E  48 8B CE                        mov rcx, rsi
00985F31  E8 BA 06 90 FF                  call 0x1402865f0
00985F36  8B C7                           mov eax, edi
00985F38  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00985F3C  48 33 CC                        xor rcx, rsp
00985F3F  E8 FC 66 D2 FF                  call 0x1406ac640
00985F44  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
00985F4C  48 81 C4 10 01 00 00            add rsp, 0x110
00985F53  41 5F                           pop r15
00985F55  41 5E                           pop r14
00985F57  41 5D                           pop r13
00985F59  41 5C                           pop r12
00985F5B  5F                              pop rdi
00985F5C  5E                              pop rsi
00985F5D  5D                              pop rbp
00985F5E  C3                              ret
00985F5F  CC                              int3
00985F60  BE 2D 01 00 C0                  mov esi, 0xc000012d
00985F65  8B 0B                           mov ecx, dword ptr [rbx]
00985F67  F6 C1 02                        test cl, 2
00985F6A  0F 84 31 51 1A 00               je 0x140b2b0a1
00985F70  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
00985F77  E8 54 48 AA FF                  call 0x14042a7d0
00985F7C  49 8B CF                        mov rcx, r15
00985F7F  E8 EC FB FF FF                  call 0x140985b70
00985F84  83 23 FD                        and dword ptr [rbx], 0xfffffffd
00985F87  E9 15 51 1A 00                  jmp 0x140b2b0a1
00985F8C  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00985F91  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00985F96  44 8B 0B                        mov r9d, dword ptr [rbx]
00985F99  44 8B C0                        mov r8d, eax
00985F9C  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00985FA1  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00985FA5  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00985FAA  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00985FAE  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00985FB3  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00985FB8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00985FBD  49 8B CC                        mov rcx, r12
00985FC0  E8 6B 08 00 00                  call 0x140986830
00985FC5  E9 F0 FE FF FF                  jmp 0x140985eba
00985FCA  48 8B C2                        mov rax, rdx
00985FCD  F0 48 0F B1 51 18               lock cmpxchg qword ptr [rcx + 0x18], rdx
00985FD3  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00985FD8  48 89 83 80 00 00 00            mov qword ptr [rbx + 0x80], rax
00985FDF  E9 01 FF FF FF                  jmp 0x140985ee5
00985FE4  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00985FE9  48 8B 48 38                     mov rcx, qword ptr [rax + 0x38]
00985FED  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00985FF2  44 39 6D E8                     cmp dword ptr [rbp - 0x18], r13d
00985FF6  0F 84 F0 02 00 00               je 0x1409862ec
00985FFC  BE 00 08 00 00                  mov esi, 0x800
00986001  41 85 76 38                     test dword ptr [r14 + 0x38], esi
00986005  0F 85 03 03 00 00               jne 0x14098630e
0098600B  4C 8D 44 24 51                  lea r8, [rsp + 0x51]
00986010  49 8B CE                        mov rcx, r14
00986013  48 8D 55 90                     lea rdx, [rbp - 0x70]
00986017  E8 58 B9 FB FF                  call 0x140941974
0098601C  8B F8                           mov edi, eax
0098601E  85 C0                           test eax, eax
00986020  0F 88 08 03 00 00               js 0x14098632e
00986026  8B 13                           mov edx, dword ptr [rbx]
00986028  BF 04 00 00 00                  mov edi, 4
0098602D  44 8D 67 02                     lea r12d, [rdi + 2]
00986031  84 D2                           test dl, dl
00986033  0F 88 07 03 00 00               js 0x140986340
00986039  F6 C2 20                        test dl, 0x20
0098603C  0F 85 05 03 00 00               jne 0x140986347
00986042  F6 C2 10                        test dl, 0x10
00986045  0F 85 06 03 00 00               jne 0x140986351
0098604B  33 C9                           xor ecx, ecx
0098604D  8B F1                           mov esi, ecx
0098604F  83 CE 10                        or esi, 0x10
00986052  0F BA E2 0A                     bt edx, 0xa
00986056  0F 43 F1                        cmovae esi, ecx
00986059  F7 C2 00 22 00 00               test edx, 0x2200
0098605F  0F 84 15 02 00 00               je 0x14098627a
00986065  F6 C2 10                        test dl, 0x10
00986068  0F 85 0C 02 00 00               jne 0x14098627a
0098606E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00986077  45 33 C9                        xor r9d, r9d
0098607A  44 8A 44 24 50                  mov r8b, byte ptr [rsp + 0x50]
0098607F  8B D6                           mov edx, esi
00986081  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00986088  48 8D 44 24 52                  lea rax, [rsp + 0x52]
0098608D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00986092  44 8B B9 50 07 00 00            mov r15d, dword ptr [rcx + 0x750]
00986099  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0098609E  E8 19 D5 08 00                  call 0x140a135bc
009860A3  8B F8                           mov edi, eax
009860A5  85 C0                           test eax, eax
009860A7  0F 88 B7 02 00 00               js 0x140986364
009860AD  F7 03 00 04 00 00               test dword ptr [rbx], 0x400
009860B3  0F 84 BA 02 00 00               je 0x140986373
009860B9  44 8A 64 24 52                  mov r12b, byte ptr [rsp + 0x52]
009860BE  BF 04 00 00 00                  mov edi, 4
009860C3  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
009860C8  44 88 63 18                     mov byte ptr [rbx + 0x18], r12b
009860CC  8B 0B                           mov ecx, dword ptr [rbx]
009860CE  0F BA E1 12                     bt ecx, 0x12
009860D2  0F 82 B9 02 00 00               jb 0x140986391
009860D8  44 8B FE                        mov r15d, esi
009860DB  41 0F BA EF 1D                  bts r15d, 0x1d
009860E0  0F BA E1 15                     bt ecx, 0x15
009860E4  44 0F 43 FE                     cmovae r15d, esi
009860E8  E8 63 E0 B6 FF                  call 0x1404f4150
009860ED  85 C0                           test eax, eax
009860EF  0F 85 B6 02 00 00               jne 0x1409863ab
009860F5  48 F7 05 88 09 64 00 00 00 02 00  test qword ptr [rip + 0x640988], 0x20000
00986100  B9 00 20 00 00                  mov ecx, 0x2000
00986105  41 B8 01 00 00 00               mov r8d, 1
0098610B  0F 85 B0 02 00 00               jne 0x1409863c1
00986111  8B 33                           mov esi, dword ptr [rbx]
00986113  85 F1                           test ecx, esi
00986115  0F 85 BF 02 00 00               jne 0x1409863da
0098611B  0F BA E6 09                     bt esi, 9
0098611F  0F 82 00 01 00 00               jb 0x140986225
00986125  0F BA E6 09                     bt esi, 9
00986129  0F 82 0F 01 00 00               jb 0x14098623e
0098612F  83 64 24 68 00                  and dword ptr [rsp + 0x68], 0
00986134  44 8B E6                        mov r12d, esi
00986137  41 C1 EC 05                     shr r12d, 5
0098613B  C1 EE 1B                        shr esi, 0x1b
0098613E  45 23 E0                        and r12d, r8d
00986141  83 E6 02                        and esi, 2
00986144  41 F6 46 3E 0C                  test byte ptr [r14 + 0x3e], 0xc
00986149  0F 85 94 02 00 00               jne 0x1409863e3
0098614F  48 83 C8 FF                     or rax, 0xffffffffffffffff
00986153  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00986158  B9 06 00 00 00                  mov ecx, 6
0098615D  44 84 E9                        test cl, r13b
00986160  0F 85 BB 02 00 00               jne 0x140986421
00986166  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0098616B  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00986170  48 8D 55 90                     lea rdx, [rbp - 0x70]
00986174  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00986179  45 8B CC                        mov r9d, r12d
0098617C  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00986180  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00986185  E8 8A 2C 00 00                  call 0x140988e14
0098618A  8B F8                           mov edi, eax
0098618C  85 C0                           test eax, eax
0098618E  0F 88 09 03 00 00               js 0x14098649d
00986194  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
00986199  0F 85 C4 02 00 00               jne 0x140986463
0098619F  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
009861A3  41 BC 04 00 00 00               mov r12d, 4
009861A9  48 85 DB                        test rbx, rbx
009861AC  74 64                           je 0x140986212
009861AE  44 84 63 0A                     test byte ptr [rbx + 0xa], r12b
009861B2  75 12                           jne 0x1409861c6
009861B4  8B 73 28                        mov esi, dword ptr [rbx + 0x28]
009861B7  4C 8D 7B 30                     lea r15, [rbx + 0x30]
009861BB  C1 EE 0C                        shr esi, 0xc
009861BE  85 F6                           test esi, esi
009861C0  0F 85 AA 02 00 00               jne 0x140986470
009861C6  48 8B 1B                        mov rbx, qword ptr [rbx]
009861C9  48 85 DB                        test rbx, rbx
009861CC  75 E0                           jne 0x1409861ae
009861CE  48 8B 5D 80                     mov rbx, qword ptr [rbp - 0x80]
009861D2  48 85 DB                        test rbx, rbx
009861D5  74 3B                           je 0x140986212
009861D7  41 BF 01 00 00 00               mov r15d, 1
009861DD  0F B7 43 0A                     movzx eax, word ptr [rbx + 0xa]
009861E1  48 8B 33                        mov rsi, qword ptr [rbx]
009861E4  41 84 C4                        test r12b, al
009861E7  0F 85 80 00 00 00               jne 0x14098626d
009861ED  A8 02                           test al, 2
009861EF  74 11                           je 0x140986202
009861F1  41 84 C7                        test r15b, al
009861F4  74 0C                           je 0x140986202
009861F6  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
009861FA  48 8B D3                        mov rdx, rbx
009861FD  E8 5E 0C 8C FF                  call 0x140246e60
00986202  48 8B CB                        mov rcx, rbx
00986205  E8 76 88 91 FF                  call 0x14029ea80
0098620A  48 8B DE                        mov rbx, rsi
0098620D  48 85 F6                        test rsi, rsi
00986210  75 CB                           jne 0x1409861dd
00986212  49 8B D6                        mov rdx, r14
00986215  49 8B CD                        mov rcx, r13
00986218  E8 27 CE B0 FF                  call 0x140493044
0098621D  48 8B F0                        mov rsi, rax
00986220  E9 09 FD FF FF                  jmp 0x140985f2e
00986225  45 84 E4                        test r12b, r12b
00986228  0F 85 AC 01 00 00               jne 0x1409863da
0098622E  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00986233  8A 40 2E                        mov al, byte ptr [rax + 0x2e]
00986236  84 C0                           test al, al
00986238  0F 88 9C 01 00 00               js 0x1409863da
0098623E  80 7C 24 54 00                  cmp byte ptr [rsp + 0x54], 0
00986243  0F 84 E6 FE FF FF               je 0x14098612f
00986249  44 0B EF                        or r13d, edi
0098624C  E9 DE FE FF FF                  jmp 0x14098612f
00986251  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
00986258  E8 73 45 AA FF                  call 0x14042a7d0
0098625D  49 8B CC                        mov rcx, r12
00986260  E8 0B F9 FF FF                  call 0x140985b70
00986265  83 23 FD                        and dword ptr [rbx], 0xfffffffd
00986268  E9 B8 FC FF FF                  jmp 0x140985f25
0098626D  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00986271  33 D2                           xor edx, edx
00986273  E8 F8 C5 1F 00                  call 0x140b82870
00986278  EB 88                           jmp 0x140986202
0098627A  44 8A 64 24 50                  mov r12b, byte ptr [rsp + 0x50]
0098627F  E9 48 FE FF FF                  jmp 0x1409860cc
00986284  48 8B 3F                        mov rdi, qword ptr [rdi]
00986287  E9 B9 FB FF FF                  jmp 0x140985e45
0098628C  8B 03                           mov eax, dword ptr [rbx]
0098628E  A8 02                           test al, 2
00986290  0F 84 F8 4C 1A 00               je 0x140b2af8e
00986296  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
0098629D  E8 2E 45 AA FF                  call 0x14042a7d0
009862A2  49 8B CF                        mov rcx, r15
009862A5  E8 C6 F8 FF FF                  call 0x140985b70
009862AA  83 23 FD                        and dword ptr [rbx], 0xfffffffd
009862AD  E9 DC 4C 1A 00                  jmp 0x140b2af8e
009862B2  8B 03                           mov eax, dword ptr [rbx]
009862B4  A8 02                           test al, 2
009862B6  0F 84 7A FC FF FF               je 0x140985f36
009862BC  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
009862C3  E8 08 45 AA FF                  call 0x14042a7d0
009862C8  49 8B CC                        mov rcx, r12
009862CB  E8 A0 F8 FF FF                  call 0x140985b70
009862D0  83 23 FD                        and dword ptr [rbx], 0xfffffffd
009862D3  E9 5E FC FF FF                  jmp 0x140985f36
009862D8  41 08 4E 3E                     or byte ptr [r14 + 0x3e], cl
009862DC  E9 18 FC FF FF                  jmp 0x140985ef9
009862E1  41 0F BA 6E 38 11               bts dword ptr [r14 + 0x38], 0x11
009862E7  E9 19 FC FF FF                  jmp 0x140985f05
009862EC  44 39 6D EC                     cmp dword ptr [rbp - 0x14], r13d
009862F0  0F 85 06 FD FF FF               jne 0x140985ffc
009862F6  44 38 69 32                     cmp byte ptr [rcx + 0x32], r13b
009862FA  0F 85 FC FC FF FF               jne 0x140985ffc
00986300  B9 00 40 00 00                  mov ecx, 0x4000
00986305  66 09 48 0C                     or word ptr [rax + 0xc], cx
00986309  E9 EE FC FF FF                  jmp 0x140985ffc
0098630E  F7 03 00 00 04 00               test dword ptr [rbx], 0x40000
00986314  0F 84 7E 4C 1A 00               je 0x140b2af98
0098631A  C7 05 D4 74 4A 00 05 00 00 00   mov dword ptr [rip + 0x4a74d4], 5
00986324  BF 33 04 00 C0                  mov edi, 0xc0000433
00986329  E9 8D 4C 1A 00                  jmp 0x140b2afbb
0098632E  41 BC 04 00 00 00               mov r12d, 4
00986334  44 89 25 BD 74 4A 00            mov dword ptr [rip + 0x4a74bd], r12d
0098633B  E9 7B 4C 1A 00                  jmp 0x140b2afbb
00986340  8B CF                           mov ecx, edi
00986342  E9 06 FD FF FF                  jmp 0x14098604d
00986347  B9 01 00 00 00                  mov ecx, 1
0098634C  E9 FC FC FF FF                  jmp 0x14098604d
00986351  8B C2                           mov eax, edx
00986353  23 C6                           and eax, esi
00986355  F7 D8                           neg eax
00986357  1B C9                           sbb ecx, ecx
00986359  41 23 CC                        and ecx, r12d
0098635C  83 C1 02                        add ecx, 2
0098635F  E9 E9 FC FF FF                  jmp 0x14098604d
00986364  C7 05 8A 74 4A 00 07 00 00 00   mov dword ptr [rip + 0x4a748a], 7
0098636E  E9 48 4C 1A 00                  jmp 0x140b2afbb
00986373  44 38 6C 24 50                  cmp byte ptr [rsp + 0x50], r13b
00986378  0F 84 51 4C 1A 00               je 0x140b2afcf
0098637E  41 0F BA E7 17                  bt r15d, 0x17
00986383  B8 01 00 00 00                  mov eax, 1
00986388  44 0F 42 E8                     cmovb r13d, eax
0098638C  E9 3E 4C 1A 00                  jmp 0x140b2afcf
00986391  41 0F B6 C4                     movzx eax, r12b
00986395  0F BA EE 1E                     bts esi, 0x1e
00986399  45 84 E4                        test r12b, r12b
0098639C  0F 44 C7                        cmove eax, edi
0098639F  44 8A E0                        mov r12b, al
009863A2  88 44 24 50                     mov byte ptr [rsp + 0x50], al
009863A6  E9 2D FD FF FF                  jmp 0x1409860d8
009863AB  F7 03 00 00 00 08               test dword ptr [rbx], 0x8000000
009863B1  0F 84 3E FD FF FF               je 0x1409860f5
009863B7  41 0F BA EF 15                  bts r15d, 0x15
009863BC  E9 34 FD FF FF                  jmp 0x1409860f5
009863C1  09 0B                           or dword ptr [rbx], ecx
009863C3  45 84 E4                        test r12b, r12b
009863C6  41 0F B6 C4                     movzx eax, r12b
009863CA  41 0F 44 C0                     cmove eax, r8d
009863CE  44 8A E0                        mov r12b, al
009863D1  88 44 24 50                     mov byte ptr [rsp + 0x50], al
009863D5  E9 37 FD FF FF                  jmp 0x140986111
009863DA  41 83 CD 02                     or r13d, 2
009863DE  E9 42 FD FF FF                  jmp 0x140986125
009863E3  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009863E8  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009863ED  E8 7E 38 14 00                  call 0x140ac9c70
009863F2  8B F8                           mov edi, eax
009863F4  85 C0                           test eax, eax
009863F6  0F 89 FD 4B 1A 00               jns 0x140b2aff9
009863FC  3D BB 00 00 C0                  cmp eax, 0xc00000bb
00986401  0F 84 48 FD FF FF               je 0x14098614f
00986407  3D 10 00 00 C0                  cmp eax, 0xc0000010
0098640C  0F 84 3D FD FF FF               je 0x14098614f
00986412  C7 05 DC 73 4A 00 08 00 00 00   mov dword ptr [rip + 0x4a73dc], 8
0098641C  E9 9A 4B 1A 00                  jmp 0x140b2afbb
00986421  48 83 F8 FF                     cmp rax, -1
00986425  0F 84 EF 4B 1A 00               je 0x140b2b01a
0098642B  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
00986430  48 8D 55 90                     lea rdx, [rbp - 0x70]
00986434  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00986439  45 8B CC                        mov r9d, r12d
0098643C  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00986440  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00986445  E8 CA 29 00 00                  call 0x140988e14
0098644A  8B F8                           mov edi, eax
0098644C  85 C0                           test eax, eax
0098644E  0F 89 AF 4B 1A 00               jns 0x140b2b003
00986454  C7 05 9A 73 4A 00 09 00 00 00   mov dword ptr [rip + 0x4a739a], 9
0098645E  E9 58 4B 1A 00                  jmp 0x140b2afbb
00986463  49 8B CE                        mov rcx, r14
00986466  E8 09 67 B1 FF                  call 0x14049cb74
0098646B  E9 2F FD FF FF                  jmp 0x14098619f
00986470  49 8B 07                        mov rax, qword ptr [r15]
00986473  48 83 F8 FF                     cmp rax, -1
00986477  0F 84 12 4C 1A 00               je 0x140b2b08f
0098647D  48 8D 0C 40                     lea rcx, [rax + rax*2]
00986481  48 C1 E1 04                     shl rcx, 4
00986485  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0098648F  48 03 C8                        add rcx, rax
00986492  E8 11 25 B2 FF                  call 0x1404a89a8
00986497  90                              nop
00986498  E9 F2 4B 1A 00                  jmp 0x140b2b08f
0098649D  C7 05 51 73 4A 00 0B 00 00 00   mov dword ptr [rip + 0x4a7351], 0xb
009864A7  E9 0F 4B 1A 00                  jmp 0x140b2afbb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreateNewSection(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m110;
    unsigned int v_stack_m118;
    unsigned int v_stack_m120;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int8 v_stack_mF4;
    unsigned __int8 v_stack_mF6;
    unsigned __int8 v_stack_mF7;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p51;
    unsigned __int64 v_stack_p52;
    unsigned __int8 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 4737389)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_mE0 = a2;
    v_stack_mE8 = 0;
    a2 = 0;
    v_stack_mD0 = 0;
    result = memset(v_stack_mB8, a2, v_rsi + 112, a4);
    v_stack_mF8 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 24));
    v_stack_mF6 = 0;
    v_stack_mD8 = *(unsigned __int64 *)(a1 + 56);
    v_stack_mF7 = 0;
    v_stack_mF4 = 0;
    v_stack_mF0 = 0;
    if (*(unsigned __int64 *)(a1 + 176) != 0) goto loc_00986284;
loc_00985E45:
    if (sign_flag) goto loc_0098628C;
    result = MiAllocateMappedWriterMdls(v_rip + 4927163, a2, v_rsi + 112, a4);
    if (sign_flag) goto loc_00985F65;
    result = MiMakePartitionActive(v_rip + 4927163, a2, v_rsi + 112, a4);
    if ((unsigned int)(result) == 0) goto loc_00985F60;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) & (0x1000000ULL));
    if (condition_is_not_equal) goto loc_00985F8C;
    v_stack_m110 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_m118 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 172)));
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    v_stack_m128 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    result = MiCreateDataFileMap(v_stack_mD8, v_rip + 4927163, v_stack_mE8, *(unsigned __int64 *)(a1 + 152));
loc_00985EBA:
    if (sign_flag) goto loc_009862B2;
    a2 = (v_rip + 4927163) | (-1);
    *(unsigned __int64 *)(v_stack_mE0) = v_stack_mE8;
    if (*(unsigned __int64 *)(a1 + 152) == 0) goto loc_00985FCA;
    *(unsigned __int64 *)(a1 + 128) = *(unsigned __int64 *)(a1 + 152);
loc_00985EE5:
    if (((*(unsigned int *)(a1)) & (0x400000ULL)) != 0) goto loc_009862D8;
loc_00985EF9:
    if (((*(unsigned int *)(a1)) & (0x1000ULL)) != 0) goto loc_009862E1;
loc_00985F05:
    result = MiSectionCreated(a1, v_stack_mD8, *(unsigned __int64 *)(v_stack_mE8), v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) != 0) goto loc_00986251;
loc_00985F25:
    if ((unsigned int)(v_r15) != 0) goto loc_00985FE4;
loc_00985F2E:
    result = MiReleaseControlAreaWaiters(result, v_stack_mD8, *(unsigned __int64 *)(v_stack_mE8), v_stack_mC8);
loc_00985F36:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_mD8, *(unsigned __int64 *)(v_stack_mE8), v_stack_mC8);
    v_rsp = (v_rsp) + (272);
    return result;
loc_00985F60:
loc_00985F65:
    result = IoSetTopLevelIrp(*(unsigned __int64 *)(v_stack_p18 + 184), v_stack_mD8, *(unsigned __int64 *)(v_stack_mE8), v_stack_mC8);
    result = FsRtlReleaseFile(v_r15, v_stack_mD8, *(unsigned __int64 *)(v_stack_mE8), v_stack_mC8);
loc_00985F8C:
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = v_stack_mB8;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = v_stack_p60;
    result = MiCreateImageFileMap(v_stack_p70, v_stack_mD8, (unsigned int)((unsigned int)(result)), (unsigned int)(*(unsigned int *)(v_stack_p18)));
    goto loc_00985EBA;
loc_00985FCA:
    *(unsigned __int64 *)(v_stack_p18 + 128) = v_stack_mD8;
    goto loc_00985EE5;
loc_00985FE4:
    v_stack_p68 = *(unsigned __int64 *)(v_stack_p60 + 56);
    if (v_stack_m60 == 0) goto loc_009862EC;
loc_00985FFC:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mE8) + 56)) & ((unsigned int)((unsigned int)(0x800ULL)))) != 0) goto loc_0098630E;
    result = MiParseComAndCetHeaders(*(unsigned __int64 *)(v_stack_mE8), v_stack_mB8, v_stack_p51, (unsigned int)(*(unsigned int *)(v_stack_p18)));
    if (sign_flag) goto loc_0098632E;
    if (sign_flag) goto loc_00986340;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (32)) != 0) goto loc_00986347;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (16)) != 0) goto loc_00986351;
    a1 = 0;
loc_0098604D:
    v_rsi = (unsigned int)((0) | (16));
    if (condition_is_above_or_equal) { v_rsi = 0; }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (0x2200ULL)) == 0) goto loc_0098627A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p18)))) & (16)) != 0) goto loc_0098627A;
    a4 = 0;
    v_stack_p20 = v_stack_p52;
    result = SeGetImageRequiredSigningLevel(v_stack_p70, (unsigned int)((unsigned int)(v_rsi)), v_stack_p50, a4);
    if (sign_flag) goto loc_00986364;
    if (((*(unsigned int *)(v_stack_p18)) & (0x400ULL)) == 0) goto loc_00986373;
    v_stack_p50 = (unsigned __int8)(v_stack_p52);
    *(unsigned __int8 *)(v_stack_p18 + 24) = (unsigned __int8)(v_stack_p52);
loc_009860CC:
    if (condition_is_below) goto loc_00986391;
loc_009860D8:
    v_r15 = (unsigned int)((unsigned int)(v_rsi));
    if (condition_is_above_or_equal) { v_r15 = (unsigned int)(v_rsi); }
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(v_stack_p18)), (unsigned int)((unsigned int)(v_rsi)), v_stack_p50, a4);
    if ((unsigned int)(result) != 0) goto loc_009863AB;
loc_009860F5:
    if (((*(unsigned __int64 *)(v_rip + 6556040)) & (0x20000ULL)) != 0) goto loc_009863C1;
loc_00986111:
    if ((((unsigned int)((unsigned int)(0x2000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))) != 0) goto loc_009863DA;
    if (condition_is_below) goto loc_00986225;
loc_00986125:
    if (condition_is_below) goto loc_0098623E;
loc_0098612F:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18))))) >> (5));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18))) >> (27));
    v_r12 = (unsigned int)((v_r12) & (1));
    v_rsi = (unsigned int)((v_rsi) & (2));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mE8) + 62)) & (12)) != 0) goto loc_009863E3;
loc_0098614F:
    result = (result) | (-1);
    v_stack_p78 = result;
    if (((6) & (0)) != 0) goto loc_00986421;
    v_stack_p28 = (unsigned int)(v_rsi);
    v_stack_p20 = result;
    result = MiRelocateImage(v_stack_p60, v_stack_mB8, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    if (sign_flag) goto loc_0098649D;
    if (v_stack_p51 != 0) goto loc_00986463;
loc_0098619F:
    if (v_stack_mC8 == 0) goto loc_00986212;
loc_009861AE:
    if (((*(unsigned __int8 *)(v_stack_mC8 + 10)) & (4)) != 0) goto loc_009861C6;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC8 + 40))) >> (12));
    if ((unsigned int)(v_rsi) != 0) goto loc_00986470;
loc_009861C6:
    if (*(unsigned __int64 *)(v_stack_mC8) != 0) goto loc_009861AE;
    if (v_stack_mC8 == 0) goto loc_00986212;
loc_009861DD:
    if (((4) & ((unsigned __int8)(*(unsigned __int16 *)(v_stack_mC8 + 10)))) != 0) goto loc_0098626D;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_mC8 + 10))) & (2)) == 0) goto loc_00986202;
    result = *(unsigned __int16 *)(v_stack_mC8 + 10);
    if (((1) & ((unsigned __int8)(*(unsigned __int16 *)(v_stack_mC8 + 10)))) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_mC8 + 24);
        a2 = v_stack_mC8;
        result = MmUnmapLockedPages(a1, a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    }
    result = IoFreeMdl(v_stack_mC8, a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    if (*(unsigned __int64 *)(v_stack_mC8) != 0) goto loc_009861DD;
loc_00986212:
    result = MiReleaseImageSection(v_stack_p70, *(unsigned __int64 *)(v_stack_mE8), (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    goto loc_00985F2E;
loc_00986225:
    if (4 != 0) goto loc_009863DA;
    if (sign_flag) goto loc_009863DA;
loc_0098623E:
    if (v_stack_p54 == 0) goto loc_0098612F;
    v_r13 = (unsigned int)((v_stack_p70) | ((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_0098612F;
loc_00986251:
    result = IoSetTopLevelIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC8) + 184), *(unsigned __int64 *)(v_stack_mE8), (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    result = FsRtlReleaseFile(4, *(unsigned __int64 *)(v_stack_mE8), (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    goto loc_00985F25;
loc_0098626D:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC8) + 32), a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    goto loc_00986202;
loc_0098627A:
    goto loc_009860CC;
loc_00986284:
    goto loc_00985E45;
loc_0098628C:
    result = IoSetTopLevelIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC8) + 184), a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    result = FsRtlReleaseFile(1, a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
loc_009862B2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC8))))) & (2)) == 0) goto loc_00985F36;
    result = IoSetTopLevelIrp(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC8) + 184), a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    result = FsRtlReleaseFile(v_stack_p50, a2, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    goto loc_00985F36;
loc_009862D8:
    goto loc_00985EF9;
loc_009862E1:
    goto loc_00985F05;
loc_009862EC:
    if (v_stack_m5C != ((unsigned int)(v_r13))) goto loc_00985FFC;
    if ((*(unsigned __int8 *)(v_stack_p50 + 50)) != ((unsigned __int8)(v_r13))) goto loc_00985FFC;
    goto loc_00985FFC;
loc_0098630E:
    *(unsigned int *)(v_rip + 4879572) = 5;
loc_0098632E:
    *(unsigned int *)(v_rip + 4879549) = 4;
loc_00986340:
    goto loc_0098604D;
loc_00986347:
    goto loc_0098604D;
loc_00986351:
    result = (unsigned int)((0) & ((unsigned int)(result)));
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((1) & (4));
    a1 = (unsigned int)((a1) + (2));
    goto loc_0098604D;
loc_00986364:
    *(unsigned int *)(v_rip + 4879498) = 7;
loc_00986373:
    if (v_stack_p50 < ((unsigned __int8)(v_r13))) { v_r13 = 1; }
loc_00986391:
    result = 4;
    if (4 == 0) { result = (unsigned int)((unsigned int)(0xC0000433ULL)); }
    v_stack_p50 = (unsigned __int8)(result);
    goto loc_009860D8;
loc_009863AB:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC8))) & (0x8000000ULL)) == 0) goto loc_009860F5;
    goto loc_009860F5;
loc_009863C1:
    result = (unsigned __int8)((unsigned __int8)(result));
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) { result = (unsigned int)((unsigned int)(v_stack_p58)); }
    v_stack_p50 = (unsigned __int8)(result);
    goto loc_00986111;
loc_009863DA:
    v_r13 = (unsigned int)((v_r13) | (2));
    goto loc_00986125;
loc_009863E3:
    result = FsRtlGetDirectImageOriginalBase(v_stack_p70, v_stack_p78, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(v_r12)));
    if (((unsigned int)(result)) == 0xC00000BBULL) goto loc_0098614F;
    if (((unsigned int)(result)) == 0xC0000010ULL) goto loc_0098614F;
    *(unsigned int *)(v_rip + 4879324) = 8;
loc_00986421:
    v_stack_p28 = (unsigned int)(result);
    v_stack_p20 = result;
    result = MiRelocateImage(v_stack_p60, v_stack_mB8, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)((unsigned __int8)(result))));
    *(unsigned int *)(v_rip + 4879258) = 9;
loc_00986463:
    result = MiMakeImageReadOnly(*(unsigned __int64 *)(v_stack_mE8), v_stack_mB8, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)((unsigned __int8)(result))));
    goto loc_0098619F;
loc_00986470:
    a1 = (*(unsigned __int64 *)(1) + *(unsigned __int64 *)(1) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(1));
    result = MiFinalizeImageHeaderPage(a1, v_stack_mB8, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)((unsigned __int8)(result))));
loc_0098649D:
    *(unsigned int *)(v_rip + 4879185) = 11;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreateNewSection(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m110;
    uint32_t v_stack_m118;
    uint32_t v_stack_m120;
    uint32_t v_stack_m128;
    uint64_t v_stack_m48;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint8_t v_stack_mF4;
    uint8_t v_stack_mF6;
    uint8_t v_stack_mF7;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p50;
    uint64_t v_stack_p51;
    uint64_t v_stack_p52;
    uint8_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x48496D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_mE0 = Arg2;
    v_stack_mE8 = 0;
    Arg2 = 0;
    v_stack_mD0 = 0;
    result = memset(v_stack_mB8, Arg2, local_rsi + 112, a4);
    v_stack_mF8 = (uint8_t)(*(uint8_t *)(arg1 + 0x18));
    v_stack_mF6 = 0;
    v_stack_mD8 = *(uint64_t *)(arg1 + 0x38);
    v_stack_mF7 = 0;
    v_stack_mF4 = 0;
    v_stack_mF0 = 0;
    if (*(uint64_t *)(arg1 + 0xB0) != 0) goto loc_00986284;
loc_00985E45:
    if (sign_flag) goto loc_0098628C;
    result = MiAllocateMappedWriterMdls(v_rip + 4927163, Arg2, local_rsi + 112, a4);
    if (sign_flag) goto loc_00985F65;
    result = MiMakePartitionActive(v_rip + 4927163, Arg2, local_rsi + 112, a4);
    if ((uint32_t)(result) == 0) goto loc_00985F60;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) & (0x1000000ULL));
    if (condition_is_not_equal) goto loc_00985F8C;
    v_stack_m110 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_m118 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xAC)));
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    v_stack_m128 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    result = MiCreateDataFileMap(v_stack_mD8, v_rip + 4927163, v_stack_mE8, *(uint64_t *)(arg1 + 0x98));
loc_00985EBA:
    if (sign_flag) goto loc_009862B2;
    Arg2 = (v_rip + 4927163) | (-1);
    *(uint64_t *)(v_stack_mE0) = v_stack_mE8;
    if (*(uint64_t *)(arg1 + 0x98) == 0) goto loc_00985FCA;
    *(uint64_t *)(arg1 + 0x80) = *(uint64_t *)(arg1 + 0x98);
loc_00985EE5:
    if (((*(uint32_t *)(arg1)) & (0x400000ULL)) != 0) goto loc_009862D8;
loc_00985EF9:
    if (((*(uint32_t *)(arg1)) & (0x1000ULL)) != 0) goto loc_009862E1;
loc_00985F05:
    result = MiSectionCreated(Arg1, v_stack_mD8, *(uint64_t *)(v_stack_mE8), v_stack_mC8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) != 0) goto loc_00986251;
loc_00985F25:
    if ((uint32_t)(local_r15) != 0) goto loc_00985FE4;
loc_00985F2E:
    result = MiReleaseControlAreaWaiters(result, v_stack_mD8, *(uint64_t *)(v_stack_mE8), v_stack_mC8);
loc_00985F36:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_mD8, *(uint64_t *)(v_stack_mE8), v_stack_mC8);
    local_rsp = (local_rsp) + (272);
    return result;
loc_00985F60:
loc_00985F65:
    result = IoSetTopLevelIrp(*(uint64_t *)(v_stack_p18 + 0xB8), v_stack_mD8, *(uint64_t *)(v_stack_mE8), v_stack_mC8);
    result = FsRtlReleaseFile(local_r15, v_stack_mD8, *(uint64_t *)(v_stack_mE8), v_stack_mC8);
loc_00985F8C:
    v_stack_p38 = v_stack_p58;
    v_stack_p30 = v_stack_mB8;
    v_stack_p28 = v_stack_mC8;
    v_stack_p20 = v_stack_p60;
    result = MiCreateImageFileMap(v_stack_p70, v_stack_mD8, (uint32_t)((uint32_t)(result)), (uint32_t)(*(uint32_t *)(v_stack_p18)));
    goto loc_00985EBA;
loc_00985FCA:
    *(uint64_t *)(v_stack_p18 + 0x80) = v_stack_mD8;
    goto loc_00985EE5;
loc_00985FE4:
    v_stack_p68 = *(uint64_t *)(v_stack_p60 + 0x38);
    if (v_stack_m60 == 0) goto loc_009862EC;
loc_00985FFC:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mE8) + 0x38)) & ((uint32_t)((uint32_t)(0x800ULL)))) != 0) goto loc_0098630E;
    result = MiParseComAndCetHeaders(*(uint64_t *)(v_stack_mE8), v_stack_mB8, v_stack_p51, (uint32_t)(*(uint32_t *)(v_stack_p18)));
    if (sign_flag) goto loc_0098632E;
    if (sign_flag) goto loc_00986340;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (32)) != 0) goto loc_00986347;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (16)) != 0) goto loc_00986351;
    Arg1 = 0;
loc_0098604D:
    local_rsi = (uint32_t)((0) | (16));
    if (condition_is_above_or_equal) { local_rsi = 0; }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (0x2200ULL)) == 0) goto loc_0098627A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p18)))) & (16)) != 0) goto loc_0098627A;
    a4 = 0;
    v_stack_p20 = v_stack_p52;
    result = SeGetImageRequiredSigningLevel(v_stack_p70, (uint32_t)((uint32_t)(local_rsi)), v_stack_p50, a4);
    if (sign_flag) goto loc_00986364;
    if (((*(uint32_t *)(v_stack_p18)) & (0x400ULL)) == 0) goto loc_00986373;
    v_stack_p50 = (uint8_t)(v_stack_p52);
    *(uint8_t *)(v_stack_p18 + 0x18) = (uint8_t)(v_stack_p52);
loc_009860CC:
    if (condition_is_below) goto loc_00986391;
loc_009860D8:
    local_r15 = (uint32_t)((uint32_t)(local_rsi));
    if (condition_is_above_or_equal) { local_r15 = (uint32_t)(local_rsi); }
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(v_stack_p18)), (uint32_t)((uint32_t)(local_rsi)), v_stack_p50, a4);
    if ((uint32_t)(result) != 0) goto loc_009863AB;
loc_009860F5:
    if (((*(uint64_t *)(v_rip + 0x640988)) & (0x20000ULL)) != 0) goto loc_009863C1;
loc_00986111:
    if ((((uint32_t)((uint32_t)(0x2000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))) != 0) goto loc_009863DA;
    if (condition_is_below) goto loc_00986225;
loc_00986125:
    if (condition_is_below) goto loc_0098623E;
loc_0098612F:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18))))) >> (5));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18))) >> (27));
    local_r12 = (uint32_t)((local_r12) & (1));
    local_rsi = (uint32_t)((local_rsi) & (2));
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_mE8) + 0x3E)) & (12)) != 0) goto loc_009863E3;
loc_0098614F:
    result = (result) | (-1);
    v_stack_p78 = result;
    if (((6) & (0)) != 0) goto loc_00986421;
    v_stack_p28 = (uint32_t)(local_rsi);
    v_stack_p20 = result;
    result = MiRelocateImage(v_stack_p60, v_stack_mB8, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    if (sign_flag) goto loc_0098649D;
    if (v_stack_p51 != 0) goto loc_00986463;
loc_0098619F:
    if (v_stack_mC8 == 0) goto loc_00986212;
loc_009861AE:
    if (((*(uint8_t *)(v_stack_mC8 + 0xA)) & (4)) != 0) goto loc_009861C6;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC8 + 0x28))) >> (12));
    if ((uint32_t)(local_rsi) != 0) goto loc_00986470;
loc_009861C6:
    if (*(uint64_t *)(v_stack_mC8) != 0) goto loc_009861AE;
    if (v_stack_mC8 == 0) goto loc_00986212;
loc_009861DD:
    if (((4) & ((uint8_t)(*(uint16_t *)(v_stack_mC8 + 0xA)))) != 0) goto loc_0098626D;
    if ((((uint8_t)(*(uint16_t *)(v_stack_mC8 + 0xA))) & (2)) == 0) goto loc_00986202;
    result = *(uint16_t *)(v_stack_mC8 + 0xA);
    if (((1) & ((uint8_t)(*(uint16_t *)(v_stack_mC8 + 0xA)))) != 0) {
        Arg1 = *(uint64_t *)(v_stack_mC8 + 0x18);
        Arg2 = v_stack_mC8;
        result = MmUnmapLockedPages(Arg1, Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    }
    result = IoFreeMdl(v_stack_mC8, Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    if (*(uint64_t *)(v_stack_mC8) != 0) goto loc_009861DD;
loc_00986212:
    result = MiReleaseImageSection(v_stack_p70, *(uint64_t *)(v_stack_mE8), (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    goto loc_00985F2E;
loc_00986225:
    if (4 != 0) goto loc_009863DA;
    if (sign_flag) goto loc_009863DA;
loc_0098623E:
    if (v_stack_p54 == 0) goto loc_0098612F;
    local_r13 = (uint32_t)((v_stack_p70) | ((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_0098612F;
loc_00986251:
    result = IoSetTopLevelIrp(*(uint64_t *)(*(uint64_t *)(v_stack_mC8) + 0xB8), *(uint64_t *)(v_stack_mE8), (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    result = FsRtlReleaseFile(4, *(uint64_t *)(v_stack_mE8), (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    goto loc_00985F25;
loc_0098626D:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_mC8) + 0x20), Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    goto loc_00986202;
loc_0098627A:
    goto loc_009860CC;
loc_00986284:
    goto loc_00985E45;
loc_0098628C:
    result = IoSetTopLevelIrp(*(uint64_t *)(*(uint64_t *)(v_stack_mC8) + 0xB8), Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    result = FsRtlReleaseFile(1, Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
loc_009862B2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC8))))) & (2)) == 0) goto loc_00985F36;
    result = IoSetTopLevelIrp(*(uint64_t *)(*(uint64_t *)(v_stack_mC8) + 0xB8), Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    result = FsRtlReleaseFile(v_stack_p50, Arg2, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    goto loc_00985F36;
loc_009862D8:
    goto loc_00985EF9;
loc_009862E1:
    goto loc_00985F05;
loc_009862EC:
    if (v_stack_m5C != ((uint32_t)(local_r13))) goto loc_00985FFC;
    if ((*(uint8_t *)(v_stack_p50 + 0x32)) != ((uint8_t)(local_r13))) goto loc_00985FFC;
    goto loc_00985FFC;
loc_0098630E:
    *(uint32_t *)(v_rip + 0x4A74D4) = 5;
loc_0098632E:
    *(uint32_t *)(v_rip + 0x4A74BD) = 4;
loc_00986340:
    goto loc_0098604D;
loc_00986347:
    goto loc_0098604D;
loc_00986351:
    result = (uint32_t)((0) & ((uint32_t)(result)));
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((1) & (4));
    Arg1 = (uint32_t)((Arg1) + (2));
    goto loc_0098604D;
loc_00986364:
    *(uint32_t *)(v_rip + 0x4A748A) = 7;
loc_00986373:
    if (v_stack_p50 < ((uint8_t)(local_r13))) { local_r13 = 1; }
loc_00986391:
    result = 4;
    if (4 == 0) { result = (uint32_t)((uint32_t)(0xC0000433ULL)); }
    v_stack_p50 = (uint8_t)(result);
    goto loc_009860D8;
loc_009863AB:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mC8))) & (0x8000000ULL)) == 0) goto loc_009860F5;
    goto loc_009860F5;
loc_009863C1:
    result = (uint8_t)((uint8_t)(result));
    if ((uint8_t)((uint8_t)(result)) == 0) { result = (uint32_t)((uint32_t)(v_stack_p58)); }
    v_stack_p50 = (uint8_t)(result);
    goto loc_00986111;
loc_009863DA:
    local_r13 = (uint32_t)((local_r13) | (2));
    goto loc_00986125;
loc_009863E3:
    result = FsRtlGetDirectImageOriginalBase(v_stack_p70, v_stack_p78, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(local_r12)));
    if (((uint32_t)(result)) == 0xC00000BBULL) goto loc_0098614F;
    if (((uint32_t)(result)) == 0xC0000010ULL) goto loc_0098614F;
    *(uint32_t *)(v_rip + 0x4A73DC) = 8;
loc_00986421:
    v_stack_p28 = (uint32_t)(result);
    v_stack_p20 = result;
    result = MiRelocateImage(v_stack_p60, v_stack_mB8, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)((uint8_t)(result))));
    *(uint32_t *)(v_rip + 0x4A739A) = 9;
loc_00986463:
    result = MiMakeImageReadOnly(*(uint64_t *)(v_stack_mE8), v_stack_mB8, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)((uint8_t)(result))));
    goto loc_0098619F;
loc_00986470:
    Arg1 = (*(uint64_t *)(1) + *(uint64_t *)(1) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(1));
    result = MiFinalizeImageHeaderPage(Arg1, v_stack_mB8, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)((uint8_t)(result))));
loc_0098649D:
    *(uint32_t *)(v_rip + 0x4A7351) = 11;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x18` | `8` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00985DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
