# IopSynchronousServiceTail

- RVA: `0x008EB440`–`0x008EB879` (길이 `1,081` bytes)
- VA: `0x00000001408EB440`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C3C`
- 디코드: `281`개 명령, `1,081/1,081` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008EB49F` → [Feature_3043197241__private_IsEnabledDeviceUsageNoInline](../../text/59/Feature_3043197241__private_IsEnabledDeviceUsageNoInline_function_00596C38.md) (function, `0x00596C38`)
- `0x008EB4E4` → [IopQueueIrpForServiceTail](../71/IopQueueIrpForServiceTail_function_0071BCC0.md) (function, `0x0071BCC0`)
- `0x008EB520` → [IopQueuePairedCopyWriteIrp](../../text/59/IopQueuePairedCopyWriteIrp_function_00598A9C.md) (function, `0x00598A9C`)
- `0x008EB566` → [IopQueueIrpToFileObject](../../text/40/IopQueueIrpToFileObject_function_00409864.md) (function, `0x00409864`)
- `0x008EB597` → [IopIsIosbInLockedRange](../A2/IopIsIosbInLockedRange_function_00A2C908.md) (function, `0x00A2C908`)
- `0x008EB5AF` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (function, `0x002075C0`)
- `0x008EB5D6` → [PsIsProcessAppContainer](../A3/PsIsProcessAppContainer_function_00A38C44.md) (function, `0x00A38C44`)
- `0x008EB5F6` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x008EB656` → [IoSetDiskIoAttributionFromThread](../../text/29/IoSetDiskIoAttributionFromThread_function_0029BF20.md) (function, `0x0029BF20`)
- `0x008EB6C5` → [IopSetIrpPriorityHintFromFileObject](../../text/40/IopSetIrpPriorityHintFromFileObject_function_0040DEA0.md) (function, `0x0040DEA0`)
- `0x008EB6CD` → [IoGetIoPriorityHint](../../text/41/IoGetIoPriorityHint_function_00411ED0.md) (function, `0x00411ED0`)
- `0x008EB6E4` → [IoGetBaseFileSystemDeviceObject](../../text/29/IoGetBaseFileSystemDeviceObject_function_0029A2A0.md) (function, `0x0029A2A0`)
- `0x008EB722` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008EB746` → [IopCallDriverReference](../../text/29/IopCallDriverReference_function_0029B1C0.md) (function, `0x0029B1C0`)
- `0x008EB78F` → [IopIoRingCompleteIrp](../../text/3E/IopIoRingCompleteIrp_function_003ED13C.md) (function, `0x003ED13C`)
- `0x008EB7B7` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008EB7DC` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)
- `0x008EB7F1` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x008EB821` → [IopWaitForSynchronousIo](../../text/29/IopWaitForSynchronousIo_function_0029D6D0.md) (function, `0x0029D6D0`)
- `0x008EB830` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)

### Direct callers
- [IopQueueCopyWrite](../../text/49/IopQueueCopyWrite_function_00492EA0.md) at `0x00492ECD`
- [IopSetEaOrQuotaInformationFile](../71/IopSetEaOrQuotaInformationFile_function_0071BD70.md) at `0x0071C178`
- [NtQueryQuotaInformationFile](../72/NtQueryQuotaInformationFile_function_00720FE0.md) at `0x007216E1`
- [NtSetVolumeInformationFile](../72/NtSetVolumeInformationFile_function_00721750.md) at `0x00721BA9`
- [NtQueryEaFile](../8A/NtQueryEaFile_function_008AC1B0.md) at `0x008AC641`
- [NtQueryVolumeInformationFile](../8A/NtQueryVolumeInformationFile_function_008AC8C0.md) at `0x008ACBF3`
- [IopFlushBuffersFile](../8A/IopFlushBuffersFile_function_008ACFA4.md) at `0x008AD1DF`
- [IopReadFile](../8A/IopReadFile_function_008AEFF0.md) at `0x008AF965`
- [IopWriteFile](IopWriteFile_function_008E9790.md) at `0x008E98CC`
- [IopXxxControlFile](IopXxxControlFile_function_008E9AD0.md) at `0x008EA46E`
- [NtQueryDirectoryFileEx](NtQueryDirectoryFileEx_function_008EC680.md) at `0x008EC753`
- [NtQueryDirectoryFile](NtQueryDirectoryFile_function_008ECF80.md) at `0x008ED05B`
- [NtLockFile](../9D/NtLockFile_function_009D86D0.md) at `0x009D8C9D`
- [NtUnlockFile](../9E/NtUnlockFile_function_009E5DA0.md) at `0x009E6179`
- [NtNotifyChangeDirectoryFileEx](../A1/NtNotifyChangeDirectoryFileEx_function_00A1DEA0.md) at `0x00A1E134`
- [NtSetEaFile](../A7/NtSetEaFile_function_00A788A0.md) at `0x00A78ABE`
- [IopReadFileScatter](../AA/IopReadFileScatter_function_00AA5D78.md) at `0x00AA6382`
- [IopWriteFileGather](../AA/IopWriteFileGather_function_00AAA95C.md) at `0x00AAAFCF`

