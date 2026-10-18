# IopWriteFileGather

- RVA: `0x00AAA95C`–`0x00AAB02B` (길이 `1,743` bytes)
- VA: `0x0000000140AAA95C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBD4C`
- 디코드: `428`개 명령, `1,743/1,743` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AAA9DD` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00AAAAA4` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (function, `0x0040EC90`)
- `0x00AAAAE1` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AAABF2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AAAC22` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AAAC3D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AAAD47` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AAAD60` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x00AAADA6` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x00AAADBC` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x00AAAE29` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00AAAEC4` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x00AAAED6` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00AAAEF3` → [MmProbeAndLockSelectedPages](../../text/23/MmProbeAndLockSelectedPages_function_0023F790.md) (function, `0x0023F790`)
- `0x00AAAF1A` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (function, `0x00456468`)
- `0x00AAAF5C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AAAFCF` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x00AAAFFC` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00AAB010` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IopIoRingDispatchWriteGather](../72/IopIoRingDispatchWriteGather_function_007203F0.md) at `0x007204E4`
- [NtWriteFileGather](../AC/NtWriteFileGather_function_00AC3AE0.md) at `0x00AC3BB0`

### Static image references
- `0x00AAAD24` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x00AAAEF8` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **14**
  - `0x00AAA9DD` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x00AAAAA4` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (`PAGE` → `.text`)
  - `0x00AAAC22` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AAAC3D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AAAD60` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x00AAADA6` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x00AAADBC` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x00AAAE29` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00AAAEC4` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x00AAAED6` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x00AAAEF3` → [MmProbeAndLockSelectedPages](../../text/23/MmProbeAndLockSelectedPages_function_0023F790.md) (`PAGE` → `.text`)
  - `0x00AAAF1A` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (`PAGE` → `.text`)
  - `0x00AAAF5C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AAB010` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAA95C  48 8B C4                        mov rax, rsp
