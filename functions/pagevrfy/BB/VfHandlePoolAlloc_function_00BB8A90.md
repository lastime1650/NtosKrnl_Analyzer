# VfHandlePoolAlloc

- RVA: `0x00BB8A90`–`0x00BB8EFB` (길이 `1,131` bytes)
- VA: `0x0000000140BB8A90`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A85F0`
- 디코드: `314`개 명령, `1,131/1,131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **21**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x00BB8AE7` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (function, `0x00B84080`)
- `0x00BB8AFF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00BB8B10` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (function, `0x00B84270`)
- `0x00BB8B39` → [VfTargetDriversGetVerifierData](VfTargetDriversGetVerifierData_function_00BB7E6C.md) (function, `0x00BB7E6C`)
- `0x00BB8B57` → [ExAllocatePoolWithTagPriority](../../text/43/ExAllocatePoolWithTagPriority_function_0043E5F0.md) (function, `0x0043E5F0`)
- `0x00BB8B8D` → [ExAllocatePoolSanityChecks](ExAllocatePoolSanityChecks_function_00BB42E4.md) (function, `0x00BB42E4`)
- `0x00BB8BD3` → [VfFaultsIsSystemSufficientlyBooted](../BA/VfFaultsIsSystemSufficientlyBooted_function_00BA664C.md) (function, `0x00BA664C`)
- `0x00BB8C04` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)
- `0x00BB8C86` → [VfTargetDriversGetVerifierData](VfTargetDriversGetVerifierData_function_00BB7E6C.md) (function, `0x00BB7E6C`)
- `0x00BB8CAC` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00BB8CBC` → [ViGrowPoolAllocation](../../text/61/ViGrowPoolAllocation_function_00614290.md) (function, `0x00614290`)
- `0x00BB8CF1` → [ExAllocatePoolWithTagPriority](../../text/43/ExAllocatePoolWithTagPriority_function_0043E5F0.md) (function, `0x0043E5F0`)
- `0x00BB8D0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00BB8D19` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (function, `0x00B84270`)
- `0x00BB8D4A` → [ViTargetUpdateTreeAllowed](../B9/ViTargetUpdateTreeAllowed_function_00B9BC04.md) (function, `0x00B9BC04`)
- `0x00BB8D56` → [VfDriverIsKernelImageAddress](VfDriverIsKernelImageAddress_function_00BB7EBC.md) (function, `0x00BB7EBC`)
- `0x00BB8D65` → [VfAvlInitializeLockContext](../../text/4A/VfAvlInitializeLockContext_function_004A686C.md) (function, `0x004A686C`)
- `0x00BB8D7B` → [VfAvlLookupTreeNode](../../text/3E/VfAvlLookupTreeNode_function_003EF1B4.md) (function, `0x003EF1B4`)
- `0x00BB8D9D` → [VfAvlCleanupLockContext](../../text/3E/VfAvlCleanupLockContext_function_003EF56C.md) (function, `0x003EF56C`)
- `0x00BB8DAE` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x00BB8DBE` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00BB8E21` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)
- `0x00BB8E6F` → [ViPostPoolAllocation](../BA/ViPostPoolAllocation_function_00BA18E0.md) (function, `0x00BA18E0`)
- `0x00BB8EB3` → [ViPtLogPoolTraceWrapper](../B9/ViPtLogPoolTraceWrapper_function_00B92100.md) (function, `0x00B92100`)
- `0x00BB8ED7` → [VfFillAllocatedMemory](../B9/VfFillAllocatedMemory_function_00B9BCF4.md) (function, `0x00B9BCF4`)

### Direct callers
- [ExAllocatePoolWithTagFromNode](../../text/35/ExAllocatePoolWithTagFromNode_function_0035A944.md) at `0x0035A9A1`
- [CcFlushCachePriv](../../text/35/CcFlushCachePriv_function_0035B040.md) at `0x0035B287`
- [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) at `0x0035B638`
- [ExAllocatePoolMm](../../text/35/ExAllocatePoolMm_function_0035B690.md) at `0x0035B765`
- [MiGetInPageAutoBoostLock](../../text/36/MiGetInPageAutoBoostLock_function_0036D3CC.md) at `0x0036D463`
- [MiStoreGetWriteSupport](../../text/45/MiStoreGetWriteSupport_function_00456DF0.md) at `0x00456E8A`
- [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) at `0x00B821DC`
- [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) at `0x00B8449A`
- [IovAllocateMdl](../B9/IovAllocateMdl_function_00B92350.md) at `0x00B923F9`
- [IovAllocateWorkItem](../B9/IovAllocateWorkItem_function_00B92490.md) at `0x00B924DB`
- [ViIrpAllocateLockedPacket](../B9/ViIrpAllocateLockedPacket_function_00B9E0AC.md) at `0x00B9E129`
- [ViSpIoSetCompletionRoutineEx_Exit](ViSpIoSetCompletionRoutineEx_Exit_function_00BB4A00.md) at `0x00BB4A43`
- [ViSpRtlReplaceStringBuffer](ViSpRtlReplaceStringBuffer_function_00BB4E34.md) at `0x00BB4E7D`