### Static image references
- `0x008EB6D7` → RVA `0x00FC6B1C` (`ALMOSTRO`; read)
- `0x008EB7A8` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **17**
  - `0x008EB49F` → [Feature_3043197241__private_IsEnabledDeviceUsageNoInline](../../text/59/Feature_3043197241__private_IsEnabledDeviceUsageNoInline_function_00596C38.md) (`PAGE` → `.text`)
  - `0x008EB520` → [IopQueuePairedCopyWriteIrp](../../text/59/IopQueuePairedCopyWriteIrp_function_00598A9C.md) (`PAGE` → `.text`)
  - `0x008EB566` → [IopQueueIrpToFileObject](../../text/40/IopQueueIrpToFileObject_function_00409864.md) (`PAGE` → `.text`)
  - `0x008EB5AF` → [IopQueueThreadIrp](../../text/20/IopQueueThreadIrp_function_002075C0.md) (`PAGE` → `.text`)
  - `0x008EB5F6` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x008EB656` → [IoSetDiskIoAttributionFromThread](../../text/29/IoSetDiskIoAttributionFromThread_function_0029BF20.md) (`PAGE` → `.text`)
  - `0x008EB6C5` → [IopSetIrpPriorityHintFromFileObject](../../text/40/IopSetIrpPriorityHintFromFileObject_function_0040DEA0.md) (`PAGE` → `.text`)
  - `0x008EB6CD` → [IoGetIoPriorityHint](../../text/41/IoGetIoPriorityHint_function_00411ED0.md) (`PAGE` → `.text`)
  - `0x008EB6E4` → [IoGetBaseFileSystemDeviceObject](../../text/29/IoGetBaseFileSystemDeviceObject_function_0029A2A0.md) (`PAGE` → `.text`)
  - `0x008EB722` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008EB746` → [IopCallDriverReference](../../text/29/IopCallDriverReference_function_0029B1C0.md) (`PAGE` → `.text`)
  - `0x008EB78F` → [IopIoRingCompleteIrp](../../text/3E/IopIoRingCompleteIrp_function_003ED13C.md) (`PAGE` → `.text`)
  - `0x008EB7B7` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008EB7DC` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (`PAGE` → `.text`)
  - `0x008EB7F1` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x008EB821` → [IopWaitForSynchronousIo](../../text/29/IopWaitForSynchronousIo_function_0029D6D0.md) (`PAGE` → `.text`)
  - `0x008EB830` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008EB440  48 8B C4                        mov rax, rsp