00AAA95F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AAA963  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AAA967  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AAA96B  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AAA96F  53                              push rbx
00AAA970  56                              push rsi
00AAA971  57                              push rdi
00AAA972  41 54                           push r12
00AAA974  41 55                           push r13
00AAA976  41 56                           push r14
00AAA978  41 57                           push r15
00AAA97A  48 81 EC 90 00 00 00            sub rsp, 0x90
00AAA981  4C 8B F9                        mov r15, rcx
00AAA984  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
00AAA98C  33 FF                           xor edi, edi
00AAA98E  8B F7                           mov esi, edi
00AAA990  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00AAA994  48 89 78 98                     mov qword ptr [rax - 0x68], rdi
00AAA998  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AAA99D  89 78 88                        mov dword ptr [rax - 0x78], edi
00AAA9A0  48 89 78 80                     mov qword ptr [rax - 0x80], rdi
00AAA9A4  C6 44 24 42 01                  mov byte ptr [rsp + 0x42], 1
00AAA9A9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AAA9B2  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00AAA9BA  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00AAA9C0  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00AAA9C4  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
00AAA9C7  A8 02                           test al, 2
00AAA9C9  74 0B                           je 0x140aaa9d6
00AAA9CB  39 BC 24 38 01 00 00            cmp dword ptr [rsp + 0x138], edi
00AAA9D2  B3 01                           mov bl, 1
00AAA9D4  7D 03                           jge 0x140aaa9d9
00AAA9D6  40 8A DF                        mov bl, dil
00AAA9D9  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
00AAA9DD  E8 3E 07 7F FF                  call 0x14029b120
00AAA9E2  4C 8B E0                        mov r12, rax
00AAA9E5  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AAA9EA  41 8B 4F 50                     mov ecx, dword ptr [r15 + 0x50]
00AAA9EE  F6 C1 08                        test cl, 8
00AAA9F1  0F 84 E6 05 00 00               je 0x140aaafdd
00AAA9F7  84 DB                           test bl, bl
00AAA9F9  0F 85 DE 05 00 00               jne 0x140aaafdd
00AAA9FF  44 8B B4 24 08 01 00 00         mov r14d, dword ptr [rsp + 0x108]
00AAAA07  41 F7 C6 FF 0F 00 00            test r14d, 0xfff
00AAAA0E  8B CF                           mov ecx, edi
00AAAA10  0F 95 C1                        setne cl
00AAAA13  41 8B C6                        mov eax, r14d
00AAAA16  C1 E8 0C                        shr eax, 0xc
00AAAA19  03 C8                           add ecx, eax
00AAAA1B  39 8C 24 F8 00 00 00            cmp dword ptr [rsp + 0xf8], ecx
00AAAA22  0F 85 B5 05 00 00               jne 0x140aaafdd
00AAAA28  41 8B 44 24 30                  mov eax, dword ptr [r12 + 0x30]
00AAAA2D  A8 04                           test al, 4
00AAAA2F  0F 85 A8 05 00 00               jne 0x140aaafdd
00AAAA35  41 8B 4C 24 48                  mov ecx, dword ptr [r12 + 0x48]
00AAAA3A  83 F9 36                        cmp ecx, 0x36
00AAAA3D  77 10                           ja 0x140aaaa4f
00AAAA3F  48 BA 48 03 10 00 01 00 40 00   movabs rdx, 0x40000100100348
00AAAA49  48 0F A3 CA                     bt rdx, rcx
00AAAA4D  72 09                           jb 0x140aaaa58
00AAAA4F  83 F9 53                        cmp ecx, 0x53
00AAAA52  0F 85 85 05 00 00               jne 0x140aaafdd
00AAAA58  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00AAAA5D  45 84 C9                        test r9b, r9b
00AAAA60  0F 84 D1 00 00 00               je 0x140aaab37
00AAAA66  48 39 BC 24 28 01 00 00         cmp qword ptr [rsp + 0x128], rdi
00AAAA6E  0F 85 C3 00 00 00               jne 0x140aaab37
00AAAA74  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00AAAA7C  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00AAAA86  48 3B CB                        cmp rcx, rbx
00AAAA89  48 0F 43 CB                     cmovae rcx, rbx
00AAAA8D  8B 01                           mov eax, dword ptr [rcx]
00AAAA8F  89 01                           mov dword ptr [rcx], eax
00AAAA91  45 33 C0                        xor r8d, r8d
00AAAA94  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00AAAA9C  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00AAAAA4  E8 E7 41 96 FF                  call 0x14040ec90
00AAAAA9  49 39 BF B0 00 00 00            cmp qword ptr [r15 + 0xb0], rdi
00AAAAB0  74 20                           je 0x140aaaad2
00AAAAB2  48 F7 84 24 E0 00 00 00 FE FF FF FF  test qword ptr [rsp + 0xe0], -2
00AAAABE  74 12                           je 0x140aaaad2
00AAAAC0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AAAAC5  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AAAAC9  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AAAACD  E9 10 05 00 00                  jmp 0x140aaafe2
00AAAAD2  BA 03 00 00 00                  mov edx, 3
00AAAAD7  4D 85 ED                        test r13, r13
00AAAADA  74 21                           je 0x140aaaafd
00AAAADC  44 84 EA                        test dl, r13b
00AAAADF  74 06                           je 0x140aaaae7
00AAAAE1  E8 EA F4 DE FF                  call 0x140899fd0
00AAAAE6  CC                              int3
00AAAAE7  48 8B C3                        mov rax, rbx
00AAAAEA  4C 3B EB                        cmp r13, rbx
00AAAAED  49 0F 42 C5                     cmovb rax, r13
00AAAAF1  90                              nop
00AAAAF2  8A 00                           mov al, byte ptr [rax]
00AAAAF4  49 8B 45 00                     mov rax, qword ptr [r13]
00AAAAF8  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AAAAFD  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
00AAAB05  48 85 C9                        test rcx, rcx
00AAAB08  74 11                           je 0x140aaab1b
00AAAB0A  48 8B C3                        mov rax, rbx
00AAAB0D  48 3B CB                        cmp rcx, rbx
00AAAB10  48 0F 42 C1                     cmovb rax, rcx
00AAAB14  90                              nop
00AAAB15  8B 00                           mov eax, dword ptr [rax]
00AAAB17  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AAAB1B  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00AAAB20  EB 45                           jmp 0x140aaab67
00AAAB22  33 FF                           xor edi, edi
00AAAB24  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AAAB2C  8B F7                           mov esi, edi
00AAAB2E  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AAAB32  E9 AB 04 00 00                  jmp 0x140aaafe2
00AAAB37  4D 85 ED                        test r13, r13
00AAAB3A  74 09                           je 0x140aaab45
00AAAB3C  49 8B 45 00                     mov rax, qword ptr [r13]
00AAAB40  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AAAB45  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00AAAB4D  48 BB 00 00 FF FF FF 7F 00 00   movabs rbx, 0x7fffffff0000
00AAAB57  BA 03 00 00 00                  mov edx, 3
00AAAB5C  48 85 C0                        test rax, rax
00AAAB5F  74 06                           je 0x140aaab67
00AAAB61  8B 00                           mov eax, dword ptr [rax]
00AAAB63  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00AAAB67  45 84 C9                        test r9b, r9b
00AAAB6A  0F 84 90 01 00 00               je 0x140aaad00
00AAAB70  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00AAAB74  C1 E8 05                        shr eax, 5
00AAAB77  F7 D0                           not eax
00AAAB79  83 E0 04                        and eax, 4
00AAAB7C  83 C8 02                        or eax, 2
00AAAB7F  84 84 24 20 01 00 00            test byte ptr [rsp + 0x120], al
00AAAB86  75 0A                           jne 0x140aaab92
00AAAB88  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AAAB8D  E9 50 04 00 00                  jmp 0x140aaafe2
00AAAB92  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00AAAB99  4C 8D 24 C5 00 00 00 00         lea r12, [rax*8]
00AAABA1  4D 85 E4                        test r12, r12
00AAABA4  74 69                           je 0x140aaac0f
00AAABA6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AAABAF  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00AAABB6  48 39 B8 10 03 00 00            cmp qword ptr [rax + 0x310], rdi
00AAABBD  74 24                           je 0x140aaabe3
00AAABBF  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
00AAABC6  B9 4C 01 00 00                  mov ecx, 0x14c
00AAABCB  66 3B C1                        cmp ax, cx
00AAABCE  74 0D                           je 0x140aaabdd
00AAABD0  B9 C4 01 00 00                  mov ecx, 0x1c4
00AAABD5  66 3B C1                        cmp ax, cx
00AAABD8  40 8A C7                        mov al, dil
00AAABDB  75 02                           jne 0x140aaabdf
00AAABDD  B0 01                           mov al, 1
00AAABDF  84 C0                           test al, al
00AAABE1  75 05                           jne 0x140aaabe8
00AAABE3  BA 07 00 00 00                  mov edx, 7
00AAABE8  48 85 94 24 00 01 00 00         test qword ptr [rsp + 0x100], rdx
00AAABF0  74 05                           je 0x140aaabf7
00AAABF2  E8 D9 F3 DE FF                  call 0x140899fd0
00AAABF7  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00AAABFF  49 8D 0C 04                     lea rcx, [r12 + rax]
00AAAC03  48 3B CB                        cmp rcx, rbx
00AAAC06  77 05                           ja 0x140aaac0d
00AAAC08  48 3B C8                        cmp rcx, rax
00AAAC0B  73 02                           jae 0x140aaac0f
00AAAC0D  8A 03                           mov al, byte ptr [rbx]
00AAAC0F  45 85 F6                        test r14d, r14d
00AAAC12  74 43                           je 0x140aaac57
00AAAC14  41 B8 49 6F 53 41               mov r8d, 0x41536f49
00AAAC1A  49 8B D4                        mov rdx, r12
00AAAC1D  B9 23 01 00 00                  mov ecx, 0x123
00AAAC22  E8 C9 74 0D 00                  call 0x140b820f0
00AAAC27  4C 8B F0                        mov r14, rax
00AAAC2A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AAAC2F  4D 8B C4                        mov r8, r12
00AAAC32  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00AAAC3A  48 8B C8                        mov rcx, rax
00AAAC3D  E8 FE BB C1 FF                  call 0x1406c6840
00AAAC42  4C 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r14
00AAAC4A  44 8B B4 24 08 01 00 00         mov r14d, dword ptr [rsp + 0x108]
00AAAC52  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00AAAC57  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00AAAC5C  EB 15                           jmp 0x140aaac73
00AAAC5E  33 FF                           xor edi, edi
00AAAC60  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AAAC68  8B F7                           mov esi, edi
00AAAC6A  8B 5C 24 44                     mov ebx, dword ptr [rsp + 0x44]
00AAAC6E  E9 6F 03 00 00                  jmp 0x140aaafe2
00AAAC73  45 84 C9                        test r9b, r9b
00AAAC76  0F 84 84 00 00 00               je 0x140aaad00
00AAAC7C  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00AAAC80  A8 08                           test al, 8
00AAAC82  74 4E                           je 0x140aaacd2
00AAAC84  41 0F B7 8C 24 30 01 00 00      movzx ecx, word ptr [r12 + 0x130]
00AAAC8D  66 85 C9                        test cx, cx
00AAAC90  74 1B                           je 0x140aaacad
00AAAC92  44 8B C1                        mov r8d, ecx
00AAAC95  8D 41 FF                        lea eax, [rcx - 1]
00AAAC98  41 85 C6                        test r14d, eax
00AAAC9B  74 10                           je 0x140aaacad
00AAAC9D  33 D2                           xor edx, edx
00AAAC9F  41 8B C6                        mov eax, r14d
00AAACA2  41 F7 F0                        div r8d
00AAACA5  85 D2                           test edx, edx
00AAACA7  0F 85 30 03 00 00               jne 0x140aaafdd
00AAACAD  4D 85 ED                        test r13, r13
00AAACB0  74 20                           je 0x140aaacd2
00AAACB2  83 7C 24 48 FF                  cmp dword ptr [rsp + 0x48], -1
00AAACB7  75 07                           jne 0x140aaacc0
00AAACB9  83 7C 24 4C FF                  cmp dword ptr [rsp + 0x4c], -1
00AAACBE  74 12                           je 0x140aaacd2
00AAACC0  66 85 C9                        test cx, cx
00AAACC3  74 0D                           je 0x140aaacd2
00AAACC5  8D 41 FF                        lea eax, [rcx - 1]
00AAACC8  85 44 24 48                     test dword ptr [rsp + 0x48], eax
00AAACCC  0F 85 0B 03 00 00               jne 0x140aaafdd
00AAACD2  45 85 F6                        test r14d, r14d
00AAACD5  74 29                           je 0x140aaad00
00AAACD7  8B D7                           mov edx, edi
00AAACD9  3B 94 24 F8 00 00 00            cmp edx, dword ptr [rsp + 0xf8]
00AAACE0  73 1E                           jae 0x140aaad00
00AAACE2  8B CA                           mov ecx, edx
00AAACE4  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00AAACEC  8B 0C C8                        mov ecx, dword ptr [rax + rcx*8]
00AAACEF  48 F7 C1 FF 0F 00 00            test rcx, 0xfff
00AAACF6  0F 85 E1 02 00 00               jne 0x140aaafdd
00AAACFC  FF C2                           inc edx
00AAACFE  EB D9                           jmp 0x140aaacd9
00AAAD00  8B 84 24 20 01 00 00            mov eax, dword ptr [rsp + 0x120]
00AAAD07  24 06                           and al, 6
00AAAD09  3C 04                           cmp al, 4
00AAAD0B  75 0A                           jne 0x140aaad17
00AAAD0D  83 4C 24 48 FF                  or dword ptr [rsp + 0x48], 0xffffffff
00AAAD12  83 4C 24 4C FF                  or dword ptr [rsp + 0x4c], 0xffffffff
00AAAD17  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00AAAD1F  48 85 C0                        test rax, rax
00AAAD22  74 41                           je 0x140aaad65
00AAAD24  4C 8B 05 55 BE 51 00            mov r8, qword ptr [rip + 0x51be55]
00AAAD2B  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00AAAD30  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AAAD35  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00AAAD3A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AAAD3F  BA 02 00 00 00                  mov edx, 2
00AAAD44  48 8B C8                        mov rcx, rax
00AAAD47  E8 64 E0 DB FF                  call 0x140868db0
00AAAD4C  8B D8                           mov ebx, eax
00AAAD4E  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AAAD53  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00AAAD58  85 C0                           test eax, eax
00AAAD5A  0F 88 82 02 00 00               js 0x140aaafe2
00AAAD60  E8 EB D5 79 FF                  call 0x140248350
00AAAD65  4D 85 ED                        test r13, r13
00AAAD68  75 0E                           jne 0x140aaad78
00AAAD6A  41 F7 47 50 80 02 00 00         test dword ptr [r15 + 0x50], 0x280
00AAAD72  0F 84 65 02 00 00               je 0x140aaafdd
00AAAD78  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AAAD7D  48 C1 E8 20                     shr rax, 0x20
00AAAD81  85 C0                           test eax, eax
00AAAD83  79 14                           jns 0x140aaad99
00AAAD85  83 F8 FF                        cmp eax, -1
00AAAD88  0F 85 4F 02 00 00               jne 0x140aaafdd
00AAAD8E  83 7C 24 48 FF                  cmp dword ptr [rsp + 0x48], -1
00AAAD93  0F 85 44 02 00 00               jne 0x140aaafdd
00AAAD99  48 39 BC 24 28 01 00 00         cmp qword ptr [rsp + 0x128], rdi
00AAADA1  75 08                           jne 0x140aaadab
00AAADA3  49 8B CF                        mov rcx, r15
00AAADA6  E8 45 28 7F FF                  call 0x14029d5f0
00AAADAB  44 8A 44 24 41                  mov r8b, byte ptr [rsp + 0x41]
00AAADB0  41 80 F0 01                     xor r8b, 1
00AAADB4  41 8A 54 24 4C                  mov dl, byte ptr [r12 + 0x4c]
00AAADB9  49 8B CC                        mov rcx, r12
00AAADBC  E8 5F C9 75 FF                  call 0x140207720
00AAADC1  48 8B F0                        mov rsi, rax
00AAADC4  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AAADC9  48 85 C0                        test rax, rax
00AAADCC  75 0A                           jne 0x140aaadd8
00AAADCE  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AAADD3  E9 0A 02 00 00                  jmp 0x140aaafe2
00AAADD8  4C 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], r15
00AAADDF  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00AAADE7  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
00AAADEE  48 89 BE A0 00 00 00            mov qword ptr [rsi + 0xa0], rdi
00AAADF5  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00AAADF9  88 46 40                        mov byte ptr [rsi + 0x40], al
00AAADFC  40 88 7E 41                     mov byte ptr [rsi + 0x41], dil
00AAAE00  40 88 7E 44                     mov byte ptr [rsi + 0x44], dil
00AAAE04  48 89 7E 68                     mov qword ptr [rsi + 0x68], rdi
00AAAE08  89 7E 10                        mov dword ptr [rsi + 0x10], edi
00AAAE0B  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00AAAE10  48 89 46 50                     mov qword ptr [rsi + 0x50], rax
00AAAE14  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
00AAAE1C  48 85 DB                        test rbx, rbx
00AAAE1F  74 28                           je 0x140aaae49
00AAAE21  BA 49 6F 52 49                  mov edx, 0x49526f49
00AAAE26  48 8B CB                        mov rcx, rbx
00AAAE29  E8 E2 58 76 FF                  call 0x140210710
00AAAE2E  0F BA 6E 10 15                  bts dword ptr [rsi + 0x10], 0x15
00AAAE33  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00AAAE3B  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
00AAAE3F  4C 8B AC 24 F0 00 00 00         mov r13, qword ptr [rsp + 0xf0]
00AAAE47  EB 20                           jmp 0x140aaae69
00AAAE49  4C 8B AC 24 F0 00 00 00         mov r13, qword ptr [rsp + 0xf0]
00AAAE51  4C 89 6E 48                     mov qword ptr [rsi + 0x48], r13
00AAAE55  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00AAAE5D  48 89 46 58                     mov qword ptr [rsi + 0x58], rax
00AAAE61  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00AAAE69  48 89 5E 60                     mov qword ptr [rsi + 0x60], rbx
00AAAE6D  48 8B 9E B8 00 00 00            mov rbx, qword ptr [rsi + 0xb8]
00AAAE74  C7 43 B8 04 00 00 00            mov dword ptr [rbx - 0x48], 4
00AAAE7B  4C 89 7B E8                     mov qword ptr [rbx - 0x18], r15
00AAAE7F  F6 84 24 38 01 00 00 01         test byte ptr [rsp + 0x138], 1
00AAAE87  0F 94 C1                        sete cl
00AAAE8A  41 F6 47 50 10                  test byte ptr [r15 + 0x50], 0x10
00AAAE8F  0F 94 C0                        sete al
00AAAE92  84 C8                           test al, cl
00AAAE94  75 04                           jne 0x140aaae9a
00AAAE96  C6 43 BA 04                     mov byte ptr [rbx - 0x46], 4
00AAAE9A  48 89 7E 18                     mov qword ptr [rsi + 0x18], rdi
00AAAE9E  48 89 7E 08                     mov qword ptr [rsi + 8], rdi
00AAAEA2  45 85 F6                        test r14d, r14d
00AAAEA5  0F 84 A2 00 00 00               je 0x140aaaf4d
00AAAEAB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AAAEB0  41 B1 01                        mov r9b, 1
00AAAEB3  45 33 C0                        xor r8d, r8d
00AAAEB6  41 8B D6                        mov edx, r14d
00AAAEB9  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00AAAEC1  48 8B 09                        mov rcx, qword ptr [rcx]
00AAAEC4  E8 27 3D 7F FF                  call 0x14029ebf0
00AAAEC9  4C 8B F0                        mov r14, rax
00AAAECC  48 85 C0                        test rax, rax
00AAAECF  75 0A                           jne 0x140aaaedb
00AAAED1  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00AAAED6  E8 75 BB 84 FF                  call 0x1402f6a50
00AAAEDB  44 0F B6 63 B8                  movzx r12d, byte ptr [rbx - 0x48]
00AAAEE0  45 33 C9                        xor r9d, r9d
00AAAEE3  44 8A 44 24 40                  mov r8b, byte ptr [rsp + 0x40]
00AAAEE8  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00AAAEF0  49 8B CE                        mov rcx, r14
00AAAEF3  E8 98 48 79 FF                  call 0x14023f790
00AAAEF8  8B 05 BE BC 51 00               mov eax, dword ptr [rip + 0x51bcbe]
00AAAEFE  A8 01                           test al, 1
00AAAF00  74 1F                           je 0x140aaaf21
00AAAF02  41 8B CC                        mov ecx, r12d
00AAAF05  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00AAAF0A  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00AAAF0F  48 8B 54 C8 70                  mov rdx, qword ptr [rax + rcx*8 + 0x70]
00AAAF14  4D 8B C4                        mov r8, r12
00AAAF17  49 8B CE                        mov rcx, r14
00AAAF1A  E8 49 B5 9A FF                  call 0x140456468
00AAAF1F  EB 05                           jmp 0x140aaaf26
00AAAF21  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00AAAF26  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00AAAF2E  48 8B 08                        mov rcx, qword ptr [rax]
00AAAF31  48 89 4E 70                     mov qword ptr [rsi + 0x70], rcx
00AAAF35  EB 16                           jmp 0x140aaaf4d
00AAAF37  8B D8                           mov ebx, eax
00AAAF39  33 FF                           xor edi, edi
00AAAF3B  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AAAF43  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00AAAF48  E9 95 00 00 00                  jmp 0x140aaafe2
00AAAF4D  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AAAF52  4D 85 F6                        test r14, r14
00AAAF55  74 0F                           je 0x140aaaf66
00AAAF57  33 D2                           xor edx, edx
00AAAF59  49 8B CE                        mov rcx, r14
00AAAF5C  E8 0F 79 0D 00                  call 0x140b82870
00AAAF61  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00AAAF66  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00AAAF6A  83 E0 08                        and eax, 8
00AAAF6D  F7 D8                           neg eax
00AAAF6F  1B C0                           sbb eax, eax
00AAAF71  F7 D8                           neg eax
00AAAF73  05 00 0A 00 00                  add eax, 0xa00
00AAAF78  09 46 10                        or dword ptr [rsi + 0x10], eax
00AAAF7B  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00AAAF82  89 43 C0                        mov dword ptr [rbx - 0x40], eax
00AAAF85  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00AAAF89  89 43 C8                        mov dword ptr [rbx - 0x38], eax
00AAAF8C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AAAF91  48 89 43 D0                     mov qword ptr [rbx - 0x30], rax
00AAAF95  49 8B 87 D0 00 00 00            mov rax, qword ptr [r15 + 0xd0]
00AAAF9C  48 85 C0                        test rax, rax
00AAAF9F  74 0D                           je 0x140aaafae
00AAAFA1  8B 00                           mov eax, dword ptr [rax]
00AAAFA3  A8 10                           test al, 0x10
00AAAFA5  74 07                           je 0x140aaafae
00AAAFA7  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
00AAAFAB  89 43 CC                        mov dword ptr [rbx - 0x34], eax
00AAAFAE  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
00AAAFB6  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AAAFBB  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00AAAFBF  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AAAFC3  41 B1 01                        mov r9b, 1
00AAAFC6  4D 8B C7                        mov r8, r15
00AAAFC9  48 8B D6                        mov rdx, rsi
00AAAFCC  49 8B CC                        mov rcx, r12
00AAAFCF  E8 6C 04 E4 FF                  call 0x1408eb440
00AAAFD4  8B D8                           mov ebx, eax
00AAAFD6  40 88 7C 24 42                  mov byte ptr [rsp + 0x42], dil
00AAAFDB  EB 05                           jmp 0x140aaafe2
00AAAFDD  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AAAFE2  40 38 7C 24 42                  cmp byte ptr [rsp + 0x42], dil
00AAAFE7  74 18                           je 0x140aab001
00AAAFE9  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00AAAFEE  45 33 C9                        xor r9d, r9d
00AAAFF1  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00AAAFF6  48 8B D6                        mov rdx, rsi
00AAAFF9  49 8B CF                        mov rcx, r15
00AAAFFC  E8 C7 35 E0 FF                  call 0x1408ae5c8
00AAB001  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AAB006  4D 85 F6                        test r14, r14
00AAB009  74 0A                           je 0x140aab015
00AAB00B  33 D2                           xor edx, edx
00AAB00D  49 8B CE                        mov rcx, r14
00AAB010  E8 5B 78 0D 00                  call 0x140b82870
00AAB015  8B C3                           mov eax, ebx
00AAB017  48 81 C4 90 00 00 00            add rsp, 0x90
00AAB01E  41 5F                           pop r15
00AAB020  41 5E                           pop r14
00AAB022  41 5D                           pop r13
00AAB024  41 5C                           pop r12
00AAB026  5F                              pop rdi
00AAB027  5E                              pop rsi
00AAB028  5B                              pop rbx
00AAB029  C3                              ret
00AAB02A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopWriteFileGather(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10, unsigned int a11, __int64 a12, __int64 a13, unsigned __int8 a14)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m86;
    unsigned __int8 v_stack_m87;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p58;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    v_rdi = 0;
    v_stack_m84 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    v_stack_m58 = 0;
    *(unsigned int *)(v_rsp - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 128) = 0;
    v_stack_m86 = 1;
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (2)) == 0) goto loc_00AAA9D6;
    v_rbx = 1;
    if (a14 < 0) {
        v_rbx = 0;
    }
    v_stack_m87 = (unsigned __int8)(v_rbx);
    result = IoGetRelatedDeviceObject(a1, a2, a3, a4);
    v_stack_m60 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) == 0) goto loc_00AAAFDD;
    if ((unsigned __int8)(v_rbx) != 0) goto loc_00AAAFDD;
    a1 = ((((unsigned int)((unsigned int)(a8))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) >> (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (a6 != ((unsigned int)(a1))) goto loc_00AAAFDD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (4)) != 0) goto loc_00AAAFDD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) > 54) goto loc_00AAAA4F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) < 54) goto loc_00AAAA58;