### Static image references
- `0x00BB8B1D` → RVA `0x00F04ABC` (`.data`; read)
- `0x00BB8B77` → RVA `0x00F04A20` (`.data`; read)
- `0x00BB8B9B` → RVA `0x00E0E944` (`.data`; read)
- `0x00BB8BB8` → RVA `0x00F04A30` (`.data`; read/write)
- `0x00BB8BC9` → RVA `0x00E681A0` (`.data`; read)
- `0x00BB8C18` → RVA `0x00F03EA0` (`.data`; read)
- `0x00BB8C27` → RVA `0x00FC5124` (`ALMOSTRO`; read)
- `0x00BB8C56` → RVA `0x00F04980` (`.data`; read)
- `0x00BB8CA0` → RVA `0x00F04A5C` (`.data`; read/write)
- `0x00BB8D2D` → RVA `0x00F04A48` (`.data`; read/write)
- `0x00BB8D74` → RVA `0x00F049A0` (`.data`; read)
- `0x00BB8DCF` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00BB8DE7` → RVA `0x00FFDD20` (`PAGEVRFD`; read/write)
- `0x00BB8E17` → RVA `0x00F04A34` (`.data`; read/write)
- `0x00BB8E39` → RVA `0x00F04A38` (`.data`; read/write)
- `0x00BB8E7E` → RVA `0x00E0EA70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x00BB8AE7` → [ExpPoolFlagsToPoolType](../../poolcode/B8/ExpPoolFlagsToPoolType_function_00B84080.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BB8AFF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BB8B10` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BB8B57` → [ExAllocatePoolWithTagPriority](../../text/43/ExAllocatePoolWithTagPriority_function_0043E5F0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8CAC` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8CBC` → [ViGrowPoolAllocation](../../text/61/ViGrowPoolAllocation_function_00614290.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8CF1` → [ExAllocatePoolWithTagPriority](../../text/43/ExAllocatePoolWithTagPriority_function_0043E5F0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8D0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BB8D19` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (`PAGEVRFY` → `POOLCODE`)
  - `0x00BB8D65` → [VfAvlInitializeLockContext](../../text/4A/VfAvlInitializeLockContext_function_004A686C.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8D7B` → [VfAvlLookupTreeNode](../../text/3E/VfAvlLookupTreeNode_function_003EF1B4.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8D9D` → [VfAvlCleanupLockContext](../../text/3E/VfAvlCleanupLockContext_function_003EF56C.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8DAE` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8DBE` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGEVRFY` → `.text`)
  - `0x00BB8E21` → [ExIsSpecialPoolAddress](../../text/49/ExIsSpecialPoolAddress_function_0049C410.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB8A90  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00BB8A95  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00BB8A9A  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00BB8A9E  55                              push rbp
00BB8A9F  56                              push rsi
00BB8AA0  57                              push rdi
00BB8AA1  41 54                           push r12
00BB8AA3  41 55                           push r13
00BB8AA5  41 56                           push r14
00BB8AA7  41 57                           push r15
00BB8AA9  48 8B EC                        mov rbp, rsp
00BB8AAC  48 81 EC 80 00 00 00            sub rsp, 0x80
00BB8AB3  45 33 FF                        xor r15d, r15d
00BB8AB6  45 8B F1                        mov r14d, r9d
00BB8AB9  44 89 7D C8                     mov dword ptr [rbp - 0x38], r15d
00BB8ABD  49 8B F8                        mov rdi, r8
00BB8AC0  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00BB8AC4  48 8B DA                        mov rbx, rdx
00BB8AC7  8B F1                           mov esi, ecx
00BB8AC9  45 8B EF                        mov r13d, r15d
00BB8ACC  48 85 D2                        test rdx, rdx
00BB8ACF  74 4C                           je 0x140bb8b1d
00BB8AD1  48 8D 45 48                     lea rax, [rbp + 0x48]
00BB8AD5  33 D2                           xor edx, edx
00BB8AD7  4C 8D 4D C0                     lea r9, [rbp - 0x40]
00BB8ADB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB8AE0  4C 8D 45 40                     lea r8, [rbp + 0x40]
00BB8AE4  48 8B CB                        mov rcx, rbx
00BB8AE7  E8 94 B5 FC FF                  call 0x140b84080
00BB8AEC  85 C0                           test eax, eax
00BB8AEE  79 2A                           jns 0x140bb8b1a
00BB8AF0  45 8B C6                        mov r8d, r14d
00BB8AF3  48 8B D7                        mov rdx, rdi
00BB8AF6  4C 8B 4D 68                     mov r9, qword ptr [rbp + 0x68]
00BB8AFA  4D 85 C9                        test r9, r9
00BB8AFD  75 0A                           jne 0x140bb8b09
00BB8AFF  E8 EC 95 FC FF                  call 0x140b820f0
00BB8B04  E9 D6 03 00 00                  jmp 0x140bb8edf
00BB8B09  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00BB8B0C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00BB8B10  E8 5B B7 FC FF                  call 0x140b84270
00BB8B15  E9 C5 03 00 00                  jmp 0x140bb8edf
00BB8B1A  8B 75 40                        mov esi, dword ptr [rbp + 0x40]
00BB8B1D  44 39 3D 98 BF 34 00            cmp dword ptr [rip + 0x34bf98], r15d
00BB8B24  4C 8B 65 78                     mov r12, qword ptr [rbp + 0x78]
00BB8B28  74 4D                           je 0x140bb8b77
00BB8B2A  40 84 F6                        test sil, sil
00BB8B2D  79 37                           jns 0x140bb8b66
00BB8B2F  49 8B CC                        mov rcx, r12
00BB8B32  C7 45 C8 01 00 00 00            mov dword ptr [rbp - 0x38], 1
00BB8B39  E8 2E F3 FF FF                  call 0x140bb7e6c
00BB8B3E  4C 8B E8                        mov r13, rax
00BB8B41  48 85 C0                        test rax, rax
00BB8B44  75 31                           jne 0x140bb8b77
00BB8B46  45 8B C6                        mov r8d, r14d
00BB8B49  48 8B D7                        mov rdx, rdi
00BB8B4C  48 85 DB                        test rbx, rbx
00BB8B4F  75 10                           jne 0x140bb8b61
00BB8B51  44 8B 4D 60                     mov r9d, dword ptr [rbp + 0x60]
00BB8B55  8B CE                           mov ecx, esi
00BB8B57  E8 94 5A 88 FF                  call 0x14043e5f0
00BB8B5C  E9 7E 03 00 00                  jmp 0x140bb8edf
00BB8B61  48 8B CB                        mov rcx, rbx
00BB8B64  EB 90                           jmp 0x140bb8af6
00BB8B66  0F BA EE 07                     bts esi, 7
00BB8B6A  89 75 40                        mov dword ptr [rbp + 0x40], esi
00BB8B6D  48 85 DB                        test rbx, rbx
00BB8B70  74 05                           je 0x140bb8b77
00BB8B72  48 0F BA EB 09                  bts rbx, 9
00BB8B77  8B 05 A3 BE 34 00               mov eax, dword ptr [rip + 0x34bea3]
00BB8B7D  A8 01                           test al, 1
00BB8B7F  74 11                           je 0x140bb8b92
00BB8B81  4D 8B CC                        mov r9, r12
00BB8B84  4C 8D 45 58                     lea r8, [rbp + 0x58]
00BB8B88  48 8B D7                        mov rdx, rdi
00BB8B8B  8B CE                           mov ecx, esi
00BB8B8D  E8 52 B7 FF FF                  call 0x140bb42e4
00BB8B92  44 89 7D C4                     mov dword ptr [rbp - 0x3c], r15d
00BB8B96  48 85 FF                        test rdi, rdi
00BB8B99  75 15                           jne 0x140bb8bb0
00BB8B9B  83 3D A2 5D 25 00 01            cmp dword ptr [rip + 0x255da2], 1
00BB8BA2  77 0C                           ja 0x140bb8bb0
00BB8BA4  C7 45 C4 01 00 00 00            mov dword ptr [rbp - 0x3c], 1
00BB8BAB  BF 01 00 00 00                  mov edi, 1
00BB8BB0  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
00BB8BB4  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
00BB8BB8  F0 FF 05 71 BE 34 00            lock inc dword ptr [rip + 0x34be71]
00BB8BBF  4C 63 7D 40                     movsxd r15, dword ptr [rbp + 0x40]
00BB8BC3  41 F6 C7 02                     test r15b, 2
00BB8BC7  74 40                           je 0x140bb8c09
00BB8BC9  8B 05 D1 F5 2A 00               mov eax, dword ptr [rip + 0x2af5d1]
00BB8BCF  A8 04                           test al, 4
00BB8BD1  74 36                           je 0x140bb8c09
00BB8BD3  E8 74 DA FE FF                  call 0x140ba664c
00BB8BD8  85 C0                           test eax, eax
00BB8BDA  74 2D                           je 0x140bb8c09
00BB8BDC  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00BB8BDF  BA 9A 00 00 00                  mov edx, 0x9a
00BB8BE4  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00BB8BE9  4D 8B C7                        mov r8, r15
00BB8BEC  49 0F BA F0 07                  btr r8, 7
00BB8BF1  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00BB8BF9  4C 8B CF                        mov r9, rdi
00BB8BFC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BB8C01  8D 4A 28                        lea ecx, [rdx + 0x28]
00BB8C04  E8 FB 4C FE FF                  call 0x140b9d904
00BB8C09  48 8B 05 90 F5 2A 00            mov rax, qword ptr [rip + 0x2af590]
00BB8C10  44 8B 75 60                     mov r14d, dword ptr [rbp + 0x60]
00BB8C14  A8 01                           test al, 1
00BB8C16  75 09                           jne 0x140bb8c21
00BB8C18  80 3D 81 B2 34 00 00            cmp byte ptr [rip + 0x34b281], 0
00BB8C1F  74 2B                           je 0x140bb8c4c
00BB8C21  41 F6 C6 09                     test r14b, 9
00BB8C25  75 13                           jne 0x140bb8c3a
00BB8C27  83 3D F6 C4 40 00 01            cmp dword ptr [rip + 0x40c4f6], 1
00BB8C2E  75 06                           jne 0x140bb8c36
00BB8C30  41 83 CE 08                     or r14d, 8
00BB8C34  EB 04                           jmp 0x140bb8c3a
00BB8C36  41 83 CE 09                     or r14d, 9
00BB8C3A  48 85 DB                        test rbx, rbx
00BB8C3D  74 0D                           je 0x140bb8c4c
00BB8C3F  48 B9 00 00 00 00 01 00 00 00   movabs rcx, 0x100000000
00BB8C49  48 0B D9                        or rbx, rcx
00BB8C4C  33 F6                           xor esi, esi
00BB8C4E  A8 08                           test al, 8
00BB8C50  0F 84 89 00 00 00               je 0x140bb8cdf
00BB8C56  0F BA 25 22 BD 34 00 0C         bt dword ptr [rip + 0x34bd22], 0xc
00BB8C5E  0F 93 C1                        setae cl
00BB8C61  41 F6 C7 20                     test r15b, 0x20
00BB8C65  0F 94 C0                        sete al
00BB8C68  84 C8                           test al, cl
00BB8C6A  74 73                           je 0x140bb8cdf
00BB8C6C  81 7D 58 56 69 49 6E            cmp dword ptr [rbp + 0x58], 0x6e496956
00BB8C73  74 6A                           je 0x140bb8cdf
00BB8C75  81 7D 58 43 61 72 4E            cmp dword ptr [rbp + 0x58], 0x4e726143
00BB8C7C  74 61                           je 0x140bb8cdf
00BB8C7E  39 75 C8                        cmp dword ptr [rbp - 0x38], esi
00BB8C81  75 0B                           jne 0x140bb8c8e
00BB8C83  49 8B CC                        mov rcx, r12
00BB8C86  E8 E1 F1 FF FF                  call 0x140bb7e6c
00BB8C8B  4C 8B E8                        mov r13, rax
00BB8C8E  4D 85 ED                        test r13, r13
00BB8C91  74 0D                           je 0x140bb8ca0
00BB8C93  48 8D 47 08                     lea rax, [rdi + 8]
00BB8C97  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00BB8C9B  48 3B C7                        cmp rax, rdi
00BB8C9E  77 08                           ja 0x140bb8ca8
00BB8CA0  FF 05 B6 BD 34 00               inc dword ptr [rip + 0x34bdb6]
00BB8CA6  EB 37                           jmp 0x140bb8cdf
00BB8CA8  49 8D 4D 50                     lea rcx, [r13 + 0x50]
00BB8CAC  E8 BF 18 B0 FF                  call 0x1406ba570
00BB8CB1  48 8B F0                        mov rsi, rax
00BB8CB4  48 85 C0                        test rax, rax
00BB8CB7  75 10                           jne 0x140bb8cc9
00BB8CB9  49 8B CD                        mov rcx, r13
00BB8CBC  E8 CF B5 A5 FF                  call 0x140614290
00BB8CC1  48 8B F0                        mov rsi, rax
00BB8CC4  48 85 C0                        test rax, rax
00BB8CC7  74 16                           je 0x140bb8cdf
00BB8CC9  48 8B 7D C8                     mov rdi, qword ptr [rbp - 0x38]
00BB8CCD  41 83 CF 40                     or r15d, 0x40
00BB8CD1  44 89 7D 40                     mov dword ptr [rbp + 0x40], r15d
00BB8CD5  48 85 DB                        test rbx, rbx
00BB8CD8  74 0A                           je 0x140bb8ce4
00BB8CDA  48 0F BA EB 0A                  bts rbx, 0xa
00BB8CDF  48 85 DB                        test rbx, rbx
00BB8CE2  75 14                           jne 0x140bb8cf8
00BB8CE4  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
00BB8CE8  45 8B CE                        mov r9d, r14d
00BB8CEB  48 8B D7                        mov rdx, rdi
00BB8CEE  41 8B CF                        mov ecx, r15d
00BB8CF1  E8 FA 58 88 FF                  call 0x14043e5f0
00BB8CF6  EB 26                           jmp 0x140bb8d1e
00BB8CF8  4C 8B 4D 68                     mov r9, qword ptr [rbp + 0x68]
00BB8CFC  48 8B D7                        mov rdx, rdi
00BB8CFF  44 8B 45 58                     mov r8d, dword ptr [rbp + 0x58]
00BB8D03  48 8B CB                        mov rcx, rbx
00BB8D06  4D 85 C9                        test r9, r9
00BB8D09  75 07                           jne 0x140bb8d12
00BB8D0B  E8 E0 93 FC FF                  call 0x140b820f0
00BB8D10  EB 0C                           jmp 0x140bb8d1e
00BB8D12  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
00BB8D15  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00BB8D19  E8 52 B5 FC FF                  call 0x140b84270
00BB8D1E  48 8B D8                        mov rbx, rax
00BB8D21  48 85 C0                        test rax, rax
00BB8D24  0F 85 A1 00 00 00               jne 0x140bb8dcb
00BB8D2A  8D 58 01                        lea ebx, [rax + 1]
00BB8D2D  01 1D 15 BD 34 00               add dword ptr [rip + 0x34bd15], ebx
00BB8D33  F7 05 E3 BC 34 00 00 10 00 00   test dword ptr [rip + 0x34bce3], 0x1000
00BB8D3D  74 63                           je 0x140bb8da2
00BB8D3F  0F 57 C0                        xorps xmm0, xmm0
00BB8D42  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00BB8D46  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00BB8D4A  E8 B5 2E FE FF                  call 0x140b9bc04
00BB8D4F  85 C0                           test eax, eax
00BB8D51  74 4F                           je 0x140bb8da2
00BB8D53  49 8B CC                        mov rcx, r12
00BB8D56  E8 61 F1 FF FF                  call 0x140bb7ebc
00BB8D5B  85 C0                           test eax, eax
00BB8D5D  75 43                           jne 0x140bb8da2
00BB8D5F  8B D3                           mov edx, ebx
00BB8D61  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00BB8D65  E8 02 DB 8E FF                  call 0x1404a686c
00BB8D6A  44 8B CB                        mov r9d, ebx
00BB8D6D  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00BB8D71  4D 8B C4                        mov r8, r12
00BB8D74  48 8D 0D 25 BC 34 00            lea rcx, [rip + 0x34bc25]
00BB8D7B  E8 34 64 83 FF                  call 0x1403ef1b4
00BB8D80  48 85 C0                        test rax, rax
00BB8D83  74 14                           je 0x140bb8d99
00BB8D85  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
00BB8D89  48 85 C0                        test rax, rax
00BB8D8C  74 0B                           je 0x140bb8d99
00BB8D8E  F0 01 98 B0 00 00 00            lock add dword ptr [rax + 0xb0], ebx
00BB8D95  44 8B 7D 40                     mov r15d, dword ptr [rbp + 0x40]
00BB8D99  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00BB8D9D  E8 CA 67 83 FF                  call 0x1403ef56c
00BB8DA2  48 85 F6                        test rsi, rsi
00BB8DA5  74 0C                           je 0x140bb8db3
00BB8DA7  49 8D 4D 50                     lea rcx, [r13 + 0x50]
00BB8DAB  48 8B D6                        mov rdx, rsi
00BB8DAE  E8 FD 17 B0 FF                  call 0x1406ba5b0
00BB8DB3  41 F6 C7 10                     test r15b, 0x10
00BB8DB7  74 0B                           je 0x140bb8dc4
00BB8DB9  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00BB8DBE  E8 8D DC 73 FF                  call 0x1402f6a50
00BB8DC3  CC                              int3
00BB8DC4  33 C0                           xor eax, eax
00BB8DC6  E9 14 01 00 00                  jmp 0x140bb8edf
00BB8DCB  83 7D C4 00                     cmp dword ptr [rbp - 0x3c], 0
00BB8DCF  4C 8D 2D 2A 72 44 FF            lea r13, [rip - 0xbb8dd6]
00BB8DD6  74 3C                           je 0x140bb8e14
00BB8DD8  8B 05 C2 F3 2A 00               mov eax, dword ptr [rip + 0x2af3c2]
00BB8DDE  A8 08                           test al, 8
00BB8DE0  74 32                           je 0x140bb8e14
00BB8DE2  B8 01 00 00 00                  mov eax, 1
00BB8DE7  F0 0F C1 05 31 4F 44 00         lock xadd dword ptr [rip + 0x444f31], eax
00BB8DEF  FF C0                           inc eax
00BB8DF1  83 E0 0F                        and eax, 0xf
00BB8DF4  48 8D 0C 40                     lea rcx, [rax + rax*2]
00BB8DF8  41 C7 84 CD 10 F8 FF 00 01 00 00 00  mov dword ptr [r13 + rcx*8 + 0xfff810], 1
00BB8E04  4D 89 A4 CD 18 F8 FF 00         mov qword ptr [r13 + rcx*8 + 0xfff818], r12
00BB8E0C  49 89 9C CD 20 F8 FF 00         mov qword ptr [r13 + rcx*8 + 0xfff820], rbx
00BB8E14  45 33 FF                        xor r15d, r15d
00BB8E17  F0 FF 05 16 BC 34 00            lock inc dword ptr [rip + 0x34bc16]
00BB8E1E  48 8B CB                        mov rcx, rbx
00BB8E21  E8 EA 35 8E FF                  call 0x14049c410
00BB8E26  83 F8 01                        cmp eax, 1
00BB8E29  75 05                           jne 0x140bb8e30
00BB8E2B  44 8B F8                        mov r15d, eax
00BB8E2E  EB 09                           jmp 0x140bb8e39
00BB8E30  48 81 FF E0 0F 00 00            cmp rdi, 0xfe0
00BB8E37  76 07                           jbe 0x140bb8e40
00BB8E39  F0 FF 05 F8 BB 34 00            lock inc dword ptr [rip + 0x34bbf8]
00BB8E40  44 8B 75 58                     mov r14d, dword ptr [rbp + 0x58]
00BB8E44  48 85 F6                        test rsi, rsi
00BB8E47  74 2B                           je 0x140bb8e74
00BB8E49  8B 55 40                        mov edx, dword ptr [rbp + 0x40]
00BB8E4C  48 8B CE                        mov rcx, rsi
00BB8E4F  41 8B C7                        mov eax, r15d
00BB8E52  48 0B C3                        or rax, rbx
00BB8E55  4C 89 66 08                     mov qword ptr [rsi + 8], r12
00BB8E59  48 89 06                        mov qword ptr [rsi], rax
00BB8E5C  45 85 FF                        test r15d, r15d
00BB8E5F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00BB8E63  48 0F 44 C7                     cmove rax, rdi
00BB8E67  4C 89 76 18                     mov qword ptr [rsi + 0x18], r14
00BB8E6B  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
00BB8E6F  E8 6C 8A FE FF                  call 0x140ba18e0
00BB8E74  8B 05 26 F3 2A 00               mov eax, dword ptr [rip + 0x2af326]
00BB8E7A  A8 08                           test al, 8
00BB8E7C  74 5E                           je 0x140bb8edc
00BB8E7E  8B 0D EC 5B 25 00               mov ecx, dword ptr [rip + 0x255bec]
00BB8E84  8D 41 FF                        lea eax, [rcx - 1]
00BB8E87  83 F8 09                        cmp eax, 9
00BB8E8A  77 17                           ja 0x140bb8ea3
00BB8E8C  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00BB8E8F  3B D1                           cmp edx, ecx
00BB8E91  73 27                           jae 0x140bb8eba
00BB8E93  8B C2                           mov eax, edx
00BB8E95  45 39 B4 85 D8 81 E6 00         cmp dword ptr [r13 + rax*4 + 0xe681d8], r14d
00BB8E9D  74 04                           je 0x140bb8ea3
00BB8E9F  FF C2                           inc edx
00BB8EA1  EB EC                           jmp 0x140bb8e8f
00BB8EA3  48 8B 7D D8                     mov rdi, qword ptr [rbp - 0x28]
00BB8EA7  45 33 C9                        xor r9d, r9d
00BB8EAA  4C 8B C7                        mov r8, rdi
00BB8EAD  41 8B D6                        mov edx, r14d
00BB8EB0  48 8B CB                        mov rcx, rbx
00BB8EB3  E8 48 92 FD FF                  call 0x140b92100
00BB8EB8  EB 04                           jmp 0x140bb8ebe
00BB8EBA  48 8B 7D D8                     mov rdi, qword ptr [rbp - 0x28]
00BB8EBE  48 85 F6                        test rsi, rsi
00BB8EC1  74 19                           je 0x140bb8edc
00BB8EC3  45 85 FF                        test r15d, r15d
00BB8EC6  75 14                           jne 0x140bb8edc
00BB8EC8  F7 45 40 00 04 00 00            test dword ptr [rbp + 0x40], 0x400
00BB8ECF  75 0B                           jne 0x140bb8edc
00BB8ED1  48 8B D7                        mov rdx, rdi
00BB8ED4  48 8B CB                        mov rcx, rbx
00BB8ED7  E8 18 2E FE FF                  call 0x140b9bcf4
00BB8EDC  48 8B C3                        mov rax, rbx
00BB8EDF  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00BB8EE7  48 81 C4 80 00 00 00            add rsp, 0x80
00BB8EEE  41 5F                           pop r15
00BB8EF0  41 5E                           pop r14
00BB8EF2  41 5D                           pop r13
00BB8EF4  41 5C                           pop r12
00BB8EF6  5F                              pop rdi
00BB8EF7  5E                              pop rsi
00BB8EF8  5D                              pop rbp
00BB8EF9  C3                              ret
00BB8EFA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfHandlePoolAlloc(int a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_r15 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    if (a2 == 0) goto loc_00BB8B1D;
    a2 = 0;
    v_stack_m98 = v_stack_p10;
    result = ExpPoolFlagsToPoolType(0, a2, v_stack_p8, v_stack_m78);
    if (!sign_flag) goto loc_00BB8B1A;
loc_00BB8AF6:
    if (a6 != 0) goto loc_00BB8B09;
    result = ExAllocatePool2(0, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), a6);
    goto loc_00BB8EDF;
loc_00BB8B09:
    v_stack_m98 = (unsigned int)((unsigned int)(a7));
    result = ExAllocatePool3(0, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), a6);
    goto loc_00BB8EDF;
loc_00BB8B1A:
loc_00BB8B1D:
    if ((*(unsigned int *)(v_rip + 3456920)) == 0) goto loc_00BB8B77;
    if (!sign_flag) goto loc_00BB8B66;
    v_stack_m70 = 1;
    result = VfTargetDriversGetVerifierData(a8, a3, (unsigned int)((unsigned int)((unsigned int)(a4))), a6);
    if (result != 0) goto loc_00BB8B77;
    if (0 != 0) goto loc_00BB8B61;
    result = ExAllocatePoolWithTagPriority((unsigned int)((unsigned int)((unsigned int)(v_stack_p8))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))), (unsigned int)(a5));
    goto loc_00BB8EDF;