008EB443  48 89 58 08                     mov qword ptr [rax + 8], rbx
008EB447  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
008EB44B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
008EB44F  55                              push rbp
008EB450  56                              push rsi
008EB451  57                              push rdi
008EB452  41 54                           push r12
008EB454  41 55                           push r13
008EB456  41 56                           push r14
008EB458  41 57                           push r15
008EB45A  48 83 EC 50                     sub rsp, 0x50
008EB45E  48 8B DA                        mov rbx, rdx
008EB461  33 ED                           xor ebp, ebp
008EB463  48 8B 52 58                     mov rdx, qword ptr [rdx + 0x58]
008EB467  49 8B F8                        mov rdi, r8
008EB46A  89 68 10                        mov dword ptr [rax + 0x10], ebp
008EB46D  4C 8B F9                        mov r15, rcx
008EB470  48 8D 73 47                     lea rsi, [rbx + 0x47]
008EB474  F6 C2 01                        test dl, 1
008EB477  74 0B                           je 0x1408eb484
008EB479  80 0E 10                        or byte ptr [rsi], 0x10
008EB47C  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
008EB480  48 89 53 58                     mov qword ptr [rbx + 0x58], rdx
008EB484  44 8B 6B 10                     mov r13d, dword ptr [rbx + 0x10]
008EB488  4C 8D 73 10                     lea r14, [rbx + 0x10]
008EB48C  49 8B 80 B0 00 00 00            mov rax, qword ptr [r8 + 0xb0]
008EB493  41 81 E5 00 00 20 00            and r13d, 0x200000
008EB49A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EB49F  E8 94 B7 CA FF                  call 0x140596c38
008EB4A4  44 0F B6 A4 24 B8 00 00 00      movzx r12d, byte ptr [rsp + 0xb8]
008EB4AD  85 C0                           test eax, eax
008EB4AF  74 79                           je 0x1408eb52a
008EB4B1  41 0F BA 26 09                  bt dword ptr [r14], 9
008EB4B6  73 22                           jae 0x1408eb4da
008EB4B8  48 8B 83 C8 00 00 00            mov rax, qword ptr [rbx + 0xc8]
008EB4BF  90                              nop
008EB4C0  40 38 2E                        cmp byte ptr [rsi], bpl
008EB4C3  7C 15                           jl 0x1408eb4da
008EB4C5  48 85 C0                        test rax, rax
008EB4C8  74 0C                           je 0x1408eb4d6
008EB4CA  66 0F BA 60 02 09               bt word ptr [rax + 2], 9
008EB4D0  0F 82 DE 00 00 00               jb 0x1408eb5b4
008EB4D6  4C 8D 73 10                     lea r14, [rbx + 0x10]
008EB4DA  45 0F B6 C4                     movzx r8d, r12b
008EB4DE  48 8B D7                        mov rdx, rdi
008EB4E1  48 8B CB                        mov rcx, rbx
008EB4E4  E8 D7 07 E3 FF                  call 0x14071bcc0
008EB4E9  41 F7 06 00 01 00 00            test dword ptr [r14], 0x100
008EB4F0  0F 84 BE 00 00 00               je 0x1408eb5b4
008EB4F6  48 8B 83 C8 00 00 00            mov rax, qword ptr [rbx + 0xc8]
008EB4FD  90                              nop
008EB4FE  40 38 6B 47                     cmp byte ptr [rbx + 0x47], bpl
008EB502  0F 8C AC 00 00 00               jl 0x1408eb5b4
008EB508  48 85 C0                        test rax, rax
008EB50B  0F 84 A3 00 00 00               je 0x1408eb5b4
008EB511  66 0F BA 60 02 09               bt word ptr [rax + 2], 9
008EB517  0F 83 97 00 00 00               jae 0x1408eb5b4
008EB51D  48 8B CB                        mov rcx, rbx
008EB520  E8 77 D5 CA FF                  call 0x140598a9c
008EB525  E9 8A 00 00 00                  jmp 0x1408eb5b4
008EB52A  45 84 E4                        test r12b, r12b
008EB52D  75 0A                           jne 0x1408eb539
008EB52F  48 39 6B 58                     cmp qword ptr [rbx + 0x58], rbp
008EB533  74 09                           je 0x1408eb53e
008EB535  48 8D 73 47                     lea rsi, [rbx + 0x47]
008EB539  45 85 ED                        test r13d, r13d
008EB53C  74 64                           je 0x1408eb5a2
008EB53E  45 85 ED                        test r13d, r13d
008EB541  74 05                           je 0x1408eb548
008EB543  45 33 C0                        xor r8d, r8d
008EB546  EB 18                           jmp 0x1408eb560
008EB548  48 39 6B 60                     cmp qword ptr [rbx + 0x60], rbp
008EB54C  74 2A                           je 0x1408eb578
008EB54E  48 39 6B 50                     cmp qword ptr [rbx + 0x50], rbp
008EB552  75 24                           jne 0x1408eb578
008EB554  48 39 AF B0 00 00 00            cmp qword ptr [rdi + 0xb0], rbp
008EB55B  74 1B                           je 0x1408eb578
008EB55D  41 B0 01                        mov r8b, 1
008EB560  48 8B D7                        mov rdx, rdi
008EB563  48 8B CB                        mov rcx, rbx
008EB566  E8 F9 E2 B1 FF                  call 0x140409864
008EB56B  84 C0                           test al, al
008EB56D  8B CD                           mov ecx, ebp
008EB56F  0F 94 C1                        sete cl
008EB572  85 C9                           test ecx, ecx
008EB574  74 3E                           je 0x1408eb5b4
008EB576  EB 34                           jmp 0x1408eb5ac
008EB578  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
008EB57B  A8 10                           test al, 0x10
008EB57D  75 2D                           jne 0x1408eb5ac
008EB57F  48 39 AF B0 00 00 00            cmp qword ptr [rdi + 0xb0], rbp
008EB586  75 24                           jne 0x1408eb5ac
008EB588  48 39 AF D0 00 00 00            cmp qword ptr [rdi + 0xd0], rbp
008EB58F  74 1B                           je 0x1408eb5ac
008EB591  48 8B D3                        mov rdx, rbx
008EB594  48 8B CF                        mov rcx, rdi
008EB597  E8 6C 13 14 00                  call 0x140a2c908
008EB59C  84 C0                           test al, al
008EB59E  75 14                           jne 0x1408eb5b4
008EB5A0  EB 0A                           jmp 0x1408eb5ac
008EB5A2  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
008EB5A5  A8 02                           test al, 2
008EB5A7  74 03                           je 0x1408eb5ac
008EB5A9  80 0E 02                        or byte ptr [rsi], 2
008EB5AC  48 8B CB                        mov rcx, rbx
008EB5AF  E8 0C C0 91 FF                  call 0x1402075c0
008EB5B4  48 8B 87 D0 00 00 00            mov rax, qword ptr [rdi + 0xd0]
008EB5BB  48 85 C0                        test rax, rax
008EB5BE  74 4F                           je 0x1408eb60f
008EB5C0  8B 00                           mov eax, dword ptr [rax]
008EB5C2  A8 04                           test al, 4
008EB5C4  74 49                           je 0x1408eb60f
008EB5C6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EB5CF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008EB5D6  E8 69 D6 14 00                  call 0x140a38c44
008EB5DB  84 C0                           test al, al
008EB5DD  74 30                           je 0x1408eb60f
008EB5DF  33 D2                           xor edx, edx
008EB5E1  C7 84 24 98 00 00 00 10 09 00 C0  mov dword ptr [rsp + 0x98], 0xc0000910
008EB5EC  48 8B CB                        mov rcx, rbx
008EB5EF  C7 43 30 10 09 00 C0            mov dword ptr [rbx + 0x30], 0xc0000910
008EB5F6  E8 C5 FF 9A FF                  call 0x14029b5c0
008EB5FB  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
008EB603  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
008EB60A  E9 45 01 00 00                  jmp 0x1408eb754
008EB60F  8B B4 24 C0 00 00 00            mov esi, dword ptr [rsp + 0xc0]
008EB616  83 FE 01                        cmp esi, 1
008EB619  76 17                           jbe 0x1408eb632
008EB61B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EB624  48 FF 80 90 03 00 00            inc qword ptr [rax + 0x390]
008EB62B  B8 E4 2E 00 00                  mov eax, 0x2ee4
008EB630  EB 50                           jmp 0x1408eb682
008EB632  41 8B 4F 48                     mov ecx, dword ptr [r15 + 0x48]
008EB636  83 E9 07                        sub ecx, 7
008EB639  74 0F                           je 0x1408eb64a
008EB63B  83 E9 01                        sub ecx, 1
008EB63E  74 0A                           je 0x1408eb64a
008EB640  83 E9 01                        sub ecx, 1
008EB643  74 05                           je 0x1408eb64a
008EB645  83 F9 1B                        cmp ecx, 0x1b
008EB648  75 11                           jne 0x1408eb65b
008EB64A  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
008EB653  48 8B CB                        mov rcx, rbx
008EB656  E8 C5 08 9B FF                  call 0x14029bf20
008EB65B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EB664  85 F6                           test esi, esi
008EB666  75 0E                           jne 0x1408eb676
008EB668  48 FF 80 80 03 00 00            inc qword ptr [rax + 0x380]
008EB66F  B8 DC 2E 00 00                  mov eax, 0x2edc
008EB674  EB 0C                           jmp 0x1408eb682
008EB676  48 FF 80 88 03 00 00            inc qword ptr [rax + 0x388]
008EB67D  B8 E0 2E 00 00                  mov eax, 0x2ee0
008EB682  65 FF 00                        inc dword ptr gs:[rax]
008EB685  48 8B BC 24 A0 00 00 00         mov rdi, qword ptr [rsp + 0xa0]
008EB68D  F7 47 50 00 00 80 00            test dword ptr [rdi + 0x50], 0x800000
008EB694  0F 84 9B 00 00 00               je 0x1408eb735
008EB69A  85 F6                           test esi, esi
008EB69C  0F 85 93 00 00 00               jne 0x1408eb735
008EB6A2  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008EB6A6  F6 40 04 40                     test byte ptr [rax + 4], 0x40
008EB6AA  0F 85 85 00 00 00               jne 0x1408eb735
008EB6B0  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008EB6B4  48 85 C0                        test rax, rax
008EB6B7  74 7C                           je 0x1408eb735
008EB6B9  F6 40 06 20                     test byte ptr [rax + 6], 0x20
008EB6BD  75 76                           jne 0x1408eb735
008EB6BF  48 8B D3                        mov rdx, rbx
008EB6C2  48 8B CF                        mov rcx, rdi
008EB6C5  E8 D6 27 B2 FF                  call 0x14040dea0
008EB6CA  48 8B CB                        mov rcx, rbx
008EB6CD  E8 FE 67 B2 FF                  call 0x140411ed0
008EB6D2  83 F8 02                        cmp eax, 2
008EB6D5  7C 5E                           jl 0x1408eb735
008EB6D7  8B 05 3F B4 6D 00               mov eax, dword ptr [rip + 0x6db43f]
008EB6DD  A8 04                           test al, 4
008EB6DF  75 54                           jne 0x1408eb735
008EB6E1  48 8B CF                        mov rcx, rdi
008EB6E4  E8 B7 EB 9A FF                  call 0x14029a2a0
008EB6E9  4C 8B D0                        mov r10, rax
008EB6EC  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008EB6F0  48 8B 51 50                     mov rdx, qword ptr [rcx + 0x50]
008EB6F4  81 3A F0 00 00 00               cmp dword ptr [rdx], 0xf0
008EB6FA  72 33                           jb 0x1408eb72f
008EB6FC  48 8B 82 E0 00 00 00            mov rax, qword ptr [rdx + 0xe0]
008EB703  48 85 C0                        test rax, rax
008EB706  74 27                           je 0x1408eb72f
008EB708  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
008EB710  4C 8B CF                        mov r9, rdi
008EB713  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008EB718  45 0F B6 C4                     movzx r8d, r12b
008EB71C  49 8B CA                        mov rcx, r10
008EB71F  48 8B D3                        mov rdx, rbx
008EB722  E8 A9 F3 DC FF                  call 0x1406baad0
008EB727  84 C0                           test al, al
008EB729  0F 85 D4 FE FF FF               jne 0x1408eb603
008EB72F  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
008EB733  EB 04                           jmp 0x1408eb739
008EB735  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008EB739  4C 8B CF                        mov r9, rdi
008EB73C  45 0F B6 C4                     movzx r8d, r12b
008EB740  48 8B D3                        mov rdx, rbx
008EB743  49 8B CF                        mov rcx, r15
008EB746  E8 75 FA 9A FF                  call 0x14029b1c0
008EB74B  8B C8                           mov ecx, eax
008EB74D  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
008EB754  40 38 AC 24 A8 00 00 00         cmp byte ptr [rsp + 0xa8], bpl
008EB75C  0F 84 A3 00 00 00               je 0x1408eb805
008EB762  81 F9 03 01 00 00               cmp ecx, 0x103
008EB768  0F 84 97 00 00 00               je 0x1408eb805
008EB76E  45 85 ED                        test r13d, r13d
008EB771  74 23                           je 0x1408eb796
008EB773  41 8B 47 48                     mov eax, dword ptr [r15 + 0x48]
008EB777  83 F8 08                        cmp eax, 8
008EB77A  74 05                           je 0x1408eb781
008EB77C  83 F8 14                        cmp eax, 0x14
008EB77F  75 05                           jne 0x1408eb786
008EB781  BD 01 00 00 00                  mov ebp, 1
008EB786  44 8B C5                        mov r8d, ebp
008EB789  48 8B D7                        mov rdx, rdi
008EB78C  48 8B CB                        mov rcx, rbx
008EB78F  E8 A8 19 B0 FF                  call 0x1403ed13c
008EB794  EB 68                           jmp 0x1408eb7fe
008EB796  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
008EB79B  44 0F 20 C6                     mov rsi, cr8
008EB79F  B8 01 00 00 00                  mov eax, 1
008EB7A4  44 0F 22 C0                     mov cr8, rax
008EB7A8  39 2D 72 B5 6D 00               cmp dword ptr [rip + 0x6db572], ebp
008EB7AE  74 0C                           je 0x1408eb7bc
008EB7B0  0F B6 D0                        movzx edx, al
008EB7B3  40 0F B6 CE                     movzx ecx, sil
008EB7B7  E8 40 9F C0 FF                  call 0x1404f56fc
008EB7BC  48 8D 44 24 30                  lea rax, [rsp + 0x30]
008EB7C1  48 8D 4B 78                     lea rcx, [rbx + 0x78]
008EB7C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EB7CA  4C 8D 8C 24 A0 00 00 00         lea r9, [rsp + 0xa0]
008EB7D2  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
008EB7D7  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
008EB7DC  E8 6F F7 91 FF                  call 0x14020af50
008EB7E1  39 2D 39 B5 6D 00               cmp dword ptr [rip + 0x6db539], ebp
008EB7E7  74 0D                           je 0x1408eb7f6
008EB7E9  44 0F 20 C1                     mov rcx, cr8
008EB7ED  40 0F B6 D6                     movzx edx, sil
008EB7F1  E8 A2 9E C0 FF                  call 0x1404f5698
008EB7F6  40 0F B6 C6                     movzx eax, sil
008EB7FA  44 0F 22 C0                     mov cr8, rax
008EB7FE  8B 8C 24 98 00 00 00            mov ecx, dword ptr [rsp + 0x98]
008EB805  45 84 E4                        test r12b, r12b
008EB808  74 34                           je 0x1408eb83e
008EB80A  81 F9 03 01 00 00               cmp ecx, 0x103
008EB810  75 1B                           jne 0x1408eb82d
008EB812  44 0F B6 84 24 B0 00 00 00      movzx r8d, byte ptr [rsp + 0xb0]
008EB81B  48 8B D7                        mov rdx, rdi
008EB81E  48 8B CB                        mov rcx, rbx
008EB821  E8 AA 1E 9B FF                  call 0x14029d6d0
008EB826  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
008EB82D  48 8B CF                        mov rcx, rdi
008EB830  E8 5B 52 96 FF                  call 0x140250a90
008EB835  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
008EB83C  EB 22                           jmp 0x1408eb860
008EB83E  45 85 ED                        test r13d, r13d
008EB841  75 18                           jne 0x1408eb85b
008EB843  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
008EB849  8B C1                           mov eax, ecx
008EB84B  74 13                           je 0x1408eb860
008EB84D  25 00 00 00 C0                  and eax, 0xc0000000
008EB852  3D 00 00 00 80                  cmp eax, 0x80000000
008EB857  8B C1                           mov eax, ecx
008EB859  75 05                           jne 0x1408eb860
008EB85B  B8 03 01 00 00                  mov eax, 0x103
008EB860  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
008EB868  48 83 C4 50                     add rsp, 0x50
008EB86C  41 5F                           pop r15
008EB86E  41 5E                           pop r14
008EB870  41 5D                           pop r13
008EB872  41 5C                           pop r12
008EB874  5F                              pop rdi
008EB875  5E                              pop rsi
008EB876  5D                              pop rbp
008EB877  C3                              ret
008EB878  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopSynchronousServiceTail(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (80);
    v_rbp = 0;
    *(unsigned int *)(v_rsp + 16) = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 88))) & (1)) != 0) {
        a2 = (*(unsigned __int64 *)(a2 + 88)) & (-2);
        *(unsigned __int64 *)(a2 + 88) = a2;
    }
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) & (0x200000ULL));
    v_stack_m50 = *(unsigned __int64 *)(a3 + 176);
    result = Feature_3043197241__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_008EB52A;
    if (condition_is_above_or_equal) goto loc_008EB4DA;
    if ((*(unsigned __int8 *)(a2 + 71)) < 0) goto loc_008EB4DA;
    if (*(unsigned __int64 *)(a2 + 200) == 0) goto loc_008EB4D6;
    if (condition_is_below) goto loc_008EB5B4;
