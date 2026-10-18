# RtlFindClearBitsAndSet

- RVA: `0x003E0CD0`–`0x003E10B0` (길이 `992` bytes)
- VA: `0x00000001403E0CD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000949CC`
- 디코드: `282`개 명령, `992/992` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **27**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E0DF9` → [RtlSetBits](RtlSetBits_function_003E1610.md) (function, `0x003E1610`)

### Direct callers
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDB48`
- [HalpDmaAllocateMapRegisters](../3D/HalpDmaAllocateMapRegisters_function_003DDA0C.md) at `0x003DDBC4`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV2](HalpDmaAllocateContiguousPagesFromContiguousPoolV2_function_003E02A0.md) at `0x003E02F9`
- [BgpFwReserveAllocate](BgpFwReserveAllocate_function_003E5230.md) at `0x003E5252`
- [BgpFwReserveAllocate](BgpFwReserveAllocate_function_003E5230.md) at `0x003E52B5`
- [HalpDmaAllocateScatterPagesFromContiguousPoolV3](../4E/HalpDmaAllocateScatterPagesFromContiguousPoolV3_function_004E380C.md) at `0x004E38C0`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevelV3](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevelV3_function_0053DD8C.md) at `0x0053DDB2`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolV3](../53/HalpDmaAllocateContiguousPagesFromContiguousPoolV3_function_0053DE24.md) at `0x0053DEB0`
- [HalpDmaAllocateScatterPagesFromContiguousPoolAtHighLevelV3](../53/HalpDmaAllocateScatterPagesFromContiguousPoolAtHighLevelV3_function_0053DF40.md) at `0x0053DF7D`
- [HalpIommuGetDomainId](../55/HalpIommuGetDomainId_function_005537E4.md) at `0x00553835`
- [HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevelV2](../55/HalpDmaAllocateContiguousPagesFromContiguousPoolAtHighLevelV2_function_00553DE4.md) at `0x00553E0A`
- [HalpDmaAllocateScatterPagesFromContiguousPoolAtHighLevelV2](../55/HalpDmaAllocateScatterPagesFromContiguousPoolAtHighLevelV2_function_00553E70.md) at `0x00553EAD`
- [SepGetAntiTamperEntry](../60/SepGetAntiTamperEntry_function_0060AEE4.md) at `0x0060AFB3`
- [SepGetAntiTamperEntry](../60/SepGetAntiTamperEntry_function_0060AEE4.md) at `0x0060B049`
- [MiReserveFaultPte](../67/MiReserveFaultPte_function_0067E64C.md) at `0x0067E68A`
- [MiZeroHugeRangeWorker](../68/MiZeroHugeRangeWorker_function_0068C960.md) at `0x0068C9BF`
- [MiCreateSlabIdentity](../68/MiCreateSlabIdentity_function_0068D2D4.md) at `0x0068D377`
- [RtlHotPatchSynchronizationRequired](../6A/RtlHotPatchSynchronizationRequired_function_006AA21C.md) at `0x006AA33B`
- [HalpIrtAllocateIndex](../../page/70/HalpIrtAllocateIndex_function_0070A9D4.md) at `0x0070AAD5`
- [TtmiCreateTerminal](../../page/77/TtmiCreateTerminal_function_0077C748.md) at `0x0077C796`
- [PspGetNewSessionId](../../page/78/PspGetNewSessionId_function_00789108.md) at `0x0078913B`
- [PspGetNewSessionId](../../page/78/PspGetNewSessionId_function_00789108.md) at `0x007891ED`
- [PspStorageAllocSlot](../../page/78/PspStorageAllocSlot_function_00789B68.md) at `0x00789BE0`
- [PspStorageAllocSlot](../../page/78/PspStorageAllocSlot_function_00789B68.md) at `0x00789BFA`
- [MiAllocatePartitionId](../../page/7F/MiAllocatePartitionId_function_007FD040.md) at `0x007FD0BA`
- [PspSchedulerSharedDataRegionSlotAllocate](../../page/A2/PspSchedulerSharedDataRegionSlotAllocate_function_00A268C8.md) at `0x00A269D6`
- [SepAddLuidToIndexEntry](../../page/A4/SepAddLuidToIndexEntry_function_00A425C0.md) at `0x00A42674`
- [SepAddLuidToIndexEntry](../../page/A4/SepAddLuidToIndexEntry_function_00A425C0.md) at `0x00A42690`
- [SepAddLuidToIndexEntry](../../page/A4/SepAddLuidToIndexEntry_function_00A425C0.md) at `0x00A427A9`
- [SepGetLowBoxNumberEntry](../../page/A6/SepGetLowBoxNumberEntry_function_00A65040.md) at `0x00A650FF`
- [SepGetLowBoxNumberEntry](../../page/A6/SepGetLowBoxNumberEntry_function_00A65040.md) at `0x00A65176`
- [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) at `0x00B75791`
- [RtlApplyHotPatch](../../pagelk/B7/RtlApplyHotPatch_function_00B7528C.md) at `0x00B757C3`
- [ViAllocateFromContiguousMemory](../../pagevrfy/B9/ViAllocateFromContiguousMemory_function_00B97E00.md) at `0x00B97E4E`
- [MiAssignHalEntropy](../../init/C6/MiAssignHalEntropy_function_00C65344.md) at `0x00C6540A`
- [MiAssignSystemVa](../../init/C6/MiAssignSystemVa_function_00C65470.md) at `0x00C654D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E0CD0  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
003E0CD5  53                              push rbx
003E0CD6  55                              push rbp
003E0CD7  56                              push rsi
003E0CD8  57                              push rdi
003E0CD9  41 54                           push r12
003E0CDB  41 55                           push r13
003E0CDD  41 56                           push r14
003E0CDF  41 57                           push r15
003E0CE1  48 83 EC 38                     sub rsp, 0x38
003E0CE5  44 8B 29                        mov r13d, dword ptr [rcx]
003E0CE8  44 8B DA                        mov r11d, edx
003E0CEB  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
003E0CEF  45 3B C5                        cmp r8d, r13d
003E0CF2  4C 8B E1                        mov r12, rcx
003E0CF5  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003E0CFA  1B DB                           sbb ebx, ebx
003E0CFC  41 23 D8                        and ebx, r8d
003E0CFF  45 8D 4D FF                     lea r9d, [r13 - 1]
003E0D03  85 D2                           test edx, edx
003E0D05  0F 84 1B 03 00 00               je 0x1403e1026
003E0D0B  48 8B CF                        mov rcx, rdi
003E0D0E  83 E1 04                        and ecx, 4
003E0D11  8B C1                           mov eax, ecx
003E0D13  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
003E0D1B  48 F7 D8                        neg rax
003E0D1E  8B C3                           mov eax, ebx
003E0D20  45 1B FF                        sbb r15d, r15d
003E0D23  41 83 E7 20                     and r15d, 0x20
003E0D27  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
003E0D2F  41 8D 14 07                     lea edx, [r15 + rax]
003E0D33  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
003E0D3A  47 8D 14 0F                     lea r10d, [r15 + r9]
003E0D3E  48 8B C1                        mov rax, rcx
003E0D41  4C 8B F7                        mov r14, rdi
003E0D44  48 F7 D8                        neg rax
003E0D47  BB 40 00 00 00                  mov ebx, 0x40
003E0D4C  41 8B C2                        mov eax, r10d
003E0D4F  48 1B C9                        sbb rcx, rcx
003E0D52  2B C2                           sub eax, edx
003E0D54  83 E1 04                        and ecx, 4
003E0D57  FF C0                           inc eax
003E0D59  4C 2B F1                        sub r14, rcx
003E0D5C  41 3B C3                        cmp eax, r11d
003E0D5F  0F 82 43 03 00 00               jb 0x1403e10a8
003E0D65  8B CA                           mov ecx, edx
003E0D67  8D 7B FF                        lea edi, [rbx - 1]
003E0D6A  40 22 CF                        and cl, dil
003E0D6D  44 8D 43 C1                     lea r8d, [rbx - 0x3f]
003E0D71  49 D3 E0                        shl r8, cl
003E0D74  41 8B EA                        mov ebp, r10d
003E0D77  41 2B EB                        sub ebp, r11d
003E0D7A  49 FF C8                        dec r8
003E0D7D  FF C5                           inc ebp
003E0D7F  8B C5                           mov eax, ebp
003E0D81  48 C1 E8 06                     shr rax, 6
003E0D85  49 8D 34 C6                     lea rsi, [r14 + rax*8]
003E0D89  8B C2                           mov eax, edx
003E0D8B  48 C1 E8 06                     shr rax, 6
003E0D8F  49 8D 14 C6                     lea rdx, [r14 + rax*8]
003E0D93  4C 0B 02                        or r8, qword ptr [rdx]
003E0D96  41 83 FB 7F                     cmp r11d, 0x7f
003E0D9A  0F 87 8B 01 00 00               ja 0x1403e0f2b
003E0DA0  44 3B DB                        cmp r11d, ebx
003E0DA3  0F 83 42 01 00 00               jae 0x1403e0eeb
003E0DA9  41 83 FB 01                     cmp r11d, 1
003E0DAD  0F 87 CA 00 00 00               ja 0x1403e0e7d
003E0DB3  49 83 F8 FF                     cmp r8, -1
003E0DB7  75 12                           jne 0x1403e0dcb
003E0DB9  48 83 C2 08                     add rdx, 8
003E0DBD  48 3B D6                        cmp rdx, rsi
003E0DC0  0F 87 80 00 00 00               ja 0x1403e0e46
003E0DC6  4C 8B 02                        mov r8, qword ptr [rdx]
003E0DC9  EB E8                           jmp 0x1403e0db3
003E0DCB  49 2B D6                        sub rdx, r14
003E0DCE  49 F7 D0                        not r8
003E0DD1  48 C1 FA 03                     sar rdx, 3
003E0DD5  49 0F BC C0                     bsf rax, r8
003E0DD9  C1 E2 06                        shl edx, 6
003E0DDC  03 D0                           add edx, eax
003E0DDE  8B DA                           mov ebx, edx
003E0DE0  3B D5                           cmp edx, ebp
003E0DE2  77 62                           ja 0x1403e0e46
003E0DE4  83 FB FF                        cmp ebx, -1
003E0DE7  74 60                           je 0x1403e0e49
003E0DE9  41 2B DF                        sub ebx, r15d
003E0DEC  83 FB FF                        cmp ebx, -1
003E0DEF  74 0D                           je 0x1403e0dfe
003E0DF1  45 8B C3                        mov r8d, r11d
003E0DF4  8B D3                           mov edx, ebx
003E0DF6  49 8B CC                        mov rcx, r12
003E0DF9  E8 12 08 00 00                  call 0x1403e1610
003E0DFE  8B C3                           mov eax, ebx
003E0E00  48 83 C4 38                     add rsp, 0x38
003E0E04  41 5F                           pop r15
003E0E06  41 5E                           pop r14
003E0E08  41 5D                           pop r13
003E0E0A  41 5C                           pop r12
003E0E0C  5F                              pop rdi
003E0E0D  5E                              pop rsi
003E0E0E  5D                              pop rbp
003E0E0F  5B                              pop rbx
003E0E10  C3                              ret
003E0E11  CC                              int3
003E0E12  49 0F BD C0                     bsr rax, r8
003E0E16  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E0E1E  0F 84 49 02 00 00               je 0x1403e106d
003E0E24  44 8B C7                        mov r8d, edi
003E0E27  44 2B C0                        sub r8d, eax
003E0E2A  48 8B C2                        mov rax, rdx
003E0E2D  49 2B C6                        sub rax, r14
003E0E30  48 C1 F8 03                     sar rax, 3
003E0E34  FF C0                           inc eax
003E0E36  C1 E0 06                        shl eax, 6
003E0E39  41 2B C0                        sub eax, r8d
003E0E3C  8B D8                           mov ebx, eax
003E0E3E  3B C5                           cmp eax, ebp
003E0E40  0F 86 8A 01 00 00               jbe 0x1403e0fd0
003E0E46  83 CB FF                        or ebx, 0xffffffff
003E0E49  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
003E0E51  83 BC 24 88 00 00 00 00         cmp dword ptr [rsp + 0x88], 0
003E0E59  74 91                           je 0x1403e0dec
003E0E5B  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003E0E63  47 8D 0C 03                     lea r9d, [r11 + r8]
003E0E67  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
003E0E6C  45 3B CD                        cmp r9d, r13d
003E0E6F  45 0F 47 CD                     cmova r9d, r13d
003E0E73  41 FF C9                        dec r9d
003E0E76  33 C0                           xor eax, eax
003E0E78  E9 AA FE FF FF                  jmp 0x1403e0d27
003E0E7D  41 8B C2                        mov eax, r10d
003E0E80  33 DB                           xor ebx, ebx
003E0E82  48 C1 E8 06                     shr rax, 6
003E0E86  45 33 D2                        xor r10d, r10d
003E0E89  49 8D 3C C6                     lea rdi, [r14 + rax*8]
003E0E8D  49 83 F8 FF                     cmp r8, -1
003E0E91  74 7A                           je 0x1403e0f0d
003E0E93  49 0F BC C0                     bsf rax, r8
003E0E97  B9 40 00 00 00                  mov ecx, 0x40
003E0E9C  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E0EA4  0F 44 C1                        cmove eax, ecx
003E0EA7  03 C3                           add eax, ebx
003E0EA9  41 3B C3                        cmp eax, r11d
003E0EAC  73 5B                           jae 0x1403e0f09
003E0EAE  4D 8B C8                        mov r9, r8
003E0EB1  45 8B D3                        mov r10d, r11d
003E0EB4  49 F7 D1                        not r9
003E0EB7  49 8B C1                        mov rax, r9
003E0EBA  41 8B CA                        mov ecx, r10d
003E0EBD  D1 E9                           shr ecx, 1
003E0EBF  48 D3 E8                        shr rax, cl
003E0EC2  4C 23 C8                        and r9, rax
003E0EC5  0F 84 AA 01 00 00               je 0x1403e1075
003E0ECB  44 2B D1                        sub r10d, ecx
003E0ECE  41 83 FA 01                     cmp r10d, 1
003E0ED2  77 E3                           ja 0x1403e0eb7
003E0ED4  49 0F BC D9                     bsf rbx, r9
003E0ED8  49 2B D6                        sub rdx, r14
003E0EDB  48 C1 FA 03                     sar rdx, 3
003E0EDF  C1 E2 06                        shl edx, 6
003E0EE2  03 DA                           add ebx, edx
003E0EE4  3B DD                           cmp ebx, ebp
003E0EE6  E9 F7 FE FF FF                  jmp 0x1403e0de2
003E0EEB  45 33 D2                        xor r10d, r10d
003E0EEE  4D 85 C0                        test r8, r8
003E0EF1  0F 89 1B FF FF FF               jns 0x1403e0e12
003E0EF7  48 83 C2 08                     add rdx, 8
003E0EFB  48 3B D6                        cmp rdx, rsi
003E0EFE  0F 87 42 FF FF FF               ja 0x1403e0e46
003E0F04  4C 8B 02                        mov r8, qword ptr [rdx]
003E0F07  EB E5                           jmp 0x1403e0eee
003E0F09  F7 DB                           neg ebx
003E0F0B  EB CB                           jmp 0x1403e0ed8
003E0F0D  48 83 C2 08                     add rdx, 8
003E0F11  48 3B D6                        cmp rdx, rsi
003E0F14  0F 87 2C FF FF FF               ja 0x1403e0e46
003E0F1A  4C 8B 02                        mov r8, qword ptr [rdx]
003E0F1D  49 83 F8 FF                     cmp r8, -1
003E0F21  74 EA                           je 0x1403e0f0d
003E0F23  41 8B DA                        mov ebx, r10d
003E0F26  E9 68 FF FF FF                  jmp 0x1403e0e93
003E0F2B  40 84 EF                        test dil, bpl
003E0F2E  4C 8D 4E 08                     lea r9, [rsi + 8]
003E0F32  4C 0F 44 CE                     cmove r9, rsi
003E0F36  45 33 D2                        xor r10d, r10d
003E0F39  4D 85 C0                        test r8, r8
003E0F3C  0F 84 1C 01 00 00               je 0x1403e105e
003E0F42  48 83 C2 08                     add rdx, 8
003E0F46  4C 39 12                        cmp qword ptr [rdx], r10
003E0F49  75 54                           jne 0x1403e0f9f
003E0F4B  49 0F BD C0                     bsr rax, r8
003E0F4F  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E0F57  0F 84 09 01 00 00               je 0x1403e1066
003E0F5D  8B CF                           mov ecx, edi
003E0F5F  2B C8                           sub ecx, eax
003E0F61  48 8B DA                        mov rbx, rdx
003E0F64  49 2B DE                        sub rbx, r14
003E0F67  48 C1 FB 03                     sar rbx, 3
003E0F6B  C1 E3 06                        shl ebx, 6
003E0F6E  2B D9                           sub ebx, ecx
003E0F70  3B DD                           cmp ebx, ebp
003E0F72  0F 87 CE FE FF FF               ja 0x1403e0e46
003E0F78  41 8B C3                        mov eax, r11d
003E0F7B  2B C1                           sub eax, ecx
003E0F7D  44 8B C0                        mov r8d, eax
003E0F80  48 C1 E8 06                     shr rax, 6
003E0F84  48 8D 0C C2                     lea rcx, [rdx + rax*8]
003E0F88  48 83 C2 08                     add rdx, 8
003E0F8C  48 3B D1                        cmp rdx, rcx
003E0F8F  0F 84 99 00 00 00               je 0x1403e102e
003E0F95  4C 39 12                        cmp qword ptr [rdx], r10
003E0F98  74 EE                           je 0x1403e0f88
003E0F9A  BB 40 00 00 00                  mov ebx, 0x40
003E0F9F  48 8B C2                        mov rax, rdx
003E0FA2  49 3B D1                        cmp rdx, r9
003E0FA5  0F 87 9B FE FF FF               ja 0x1403e0e46
003E0FAB  48 83 C2 08                     add rdx, 8
003E0FAF  4C 39 12                        cmp qword ptr [rdx], r10
003E0FB2  75 EB                           jne 0x1403e0f9f
003E0FB4  48 8B 00                        mov rax, qword ptr [rax]
003E0FB7  4C 0F BD C0                     bsr r8, rax
003E0FBB  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E0FC3  0F 84 9D 00 00 00               je 0x1403e1066
003E0FC9  8B CF                           mov ecx, edi
003E0FCB  41 2B C8                        sub ecx, r8d
003E0FCE  EB 91                           jmp 0x1403e0f61
003E0FD0  41 8B CB                        mov ecx, r11d
003E0FD3  41 2B C8                        sub ecx, r8d
003E0FD6  0F 84 08 FE FF FF               je 0x1403e0de4
003E0FDC  48 83 C2 08                     add rdx, 8
003E0FE0  41 B9 40 00 00 00               mov r9d, 0x40
003E0FE6  48 8B 02                        mov rax, qword ptr [rdx]
003E0FE9  4C 8B C0                        mov r8, rax
003E0FEC  41 3B C9                        cmp ecx, r9d
003E0FEF  72 15                           jb 0x1403e1006
003E0FF1  48 85 C0                        test rax, rax
003E0FF4  75 28                           jne 0x1403e101e
003E0FF6  83 C1 C0                        add ecx, -0x40
003E0FF9  0F 84 E5 FD FF FF               je 0x1403e0de4
003E0FFF  48 83 C2 08                     add rdx, 8
003E1003  4C 8B 02                        mov r8, qword ptr [rdx]
003E1006  49 0F BC C0                     bsf rax, r8
003E100A  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E1012  41 0F 44 C1                     cmove eax, r9d
003E1016  3B C1                           cmp eax, ecx
003E1018  0F 83 C6 FD FF FF               jae 0x1403e0de4
003E101E  41 8B D9                        mov ebx, r9d
003E1021  E9 C8 FE FF FF                  jmp 0x1403e0eee
003E1026  83 E3 F8                        and ebx, 0xfffffff8
003E1029  E9 BE FD FF FF                  jmp 0x1403e0dec
003E102E  44 23 C7                        and r8d, edi
003E1031  0F 84 AD FD FF FF               je 0x1403e0de4
003E1037  48 8B 02                        mov rax, qword ptr [rdx]
003E103A  48 0F BC C8                     bsf rcx, rax
003E103E  B8 40 00 00 00                  mov eax, 0x40
003E1043  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E104B  0F 44 C8                        cmove ecx, eax
003E104E  41 3B C8                        cmp ecx, r8d
003E1051  0F 83 8D FD FF FF               jae 0x1403e0de4
003E1057  8B D8                           mov ebx, eax
003E1059  E9 41 FF FF FF                  jmp 0x1403e0f9f
003E105E  41 8B CA                        mov ecx, r10d
003E1061  E9 FB FE FF FF                  jmp 0x1403e0f61
003E1066  8B CB                           mov ecx, ebx
003E1068  E9 F4 FE FF FF                  jmp 0x1403e0f61
003E106D  44 8B C3                        mov r8d, ebx
003E1070  E9 B5 FD FF FF                  jmp 0x1403e0e2a
003E1075  48 3B D7                        cmp rdx, rdi
003E1078  0F 84 C8 FD FF FF               je 0x1403e0e46
003E107E  45 33 D2                        xor r10d, r10d
003E1081  49 0F BD C0                     bsr rax, r8
003E1085  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
003E108D  74 12                           je 0x1403e10a1
003E108F  41 8D 5A 3F                     lea ebx, [r10 + 0x3f]
003E1093  2B D8                           sub ebx, eax
003E1095  48 83 C2 08                     add rdx, 8
003E1099  4C 8B 02                        mov r8, qword ptr [rdx]
003E109C  E9 EC FD FF FF                  jmp 0x1403e0e8d
003E10A1  BB 40 00 00 00                  mov ebx, 0x40
003E10A6  EB ED                           jmp 0x1403e1095
003E10A8  83 CB FF                        or ebx, 0xffffffff
003E10AB  E9 A1 FD FF FF                  jmp 0x1403e0e51
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlFindClearBitsAndSet(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;
    unsigned int v_stack_p80;
    unsigned int v_stack_p88;
    unsigned int v_stack_p90;
    unsigned __int64 v_stack_p98;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (56);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 8);
    v_rbx = (unsigned int)((v_rbx) & (a3));
    if (a2 == 0) goto loc_003E1026;
    a1 = (unsigned int)((*(unsigned __int64 *)(a1 + 8)) & (4));
    v_stack_p20 = a1;
    result = -((unsigned int)((unsigned int)(a1)));
    v_r15 = (unsigned int)((v_r15) & (32));
loc_003E0D27:
    v_stack_p10 = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    result = -(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) - ((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1)));
    a1 = (unsigned int)((a1) & (4));
    result = (unsigned int)((result) + 1);
    v_r14 = (*(unsigned __int64 *)(a1 + 8)) - (a1);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(a2)))) goto loc_003E10A8;
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1))) & ((unsigned __int8)(64 - 1)));
    a3 = (64 - 63) << ((unsigned __int8)(a1));
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) - ((unsigned int)((unsigned int)(a2))));
    a3 = (a3) - 1;
    v_rbp = (unsigned int)((v_rbp) + 1);
    result = ((unsigned int)((unsigned int)(v_rbp))) >> (6);
    result = ((unsigned int)((unsigned int)(v_r15 + (unsigned int)((unsigned int)(v_rbx)) * 1))) >> (6);
    a3 = (a3) | (*(unsigned __int64 *)(v_r14 + result * 8));
    if (((unsigned int)((unsigned int)(a2))) > 127) goto loc_003E0F2B;
    if (((unsigned int)((unsigned int)(a2))) >= 64) goto loc_003E0EEB;
    if (((unsigned int)((unsigned int)(a2))) > 1) goto loc_003E0E7D;
loc_003E0DB3:
    if (a3 != -1) goto loc_003E0DCB;
    a2 = (v_r14 + result * 8) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_003E0E46;
    goto loc_003E0DB3;
loc_003E0DCB:
    a2 = (a2) - (v_r14);
    a3 = ~(*(unsigned __int64 *)(a2));
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
loc_003E0DE2:
    if (a2 > ((unsigned int)(v_rbp))) goto loc_003E0E46;
loc_003E0DE4:
    if (((unsigned int)((unsigned int)(a2))) == -1) goto loc_003E0E49;
    v_rbx = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(v_r15)));
loc_003E0DEC:
    if (((unsigned int)(v_rbx)) != -1) {
        a3 = (unsigned int)((unsigned int)(a2));
        a2 = (unsigned int)(v_rbx);
        a1 = a1;
        result = RtlSetBits(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1)) - 1);
    }
    v_rsp = (v_rsp) + (56);
    return (unsigned int)((unsigned int)(v_rbx));
loc_003E0E12:
    v_stack_p80 = (unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1);
    if (condition_is_equal) goto loc_003E106D;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(64 - 1))) - ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
loc_003E0E2A:
    result = (a2) - (v_r14);
    result = (result) >> (3);
    result = (unsigned int)((result) + 1);
    result = (unsigned int)((result) << (6));
    result = (unsigned int)((result) - (a3));
    if (((unsigned int)(result)) <= ((unsigned int)(v_rbp))) goto loc_003E0FD0;
loc_003E0E46:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) | (0xFFFFFFFFULL));
loc_003E0E49:
loc_003E0E51:
    if (v_stack_p88 == 0) goto loc_003E0DEC;
    a4 = (unsigned int)(a2) + (unsigned int)(v_stack_p90) * 1;
    if (((unsigned int)((unsigned int)(a2) + (unsigned int)(v_stack_p90) * 1)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a1))); }
    a4 = (unsigned int)((a4) - 1);
    result = 0;
    goto loc_003E0D27;
loc_003E0E7D:
    v_rbx = 0;
    result = ((unsigned int)((unsigned int)(v_r15 + (unsigned int)(*(unsigned int *)(a1)) - 1 * 1))) >> (6);
    v_r10 = 0;
loc_003E0E8D:
    if (((unsigned int)(v_stack_p90)) == -1) goto loc_003E0F0D;
loc_003E0E93:
    v_stack_p80 = 0;
    if (((unsigned int)(v_stack_p90)) == -1) { result = 64; }
    result = (unsigned int)((result) + (0));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(a2)))) goto loc_003E0F09;
    a4 = ~((unsigned int)(v_stack_p90));
loc_003E0EB7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a2)))))) >> (1));
    result = (a4) >> ((unsigned __int8)(a1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003E1075;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r10)) > 1) goto loc_003E0EB7;
loc_003E0ED8:
    a2 = (a2) - (v_r14);
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) << (6));
    v_rbx = (unsigned int)((v_rbx) + (a2));
    goto loc_003E0DE2;
loc_003E0EEB:
    v_r10 = 0;
loc_003E0EEE:
    if (!sign_flag) goto loc_003E0E12;
    a2 = (a2) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_003E0E46;
    goto loc_003E0EEE;
loc_003E0F09:
    v_rbx = (unsigned int)(-(v_rbx));
    goto loc_003E0ED8;
loc_003E0F0D:
    a2 = (a2) + (8);
    if (a2 > (v_r14 + result * 8)) goto loc_003E0E46;
    if ((*(unsigned __int64 *)(a2)) == -1) goto loc_003E0F0D;
    goto loc_003E0E93;
loc_003E0F2B:
    a4 = v_r14 + result * 8 + 8;
    if ((((unsigned __int8)(v_r14 + result * 8)) & ((unsigned __int8)(v_rbp))) == 0) { a4 = v_r14 + result * 8; }
    v_r10 = 0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003E105E;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003E0F9F;
    v_stack_p80 = 0;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003E1066;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14 + result * 8))) - ((unsigned int)(result)));
loc_003E0F61:
    v_rbx = (a2) - (v_r14);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (unsigned int)((v_rbx) << (6));
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(a1)));
    if (((unsigned int)(v_rbx)) > ((unsigned int)(v_rbp))) goto loc_003E0E46;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(a1)));
    result = (result) >> (6);
loc_003E0F88:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_003E102E;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003E0F88;
loc_003E0F9F:
    if (a2 > a4) goto loc_003E0E46;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_003E0F9F;
    v_stack_p80 = 0;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003E1066;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14 + result * 8))) - ((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_003E0F61;
loc_003E0FD0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)((unsigned int)((unsigned int)(result)))));
    if (condition_is_equal) goto loc_003E0DE4;
    a2 = (a2) + (8);
    if (((unsigned int)(a1)) < 64) goto loc_003E1006;
    if (*(unsigned __int64 *)(a2) != 0) goto loc_003E101E;
    a1 = (unsigned int)((a1) + (-64));
    if (condition_is_equal) goto loc_003E0DE4;
    a2 = (a2) + (8);
loc_003E1006:
    v_stack_p80 = 0;
    result = *(unsigned __int64 *)(a2);
    if (condition_is_equal) { result = 64; }
    if (((unsigned int)(result)) >= ((unsigned int)(a1))) goto loc_003E0DE4;
loc_003E101E:
    goto loc_003E0EEE;
loc_003E1026:
    v_rbx = (unsigned int)((64) & (0xFFFFFFF8ULL));
    goto loc_003E0DEC;
loc_003E102E:
    a3 = (unsigned int)((*(unsigned __int64 *)(a2)) & ((unsigned int)(v_r14 + result * 8)));
    if (condition_is_equal) goto loc_003E0DE4;
    v_stack_p80 = 0;
    if (condition_is_equal) { a1 = 64; }
    if (((unsigned int)(a1)) >= a3) goto loc_003E0DE4;
    goto loc_003E0F9F;
loc_003E105E:
    goto loc_003E0F61;
loc_003E1066:
    goto loc_003E0F61;
loc_003E106D:
    goto loc_003E0E2A;
loc_003E1075:
    if (a2 == (v_r14 + result * 8)) goto loc_003E0E46;
    v_r10 = 0;
    v_stack_p80 = 0;
    if (condition_is_equal) goto loc_003E10A1;
    v_rbx = (unsigned int)((v_r10 + 63) - (64));
loc_003E1095:
    a2 = (a2) + (8);
    goto loc_003E0E8D;
loc_003E10A1:
    goto loc_003E1095;
loc_003E10A8:
    v_rbx = (unsigned int)((64) | (0xFFFFFFFFULL));
    goto loc_003E0E51;
}
```