loc_00AAAA4F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) != 83) goto loc_00AAAFDD;
loc_00AAAA58:
    if ((unsigned __int8)(v_stack_m88) == 0) goto loc_00AAAB37;
    if (a12 != 0) goto loc_00AAAB37;
    if (a5 >= v_rbx) { a5 = v_rbx; }
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    a3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(a5, v_stack_p18, a3, v_stack_m88);
    if ((*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_00AAAAD2;
    if (((v_stack_p18) & (-2)) == 0) goto loc_00AAAAD2;
    v_stack_m84 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00AAAFE2;
loc_00AAAAD2:
    if (a9 == 0) goto loc_00AAAAFD;
    if (((3) & ((unsigned __int8)(a9))) != 0) {
        result = ExRaiseDatatypeMisalignment(a5, 3, a3, v_stack_m88);
    }
    result = (unsigned int)(v_stack_m84);
    if (a9 < ((unsigned int)(v_stack_m84))) { result = a9; }
    v_stack_m80 = *(unsigned __int64 *)(a9);
loc_00AAAAFD:
    result = *(unsigned __int64 *)(a9);
    if (a10 != 0) {
        result = (unsigned int)(v_stack_m84);
        if (a10 < ((unsigned int)(v_stack_m84))) { result = a10; }
        result = *(unsigned int *)(result);
        v_stack_m78 = (unsigned int)(result);
    }
    goto loc_00AAAB67;
loc_00AAAB37:
    if (a9 != 0) {
        result = *(unsigned __int64 *)(a9);
        v_stack_m80 = result;
    }
    result = a10;
    if (a10 != 0) {
        result = *(unsigned int *)(a10);
        v_stack_m78 = (unsigned int)(result);
    }
    if ((unsigned __int8)(v_stack_m88) == 0) goto loc_00AAAD00;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) >> (5));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (4));
    result = (unsigned int)((result) | (2));
    if (((v_stack_p58) & ((unsigned __int8)(result))) != 0) goto loc_00AAAB92;
    goto loc_00AAAFE2;