loc_008EB4D6:
loc_008EB4DA:
    result = IopQueueIrpForServiceTail(a2, a3, a6, a4);
    if (((*(unsigned int *)(a2 + 16)) & (256)) == 0) goto loc_008EB5B4;
    if ((*(unsigned __int8 *)(a2 + 71)) < 0) goto loc_008EB5B4;
    if (*(unsigned __int64 *)(a2 + 200) == 0) goto loc_008EB5B4;
    if (condition_is_above_or_equal) goto loc_008EB5B4;
    result = IopQueuePairedCopyWriteIrp(a2, a3, a6, a4);
    goto loc_008EB5B4;
loc_008EB52A:
    if (a6 != 0) goto loc_008EB539;
    if ((*(unsigned __int64 *)(a2 + 88)) == 0) goto loc_008EB53E;
loc_008EB539:
    if ((unsigned int)(v_r13) == 0) goto loc_008EB5A2;
loc_008EB53E:
    if ((unsigned int)(v_r13) == 0) goto loc_008EB548;
    a3 = 0;
    goto loc_008EB560;
loc_008EB548:
    if ((*(unsigned __int64 *)(a2 + 96)) == 0) goto loc_008EB578;
    if ((*(unsigned __int64 *)(a2 + 80)) != 0) goto loc_008EB578;
    if ((*(unsigned __int64 *)(a3 + 176)) == 0) goto loc_008EB578;
