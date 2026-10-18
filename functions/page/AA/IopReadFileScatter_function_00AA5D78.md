# IopReadFileScatter

- RVA: `0x00AA5D78`–`0x00AA6392` (길이 `1,562` bytes)
- VA: `0x0000000140AA5D78`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB868`
- 디코드: `386`개 명령, `1,562/1,562` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA5DF9` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x00AA5EB3` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (function, `0x0040EC90`)
- `0x00AA5EF3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AA5FE2` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AA6016` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA6031` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AA60D3` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x00AA60E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA616E` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AA6187` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x00AA61B8` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (function, `0x0029D5F0`)
- `0x00AA61D1` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x00AA6236` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00AA62BA` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x00AA62C9` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x00AA62E5` → [MmProbeAndLockSelectedPages](../../text/23/MmProbeAndLockSelectedPages_function_0023F790.md) (function, `0x0023F790`)
- `0x00AA6318` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA6382` → [IopSynchronousServiceTail](../8E/IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)

### Direct callers
- [IopIoRingDispatchReadScatter](../71/IopIoRingDispatchReadScatter_function_0071FB0C.md) at `0x0071FBD6`
- [NtReadFileScatter](../AD/NtReadFileScatter_function_00AD9680.md) at `0x00AD9737`

### Static image references
- `0x00AA6149` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **13**
  - `0x00AA5DF9` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x00AA5EB3` → [IopMarkApcRoutineIfAsynchronousIo32](../../text/40/IopMarkApcRoutineIfAsynchronousIo32_function_0040EC90.md) (`PAGE` → `.text`)
  - `0x00AA6016` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6031` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AA60E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA6187` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x00AA61B8` → [IopResetEvent](../../text/29/IopResetEvent_function_0029D5F0.md) (`PAGE` → `.text`)
  - `0x00AA61D1` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x00AA6236` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00AA62BA` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x00AA62C9` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x00AA62E5` → [MmProbeAndLockSelectedPages](../../text/23/MmProbeAndLockSelectedPages_function_0023F790.md) (`PAGE` → `.text`)
  - `0x00AA6318` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA5D78  48 8B C4                        mov rax, rsp