loc_00BB8B61:
    goto loc_00BB8AF6;
loc_00BB8B66:
    v_stack_p8 = (unsigned int)((unsigned int)(v_stack_p8));
    if (0 != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 3456675));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3456675)))) & (1)) != 0) {
        a4 = a8;
        a3 = v_stack_p20;
        a2 = a3;
        a1 = (unsigned int)((unsigned int)(v_stack_p8));
        result = ExAllocatePoolSanityChecks(a1, a2, a3, a4);
    }
    v_stack_m74 = 0;
    if (a3 != 0) goto loc_00BB8BB0;
    v_rdi = a3;
    if ((*(unsigned int *)(v_rip + 2448802)) <= 1) {
        v_stack_m74 = 1;
        v_rdi = 1;
    }
    v_stack_m58 = v_rdi;
    v_stack_m60 = v_rdi;
    if ((((unsigned __int8)((int)(v_stack_p8))) & (2)) == 0) goto loc_00BB8C09;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2815441)))) & (4)) == 0) goto loc_00BB8C09;
    result = VfFaultsIsSystemSufficientlyBooted(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        result = v_stack_p20;
        a2 = 154;
        v_stack_m88 = a8;
        a3 = (int)(v_stack_p8);
        v_stack_m90 = 2;
        a4 = v_rdi;
        v_stack_m98 = result;
        a1 = a2 + 40;
        result = CarReportRuleViolationFromNt(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 2815376))) & (1)) != 0) goto loc_00BB8C21;
    if ((*(unsigned __int8 *)(v_rip + 3453569)) == 0) goto loc_00BB8C4C;