loc_008EB560:
    result = IopQueueIrpToFileObject(a2, 0, 1, a4);
    a1 = ((unsigned __int8)(result) == 0) ? 1 : 0;
    if ((unsigned int)(a1) == 0) goto loc_008EB5B4;
    goto loc_008EB5AC;
loc_008EB578:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16)))) & (16)) != 0) goto loc_008EB5AC;
    if ((*(unsigned __int64 *)(a3 + 176)) != 0) goto loc_008EB5AC;
    if ((*(unsigned __int64 *)(a3 + 208)) == 0) goto loc_008EB5AC;
    result = IopIsIosbInLockedRange(0, a2, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008EB5B4;
    goto loc_008EB5AC;
loc_008EB5A2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 80)))) & (2)) != 0) {
    }
    result = IopQueueThreadIrp(a2, a2, 1, a4);
loc_008EB5B4:
    if (*(unsigned __int64 *)(a3 + 208) == 0) goto loc_008EB60F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 208))))) & (4)) == 0) goto loc_008EB60F;
    result = PsIsProcessAppContainer(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008EB60F;
    a2 = 0;
    v_stack_p10 = 0xC0000910ULL;
    *(unsigned int *)(a2 + 48) = 0xC0000910ULL;
    result = IofCompleteRequest(0, a2, 1, a4);
loc_008EB603:
    goto loc_008EB754;
loc_008EB60F:
    if (((unsigned int)((unsigned int)(a7))) <= 1) goto loc_008EB632;
    goto loc_008EB682;
loc_008EB632:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 72))) - (7));
    if (condition_is_equal) goto loc_008EB64A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008EB64A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008EB64A;
    result = (unsigned int)(0x2EE4ULL);
    if (((unsigned int)(a1)) == 27) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = a2;
        result = IoSetDiskIoAttributionFromThread(a1, a2, 1, a4);
    }
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_008EB676;
    goto loc_008EB682;