00AA5D7B  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AA5D7F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00AA5D83  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AA5D87  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AA5D8B  53                              push rbx
00AA5D8C  56                              push rsi
00AA5D8D  57                              push rdi
00AA5D8E  41 54                           push r12
00AA5D90  41 55                           push r13
00AA5D92  41 56                           push r14
00AA5D94  41 57                           push r15
00AA5D96  48 81 EC 90 00 00 00            sub rsp, 0x90
00AA5D9D  4C 8B F9                        mov r15, rcx
00AA5DA0  33 DB                           xor ebx, ebx
00AA5DA2  8B F3                           mov esi, ebx
00AA5DA4  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
00AA5DA8  48 89 58 98                     mov qword ptr [rax - 0x68], rbx
00AA5DAC  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
00AA5DB1  89 58 80                        mov dword ptr [rax - 0x80], ebx
00AA5DB4  48 89 58 88                     mov qword ptr [rax - 0x78], rbx
00AA5DB8  C6 44 24 42 01                  mov byte ptr [rsp + 0x42], 1
00AA5DBD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AA5DC6  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00AA5DCE  44 8A B0 32 02 00 00            mov r14b, byte ptr [rax + 0x232]
00AA5DD5  44 88 74 24 40                  mov byte ptr [rsp + 0x40], r14b
00AA5DDA  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
00AA5DDD  4C 8B AC 24 20 01 00 00         mov r13, qword ptr [rsp + 0x120]
00AA5DE5  A8 02                           test al, 2
00AA5DE7  74 08                           je 0x140aa5df1
00AA5DE9  4D 85 ED                        test r13, r13
00AA5DEC  40 B7 01                        mov dil, 1
00AA5DEF  74 03                           je 0x140aa5df4
00AA5DF1  40 8A FB                        mov dil, bl
00AA5DF4  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00AA5DF9  E8 22 53 7F FF                  call 0x14029b120
00AA5DFE  48 8B D0                        mov rdx, rax
00AA5E01  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AA5E06  41 8B 4F 50                     mov ecx, dword ptr [r15 + 0x50]
00AA5E0A  F6 C1 08                        test cl, 8
00AA5E0D  0F 84 A3 02 00 00               je 0x140aa60b6
00AA5E13  40 84 FF                        test dil, dil
00AA5E16  0F 85 9A 02 00 00               jne 0x140aa60b6
00AA5E1C  44 8B A4 24 08 01 00 00         mov r12d, dword ptr [rsp + 0x108]
00AA5E24  41 F7 C4 FF 0F 00 00            test r12d, 0xfff
00AA5E2B  8B CB                           mov ecx, ebx
00AA5E2D  0F 95 C1                        setne cl
00AA5E30  41 8B C4                        mov eax, r12d
00AA5E33  C1 E8 0C                        shr eax, 0xc
00AA5E36  03 C8                           add ecx, eax
00AA5E38  39 8C 24 F8 00 00 00            cmp dword ptr [rsp + 0xf8], ecx
00AA5E3F  0F 85 71 02 00 00               jne 0x140aa60b6
00AA5E45  8B 42 30                        mov eax, dword ptr [rdx + 0x30]
00AA5E48  A8 04                           test al, 4
00AA5E4A  0F 85 66 02 00 00               jne 0x140aa60b6
00AA5E50  8B 4A 48                        mov ecx, dword ptr [rdx + 0x48]
00AA5E53  83 F9 36                        cmp ecx, 0x36
00AA5E56  77 10                           ja 0x140aa5e68
00AA5E58  48 BA 48 03 10 00 01 00 40 00   movabs rdx, 0x40000100100348
00AA5E62  48 0F A3 CA                     bt rdx, rcx
00AA5E66  72 09                           jb 0x140aa5e71
00AA5E68  83 F9 53                        cmp ecx, 0x53
00AA5E6B  0F 85 45 02 00 00               jne 0x140aa60b6
00AA5E71  45 84 F6                        test r14b, r14b
00AA5E74  0F 84 C9 00 00 00               je 0x140aa5f43
00AA5E7A  4D 85 ED                        test r13, r13
00AA5E7D  0F 85 C0 00 00 00               jne 0x140aa5f43
00AA5E83  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00AA5E8B  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
00AA5E95  48 3B CF                        cmp rcx, rdi
00AA5E98  48 0F 43 CF                     cmovae rcx, rdi
00AA5E9C  8B 01                           mov eax, dword ptr [rcx]
00AA5E9E  89 01                           mov dword ptr [rcx], eax
00AA5EA0  45 33 C0                        xor r8d, r8d
00AA5EA3  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00AA5EAB  48 8D 8C 24 F0 00 00 00         lea rcx, [rsp + 0xf0]
00AA5EB3  E8 D8 8D 96 FF                  call 0x14040ec90
00AA5EB8  49 39 9F B0 00 00 00            cmp qword ptr [r15 + 0xb0], rbx
00AA5EBF  74 20                           je 0x140aa5ee1
00AA5EC1  48 F7 84 24 E0 00 00 00 FE FF FF FF  test qword ptr [rsp + 0xe0], -2
00AA5ECD  74 12                           je 0x140aa5ee1
00AA5ECF  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AA5ED4  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
00AA5ED8  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00AA5EDC  E9 DA 01 00 00                  jmp 0x140aa60bb
00AA5EE1  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
00AA5EE9  48 85 D2                        test rdx, rdx
00AA5EEC  74 20                           je 0x140aa5f0e
00AA5EEE  F6 C2 03                        test dl, 3
00AA5EF1  74 06                           je 0x140aa5ef9
00AA5EF3  E8 D8 40 DF FF                  call 0x140899fd0
00AA5EF8  CC                              int3
00AA5EF9  48 8B C7                        mov rax, rdi
00AA5EFC  48 3B D7                        cmp rdx, rdi
00AA5EFF  48 0F 42 C2                     cmovb rax, rdx
00AA5F03  90                              nop
00AA5F04  8A 00                           mov al, byte ptr [rax]
00AA5F06  48 8B 02                        mov rax, qword ptr [rdx]
00AA5F09  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AA5F0E  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
00AA5F16  48 85 C9                        test rcx, rcx
00AA5F19  74 11                           je 0x140aa5f2c
00AA5F1B  48 8B C7                        mov rax, rdi
00AA5F1E  48 3B CF                        cmp rcx, rdi
00AA5F21  48 0F 42 C1                     cmovb rax, rcx
00AA5F25  90                              nop
00AA5F26  8B 00                           mov eax, dword ptr [rax]
00AA5F28  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AA5F2C  EB 47                           jmp 0x140aa5f75
00AA5F2E  33 DB                           xor ebx, ebx
00AA5F30  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AA5F38  8B F3                           mov esi, ebx
00AA5F3A  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00AA5F3E  E9 78 01 00 00                  jmp 0x140aa60bb
00AA5F43  48 8B 94 24 10 01 00 00         mov rdx, qword ptr [rsp + 0x110]
00AA5F4B  48 85 D2                        test rdx, rdx
00AA5F4E  74 08                           je 0x140aa5f58
00AA5F50  48 8B 02                        mov rax, qword ptr [rdx]
00AA5F53  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AA5F58  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00AA5F60  48 BF 00 00 FF FF FF 7F 00 00   movabs rdi, 0x7fffffff0000
00AA5F6A  48 85 C0                        test rax, rax
00AA5F6D  74 06                           je 0x140aa5f75
00AA5F6F  8B 00                           mov eax, dword ptr [rax]
00AA5F71  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AA5F75  45 84 F6                        test r14b, r14b
00AA5F78  0F 84 B6 01 00 00               je 0x140aa6134
00AA5F7E  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00AA5F85  4C 8D 24 C5 00 00 00 00         lea r12, [rax*8]
00AA5F8D  4D 85 E4                        test r12, r12
00AA5F90  74 6D                           je 0x140aa5fff
00AA5F92  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AA5F9B  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00AA5FA2  48 39 98 10 03 00 00            cmp qword ptr [rax + 0x310], rbx
00AA5FA9  74 28                           je 0x140aa5fd3
00AA5FAB  0F B7 80 EC 06 00 00            movzx eax, word ptr [rax + 0x6ec]
00AA5FB2  B9 4C 01 00 00                  mov ecx, 0x14c
00AA5FB7  66 3B C1                        cmp ax, cx
00AA5FBA  74 0C                           je 0x140aa5fc8
00AA5FBC  B9 C4 01 00 00                  mov ecx, 0x1c4
00AA5FC1  66 3B C1                        cmp ax, cx
00AA5FC4  8A C3                           mov al, bl
00AA5FC6  75 02                           jne 0x140aa5fca
00AA5FC8  B0 01                           mov al, 1
00AA5FCA  84 C0                           test al, al
00AA5FCC  B8 03 00 00 00                  mov eax, 3
00AA5FD1  75 05                           jne 0x140aa5fd8
00AA5FD3  B8 07 00 00 00                  mov eax, 7
00AA5FD8  48 85 84 24 00 01 00 00         test qword ptr [rsp + 0x100], rax
00AA5FE0  74 05                           je 0x140aa5fe7
00AA5FE2  E8 E9 3F DF FF                  call 0x140899fd0
00AA5FE7  4C 8B B4 24 00 01 00 00         mov r14, qword ptr [rsp + 0x100]
00AA5FEF  4B 8D 04 34                     lea rax, [r12 + r14]
00AA5FF3  48 3B C7                        cmp rax, rdi
00AA5FF6  77 05                           ja 0x140aa5ffd
00AA5FF8  49 3B C6                        cmp rax, r14
00AA5FFB  73 02                           jae 0x140aa5fff
00AA5FFD  8A 07                           mov al, byte ptr [rdi]
00AA5FFF  39 9C 24 08 01 00 00            cmp dword ptr [rsp + 0x108], ebx
00AA6006  74 36                           je 0x140aa603e
00AA6008  41 B8 49 6F 53 41               mov r8d, 0x41536f49
00AA600E  49 8B D4                        mov rdx, r12
00AA6011  B9 23 01 00 00                  mov ecx, 0x123
00AA6016  E8 D5 C0 0D 00                  call 0x140b820f0
00AA601B  4C 8B F0                        mov r14, rax
00AA601E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AA6023  4D 8B C4                        mov r8, r12
00AA6026  48 8B 94 24 00 01 00 00         mov rdx, qword ptr [rsp + 0x100]
00AA602E  48 8B C8                        mov rcx, rax
00AA6031  E8 0A 08 C2 FF                  call 0x1406c6840
00AA6036  4C 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r14
00AA603E  44 8B A4 24 08 01 00 00         mov r12d, dword ptr [rsp + 0x108]
00AA6046  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00AA604B  EB 12                           jmp 0x140aa605f
00AA604D  33 DB                           xor ebx, ebx
00AA604F  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AA6057  8B F3                           mov esi, ebx
00AA6059  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
00AA605D  EB 5C                           jmp 0x140aa60bb
00AA605F  45 84 F6                        test r14b, r14b
00AA6062  0F 84 CC 00 00 00               je 0x140aa6134
00AA6068  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00AA606C  A8 08                           test al, 8
00AA606E  0F 84 8E 00 00 00               je 0x140aa6102
00AA6074  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AA6079  0F B7 89 30 01 00 00            movzx ecx, word ptr [rcx + 0x130]
00AA6080  66 85 C9                        test cx, cx
00AA6083  74 17                           je 0x140aa609c
00AA6085  44 8B C1                        mov r8d, ecx
00AA6088  8D 41 FF                        lea eax, [rcx - 1]
00AA608B  41 85 C4                        test r12d, eax
00AA608E  74 0C                           je 0x140aa609c
00AA6090  33 D2                           xor edx, edx
00AA6092  41 8B C4                        mov eax, r12d
00AA6095  41 F7 F0                        div r8d
00AA6098  85 D2                           test edx, edx
00AA609A  75 1A                           jne 0x140aa60b6
00AA609C  4C 8B B4 24 10 01 00 00         mov r14, qword ptr [rsp + 0x110]
00AA60A4  4D 85 F6                        test r14, r14
00AA60A7  74 61                           je 0x140aa610a
00AA60A9  66 85 C9                        test cx, cx
00AA60AC  74 5C                           je 0x140aa610a
00AA60AE  FF C9                           dec ecx
00AA60B0  85 4C 24 50                     test dword ptr [rsp + 0x50], ecx
00AA60B4  74 54                           je 0x140aa610a
00AA60B6  BF 0D 00 00 C0                  mov edi, 0xc000000d
00AA60BB  38 5C 24 42                     cmp byte ptr [rsp + 0x42], bl
00AA60BF  74 17                           je 0x140aa60d8
00AA60C1  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00AA60C5  45 33 C9                        xor r9d, r9d
00AA60C8  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00AA60CD  48 8B D6                        mov rdx, rsi
00AA60D0  49 8B CF                        mov rcx, r15
00AA60D3  E8 F0 84 E0 FF                  call 0x1408ae5c8
00AA60D8  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AA60DD  4D 85 F6                        test r14, r14
00AA60E0  74 0A                           je 0x140aa60ec
00AA60E2  33 D2                           xor edx, edx
00AA60E4  49 8B CE                        mov rcx, r14
00AA60E7  E8 84 C7 0D 00                  call 0x140b82870
00AA60EC  8B C7                           mov eax, edi
00AA60EE  48 81 C4 90 00 00 00            add rsp, 0x90
00AA60F5  41 5F                           pop r15
00AA60F7  41 5E                           pop r14
00AA60F9  41 5D                           pop r13
00AA60FB  41 5C                           pop r12
00AA60FD  5F                              pop rdi
00AA60FE  5E                              pop rsi
00AA60FF  5B                              pop rbx
00AA6100  C3                              ret
00AA6101  CC                              int3
00AA6102  4C 8B B4 24 10 01 00 00         mov r14, qword ptr [rsp + 0x110]
00AA610A  45 85 E4                        test r12d, r12d
00AA610D  74 2D                           je 0x140aa613c
00AA610F  8B D3                           mov edx, ebx
00AA6111  3B 94 24 F8 00 00 00            cmp edx, dword ptr [rsp + 0xf8]
00AA6118  73 22                           jae 0x140aa613c
00AA611A  8B CA                           mov ecx, edx
00AA611C  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00AA6124  8B 0C C8                        mov ecx, dword ptr [rax + rcx*8]
00AA6127  48 F7 C1 FF 0F 00 00            test rcx, 0xfff
00AA612E  75 86                           jne 0x140aa60b6
00AA6130  FF C2                           inc edx
00AA6132  EB DD                           jmp 0x140aa6111
00AA6134  4C 8B B4 24 10 01 00 00         mov r14, qword ptr [rsp + 0x110]
00AA613C  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00AA6144  48 85 C9                        test rcx, rcx
00AA6147  74 43                           je 0x140aa618c
00AA6149  4C 8B 05 30 0A 52 00            mov r8, qword ptr [rip + 0x520a30]
00AA6150  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00AA6155  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00AA615A  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00AA615F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AA6164  44 8A 4C 24 40                  mov r9b, byte ptr [rsp + 0x40]
00AA6169  BA 02 00 00 00                  mov edx, 2
00AA616E  E8 3D 2C DC FF                  call 0x140868db0
00AA6173  8B F8                           mov edi, eax
00AA6175  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AA617A  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
00AA617F  85 C0                           test eax, eax
00AA6181  0F 88 34 FF FF FF               js 0x140aa60bb
00AA6187  E8 C4 21 7A FF                  call 0x140248350
00AA618C  4D 85 F6                        test r14, r14
00AA618F  75 0E                           jne 0x140aa619f
00AA6191  41 F7 47 50 80 02 00 00         test dword ptr [r15 + 0x50], 0x280
00AA6199  0F 84 17 FF FF FF               je 0x140aa60b6
00AA619F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AA61A4  48 C1 E8 20                     shr rax, 0x20
00AA61A8  85 C0                           test eax, eax
00AA61AA  0F 88 06 FF FF FF               js 0x140aa60b6
00AA61B0  4D 85 ED                        test r13, r13
00AA61B3  75 08                           jne 0x140aa61bd
00AA61B5  49 8B CF                        mov rcx, r15
00AA61B8  E8 33 74 7F FF                  call 0x14029d5f0
00AA61BD  44 8A 44 24 41                  mov r8b, byte ptr [rsp + 0x41]
00AA61C2  41 80 F0 01                     xor r8b, 1
00AA61C6  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00AA61CB  8A 50 4C                        mov dl, byte ptr [rax + 0x4c]
00AA61CE  48 8B C8                        mov rcx, rax
00AA61D1  E8 4A 15 76 FF                  call 0x140207720
00AA61D6  48 8B F0                        mov rsi, rax
00AA61D9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AA61DE  48 85 C0                        test rax, rax
00AA61E1  75 0A                           jne 0x140aa61ed
00AA61E3  BF 9A 00 00 C0                  mov edi, 0xc000009a
00AA61E8  E9 CE FE FF FF                  jmp 0x140aa60bb
00AA61ED  4C 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], r15
00AA61F4  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00AA61FC  48 89 86 98 00 00 00            mov qword ptr [rsi + 0x98], rax
00AA6203  48 89 9E A0 00 00 00            mov qword ptr [rsi + 0xa0], rbx
00AA620A  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
00AA620F  44 88 76 40                     mov byte ptr [rsi + 0x40], r14b
00AA6213  88 5E 41                        mov byte ptr [rsi + 0x41], bl
00AA6216  88 5E 44                        mov byte ptr [rsi + 0x44], bl
00AA6219  48 89 5E 68                     mov qword ptr [rsi + 0x68], rbx
00AA621D  89 5E 10                        mov dword ptr [rsi + 0x10], ebx
00AA6220  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00AA6225  48 89 46 50                     mov qword ptr [rsi + 0x50], rax
00AA6229  4D 85 ED                        test r13, r13
00AA622C  74 30                           je 0x140aa625e
00AA622E  BA 49 6F 52 49                  mov edx, 0x49526f49
00AA6233  49 8B CD                        mov rcx, r13
00AA6236  E8 D5 A4 76 FF                  call 0x140210710
00AA623B  0F BA 6E 10 15                  bts dword ptr [rsi + 0x10], 0x15
00AA6240  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
00AA6248  48 89 46 48                     mov qword ptr [rsi + 0x48], rax
00AA624C  4C 8B AC 24 F0 00 00 00         mov r13, qword ptr [rsp + 0xf0]
00AA6254  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00AA625C  EB 20                           jmp 0x140aa627e
00AA625E  4C 8B AC 24 F0 00 00 00         mov r13, qword ptr [rsp + 0xf0]
00AA6266  4C 89 6E 48                     mov qword ptr [rsi + 0x48], r13
00AA626A  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00AA6272  48 89 46 58                     mov qword ptr [rsi + 0x58], rax
00AA6276  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00AA627E  48 89 46 60                     mov qword ptr [rsi + 0x60], rax
00AA6282  48 8B BE B8 00 00 00            mov rdi, qword ptr [rsi + 0xb8]
00AA6289  C7 47 B8 03 00 00 00            mov dword ptr [rdi - 0x48], 3
00AA6290  4C 89 7F E8                     mov qword ptr [rdi - 0x18], r15
00AA6294  48 89 5E 18                     mov qword ptr [rsi + 0x18], rbx
00AA6298  48 89 5E 08                     mov qword ptr [rsi + 8], rbx
00AA629C  45 85 E4                        test r12d, r12d
00AA629F  74 68                           je 0x140aa6309
00AA62A1  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AA62A6  41 B1 01                        mov r9b, 1
00AA62A9  45 33 C0                        xor r8d, r8d
00AA62AC  41 8B D4                        mov edx, r12d
00AA62AF  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00AA62B7  48 8B 09                        mov rcx, qword ptr [rcx]
00AA62BA  E8 31 89 7F FF                  call 0x14029ebf0
00AA62BF  48 85 C0                        test rax, rax
00AA62C2  75 0A                           jne 0x140aa62ce
00AA62C4  B9 9A 00 00 C0                  mov ecx, 0xc000009a
00AA62C9  E8 82 07 85 FF                  call 0x1402f6a50
00AA62CE  41 B9 01 00 00 00               mov r9d, 1
00AA62D4  45 8A C6                        mov r8b, r14b
00AA62D7  4C 8B B4 24 00 01 00 00         mov r14, qword ptr [rsp + 0x100]
00AA62DF  49 8B D6                        mov rdx, r14
00AA62E2  48 8B C8                        mov rcx, rax
00AA62E5  E8 A6 94 79 FF                  call 0x14023f790
00AA62EA  49 8B 06                        mov rax, qword ptr [r14]
00AA62ED  48 89 46 70                     mov qword ptr [rsi + 0x70], rax
00AA62F1  EB 16                           jmp 0x140aa6309
00AA62F3  8B F8                           mov edi, eax
00AA62F5  33 DB                           xor ebx, ebx
00AA62F7  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00AA62FF  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00AA6304  E9 B2 FD FF FF                  jmp 0x140aa60bb
00AA6309  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AA630E  4D 85 F6                        test r14, r14
00AA6311  74 0F                           je 0x140aa6322
00AA6313  33 D2                           xor edx, edx
00AA6315  49 8B CE                        mov rcx, r14
00AA6318  E8 53 C5 0D 00                  call 0x140b82870
00AA631D  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00AA6322  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
00AA6326  83 E0 08                        and eax, 8
00AA6329  F7 D8                           neg eax
00AA632B  1B C0                           sbb eax, eax
00AA632D  F7 D8                           neg eax
00AA632F  05 00 09 00 00                  add eax, 0x900
00AA6334  09 46 10                        or dword ptr [rsi + 0x10], eax
00AA6337  44 89 67 C0                     mov dword ptr [rdi - 0x40], r12d
00AA633B  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00AA633F  89 47 C8                        mov dword ptr [rdi - 0x38], eax
00AA6342  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AA6347  48 89 47 D0                     mov qword ptr [rdi - 0x30], rax
00AA634B  49 8B 87 D0 00 00 00            mov rax, qword ptr [r15 + 0xd0]
00AA6352  48 85 C0                        test rax, rax
00AA6355  74 0D                           je 0x140aa6364
00AA6357  8B 00                           mov eax, dword ptr [rax]
00AA6359  A8 10                           test al, 0x10
00AA635B  74 07                           je 0x140aa6364
00AA635D  41 8B 45 08                     mov eax, dword ptr [r13 + 8]
00AA6361  89 47 CC                        mov dword ptr [rdi - 0x34], eax
00AA6364  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
00AA6368  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
00AA636C  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00AA6370  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AA6374  41 B1 01                        mov r9b, 1
00AA6377  4D 8B C7                        mov r8, r15
00AA637A  48 8B D6                        mov rdx, rsi
00AA637D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AA6382  E8 B9 50 E4 FF                  call 0x1408eb440
00AA6387  8B F8                           mov edi, eax
00AA6389  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
00AA638D  E9 29 FD FF FF                  jmp 0x140aa60bb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopReadFileScatter(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m86;
    unsigned __int8 v_stack_m87;
    unsigned __int8 v_stack_m88;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int8 v_stack_p42;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    v_rbx = 0;
    v_stack_m84 = 0;
    *(unsigned __int64 *)(v_rsp - 104) = 0;
    v_stack_m58 = 0;
    *(unsigned int *)(v_rsp - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 120) = 0;
    v_stack_m86 = 1;
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (2)) == 0) goto loc_00AA5DF1;
    v_rdi = 1;
    if (a11 != 0) {
        v_rdi = 0;
    }
    v_stack_m87 = (unsigned __int8)(v_rdi);
    result = IoGetRelatedDeviceObject(a1, a2, a3, a4);
    v_stack_m60 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) == 0) goto loc_00AA60B6;
    if ((unsigned __int8)(v_rdi) != 0) goto loc_00AA60B6;
    a1 = ((((unsigned int)((unsigned int)(a8))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) >> (12));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    if (a6 != ((unsigned int)(a1))) goto loc_00AA60B6;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 48)))) & (4)) != 0) goto loc_00AA60B6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) > 54) goto loc_00AA5E68;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) < 54) goto loc_00AA5E71;