loc_00BB8C21:
    if ((((unsigned __int8)((unsigned int)(a5))) & (9)) != 0) goto loc_00BB8C3A;
    if ((*(unsigned int *)(v_rip + 4244726)) != 1) goto loc_00BB8C36;
    v_r14 = (unsigned int)(((unsigned int)(a5)) | (8));
    goto loc_00BB8C3A;
loc_00BB8C36:
    v_r14 = (unsigned int)((v_r14) | (9));
loc_00BB8C3A:
    v_rbx = a2;
    if (a2 != 0) {
        v_rbx = (a2) | (a1);
    }
    v_rsi = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 2815376))) & (8)) == 0) goto loc_00BB8CDF;
    a1 = (condition_is_above_or_equal) ? 1 : 0;
    result = ((((unsigned __int8)((int)(v_stack_p8))) & (32)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00BB8CDF;
    if (v_stack_p20 == 0x6E496956ULL) goto loc_00BB8CDF;
    if (v_stack_p20 == 0x4E726143ULL) goto loc_00BB8CDF;
    v_r13 = result;
    if (v_stack_m70 == 0) {
        a1 = a8;
        result = VfTargetDriversGetVerifierData(a1, a2, a3, a4);
        v_r13 = result;
    }
    if (v_r13 == 0) goto loc_00BB8CA0;
    v_stack_m70 = v_rdi + 8;
    if ((v_rdi + 8) > v_rdi) goto loc_00BB8CA8;
loc_00BB8CA0:
    goto loc_00BB8CDF;
loc_00BB8CA8:
    result = ExpInterlockedPopEntrySList(v_r13 + 80, a2, a3, a4);
    if (result != 0) goto loc_00BB8CC9;
    result = ViGrowPoolAllocation(v_r13, a2, a3, a4);
    if (result == 0) goto loc_00BB8CDF;
loc_00BB8CC9:
    v_r15 = (unsigned int)(((int)(v_stack_p8)) | (64));
    v_stack_p8 = (unsigned int)(v_r15);
    if (v_rbx == 0) goto loc_00BB8CE4;
loc_00BB8CDF:
    if (v_rbx != 0) goto loc_00BB8CF8;
loc_00BB8CE4:
    result = ExAllocatePoolWithTagPriority((unsigned int)((unsigned int)(v_r15)), v_stack_m70, (unsigned int)(v_stack_p20), (unsigned int)((unsigned int)(v_r14)));
    goto loc_00BB8D1E;
loc_00BB8CF8:
    if (a6 != 0) goto loc_00BB8D12;
    result = ExAllocatePool2(v_rbx, v_stack_m70, (unsigned int)(v_stack_p20), a6);
    goto loc_00BB8D1E;
loc_00BB8D12:
    v_stack_m98 = (unsigned int)((unsigned int)(a7));
    result = ExAllocatePool3(v_rbx, v_stack_m70, (unsigned int)(v_stack_p20), a6);
loc_00BB8D1E:
    if (result != 0) goto loc_00BB8DCB;
    if (((*(unsigned int *)(v_rip + 3456227)) & (0x1000ULL)) == 0) goto loc_00BB8DA2;
    v_stack_m40 = result;
    v_stack_m50 = v_xmm0;
    result = ViTargetUpdateTreeAllowed(v_rbx, v_stack_m70, (unsigned int)(v_stack_p20), a6);
    if ((unsigned int)(result) == 0) goto loc_00BB8DA2;
    result = VfDriverIsKernelImageAddress(a8, v_stack_m70, (unsigned int)(v_stack_p20), a6);
    if ((unsigned int)(result) != 0) goto loc_00BB8DA2;
    result = VfAvlInitializeLockContext(v_stack_m50, (unsigned int)((unsigned int)(result + 1)), (unsigned int)(v_stack_p20), a6);
    result = VfAvlLookupTreeNode(v_rip + 3456037, v_stack_m50, a8, (unsigned int)((unsigned int)(result + 1)));
    if (result == 0) goto loc_00BB8D99;
    if (*(unsigned __int64 *)(result + 64) != 0) {
        v_r15 = v_stack_p8;
    }
    result = VfAvlCleanupLockContext(v_stack_m50, v_stack_m50, a8, (unsigned int)((unsigned int)(result + 1)));
loc_00BB8DA2:
    if (result != 0) {
        a1 = v_r13 + 80;
        a2 = result;
        result = ExpInterlockedPushEntrySList(a1, a2, a8, (unsigned int)((unsigned int)(result + 1)));
    }
    if ((((unsigned __int8)(v_r15)) & (16)) != 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, a2, a8, (unsigned int)((unsigned int)(result + 1)));
    }
    result = 0;
    goto loc_00BB8EDF;
loc_00BB8DCB:
    if (v_stack_m74 == 0) goto loc_00BB8E14;
    result = (unsigned int)(*(unsigned int *)(v_rip + 2814914));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2814914)))) & (8)) != 0) {
        result = 1;
        result = (unsigned int)((result) + 1);
        result = (unsigned int)((result) & (15));
        a1 = result + result * 2;
        *(unsigned int *)(v_rip - 12291542 + a1 * 8 + 16775184) = 1;
        *(unsigned __int64 *)(v_rip - 12291542 + a1 * 8 + 16775192) = a8;
        *(unsigned __int64 *)(v_rip - 12291542 + a1 * 8 + 16775200) = result + 1;
    }
    v_r15 = 0;
    result = ExIsSpecialPoolAddress(result + 1, a2, a8, (unsigned int)((unsigned int)(result + 1)));
    if (((unsigned int)(result)) != 1) goto loc_00BB8E30;
    goto loc_00BB8E39;