loc_008EB676:
loc_008EB682:
    if (((*(unsigned int *)(v_stack_p18 + 80)) & (0x800000ULL)) == 0) goto loc_008EB735;
    if ((unsigned int)((unsigned int)(a7)) != 0) goto loc_008EB735;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 16) + 4)) & (64)) != 0) goto loc_008EB735;
    if (*(unsigned __int64 *)(v_stack_p18 + 24) == 0) goto loc_008EB735;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p18 + 24) + 6)) & (32)) != 0) goto loc_008EB735;
    result = IopSetIrpPriorityHintFromFileObject(v_stack_p18, a2, 1, a4);
    result = IoGetIoPriorityHint(a2, a2, 1, a4);
    if (((unsigned int)(result)) < 2) goto loc_008EB735;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7189567)))) & (4)) != 0) goto loc_008EB735;
    result = IoGetBaseFileSystemDeviceObject(v_stack_p18, a2, 1, a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80))) < 240) goto loc_008EB72F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 80) + 224) == 0) goto loc_008EB72F;
    v_stack_m68 = v_stack_p10;
    result = guard_dispatch_icall(result, a2, a6, v_stack_p18);
    if ((unsigned __int8)(result) != 0) goto loc_008EB603;
loc_008EB72F:
    v_stack_m68 = 0;
    goto loc_008EB739;
loc_008EB735:
    v_stack_m68 = (unsigned int)((unsigned int)(a7));
loc_008EB739:
    result = IopCallDriverReference(a1, a2, a6, v_stack_p18);
    v_stack_p10 = (unsigned int)(result);
loc_008EB754:
    if (v_stack_p20 == 0) goto loc_008EB805;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 259) goto loc_008EB805;
    if ((unsigned int)(v_r13) == 0) goto loc_008EB796;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)))) == 8) goto loc_008EB781;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 72)))) == 20) {
        v_rbp = 1;
    }
    result = IopIoRingCompleteIrp(a2, v_stack_p18, (unsigned int)((unsigned int)(v_rbp)), v_stack_p18);
    goto loc_008EB7FE;