loc_00AA5E68:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 72)))) != 83) goto loc_00AA60B6;
loc_00AA5E71:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AA5F43;
    if (a11 != 0) goto loc_00AA5F43;
    if (a5 >= v_rdi) { a5 = v_rdi; }
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)(*(unsigned int *)(a5)));
    a3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(a5, v_stack_p18, a3, a4);
    if ((*(unsigned __int64 *)(a1 + 176)) == 0) goto loc_00AA5EE1;
    if (((v_stack_p18) & (-2)) == 0) goto loc_00AA5EE1;
    v_stack_m84 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00AA60BB;
loc_00AA5EE1:
    if (a9 == 0) goto loc_00AA5F0E;
    if ((((unsigned __int8)(a9)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a5, a9, a3, a4);
    }
    result = (unsigned int)(v_stack_m84);
    if (a9 < ((unsigned int)(v_stack_m84))) { result = a9; }
    v_stack_m78 = *(unsigned __int64 *)(a9);
loc_00AA5F0E:
    result = *(unsigned __int64 *)(a9);
    if (a10 != 0) {
        result = (unsigned int)(v_stack_m84);
        if (a10 < ((unsigned int)(v_stack_m84))) { result = a10; }
        result = *(unsigned int *)(result);
        v_stack_m80 = (unsigned int)(result);
    }
    goto loc_00AA5F75;
loc_00AA5F43:
    if (a9 != 0) {
        result = *(unsigned __int64 *)(a9);
        v_stack_m78 = result;
    }
    result = a10;
    if (a10 != 0) {
        result = *(unsigned int *)(a10);
        v_stack_m80 = (unsigned int)(result);
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AA6134;
    if ((unsigned int)(a6) * 8 == 0) goto loc_00AA5FFF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_00AA5FD3;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_00AA5FC8;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 452) {
        result = 1;
    }
    result = 3;
    if ((unsigned __int8)(result) == 0) {
        result = 7;
    }
    if (((a7) & (result)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, a9, a3, a4);
    }
    if (((unsigned int)(a6) * 8 + a7 * 1) > ((unsigned int)(v_stack_m84))) goto loc_00AA5FFD;
    result = (unsigned int)(a6) * 8 + a7 * 1;
    if (((unsigned int)(a6) * 8 + a7 * 1) < a7) {
        result = *(unsigned __int8 *)((unsigned int)(v_stack_m84));
    }
    v_r14 = a7;
    if (a8 != 0) {
        a3 = 0x41536F49ULL;
        a2 = (unsigned int)(a6) * 8;
        a1 = 291;
        result = ExAllocatePool2(a1, a2, a3, a4);
        v_r14 = result;
        v_stack_m68 = result;
        a3 = (unsigned int)(a6) * 8;
        a2 = a7;
        a1 = result;
        result = memcpy(a1, a2, a3, a4);
        v_stack_p38 = v_r14;
    }
    goto loc_00AA605F;
loc_00AA605F:
    if ((unsigned __int8)(v_stack_m88) == 0) goto loc_00AA6134;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 80)))) & (8)) == 0) goto loc_00AA6102;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m60 + 304)) == 0) goto loc_00AA609C;
    if ((((unsigned int)((unsigned int)(a8))) & ((unsigned int)(*(unsigned __int16 *)(v_stack_m60 + 304) - 1))) == 0) goto loc_00AA609C;
    a2 = 0;
    if (0 != 0) goto loc_00AA60B6;