loc_00BB8E30:
    if (v_stack_m70 >= = 0xFE0ULL) {
    }
    if (result != 0) {
        a2 = v_stack_p8;
        a1 = result;
        result = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = (result) | (result + 1);
        *(unsigned __int64 *)(result + 8) = a8;
        *(unsigned __int64 *)(result) = result;
        result = v_stack_m58;
        if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) { result = v_stack_m70; }
        *(unsigned __int64 *)(result + 24) = (unsigned int)(v_stack_p20);
        *(unsigned __int64 *)(result + 16) = result;
        result = ViPostPoolAllocation(a1, a2, a8, (unsigned int)((unsigned int)(result + 1)));
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2814758)))) & (8)) == 0) goto loc_00BB8EDC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2448364)) - 1)) > 9) goto loc_00BB8EA3;
loc_00BB8E8F:
    if (((unsigned int)((unsigned int)(v_stack_m68))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2448364))))) goto loc_00BB8EBA;
    if ((*(unsigned int *)(v_rip - 12291542 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m68))) * 4 + 15106520)) == ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_00BB8EA3;
    a2 = (unsigned int)(((unsigned int)(v_stack_m68)) + 1);
    goto loc_00BB8E8F;
loc_00BB8EA3:
    a4 = 0;
    result = ViPtLogPoolTraceWrapper(result + 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p20))), v_stack_m60, a4);
    goto loc_00BB8EBE;