loc_00AAAB92:
    if ((unsigned int)(a6) * 8 == 0) goto loc_00AAAC0F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_00AAABE3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_00AAABDD;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) {
        result = 1;
    }
    if ((unsigned __int8)(result) == 0) {
        a2 = 7;
    }
    if (((a7) & (a2)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, a2, a3, v_stack_m88);
    }
    if (((unsigned int)(a6) * 8 + a7 * 1) > ((unsigned int)(0xC0000022ULL))) goto loc_00AAAC0D;
    result = a7;
    if (((unsigned int)(a6) * 8 + a7 * 1) < a7) {
        result = *(unsigned __int8 *)((unsigned int)(0xC0000022ULL));
    }
    v_r14 = (unsigned int)(a8);
    if ((unsigned int)((unsigned int)(a8)) != 0) {
        a3 = 0x41536F49ULL;
        a2 = (unsigned int)(a6) * 8;
        a1 = 291;
        result = ExAllocatePool2(a1, a2, a3, v_stack_m88);
        v_r14 = result;
        v_stack_m68 = result;
        a3 = (unsigned int)(a6) * 8;
        a2 = a7;
        a1 = result;
        result = memcpy(a1, a2, a3, v_stack_m88);
        v_stack_p38 = v_r14;
        v_r14 = a8;
        a4 = v_stack_m88;
    }
    goto loc_00AAAC73;