loc_00AA609C:
    if (a9 == 0) goto loc_00AA610A;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m60 + 304)) == 0) goto loc_00AA610A;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m60 + 304)) - 1);
    if (((v_stack_m78) & ((unsigned int)(a1))) == 0) goto loc_00AA610A;
loc_00AA60B6:
loc_00AA60BB:
    result = (unsigned int)((unsigned int)((unsigned int)(a8)));
    if (v_stack_m86 != 0) {
        v_stack_mA8 = 0;
        a4 = 0;
        a3 = v_stack_m58;
        a2 = 0;
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
loc_00AA6102:
loc_00AA610A:
    if ((unsigned int)((unsigned int)(a8)) == 0) goto loc_00AA613C;
loc_00AA6111:
    if (0 >= a6) goto loc_00AA613C;
    if ((((unsigned int)(*(unsigned int *)(a7 + 0 * 8))) & (0xFFFULL)) != 0) goto loc_00AA60B6;
    a2 = (unsigned int)((0) + 1);
    goto loc_00AA6111;
loc_00AA6134:
loc_00AA613C:
    if (v_stack_pD8 == 0) goto loc_00AA618C;
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_pD8, 2, *(unsigned __int64 *)(v_rip + 5376560), v_stack_p40);
    v_stack_p70 = v_stack_p78;
    if (sign_flag) goto loc_00AA60BB;
    result = KeResetEvent(v_stack_p78, 2, *(unsigned __int64 *)(v_rip + 5376560), v_stack_p40);