loc_00BB8EBA:
loc_00BB8EBE:
    if (result == 0) goto loc_00BB8EDC;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_00BB8EDC;
    if (((v_stack_p8) & (0x400ULL)) == 0) {
        a2 = v_stack_m60;
        a1 = result + 1;
        result = VfFillAllocatedMemory(a1, a2, v_stack_m60, a4);
    }
loc_00BB8EDF:
    v_rsp = (v_rsp) + (128);
    return result + 1;
}
```

## 5. (Beta) C Style

```c
int64_t VfHandlePoolAlloc(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r15 = 0;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    if (Arg2 == 0) goto loc_00BB8B1D;
    Arg2 = 0;
    v_stack_m98 = v_stack_p10;
    result = ExpPoolFlagsToPoolType(0, Arg2, v_stack_p8, v_stack_m78);
    if (!sign_flag) goto loc_00BB8B1A;
loc_00BB8AF6:
    if (Arg6 != 0) goto loc_00BB8B09;
    result = ExAllocatePool2(0, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg6);
    goto loc_00BB8EDF;
loc_00BB8B09:
    v_stack_m98 = (uint32_t)((uint32_t)(Arg7));
    result = ExAllocatePool3(0, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg6);
    goto loc_00BB8EDF;
loc_00BB8B1A:
loc_00BB8B1D:
    if ((*(uint32_t *)(v_rip + 0x34BF98)) == 0) goto loc_00BB8B77;
    if (!sign_flag) goto loc_00BB8B66;
    v_stack_m70 = 1;
    result = VfTargetDriversGetVerifierData(Arg8, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), Arg6);
    if (result != 0) goto loc_00BB8B77;
    if (0 != 0) goto loc_00BB8B61;
    result = ExAllocatePoolWithTagPriority((uint32_t)((uint32_t)((uint32_t)(v_stack_p8))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))), (uint32_t)(Arg5));
    goto loc_00BB8EDF;