loc_00AAAC73:
    if ((unsigned __int8)(a4) == 0) goto loc_00AAAD00;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) == 0) goto loc_00AAACD2;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m60 + 304)) == 0) goto loc_00AAACAD;
    if ((((unsigned int)(v_r14)) & ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + 304) - 1))) == 0) goto loc_00AAACAD;
    a2 = 0;
    if (0 != 0) goto loc_00AAAFDD;
loc_00AAACAD:
    if (a9 == 0) goto loc_00AAACD2;
    if (v_stack_m80 != -1) goto loc_00AAACC0;
    if (v_stack_m7C == -1) goto loc_00AAACD2;
loc_00AAACC0:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m60 + 304)) == 0) goto loc_00AAACD2;
    if (((v_stack_m80) & ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + 304) - 1))) != 0) goto loc_00AAAFDD;
loc_00AAACD2:
    if ((unsigned int)(v_r14) == 0) goto loc_00AAAD00;
loc_00AAACD9:
    if (0 >= a6) goto loc_00AAAD00;
    if ((((unsigned int)(*(unsigned int *)(a7 + 0 * 8))) & (0xFFFULL)) != 0) goto loc_00AAAFDD;
    a2 = (unsigned int)((0) + 1);
    goto loc_00AAACD9;
loc_00AAAD00:
    result = (unsigned __int8)(((unsigned int)(a11)) & (6));
    if (((unsigned __int8)(result)) == 4) {
    }
    if (v_stack_p10 == 0) goto loc_00AAAD65;
    v_stack_m50 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = v_stack_m50;
    result = ObReferenceObjectByHandle(v_stack_p10, 2, *(unsigned __int64 *)(v_rip + 5357141), a4);
    v_stack_m58 = v_stack_m50;
    if (sign_flag) goto loc_00AAAFE2;
    result = KeResetEvent(v_stack_m50, 2, *(unsigned __int64 *)(v_rip + 5357141), a4);