loc_00AA618C:
    if (a9 != 0) goto loc_00AA619F;
    if (((*(unsigned int *)(a1 + 80)) & (640)) == 0) goto loc_00AA60B6;
loc_00AA619F:
    result = (v_stack_p50) >> (32);
    if (sign_flag) goto loc_00AA60B6;
    if (a11 == 0) {
        a1 = a1;
        result = IopResetEvent(a1, 2, *(unsigned __int64 *)(v_rip + 5376560), v_stack_p40);
    }
    a3 = (unsigned __int8)((v_stack_p41) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_p68, *(unsigned __int8 *)(v_stack_p68 + 76), a3, v_stack_p40);
    v_stack_p58 = result;
    if (result != 0) goto loc_00AA61ED;
    goto loc_00AA60BB;
loc_00AA61ED:
    *(unsigned __int64 *)(result + 192) = a1;
    *(unsigned __int64 *)(result + 152) = v_stack_p80;
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(v_stack_p40);
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 80) = v_stack_p70;
    if (a11 == 0) goto loc_00AA625E;
    result = ObfReferenceObjectWithTag(a11, (unsigned int)(0x49526F49ULL), a3, v_stack_p40);
    *(unsigned __int64 *)(result + 72) = a12;
    goto loc_00AA627E;
loc_00AA625E:
    *(unsigned __int64 *)(result + 72) = a5;
    *(unsigned __int64 *)(result + 88) = v_stack_pE0;