loc_008EB796:
    v_stack_m58 = v_rbp;
    result = 1;
    if ((*(unsigned int *)(v_rip + 7189874)) != ((unsigned int)(v_rbp))) {
        a2 = 1;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, (unsigned int)((unsigned int)(v_rbp)), v_stack_p18);
    }
    v_stack_m68 = v_stack_m58;
    result = IopCompleteRequest(a2 + 120, v_stack_m48, v_stack_m58, v_stack_p18);
    if ((*(unsigned int *)(v_rip + 7189817)) != ((unsigned int)(v_rbp))) {
        a1 = 1;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, v_stack_m58, v_stack_p18);
    }
loc_008EB7FE:
loc_008EB805:
    if (a6 == 0) goto loc_008EB83E;
    result = (unsigned __int8)(v_cr8);
    if (((unsigned int)((unsigned int)(v_stack_p10))) == 259) {
        a3 = a5;
        a2 = v_stack_p18;
        a1 = a2;
        result = IopWaitForSynchronousIo(a1, a2, a3, v_stack_p18);
        v_stack_p10 = (unsigned int)(result);
    }
    result = IopReleaseFileObjectLock(v_stack_p18, a2, a3, v_stack_p18);
    goto loc_008EB860;
loc_008EB83E:
    if ((unsigned int)(v_r13) != 0) goto loc_008EB85B;
    if (v_stack_m50 == 0) goto loc_008EB860;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & (0xC0000000ULL));
    result = (unsigned int)((unsigned int)(v_stack_p18));
    if (((unsigned int)(result)) == 0x80000000ULL) {
        result = 259;
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopSynchronousServiceTail(void *Arg1, void *Arg2, void *Arg3, uint8_t Arg4, uint8_t Arg5, uint8_t Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (80);
    local_rbp = 0;
    *(uint32_t *)(local_rsp + 0x10) = 0;
    if ((((uint8_t)(*(uint64_t *)(arg2 + 0x58))) & (1)) != 0) {
        Arg2 = (*(uint64_t *)(arg2 + 0x58)) & (-2);
        *(void **)(arg2 + 0x58) = Arg2;
    }
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) & (0x200000ULL));
    v_stack_m50 = *(uint64_t *)(arg3 + 0xB0);
    result = Feature_3043197241__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008EB52A;
    if (condition_is_above_or_equal) goto loc_008EB4DA;
    if ((*(uint8_t *)(arg2 + 0x47)) < 0) goto loc_008EB4DA;
    if (*(uint64_t *)(arg2 + 0xC8) == 0) goto loc_008EB4D6;
    if (condition_is_below) goto loc_008EB5B4;
loc_008EB4D6:
loc_008EB4DA:
    result = IopQueueIrpForServiceTail(Arg2, Arg3, Arg6, Arg4);
    if (((*(uint32_t *)(arg2 + 0x10)) & (256)) == 0) goto loc_008EB5B4;
    if ((*(uint8_t *)(arg2 + 0x47)) < 0) goto loc_008EB5B4;
    if (*(uint64_t *)(arg2 + 0xC8) == 0) goto loc_008EB5B4;
    if (condition_is_above_or_equal) goto loc_008EB5B4;
    result = IopQueuePairedCopyWriteIrp(Arg2, Arg3, Arg6, Arg4);
    goto loc_008EB5B4;
loc_008EB52A:
    if (Arg6 != 0) goto loc_008EB539;
    if ((*(uint64_t *)(arg2 + 0x58)) == 0) goto loc_008EB53E;
loc_008EB539:
    if ((uint32_t)(local_r13) == 0) goto loc_008EB5A2;
loc_008EB53E:
    if ((uint32_t)(local_r13) == 0) goto loc_008EB548;
    Arg3 = 0;
    goto loc_008EB560;
loc_008EB548:
    if ((*(uint64_t *)(arg2 + 0x60)) == 0) goto loc_008EB578;
    if ((*(uint64_t *)(arg2 + 0x50)) != 0) goto loc_008EB578;
    if ((*(uint64_t *)(arg3 + 0xB0)) == 0) goto loc_008EB578;
loc_008EB560:
    result = IopQueueIrpToFileObject(Arg2, 0, 1, Arg4);
    Arg1 = ((uint8_t)(result) == 0) ? 1 : 0;
    if ((uint32_t)(Arg1) == 0) goto loc_008EB5B4;
    goto loc_008EB5AC;
loc_008EB578:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) & (16)) != 0) goto loc_008EB5AC;
    if ((*(uint64_t *)(arg3 + 0xB0)) != 0) goto loc_008EB5AC;
    if ((*(uint64_t *)(arg3 + 0xD0)) == 0) goto loc_008EB5AC;
    result = IopIsIosbInLockedRange(0, Arg2, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008EB5B4;
    goto loc_008EB5AC;
loc_008EB5A2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg3 + 0x50)))) & (2)) != 0) {
    }
    result = IopQueueThreadIrp(Arg2, Arg2, 1, Arg4);