## 5. (Beta) C Style

```c
int64_t RtlFindClearBitsAndSet(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;
    uint32_t v_stack_p80;
    uint32_t v_stack_p88;
    uint32_t v_stack_p90;
    uint64_t v_stack_p98;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (56);
    v_stack_m58 = *(uint64_t *)(arg1 + 0x8);
    local_rbx = (uint32_t)((local_rbx) & (Arg3));
    if (Arg2 == 0) goto loc_003E1026;
    Arg1 = (uint32_t)((*(uint64_t *)(arg1 + 0x8)) & (4));
    v_stack_p20 = Arg1;
    result = -((uint32_t)((uint32_t)(Arg1)));
    local_r15 = (uint32_t)((local_r15) & (32));
loc_003E0D27:
    v_stack_p10 = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    result = -(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) - ((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1)));
    Arg1 = (uint32_t)((Arg1) & (4));
    result = (uint32_t)((result) + 1);
    local_r14 = (*(uint64_t *)(arg1 + 0x8)) - (Arg1);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_003E10A8;
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1))) & ((uint8_t)(64 - 1)));
    Arg3 = (64 - 63) << ((uint8_t)(Arg1));
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) - ((uint32_t)((uint32_t)(Arg2))));
    Arg3 = (Arg3) - 1;
    local_rbp = (uint32_t)((local_rbp) + 1);
    result = ((uint32_t)((uint32_t)(local_rbp))) >> (6);
    result = ((uint32_t)((uint32_t)(local_r15 + (uint32_t)((uint32_t)(local_rbx)) * 1))) >> (6);
    Arg3 = (Arg3) | (*(uint64_t *)(local_r14 + result * 8));
    if (((uint32_t)((uint32_t)(Arg2))) > 127) goto loc_003E0F2B;
    if (((uint32_t)((uint32_t)(Arg2))) >= 64) goto loc_003E0EEB;
    if (((uint32_t)((uint32_t)(Arg2))) > 1) goto loc_003E0E7D;
loc_003E0DB3:
    if (Arg3 != -1) goto loc_003E0DCB;
    Arg2 = (local_r14 + result * 8) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_003E0E46;
    goto loc_003E0DB3;
loc_003E0DCB:
    Arg2 = (Arg2) - (local_r14);
    Arg3 = ~(*(uint64_t *)(Arg2));
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) << (6));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
loc_003E0DE2:
    if (Arg2 > ((uint32_t)(local_rbp))) goto loc_003E0E46;
loc_003E0DE4:
    if (((uint32_t)((uint32_t)(Arg2))) == -1) goto loc_003E0E49;
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(local_r15)));
loc_003E0DEC:
    if (((uint32_t)(local_rbx)) != -1) {
        Arg3 = (uint32_t)((uint32_t)(Arg2));
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = Arg1;
        result = RtlSetBits(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1)) - 1);
    }
    local_rsp = (local_rsp) + (56);
    return (uint32_t)((uint32_t)(local_rbx));
loc_003E0E12:
    v_stack_p80 = (uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1);
    if (condition_is_equal) goto loc_003E106D;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(64 - 1))) - ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
loc_003E0E2A:
    result = (Arg2) - (local_r14);
    result = (result) >> (3);
    result = (uint32_t)((result) + 1);
    result = (uint32_t)((result) << (6));
    result = (uint32_t)((result) - (Arg3));
    if (((uint32_t)(result)) <= ((uint32_t)(local_rbp))) goto loc_003E0FD0;
loc_003E0E46:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) | (0xFFFFFFFFULL));
loc_003E0E49:
loc_003E0E51:
    if (v_stack_p88 == 0) goto loc_003E0DEC;
    a4 = (uint32_t)(Arg2) + (uint32_t)(v_stack_p90) * 1;
    if (((uint32_t)((uint32_t)(Arg2) + (uint32_t)(v_stack_p90) * 1)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) { a4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1))); }
    a4 = (uint32_t)((a4) - 1);
    result = 0;
    goto loc_003E0D27;
loc_003E0E7D:
    local_rbx = 0;
    result = ((uint32_t)((uint32_t)(local_r15 + (uint32_t)(*(uint32_t *)(arg1)) - 1 * 1))) >> (6);
    local_r10 = 0;
loc_003E0E8D:
    if (((uint32_t)(v_stack_p90)) == -1) goto loc_003E0F0D;
loc_003E0E93:
    v_stack_p80 = 0;
    if (((uint32_t)(v_stack_p90)) == -1) { result = 64; }
    result = (uint32_t)((result) + (0));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_003E0F09;
    a4 = ~((uint32_t)(v_stack_p90));
loc_003E0EB7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg2)))))) >> (1));
    result = (a4) >> ((uint8_t)(Arg1));
    a4 = (a4) & (result);
    if (condition_is_equal) goto loc_003E1075;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r10)) > 1) goto loc_003E0EB7;
loc_003E0ED8:
    Arg2 = (Arg2) - (local_r14);
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) << (6));
    local_rbx = (uint32_t)((local_rbx) + (Arg2));
    goto loc_003E0DE2;
loc_003E0EEB:
    local_r10 = 0;
loc_003E0EEE:
    if (!sign_flag) goto loc_003E0E12;
    Arg2 = (Arg2) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_003E0E46;
    goto loc_003E0EEE;
loc_003E0F09:
    local_rbx = (uint32_t)(-(local_rbx));
    goto loc_003E0ED8;
loc_003E0F0D:
    Arg2 = (Arg2) + (8);
    if (Arg2 > (local_r14 + result * 8)) goto loc_003E0E46;
    if ((*(uint64_t *)(Arg2)) == -1) goto loc_003E0F0D;
    goto loc_003E0E93;
loc_003E0F2B:
    a4 = local_r14 + result * 8 + 8;
    if ((((uint8_t)(local_r14 + result * 8)) & ((uint8_t)(local_rbp))) == 0) { a4 = local_r14 + result * 8; }
    local_r10 = 0;
    if (*(uint64_t *)(Arg2) == 0) goto loc_003E105E;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003E0F9F;
    v_stack_p80 = 0;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003E1066;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14 + result * 8))) - ((uint32_t)(result)));
loc_003E0F61:
    local_rbx = (Arg2) - (local_r14);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (uint32_t)((local_rbx) << (6));
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_rbx)) > ((uint32_t)(local_rbp))) goto loc_003E0E46;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_003E0F88:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_003E102E;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003E0F88;
loc_003E0F9F:
    if (Arg2 > a4) goto loc_003E0E46;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_003E0F9F;
    v_stack_p80 = 0;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003E1066;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14 + result * 8))) - ((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_003E0F61;
loc_003E0FD0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)((uint32_t)((uint32_t)(result)))));
    if (condition_is_equal) goto loc_003E0DE4;
    Arg2 = (Arg2) + (8);
    if (((uint32_t)(Arg1)) < 64) goto loc_003E1006;
    if (*(uint64_t *)(Arg2) != 0) goto loc_003E101E;
    Arg1 = (uint32_t)((Arg1) + (-64));
    if (condition_is_equal) goto loc_003E0DE4;
    Arg2 = (Arg2) + (8);
loc_003E1006:
    v_stack_p80 = 0;
    result = *(uint64_t *)(Arg2);
    if (condition_is_equal) { result = 64; }
    if (((uint32_t)(result)) >= ((uint32_t)(Arg1))) goto loc_003E0DE4;
loc_003E101E:
    goto loc_003E0EEE;
loc_003E1026:
    local_rbx = (uint32_t)((64) & (0xFFFFFFF8ULL));
    goto loc_003E0DEC;
loc_003E102E:
    Arg3 = (uint32_t)((*(uint64_t *)(Arg2)) & ((uint32_t)(local_r14 + result * 8)));
    if (condition_is_equal) goto loc_003E0DE4;
    v_stack_p80 = 0;
    if (condition_is_equal) { Arg1 = 64; }
    if (((uint32_t)(Arg1)) >= Arg3) goto loc_003E0DE4;
    goto loc_003E0F9F;
loc_003E105E:
    goto loc_003E0F61;
loc_003E1066:
    goto loc_003E0F61;
loc_003E106D:
    goto loc_003E0E2A;
loc_003E1075:
    if (Arg2 == (local_r14 + result * 8)) goto loc_003E0E46;
    local_r10 = 0;
    v_stack_p80 = 0;
    if (condition_is_equal) goto loc_003E10A1;
    local_rbx = (uint32_t)((local_r10 + 63) - (64));
loc_003E1095:
    Arg2 = (Arg2) + (8);
    goto loc_003E0E8D;
loc_003E10A1:
    goto loc_003E1095;
loc_003E10A8:
    local_rbx = (uint32_t)((64) | (0xFFFFFFFFULL));
    goto loc_003E0E51;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E0CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