loc_00AA627E:
    *(unsigned __int64 *)(result + 96) = v_stack_pE8;
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 72) = 3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 24) = a1;
    *(unsigned __int64 *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
    if ((unsigned int)((unsigned int)(a8)) == 0) goto loc_00AA6309;
    v_stack_p20 = result;
    a3 = 0;
    result = IoAllocateMdl(*(unsigned __int64 *)(a7), (unsigned int)((unsigned int)((unsigned int)(a8))), a3, 1);
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)((unsigned int)(a8))), a3, 1);
    }
    result = MmProbeAndLockSelectedPages(result, a7, (unsigned __int8)(v_stack_p40), 1);
    *(unsigned __int64 *)(result + 112) = *(unsigned __int64 *)(a7);
    goto loc_00AA6309;
loc_00AA6309:
    result = *(unsigned __int64 *)(a7);
    if (v_stack_p60 != 0) {
        a2 = 0;
        a1 = v_stack_p60;
        result = ExFreePoolWithTag(a1, a2, (unsigned __int8)(v_stack_p40), 1);
        v_stack_p60 = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 80))) & (8));
    result = (unsigned int)(-(result));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + (0x900ULL));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 64) = (unsigned int)((unsigned int)(a8));
    *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 56) = (unsigned int)((unsigned int)(v_stack_p48));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 184) - 48) = v_stack_p50;
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_00AA6364;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 208))))) & (16)) != 0) {
        result = *(unsigned int *)(a5 + 8);
        *(unsigned int *)(*(unsigned __int64 *)(result + 184) - 52) = (unsigned int)(result);
    }
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = (unsigned __int8)(v_stack_p40);
    result = IopSynchronousServiceTail(v_stack_p68, result, a1, 1);
    v_stack_p42 = 0;
    goto loc_00AA60BB;
}
```

## 5. (Beta) C Style

```c
int64_t IopReadFileScatter(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, void *Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12)
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
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m86;
    uint8_t v_stack_m87;
    uint8_t v_stack_m88;
    uint8_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint8_t v_stack_p41;
    uint8_t v_stack_p42;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    local_rbx = 0;
    v_stack_m84 = 0;
    *(uint64_t *)(local_rsp - 0x68) = 0;
    v_stack_m58 = 0;
    *(uint32_t *)(local_rsp - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x78) = 0;
    v_stack_m86 = 1;
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m88 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (2)) == 0) goto loc_00AA5DF1;
    local_rdi = 1;
    if (Arg11 != 0) {
        local_rdi = 0;
    }
    v_stack_m87 = (uint8_t)(local_rdi);
    result = IoGetRelatedDeviceObject(Arg1, Arg2, Arg3, Arg4);
    v_stack_m60 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) == 0) goto loc_00AA60B6;
    if ((uint8_t)(local_rdi) != 0) goto loc_00AA60B6;
    Arg1 = ((((uint32_t)((uint32_t)(Arg8))) & (0xFFFULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) >> (12));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    if (Arg6 != ((uint32_t)(Arg1))) goto loc_00AA60B6;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x30)))) & (4)) != 0) goto loc_00AA60B6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) > 54) goto loc_00AA5E68;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) < 54) goto loc_00AA5E71;