loc_00BB8B61:
    goto loc_00BB8AF6;
loc_00BB8B66:
    v_stack_p8 = (uint32_t)((uint32_t)(v_stack_p8));
    if (0 != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x34BEA3));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x34BEA3)))) & (1)) != 0) {
        Arg4 = Arg8;
        Arg3 = v_stack_p20;
        Arg2 = Arg3;
        Arg1 = (uint32_t)((uint32_t)(v_stack_p8));
        result = ExAllocatePoolSanityChecks(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m74 = 0;
    if (Arg3 != 0) goto loc_00BB8BB0;
    local_rdi = Arg3;
    if ((*(uint32_t *)(v_rip + 0x255DA2)) <= 1) {
        v_stack_m74 = 1;
        local_rdi = 1;
    }
    v_stack_m58 = local_rdi;
    v_stack_m60 = local_rdi;
    if ((((uint8_t)((int32_t)(v_stack_p8))) & (2)) == 0) goto loc_00BB8C09;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2AF5D1)))) & (4)) == 0) goto loc_00BB8C09;
    result = VfFaultsIsSystemSufficientlyBooted(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = v_stack_p20;
        Arg2 = 154;
        v_stack_m88 = Arg8;
        Arg3 = (int32_t)(v_stack_p8);
        v_stack_m90 = 2;
        Arg4 = local_rdi;
        v_stack_m98 = result;
        Arg1 = Arg2 + 40;
        result = CarReportRuleViolationFromNt(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x2AF590))) & (1)) != 0) goto loc_00BB8C21;
    if ((*(uint8_t *)(v_rip + 0x34B281)) == 0) goto loc_00BB8C4C;
loc_00BB8C21:
    if ((((uint8_t)((uint32_t)(Arg5))) & (9)) != 0) goto loc_00BB8C3A;
    if ((*(uint32_t *)(v_rip + 0x40C4F6)) != 1) goto loc_00BB8C36;
    local_r14 = (uint32_t)(((uint32_t)(Arg5)) | (8));
    goto loc_00BB8C3A;
loc_00BB8C36:
    local_r14 = (uint32_t)((local_r14) | (9));