loc_00AAAD65:
    if (a9 != 0) goto loc_00AAAD78;
    if (((*(unsigned int *)(a1 + 80)) & (640)) == 0) goto loc_00AAAFDD;
loc_00AAAD78:
    result = (v_stack_m80) >> (32);
    if (!sign_flag) goto loc_00AAAD99;
    if (((unsigned int)(result)) != -1) goto loc_00AAAFDD;
    if (v_stack_m80 != -1) goto loc_00AAAFDD;
loc_00AAAD99:
    if (a12 == 0) {
        a1 = a1;
        result = IopResetEvent(a1, 2, *(unsigned __int64 *)(v_rip + 5357141), a4);
    }
    a3 = (unsigned __int8)((v_stack_m87) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_m60, *(unsigned __int8 *)(v_stack_m60 + 76), a3, a4);
    v_stack_m70 = result;
    if (result != 0) goto loc_00AAADD8;
    goto loc_00AAAFE2;
loc_00AAADD8:
    *(unsigned __int64 *)(result + 192) = a1;
    *(unsigned __int64 *)(result + 152) = v_stack_m48;
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_m88);
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 80) = v_stack_m58;
    if (a12 == 0) goto loc_00AAAE49;
    result = ObfReferenceObjectWithTag(a12, (unsigned int)(0x49526F49ULL), a3, a4);
    *(unsigned __int64 *)(result + 72) = a13;
    goto loc_00AAAE69;
loc_00AAAE49:
    *(unsigned __int64 *)(result + 72) = a5;
    *(unsigned __int64 *)(result + 88) = v_stack_p18;
loc_00AAAE69:
    *(unsigned __int64 *)(result + 96) = v_stack_p20;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 72) = 4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = a1;
    a1 = (((a14) & (1)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(a1 + 80)) & (16)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) {
        *(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 70) = 4;
    }
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((unsigned int)(v_r14) == 0) goto loc_00AAAF4D;
    v_stack_mA8 = result;
    a3 = 0;
    result = IoAllocateMdl(*(unsigned __int64 *)(a7), (unsigned int)((unsigned int)(v_r14)), a3, 1);
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)(v_r14)), a3, 1);
    }
    a4 = 0;
    result = MmProbeAndLockSelectedPages(result, a7, v_stack_m88, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5356734)))) & (1)) == 0) goto loc_00AAAF21;
    result = MmUpdateMdlTracker(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m60 + 8) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result + 184) - 72))) * 8 + 112), v_stack_m60, a4);
    goto loc_00AAAF26;
loc_00AAAF21:
loc_00AAAF26:
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a7);
    goto loc_00AAAF4D;