loc_00AA5E68:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x48)))) != 83) goto loc_00AA60B6;
loc_00AA5E71:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AA5F43;
    if (Arg11 != 0) goto loc_00AA5F43;
    if (Arg5 >= local_rdi) { Arg5 = local_rdi; }
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)(*(uint32_t *)(arg5)));
    Arg3 = 0;
    result = IopMarkApcRoutineIfAsynchronousIo32(Arg5, v_stack_p18, Arg3, Arg4);
    if ((*(uint64_t *)(arg1 + 0xB0)) == 0) goto loc_00AA5EE1;
    if (((v_stack_p18) & (-2)) == 0) goto loc_00AA5EE1;
    v_stack_m84 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00AA60BB;
loc_00AA5EE1:
    if (Arg9 == 0) goto loc_00AA5F0E;
    if ((((uint8_t)(Arg9)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg5, Arg9, Arg3, Arg4);
    }
    result = (uint32_t)(v_stack_m84);
    if (Arg9 < ((uint32_t)(v_stack_m84))) { result = Arg9; }
    v_stack_m78 = *(uint64_t *)(Arg9);
loc_00AA5F0E:
    result = *(uint64_t *)(Arg9);
    if (Arg10 != 0) {
        result = (uint32_t)(v_stack_m84);
        if (Arg10 < ((uint32_t)(v_stack_m84))) { result = Arg10; }
        result = *(uint32_t *)(result);
        v_stack_m80 = (uint32_t)(result);
    }
    goto loc_00AA5F75;
loc_00AA5F43:
    if (Arg9 != 0) {
        result = *(uint64_t *)(Arg9);
        v_stack_m78 = result;
    }
    result = Arg10;
    if (Arg10 != 0) {
        result = *(uint32_t *)(Arg10);
        v_stack_m80 = (uint32_t)(result);
    }
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AA6134;
    if ((uint32_t)(Arg6) * 8 == 0) goto loc_00AA5FFF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_00AA5FD3;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_00AA5FC8;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 452) {
        result = 1;
    }
    result = 3;
    if ((uint8_t)(result) == 0) {
        result = 7;
    }
    if (((Arg7) & (result)) != 0) {
        result = ExRaiseDatatypeMisalignment(452, Arg9, Arg3, Arg4);
    }
    if (((uint32_t)(Arg6) * 8 + Arg7 * 1) > ((uint32_t)(v_stack_m84))) goto loc_00AA5FFD;
    result = (uint32_t)(Arg6) * 8 + Arg7 * 1;
    if (((uint32_t)(Arg6) * 8 + Arg7 * 1) < Arg7) {
        result = *(uint8_t *)((uint32_t)(v_stack_m84));
    }
    local_r14 = Arg7;
    if (Arg8 != 0) {
        Arg3 = 0x41536F49ULL;
        Arg2 = (uint32_t)(Arg6) * 8;
        Arg1 = 291;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, Arg4);
        local_r14 = result;
        v_stack_m68 = result;
        Arg3 = (uint32_t)(Arg6) * 8;
        Arg2 = Arg7;
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, Arg4);
        v_stack_p38 = local_r14;
    }
    goto loc_00AA605F;