loc_00BB8C3A:
    local_rbx = Arg2;
    if (Arg2 != 0) {
        local_rbx = (Arg2) | (Arg1);
    }
    local_rsi = 0;
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x2AF590))) & (8)) == 0) goto loc_00BB8CDF;
    Arg1 = (condition_is_above_or_equal) ? 1 : 0;
    result = ((((uint8_t)((int32_t)(v_stack_p8))) & (32)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00BB8CDF;
    if (v_stack_p20 == 0x6E496956ULL) goto loc_00BB8CDF;
    if (v_stack_p20 == 0x4E726143ULL) goto loc_00BB8CDF;
    local_r13 = result;
    if (v_stack_m70 == 0) {
        Arg1 = Arg8;
        result = VfTargetDriversGetVerifierData(Arg1, Arg2, Arg3, Arg4);
        local_r13 = result;
    }
    if (local_r13 == 0) goto loc_00BB8CA0;
    v_stack_m70 = local_rdi + 8;
    if ((local_rdi + 8) > local_rdi) goto loc_00BB8CA8;
loc_00BB8CA0:
    goto loc_00BB8CDF;
loc_00BB8CA8:
    result = ExpInterlockedPopEntrySList(local_r13 + 80, Arg2, Arg3, Arg4);
    if (result != 0) goto loc_00BB8CC9;
    result = ViGrowPoolAllocation(local_r13, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00BB8CDF;
loc_00BB8CC9:
    local_r15 = (uint32_t)(((int32_t)(v_stack_p8)) | (64));
    v_stack_p8 = (uint32_t)(local_r15);
    if (local_rbx == 0) goto loc_00BB8CE4;
loc_00BB8CDF:
    if (local_rbx != 0) goto loc_00BB8CF8;
loc_00BB8CE4:
    result = ExAllocatePoolWithTagPriority((uint32_t)((uint32_t)(local_r15)), v_stack_m70, (uint32_t)(v_stack_p20), (uint32_t)((uint32_t)(local_r14)));
    goto loc_00BB8D1E;
loc_00BB8CF8:
    if (Arg6 != 0) goto loc_00BB8D12;
    result = ExAllocatePool2(local_rbx, v_stack_m70, (uint32_t)(v_stack_p20), Arg6);
    goto loc_00BB8D1E;
loc_00BB8D12:
    v_stack_m98 = (uint32_t)((uint32_t)(Arg7));
    result = ExAllocatePool3(local_rbx, v_stack_m70, (uint32_t)(v_stack_p20), Arg6);
loc_00BB8D1E:
    if (result != 0) goto loc_00BB8DCB;
    if (((*(uint32_t *)(v_rip + 0x34BCE3)) & (0x1000ULL)) == 0) goto loc_00BB8DA2;
    v_stack_m40 = result;
    v_stack_m50 = v_xmm0;
    result = ViTargetUpdateTreeAllowed(local_rbx, v_stack_m70, (uint32_t)(v_stack_p20), Arg6);
    if ((uint32_t)(result) == 0) goto loc_00BB8DA2;
    result = VfDriverIsKernelImageAddress(Arg8, v_stack_m70, (uint32_t)(v_stack_p20), Arg6);
    if ((uint32_t)(result) != 0) goto loc_00BB8DA2;
    result = VfAvlInitializeLockContext(v_stack_m50, (uint32_t)((uint32_t)(result + 1)), (uint32_t)(v_stack_p20), Arg6);
    result = VfAvlLookupTreeNode(v_rip + 3456037, v_stack_m50, Arg8, (uint32_t)((uint32_t)(result + 1)));
    if (result == 0) goto loc_00BB8D99;
    if (*(uint64_t *)(result + 0x40) != 0) {
        local_r15 = v_stack_p8;
    }
    result = VfAvlCleanupLockContext(v_stack_m50, v_stack_m50, Arg8, (uint32_t)((uint32_t)(result + 1)));
loc_00BB8DA2:
    if (result != 0) {
        Arg1 = local_r13 + 80;
        Arg2 = result;
        result = ExpInterlockedPushEntrySList(Arg1, Arg2, Arg8, (uint32_t)((uint32_t)(result + 1)));
    }
    if ((((uint8_t)(local_r15)) & (16)) != 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, Arg2, Arg8, (uint32_t)((uint32_t)(result + 1)));
    }
    result = 0;
    goto loc_00BB8EDF;
loc_00BB8DCB:
    if (v_stack_m74 == 0) goto loc_00BB8E14;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x2AF3C2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2AF3C2)))) & (8)) != 0) {
        result = 1;
        result = (uint32_t)((result) + 1);
        result = (uint32_t)((result) & (15));
        Arg1 = result + result * 2;
        *(uint32_t *)(v_rip - 0xBB8DD6 + Arg1 * 8 + 0xFFF810) = 1;
        *(uint64_t *)(v_rip - 0xBB8DD6 + Arg1 * 8 + 0xFFF818) = Arg8;
        *(uint64_t *)(v_rip - 0xBB8DD6 + Arg1 * 8 + 0xFFF820) = result + 1;
    }
    local_r15 = 0;
    result = ExIsSpecialPoolAddress(result + 1, Arg2, Arg8, (uint32_t)((uint32_t)(result + 1)));
    if (((uint32_t)(result)) != 1) goto loc_00BB8E30;
    goto loc_00BB8E39;
loc_00BB8E30:
    if (v_stack_m70 >= = 0xFE0ULL) {
    }
    if (result != 0) {
        Arg2 = v_stack_p8;
        Arg1 = result;
        result = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = (result) | (result + 1);
        *(uint64_t *)(result + 0x8) = Arg8;
        *(uint64_t *)(result) = result;
        result = v_stack_m58;
        if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) { result = v_stack_m70; }
        *(uint64_t *)(result + 0x18) = (uint32_t)(v_stack_p20);
        *(uint64_t *)(result + 0x10) = result;
        result = ViPostPoolAllocation(Arg1, Arg2, Arg8, (uint32_t)((uint32_t)(result + 1)));
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2AF326)))) & (8)) == 0) goto loc_00BB8EDC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x255BEC)) - 1)) > 9) goto loc_00BB8EA3;
loc_00BB8E8F:
    if (((uint32_t)((uint32_t)(v_stack_m68))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x255BEC))))) goto loc_00BB8EBA;
    if ((*(uint32_t *)(v_rip - 0xBB8DD6 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m68))) * 4 + 0xE681D8)) == ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_00BB8EA3;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m68)) + 1);
    goto loc_00BB8E8F;
loc_00BB8EA3:
    Arg4 = 0;
    result = ViPtLogPoolTraceWrapper(result + 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p20))), v_stack_m60, Arg4);
    goto loc_00BB8EBE;
loc_00BB8EBA:
loc_00BB8EBE:
    if (result == 0) goto loc_00BB8EDC;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_00BB8EDC;
    if (((v_stack_p8) & (0x400ULL)) == 0) {
        Arg2 = v_stack_m60;
        Arg1 = result + 1;
        result = VfFillAllocatedMemory(Arg1, Arg2, v_stack_m60, Arg4);
    }
loc_00BB8EDF:
    local_rsp = (local_rsp) + (128);
    return result + 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB8A90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