loc_00AAAF4D:
    result = a7;
    if (v_stack_m68 != 0) {
        a2 = 0;
        a1 = v_stack_m68;
        result = ExFreePoolWithTag(a1, a2, v_stack_m60, a4);
        v_stack_m68 = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) & (8));
    result = (unsigned int)(-(result));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + (0xA00ULL));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(a8));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((unsigned int)(v_stack_m78));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 48) = v_stack_m80;
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_00AAAFAE;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208))))) & (16)) != 0) {
        result = *(unsigned int *)(a5 + 8);
        *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 52) = (unsigned int)(result);
    }
    v_stack_m98 = 1;
    v_stack_mA0 = 0;
    v_stack_mA8 = (unsigned __int8)(v_stack_m88);
    result = IopSynchronousServiceTail(v_stack_m60, result, a1, 1);
    v_stack_m86 = 0;
    goto loc_00AAAFE2;
loc_00AAAFDD:
loc_00AAAFE2:
    if (v_stack_m86 != 0) {
        v_stack_mA8 = 0;
        a4 = 0;
        a3 = v_stack_m58;
        a2 = result;
        a1 = a1;
        result = IopExceptionCleanupEx(a1, a2, a3, a4);
    }
    if (v_stack_m68 != 0) {
        a2 = 0;
        a1 = v_stack_m68;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (144);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t IopWriteFileGather(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, void *Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10, uint32_t Arg11, int64_t Arg12, int64_t Arg13, uint8_t Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m86;
    uint8_t v_stack_m87;
    uint8_t v_stack_m88;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint8_t v_stack_p58;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    local_rdi = 0;
    v_stack_m84 = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    v_stack_m58 = 0;
    *(uint32_t *)(local_rsp - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x80) = 0;
    v_stack_m86 = 1;
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m88 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (2)) == 0) goto loc_00AAA9D6;
    local_rbx = 1;
    if (Arg14 < 0) {
        local_rbx = 0;
    }
    v_stack_m87 = (uint8_t)(local_rbx);
    result = IoGetRelatedDeviceObject(Arg1, Arg2, Arg3, Arg4);
    v_stack_m60 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) == 0) goto loc_00AAAFDD;
    if ((uint8_t)(local_rbx) != 0) goto loc_00AAAFDD;
    Arg1 = ((((uint32_t)((uint32_t)(Arg8))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) >> (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (Arg6 != ((uint32_t)(Arg1))) goto loc_00AAAFDD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (4)) != 0) goto loc_00AAAFDD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) > 54) goto loc_00AAAA4F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) < 54) goto loc_00AAAA58;
loc_00AAAA4F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) != 83) goto loc_00AAAFDD;
loc_00AAAA58:
    if ((uint8_t)(v_stack_m88) == 0) goto loc_00AAAB37;
    if (Arg12 != 0) goto loc_00AAAB37;
    if (Arg5 >= local_rbx) { Arg5 = local_rbx; }
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    Arg3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(Arg5, v_stack_p18, Arg3, v_stack_m88);
    if ((*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_00AAAAD2;
    if (((v_stack_p18) & (-2)) == 0) goto loc_00AAAAD2;
    v_stack_m84 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00AAAFE2;
loc_00AAAAD2:
    if (Arg9 == 0) goto loc_00AAAAFD;
    if (((3) & ((uint8_t)(Arg9))) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg5, 3, Arg3, v_stack_m88);
    }
    result = (uint32_t)(v_stack_m84);
    if (Arg9 < ((uint32_t)(v_stack_m84))) { result = Arg9; }
    v_stack_m80 = *(uint64_t *)(Arg9);
loc_00AAAAFD:
    result = *(uint64_t *)(Arg9);
    if (Arg10 != 0) {
        result = (uint32_t)(v_stack_m84);
        if (Arg10 < ((uint32_t)(v_stack_m84))) { result = Arg10; }
        result = *(uint32_t *)(result);
        v_stack_m78 = (uint32_t)(result);
    }
    goto loc_00AAAB67;
loc_00AAAB37:
    if (Arg9 != 0) {
        result = *(uint64_t *)(Arg9);
        v_stack_m80 = result;
    }
    result = Arg10;
    if (Arg10 != 0) {
        result = *(uint32_t *)(Arg10);
        v_stack_m78 = (uint32_t)(result);
    }
    if ((uint8_t)(v_stack_m88) == 0) goto loc_00AAAD00;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) >> (5));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (4));
    result = (uint32_t)((result) | (2));
    if (((v_stack_p58) & ((uint8_t)(result))) != 0) goto loc_00AAAB92;
    goto loc_00AAAFE2;
loc_00AAAB92:
    if ((uint32_t)(Arg6) * 8 == 0) goto loc_00AAAC0F;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_00AAABE3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_00AAABDD;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) {
        result = 1;
    }
    if ((uint8_t)(result) == 0) {
        Arg2 = 7;
    }
    if (((Arg7) & (Arg2)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, Arg2, Arg3, v_stack_m88);
    }
    if (((uint32_t)(Arg6) * 8 + Arg7 * 1) > ((uint32_t)(0xC0000022ULL))) goto loc_00AAAC0D;
    result = Arg7;
    if (((uint32_t)(Arg6) * 8 + Arg7 * 1) < Arg7) {
        result = *(uint8_t *)((uint32_t)(0xC0000022ULL));
    }
    local_r14 = (uint32_t)(Arg8);
    if ((uint32_t)((uint32_t)(Arg8)) != 0) {
        Arg3 = 0x41536F49ULL;
        Arg2 = (uint32_t)(Arg6) * 8;
        Arg1 = 291;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, v_stack_m88);
        local_r14 = result;
        v_stack_m68 = result;
        Arg3 = (uint32_t)(Arg6) * 8;
        Arg2 = Arg7;
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m88);
        v_stack_p38 = local_r14;
        local_r14 = Arg8;
        Arg4 = v_stack_m88;
    }
    goto loc_00AAAC73;