loc_00AA605F:
    if ((uint8_t)(v_stack_m88) == 0) goto loc_00AA6134;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50)))) & (8)) == 0) goto loc_00AA6102;
    if ((uint16_t)(*(uint16_t *)(v_stack_m60 + 0x130)) == 0) goto loc_00AA609C;
    if ((((uint32_t)((uint32_t)(Arg8))) & ((uint32_t)(*(uint16_t *)(v_stack_m60 + 0x130) - 1))) == 0) goto loc_00AA609C;
    Arg2 = 0;
    if (0 != 0) goto loc_00AA60B6;
loc_00AA609C:
    if (Arg9 == 0) goto loc_00AA610A;
    if ((uint16_t)(*(uint16_t *)(v_stack_m60 + 0x130)) == 0) goto loc_00AA610A;
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m60 + 0x130)) - 1);
    if (((v_stack_m78) & ((uint32_t)(Arg1))) == 0) goto loc_00AA610A;
loc_00AA60B6:
loc_00AA60BB:
    result = (uint32_t)((uint32_t)((uint32_t)(Arg8)));
    if (v_stack_m86 != 0) {
        v_stack_mA8 = 0;
        Arg4 = 0;
        Arg3 = v_stack_m58;
        Arg2 = 0;
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
loc_00AA6102:
loc_00AA610A:
    if ((uint32_t)((uint32_t)(Arg8)) == 0) goto loc_00AA613C;
loc_00AA6111:
    if (0 >= Arg6) goto loc_00AA613C;
    if ((((uint32_t)(*(uint32_t *)(arg7 + 0x0 * 8))) & (0xFFFULL)) != 0) goto loc_00AA60B6;
    Arg2 = (uint32_t)((0) + 1);
    goto loc_00AA6111;
loc_00AA6134:
loc_00AA613C:
    if (v_stack_pD8 == 0) goto loc_00AA618C;
    v_stack_p78 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = v_stack_p78;
    result = ObReferenceObjectByHandle(v_stack_pD8, 2, *(uint64_t *)(v_rip + 0x520A30), v_stack_p40);
    v_stack_p70 = v_stack_p78;
    if (sign_flag) goto loc_00AA60BB;
    result = KeResetEvent(v_stack_p78, 2, *(uint64_t *)(v_rip + 0x520A30), v_stack_p40);
loc_00AA618C:
    if (Arg9 != 0) goto loc_00AA619F;
    if (((*(uint32_t *)(arg1 + 0x50)) & (640)) == 0) goto loc_00AA60B6;
loc_00AA619F:
    result = (v_stack_p50) >> (32);
    if (sign_flag) goto loc_00AA60B6;
    if (Arg11 == 0) {
        Arg1 = Arg1;
        result = IopResetEvent(Arg1, 2, *(uint64_t *)(v_rip + 0x520A30), v_stack_p40);
    }
    Arg3 = (uint8_t)((v_stack_p41) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_p68, *(uint8_t *)(v_stack_p68 + 0x4C), Arg3, v_stack_p40);
    v_stack_p58 = result;
    if (result != 0) goto loc_00AA61ED;
    goto loc_00AA60BB;
loc_00AA61ED:
    *(void **)(result + 0xC0) = Arg1;
    *(uint64_t *)(result + 0x98) = v_stack_p80;
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(v_stack_p40);
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x50) = v_stack_p70;
    if (Arg11 == 0) goto loc_00AA625E;
    result = ObfReferenceObjectWithTag(Arg11, (uint32_t)(0x49526F49ULL), Arg3, v_stack_p40);
    *(uint64_t *)(result + 0x48) = Arg12;
    goto loc_00AA627E;
loc_00AA625E:
    *(void **)(result + 0x48) = Arg5;
    *(uint64_t *)(result + 0x58) = v_stack_pE0;
loc_00AA627E:
    *(uint64_t *)(result + 0x60) = v_stack_pE8;
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x48) = 3;
    *(void **)(*(uint64_t *)(result + 0xB8) - 0x18) = Arg1;
    *(uint64_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = 0;
    if ((uint32_t)((uint32_t)(Arg8)) == 0) goto loc_00AA6309;
    v_stack_p20 = result;
    Arg3 = 0;
    result = IoAllocateMdl(*(uint64_t *)(arg7), (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg3, 1);
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg3, 1);
    }
    result = MmProbeAndLockSelectedPages(result, Arg7, (uint8_t)(v_stack_p40), 1);
    *(uint64_t *)(result + 0x70) = *(uint64_t *)(arg7);
    goto loc_00AA6309;
loc_00AA6309:
    result = *(uint64_t *)(arg7);
    if (v_stack_p60 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p60;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint8_t)(v_stack_p40), 1);
        v_stack_p60 = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) & (8));
    result = (uint32_t)(-(result));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + (0x900ULL));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x40) = (uint32_t)((uint32_t)(Arg8));
    *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x38) = (uint32_t)((uint32_t)(v_stack_p48));
    *(uint64_t *)(*(uint64_t *)(result + 0xB8) - 0x30) = v_stack_p50;
    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_00AA6364;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xD0))))) & (16)) != 0) {
        result = *(uint32_t *)(arg5 + 0x8);
        *(uint32_t *)(*(uint64_t *)(result + 0xB8) - 0x34) = (uint32_t)(result);
    }
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    v_stack_p20 = (uint8_t)(v_stack_p40);
    result = IopSynchronousServiceTail(v_stack_p68, result, Arg1, 1);
    v_stack_p42 = 0;
    goto loc_00AA60BB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |
| `Arg5` | `+ 0x8` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0 + rcx*8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA5D78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