loc_008EB5B4:
    if (*(uint64_t *)(arg3 + 0xD0) == 0) goto loc_008EB60F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3 + 0xD0))))) & (4)) == 0) goto loc_008EB60F;
    result = PsIsProcessAppContainer(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008EB60F;
    Arg2 = 0;
    v_stack_p10 = 0xC0000910ULL;
    *(uint32_t *)(arg2 + 0x30) = 0xC0000910ULL;
    result = IofCompleteRequest(0, Arg2, 1, Arg4);
loc_008EB603:
    goto loc_008EB754;
loc_008EB60F:
    if (((uint32_t)((uint32_t)(Arg7))) <= 1) goto loc_008EB632;
    goto loc_008EB682;
loc_008EB632:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x48))) - (7));
    if (condition_is_equal) goto loc_008EB64A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008EB64A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008EB64A;
    result = (uint32_t)(0x2EE4ULL);
    if (((uint32_t)(Arg1)) == 27) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = Arg2;
        result = IoSetDiskIoAttributionFromThread(Arg1, Arg2, 1, Arg4);
    }
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_008EB676;
    goto loc_008EB682;
loc_008EB676:
loc_008EB682:
    if (((*(uint32_t *)(v_stack_p18 + 0x50)) & (0x800000ULL)) == 0) goto loc_008EB735;
    if ((uint32_t)((uint32_t)(Arg7)) != 0) goto loc_008EB735;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x10) + 0x4)) & (64)) != 0) goto loc_008EB735;
    if (*(uint64_t *)(v_stack_p18 + 0x18) == 0) goto loc_008EB735;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_p18 + 0x18) + 0x6)) & (32)) != 0) goto loc_008EB735;
    result = IopSetIrpPriorityHintFromFileObject(v_stack_p18, Arg2, 1, Arg4);
    result = IoGetIoPriorityHint(Arg2, Arg2, 1, Arg4);
    if (((uint32_t)(result)) < 2) goto loc_008EB735;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6DB43F)))) & (4)) != 0) goto loc_008EB735;
    result = IoGetBaseFileSystemDeviceObject(v_stack_p18, Arg2, 1, Arg4);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50))) < 240) goto loc_008EB72F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x50) + 0xE0) == 0) goto loc_008EB72F;
    v_stack_m68 = v_stack_p10;
    result = guard_dispatch_icall(result, Arg2, Arg6, v_stack_p18);
    if ((uint8_t)(result) != 0) goto loc_008EB603;
loc_008EB72F:
    v_stack_m68 = 0;
    goto loc_008EB739;
loc_008EB735:
    v_stack_m68 = (uint32_t)((uint32_t)(Arg7));
loc_008EB739:
    result = IopCallDriverReference(Arg1, Arg2, Arg6, v_stack_p18);
    v_stack_p10 = (uint32_t)(result);
loc_008EB754:
    if (v_stack_p20 == 0) goto loc_008EB805;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 259) goto loc_008EB805;
    if ((uint32_t)(local_r13) == 0) goto loc_008EB796;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)))) == 8) goto loc_008EB781;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x48)))) == 20) {
        local_rbp = 1;
    }
    result = IopIoRingCompleteIrp(Arg2, v_stack_p18, (uint32_t)((uint32_t)(local_rbp)), v_stack_p18);
    goto loc_008EB7FE;
loc_008EB796:
    v_stack_m58 = local_rbp;
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x6DB572)) != ((uint32_t)(local_rbp))) {
        Arg2 = 1;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, (uint32_t)((uint32_t)(local_rbp)), v_stack_p18);
    }
    v_stack_m68 = v_stack_m58;
    result = IopCompleteRequest(Arg2 + 120, v_stack_m48, v_stack_m58, v_stack_p18);
    if ((*(uint32_t *)(v_rip + 0x6DB539)) != ((uint32_t)(local_rbp))) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m58, v_stack_p18);
    }
loc_008EB7FE:
loc_008EB805:
    if (Arg6 == 0) goto loc_008EB83E;
    result = (uint8_t)(v_cr8);
    if (((uint32_t)((uint32_t)(v_stack_p10))) == 259) {
        Arg3 = Arg5;
        Arg2 = v_stack_p18;
        Arg1 = Arg2;
        result = IopWaitForSynchronousIo(Arg1, Arg2, Arg3, v_stack_p18);
        v_stack_p10 = (uint32_t)(result);
    }
    result = IopReleaseFileObjectLock(v_stack_p18, Arg2, Arg3, v_stack_p18);
    goto loc_008EB860;
loc_008EB83E:
    if ((uint32_t)(local_r13) != 0) goto loc_008EB85B;
    if (v_stack_m50 == 0) goto loc_008EB860;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & (0xC0000000ULL));
    result = (uint32_t)((uint32_t)(v_stack_p18));
    if (((uint32_t)(result)) == 0x80000000ULL) {
        result = 259;
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `32` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x47` | `8` | `R` |
| `Arg2` | `+ 0x47` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `W` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x78` | `64` | `R` |
| `Arg2` | `+ 0xC8` | `64` | `R` |
| `Arg3` | `+ 0x50` | `32` | `R` |
| `Arg3` | `+ 0xB0` | `64` | `R` |
| `Arg3` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EB440&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