loc_00AAAC73:
    if ((uint8_t)(Arg4) == 0) goto loc_00AAAD00;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) == 0) goto loc_00AAACD2;
    if ((uint16_t)(*(uint16_t *)(v_stack_m60 + 0x130)) == 0) goto loc_00AAACAD;
    if ((((uint32_t)(local_r14)) & ((uint32_t)(*(uint16_t *)(v_stack_m60 + 0x130) - 1))) == 0) goto loc_00AAACAD;
    Arg2 = 0;
    if (0 != 0) goto loc_00AAAFDD;
loc_00AAACAD:
    if (Arg9 == 0) goto loc_00AAACD2;
    if (v_stack_m80 != -1) goto loc_00AAACC0;
    if (v_stack_m7C == -1) goto loc_00AAACD2;
loc_00AAACC0:
    if ((uint16_t)(*(uint16_t *)(v_stack_m60 + 0x130)) == 0) goto loc_00AAACD2;
    if (((v_stack_m80) & ((uint32_t)(*(uint16_t *)(v_stack_m60 + 0x130) - 1))) != 0) goto loc_00AAAFDD;
loc_00AAACD2:
    if ((uint32_t)(local_r14) == 0) goto loc_00AAAD00;
loc_00AAACD9:
    if (0 >= Arg6) goto loc_00AAAD00;
    if ((((uint32_t)(*(uint32_t *)(arg7 + 0x0 * 8))) & (0xFFFULL)) != 0) goto loc_00AAAFDD;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00AAACD9;
loc_00AAAD00:
    result = (uint8_t)(((uint32_t)(Arg11)) & (6));
    if (((uint8_t)(result)) == 4) {
    }
    if (v_stack_p10 == 0) goto loc_00AAAD65;
    v_stack_m50 = 0;
    v_stack_mA0 = 0;
    v_stack_mA8 = v_stack_m50;
    result = ObReferenceObjectByHandle(v_stack_p10, 2, *(uint64_t *)(v_rip + 0x51BE55), Arg4);
    v_stack_m58 = v_stack_m50;
    if (sign_flag) goto loc_00AAAFE2;
    result = KeResetEvent(v_stack_m50, 2, *(uint64_t *)(v_rip + 0x51BE55), Arg4);
loc_00AAAD65:
    if (Arg9 != 0) goto loc_00AAAD78;
    if (((*(uint32_t *)(arg1 + 0x50)) & (640)) == 0) goto loc_00AAAFDD;
loc_00AAAD78:
    result = (v_stack_m80) >> (32);
    if (!sign_flag) goto loc_00AAAD99;
    if (((uint32_t)(result)) != -1) goto loc_00AAAFDD;
    if (v_stack_m80 != -1) goto loc_00AAAFDD;
loc_00AAAD99:
    if (Arg12 == 0) {
        Arg1 = Arg1;
        result = IopResetEvent(Arg1, 2, *(uint64_t *)(v_rip + 0x51BE55), Arg4);
    }
    Arg3 = (uint8_t)((v_stack_m87) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_m60, *(uint8_t *)(v_stack_m60 + 0x4C), Arg3, Arg4);
    v_stack_m70 = result;
    if (result != 0) goto loc_00AAADD8;
    goto loc_00AAAFE2;
loc_00AAADD8:
    *(void **)(result + 0xC0) = Arg1;
    *(uint64_t *)(result + 0x98) = v_stack_m48;
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_m88);
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x50) = v_stack_m58;
    if (Arg12 == 0) goto loc_00AAAE49;
    result = ObfReferenceObjectWithTag(Arg12, (uint32_t)(0x49526F49ULL), Arg3, Arg4);
    *(uint64_t *)(result + 0x48) = Arg13;
    goto loc_00AAAE69;
loc_00AAAE49:
    *(void **)(result + 0x48) = Arg5;
    *(uint64_t *)(result + 0x58) = v_stack_p18;
loc_00AAAE69:
    *(uint64_t *)(result + 0x60) = v_stack_p20;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 4;
    *(void **)(*(uint64_t *)(result + 0xB8) - 0x18) = Arg1;
    Arg1 = (((Arg14) & (1)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(arg1 + 0x50)) & (16)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) {
        *(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x46) = 4;
    }
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((uint32_t)(local_r14) == 0) goto loc_00AAAF4D;
    v_stack_mA8 = result;
    Arg3 = 0;
    result = IoAllocateMdl(*(uint64_t *)(arg7), (uint32_t)((uint32_t)(local_r14)), Arg3, 1);
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)(local_r14)), Arg3, 1);
    }
    Arg4 = 0;
    result = MmProbeAndLockSelectedPages(result, Arg7, v_stack_m88, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x51BCBE)))) & (1)) == 0) goto loc_00AAAF21;
    result = MmUpdateMdlTracker(result, *(uint64_t *)(*(uint64_t *)(v_stack_m60 + 0x8) + (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result + 0xB8) - 0x48))) * 8 + 0x70), v_stack_m60, Arg4);
    goto loc_00AAAF26;
loc_00AAAF21:
loc_00AAAF26:
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(arg7);
    goto loc_00AAAF4D;
loc_00AAAF4D:
    result = Arg7;
    if (v_stack_m68 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m68;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m60, Arg4);
        v_stack_m68 = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) & (8));
    result = (uint32_t)(-(result));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + (0xA00ULL));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(Arg8));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((uint32_t)(v_stack_m78));
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = v_stack_m80;
    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_00AAAFAE;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0))))) & (16)) != 0) {
        result = *(uint32_t *)(arg5 + 0x8);
        *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x34) = (uint32_t)(result);
    }
    v_stack_m98 = 1;
    v_stack_mA0 = 0;
    v_stack_mA8 = (uint8_t)(v_stack_m88);
    result = IopSynchronousServiceTail(v_stack_m60, result, Arg1, 1);
    v_stack_m86 = 0;
    goto loc_00AAAFE2;
loc_00AAAFDD:
loc_00AAAFE2:
    if (v_stack_m86 != 0) {
        v_stack_mA8 = 0;
        Arg4 = 0;
        Arg3 = v_stack_m58;
        Arg2 = result;
        Arg1 = Arg1;
        result = IopExceptionCleanupEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m68 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m68;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (144);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `8` | `R` |
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg5` | `+ 0x8` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0 + rcx*8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAA95C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
